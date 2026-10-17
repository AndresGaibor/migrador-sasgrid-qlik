"""Constructor de estructura: sentencias → pasos DATA/PROC, macros y sentencias globales."""

import re

from sas_grid_migrator.domain.models import Evidence, Finding, Severity
from sas_grid_migrator.sas_parser.ast import (
    DataStep,
    GlobalStmt,
    Loc,
    MacroCall,
    MacroDef,
    MacroParam,
    Node,
    ParsedProgram,
    ParseStats,
    ProcStep,
    StepStmt,
)
from sas_grid_migrator.sas_parser.datasets import dataset_list
from sas_grid_migrator.sas_parser.lexer import MACRO_KEYWORDS, Stmt, split_statements
from sas_grid_migrator.sas_parser.sql import parse_sql_statement

_KW = re.compile(r"%?[A-Za-z_]\w*")
_X_CMD = re.compile(r"^x\s+['\"%&]", re.IGNORECASE)
# Sentencias que, si aparecen con un paso abierto, lo cierran.
_STEP_CLOSERS = {"libname", "filename", "endsas", "%mend"}
# PROCs que siguen activos tras `run;` y solo terminan con `quit;`.
_QUIT_ONLY = {"sql", "datasets"}
_GLOBAL_KNOWN = {
    "option", "title", "footnote", "%put", "%global", "%local", "%symdel", "%abort", "%mend", "endsas",
    "run", "quit", "dm", "ods", "goptions", "options", "%if", "%then", "%else", "%do", "%end",
    "%goto", "%return", "%label", "%sysexec", "%window", "%display", "%input", "%copy",
}  # fmt: skip
_FUNC = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
_NOT_FUNC = {
    "keep", "drop", "rename", "where", "if", "in", "then", "do", "while", "until", "and", "or",
    "not", "set", "merge", "by", "retain", "array", "length", "format", "informat", "label",
    "else", "select", "when", "otherwise", "output", "call", "from", "as", "on", "case", "end",
    "data", "proc", "lib", "obs", "firstobs", "compress",
}  # fmt: skip
_DATE_FUNCS = {
    "intck", "intnx", "today", "date", "datepart", "timepart", "mdy", "year", "month", "day",
    "weekday", "yymmdd", "datetime", "dhms", "qtr", "yrdif", "datdif",
}  # fmt: skip
_MISSING_FUNCS = {"missing", "coalesce", "coalescec", "nmiss", "cmiss"}


def _kw(text: str) -> str:
    m = _KW.match(text)
    return m.group().lower() if m else ""


def _loc(file: str, s: Stmt, end: Stmt | None = None) -> Loc:
    return Loc(file=file, line=s.line, end_line=(end or s).end_line)


class _Ctx:
    def __init__(self, file: str):
        self.file = file
        self.findings: list[Finding] = []
        self.unrecognized = 0
        self.fragments = 0
        self.macro_depth = 0

    def unrec(self, s: Stmt) -> None:
        """Sentencia no reconocida; dentro de una macro es código generado/fragmento."""
        fragment = self.macro_depth > 0
        self.fragments += fragment
        self.unrecognized += not fragment
        self.findings.append(
            Finding(
                code="macro_fragment" if fragment else "unrecognized_statement",
                severity=Severity.INFO,
                message=s.text[:80],
                evidence=Evidence(file=self.file, line=s.line),
            )
        )


# ---------- estructura ----------


