"""Genera el plan de construcción de un Job de Talend a partir de la representación intermedia.

Nada de lo que produce está verificado: componentes y propiedades son candidatos de
`rules/mappings/talend-components.json` hasta que el adaptador los contraste con talend-mcp.
"""

import re
from pathlib import Path

from pydantic import BaseModel

from sas_grid_migrator.intermediate_representation.models import IROperation, LibraryRef, ProgramIR
from sas_grid_migrator.migration_planner.expressions import translate
from sas_grid_migrator.migration_planner.models import (
    ChildJob,
    Connection,
    ContextVariable,
    Expression,
    JobPlan,
    LibraryNeeded,
    Orchestration,
    PlanStep,
    Property,
    SchemaColumn,
    ValidationCase,
)
from sas_grid_migrator.talend_adapter.catalog import load_catalog

_AGG = re.compile(
    r"^(count|sum|avg|mean|min|max)\s*\(\s*(?:distinct\s+)?(.*?)\s*\)$", re.IGNORECASE | re.DOTALL
)
_KEY = re.compile(r"(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)")
_READS = {"read", "read_file", "inline_data"}


class OpRule(BaseModel):
    component: str
    alternatives: list[str] = []
    properties: list[str] = []
    required: list[str] = []
    tests: list[dict[str, str]] = []


class MappingRules(BaseModel):
    version: str
    engines: dict[str, dict[str, str]]
    operations: dict[str, OpRule]
    editor_properties: dict[str, list[str]] = {}
    generic_components: list[str] = []


def load_mapping_rules(path: Path | None = None) -> MappingRules:
    p = (
        path
        or Path(__file__).resolve().parents[3] / "rules" / "mappings" / "talend-components.json"
    )
    return MappingRules.model_validate_json(p.read_text())


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


class _Planner:
    def __init__(self, rules: MappingRules, libs: dict[str, LibraryRef], file: str):
        self.rules, self.libs, self.file = rules, libs, file
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
    ) -> tuple[dict[str, str | None], list[Expression], list[SchemaColumn], list[str]]:
        d, line = op.details, op.evidence.line
        props: dict[str, str | None] = {}
        exprs: list[Expression] = []
        cols: list[SchemaColumn] = []
        pend: list[str] = []
        origin = f"SAS {op.evidence.file}:{line}"

        def col(name: str | None) -> None:
            if name and name != "*" and all(c.name != name for c in cols):
                cols.append(SchemaColumn(name=name, origin=origin))

        def expr(sas: str, ln: int | None = None) -> Expression:
            t = translate(sas)
            e = Expression(sas=sas, talend=t.talend, line=ln or line, warnings=t.warnings)
            exprs.append(e)
            for c in t.columns:
                col(c)
            return e

        if op.type in ("read", "write", "append"):
            ds = (op.inputs or op.outputs or [""])[0]
            props["TABLE"] = ds.split(".")[-1] if ds else None
            if op.type == "write":  # DATA lib.x reemplaza el dataset
                props["TABLE_ACTION"], props["DATA_ACTION"] = "DROP_CREATE", "INSERT"
                pend.append("Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo")
            elif op.type == "append":
                props["TABLE_ACTION"], props["DATA_ACTION"] = "NONE", "INSERT"
        elif op.type == "filter":
            t = translate(d.get("expression", ""))
            exprs.append(Expression(sas=t.sas, talend=t.talend, line=line, warnings=t.warnings))
            for c in t.columns:
                col(c)
            if t.simple:
                props["LOGICAL_OP"] = t.logical
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
            pass
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
                pend.append(
                    "Mapear las estadísticas de PROC "
                    + d["proc"].upper()
                    + " a operaciones de agregación"
                )
        elif op.type == "sort":
            keys = [
                re.sub(r"\s+(asc|desc|ascending|descending)$", "", k, flags=re.IGNORECASE).split(
                    "."
                )[-1]
                for k in d.get("keys", [])
            ]
            props["CRITERIA"] = ", ".join(d.get("keys", [])) or None
            for k in keys:
                col(k)
        elif op.type == "dedupe":
            props["UNIQUE_KEY"] = ", ".join(d.get("keys", [])) or None
            for k in d.get("keys", []):
                col(k)
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
                expr(a["expression"], a["line"])
                col(a["target"])
            for cnd in d.get("conditionals", []):
                exprs.append(
                    Expression(
                        sas=cnd["text"],
                        talend=None,
                        line=cnd["line"],
                        warnings=[
                            "Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow"
                        ],
                    )
                )
            props["Expressions"] = (
                f"{len(d.get('assignments', []))} asignaciones, {len(d.get('conditionals', []))} condicionales"
            )
        elif op.type == "read_file" or op.type == "write_file":
            props["FILENAME"] = d.get("file")
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
        return props, exprs, cols, pend

    # ---- conversión de una operación ----
    def step(self, op: IROperation, order: int, prefix: str) -> PlanStep:
        rule = self.rules.operations.get(op.type) or self.rules.operations["unsupported"]
        comp, alts, pend, assume = self.component(op, rule)
        values, exprs, cols, pend2 = self.fill(op, comp)
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
        pending = [*rule.required, *pend, *pend2]
        sem = (
            op.type
            in ("filter", "join", "compute", "aggregate", "dedupe", "stateful", "union", "sort")
            or op.confidence != "high"
        )
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
            expressions=exprs,
            assumptions=[*op.notes, *assume],
            pending=pending,
            tests=tests,
            evidence=op.evidence,
            confidence=op.confidence,
            status="pendiente" if pending else "propuesto",
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


