"""Construye `ProgramIR` a partir de un `ParsedProgram`."""

import hashlib
import json
import re
from collections import Counter
from typing import Any

from sas_grid_migrator.intermediate_representation.models import (
    IROperation,
    LibraryRef,
    MacroIR,
    ProgramIR,
)
from sas_grid_migrator.migration_planner.plumbing import is_studio_helper
from sas_grid_migrator.intermediate_representation.remote import fold_remote_transfers
from sas_grid_migrator.sas_parser.ast import (
    DatasetRef,
    DataStep,
    GlobalStmt,
    Loc,
    MacroDef,
    Node,
    ParsedProgram,
    ProcStep,
    SqlQuery,
)
from sas_grid_migrator.sas_parser.parser import split_args

_OPT = re.compile(
    r"\b(keep|drop|rename|where|in|obs|firstobs|label|sortedby|index|compress)\s*=", re.IGNORECASE
)
_ASSIGN = re.compile(r"^([A-Za-z_][\w.]*)\s*=(?!=)\s*(.*)$", re.DOTALL)
_ALIAS = re.compile(r"^(.*?)\s+as\s+([A-Za-z_]\w*)$", re.IGNORECASE | re.DOTALL)
_NON_ASSIGN = {
    "if", "else", "do", "select", "when", "otherwise", "end", "retain", "array", "length", "format",
    "informat", "label", "attrib", "call", "set", "merge", "where", "keep", "drop", "rename", "by",
    "output", "infile", "input", "file", "put", "declare", "dcl", "datalines", "cards", "update",
    "modify", "data",
}  # fmt: skip
_REPORT_PROCS = {
    "print",
    "report",
    "tabulate",
    "sgplot",
    "sgpanel",
    "gplot",
    "univariate",
    "gchart",
}
_AGG_PROCS = {"means", "summary", "freq", "tabulate", "univariate"}
_MAINT_PROCS = {"datasets", "delete", "copy", "contents", "printto", "optload", "optsave"}


def dsid(ref: DatasetRef) -> str:
    """Identificador normalizado: `lib.nombre` en minúsculas; sin librería, `work`."""
    if ref.dynamic:
        return ref.raw
    return f"{(ref.lib or 'work').lower()}.{ref.name.lower()}"


def dataset_options(opts: str | None) -> dict:
    """keep/drop/rename/where de las opciones de un dataset (`(keep=a b where=(x>1))`)."""
    out: dict = {}
    if not opts:
        return out
    marks = list(_OPT.finditer(opts))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(opts)
        key, val = m.group(1).lower(), opts[m.end() : end].strip()
        if key in ("keep", "drop"):
            out[key] = val.split()
        elif key == "rename":
            pairs = re.findall(r"(\w+)\s*=\s*(\w+)", val.strip("() "))
            out["rename"] = dict(pairs)
        elif key == "where":
            out["where"] = val.strip()[1:-1] if val.startswith("(") and val.endswith(")") else val
    return out


def split_select_list(select_list: str | None) -> list[dict]:
    items = []
    for raw in split_args(select_list or ""):
        m = _ALIAS.match(raw)
        expr, alias = (m.group(1).strip(), m.group(2)) if m else (raw.strip(), None)
        if alias is None:
            bare = re.fullmatch(r"(?:\w+\.)?(\w+|\*)", expr)
            alias = bare.group(1) if bare else None
        items.append({"expression": expr, "alias": alias})
    return items


def guess_join_type(subsetting: list[str], in_vars: list[str | None]) -> str | None:
    if len(in_vars) != 2 or not all(in_vars):
        return None
    a, b = (v.lower() for v in in_vars)  # type: ignore[union-attr]
    if not subsetting:
        return "full"
    e = re.sub(r"[\s()]+", "", subsetting[-1].lower().replace(" ", ""))
    e = re.sub(rf"\b{a}\b", "A", e)
    e = re.sub(rf"\b{b}\b", "B", e)
    table = {
        "A": "left",
        "B": "right",
        "AandB": "inner",
        "BandA": "inner",
        "AandnotB": "left_anti",
        "notBandA": "left_anti",
        "notAandB": "right_anti",
        "BandnotA": "right_anti",
    }
    return table.get(e.replace("^", "not").replace("~", "not"))


