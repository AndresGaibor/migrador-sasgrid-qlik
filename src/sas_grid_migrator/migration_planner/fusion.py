"""Fusión de operaciones fila a fila en un único tMap.

Una cadena de filter, compute, rename, select_columns y project se convierte en UN paso `tMap`:
el filtro pasa a la condición de salida, los cálculos y renombres a expresiones de columna y KEEP/DROP
al esquema de salida. Cada expresión conserva su línea SAS (`Expression.line`) y el paso guarda los
ids originales en `fused_from`.

Una operación entra en la cadena solo si su lógica se puede escribir como expresión de tMap y no
depende de una columna que la misma cadena ya calculó o renombró: en un tMap las expresiones de salida
leen columnas de entrada, no otras salidas. Si no se cumple, la cadena se parte y la operación queda
como su propio paso (con su componente de siempre).
"""

from __future__ import annotations

import re
from collections.abc import Callable

from sas_grid_migrator.intermediate_representation.models import IROperation
from sas_grid_migrator.migration_planner.expressions import translate
from sas_grid_migrator.migration_planner.models import (
    Expression,
    PlanStep,
    Property,
    SchemaColumn,
)
from sas_grid_migrator.sas_parser.ast import Loc

#: Operaciones que se funden en un tMap (fila a fila, sin estado).
FUSABLE = frozenset({"filter", "compute", "rename", "select_columns", "project"})

_WORD = re.compile(r"[A-Za-z_]\w*")
_IF = re.compile(r"^\s*(?:else\s+)?if\s+(.+?)\s+then\s+(\w+)\s*=\s*(.+?)\s*;?\s*$", re.IGNORECASE | re.DOTALL)
_ELSE = re.compile(r"^\s*else\s+(\w+)\s*=\s*(.+?)\s*;?\s*$", re.IGNORECASE | re.DOTALL)
_OPERATORS = {"=": "==", "eq": "==", "ne": "!=", "<>": "!=", "^=": "!="}
_CONDITIONAL_TEXT = re.compile(r"\s*(?:else\s+)?if\b", re.IGNORECASE)
_NOTE_TYPES = "Comparación con columna de tipo no confirmado: validar tipos y nulos en Studio"


def _words(text: str | None) -> set[str]:
    return {w.lower() for w in _WORD.findall(text or "")}


def refs_of(op: IROperation) -> set[str]:
    """Palabras que la operación lee (en minúsculas). Conservador: incluye todo lo que aparece en la expresión."""
    d = op.details
    if op.type == "filter":
        return _words(str(d.get("expression", "")))
    if op.type == "compute":
        refs: set[str] = set()
        for a in d.get("assignments", []):
            refs |= _words(str(a.get("expression", "")))
        for c in d.get("conditionals", []):
            refs |= _words(str(c.get("text", "")))
        return refs
    if op.type == "rename":
        refs = set()
        for a, b in d.get("mapping", {}).items():
            refs |= _words(a) | _words(str(b))
        return refs
    if op.type == "project":
        refs = set()
        for it in d.get("select", []):
            refs |= _words(str(it.get("expression", "")))
        return refs
    return set()


def _simple_condition(text: str) -> tuple[str | None, list[str]]:
    """Condición SAS a Java de tMap: la traducción completa si la hay; si no, las comparaciones simples."""
    t = translate(text)
    if t.talend:
        return t.talend, list(t.warnings)
    if not t.simple:
        return None, []
    parts = []
    for item in t.simple:
        column = item.get("column")
        operator = _OPERATORS.get(str(item.get("operator")), str(item.get("operator")))
        value = str(item.get("value", ""))
        if len(value) >= 2 and value[0] == value[-1] == "'":
            value = '"' + value[1:-1].replace('"', '\\"') + '"'
        parts.append(f"input_row.{column} {operator} {value}")
    joiner = " || " if t.logical == "||" else " && "
    return "(" + joiner.join(parts) + ")", [_NOTE_TYPES]