def plan_program(
    ir: ProgramIR,
    project_id: str,
    rules: MappingRules,
    libraries: dict[str, LibraryRef],
    unresolved: list[str] | None = None,
    orchestration: Orchestration | None = None,
) -> JobPlan:
    libs = {**libraries, **{x.name.lower(): x for x in ir.libraries}}
    pl = _Planner(rules, libs, ir.file)
    steps = [pl.step(op, i + 1, "") for i, op in enumerate(ir.operations)]
    written: dict[str, str] = {}
    for st, op in zip(steps, ir.operations, strict=True):
        if op.type == "read" and op.inputs[0] in written:
            st.assumptions.append(
                f"Dataset producido antes en este programa ({written[op.inputs[0]]}): puede sustituirse por una conexión directa o un tHashOutput"
            )
        if op.type == "write":
            written.update({o: st.id for o in op.outputs})
    _connect(steps, None)
    children = []
    for m in ir.macros:
        ms = [pl.step(op, i + 1, f"m:{m.name}:") for i, op in enumerate(m.operations)]
        _connect(ms, None)
        children.append(ChildJob(name=m.name, params=m.params, steps=ms))
    all_steps = steps + [s for c in children for s in c.steps]
    ctx = {
        k: ContextVariable(
            name=k, sas_value=v, suggested=f"context.{k}", origin="%LET de primer nivel"
        )
        for k, v in ir.parameters.items()
    }
    for s in all_steps:
        for e in s.expressions:
            for name in re.findall(r"context\.(\w+)", e.talend or ""):
                ctx.setdefault(
                    name,
                    ContextVariable(
                        name=name,
                        suggested=f"context.{name}",
                        origin=f"&{name} en {s.evidence.file}:{s.evidence.line}",
                    ),
                )
        for p in s.properties:
            for name in re.findall(r"&(\w+)", p.value or ""):
                ctx.setdefault(
                    name,
                    ContextVariable(
                        name=name,
                        suggested=f"context.{name}",
                        origin=f"&{name} en {s.evidence.file}:{s.evidence.line}",
                    ),
                )
    needed = []
    for lib in sorted(pl.used_libs):
        ref = libs.get(lib)
        eng = (ref.engine or "").lower() if ref else ""
        conn = (
            rules.engines[eng]["input"].replace("Input", "Connection")
            if eng in rules.engines
            else "por_determinar (metadatos de archivo o base de datos)"
        )
        needed.append(
            LibraryNeeded(
                sas_name=ref.name if ref else lib,
                engine=ref.engine if ref else None,
                path=ref.path if ref else None,
                suggested_connection=conn,
            )
        )
    pending = any(s.pending or s.confidence == "low" for s in all_steps)
    return JobPlan(
        project_id=project_id,
        rules_version=rules.version,
        program=ir.file,
        sha256=ir.sha256,
        job_name="job_" + slug(Path(ir.file).stem),
        job_status="needs_review" if pending or unresolved else "proposed",
        steps=steps,
        children=children,
        validation_cases=pl.cases,
        context_variables=sorted(ctx.values(), key=lambda c: c.name.lower()),
        libraries_needed=needed,
        orchestration=orchestration or Orchestration(),
        unresolved=unresolved or [],
    )
