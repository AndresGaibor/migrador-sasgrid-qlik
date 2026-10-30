"""Genera el plan de construcción de un Job de Talend a partir de la representación intermedia.

Nada de lo que produce está verificado: componentes y propiedades son candidatos de
`rules/mappings/talend-components.json` hasta que el adaptador los contraste con talend-mcp.
"""

import re
from collections.abc import Callable
from pathlib import Path, PurePosixPath
from typing import Literal

from pydantic import BaseModel

from sas_grid_migrator.environment.catalog import EnvironmentCatalog, EnvironmentDataset
from sas_grid_migrator.intermediate_representation.models import (
    IROperation,
    LibraryRef,
    MacroIR,
    ProgramIR,
)
from sas_grid_migrator.migration_planner import context_rules
from sas_grid_migrator.migration_planner.expressions import (
    is_simple_arithmetic_translation,
    translate,
)
from sas_grid_migrator.migration_planner.job_structure import apply_structure
from sas_grid_migrator.migration_planner.joblets import attach_joblets, macro_call_joblets
from sas_grid_migrator.migration_planner.regions import fold_regions, place_region_jobs
from sas_grid_migrator.migration_planner.copy_back import fold_copy_back
from sas_grid_migrator.migration_planner.elt import fold_elt
from sas_grid_migrator.migration_planner.sql_compose import compose_items
from sas_grid_migrator.migration_planner.job_structure import (
    engine_hint_from_texts,
    installed_components,
    official_inventory_names,
)
from sas_grid_migrator.migration_planner.pipeline import build_flow
from sas_grid_migrator.migration_planner.plan_cleanup import collapse_undefined_macros, prune_unused_context
from sas_grid_migrator.migration_planner.plumbing import macro_parts, plumbing_macros, tag_macro_calls
from sas_grid_migrator.migration_planner.models import (
    ChildJob,
    Connection,
    NotMigrated,
    ContextVariable,
    Expression,
    GridRecommendation,
    JobPlan,
    LibraryNeeded,
    MacroEntrypoint,
    Orchestration,
    PlanStep,
    Property,
    SchemaColumn,
    ValidationCase,
)
from sas_grid_migrator.sas_parser.ast import Loc
from sas_grid_migrator.sas_parser.parser import split_args
from sas_grid_migrator.talend_adapter.catalog import load_catalog

_AGG = re.compile(
    r"^(count|sum|avg|mean|min|max)\s*\(\s*(?:distinct\s+)?(.*?)\s*\)$", re.IGNORECASE | re.DOTALL
)
_KEY = re.compile(r"(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)")
_READS = {"read", "read_file", "inline_data"}


_FMT_NAME = re.compile(r"^\s*value\s+\$?(\w+)", re.IGNORECASE)
_FMT_ROW = re.compile(
    r"^\s*('(?:[^']|'')*'|\"[^\"]*\"|[^=\s][^=]*?)\s*=\s*('(?:[^']|'')*'|\"[^\"]*\")\s*$"
)


#: Estadística de PROC MEANS/SUMMARY → operación de `tAggregateRow`. Lo que no esté aquí queda pendiente.
_MEANS_OPS = {
    "n": "count",
    "sum": "sum",
    "mean": "avg",
    "min": "min",
    "max": "max",
    "std": "stddev",
    "stddev": "stddev",
}
_MEANS_DEFAULT = ["n", "mean", "std", "min", "max"]


def _proc_aggregate(
    proc: str, details: dict[str, object]
) -> tuple[list[str], list[str], str | None]:
    """PROC MEANS/SUMMARY/FREQ → (`GROUPBYS`, `OPERATIONS`, motivo si no se puede).

    Solo se automatiza lo que el programa dice: las variables del `VAR`, los grupos de `CLASS`/`BY`, las estadísticas
    pedidas y los nombres de salida del `OUTPUT OUT=`. PROC TABULATE y PROC UNIVARIATE no salen como una tabla de una fila
    por grupo, así que quedan como pendiente.
    """
    statements = [str(s) for s in details.get("statements") or []]
    if proc in ("tabulate", "univariate"):
        return [], [], f"PROC {proc.upper()}: su salida no es una tabla de una fila por grupo; revisar a mano"
    group: list[str] = []
    for value in details.get("by") or []:
        name = str(value).split(".")[-1]
        if name and name not in group:
            group.append(name)
    for text in statements:
        m = re.match(r"\s*(class|by)\s+(.+?)\s*;?\s*$", text, re.IGNORECASE)
        if m:
            for value in m.group(2).split():
                name = value.split(".")[-1]
                if name and name not in group:
                    group.append(name)
    if proc == "freq":
        tables = [t for t in statements if re.match(r"\s*tables?\b", t, re.IGNORECASE)]
        if len(tables) != 1 or "/" in tables[0]:
            return [], [], "PROC FREQ sin una única tabla simple en TABLES: revisar cruces y opciones a mano"
        spec = re.sub(r"^\s*tables?\s+", "", tables[0].strip().rstrip(";"), flags=re.IGNORECASE)
        columns = [part.strip().split(".")[-1] for part in spec.split("*")]
        if not columns or any(not re.fullmatch(r"\w+", c) for c in columns):
            return [], [], "PROC FREQ con una tabla que no son columnas simples: revisar a mano"
        return columns, [f"COUNT = count({columns[0]})"], None
    variables: list[str] = []
    for text in statements:
        m = re.match(r"\s*var\s+(.+?)\s*;?\s*$", text, re.IGNORECASE)
        if m:
            variables += [value.split(".")[-1] for value in m.group(1).split()]
    if not variables:
        return [], [], (
            f"PROC {proc.upper()} sin VAR: agregaría todas las variables numéricas del dataset y su esquema no se conoce"
        )
    # `output out=x mean=media std=desv;` manda; si no hay OUTPUT, SAS escribe las estadísticas por defecto.
    requested: list[tuple[str, str]] = []
    for text in statements:
        if not re.match(r"\s*output\b", text, re.IGNORECASE):
            continue
        body = re.sub(r"\s*out\s*=\s*[^\s;]+(?:\s*\([^)]*\))?", "", text, flags=re.IGNORECASE)
        requested += [
            (stat.lower(), alias)
            for stat, alias in re.findall(r"([A-Za-z_]+)\s*=\s*(\w*)", body)
            if stat.lower() != "out"
        ]
    if requested:
        unsupported = sorted({stat for stat, _alias in requested if stat not in _MEANS_OPS})
        if unsupported:
            return [], [], (
                f"PROC {proc.upper()} pide estadísticas sin equivalente directo en tAggregateRow ({', '.join(unsupported)})"
            )
        if len(variables) > 1 and any(alias for _stat, alias in requested):
            return [], [], (
                f"PROC {proc.upper()}: el OUTPUT da un solo nombre de salida para {len(variables)} variables; "
                "SAS necesita AUTONAME y la lista de columnas de salida hay que fijarla a mano"
            )
    else:
        requested = [(stat, "") for stat in _MEANS_DEFAULT]
    operations = []
    for stat, alias in requested:
        for variable in variables:
            name = alias or f"{variable}_{stat.capitalize()}"
            operations.append(f"{name} = {_MEANS_OPS[stat]}({variable})")
    return group, operations, None


#: `IF cond THEN target = expr;` y su `ELSE target = expr;`: se pueden llevar a una expresión ternaria de tMap.
_COND_ASSIGN = re.compile(r"^\s*if\s+(.+?)\s+then\s+(\w+)\s*=\s*(.+?)\s*;?\s*$", re.IGNORECASE | re.DOTALL)
_ELSE_ASSIGN = re.compile(r"^\s*else\s+(\w+)\s*=\s*(.+?)\s*;?\s*$", re.IGNORECASE | re.DOTALL)

#: Clave de un formato que no es un valor suelto: rango, comparación u OTHER (necesita lógica, no una tabla).
_FORMAT_RANGE = re.compile(r"<-?|-|\b(?:low|high|other)\b|[<>&]", re.IGNORECASE)