def _conditional_expressions(op: IROperation) -> list[Expression] | None:
    """IF/ELSE IF/ELSE de un DATA step → una expresión ternaria por variable destino; None si no se puede."""
    items = op.details.get("conditionals", [])
    parsed: list[tuple[str, str | None, str, str]] = []
    for item in items:
        text = str(item.get("text", ""))
        m = _IF.match(text)
        if m:
            parsed.append(("if", m.group(1), m.group(2), m.group(3)))
            continue
        e = _ELSE.match(text)
        if e:
            parsed.append(("else", None, e.group(1), e.group(2)))
            continue
        return None
    if not parsed:
        return []
    targets = {target for _, _, target, _ in parsed}
    if len(targets) != 1 or any(kind == "else" for kind, *_ in parsed[:-1]):
        return None
    target = targets.pop()
    java = "null"
    warnings: list[str] = []
    for index in range(len(parsed) - 1, -1, -1):
        kind, condition, _target, value = parsed[index]
        value_t = translate(value)
        if not value_t.talend:
            return None
        warnings.extend(value_t.warnings)
        if kind == "else":
            java = value_t.talend
            continue
        cond_java, cond_warnings = _simple_condition(condition or "")
        if cond_java is None:
            return None
        warnings.extend(cond_warnings)
        java = f"({cond_java} ? {value_t.talend} : {java})"
    line = int(items[0].get("line", op.evidence.line)) if items else op.evidence.line
    sas = " ".join(str(item.get("text", "")) for item in items)
    return [Expression(sas=sas, talend=java, target=target, line=line, warnings=list(dict.fromkeys(warnings)))]


def fusable_expressions(op: IROperation, probe: PlanStep) -> list[Expression] | None:
    """Expresiones que la operación aporta al tMap; None si no puede fundirse (queda como paso propio)."""
    d = op.details
    if op.type in ("rename", "select_columns"):
        return []
    if op.type == "filter":
        java, warnings = _simple_condition(str(d.get("expression", "")))
        if java is None:
            return None
        return [
            Expression(
                sas=str(d.get("expression", "")),
                talend=java,
                line=op.evidence.line,
                warnings=["Filtro de salida del tMap: " + w for w in warnings],
            )
        ]
    if op.type == "compute" and op.details.get("superseded"):
        return []  # toda su columna la sustituye una reasignación posterior de la misma cadena
    if op.type == "compute":
        assigned = [
            e
            for e in probe.expressions
            if e.target and not _CONDITIONAL_TEXT.match(e.sas)
        ]
        # Una asignación sin traducción automática sigue en el tMap como expresión pendiente (su aviso
        # viaja con `pending`): así N bloques de copia de vuelta siguen siendo un solo tMap.
        if not assigned and not d.get("conditionals"):
            return None
        if d.get("conditionals"):
            rebuilt = _conditional_expressions(op)
            if rebuilt is None:
                return None
            return [*assigned, *rebuilt]
        return list(assigned)
    if op.type == "project":
        if any(e.talend is None for e in probe.expressions):
            return None
        return list(probe.expressions)
    return None


class ChainState:
    """Lo que una cadena ya calculó o renombró; decide si la siguiente operación puede fundirse."""

    def __init__(self) -> None:
        self.computed: set[str] = set()
        self.renamed: set[str] = set()

    def accepts(self, op: IROperation, exprs: list[Expression] | None) -> bool:
        if op.type not in FUSABLE or exprs is None:
            return False
        if op.type == "select_columns":
            return True
        if op.details.get("resolved_inputs"):
            return True  # sus columnas ya se sustituyeron por la expresión de origen (versions.inline)
        if op.type == "rename":
            keys = {k.lower() for k in op.details.get("mapping", {})}
            values = {str(v).lower() for v in op.details.get("mapping", {}).values()}
            return not (keys | values) & self.computed
        return not refs_of(op) & (self.computed | self.renamed)

    def add(self, op: IROperation) -> None:
        if op.type == "compute":
            self.computed |= {str(a.get("target", "")).lower() for a in op.details.get("assignments", [])}
            self.computed |= {t.lower() for t in _conditional_targets(op)}
        elif op.type == "rename":
            for a, b in op.details.get("mapping", {}).items():
                self.renamed |= {a.lower(), str(b).lower()}
        elif op.type == "project":
            self.computed |= {
                str(it.get("alias")).lower()
                for it in op.details.get("select", [])
                if it.get("alias") and not re.fullmatch(r"(?:\w+\.)?\w+", str(it.get("expression", "")))
            }


def _conditional_targets(op: IROperation) -> list[str]:
    out: list[str] = []
    for c in op.details.get("conditionals", []):
        m = _IF.match(str(c.get("text", ""))) or _ELSE.match(str(c.get("text", "")))
        if m:
            out.append(m.group(2) if m.re is _IF else m.group(1))
    return out


