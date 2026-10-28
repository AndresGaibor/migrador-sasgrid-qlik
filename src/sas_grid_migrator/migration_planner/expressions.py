"""Traducción conservadora de condiciones y expresiones SAS a Java (sintaxis de Talend).

Solo cubre un subconjunto seguro (comparaciones, AND/OR/NOT, aritmética, literales, funciones
de texto simples). Todo lo demás devuelve `talend=None`: no se inventa una traducción.
Cada resultado debe validarse semánticamente (missing, mayúsculas, tipos).
"""

import re
from dataclasses import dataclass, field


@dataclass
class Translation:
    sas: str
    talend: str | None = None
    columns: list[str] = field(default_factory=list)
    simple: list[dict] | None = None  # condiciones tFilterRow (modo simple)
    logical: str | None = None  # "&&" | "||" para el modo simple
    warnings: list[str] = field(default_factory=list)


class _Unsupported(Exception):
    pass


_TOKEN = re.compile(
    r"""\s*(?:
    (?P<str>'(?:[^']|'')*'|"(?:[^"]|"")*")
    |(?P<num>\d+(?:\.\d+)?)
    |(?P<mvar>&[A-Za-z_]\w*\.?)
    |(?P<op>\^=|~=|<>|>=|<=|\|\||=|>|<|\+|-|\*|/|\(|\)|,|&|\|)
    |(?P<id>[A-Za-z_][\w]*(?:\.[A-Za-z_]\w*)?)
    )""",
    re.VERBOSE,
)
_ARITHMETIC_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[()+*/-]")
_CMP = {"=": "==", "eq": "==", "^=": "!=", "~=": "!=", "<>": "!=", "ne": "!=", ">": ">", "gt": ">",
        "<": "<", "lt": "<", ">=": ">=", "ge": ">=", "<=": "<=", "le": "<="}  # fmt: skip
_FUNCS = {
    "upcase": "{0}.toUpperCase()",
    "lowcase": "{0}.toLowerCase()",
    "strip": "{0}.trim()",
    "trim": "{0}.trim()",
}


def _tokens(s: str) -> list[tuple[str, str]]:
    out, pos = [], 0
    s = s.strip()
    while pos < len(s):
        m = _TOKEN.match(s, pos)
        if not m or m.end() == pos:
            raise _Unsupported(f"token no soportado: {s[pos : pos + 12]!r}")
        kind = m.lastgroup or ""
        out.append((kind, m.group(kind)))
        pos = m.end()
    return out