def _format_needs_logic(key: str) -> bool:
    """Una clave vacía es el valor perdido y un rango exige lógica: ninguna de las dos es una fila de lookup."""
    return not key.strip() or bool(_FORMAT_RANGE.search(key))

_LIST_INPUT = re.compile(r"^\s*input\s+(.+?)\s*;?\s*$", re.IGNORECASE | re.DOTALL)
_DLM = re.compile(r"\b(?:dlm|delimiter)\s*=\s*'?(.)'?", re.IGNORECASE)


def _inline_data(
    details: dict[str, object],
) -> tuple[list[tuple[str, str]], list[list[str]], str | None]:
    """Esquema y filas de un bloque `datalines` de entrada por lista (WP2).

    Devuelve `(columnas, filas, motivo)`. Si el SAS usa entrada por columnas (`@1`, `#2`) o por grupos, o una fila no
    tiene el número de valores del `INPUT`, **no se inventa nada**: se devuelve el motivo para que quede como pendiente.
    """
    rows = [str(r) for r in details.get("rows") or []]
    statements = [str(s) for s in details.get("statements") or []]
    spec = next((s for s in statements if re.match(r"^\s*input\b", s, re.IGNORECASE)), None)
    if spec is None:
        return [], [], "El bloque `datalines` no trae una sentencia `INPUT`: revisar a mano"
    body = _LIST_INPUT.match(spec.split(";")[0]).group(1) if _LIST_INPUT.match(spec.split(";")[0]) else ""
    if not body or any(ch in body for ch in "@#("):
        return [], [], (
            "Datos incrustados con entrada por columnas, punteros o grupos: el mapeo a tFixedFlowInput necesita revisión manual"
        )
    tokens = body.split()
    columns: list[tuple[str, str]] = []
    index = 0
    while index < len(tokens):
        name = tokens[index]
        if not re.fullmatch(r"[A-Za-z_]\w*", name):
            return [], [], f"Nombre de columna no reconocido en INPUT ({name!r}): revisar a mano"
        index += 1
        char = False
        if index < len(tokens) and tokens[index].startswith("$"):
            char = True
            index += 1
        elif index < len(tokens) and re.fullmatch(r"[A-Za-z_$][\w$]*\d+\.\d*|\$?\d+\.\d*", tokens[index]):
            index += 1  # formato numérico (8., best12., comma10.2)
        columns.append((name, "String" if char else "Double"))
    if not columns:
        return [], [], "El `INPUT` no declara columnas utilizables: revisar a mano"
    infile = next((s for s in statements if re.match(r"^\s*infile\b", s, re.IGNORECASE)), "")
    dlm = _DLM.search(infile)
    delimiter = dlm.group(1) if dlm else None
    parsed: list[list[str]] = []
    for row in rows:
        if not row:
            continue
        values = [v for v in (row.split(delimiter) if delimiter else row.split())]
        values = [v.strip().strip("\"'") for v in values]
        if len(values) != len(columns):
            return [], [], (
                "Las filas de `datalines` no coinciden con las columnas del `INPUT` (¿texto con espacios?): revisar a mano"
            )
        parsed.append(values)
    if not parsed:
        return [], [], "El bloque `datalines` está vacío: no hay datos que cargar"
    return columns, parsed, None


def _format_rows(statements: list[str]) -> list[tuple[str, str, str]]:
    """Filas (formato, código, etiqueta) de los `value` de un PROC FORMAT; rangos y OTHER se copian tal cual."""
    rows: list[tuple[str, str, str]] = []
    for text in statements:
        lines = text.splitlines()
        head = _FMT_NAME.match(lines[0]) if lines else None
        if not head:
            continue
        for ln in lines[1:]:
            m = _FMT_ROW.match(ln)
            if m:
                rows.append((head.group(1), m.group(1).strip("'\""), m.group(2).strip("'\"")))
    return rows


def _sort_key(key: str) -> tuple[str, str]:
    """Devuelve la columna y dirección para claves SAS BY o SQL ORDER BY."""
    prefix = re.match(r"^(ascending|descending)\s+(.+)$", key, re.IGNORECASE)
    if prefix:
        direction = "DESC" if prefix.group(1).lower().startswith("desc") else "ASC"
        return prefix.group(2).strip(), direction
    suffix = re.match(r"^(.+?)\s+(asc|desc|ascending|descending)$", key, re.IGNORECASE)
    if suffix:
        direction = "DESC" if suffix.group(2).lower().startswith("desc") else "ASC"
        return suffix.group(1).strip(), direction
    return key.strip(), "ASC"


class OpRule(BaseModel):
    component: str
    alternatives: list[str] = []
    properties: list[str] = []
    required: list[str] = []
    tests: list[dict[str, str]] = []


class GridRule(BaseModel):
    component: str | None = None
    connection: str | None = None
    properties: list[str] = []
    required: list[str] = []
    status: Literal["supported", "partial", "unsupported"]
    instruction: str
    reason: str


class GridPattern(BaseModel):
    id: str
    status: Literal["supported", "partial", "unsupported"]
    description: str
    limitations: list[str]
    prerequisites: list[str]


class GridCatalog(BaseModel):
    version: str
    patterns: list[GridPattern]


class MappingRules(BaseModel):
    version: str
    # motor -> {"input", "output", "row"}; un lado ausente o vacío = el Studio no trae componente para él
    engines: dict[str, dict[str, str]]
    operations: dict[str, OpRule]
    grid: dict[str, GridRule] = {}
    editor_properties: dict[str, list[str]] = {}
    generic_components: list[str] = []
    engine_notes: dict[str, str] = {}


def load_mapping_rules(path: Path | None = None) -> MappingRules:
    p = (
        path
        or Path(__file__).resolve().parents[3] / "rules" / "mappings" / "talend-components.json"
    )
    rules = MappingRules.model_validate_json(p.read_text(encoding="utf-8"))
    validate_grid_mappings(rules, load_grid_catalog())
    return rules


def load_grid_catalog(path: Path | None = None) -> GridCatalog:
    p = path or Path(__file__).resolve().parents[3] / "rules" / "sas" / "grid_catalog.json"
    return GridCatalog.model_validate_json(p.read_text(encoding="utf-8"))


def validate_grid_mappings(rules: MappingRules, catalog: GridCatalog) -> None:
    patterns = {pattern.id: pattern for pattern in catalog.patterns}
    if rules.grid.keys() != patterns.keys():
        raise ValueError("Grid catalog and Talend mappings must contain the same pattern ids")
    talend = load_catalog()
    for pattern_id, rule in rules.grid.items():
        if rule.status != patterns[pattern_id].status:
            raise ValueError(f"Grid status differs between catalog and mapping: {pattern_id}")
        if rule.component and not talend.has(rule.component):
            raise ValueError(f"Grid mapping references unknown Talend component: {pattern_id}")
        run_job = talend.get("tRunJob") or {}
        if rule.connection and not any(
            connector["type"] == rule.connection for connector in run_job.get("connectors", [])
        ):
            raise ValueError(f"Grid mapping references unknown Talend connection: {pattern_id}")


