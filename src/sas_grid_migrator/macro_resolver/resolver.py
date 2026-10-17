"""Resolución estática: índice de macros, constantes `%LET` de primer nivel y rutas de %INCLUDE.

No expande macros. Lo que no se puede resolver con certeza queda sin resolver (nunca se adivina).
"""

import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import PurePosixPath

from sas_grid_migrator.sas_parser.ast import GlobalStmt, MacroDef, Node, ParsedProgram

_VAR = re.compile(r"&([A-Za-z_]\w*)\.?")
_QUOTED = re.compile(r"""^\s*(['"])(.*?)\1""", re.DOTALL)


def walk(nodes: list[Node]) -> Iterator[Node]:
    """Todos los nodos, entrando en cuerpos de macro."""
    for n in nodes:
        yield n
        if isinstance(n, MacroDef):
            yield from walk(n.body)


def macro_index(programs: list[ParsedProgram]) -> dict[str, list[tuple[str, MacroDef]]]:
    idx: dict[str, list[tuple[str, MacroDef]]] = {}
    for p in programs:
        for n in walk(p.nodes):
            if isinstance(n, MacroDef):
                idx.setdefault(n.name.lower(), []).append((p.file, n))
    return idx


def constant_vars(programs: list[ParsedProgram]) -> dict[str, str]:
    """`%let x = literal;` de primer nivel con un único valor en todo el proyecto."""
    seen: dict[str, set[str]] = {}
    for p in programs:
        for n in p.nodes:
            if isinstance(n, GlobalStmt) and n.kind == "let" and n.fields:
                v = n.fields["value"].strip().strip("'\"")
                if not re.search(r"[&%]", v):
                    seen.setdefault(n.fields["name"].lower(), set()).add(v)
    return {k: next(iter(v)) for k, v in seen.items() if len(v) == 1}


def substitute(text: str, variables: dict[str, str]) -> tuple[str, bool]:
    """Sustituye `&var`/`&var.` conocidas. Devuelve (texto, completo)."""
    complete = "&&" not in text

    def rep(m: re.Match) -> str:
        nonlocal complete
        v = variables.get(m.group(1).lower())
        if v is None:
            complete = False
            return m.group(0)
        return v

    res = _VAR.sub(rep, text)
    return res, complete and "&" not in res


def first_quoted(s: str) -> str | None:
    m = _QUOTED.match(s)
    return m.group(2) if m else None


@dataclass(frozen=True)
class PathMatch:
    status: str  # resolved | candidate | ambiguous | external
    file: str | None = None


class PathIndex:
    """Archivos del proyecto indexados por nombre (minúsculas): evita recorrerlos todos por cada ruta."""

    def __init__(self, files: Iterable[str]):
        self.by_name: dict[str, list[tuple[str, list[str]]]] = {}
        for f in files:
            parts = [c.lower() for c in PurePosixPath(f).parts]
            if parts:
                self.by_name.setdefault(parts[-1], []).append((f, parts))


def resolve_path(raw: str, files: "Iterable[str] | PathIndex") -> PathMatch:
    """Casa una ruta de `%include`/programa con un archivo del proyecto por sufijo de ruta.

    resolved: coinciden ≥2 componentes (o todos los de una ruta corta).
    candidate: solo coincide el nombre de archivo (no se enlaza; se informa).
    """
    want = [c.lower() for c in PurePosixPath(raw.replace("\\", "/")).parts if c not in ("/", ".")]
    if not want:
        return PathMatch("external")
    index = files if isinstance(files, PathIndex) else PathIndex(files)
    best, best_len, tie = None, 0, False
    for f, have in index.by_name.get(want[-1], ()):
        n = 0
        while n < min(len(want), len(have)) and want[-1 - n] == have[-1 - n]:
            n += 1
        if n > best_len:
            best, best_len, tie = f, n, False
        elif n == best_len and n > 0:
            tie = True
    if not best_len:
        return PathMatch("external")
    if tie:
        return PathMatch("ambiguous")
    if best_len >= 2 or len(want) == 1 or best_len == len(want):
        return PathMatch("resolved", best)
    return PathMatch("candidate", best)