def _build(stmts: list[Stmt], ctx: _Ctx) -> list[Node]:
    nodes: list[Node] = []
    cur: list[Stmt] | None = None

    def close() -> None:
        nonlocal cur
        if cur:
            nodes.append(_make_step(cur, ctx))
        cur = None

    i = 0
    while i < len(stmts):
        s = stmts[i]
        kw = _kw(s.text)
        if kw == "%macro":
            # una definición de macro dentro de un paso abierto no lo cierra
            depth, j = 1, i + 1
            while j < len(stmts):
                k = _kw(stmts[j].text)
                depth += k == "%macro"
                depth -= k == "%mend"
                if depth == 0:
                    break
                j += 1
            if j >= len(stmts):
                ctx.findings.append(
                    Finding(
                        code="unterminated_macro",
                        severity=Severity.WARNING,
                        message=s.text[:80],
                        evidence=Evidence(file=ctx.file, line=s.line),
                    )
                )
                j = len(stmts) - 1
                body = stmts[i + 1 :]
            else:
                body = stmts[i + 1 : j]
            nodes.append(_macro_def(s, body, stmts[j] if j > i else s, ctx))
            i = j + 1
            continue
        starts_step = (kw == "data" and not s.text[4:].lstrip().startswith("=")) or kw == "proc"
        if starts_step:
            close()
            cur = [s]
            i += 1
            continue
        if cur is not None:
            closes = kw in _STEP_CLOSERS or bool(_X_CMD.match(s.text))
            if not closes:
                cur.append(s)
                head = _kw(cur[0].text)
                proc = (
                    re.match(r"proc\s+(\w+)", cur[0].text, re.IGNORECASE)
                    if head == "proc"
                    else None
                )
                quit_only = proc and proc.group(1).lower() in _QUIT_ONLY
                if kw == "quit" or (kw in ("run", "cancel") and not quit_only):
                    close()
                i += 1
                continue
            close()
        nodes.append(_global(s, ctx))
        i += 1
    close()
    return nodes


def split_args(s: str) -> list[str]:
    out, depth, q, cur = [], 0, None, []
    for ch in s:
        if q:
            q = None if ch == q else q
        elif ch in "'\"":
            q = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            out.append("".join(cur).strip())
            cur = []
            continue
        cur.append(ch)
    if "".join(cur).strip():
        out.append("".join(cur).strip())
    return out


def _macro_def(s: Stmt, body: list[Stmt], end: Stmt, ctx: _Ctx) -> MacroDef:
    m = re.match(
        r"%macro\s+([A-Za-z_]\w*)\s*(?:\((.*)\))?\s*(?:/.*)?$", s.text, re.IGNORECASE | re.DOTALL
    )
    params = []
    if m and m.group(2):
        for a in split_args(m.group(2)):
            name, eq, default = a.partition("=")
            params.append(MacroParam(name=name.strip(), default=default.strip() if eq else None))
    name = m.group(1) if m else "?"
    calls = {x.group(1).lower() for b in body for x in _PCALL.finditer(b.text)}
    ctx.macro_depth += 1
    inner = _build(body, ctx)
    ctx.macro_depth -= 1
    constructs = ["macro_def"]
    if params:
        constructs.append("macro_params")
    return MacroDef(
        loc=_loc(ctx.file, s, end),
        name=name,
        params=params,
        calls=sorted(calls - MACRO_KEYWORDS - {name.lower()}),
        body=inner,
        constructs=constructs,
    )


# ---------- sentencias globales ----------