class _Ctx:
    def __init__(self, file: str, macro_files: dict[str, str]):
        self.file = file
        self.macro_files = macro_files
        self.counter: Counter[tuple[int, str]] = Counter()

    def op(self, type_: str, step: str, loc: Loc, line: int | None = None, **kw) -> IROperation:
        ln = line or loc.line
        self.counter[(ln, type_)] += 1
        return IROperation(
            id=f"op_{ln}_{type_}_{self.counter[(ln, type_)]}",
            type=type_,  # type: ignore[arg-type]
            step=step,
            evidence=loc.model_copy(update={"line": ln}) if line else loc,
            **kw,
        )


# ---------- DATA step ----------


#: `if last.g;` (subsetting IF sobre el último de grupo) y `if first.g then acc = 0;` (reinicio por grupo).
_LAST_SUBSET = re.compile(r"^if\s+last\.(\w+)\s*;?$", re.IGNORECASE)
_FIRST_RESET = re.compile(r"^if\s+first\.\w+\s+then\s+[A-Za-z_]\w*\s*=\s*0\s*;?$", re.IGNORECASE)
#: Construcciones que no son un acumulado por grupo simple.
_NOT_GROUP_SUM = frozenset(
    {"explicit_output", "array", "hash", "retain", "file_output", "call_execute", "call_symput", "call_routine"}
)


def _group_sum(n: DataStep) -> tuple[list[str], list[tuple[str, str]]] | None:
    """Acumulado por grupo: `by g; if first.g then acc = 0; acc + x; if last.g;` (una fila por grupo con la suma).

    Devuelve (claves BY, [(acumulador, columna sumada)]) o None si el paso no tiene esa forma exacta. Se traduce a un
    `aggregate` (tAggregateRow) en lugar del estado entre filas. Sin salidas explícitas ni otras construcciones de
    estado; un `if`/`else` con THEN distinto del reinicio por grupo lo deja fuera.
    """
    if not n.by or "first_last" not in n.constructs or set(n.constructs) & _NOT_GROUP_SUM:
        return None
    by = [b.split(".")[-1].lower() for b in n.by]
    last_match = [
        m for s in n.statements if s.kw == "if" for m in [_LAST_SUBSET.match(s.text.strip())] if m
    ]
    if not any(m.group(1).lower() == by[-1] for m in last_match):
        return None
    accumulators: list[tuple[str, str]] = []
    for s in n.statements:
        text = s.text.strip()
        if s.kw == "else":
            return None
        if s.kw == "if" and re.search(r"\bthen\b", text, re.IGNORECASE) and not _FIRST_RESET.match(text):
            return None
        sums = _SUM_STATEMENT.match(s.text)
        if sums and s.kw not in _NON_ASSIGN:
            target, addend = sums.group(1), sums.group(2).strip()
            if not re.fullmatch(r"[A-Za-z_]\w*", addend) or target.lower() in by:
                return None
            accumulators.append((target, addend))
    return (by, accumulators) if accumulators else None


