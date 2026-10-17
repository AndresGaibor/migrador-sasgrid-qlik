"""Lectura de listas de datasets SAS: `lib.nombre(opciones) otro nombre2(...)`."""

import re

from sas_grid_migrator.sas_parser.ast import DatasetRef

_IN_VAR = re.compile(r"\bin\s*=\s*([A-Za-z_]\w*)", re.IGNORECASE)


def _balanced(s: str, i: int) -> int:
    """Índice tras el ')' que cierra el '(' en s[i]."""
    depth = 0
    q = None
    while i < len(s):
        c = s[i]
        if q:
            q = None if c == q else q
        elif c in "'\"":
            q = c
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return i


def make_ref(token: str, options: str | None = None) -> DatasetRef:
    dynamic = "&" in token or "%" in token
    lib, _, name = ("", "", token) if dynamic else token.rpartition(".")
    m = _IN_VAR.search(options) if options else None
    return DatasetRef(
        raw=token,
        lib=lib or None,
        name=name or token,
        dynamic=dynamic,
        options=options,
        in_var=m.group(1) if m else None,
    )


def dataset_list(s: str) -> list[DatasetRef]:
    """Datasets de una lista; se detiene en '/'. Ignora `opcion=valor` (nobs=, end=, key=)."""
    out: list[DatasetRef] = []
    i, n = 0, len(s)
    while i < n:
        if s[i].isspace():
            i += 1
        elif s[i] == "/":
            break
        else:
            m = re.compile(r"[^\s(/=]+").match(s, i)
            if not m:
                i += 1
                continue
            token, j = m.group(), m.end()
            k = j
            while k < n and s[k].isspace():
                k += 1
            if k < n and s[k] == "=":  # opcion=valor
                k += 1
                while k < n and s[k].isspace():
                    k += 1
                v = re.compile(r"[^\s(]+").match(s, k)
                i = v.end() if v else k
                continue
            opts = None
            if k < n and s[k] == "(":
                end = _balanced(s, k)
                opts = s[k + 1 : end - 1].strip()
                j = end
            out.append(make_ref(token, opts))
            i = j
    return out