class _Parser:
    def __init__(self, toks: list[tuple[str, str]]):
        self.t, self.i = toks, 0
        self.cols: list[str] = []
        self.warnings: list[str] = []
        self.simple: list[dict] = []
        self.ops: set[str] = set()

    def peek(self) -> tuple[str, str]:
        return self.t[self.i] if self.i < len(self.t) else ("end", "")

    def take(self) -> tuple[str, str]:
        tok = self.peek()
        self.i += 1
        return tok

    def is_word(self, w: str) -> bool:
        k, v = self.peek()
        return k == "id" and v.lower() == w

    # lógica
    def expr(self) -> str:
        left = self.and_()
        while self.is_word("or") or self.peek()[1] == "|":
            self.take()
            self.ops.add("||")
            left = f"({left} || {self.and_()})"
        return left

    def and_(self) -> str:
        left = self.not_()
        while self.is_word("and") or self.peek()[1] == "&":
            self.take()
            self.ops.add("&&")
            left = f"({left} && {self.not_()})"
        return left

    def not_(self) -> str:
        if self.is_word("not") or self.peek()[1] in ("^", "~"):
            self.take()
            self.ops.add("!")
            return f"!({self.not_()})"
        return self.cmp()

    def cmp(self) -> str:
        left_start = self.i
        left = self.arith()
        k, v = self.peek()
        op = _CMP.get(v.lower()) if k in ("op", "id") else None
        if self.is_word("in"):
            self.take()
            if self.take()[1] != "(":
                raise _Unsupported("IN sin paréntesis")
            vals = [self.arith()]
            while self.peek()[1] in (",",) or self.peek()[0] in ("str", "num"):
                if self.peek()[1] == ",":
                    self.take()
                vals.append(self.arith())
            if self.take()[1] != ")":
                raise _Unsupported("IN sin cierre")
            self.ops.add("in")
            if re.fullmatch(r"input_row\.\w+", left):
                if any(re.fullmatch(r"input_row\.\w+", value) for value in vals):
                    raise _Unsupported("IN entre columnas sin tipos confirmados")
                if any(value.startswith('"') for value in vals):
                    self.warnings.append("IN textual: validar semántica de missing/nulos antes de promover")
            return (
                "("
                + " || ".join(
                    f"{left}.equals({x})" if x.startswith('"') else f"{left} == {x}" for x in vals
                )
                + ")"
            )
        if op is None:
            return left
        self.take()
        right = self.arith()
        left_column = re.fullmatch(r"input_row\.\w+", left)
        right_column = re.fullmatch(r"input_row\.\w+", right)
        if op in ("==", "!=") and left_column and right_column:
            raise _Unsupported("igualdad entre columnas sin tipos confirmados")
        if op in ("==", "!=") and (
            (left_column and right.startswith('"')) or (right_column and left.startswith('"'))
        ):
            self.warnings.append("Comparación textual: validar semántica de missing/nulos antes de promover")
        if (
            len(self.t)
            and self.i - left_start == 3
            and self.t[left_start][0] == "id"
            and self.t[left_start + 2][0] in ("str", "num", "mvar")
        ):
            self.simple.append(
                {
                    "column": self.t[left_start][1],
                    "operator": op,
                    "value": self.t[left_start + 2][1],
                }
            )
        else:
            self.simple.append({})  # no representable en modo simple
        if op in ("<", "<=", "!="):
            self.warnings.append(
                "Missing numérico: en SAS es menor que cualquier número; en Java un null no compara igual"
            )
        if op in ("==", "!=") and (right.startswith('"') or left.startswith('"')):
            s, o = (right, left) if right.startswith('"') else (left, right)
            return f"{'!' if op == '!=' else ''}{o}.equals({s})"
        return f"({left} {op} {right})"

    # aritmética
    def arith(self) -> str:
        left = self.term()
        while self.peek()[1] in ("+", "-", "||"):
            op = self.take()[1]
            right = self.term()
            left = f"({left} {'+' if op == '||' else op} {right})"
        return left

    def term(self) -> str:
        left = self.atom()
        while self.peek()[1] in ("*", "/"):
            op = self.take()[1]
            left = f"({left} {op} {self.atom()})"
        return left

    def atom(self) -> str:
        k, v = self.take()
        if k == "str":
            body = v[1:-1].replace(v[0] * 2, v[0]).replace("\\", "\\\\").replace('"', '\\"')
            return f'"{body}"'
        if k == "num":
            return v
        if k == "mvar":
            name = v.lstrip("&").rstrip(".")
            self.warnings.append(
                f"Macrovariable &{name} → context.{name} (crear variable de contexto)"
            )
            return f"context.{name}"
        if k == "op" and v == "(":
            e = self.expr()
            if self.take()[1] != ")":
                raise _Unsupported("paréntesis sin cerrar")
            return f"({e})"
        if k == "op" and v == "-":
            return f"-{self.atom()}"
        if k == "id":
            if self.peek()[1] == "(":
                name = v.lower()
                if name == "missing":
                    self.take()
                    arg = self.expr()
                    if self.take()[1] != ")":
                        raise _Unsupported("missing(")
                    self.warnings.append("missing(): null (y cadena vacía si es texto) en Java")
                    return f"({arg} == null)"
                if name not in _FUNCS:
                    raise _Unsupported(f"función {v}")
                self.take()
                arg = self.expr()
                if self.take()[1] != ")":
                    raise _Unsupported(f"{v}(")
                self.warnings.append(f"{v}(): comprobar nulos antes de invocar el método")
                return _FUNCS[name].format(arg)
            if v == "." or v.lower() in ("and", "or", "not", "in"):
                raise _Unsupported(f"palabra {v}")
            col = v.split(".")[-1]
            self.cols.append(col)
            return f"input_row.{col}"
        raise _Unsupported(f"inesperado: {v!r}")


def translate(sas: str) -> Translation:
    """Traduce una condición o expresión SAS; `talend=None` si no es seguro."""
    t = Translation(sas=sas)
    s = re.sub(r"\s+", " ", sas).strip()
    if re.search(r"\bis\s+(not\s+)?missing\b|\bcalculated\b", s, re.IGNORECASE):
        t.warnings.append("Construcción SAS sin traducción automática")
        return t
    try:
        p = _Parser(_tokens(s))
        java = p.expr()
        if p.i != len(p.t):
            raise _Unsupported("texto sobrante")
    except _Unsupported as e:
        t.warnings.append(f"Sin traducción automática: {e}")
        return t
    t.talend = java
    t.columns = sorted(set(p.cols))
    t.warnings = sorted(set(p.warnings))
    if p.simple and all(p.simple) and len(p.ops) <= 1 and p.ops <= {"&&", "||"}:
        t.simple = p.simple
        t.logical = next(iter(p.ops), "&&")
    return t


def is_simple_arithmetic_translation(expression: str | None) -> bool:
    """Indica si la traducción solo contiene columnas, números y aritmética básica."""
    if not expression:
        return False
    tokens = _ARITHMETIC_TOKEN.findall(expression)
    if not tokens or "".join(tokens) != re.sub(r"\s+", "", expression):
        return False

    expecting_value = True
    depth = 0
    for token in tokens:
        if token == "(":
            if not expecting_value:
                return False
            depth += 1
            continue
        if token == ")":
            if expecting_value or depth == 0:
                return False
            depth -= 1
            expecting_value = False
            continue
        if token in {"+", "-", "*", "/"}:
            if token in {"+", "-"} and expecting_value:
                continue
            if expecting_value:
                return False
            expecting_value = True
            continue
        if not expecting_value:
            return False
        expecting_value = False
    return not expecting_value and depth == 0