def grid_recommendation(
    pattern_id: str,
    catalog: GridCatalog,
    rules: MappingRules,
    evidence: Loc,
    *,
    target_program: str | None = None,
    details: dict[str, object] | None = None,
    dependencies: list[str] | None = None,
) -> GridRecommendation:
    pattern = next((p for p in catalog.patterns if p.id == pattern_id), None)
    rule = rules.grid.get(pattern_id)
    if pattern is None or rule is None:
        raise ValueError(f"No Grid catalog mapping for pattern: {pattern_id}")
    item = load_catalog().get(rule.component) if rule.component else None
    return GridRecommendation(
        id=f"{evidence.file}:{evidence.line}:{pattern_id}",
        pattern_id=pattern_id,
        catalog_version=catalog.version,
        status=rule.status,
        instruction=rule.instruction,
        reason=rule.reason,
        component_candidate=rule.component,
        doc_url=item.get("doc_url") if item else None,
        required=rule.required,
        dependencies=dependencies or [],
        target_program=target_program,
        evidence=evidence,
        details=details or {},
    )


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def unique_job_names(
    plans: list[JobPlan],
    name_with_folders: Callable[[tuple[str, ...], int], str] | None = None,
) -> None:
    """Hace únicos los nombres de Job del proyecto: Talend no admite dos Jobs con el mismo nombre.

    Solo se renombran los que chocan, añadiendo carpetas del programa de dentro hacia fuera
    (`DB2/bulkload.sas` y `Hadoop/bulkload.sas` pasan a `job_db2_bulkload` y `job_hadoop_bulkload`).
    Si aun así dos rutas dan el mismo nombre, se añade un número.
    """
    name_with_folders = name_with_folders or _job_name_with_folders
    by_name: dict[str, list[JobPlan]] = {}
    for plan in plans:
        by_name.setdefault(plan.job_name, []).append(plan)
    taken = {name for name, group in by_name.items() if len(group) == 1}
    for group in by_name.values():
        if len(group) == 1:
            continue
        parts = [PurePosixPath(plan.program.replace("\\", "/")).parts for plan in group]
        depth = 1
        while depth < max(len(item) for item in parts):
            candidates = [name_with_folders(item, depth) for item in parts]
            if len(set(candidates)) == len(candidates) and not taken.intersection(candidates):
                break
            depth += 1
        candidates = [name_with_folders(item, depth) for item in parts]
        for plan, candidate in zip(group, candidates, strict=True):
            final, number = candidate, 2
            while final in taken:
                final, number = f"{candidate}_{number}", number + 1
            plan.job_name = final
            taken.add(final)


def _job_name_with_folders(parts: tuple[str, ...], depth: int) -> str:
    stem = PurePosixPath(parts[-1]).stem
    return "job_" + slug("_".join([*parts[-(depth + 1):-1], stem]))


def _macro_call_arguments(raw: str, params: list[str]) -> dict[str, str]:
    """Asocia argumentos SAS posicionales o nombrados con los parámetros del macro."""
    parameter_names = {name.casefold(): name for name in params}
    result: dict[str, str] = {}
    positional = 0
    for argument in split_args(raw):
        if not argument:
            continue
        key, separator, value = argument.partition("=")
        normalized_key = key.strip().casefold()
        if separator and normalized_key in parameter_names:
            result[parameter_names[normalized_key]] = value.strip().strip("\"'")
            continue
        while positional < len(params) and params[positional] in result:
            positional += 1
        if positional < len(params):
            result[params[positional]] = argument.strip().strip("\"'")
            positional += 1
    return result


#: Políticas de reportes de `docs/conventions.md` (WP3): registrar en el log, exportar a CSV o descartar.
REPORT_POLICIES = {"log": "tLogRow", "csv": "tFileOutputDelimited", "discard": "ninguno"}


