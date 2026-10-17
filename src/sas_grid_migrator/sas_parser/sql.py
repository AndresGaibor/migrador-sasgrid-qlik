"""Análisis de sentencias de PROC SQL a nivel de cláusulas (no gramática SQL completa)."""

import re

from sas_grid_migrator.sas_parser.ast import DatasetRef, Loc, SqlJoin, SqlQuery
from sas_grid_migrator.sas_parser.datasets import _balanced, make_ref

_SET_OPS = re.compile(r"\b(outer\s+union|union(?:\s+all)?|intersect|except)\b", re.IGNORECASE)
_CLAUSES = re.compile(r"\b(select|from|where|group\s+by|having|order\s+by)\b", re.IGNORECASE)
_JOIN = re.compile(
    r"\b((?:natural\s+)?(?:(?:inner|left|right|full|cross)\s+)?(?:outer\s+)?join)\b", re.IGNORECASE
)
_ON = re.compile(r"\b(on|using)\b", re.IGNORECASE)
_TABLE = re.compile(
    r"([^\s(),]+)\s*(\(.*\))?\s*(?:as\s+)?([A-Za-z_]\w*)?\s*$", re.IGNORECASE | re.DOTALL
)
_AGG = re.compile(r"\b(count|sum|avg|mean|min|max|std|var)\s*\(", re.IGNORECASE)
_RESERVED_ALIAS = {
    "where",
    "group",
    "order",
    "having",
    "on",
    "using",
    "inner",
    "left",
    "right",
    "full",
}


def _mask(t: str) -> str:
    """Misma longitud; contenido de cadenas y de paréntesis anidados → '_'."""
    out, depth, q = [], 0, None
    for ch in t:
        if q:
            out.append("_")
            q = None if ch == q else q
        elif ch in "'\"":
            q = ch
            out.append("_")
        elif ch == "(":
            out.append("(" if depth == 0 else "_")
            depth += 1
        elif ch == ")":
            depth = max(depth - 1, 0)
            out.append(")" if depth == 0 else "_")
        else:
            out.append(ch if depth == 0 else "_")
    return "".join(out)


def _nested_selects(s: str) -> list[str]:
    """Textos internos de subconsultas `(select ...)` de primer nivel en `s`."""
    out, i = [], 0
    m = _mask(s)
    while True:
        k = re.compile(r"\(\s*select\b", re.IGNORECASE).search(s, i)
        if not k:
            return out
        if m[k.start()] != "(":  # anidada dentro de otra: ya la verá la recursión
            i = k.end()
            continue
        end = _balanced(s, k.start())
        out.append(s[k.start() + 1 : end - 1])
        i = end


class _Select:
    def __init__(self) -> None:
        self.sources: list[DatasetRef] = []
        self.joins: list[SqlJoin] = []
        self.constructs: set[str] = set()
        self.select_list = ""
        self.distinct = False
        self.into: list[str] = []
        self.where = self.group_by = self.having = self.order_by = None


def _table_spec(spec: str, sel: _Select) -> DatasetRef | None:
    spec = spec.strip()
    if spec.startswith("("):
        end = _balanced(spec, 0)
        _parse_select(spec[1 : end - 1], sel, nested=True)
        sel.constructs.add("sql_subquery")
        return None
    if re.match(r"connection\s+to\b", spec, re.IGNORECASE):
        sel.constructs.add("sql_passthrough")
        return None
    m = _TABLE.match(spec)
    if not m:
        return None
    ref = make_ref(m.group(1), m.group(2)[1:-1].strip() if m.group(2) else None)
    alias = m.group(3)
    ref.alias = alias if alias and alias.lower() not in _RESERVED_ALIAS else None
    return ref


def _parse_from(fc: str, sel: _Select) -> None:
    masked = _mask(fc)
    cuts = sorted(
        [(m.start(), m.end(), "join", m.group(1).lower()) for m in _JOIN.finditer(masked)]
        + [(m.start(), m.end(), "comma", ",") for m in re.finditer(",", masked)]
    )
    pieces, pos, kind = [], 0, "from"
    for s, e, ctype, text in cuts:
        pieces.append((kind, fc[pos:s]))
        pos, kind = e, (" ".join(text.split()) if ctype == "join" else "comma")
        if ctype == "comma":
            sel.constructs.add("sql_implicit_join")
    pieces.append((kind, fc[pos:]))
    for kind, piece in pieces:
        on = None
        mm = _mask(piece)
        m_on = _ON.search(mm)
        if m_on:
            piece, on = piece[: m_on.start()], piece[m_on.start() :].strip()
        ref = _table_spec(piece, sel)
        if kind not in ("from", "comma"):
            sel.joins.append(SqlJoin(kind=kind, table=ref, on=on))
            sel.constructs.add("sql_join")
            if re.search(r"left|right|full", kind):
                sel.constructs.add("sql_outer_join")
        if ref:
            sel.sources.append(ref)