def _data_step(n: DataStep, c: _Ctx) -> list[IROperation]:
    step = f"s{n.loc.line}"
    ops: list[IROperation] = []
    add = lambda t, **kw: ops.append(c.op(t, step, n.loc, **kw))
    ins = [dsid(i) for i in n.inputs]
    for i in n.inputs:
        o = dataset_options(i.options)
        add(
            "read",
            inputs=[dsid(i)],
            details={"dataset": i.raw, "in_var": i.in_var, "options": i.options},
        )
        if "where" in o:
            add(
                "filter",
                inputs=[dsid(i)],
                details={"expression": o["where"], "origin": "opción where= del dataset"},
            )
        if "keep" in o or "drop" in o:
            add(
                "select_columns",
                inputs=[dsid(i)],
                details={k: o[k] for k in ("keep", "drop") if k in o},
            )
        if "rename" in o:
            add("rename", inputs=[dsid(i)], details={"mapping": o["rename"]})
    first = next((s for s in n.statements if s.kw in ("infile", "input")), None)
    if first and not n.inputs and not n.datalines_rows:
        # Con `datalines` los datos están en el programa: un solo paso (`inline_data`), no una lectura de archivo.
        add(
            "read_file",
            line=first.line,
            details={"statements": [s.text for s in n.statements if s.kw in ("infile", "input")]},
            confidence="medium",
        )
    if "datalines" in n.constructs:
        add(
            "inline_data",
            details={
                "rows": list(n.datalines_rows),
                "statements": [s.text for s in n.statements if s.kw in ("infile", "input")],
            },
            confidence="medium",
            notes=["Datos incrustados en el programa"],
        )
    if n.input_kind == "merge":
        guess = guess_join_type(n.subsetting_if, [i.in_var for i in n.inputs])
        add(
            "join",
            inputs=ins,
            details={"kind": "merge_by", "keys": n.by, "join_type_guess": guess},
            confidence="medium",
            notes=[
                "MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere"
            ],
        )
    elif n.input_kind == "set" and len(n.inputs) > 1:
        add(
            "union",
            inputs=ins,
            details={"interleave_by": n.by or None},
            notes=["SET con varias entradas concatena; con BY intercala ordenado"] if n.by else [],
        )
    elif n.input_kind == "update":
        add("unsupported", inputs=ins, details={"statement": "update"}, confidence="low")
    for s in n.statements:
        if s.kw == "where":
            add(
                "filter",
                line=s.line,
                inputs=ins,
                details={"expression": s.text[5:].strip(), "origin": "sentencia WHERE"},
            )
    in_vars = {i.in_var.lower() for i in n.inputs if i.in_var}
    group = _group_sum(n)
    for s in n.statements:
        if group and s.kw == "if" and _LAST_SUBSET.match(s.text.strip()):
            continue  # el tAggregateRow ya da una fila por grupo
        if s.kw == "if" and not re.search(r"\bthen\b", s.text, re.IGNORECASE):
            expr = s.text[2:].strip()
            words = set(re.findall(r"\w+", expr.lower()))
            if n.input_kind == "merge" and words and words <= in_vars | {"and", "or", "not"}:
                continue  # `if a;` en un MERGE determina el tipo de join, no es un filtro de datos
            add(
                "filter",
                line=s.line,
                inputs=ins,
                details={"expression": expr, "origin": "IF subsetting"},
            )
    assigns = []
    for s in n.statements:
        m = _ASSIGN.match(s.text)
        if m and s.kw not in _NON_ASSIGN:
            assigns.append({"line": s.line, "target": m.group(1), "expression": m.group(2).strip()})
            continue
        # Sentencia de suma de SAS (`contador + 1;`, `total + importe;`): acumula sobre sí misma.
        sums = _SUM_STATEMENT.match(s.text)
        if sums and s.kw not in _NON_ASSIGN:
            name, addend = sums.group(1), sums.group(2).strip()
            if group and name in {acc for acc, _ in group[1]}:
                continue  # acumulado por grupo: lo calcula el tAggregateRow
            assigns.append({"line": s.line, "target": name, "expression": f"{name} + {addend}", "accumulates": True})
    conds = [
        {"line": s.line, "text": s.text}
        for s in n.statements
        if s.kw in ("if", "else")
        and (s.kw == "else" or re.search(r"\bthen\b", s.text, re.IGNORECASE))
        and not (group and _FIRST_RESET.match(s.text.strip()))
    ]
    if assigns or conds:
        add(
            "compute",
            inputs=ins,
            details={"assignments": assigns, "conditionals": conds},
            confidence="medium" if conds else "high",
            notes=["Lógica condicional: revisar orden de evaluación y valores missing"]
            if conds
            else [],
        )
    if {"retain", "first_last", "array", "hash"} & set(n.constructs) and group is None:
        tags = sorted({"retain", "first_last", "array", "hash"} & set(n.constructs))
        add(
            "stateful",
            inputs=ins,
            details={"constructs": tags, "by": n.by, "retain": n.retain, "arrays": n.arrays},
            confidence="low",
            notes=[
                "Estado entre filas: no hay traducción directa a un componente; requiere diseño manual"
            ],
        )
    if group:
        by_vars, accumulators = group
        add(
            "aggregate",
            inputs=ins,
            details={
                "group_by": by_vars,
                "select": [{"expression": f"sum({addend})", "alias": target} for target, addend in accumulators],
            },
            confidence="medium",
            notes=["Acumulado por grupo (first./last.) traducido a tAggregateRow: una fila por grupo"],
        )
    for s in n.statements:
        if s.kw == "call":
            low = s.text[4:].strip().lower()
            if low.startswith("execute"):
                add(
                    "dynamic_code",
                    line=s.line,
                    details={"statement": s.text},
                    confidence="low",
                    notes=["CALL EXECUTE: documentar el código que genera"],
                )
            elif low.startswith("symput"):
                add("set_variable", line=s.line, details={"statement": s.text}, confidence="medium")
    if n.keep or n.drop:
        add(
            "select_columns",
            details={
                "keep": " ".join(n.keep).split(),
                "drop": " ".join(n.drop).split(),
                "origin": "sentencia KEEP/DROP",
            },
        )
    if n.rename:
        add(
            "rename",
            details={"mapping": dict(re.findall(r"(\w+)\s*=\s*(\w+)", " ".join(n.rename)))},
        )
    conditional_multi_output = (
        len(n.outputs) > 1
        and n.n_conditionals > 0
        and any(
            statement.kw == "output"
            or (
                statement.kw in {"if", "else"}
                and re.search(r"\boutput\b", statement.text, re.IGNORECASE)
            )
            for statement in n.statements
        )
    )
    if conditional_multi_output:
        add(
            "unsupported",
            outputs=[dsid(output) for output in n.outputs],
            confidence="low",
            notes=["OUTPUT condicional a varios datasets: modelar el routing de filas manualmente"],
        )
    else:
        for o in n.outputs:
            oo = dataset_options(o.options)
            d = {"dataset": o.raw, "options": o.options}
            if "keep" in oo or "drop" in oo:
                add(
                    "select_columns",
                    outputs=[dsid(o)],
                    details={k: oo[k] for k in ("keep", "drop") if k in oo},
                )
            if "rename" in oo:
                add("rename", outputs=[dsid(o)], details={"mapping": oo["rename"]})
            add("write", outputs=[dsid(o)], details=d)
    if "file_output" in n.constructs:
        add(
            "write_file",
            confidence="medium",
            details={"statements": [s.text for s in n.statements if s.kw in ("file", "put")][:5]},
        )
    return ops