class _Planner:
    def __init__(
        self,
        rules: MappingRules,
        libs: dict[str, LibraryRef],
        file: str,
        report_policy: str = "log",
        environment: EnvironmentCatalog | None = None,
        table_action: str = "drop_create",
    ):
        if report_policy not in REPORT_POLICIES:
            raise ValueError(
                f"Política de reportes desconocida: {report_policy!r} (admitidas: {', '.join(REPORT_POLICIES)})"
            )
        self.rules, self.libs, self.file = rules, libs, file
        self.report_policy = report_policy
        self.environment = environment
        self.table_action = table_action
        self.catalog = load_catalog()
        self.cases: list[ValidationCase] = []
        self.used_libs: set[str] = set()
        #: Motor de las cargas (transferencias) del programa: el que nombran sus librerías o su entorno.
        self.transfer_engine: str | None = None

    def tmap_meta(self) -> tuple[bool | None, str | None, list[str]]:
        """Catálogo del tMap (en catálogo, documentación y variantes) para los pasos fusionados."""
        cat = self.catalog.get("tMap")
        if not cat:
            return None, None, []
        return True, cat.get("doc_url"), self.catalog.variants_of("tMap")[:12]

    # ---- componentes ----
    def _engine_component(self, engine: str, side: str) -> tuple[str, list[str]]:
        """Componente del motor para un lado (input/output/row) y la pendiente si no hay ninguno."""
        component = self.rules.engines.get(engine, {}).get(side, "")
        if component:
            return component, []
        note = self.rules.engine_notes.get(engine) or (
            f"El Studio instalado no trae un componente de {side} para el motor {engine}. "
            "Elige el conector del motor o el genérico que trae la edición de Studio en uso."
        )
        return "", [note]

    def component(
        self, op: IROperation, rule: OpRule
    ) -> tuple[str, list[str], list[str], list[str]]:
        """(componente, alternativas, pendientes, supuestos)"""
        if op.details.get("passthrough") and op.type == "read":
            # R46: lectura pass-through (`from connection to <motor> (...)`): componente de entrada del motor.
            engine = str(op.details.get("engine") or "")
            component, pend = self._engine_component(engine, "input")
            return component, rule.alternatives, pend, [f"Lectura pass-through del motor {engine}"]
        if op.type == "sql_passthrough":
            # SQL pass-through (`execute (...) by <motor>`): se ejecuta en el motor con su componente Row.
            engine = str(op.details.get("engine") or "")
            if not engine:
                return (
                    "",
                    rule.alternatives,
                    ["SQL pass-through sin motor identificado: indicar el motor de la sentencia `by`."],
                    [],
                )
            component, pend = self._engine_component(engine, "row")
            if component and component not in installed_components() and component not in official_inventory_names():
                # Solo se propone un componente que el Studio instalado trae (snapshot) o que el inventario oficial documenta.
                pend = [f"{component} no está en el Studio instalado: elige el componente Row del motor"]
                component = ""
            return component, rule.alternatives, pend, []
        if op.details.get("transfer"):
            # Carga de una tabla WORK a la base del entorno: el componente de salida del motor que nombra el programa.
            table = op.details.get("tabla_destino", "")
            if self.transfer_engine and self.transfer_engine in self.rules.engines:
                component, pend = self._engine_component(self.transfer_engine, "output")
                return component, rule.alternatives, pend, [f"Carga de WORK.{table} al motor {self.transfer_engine}"]
            return (
                "por_determinar",
                rule.alternatives,
                ["Motor de destino de la carga no identificado en el programa: indicar la base de destino"],
                [],
            )
        if not rule.component.startswith("@engine."):
            return rule.component, rule.alternatives, [], []
        side = rule.component.split(".")[1]
        ds = (op.inputs if side == "input" else op.outputs) or op.inputs or op.outputs
        target = ds[0] if ds else ""
        # La librería es literal aunque la tabla sea dinámica (`td.&destino`); el nombre dinámico de la librería no.
        prefix = target.split(".")[0] if "." in target else ""
        lib = prefix if prefix and "&" not in prefix else None
        if lib == "work":
            return (
                "por_determinar",
                rule.alternatives,
                [],
                [
                    "Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal"
                ],
            )
        if lib:
            self.used_libs.add(lib)
            ref = self.libs.get(lib)
            eng = (ref.engine or "").lower() if ref else ""
            if eng in self.rules.engines:
                component, pend = self._engine_component(eng, side)
                return component, rule.alternatives, pend, [f"Librería {lib} usa el motor {eng}"]
            # El SAS puede no traer el LIBNAME (vive en un autoexec): lo dice el catálogo de entorno.
            catalog_library = self.environment.library(lib) if self.environment else None
            if catalog_library and catalog_library.engine.casefold() in self.rules.engines:
                engine = catalog_library.engine.casefold()
                component, pend = self._engine_component(engine, side)
                return (
                    component,
                    rule.alternatives,
                    pend,
                    [f"Librería {lib} según el catálogo de entorno: motor {catalog_library.engine}"],
                )
            where = f" en {ref.path}" if ref and ref.path else ""
            return (
                "por_determinar",
                rule.alternatives,
                [
                    f"Librería {lib} es de tipo BASE{where}: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo"
                ],
                [],
            )
        return (
            "por_determinar",
            rule.alternatives,
            ["Librería o sistema de origen no determinable (nombre dinámico)"],
            [],
        )

    # ---- valores por operación ----
    def fill(
        self, op: IROperation, comp: str
    ) -> tuple[
        dict[str, str | None], list[Expression], list[SchemaColumn], list[str], dict[str, object]
    ]:
        d, line = op.details, op.evidence.line
        props: dict[str, str | None] = {}
        exprs: list[Expression] = []
        cols: list[SchemaColumn] = []
        pend: list[str] = []
        component_tables: dict[str, object] = {}
        origin = f"SAS {op.evidence.file}:{line}"

        def col(name: str | None) -> None:
            if name and name != "*" and all(c.name != name for c in cols):
                cols.append(SchemaColumn(name=name, origin=origin))

        kinds: dict[str, str] = {}

        def expr(sas: str, ln: int | None = None, target: str | None = None) -> Expression:
            t = translate(sas)
            if target:
                kinds[target] = t.kind
            e = Expression(
                sas=sas,
                talend=t.talend,
                target=target,
                line=ln or line,
                requires_semantic_validation=not is_simple_arithmetic_translation(t.talend)
                or bool(t.warnings),
                warnings=t.warnings,
            )
            exprs.append(e)
            for c in t.columns:
                col(c)
            return e

        if op.type == "format_definition":
            rows = _format_rows(d.get("statements", []))
            if rows:
                cols.extend(
                    SchemaColumn(name=c, talend_type="String", origin=origin)
                    for c in ("FORMAT", "CODE", "LABEL")
                )
                props["USE_INTABLE"] = "true"
                props["INTABLE"] = "\n".join(" | ".join(r) for r in rows)
                risky = sorted({r[1] for r in rows if _format_needs_logic(r[1])})
                if risky:
                    pend.append(
                        "El formato tiene rangos u OTHER ("
                        + ", ".join(risky[:5])
                        + "): necesita lógica equivalente, no solo una tabla de valores"
                    )
        elif op.type == "inline_data":
            columns, rows, problem = _inline_data(d)
            if problem:
                pend.append(problem)
            else:
                for name, kind in columns:
                    cols.append(SchemaColumn(name=name, talend_type=kind, origin=origin))
                props["USE_SINGLEMODE"] = "true"
                props["NB_ROWS"] = str(len(rows))
                component_tables["VALUES"] = {
                    "columns": [name for name, _kind in columns],
                    "rows": [dict(zip((c for c, _k in columns), row, strict=True)) for row in rows],
                }
        elif op.type in ("read", "write", "append"):
            datasets = op.outputs if op.type == "append" else op.inputs or op.outputs
            ds = datasets[0] if datasets else ""
            props["TABLE"] = ds.split(".")[-1] if ds else None
            # El catálogo de entorno dice a qué tabla física y con qué columnas (WP5/WP6).
            entry = self.environment_dataset(ds) if ds else None
            if entry is not None:
                props["TABLE"] = entry.physical
                for column in entry.columns:
                    cols.append(
                        SchemaColumn(
                            name=column.name,
                            talend_type=column.talend_type,
                            nullable=column.nullable,
                            length=column.length,
                            precision=column.precision,
                            origin="catálogo de entorno",
                        )
                    )
            actions = {
                "drop_create": ("DROP_CREATE", "INSERT"),
                "truncate": ("CLEAR", "INSERT"),
                "append": ("NONE", "INSERT"),
            }
            if op.type == "write":  # DATA lib.x reemplaza el dataset: la acción es del proyecto, no del Job
                if self.table_action not in actions:
                    pend.append(
                        f"Acción al escribir desconocida ({self.table_action}): usar drop_create, truncate o append"
                    )
                else:
                    props["TABLE_ACTION"], props["DATA_ACTION"] = actions[self.table_action]
            elif op.type == "append":
                props["TABLE_ACTION"], props["DATA_ACTION"] = "NONE", "INSERT"
                if re.search(r"\bforce\b", str(d.get("options") or ""), re.IGNORECASE):
                    pend.append(
                        "PROC APPEND FORCE permite diferencias de esquema; validar columnas y tipos antes de migrar"
                    )
        elif op.type == "filter":
            t = translate(d.get("expression", ""))
            exprs.append(Expression(sas=t.sas, talend=t.talend, line=line, warnings=t.warnings))
            for c in t.columns:
                col(c)
            if t.simple:
                props["LOGICAL_OP"] = "OR" if t.logical == "||" else "AND"
                props["CONDITIONS"] = "; ".join(
                    f"{c['column']} {c['operator']} {c['value']}" for c in t.simple
                )
                props["USE_ADVANCED"] = "false"
            elif t.talend:
                props["USE_ADVANCED"] = "true"
                props["ADVANCED_COND"] = t.talend
            else:
                pend.append(
                    "Traducir la condición manualmente (no hay traducción automática segura)"
                )
        elif op.type == "join":
            on = d.get("on")
            keys = _KEY.findall(on or "")
            if d.get("kind") == "merge_by":
                props["Expression key"] = ", ".join(d.get("keys", []))
                props["Join model"] = {
                    "left": "Left Outer Join",
                    "inner": "Inner Join",
                    "right": "Left Outer Join (invertir lados)",
                    "full": "tMap no soporta full outer: usar tJoin + tUnite o dos tMap",
                }.get(d.get("join_type_guess") or "", None)
                for k in d.get("keys", []):
                    col(k)
                if not d.get("join_type_guess"):
                    pend.append(
                        "Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)"
                    )
            else:
                kind = (d.get("kind") or "").lower()
                props["Join model"] = (
                    "Inner Join"
                    if "inner" in kind or kind == "join"
                    else ("Left Outer Join" if "left" in kind else None)
                )
                if "right" in kind or "full" in kind:
                    props["Join model"] = (
                        "Left Outer Join con lados invertidos"
                        if "right" in kind
                        else "Full outer: tMap no lo soporta directamente"
                    )
                props["Expression key"] = (
                    ", ".join(f"{a}.{b} = {c}.{e}" for a, b, c, e in keys) or None
                )
                if on:
                    exprs.append(
                        Expression(
                            sas=on,
                            talend=None,
                            line=line,
                            warnings=["Mapear las claves del ON en la tabla de join de tMap"],
                        )
                    )
                for a, b, c, e in keys:
                    col(b)
                    col(e)
                if not keys:
                    pend.append(
                        "Condición de join no reducible a igualdad de columnas: revisar manualmente"
                    )
        elif op.type == "union":
            text = d.get("text", "")
            if re.search(r"\bunion\b(?!\s+all\b)", text, re.IGNORECASE):
                pend.append(
                    "Validar eliminación de filas duplicadas: UNION SAS/SQL sin ALL no equivale a concatenar con tUnite"
                )
        elif op.type == "aggregate":
            gb = d.get("group_by", [])
            props["GROUPBYS"] = ", ".join(g.split(".")[-1] for g in gb) or None
            ops_ = []
            for it in d.get("select", []):
                m = _AGG.match(it["expression"])
                if m:
                    ops_.append(
                        f"{it['alias'] or '?'} = {m.group(1).lower()}({m.group(2).split('.')[-1]})"
                    )
                    col(it["alias"])
                else:
                    col(it["alias"] or it["expression"])
            props["OPERATIONS"] = "; ".join(ops_) or None
            for g in gb:
                col(g.split(".")[-1])
            if d.get("proc"):
                proc_group, proc_ops, reason = _proc_aggregate(str(d["proc"]).lower(), d)
                if reason:
                    pend.append(reason)
                else:
                    props["GROUPBYS"] = ", ".join(proc_group) or None
                    props["OPERATIONS"] = "; ".join(proc_ops) or None
                    for name in proc_group:
                        col(name)
                    for operation in proc_ops:
                        col(operation.split(" = ")[0])
        elif op.type == "sort":
            keys = [_sort_key(key) for key in d.get("keys", [])]
            props["CRITERIA"] = ", ".join(
                f"{name.split('.')[-1]} {direction}" for name, direction in keys
            ) or None
            for k in keys:
                col(k[0].split(".")[-1])
        elif op.type == "dedupe":
            keys = [_sort_key(key)[0] for key in d.get("keys", [])]
            props["UNIQUE_KEY"] = ", ".join(keys) or None
            for k in keys:
                col(k.split(".")[-1])
        elif op.type == "project":
            for it in d.get("select", []):
                col(it["alias"])
                if not re.fullmatch(r"(?:\w+\.)?(\w+|\*)", it["expression"]):
                    expr(it["expression"])
            props["Output columns"] = ", ".join(
                it["alias"] or it["expression"] for it in d.get("select", [])
            )
        elif op.type == "select_columns":
            keep, drop = d.get("keep"), d.get("drop")
            props["SCHEMA"] = (
                ("keep: " + ", ".join(keep))
                if keep
                else (("drop: " + ", ".join(drop)) if drop else None)
            )
            for k in keep or []:
                col(k)
        elif op.type == "rename":
            props["Output columns"] = ", ".join(
                f"{a} → {b}" for a, b in d.get("mapping", {}).items()
            )
            for b in d.get("mapping", {}).values():
                col(b)
        elif op.type == "compute":
            for a in d.get("assignments", []):
                expr(a["expression"], a["line"], a["target"])
                col(a["target"])
            conditionals = d.get("conditionals", [])
            index = 0
            untranslated = 0
            while index < len(conditionals):
                cnd = conditionals[index]
                m = _COND_ASSIGN.match(str(cnd["text"]))
                if not m:
                    # `else` suelto, `then do;` o una cadena de condiciones: no hay ternaria segura.
                    exprs.append(
                        Expression(
                            sas=cnd["text"],
                            talend=None,
                            line=cnd["line"],
                            warnings=["Condicional IF/ELSE sin traducción automática"],
                        )
                    )
                    untranslated += 1
                    index += 1
                    continue
                condition, target, when_true = m.group(1), m.group(2), m.group(3)
                when_false, consumed = None, 1
                if index + 1 < len(conditionals):
                    e = _ELSE_ASSIGN.match(str(conditionals[index + 1]["text"]))
                    if e and e.group(1) == target:
                        when_false, consumed = e.group(2), 2
                t_cond, t_true = translate(condition), translate(when_true)
                t_false = translate(when_false) if when_false is not None else None
                # Sin ELSE, SAS deja el valor perdido: `null` es compatible con cualquier tipo del lado verdadero.
                kinds[target] = (
                    t_true.kind if t_false is None or t_false.kind == t_true.kind else "any"
                )
                if (
                    t_cond.kind != "bool"
                    or not t_cond.talend
                    or not t_true.talend
                    or (t_false is not None and not t_false.talend)
                ):
                    exprs.append(
                        Expression(
                            sas=" ".join(
                                str(conditionals[i]["text"]) for i in range(index, index + consumed)
                            ),
                            talend=None,
                            line=cnd["line"],
                            warnings=["Condicional IF/THEN sin traducción automática de la condición o los valores"],
                        )
                    )
                    untranslated += 1
                    index += consumed
                    continue
                else_java = t_false.talend if t_false is not None else "null"
                exprs.append(
                    Expression(
                        sas=" ".join(str(conditionals[i]["text"]) for i in range(index, index + consumed)),
                        talend=f"({t_cond.talend} ? {t_true.talend} : {else_java})",
                        target=target,
                        line=cnd["line"],
                        warnings=t_cond.warnings + t_true.warnings + (t_false.warnings if t_false else []),
                    )
                )
                for name in t_cond.columns + t_true.columns + (t_false.columns if t_false else []):
                    col(name)
                col(target)
                index += consumed
            if untranslated:
                pend.append("Condicional IF/ELSE sin traducción automática: revisar a mano")
            # El tipo de una columna calculada sale de la propia expresión (aritmética -> numérico, texto -> cadena).
            # Solo queda pendiente lo que el traductor no sabe tipar.
            talend_type = {"num": "Double", "str": "String", "bool": "Boolean", "date": "Date"}
            untyped = [
                target
                for target in (a["target"] for a in d.get("assignments", []))
                if target not in kinds
            ]
            for target, expression_kind in kinds.items():
                kind = talend_type.get(expression_kind)
                if not kind:
                    untyped.append(target)
                    continue
                for column in cols:
                    if column.name == target:
                        column.talend_type = kind
            if untyped:
                pend.append("Tipos de las columnas calculadas")
            props["Expressions"] = (
                f"{len(d.get('assignments', []))} asignaciones, {len(d.get('conditionals', []))} condicionales"
            )
        elif op.type == "read_file" or op.type == "write_file":
            file_config = d.get("offline_file_config")
            if isinstance(file_config, dict):
                props["FILENAME"] = file_config.get("filename")
                props["FIELDSEPARATOR"] = file_config.get("delimiter")
                if op.type == "read_file":
                    props["HEADER"] = file_config.get("header")
                else:
                    props["INCLUDEHEADER"] = file_config.get("create_header") or "false"
                    props["FILE_EXIST_EXCEPTION"] = "false"
                props["ENCODING"] = file_config.get("encoding")
                cols.extend(
                    SchemaColumn(
                        name=str(column.get("name", "")),
                        talend_type=column.get("talend_type"),
                        nullable=column.get("nullable"),
                        origin=str(column.get("origin", origin)),
                    )
                    for column in file_config.get("schema", [])
                )
                if not file_config.get("ready"):
                    pend.append(
                        "No se pudo comprobar offline la ruta, el esquema o el formato del archivo; completar antes de ejecutar"
                    )
            else:
                props["FILENAME"] = d.get("file")
        if d.get("offline_schema") and op.type not in {"read_file", "write_file"}:
            cols = [
                SchemaColumn(
                    name=str(column.get("name", "")),
                    talend_type=column.get("talend_type"),
                    nullable=column.get("nullable"),
                    origin=str(column.get("origin", origin)),
                )
                for column in d["offline_schema"]
            ]
        elif op.type == "set_variable":
            props["VARIABLES"] = f"KEY={d.get('macro_variable')}"
        elif op.type == "macro_call":
            props["PROCESS"] = d.get("name")
            props["CONTEXTPARAMS"] = d.get("args") or None
            if d.get("defined_in"):
                pend.append(
                    f"Crear/identificar el Job hijo para %{d['name']} (definida en {d['defined_in']})"
                )
        elif op.type == "include":
            props["PROCESS"] = d.get("path")
        elif op.type == "os_command":
            props["COMMAND"] = d.get("text")
        elif (op.type == "sql_passthrough" or d.get("passthrough")) and d.get("sql"):
            props["QUERY"] = d.get("sql")
        return props, exprs, cols, pend, component_tables

    def environment_dataset(self, reference: str) -> EnvironmentDataset | None:
        """El dataset del catálogo que corresponde a `lib.nombre`; `None` si no lo declara o es temporal."""
        if self.environment is None or not reference or "&" in reference or "%" in reference:
            return None
        lib, _, name = reference.partition(".")
        if not name:
            return None
        return self.environment.dataset(lib, name)

    def report(self, values: dict[str, str | None], pend: list[str]) -> tuple[str, list[str]]:
        """Qué se hace con un reporte (PROC PRINT/REPORT/TABULATE) segun la política del proyecto (WP3).

        `log` (valor por defecto): el reporte se registra con `tLogRow`, sin pendiente, porque el SAS ya trae lo que hay
        que mostrar. `csv` necesita una ruta de contexto, que sí queda como pendiente. `discard` lo descarta y lo deja
        anotado en el paso, para que el informe diga qué se perdió.
        """
        comp = REPORT_POLICIES[self.report_policy]
        if self.report_policy == "log":
            values["BASIC_MODE"] = "true"
        elif self.report_policy == "csv":
            pend.append(
                "Ruta del archivo de salida del reporte (política CSV): crear la variable de contexto path_<reporte>"
            )
        return comp, pend

    # ---- conversión de una operación ----
    def step(self, op: IROperation, order: int, prefix: str) -> PlanStep:
        rule = self.rules.operations.get(op.type) or self.rules.operations["unsupported"]
        comp, alts, pend, assume = self.component(op, rule)
        values, exprs, cols, pend2, component_tables = self.fill(op, comp)
        if op.type == "report":
            comp, pend2 = self.report(values, pend2)
        offline_configured = False
        filter_semantic_warning = False
        if op.type in ("read", "write", "append"):
            # Con el dataset en el catálogo, tabla y esquema están decididos: no queda pendiente de datos.
            datasets = op.outputs if op.type == "append" else op.inputs or op.outputs
            offline_configured = bool(datasets) and self.environment_dataset(datasets[0]) is not None
        if op.type == "report":
            # La política del proyecto decide el componente; no queda decision pendiente (salvo la ruta del CSV).
            offline_configured = self.report_policy in {"log", "discard"}
        elif op.type == "format_definition":
            # Un formato que solo traduce valores sueltos es una tabla de lookup: no queda decisión pendiente.
            offline_configured = bool(values.get("INTABLE")) and not pend2
        elif op.type in {"read_file", "write_file"}:
            file_config = op.details.get("offline_file_config")
            offline_configured = bool(isinstance(file_config, dict) and file_config.get("ready"))
        elif op.type == "filter" and op.details.get("offline_schema"):
            translated = translate(str(op.details.get("expression", "")))
            simple = translated.simple or []
            if (
                simple
                and all(
                    item.get("column") and item.get("operator") and item.get("value")
                    for item in simple
                )
                and all(column.name and column.talend_type for column in cols)
            ):
                rows = []
                for item in simple:
                    raw_value = str(item["value"])
                    if (
                        len(raw_value) >= 2
                        and raw_value[0] == raw_value[-1]
                        and raw_value[0] in "'\""
                    ):
                        raw_value = raw_value[1:-1].replace(raw_value[0] * 2, raw_value[0])
                    rows.append(
                        {
                            "INPUT_COLUMN": str(item["column"]),
                            "FUNCTION": "",
                            "OPERATOR": str(item["operator"]),
                            "RVALUE": raw_value,
                        }
                    )
                component_tables["CONDITIONS"] = {
                    "columns": ["INPUT_COLUMN", "FUNCTION", "OPERATOR", "RVALUE"],
                    "rows": rows,
                }
                values["LOGICAL_OP"] = "OR" if translated.logical == "||" else "AND"
                offline_configured = True
                filter_semantic_warning = bool(translated.warnings)
        origin = f"SAS {op.evidence.file}:{op.evidence.line}"
        props = [
            Property(
                name=n, value=values.get(n), origin=origin if values.get(n) else "regla mappings"
            )
            for n in rule.properties
        ]
        props += [
            Property(name=n, value=v, origin=origin)
            for n, v in values.items()
            if n not in rule.properties and v
        ]
        base = comp.split(" ")[0]
        cat = self.catalog.get(base)
        known = self.catalog.params(base)
        editor = set(self.rules.editor_properties.get(base, []))
        for p in props:
            if p.name in known:
                p.in_catalog = True
                p.label = known[p.name].get("label")
                p.options = [i["name"] for i in known[p.name].get("items", [])][:30]
            elif p.name in editor:
                p.label = "Editor del componente (no es un parámetro plano)"
            elif cat:
                p.in_catalog = False
        sid = f"{prefix}{op.id}"
        tests = []
        for t in rule.tests:
            vc = ValidationCase(
                id=f"vc_{sid}_{t['kind']}", kind=t["kind"], description=t["text"], applies_to=[sid]
            )
            self.cases.append(vc)
            tests.append(vc.id)
        pending = [*([] if offline_configured else rule.required), *pend, *pend2]
        sem = (
            op.type
            in ("filter", "join", "compute", "aggregate", "dedupe", "stateful", "union", "sort")
            or op.confidence != "high"
        )
        if op.type == "compute":
            assignments = op.details.get("assignments", [])
            conditionals = op.details.get("conditionals", [])
            safe_assignments = bool(assignments) and not conditionals and all(
                expression.target and is_simple_arithmetic_translation(expression.talend)
                and not expression.warnings
                for expression in exprs
            )
            sem = not safe_assignments or op.confidence != "high"
        elif op.type == "project":
            sem = any(expression.talend is None or expression.warnings for expression in exprs)
            sem = sem or op.confidence != "high"
        if offline_configured and op.type in {"read_file", "write_file", "filter"}:
            sem = filter_semantic_warning if op.type == "filter" else False
        return PlanStep(
            id=sid,
            order=order,
            subjob=f"{prefix}{op.step}",
            library=_dataset_library(op),
            action="manual_decision"
            if comp == ""
            or (
                comp in ("por_determinar", "ninguno")
                and op.type in ("stateful", "dynamic_code", "unsupported", "report")
            )
            else "add_component",
            operation_id=op.id,
            operation_type=op.type,
            component_candidate=comp,
            why=(pend[0] if pend else "Sin componente en el Studio instalado: elige el conector del motor.")
            if comp == ""
            else None,
            in_catalog=True
            if cat
            else (
                False
                if base.startswith("t") and base not in self.rules.generic_components
                else None
            ),
            doc_url=cat.get("doc_url") if cat else None,
            variants=self.catalog.variants_of(base)[:12] if cat else [],
            alternatives=alts,
            purpose=self.purpose(op),
            properties=props,
            schema_columns=cols,
            component_tables=component_tables,
            offline_configured=offline_configured,
            expressions=exprs,
            assumptions=[*op.notes, *assume],
            pending=pending,
            tests=tests,
            evidence=op.evidence,
            confidence=op.confidence,
            status="pendiente"
            if pending
            else ("descartado" if op.type == "report" and self.report_policy == "discard" else "propuesto"),
            note=f"Descartado por la política de reportes del proyecto ({self.report_policy})"
            if op.type == "report" and self.report_policy == "discard"
            else None,
            requires_semantic_validation=sem,
        )

    def purpose(self, op: IROperation) -> str:
        d, t = op.details, op.type
        if t == "read":
            return f"Leer {d.get('dataset')}"
        if t == "write":
            return f"Escribir {d.get('dataset') or ', '.join(op.outputs)}" + (
                " (reemplaza)" if d.get("mode") == "replace" else ""
            )
        if t == "filter":
            return f"Filtrar filas ({d.get('origin', 'condición')}): {d.get('expression', '')[:80]}"
        if t == "join":
            return f"Unir ({d.get('kind')}): {', '.join(op.inputs)}"
        if t == "sort":
            return "Ordenar por " + ", ".join(d.get("keys", []))
        if t == "aggregate":
            return "Agregar" + (" por " + ", ".join(d["group_by"]) if d.get("group_by") else "")
        return {
            "union": "Concatenar entradas",
            "dedupe": "Eliminar duplicados",
            "project": "Seleccionar/calcular columnas",
            "select_columns": "Conservar/descartar columnas",
            "rename": "Renombrar columnas",
            "compute": "Calcular columnas (asignaciones y condicionales)",
            "stateful": "Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)",
            "read_file": "Leer archivo externo",
            "write_file": "Escribir archivo externo",
            "inline_data": "Datos incrustados (datalines)",
            "append": "Añadir filas a una tabla existente",
            "format_definition": "Definir formatos como tabla de lookup",
            "set_variable": "Asignar variable desde datos",
            "macro_call": f"Invocar macro %{d.get('name')}",
            "include": "Incluir otro programa",
            "dynamic_code": "Código generado dinámicamente",
            "os_command": "Comando del sistema operativo",
            "report": "Salida de reporte",
            "maintenance": "Mantenimiento de datasets",
            "unsupported": "Lógica sin traducción definida",
        }.get(t, t)