def _parse_select(text: str, sel: _Select, nested: bool = False) -> None:
    masked = _mask(text)
    cuts = [(m.start(), m.end()) for m in _SET_OPS.finditer(masked)]
    if cuts:
        sel.constructs.add("sql_set_operation")
    bounds = [0] + [x for c in cuts for x in c] + [len(text)]
    segments = [text[bounds[i] : bounds[i + 1]] for i in range(0, len(bounds), 2)]
    for seg in segments:
        _parse_segment(seg, sel, nested)


def _parse_segment(seg: str, sel: _Select, nested: bool) -> None:
    masked = _mask(seg)
    pos: dict[str, tuple[int, int]] = {}
    for m in _CLAUSES.finditer(masked):
        pos.setdefault(" ".join(m.group(1).lower().split()), (m.start(), m.end()))
    order = sorted((s, e, k) for k, (s, e) in pos.items())

    def clause(name: str) -> str | None:
        for idx, (_, e, k) in enumerate(order):
            if k == name:
                nxt = order[idx + 1][0] if idx + 1 < len(order) else len(seg)
                return seg[e:nxt].strip()
        return None

    sl = clause("select")
    if sl is not None:
        if not nested and not sel.select_list:
            sel.distinct = bool(re.match(r"distinct\b", sl, re.IGNORECASE))
            into = re.search(r"\binto\s+(:[^,]+(?:,\s*:[^,]+)*)", sl, re.IGNORECASE)
            if into:
                sel.into = [v.strip().lstrip(":") for v in into.group(1).split(",")]
                sel.constructs.add("sql_into_macro")
                sl = sl[: into.start()].strip()
            sel.select_list = sl
        if re.search(r"\bcalculated\b", sl, re.IGNORECASE):
            sel.constructs.add("sql_calculated")
    if re.search(r"\bcalculated\b", seg, re.IGNORECASE):
        sel.constructs.add("sql_calculated")
    fc = clause("from")
    if fc:
        _parse_from(fc, sel)
    for name, attr in (
        ("where", "where"),
        ("group by", "group_by"),
        ("having", "having"),
        ("order by", "order_by"),
    ):
        c = clause(name)
        if c and not nested and getattr(sel, attr) is None:
            setattr(sel, attr, c)
        if c and name == "group by":
            sel.constructs.add("sql_group_by")
    for part in (sl or "", clause("where") or "", clause("having") or ""):
        for inner in _nested_selects(part):
            sel.constructs.add("sql_subquery")
            _parse_select(inner, sel, nested=True)
    if sl and _AGG.search(sl):
        sel.constructs.add("sql_aggregate")


_DDL = re.compile(
    r"^(create\s+(?:table|view)|insert\s+into|delete\s+from|update)\s+([^\s(]+)(.*)$",
    re.IGNORECASE | re.DOTALL,
)


def parse_sql_statement(text: str, loc: Loc) -> SqlQuery | None:
    t = " ".join(text.split())
    low = t.lower()
    first = low.split(" ", 1)[0]
    if first in ("reset", "validate", "quit", "describe") or low.startswith("%"):
        return None
    sel = _Select()
    kind, target = first, None
    if re.match(r"(connect|disconnect|execute)\b", low):
        sel.constructs.add("sql_passthrough")
        kind = first
    elif m := _DDL.match(t):
        kind = " ".join(m.group(1).lower().split()).replace(" ", "_")
        target = make_ref(m.group(2))
        rest = m.group(3).strip()
        mm = re.search(r"\bselect\b", rest, re.IGNORECASE)
        if mm and kind in ("create_table", "create_view", "insert_into"):
            _parse_select(rest[mm.start() :], sel)
        elif kind == "create_table" and re.match(r"like\s+(\S+)", rest, re.IGNORECASE):
            sel.sources.append(make_ref(rest.split()[1]))
        elif kind in ("delete_from", "update"):
            wm = re.search(r"\bwhere\b(.*)$", rest, re.IGNORECASE)
            sel.where = wm.group(1).strip() if wm else None
        if kind in ("delete_from", "update", "insert_into"):
            sel.constructs.add(f"sql_{kind}")
    elif first == "select":
        _parse_select(t, sel)
    elif first in ("drop", "alter"):
        kind = first
        sel.constructs.add(f"sql_{first}")
    else:
        kind = "other"
    return SqlQuery(
        kind=kind,
        target=target,
        select_list=sel.select_list or None,
        distinct=sel.distinct,
        sources=sel.sources,
        joins=sel.joins,
        where=sel.where,
        group_by=sel.group_by,
        having=sel.having,
        order_by=sel.order_by,
        into=sel.into,
        text=t,
        loc=loc,
        constructs=sorted(sel.constructs),
    )