# ---------- PROC ----------


_PASSTHROUGH_ENGINE = {
    # `execute (<sql>) by impala`: el motor va al final, después del paréntesis.
    "execute": re.compile(r"\)\s*by\s+([A-Za-z]\w*)\s*;?\s*$|^\s*execute\s+by\s+([A-Za-z]\w*)", re.IGNORECASE),
    # `connect to impala (...)`
    "connect": re.compile(r"\bconnect\s+to\s+([A-Za-z]\w*)", re.IGNORECASE),
}


def _passthrough_engine(kind: str, text: str) -> str | None:
    """Motor de una sentencia SQL pass-through (`impala`, `oracle`…), en minúsculas."""
    pattern = _PASSTHROUGH_ENGINE.get(kind)
    match = pattern.search(text) if pattern else None
    if not match:
        return None
    return next(group for group in match.groups() if group).lower()


_CONNECTION_TO = re.compile(r"connection\s+to\s+([A-Za-z]\w*)\s*\(", re.IGNORECASE)


def _passthrough_reads(text: str) -> list[tuple[str, str]]:
    """(motor, consulta) de cada `connection to <motor> (...)` del texto, en orden."""
    from sas_grid_migrator.sas_parser.datasets import _balanced

    out: list[tuple[str, str]] = []
    for match in _CONNECTION_TO.finditer(text):
        open_at = match.end() - 1
        end = _balanced(text, open_at)
        out.append((match.group(1).lower(), text[open_at + 1 : end - 1].strip()))
    return out