def _variable(
    name: str, value: str | None, origin: str, line: int | None
) -> ContextVariable:
    """Variable de contexto con tipo Talend. Un secreto nunca conserva su valor en el plan."""
    info = context_rules.classify(name, value)
    return ContextVariable(
        name=name,
        sas_value=None if info.is_secret else value,
        suggested=f"context.{name}",
        origin=origin,
        talend_type=info.talend_type,
        is_secret=info.is_secret,
        needs_value=info.needs_value,
        sas_line=line,
    )


def _apply_environment_groups(
    variables: dict[str, ContextVariable], environment: dict[str, dict[str, str]]
) -> None:
    """Marca por ambiente (DEV/QA/PROD) las variables que el programa cambia según el ambiente elegido."""
    for name, variable in variables.items():
        if name in environment:
            variable.group_values = context_rules.env_group(environment[name])


def _dataset_library(op: IROperation) -> str | None:
    """Biblioteca SAS (LIB de LIB.TABLA) del primer dataset del paso, si lo tiene."""
    for dataset in [*op.inputs, *op.outputs]:
        if "." in dataset:
            return dataset.split(".", 1)[0].upper()
    return None


def _context_variables(
    ir: ProgramIR, steps: list[PlanStep], source_text: str | None = None
) -> list[ContextVariable]:
    variables: dict[str, ContextVariable] = {
        name: _variable(
            name, value, "%LET de primer nivel", ir.parameter_lines.get(name)
        )
        for name, value in ir.parameters.items()
    }
    environment = context_rules.environment_groups(source_text)
    for name in context_rules.environment_parameters(source_text):
        variables.setdefault(
            name, _variable(name, None, "parámetro de ambiente (D/C/P) comparado en el SAS", None)
        )
    for name in environment:
        variables.setdefault(
            name,
            _variable(name, None, "%LET dentro de %if &<selector> (valor por ambiente)", None),
        )
    for step in steps:
        for expression in step.expressions:
            for name in re.findall(r"context\.(\w+)", expression.talend or ""):
                variables.setdefault(
                    name,
                    _variable(
                        name, None, f"&{name} en {step.evidence.file}:{step.evidence.line}", step.evidence.line
                    ),
                )
        for prop in step.properties:
            for name in re.findall(r"&(\w+)", prop.value or ""):
                variables.setdefault(
                    name,
                    _variable(
                        name, None, f"&{name} en {step.evidence.file}:{step.evidence.line}", step.evidence.line
                    ),
                )
    _apply_environment_groups(variables, environment)
    return sorted(variables.values(), key=lambda variable: variable.name.lower())