def _apply_schema(cols: list[SchemaColumn], op: IROperation, sub: PlanStep) -> list[SchemaColumn]:
    """Esquema tras una operación: renombres, KEEP/DROP y proyección; el resto añade sus columnas."""
    if op.type == "rename":
        mapping = {a.lower(): str(b) for a, b in op.details.get("mapping", {}).items()}
        return [c.model_copy(update={"name": mapping[c.name.lower()]}) if c.name.lower() in mapping else c for c in cols]
    if op.type == "select_columns":
        keep = [str(k).lower() for k in op.details.get("keep") or []]
        drop = {str(k).lower() for k in op.details.get("drop") or []}
        if keep:
            by_name = {c.name.lower(): c for c in cols}
            return [by_name.get(k, SchemaColumn(name=k, origin="KEEP")) for k in keep]
        return [c for c in cols if c.name.lower() not in drop]
    if op.type == "project":
        by_name = {c.name.lower(): c for c in cols}
        out: list[SchemaColumn] = []
        for it in op.details.get("select", []):
            name = str(it.get("alias") or str(it.get("expression")).split(".")[-1])
            if name == "*":
                out.extend(cols)
                continue
            out.append(by_name.get(name.lower(), SchemaColumn(name=name, origin="SELECT")))
        return out
    names = {c.name.lower() for c in cols}
    return cols + [c for c in sub.schema_columns if c.name.lower() not in names]


#: Pendientes que la fusión resuelve: la traducción de la condición o del IF/ELSE ya está en el tMap.
_RESOLVED_BY_FUSION: dict[str, Callable[[str], bool]] = {
    "filter": lambda p: p.startswith("Traducir la condición manualmente"),
    "compute": lambda p: p.startswith("Condicional IF/ELSE sin traducción automática"),
}


def merge_tmap(
    entries: list[tuple[IROperation, PlanStep, list[Expression]]],
    *,
    step_id: str,
    meta: tuple[bool | None, str | None, list[str]],
) -> PlanStep:
    """Un único paso tMap a partir de las operaciones de una cadena fusionable."""
    ops = [op for op, _, _ in entries]
    subs = [sub for _, sub, _ in entries]
    in_catalog, doc_url, variants = meta
    cols: list[SchemaColumn] = []
    exprs: list[Expression] = []
    filters: list[str] = []
    outputs: list[str] = []
    pending: list[str] = []
    tests: list[str] = []
    assumptions: list[str] = []
    for op, sub, own in entries:
        cols = _apply_schema(cols, op, sub)
        exprs.extend(own)
        if op.type == "filter":
            filters.extend(e.talend or e.sas for e in own)
        if op.type == "rename":
            outputs.append(", ".join(f"{a} → {b}" for a, b in op.details.get("mapping", {}).items()))
        if op.type == "project":
            outputs.append(", ".join(str(it.get("alias") or it.get("expression")) for it in op.details.get("select", [])))
        resolved = _RESOLVED_BY_FUSION.get(op.type, lambda _p: False)
        for item in sub.pending:
            if not resolved(item) and item not in pending:
                pending.append(item)
        tests.extend(t for t in sub.tests if t not in tests)
        assumptions.extend(a for a in sub.assumptions if a not in assumptions)
    properties: list[Property] = []
    if filters:
        properties.append(Property(name="Output filter", value=" && ".join(f"({f})" for f in filters), origin="SAS fusionado"))
    if outputs:
        properties.append(Property(name="Output columns", value="; ".join(outputs), origin="SAS fusionado"))
    names = [op.type for op in ops]
    first = subs[0]
    evidence = Loc(
        file=first.evidence.file,
        line=min(sub.evidence.line for sub in subs),
        end_line=max(sub.evidence.end_line for sub in subs),
    )
    confidences = [sub.confidence for sub in subs]
    confidence = "low" if "low" in confidences else ("medium" if "medium" in confidences else "high")
    purposes = [sub.purpose for sub in subs]
    return PlanStep(
        id=step_id,
        order=0,
        subjob=first.subjob,
        library=next((sub.library for sub in subs if sub.library), None),
        action="add_component",
        operation_id=ops[0].id,
        operation_type="fused_tmap",
        component_candidate="tMap",
        purpose="Transformar en un solo tMap: " + "; ".join(purposes)[:300],
        properties=properties,
        schema_columns=cols,
        expressions=exprs,
        assumptions=assumptions,
        pending=pending,
        tests=tests,
        evidence=evidence,
        confidence=confidence,  # type: ignore[arg-type]
        status="pendiente" if pending else "propuesto",
        in_catalog=in_catalog,
        doc_url=doc_url,
        variants=variants,
        requires_semantic_validation=True,
        why=(
            f"Un solo tMap en vez de {len(ops)} componentes ({', '.join(names)}): las operaciones fila a fila "
            "se resuelven en el filtro de salida y las expresiones de columna, sin datasets intermedios."
        ),
        fused_from=[op.id for op in ops],
    )