def _sql_ops(q: SqlQuery, step: str, c: _Ctx) -> list[IROperation]:
    ops: list[IROperation] = []
    loc = q.loc
    add = lambda t, **kw: ops.append(c.op(t, step, loc, **kw))
    srcs = [dsid(s) for s in q.sources]
    for s in q.sources:
        add(
            "read",
            inputs=[dsid(s)],
            details={"dataset": s.raw, "alias": s.alias, "options": s.options},
        )
    if len(q.joins) > 1:
        add(
            "unsupported",
            inputs=srcs,
            details={"statement": "chained_sql_joins", "text": q.text[:300]},
            confidence="low",
            notes=["SQL con JOIN encadenados: diseñar manualmente la topología de entradas y claves"],
        )
    else:
        for j in q.joins:
            add(
                "join",
                inputs=srcs,
                details={
                    "kind": j.kind,
                    "table": j.table.raw if j.table else None,
                    "alias": j.table.alias if j.table else None,
                    "on": j.on,
                },
                confidence="high" if j.on else "medium",
            )
    if "sql_implicit_join" in q.constructs and len(q.joins) <= 1:
        add(
            "join",
            inputs=srcs,
            details={"kind": "implicit", "on": q.where},
            confidence="medium",
            notes=["Join por coma: la condición está en el WHERE"],
        )
    if "sql_set_operation" in q.constructs:
        unsupported = [op for op in q.set_operations if op in {"intersect", "except"}]
        if unsupported:
            add(
                "unsupported",
                inputs=srcs,
                details={"set_operations": unsupported, "text": q.text[:200]},
                confidence="low",
                notes=[f"SQL {op.upper()}: requiere diseño manual; no equivale a tUnite" for op in unsupported],
            )
        else:
            add("union", inputs=srcs, details={"text": q.text[:200]}, confidence="medium")
    # R46: `from connection to <motor> (select ...)`: lectura pass-through; la consulta va tal cual al motor.
    if q.kind not in ("connect", "execute", "disconnect"):
        for engine, inner in _passthrough_reads(q.text):
            add(
                "read",
                details={"passthrough": True, "engine": engine, "sql": inner, "dataset": f"connection to {engine}"},
                confidence="medium",
                notes=["Lectura pass-through: la consulta se ejecuta en el motor, sin ida y vuelta por SAS"],
            )
    if q.where:
        add("filter", inputs=srcs, details={"expression": q.where, "origin": "WHERE"})
    items = split_select_list(q.select_list)
    if q.group_by or "sql_aggregate" in q.constructs:
        add(
            "aggregate",
            inputs=srcs,
            details={
                "group_by": [g.strip() for g in split_args(q.group_by or "")],
                "select": items,
            },
        )
    elif items:
        add("project", inputs=srcs, details={"select": items, "distinct": q.distinct})
    if q.having:
        add("filter", inputs=srcs, details={"expression": q.having, "origin": "HAVING"})
    if q.distinct and (q.group_by or "sql_aggregate" in q.constructs):
        add("dedupe", inputs=srcs, details={"origin": "DISTINCT"})
    if q.order_by:
        add("sort", inputs=srcs, details={"keys": [k.strip() for k in split_args(q.order_by)]})
    for mv in q.into:
        add(
            "set_variable",
            details={"macro_variable": mv, "origin": "SELECT INTO"},
            confidence="medium",
        )
    if q.target and q.kind in ("create_table", "create_view", "insert_into"):
        add(
            "write",
            outputs=[dsid(q.target)],
            details={
                "dataset": q.target.raw,
                "mode": "append" if q.kind == "insert_into" else "replace",
                "view": q.kind == "create_view",
                # Texto SQL completo: el ELT (migration_planner/elt.py) lo empuja al motor si todo es de un mismo motor.
                "sql": q.text if q.kind in ("create_table", "insert_into") else None,
            },
        )
    elif q.kind in ("delete_from", "update"):
        add(
            "write",
            outputs=[dsid(q.target)] if q.target else [],
            details={"mode": q.kind, "where": q.where},
            confidence="medium",
        )
    elif q.kind in ("connect", "execute", "disconnect"):
        engine = _passthrough_engine(q.kind, q.text)
        add(
            "sql_passthrough" if q.kind == "execute" else "unsupported",
            details={
                "statement": q.kind,
                "text": q.text[:300],
                "sql": q.text if q.kind == "execute" else None,
                "engine": engine,
            },
            confidence="low",
            notes=["SQL pass-through: el SQL se ejecuta en el motor externo"],
        )
    elif q.kind == "other":
        add("unsupported", details={"text": q.text[:300]}, confidence="low")
    return ops