def _needed_libraries(
    used_libraries: set[str], libraries: dict[str, LibraryRef], rules: MappingRules
) -> list[LibraryNeeded]:
    needed = []
    for name in sorted(used_libraries):
        ref = libraries.get(name)
        engine = (ref.engine or "").lower() if ref else ""
        connection = (
            rules.engines[engine]["input"].replace("Input", "Connection")
            if engine in rules.engines
            else "por_determinar (metadatos de archivo o base de datos)"
        )
        needed.append(
            LibraryNeeded(
                sas_name=ref.name if ref else name,
                engine=ref.engine if ref else None,
                path=ref.path if ref else None,
                suggested_connection=connection,
            )
        )
    return needed


def _composition_entries(notes: list[str]) -> list[NotMigrated]:
    """Sentencias SQL que no se compusieron (sql_compose.py), agrupadas por motivo: cada una sigue como paso propio."""
    by_reason: dict[str, int] = {}
    for note in notes:
        if note.startswith("No se compone") and ": " in note:
            reason = note.split(": ", 1)[1]
            by_reason[reason] = by_reason.get(reason, 0) + 1
    return [
        NotMigrated(
            category="composicion_sql",
            what=f"{count} sentencia(s) SQL no compuesta(s): {reason}",
            reason="La composición de sentencias SQL solo se hace si el resultado es seguro y se puede comprobar.",
            talend_equivalent="Cada sentencia se mantiene como su propio paso, como antes de la composición.",
        )
        for reason, count in by_reason.items()
    ]


