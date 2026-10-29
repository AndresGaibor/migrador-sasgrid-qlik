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
from sas_grid_migrator.intermediate_representation.models import IROperation, LibraryRef, ProgramIR
from sas_grid_migrator.migration_planner.expressions import (
    is_simple_arithmetic_translation,
    translate,
)
from sas_grid_migrator.migration_planner.models import (
    ChildJob,
    Connection,
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
    engines: dict[str, dict[str, str]]
    operations: dict[str, OpRule]
    grid: dict[str, GridRule] = {}
    editor_properties: dict[str, list[str]] = {}
    generic_components: list[str] = []


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

    # ---- componentes ----
    def component(
        self, op: IROperation, rule: OpRule
    ) -> tuple[str, list[str], list[str], list[str]]:
        """(componente, alternativas, pendientes, supuestos)"""
        if not rule.component.startswith("@engine."):
            return rule.component, rule.alternatives, [], []
        side = rule.component.split(".")[1]
        ds = (op.inputs if side == "input" else op.outputs) or op.inputs or op.outputs
        target = ds[0] if ds else ""
        lib = target.split(".")[0] if "." in target and "&" not in target else None
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
                return (
                    self.rules.engines[eng][side],
                    rule.alternatives,
                    [],
                    [f"Librería {lib} usa el motor {eng}"],
                )
            # El SAS puede no traer el LIBNAME (vive en un autoexec): lo dice el catálogo de entorno.
            catalog_library = self.environment.library(lib) if self.environment else None
            if catalog_library and catalog_library.engine.casefold() in self.rules.engines:
                return (
                    self.rules.engines[catalog_library.engine.casefold()][side],
                    rule.alternatives,
                    [],
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
            action="manual_decision"
            if comp in ("por_determinar", "ninguno")
            and op.type in ("stateful", "dynamic_code", "unsupported", "report")
            else "add_component",
            operation_id=op.id,
            operation_type=op.type,
            component_candidate=comp,
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


def _connect(steps: list[PlanStep], prev_subjob_last: str | None) -> None:
    """Conexiones Main/Lookup dentro de cada subjob y OnSubjobOk entre subjobs consecutivos."""
    by_subjob: dict[str, list[PlanStep]] = {}
    for s in steps:
        by_subjob.setdefault(s.subjob, []).append(s)
    last = prev_subjob_last
    for group in by_subjob.values():
        reads: list[PlanStep] = []
        prev: PlanStep | None = None
        first_join_done = False
        for s in group:
            if s.operation_type in _READS:
                reads.append(s)
                prev = prev or s
                continue
            if s.operation_type == "join" and not first_join_done and reads:
                s.connections = [Connection(type="Main", from_step=reads[0].id)] + [
                    Connection(type="Lookup", from_step=r.id) for r in reads[1:]
                ]
                first_join_done = True
            elif s.operation_type == "union" and reads:
                s.connections = [Connection(type="Main", from_step=r.id) for r in reads]
            elif prev is not None:
                s.connections = [Connection(type="Main", from_step=prev.id)]
            prev = s
        if reads and not reads[0].connections and last:
            reads[0].connections = [Connection(type="OnSubjobOk", from_step=last)]
        elif not reads and group and last:
            group[0].connections = [
                *group[0].connections,
                Connection(type="OnSubjobOk", from_step=last),
            ]
        last = group[-1].id


def _context_variables(ir: ProgramIR, steps: list[PlanStep]) -> list[ContextVariable]:
    variables = {
        name: ContextVariable(
            name=name, sas_value=value, suggested=f"context.{name}", origin="%LET de primer nivel"
        )
        for name, value in ir.parameters.items()
    }
    for step in steps:
        for expression in step.expressions:
            for name in re.findall(r"context\.(\w+)", expression.talend or ""):
                variables.setdefault(
                    name,
                    ContextVariable(
                        name=name,
                        suggested=f"context.{name}",
                        origin=f"&{name} en {step.evidence.file}:{step.evidence.line}",
                    ),
                )
        for prop in step.properties:
            for name in re.findall(r"&(\w+)", prop.value or ""):
                variables.setdefault(
                    name,
                    ContextVariable(
                        name=name,
                        suggested=f"context.{name}",
                        origin=f"&{name} en {step.evidence.file}:{step.evidence.line}",
                    ),
                )
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
) -> JobPlan:
    libs = {**libraries, **{x.name.lower(): x for x in ir.libraries}}
    pl = _Planner(rules, libs, ir.file, report_policy, environment, table_action)
    source_macro = Path(ir.file.replace("\\", "/")).stem.casefold()
    entry_definition = next((macro for macro in ir.macros if macro.name.casefold() == source_macro), None)
    entry_calls = [
        operation
        for operation in ir.operations
        if operation.type == "macro_call"
        and str(operation.details.get("name", "")).casefold() == source_macro
    ]
    entry_macro = None
    expanded_operations: list[tuple[IROperation, str]] = []
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
                expanded_operations.extend((body_operation, prefix) for body_operation in entry_definition.operations)
            else:
                expanded_operations.append((operation, ""))
    else:
        expanded_operations = [
            (operation, "") for operation in ir.operations if operation.type != "include"
        ]
    steps = [pl.step(operation, index + 1, prefix) for index, (operation, prefix) in enumerate(expanded_operations)]
    written: dict[str, str] = {}
    for st, (op, _) in zip(steps, expanded_operations, strict=True):
        if op.type == "read" and op.inputs and op.inputs[0] in written:
            st.assumptions.append(
                f"Dataset producido antes en este programa ({written[op.inputs[0]]}): puede sustituirse por una conexión directa o un tHashOutput"
            )
        if op.type == "write":
            written.update({o: st.id for o in op.outputs})
    _connect(steps, None)
    children = []
    for m in ir.macros:
        if entry_macro and m.name.casefold() == entry_macro.name.casefold():
            continue
        ms = [pl.step(op, i + 1, f"m:{m.name}:") for i, op in enumerate(m.operations)]
        _connect(ms, None)
        children.append(ChildJob(name=m.name, params=m.params, steps=ms))
    all_steps = steps + [s for c in children for s in c.steps]
    context_by_name = {variable.name: variable for variable in _context_variables(ir, all_steps)}
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
    context_variables = sorted(context_by_name.values(), key=lambda variable: variable.name.lower())
    needed = _needed_libraries(pl.used_libs, libs, rules)
    pending = any(s.pending or s.confidence == "low" for s in all_steps)
    return JobPlan(
        project_id=project_id,
        rules_version=rules.version,
        program=ir.file,
        sha256=ir.sha256,
        job_name="job_" + slug(Path(ir.file).stem),
        job_status="needs_review" if pending or unresolved else "proposed",
        steps=steps,
        entry_macro=entry_macro,
        children=children,
        validation_cases=pl.cases,
        context_variables=context_variables,
        libraries_needed=needed,
        orchestration=orchestration or Orchestration(),
        unresolved=unresolved or [],
    )