def _proc_step(n: ProcStep, c: _Ctx) -> list[IROperation]:
    step = f"s{n.loc.line}"
    ops: list[IROperation] = []
    add = lambda t, **kw: ops.append(c.op(t, step, n.loc, **kw))
    ins, outs = [dsid(i) for i in n.inputs], [dsid(o) for o in n.outputs]
    if n.name == "sql":
        for q in n.queries:
            ops += _sql_ops(q, step, c)
    elif n.name == "sort":
        keys = n.by
        add("read", inputs=ins, details={"dataset": n.inputs[0].raw if n.inputs else None})
        add("sort", inputs=ins, outputs=outs or ins, details={"keys": keys, "options": n.options})
        if re.search(r"\bnodupkey\b", n.options, re.IGNORECASE):
            add(
                "dedupe",
                inputs=ins,
                outputs=outs or ins,
                details={"keys": keys, "mode": "nodupkey"},
            )
        elif re.search(r"\bnodup\b", n.options, re.IGNORECASE):
            add(
                "dedupe",
                inputs=ins,
                outputs=outs or ins,
                details={"mode": "nodup (fila completa)"},
                confidence="medium",
            )
        add(
            "write",
            outputs=outs or ins,
            details={
                "dataset": (n.outputs or n.inputs)[0].raw if (n.outputs or n.inputs) else None,
                "in_place": not n.outputs,
            },
        )
    elif n.name == "append":
        base = re.search(r"\bbase\s*=\s*(\S+)", n.options, re.IGNORECASE)
        add(
            "append",
            inputs=ins,
            outputs=[base.group(1).lower()] if base else [],
            details={"options": n.options},
        )
    elif n.name == "format":
        add(
            "format_definition",
            details={"statements": [s.text for s in n.statements][:500]},
            confidence="medium",
        )
    elif n.name in ("import", "export"):
        f = n.fields.get("datafile") or n.fields.get("outfile")
        add(
            "read_file" if n.name == "import" else "write_file",
            inputs=ins if n.name == "export" else [],
            outputs=outs if n.name == "import" else [],
            details={"file": f, "options": n.options},
        )
    elif n.name in _AGG_PROCS:
        add(
            "aggregate",
            inputs=ins,
            outputs=outs,
            details={"proc": n.name, "by": n.by, "statements": [s.text for s in n.statements][:20]},
            confidence="low",
            notes=[f"PROC {n.name.upper()}: mapear estadísticas concretas a tAggregateRow"],
        )
        if n.name in _REPORT_PROCS:
            add(
                "report",
                inputs=ins,
                confidence="low",
                notes=["Salida de reporte: decidir si se migra"],
            )
    elif n.name in _REPORT_PROCS:
        add(
            "report",
            inputs=ins,
            details={"proc": n.name},
            confidence="low",
            notes=["Salida de reporte: decidir si se migra"],
        )
    elif n.name in _MAINT_PROCS:
        add(
            "maintenance",
            inputs=ins,
            details={"proc": n.name, "options": n.options, "statements": [s.text for s in n.statements][:10]},
            confidence="low",
        )
    else:
        add(
            "unsupported",
            inputs=ins,
            outputs=outs,
            details={"proc": n.name, "options": n.options},
            confidence="low",
            notes=[f"PROC {n.name.upper()} sin traducción definida"],
        )
    return ops


# ---------- global ----------

def _global(n: GlobalStmt, c: _Ctx) -> list[IROperation]:
    step = f"s{n.loc.line}"
    if n.kind == "macro_call":
        name = n.fields["name"].lower()
        # Auxiliares que SAS Studio añade a sus consultas (visor de resultados): no transforman datos.
        if is_studio_helper(name, set(c.macro_files)):
            return []
        return [
            c.op(
                "macro_call",
                step,
                n.loc,
                details={
                    "name": name,
                    "args": n.fields.get("args", ""),
                    "defined_in": c.macro_files.get(name),
                },
                confidence="high" if name in c.macro_files else "low",
                notes=[] if name in c.macro_files else ["Macro sin definición en el proyecto"],
            )
        ]
    if n.kind == "include":
        return [c.op("include", step, n.loc, details={"path": n.fields.get("path")})]
    # Sentencias de SAS que el propio programa usa para orquestar (%put, %sysexec, filename pipe, let con
    # medición o pausa): se registran como operaciones para que la fontanería las vea por su forma.
    if n.kind == "put":
        return [
            c.op(
                "unsupported",
                step,
                n.loc,
                details={"statement": "put", "text": n.text},
                confidence="low",
                notes=["Mensaje al log de SAS"],
            )
        ]
    if n.kind == "let" and re.search(r"datetime\(\)|\bsleep\s*\(", n.text, re.IGNORECASE):
        return [
            c.op(
                "compute",
                step,
                n.loc,
                details={"assignments": [{"target": n.fields.get("name", ""), "expression": n.text}]},
                confidence="low",
                notes=["Medición o pausa del programa (macro variable)"],
            )
        ]
    if n.kind == "sysexec" or "filename_pipe" in n.constructs or "x_command" in n.constructs or "systask" in n.constructs:
        return [
            c.op(
                "os_command",
                step,
                n.loc,
                details={"text": n.text},
                confidence="low",
                notes=["Comando del SO: mover a orquestación"],
            )
        ]
    return []


def _nodes(nodes: list[Node], c: _Ctx) -> list[IROperation]:
    ops: list[IROperation] = []
    for n in nodes:
        if isinstance(n, DataStep):
            ops += _data_step(n, c)
        elif isinstance(n, ProcStep):
            ops += _proc_step(n, c)
        elif isinstance(n, GlobalStmt):
            ops += _global(n, c)
    return ops