def _datasets_of(operations) -> set[str]:
    return {d for op in operations for d in [*op.inputs, *op.outputs] if d}


def _inline_calls(ir: ProgramIR, entry_name: str | None) -> dict[str, MacroIR]:
    """Macros que se expanden en línea: llamadas una sola vez, desde el programa, y sin fontanería."""
    calls: dict[str, int] = {}
    for op in [*ir.operations, *(o for m in ir.macros for o in m.operations)]:
        if op.type == "macro_call":
            key = str(op.details.get("name", "")).casefold()
            calls[key] = calls.get(key, 0) + 1
    top_level = {
        str(op.details.get("name", "")).casefold(): op
        for op in ir.operations
        if op.type == "macro_call"
    }
    result: dict[str, MacroIR] = {}
    for macro in ir.macros:
        key = macro.name.casefold()
        if key == entry_name or calls.get(key) != 1 or key not in top_level:
            continue
        result[key] = macro
    return result


def _prune_cases(cases, retarget: dict[str, str | None], live: set[str]):
    """Casos de prueba de pasos que ya no existen: se retargetean al paso que los absorbe o se quitan."""
    out = []
    for case in cases:
        applies: list[str] = []
        for sid in case.applies_to:
            target = retarget.get(sid, sid)
            if target and target in live and target not in applies:
                applies.append(target)
        if applies:
            out.append(case.model_copy(update={"applies_to": applies}))
    return out