def _global(s: Stmt, ctx: _Ctx) -> GlobalStmt:
    text, kw = s.text, _kw(s.text)
    rest = text[len(kw) :].strip()
    loc = _loc(ctx.file, s)
    g = GlobalStmt(loc=loc, kind=kw.lstrip("%") or "other", text=text[:300])

    if kw == "libname":
        m = re.match(r"(\S+)\s*(.*)$", rest, re.DOTALL)
        name, tail = (m.group(1), m.group(2)) if m else (rest, "")
        g.fields = {"name": name}
        if re.match(r"clear\b|list\b", tail, re.IGNORECASE):
            g.fields["action"] = tail.split()[0].lower()
        else:
            eng = re.match(r"([A-Za-z_]\w*)\b(?!\s*=)", tail)
            if eng:
                g.fields["engine"] = eng.group(1).lower()
            q = re.search(r"""['"]([^'"]*)['"]""", tail) or re.search(
                r"\bpath\s*=\s*(\S+)", tail, re.IGNORECASE
            )
            if q:
                g.fields["path"] = q.group(1)
            g.fields["options"] = tail
        g.constructs = ["libname"]
    elif kw == "filename":
        g.fields = {"text": rest}
        g.constructs = ["filename"] + (
            ["filename_pipe"] if re.search(r"\bpipe\b", rest, re.IGNORECASE) else []
        )
    elif kw == "%let":
        m = re.match(r"([^=\s]+)\s*=\s*(.*)$", rest, re.DOTALL)
        g.fields = {"name": m.group(1), "value": m.group(2).strip()} if m else {}
        g.constructs = ["macro_let"]
    elif kw == "%include":
        g.fields = {"path": rest}
        static = bool(re.match(r"""['"][^&%]*['"]\s*$""", rest))
        g.constructs = ["include_static" if static else "include_dynamic"]
    elif kw == "options":
        g.fields = {"text": rest}
        g.constructs = ["options"]
    elif _X_CMD.match(text) or kw == "%sysexec":
        g.kind = "x_command"
        g.constructs = ["x_command"]
    elif kw == "systask":
        g.constructs = ["systask"]
    elif kw.startswith("%") and kw[1:] not in MACRO_KEYWORDS and kw not in _GLOBAL_KNOWN:
        args = re.match(r"%\w+\s*\((.*)\)\s*$", text, re.DOTALL)
        g.kind = "macro_call"
        g.fields = {"name": kw[1:], "args": args.group(1) if args else ""}
        g.constructs = ["macro_call"]
    elif kw in ("%if", "%then", "%else", "%do", "%end", "%goto", "%return", "%label"):
        g.constructs = ["macro_control"]
    elif kw in _GLOBAL_KNOWN or kw.startswith(("title", "footnote")):
        pass
    else:
        g.kind = "other"
        ctx.unrec(s)
    if "&&" in text:
        g.constructs = [*g.constructs, "macro_indirect_reference"]
    return g


# ---------- pasos ----------


def _make_step(stmts: list[Stmt], ctx: _Ctx) -> Node:
    if _kw(stmts[0].text) == "data":
        return _data_step(stmts, ctx)
    return _proc_step(stmts, ctx)


_ASSIGN = re.compile(r"^[A-Za-z_][\w.]*(?:\[[^\]]*\]|\{[^}]*\})?\s*=(?!=)")
_FIRST_LAST = re.compile(r"\b(?:first|last)\.[A-Za-z_]\w*", re.IGNORECASE)


def _data_step(stmts: list[Stmt], ctx: _Ctx) -> DataStep:
    head = stmts[0].text[4:].strip()
    outs = dataset_list(
        head.split("/", 1)[0] if "/" in head and "(" not in head.split("/", 1)[0] else head
    )
    ds = DataStep(loc=_loc(ctx.file, stmts[0], stmts[-1]))
    cons: dict[str, int] = {}
    cur = stmts[0].line

    def add(tag: str) -> None:
        cons.setdefault(tag, cur)

    add("data_step")
    ds.outputs = [o for o in outs if o.name.lower() != "_null_"]
    if outs and not ds.outputs:
        add("data_null")
    if len(ds.outputs) > 1:
        add("multiple_outputs")
    funcs: set[str] = set()
    for s in stmts[1:]:
        cur = s.line
        t = s.text
        kw = _kw(t)
        ds.statements.append(StepStmt(line=s.line, kw=kw, text=t[:600]))
        rest = t[len(kw) :].strip()
        if kw in ("set", "merge", "update", "modify"):
            ds.input_kind = ds.input_kind or kw
            ds.inputs += dataset_list(rest)
            if kw != "set":
                add({"merge": "merge", "update": "update_stmt", "modify": "modify_stmt"}[kw])
            if len(ds.inputs) > 1 and kw == "set":
                add("set_concatenate")
        elif kw == "by":
            ds.by += rest.split()
        elif kw == "where":
            ds.where.append(rest)
        elif kw in ("if", "else"):
            ds.n_conditionals += 1
            if kw == "if" and not re.search(r"\bthen\b", rest, re.IGNORECASE):
                ds.subsetting_if.append(rest)
        elif kw in ("keep", "drop", "rename", "retain"):
            getattr(ds, kw).append(rest)
            if kw == "retain":
                add("retain")
        elif kw == "array":
            ds.arrays.append(rest)
            add("array")
        elif kw in ("infile", "input", "datalines", "cards", "<datalines>"):
            add("infile_input" if kw in ("infile", "input") else "datalines")
        elif kw == "file":
            add("file_output")
        elif kw == "output":
            add("explicit_output")
        elif kw == "call":
            low = rest.lower()
            if low.startswith("execute"):
                add("call_execute")
            elif low.startswith("symput"):
                add("call_symput")
            else:
                add("call_routine")
        elif kw in ("declare", "dcl") and "hash" in rest.lower():
            add("hash")
        elif _ASSIGN.match(t) or re.match(r"^[A-Za-z_]\w*\s*\+", t):
            ds.n_assignments += 1
        here = {f.lower() for f in _FUNC.findall(t)} - _NOT_FUNC
        funcs |= here
        if _FIRST_LAST.search(t):
            add("first_last")
        if here & _DATE_FUNCS:
            add("date_functions")
        if here & _MISSING_FUNCS:
            add("missing_handling")
        if here & {"put", "input"}:
            add("format_conversion")
        if "&&" in t:
            add("macro_indirect_reference")
    ds.functions = sorted(funcs)
    ds.constructs = sorted(cons)
    ds.construct_lines = cons
    return ds