#: Claves que solo describen dónde está el código, no qué hace. Dos macros con el mismo cuerpo
#: en líneas distintas (copias pegadas en el programa) tienen la misma huella.
_POSITION_KEYS = frozenset({"loc", "line", "end_line", "construct_lines", "evidence"})


def _without_positions(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _without_positions(v) for k, v in value.items() if k not in _POSITION_KEYS}
    if isinstance(value, list):
        return [_without_positions(v) for v in value]
    if isinstance(value, str):
        return " ".join(value.split())
    return value


def macro_fingerprint(node: MacroDef) -> str:
    """Huella SHA-256 de parámetros y cuerpo de una macro, sin posiciones ni espacios sobrantes."""
    dumped = node.model_dump(mode="json")
    payload = _without_positions({"params": dumped["params"], "body": dumped["body"]})
    text = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _collect_macros(program: ParsedProgram, ir: ProgramIR, ctx: _Ctx) -> None:
    """Una entrada por macro distinta. Copias idénticas se colapsan; definiciones distintas con el
    mismo nombre conservan ambas, la segunda como `<nombre>_v2`, la tercera como `_v3`, etc."""
    first_by_fingerprint: dict[tuple[str, str], MacroIR] = {}
    variants: dict[str, list[MacroIR]] = {}  # casefold del nombre -> definiciones distintas
    used_names: set[str] = set()
    for node in program.nodes:
        if not isinstance(node, MacroDef):
            continue
        key = node.name.casefold()
        fingerprint = (key, macro_fingerprint(node))
        if fingerprint in first_by_fingerprint:
            original = first_by_fingerprint[fingerprint]
            original.copies += 1
            original.duplicate_lines.append(node.loc.line)
            continue
        family = variants.setdefault(key, [])
        number = len(family) + 1
        name = node.name if number == 1 else f"{node.name}_v{number}"
        while name.casefold() in used_names:
            number += 1
            name = f"{node.name}_v{number}"
        notes: list[str] = []
        if family:
            first_line = family[0].loc.line
            notes.append(
                f"Otra definición de %{node.name} con cuerpo distinto (línea {first_line}): "
                "SAS usa la última definición compilada; confirmar cuál aplica."
            )
        macro = MacroIR(
            name=name,
            params=[param.name for param in node.params],
            loc=node.loc,
            operations=_nodes(node.body, ctx),
            source_name=node.name if name != node.name else None,
            notes=notes,
        )
        used_names.add(name.casefold())
        family.append(macro)
        first_by_fingerprint[fingerprint] = macro
        ir.macros.append(macro)


def _collect_metadata(program: ParsedProgram, ir: ProgramIR, ctx: _Ctx) -> None:
    for node in program.nodes:
        if isinstance(node, GlobalStmt):
            if node.kind == "let" and node.fields:
                ir.parameters[node.fields["name"]] = node.fields["value"]
                ir.parameter_lines.setdefault(node.fields["name"], node.loc.line)
            elif node.kind == "libname" and node.fields.get("action") is None:
                schema = re.search(r"\bschema\s*=\s*([\w.]+)", node.fields.get("options", ""), re.IGNORECASE)
                ir.libraries.append(
                    LibraryRef(
                        name=node.fields["name"],
                        engine=node.fields.get("engine"),
                        path=node.fields.get("path"),
                        db_schema=schema.group(1) if schema else None,
                    )
                )
            elif node.kind == "include":
                ir.includes.append(node.fields.get("path", ""))
    _collect_macros(program, ir, ctx)


def build_ir(program: ParsedProgram, macro_files: dict[str, str] | None = None) -> ProgramIR:
    ctx = _Ctx(program.file, macro_files or {})
    ir = ProgramIR(file=program.file, sha256=program.sha256, operations=_nodes(program.nodes, ctx))
    _collect_metadata(program, ir, ctx)
    _tag_infrastructure(ir)
    fold_remote_transfers(ir)
    return ir


_SUM_STATEMENT = re.compile(r"^\s*([A-Za-z_]\w*)\s*\+\s*(.+?)\s*;?\s*$", re.DOTALL)
_WORK_REF = re.compile(r"\bwork\.(\w+)", re.IGNORECASE)
_SHELL_CATEGORIES = frozenset({"shell_auxiliar", "carga_comando"})