def plan_program(
    ir: ProgramIR,
    project_id: str,
    rules: MappingRules,
    libraries: dict[str, LibraryRef],
    unresolved: list[str] | None = None,
    orchestration: Orchestration | None = None,
    report_policy: str = "log",
    environment: EnvironmentCatalog | None = None,
    table_action: str = "drop_create",
    source_text: str | None = None,
    shared_datasets: set[str] | None = None,
) -> JobPlan:
    libs = {**libraries, **{x.name.lower(): x for x in ir.libraries}}
    pl = _Planner(rules, libs, ir.file, report_policy, environment, table_action)
    env_texts = [v for group in context_rules.environment_groups(source_text).values() for v in group.values() if v]
    pl.transfer_engine = (
        (engine_hint_from_texts([ref.engine or "" for ref in libs.values()] + env_texts + list(ir.parameters.values())) or "").lower()
        or None
    )
    plumbing = plumbing_macros(ir.macros)
    tag_macro_calls(ir, plumbing)
    source_macro = Path(ir.file.replace("\\", "/")).stem.casefold()
    entry_definition = next((macro for macro in ir.macros if macro.name.casefold() == source_macro), None)
    entry_calls = [
        operation
        for operation in ir.operations
        if operation.type == "macro_call"
        and str(operation.details.get("name", "")).casefold() == source_macro
    ]
    entry_macro = None
    expanded: list[tuple[IROperation, str]] = []
    if entry_definition and entry_calls:
        entry_call = entry_calls[0]
        entry_macro = MacroEntrypoint(
            name=entry_definition.name,
            params=entry_definition.params,
            arguments=_macro_call_arguments(
                str(entry_call.details.get("args", "")), entry_definition.params
            ),
        )
        calls_by_id = {operation.id for operation in entry_calls}
        for operation in ir.operations:
            if operation.type == "include":
                continue
            if operation.id in calls_by_id:
                suffix = f"{operation.id}:" if len(entry_calls) > 1 else ""
                prefix = f"m:{entry_definition.name}:{suffix}"
                expanded.extend((body_operation, prefix) for body_operation in entry_definition.operations)
            else:
                expanded.append((operation, ""))
    else:
        expanded = [(operation, "") for operation in ir.operations if operation.type != "include"]

    # Macros llamadas una sola vez se expanden en línea: sus operaciones entran en la corriente del Job.
    inlined = _inline_calls(ir, entry_macro.name.casefold() if entry_macro else None)
    inlined_names: set[str] = set()
    flow_items: list[tuple[IROperation, str]] = []
    for operation, prefix in expanded:
        key = str(operation.details.get("name", "")).casefold() if operation.type == "macro_call" else ""
        if key in inlined:
            inlined_names.add(key)
            flow_items.extend((body, f"m:{inlined[key].name}:") for body in inlined[key].operations)
        else:
            flow_items.append((operation, prefix))
    children_macros = [
        m
        for m in ir.macros
        if not (entry_macro and m.name.casefold() == entry_macro.name.casefold())
        and m.name.casefold() not in inlined_names
        and m.name.casefold() not in plumbing

    ]

    # Un dataset que usa otro ámbito (otra macro o el programa) no es intermedio para el ámbito actual.
    # La composición SQL va ANTES del ELT: el ELT necesita la consulta ya compuesta (sql_compose.py).
    top_datasets = _datasets_of(op for op, _ in flow_items)
    macro_datasets = {m.name: _datasets_of(m.operations) for m in children_macros}
    external = set(shared_datasets or set())
    flow_items, composed_notes = compose_items(
        flow_items, external | set().union(set(), *macro_datasets.values()), libs, rules.engines
    )
    flow_items, _ = fold_elt(flow_items, libs, rules.engines)
    flow_items, _ = fold_copy_back(flow_items)
    top_flow = build_flow(
        pl,
        flow_items,
        external | set().union(set(), *macro_datasets.values()),
    )
    steps = top_flow.steps
    not_migrated = list(top_flow.not_migrated)
    macros_by_name = {m.name.casefold(): m for m in ir.macros}
    for key, info in sorted(plumbing.items()):
        macro = macros_by_name.get(key)
        lines = [macro.loc.line, macro.loc.end_line] if macro else []
        parts = macro_parts(macro, plumbing, macros_by_name) if macro else [info]
        for part in parts:
            not_migrated.append(
                NotMigrated(
                    category=part.category,
                    lines=lines,
                    what=f"macro %{macro.name if macro else key} no se migra: {part.what}",
                    reason=part.reason,
                    talend_equivalent=part.talend,
                )
            )
    not_migrated.extend(_remote_session_entries(source_text))
    retarget: dict[str, str | None] = dict(top_flow.retarget)
    children: list[ChildJob] = []
    for m in children_macros:
        others = set().union(set(), top_datasets, *(ds for name, ds in macro_datasets.items() if name != m.name))
        child_items, child_notes = compose_items(
            [(op, f"m:{m.name}:") for op in m.operations], external | others, libs, rules.engines
        )
        composed_notes.extend(child_notes)
        child_items, _ = fold_elt(child_items, libs, rules.engines)
        child_items, _ = fold_copy_back(child_items)
        flow = build_flow(pl, child_items, external | others)
        children.append(ChildJob(name=m.name, params=m.params, steps=flow.steps))
        not_migrated.extend(flow.not_migrated)
        retarget.update(flow.retarget)
    not_migrated.extend(_composition_entries(composed_notes))
    all_steps = steps + [s for c in children for s in c.steps]
    live = {s.id for s in all_steps}
    cases = _prune_cases(pl.cases, retarget, live)

    context_by_name = {
        variable.name: variable for variable in _context_variables(ir, all_steps, source_text)
    }
    if entry_macro:
        for parameter in entry_macro.params:
            argument = entry_macro.arguments.get(parameter)
            literal = argument if argument and not re.search(r"[&%]", argument) else None
            context_by_name.setdefault(
                parameter,
                ContextVariable(
                    name=parameter,
                    sas_value=literal,
                    suggested=f"context.{parameter}",
                    origin=f"Parámetro de la macro principal %{entry_macro.name}; argumento SAS: {argument or 'sin asignar'}",
                ),
            )
            for referenced_name in re.findall(r"&([A-Za-z_]\w*)", argument or ""):
                context_by_name.setdefault(
                    referenced_name,
                    ContextVariable(
                        name=referenced_name,
                        suggested=f"context.{referenced_name}",
                        origin=f"Variable SAS referenciada por %{entry_macro.name}({parameter}=...)",
                    ),
                )
    _apply_environment_groups(context_by_name, context_rules.environment_groups(source_text))
    context_variables = sorted(context_by_name.values(), key=lambda variable: variable.name.lower())
    needed = _needed_libraries(pl.used_libs, libs, rules)
    pending = any(s.pending or s.confidence == "low" for s in all_steps)
    # Las credenciales se avisan sin copiar su valor: el aviso va a `unresolved`.
    warnings = [*(unresolved or []), *_credential_warnings(ir.file, source_text), *_literal_dsn_warnings(source_text)]
    plan = JobPlan(
        project_id=project_id,
        rules_version=rules.version,
        program=ir.file,
        sha256=ir.sha256,
        job_name="job_" + slug(Path(ir.file).stem),
        job_status="needs_review" if pending or warnings else "proposed",
        steps=steps,
        entry_macro=entry_macro,
        children=children,
        validation_cases=cases,
        context_variables=context_variables,
        libraries_needed=needed,
        orchestration=orchestration or Orchestration(),
        unresolved=warnings,
        not_migrated=not_migrated,
    )
    macro_call_joblets(plan, ir, lambda op: _call_values(op, ir))
    collapse_undefined_macros(plan, ir)
    fold_regions(plan)  # regiones largas repetidas: antes de repartir el Job, para que la partición vea el plegado
    apply_structure(plan, source_text)
    place_region_jobs(plan)
    attach_joblets(plan, ir)
    prune_unused_context(plan)  # después de la estructura: el motor se deduce del valor de ambiente
    return plan


_REMOTE_SESSION = re.compile(r"^\s*(signon|signoff|rsubmit|endrsubmit|waitfor)\b|\boptions\s+remote\s*=", re.IGNORECASE)


def _remote_session_entries(source_text: str | None) -> list[NotMigrated]:
    """R04: las sentencias de sesión remota no producen operaciones; se registran como fontanería."""
    if not source_text:
        return []
    lines = [i for i, text in enumerate(source_text.splitlines(), 1) if _REMOTE_SESSION.search(text)]
    if not lines:
        return []
    return [
        NotMigrated(
            category="sesion_remota",
            lines=lines,
            what="sesión remota de SAS (signon, rsubmit, waitfor, signoff)",
            reason="La sesión solo orquesta un proceso en otro servidor; no transforma filas.",
            talend_equivalent="Sin sesión: el Job lee y escribe en la ruta o el motor del contexto; el orden lo marca el Job.",
        )
    ]


_LITERAL_DSN = re.compile(r"\bdsn\s*=\s*([A-Za-z_]\w*)", re.IGNORECASE)


def _literal_dsn_warnings(source_text: str | None) -> list[str]:
    """R13: un DSN escrito a mano en un programa que ya elige su entorno (selector) salta el selector."""
    if not source_text or not context_rules.environment_groups(source_text):
        return []
    literals = sorted({m.group(1) for m in _LITERAL_DSN.finditer(source_text)})
    return [
        f"Aviso de alta severidad: DSN literal {name} en una conexión, aunque el programa elige el entorno con un selector. "
        "Una conexión así puede escribir en producción desde otro entorno: parametrizar el DSN con el contexto del entorno."
        for name in literals
    ]


def _call_values(op: IROperation, ir: ProgramIR) -> dict[str, str]:
    """Argumentos de una llamada a macro, por nombre del parámetro de la definición."""
    name = str(op.details.get("name", "")).casefold()
    macro = next((m for m in ir.macros if m.name.casefold() == name), None)
    return _macro_call_arguments(str(op.details.get("args", "")), macro.params if macro else [])


def _credential_warnings(file: str, source_text: str | None) -> list[str]:
    return [
        f"Credencial en claro o cifrada en {file}:{hit.line} ({'proc pwencode' if hit.kind == 'pwencode' else 'pass= literal'}): "
        "guárdala en una variable de contexto de tipo id_Password; el valor no se copia al plan."
        for hit in context_rules.credential_hits(source_text)
    ]