_OPT_DS = re.compile(
    r"\b(data|out|outfile|datafile)\s*=\s*('[^']*'|\"[^\"]*\"|[^\s;()]+(?:\([^)]*\))?)",
    re.IGNORECASE,
)


def _proc_step(stmts: list[Stmt], ctx: _Ctx) -> ProcStep:
    m = re.match(r"proc\s+(\w+)\s*(.*)$", stmts[0].text, re.IGNORECASE | re.DOTALL)
    name = m.group(1).lower() if m else "?"
    ps = ProcStep(
        loc=_loc(ctx.file, stmts[0], stmts[-1]), name=name, options=m.group(2).strip() if m else ""
    )
    ps.constructs = [f"proc:{name}"]
    ps.statements = [
        StepStmt(line=s.line, kw=_kw(s.text), text=s.text[:600])
        for s in stmts[1:]
        if s.text != "<datalines>"
    ]
    cons: set[str] = set(ps.constructs)

    def opt_refs(text: str) -> None:
        for key, val in _OPT_DS.findall(text):
            if key.lower() in ("outfile", "datafile"):
                ps.fields[key.lower()] = val.strip("'\"")
                cons.add("external_file_io")
            elif key.lower() == "data":
                ps.inputs += dataset_list(val)
            else:
                ps.outputs += dataset_list(val)

    opt_refs(ps.options)
    for s in stmts[1:]:
        kw = _kw(s.text)
        rest = s.text[len(kw) :].strip()
        if kw == "by":
            ps.by += rest.split()
        elif kw in ("output", "out") or (
            kw not in ("var", "class", "model", "tables", "table") and "out=" in rest.lower()
        ):
            opt_refs(rest)
    if name == "sql":
        for s in stmts[1:]:
            q = parse_sql_statement(s.text, _loc(ctx.file, s))
            if q:
                ps.queries.append(q)
                cons.update(q.constructs)
                ps.inputs += q.sources
                if q.target and q.kind in ("create_table", "create_view", "insert_into"):
                    ps.outputs.append(q.target)
    if any("&&" in s.text for s in stmts):
        cons.add("macro_indirect_reference")
    ps.constructs = sorted(cons)
    return ps


# ---------- programa ----------

_PCALL = re.compile(r"%([A-Za-z_]\w*)")


def parse_program(text: str, file: str, sha256: str | None = None) -> ParsedProgram:
    stmts = split_statements(text)
    ctx = _Ctx(file)
    nodes = _build(stmts, ctx)
    calls: list[MacroCall] = []
    seen: set[tuple[str, int]] = set()
    for s in stmts:
        for m in _PCALL.finditer(s.text):
            n = m.group(1).lower()
            if n not in MACRO_KEYWORDS and (n, s.line) not in seen:
                seen.add((n, s.line))
                calls.append(MacroCall(name=n, line=s.line))
    return ParsedProgram(
        file=file,
        sha256=sha256,
        nodes=nodes,
        macro_calls=calls,
        findings=ctx.findings,
        stats=ParseStats(
            statements=len(stmts), unrecognized=ctx.unrecognized, fragments=ctx.fragments
        ),
    )
