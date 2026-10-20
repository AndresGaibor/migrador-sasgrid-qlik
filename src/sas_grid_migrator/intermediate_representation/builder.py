"""Construye `ProgramIR` a partir de un `ParsedProgram`."""

import re
from collections import Counter

from sas_grid_migrator.intermediate_representation.models import (
    IROperation,
    LibraryRef,
    MacroIR,
    ProgramIR,
)
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
    if first and not n.inputs:
        add(
            "read_file",
            line=first.line,
            details={"statements": [s.text for s in n.statements if s.kw in ("infile", "input")]},
            confidence="medium",
        )
    if "datalines" in n.constructs:
        add("inline_data", confidence="medium", notes=["Datos incrustados en el programa"])
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
    for s in n.statements:
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
    conds = [
        {"line": s.line, "text": s.text}
        for s in n.statements
        if s.kw in ("if", "else")
        and (s.kw == "else" or re.search(r"\bthen\b", s.text, re.IGNORECASE))
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
    if {"retain", "first_last", "array", "hash"} & set(n.constructs):
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
    if "sql_implicit_join" in q.constructs:
        add(
            "join",
            inputs=srcs,
            details={"kind": "implicit", "on": q.where},
            confidence="medium",
            notes=["Join por coma: la condición está en el WHERE"],
        )
    if "sql_set_operation" in q.constructs:
        add("union", inputs=srcs, details={"text": q.text[:200]}, confidence="medium")
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
        add(
            "unsupported",
            details={"statement": q.kind, "text": q.text[:300]},
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
            details={"proc": n.name, "statements": [s.text for s in n.statements][:10]},
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
    if "x_command" in n.constructs or "systask" in n.constructs:
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


def _collect_metadata(program: ParsedProgram, ir: ProgramIR, ctx: _Ctx) -> None:
    for node in program.nodes:
        if isinstance(node, GlobalStmt):
            if node.kind == "let" and node.fields:
                ir.parameters[node.fields["name"]] = node.fields["value"]
            elif node.kind == "libname" and node.fields.get("action") is None:
                ir.libraries.append(
                    LibraryRef(
                        name=node.fields["name"],
                        engine=node.fields.get("engine"),
                        path=node.fields.get("path"),
                    )
                )
            elif node.kind == "include":
                ir.includes.append(node.fields.get("path", ""))
        elif isinstance(node, MacroDef):
            ir.macros.append(
                MacroIR(
                    name=node.name,
                    params=[param.name for param in node.params],
                    loc=node.loc,
                    operations=_nodes(node.body, ctx),
                )
            )


def build_ir(program: ParsedProgram, macro_files: dict[str, str] | None = None) -> ProgramIR:
    ctx = _Ctx(program.file, macro_files or {})
    ir = ProgramIR(file=program.file, sha256=program.sha256, operations=_nodes(program.nodes, ctx))
    _collect_metadata(program, ir, ctx)
    return ir