def _closure(macro, by_name: dict, depth: int = 0) -> list:
    """Operaciones de la macro y de las macros que llama (en el proyecto), hasta cinco niveles."""
    ops = list(macro.operations)
    if depth < 5:
        for op in macro.operations:
            callee = by_name.get(str(op.details.get("name", "")).casefold())
            if callee is not None and callee is not macro:
                ops.extend(_closure(callee, by_name, depth + 1))
    return ops


def _definition_for(call: IROperation, macros: list[MacroIR]) -> MacroIR | None:
    """SAS usa la última definición de la familia (mismo nombre, con o sin sufijo _vN) compilada antes de
    la llamada. Sin definición anterior, la primera de la familia."""
    name = str(call.details.get("name", "")).casefold()
    family = [m for m in macros if re.sub(r"_v\d+$", "", m.name.casefold()) == re.sub(r"_v\d+$", "", name)]
    if not family:
        return None
    before = [m for m in family if m.loc.line <= call.evidence.line]
    return max(before, key=lambda m: m.loc.line) if before else family[0]


def _mark_transfers(ir: ProgramIR) -> None:
    """Una macro transfiere una tabla al motor cuando su cierre ejecuta un comando de shell (la carga) y
    lee una tabla WORK. Su llamada pasa a ser una escritura hacia el motor de la librería del entorno
    (`write` con `transfer`); la macro deja de ser fontanería. Dato y motor sin nombres de script."""
    by_name = {m.name.casefold(): m for m in ir.macros}
    for macro in ir.macros:
        ops = _closure(macro, by_name)
        shell = any(
            op.type == "os_command"
            or (op.type == "infrastructure" and op.details.get("plumbing", {}).get("category") in _SHELL_CATEGORIES)
            for op in ops
        )
        if not shell:
            continue
        # La tabla entra desde fuera del cierre: si el propio cierre la produce (tabla de trabajo), no es carga.
        produced = {name.casefold() for op in ops for name in op.outputs}
        found = next(
            (
                match
                for match in _WORK_REF.finditer(" ".join(str(op.details) + " " + " ".join(op.inputs) for op in ops))
                if f"work.{match.group(1)}".casefold() not in produced
            ),
            None,
        )
        if found is not None:
            macro.transfer_table = found.group(1)
            macro.notes.append(f"Entrega la tabla WORK.{found.group(1)} a un motor externo (comando de carga)")
    for ops in [ir.operations, *(m.operations for m in ir.macros)]:
        for op in ops:
            if op.type == "macro_call":
                target = _definition_for(op, ir.macros)
                if target is not None and target.transfer_table:
                    op.type = "write"
                    op.details = {"transfer": True, "tabla_destino": target.transfer_table}
                    op.inputs = [f"work.{target.transfer_table}"]
                    op.outputs = []


def _tag_infrastructure(ir: ProgramIR) -> None:
    """Marca como `infrastructure` la fontanería de SAS (shell, espera, mensajes, tiempos, troceo, borrados
    de temporales). El motivo queda en `details["plumbing"]`; el planificador no la traduce."""
    from dataclasses import asdict

    from sas_grid_migrator.migration_planner.plumbing import macro_refs, plumbing_of, tag_structural

    # Macro variables que alguna operación usa: un call symputx que las asigna llega a datos y no es fontanería.
    everything = [op for ops_ in [ir.operations, *(m.operations for m in ir.macros)] for op in ops_]
    used = frozenset(macro_refs(everything))

    for ops in [ir.operations, *(macro.operations for macro in ir.macros)]:
        structural = tag_structural(ops, used)
        for op in ops:
            found = plumbing_of(op, used) or structural.get(id(op))
            if found is not None:
                op.type = "infrastructure"
                op.details = {**op.details, "plumbing": asdict(found)}
        # Una lectura cuyo mismo paso SAS solo contiene fontanería (p. ej. la lectura de un select count)
        # tampoco se migra: no hay nada que leer si el resultado es solo un número en el log.
        by_step: dict[str, list[IROperation]] = {}
        for op in ops:
            by_step.setdefault(op.step, []).append(op)
        for op in ops:
            siblings = [other for other in by_step[op.step] if other is not op]
            if op.type == "read" and siblings and all(other.type == "infrastructure" for other in siblings):
                op.type = "infrastructure"
                op.details = {**op.details, "plumbing": siblings[0].details["plumbing"]}
    _mark_transfers(ir)


