"""Traductor de expresiones SAS a Java de Talend apoyado en la rutina `SasFunctions`.

El traductor en línea de `expressions.py` emite Java suelto y se rinde ante cualquier comparación con una columna de tipo
desconocido. Este motor separa dos responsabilidades, como hacen los conversores profesionales:

- **Gramática completa**: funciones de varios argumentos, `CASE WHEN`, `IN`, `BETWEEN`, `IS [NOT] MISSING`, `LIKE`,
  el literal `.` de valor perdido, formatos (`date9.`), literales de fecha (`'01JAN2020'd`) y nombres entre comillas.
- **Semántica en una biblioteca de ejecución** (`rules/talend/routines/SasFunctions.java`, una rutina de Talend): cada
  operador y cada función SAS se traduce a una llamada `SasFunctions.<nombre>(...)`. Los valores perdidos (null), el
  orden de los perdidos, la concatenación y la época de fechas (1960) se resuelven ahí una vez, no en cada expresión.

Lo que no se puede traducir con seguridad (`lag`, funciones sin equivalente) lanza `Unsupported` y queda como pendiente.
"""

import re

MASK_UNSUPPORTED = {"lag", "dif", "call", "put_dynamic"}

#: Función SAS → método de `SasFunctions`. Las que no cambian de nombre se listan con el mismo.
FUNCTIONS: dict[str, str] = {
    "abs": "abs", "ceil": "ceil", "floor": "floor", "int": "intFn", "round": "round", "sqrt": "sqrt", "exp": "exp",
    "log": "log", "log10": "log10", "mod": "mod", "sign": "sign",
    "max": "max", "min": "min", "sum": "sum", "mean": "mean", "n": "n", "nmiss": "nmiss", "coalesce": "coalesce",
    "coalescec": "coalesce", "ifn": "ifv", "ifc": "ifv", "missing": "isMissing",
    "cat": "cat", "cats": "cats", "catt": "catt", "catx": "catx", "trim": "trim", "strip": "strip", "left": "left",
    "right": "right", "upcase": "upcase", "lowcase": "lowcase", "propcase": "propcase", "length": "length",
    "lengthc": "length", "lengthn": "length", "compbl": "compbl", "compress": "compress", "tranwrd": "tranwrd",
    "translate": "translate", "reverse": "reverse", "substr": "substr", "substrn": "substr", "scan": "scan",
    "index": "index", "indexc": "indexc", "indexw": "index", "find": "find", "countw": "countw", "count": "count",
    "input": "input", "inputn": "input", "inputc": "input", "put": "put", "putn": "put", "putc": "put",
    "prxchange": "prxchange", "prxmatch": "prxmatch",
    "mdy": "mdy", "year": "year", "month": "month", "day": "day", "qtr": "qtr", "weekday": "weekday",
    "today": "today", "date": "today", "datetime": "datetime", "datepart": "datepart", "timepart": "timepart",
    "intnx": "intnx", "intck": "intck", "yrdif": "yrdif", "datdif": "datdif", "dhms": "dhms", "hms": "hms",
    "constant": "constant", "rand": "rand", "ranuni": "rand", "uuidgen": "uuid",
}
_FORMAT_ARGS = {"input", "inputn", "inputc", "put", "putn", "putc"}
_CMP = {"=": "eq", "eq": "eq", "^=": "ne", "~=": "ne", "¬=": "ne", "ne": "ne", "<>": "ne", ">": "gt", "gt": "gt",
        "<": "lt", "lt": "lt", ">=": "ge", "ge": "ge", "<=": "le", "le": "le"}  # fmt: skip

_TOKEN = re.compile(
    r"""\s*(?:
    (?P<datelit>'[0-9]{1,2}[A-Za-z]{3}[0-9]{2,4}'[dD])
    |(?P<name>(?:[A-Za-z_]\w*\.)?'[^']+'[nN])
    |(?P<str>'(?:[^']|'')*'|"(?:[^"]|"")*")
    |(?P<fmt>(?:\$?[A-Za-z_]+\d*\.\d*|\$\d+\.\d*)(?![\w]))
    |(?P<num>\d+\.?\d*(?:[eE][+-]?\d+)?|\.\d+)
    |(?P<mvar>&+[A-Za-z_]\w*\.?)
    |(?P<op>\*\*|\^=|~=|¬=|<>|>=|<=|\|\||!!|=|>|<|\+|-|\*|/|\(|\)|,|&|\||\^|~|¬|\.)
    |(?P<id>[A-Za-z_À-ɏ][\wÀ-ɏ]*(?:\.[A-Za-z_À-ɏ][\wÀ-ɏ]*)?)
    )""",
    re.VERBOSE,
)


class Unsupported(Exception):
    pass


class Result:
    def __init__(self, java: str, columns: list[str], warnings: list[str]):
        self.java, self.columns, self.warnings = java, columns, warnings


def _tokens(text: str) -> list[tuple[str, str]]:
    out, pos = [], 0
    text = text.strip()
    while pos < len(text):
        m = _TOKEN.match(text, pos)
        if not m or m.end() == pos:
            raise Unsupported(f"token no soportado: {text[pos : pos + 12]!r}")
        kind = m.lastgroup or ""
        out.append((kind, m.group(kind)))
        pos = m.end()
    return out


def _java_string(raw: str) -> str:
    body = raw[1:-1].replace(raw[0] * 2, raw[0]).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{body}"'


class _P:
    def __init__(self, tokens: list[tuple[str, str]]):
        self.t, self.i = tokens, 0
        self.cols: list[str] = []
        self.warnings: set[str] = set()

    def peek(self, offset: int = 0) -> tuple[str, str]:
        j = self.i + offset
        return self.t[j] if j < len(self.t) else ("end", "")

    def take(self) -> tuple[str, str]:
        tok = self.peek()
        self.i += 1
        return tok

    def word(self, w: str, offset: int = 0) -> bool:
        k, v = self.peek(offset)
        return k == "id" and v.lower() == w

    def expect(self, value: str) -> None:
        if self.take()[1] != value:
            raise Unsupported(f"se esperaba {value!r}")

    # ---- lógica
    def expr(self) -> str:
        left = self.and_()
        while self.word("or") or self.peek()[1] in ("|", "!"):
            self.take()
            left = f"({self.truthy(left)} || {self.truthy(self.and_())})"
        return left

    def and_(self) -> str:
        left = self.not_()
        while self.word("and") or self.peek()[1] == "&":
            self.take()
            left = f"({self.truthy(left)} && {self.truthy(self.not_())})"
        return left

    def not_(self) -> str:
        if self.word("not") or self.peek()[1] in ("^", "~", "¬"):
            self.take()
            return f"(!{self.truthy(self.not_())})"
        return self.cmp()

    @staticmethod
    def truthy(java: str) -> str:
        return java if java.startswith(("SasFunctions.eq(", "SasFunctions.ne(", "SasFunctions.lt(", "SasFunctions.le(",
                                        "SasFunctions.gt(", "SasFunctions.ge(", "SasFunctions.isMissing(", "(!", "(SasFunctions.truthy(")) \
            else f"SasFunctions.truthy({java})"

    # ---- comparaciones
    def cmp(self) -> str:
        left = self.add()
        k, v = self.peek()
        low = v.lower()
        if k == "id" and low == "is":
            self.take()
            negate = self.word("not")
            if negate:
                self.take()
            if self.take()[1].lower() not in ("missing", "null"):
                raise Unsupported("IS sin MISSING/NULL")
            return f"{'(!' if negate else ''}SasFunctions.isMissing({left}){')' if negate else ''}"
        negate = False
        if k == "id" and low == "not" and self.peek(1)[1].lower() in ("in", "between", "like"):
            self.take()
            negate = True
            k, v = self.peek()
            low = v.lower()
        if k == "id" and low == "in":
            self.take()
            self.expect("(")
            values = [self.add()]
            while self.peek()[1] == ",":
                self.take()
                values.append(self.add())
            self.expect(")")
            call = f"SasFunctions.in({left}, {', '.join(values)})"
            return f"(!{call})" if negate else call
        if k == "id" and low == "between":
            self.take()
            lo = self.add()
            if not self.word("and"):
                raise Unsupported("BETWEEN sin AND")
            self.take()
            hi = self.add()
            call = f"SasFunctions.between({left}, {lo}, {hi})"
            return f"(!{call})" if negate else call
        if k == "id" and low == "like":
            self.take()
            call = f"SasFunctions.like({left}, {self.add()})"
            return f"(!{call})" if negate else call
        op = _CMP.get(low) if k in ("op", "id") else None
        if op is None:
            return left
        self.take()
        right = self.add()
        return f"SasFunctions.{op}({left}, {right})"

    # ---- aritmética
    def add(self) -> str:
        left = self.mul()
        while self.peek()[1] in ("+", "-", "||", "!!"):
            op = self.take()[1]
            right = self.mul()
            name = {"+": "add", "-": "sub"}.get(op, "concat")
            left = f"SasFunctions.{name}({left}, {right})"
        return left

    def mul(self) -> str:
        left = self.pow()
        while self.peek()[1] in ("*", "/"):
            op = self.take()[1]
            left = f"SasFunctions.{'mul' if op == '*' else 'div'}({left}, {self.pow()})"
        return left

    def pow(self) -> str:
        base = self.unary()
        if self.peek()[1] == "**":
            self.take()
            return f"SasFunctions.pow({base}, {self.pow()})"
        return base

    def unary(self) -> str:
        if self.peek()[1] == "-" :
            self.take()
            return f"SasFunctions.neg({self.unary()})"
        if self.peek()[1] == "+":
            self.take()
            return self.unary()
        return self.atom()

    # ---- átomos
    def atom(self) -> str:
        k, v = self.take()
        if k == "str":
            return _java_string(v)
        if k == "datelit":
            return f'SasFunctions.dateLiteral("{v[1:-2]}")'
        if k == "num":
            return f"{v}d" if re.fullmatch(r"\d+", v) is None else v
        if k == "fmt":
            return _java_string(f"'{v}'")
        if k == "mvar":
            name = v.lstrip("&").rstrip(".")
            self.warnings.add(f"Macrovariable &{name} -> context.{name} (crear la variable de contexto)")
            return f"context.{name}"
        if k == "name":
            return self.column(re.search(r"'([^']+)'[nN]$", v).group(1))
        if k == "op" and v == ".":
            return "null"  # valor perdido
        if k == "op" and v == "(":
            inner = self.expr()
            self.expect(")")
            return f"({inner})"
        if k == "id":
            low = v.lower()
            if low == "case":
                return self.case()
            if low == "calculated":
                return self.atom()
            if self.peek()[1] == "(" and low not in ("and", "or", "not", "in"):
                return self.call(low)
            if low in ("and", "or", "not", "in", "is", "then", "else", "end", "when"):
                raise Unsupported(f"palabra {v}")
            return self.column(v.split(".")[-1])
        raise Unsupported(f"inesperado: {v!r}")

    def column(self, name: str) -> str:
        self.cols.append(name)
        return f"input_row.{name}"

    def case(self) -> str:
        branches: list[tuple[str, str]] = []
        operand = None
        if not self.word("when"):  # CASE x WHEN v THEN ...
            operand = self.add()
        while self.word("when"):
            self.take()
            cond = self.expr() if operand is None else f"SasFunctions.eq({operand}, {self.add()})"
            if not self.word("then"):
                raise Unsupported("CASE sin THEN")
            self.take()
            branches.append((cond, self.expr()))
        other = "null"
        if self.word("else"):
            self.take()
            other = self.expr()
        if not self.word("end"):
            raise Unsupported("CASE sin END")
        self.take()
        out = other
        for cond, value in reversed(branches):
            out = f"SasFunctions.ifv({self.truthy(cond)}, {value}, {out})"
        return out

    def call(self, name: str) -> str:
        if name in MASK_UNSUPPORTED or name not in FUNCTIONS:
            raise Unsupported(f"función {name}")
        self.take()  # (
        args: list[str] = []
        if self.peek()[1] != ")":
            while True:
                if name in _FORMAT_ARGS and len(args) == 1:
                    args.append(self.raw_format())
                else:
                    args.append(self.expr())
                if self.peek()[1] == ",":
                    self.take()
                    continue
                break
        self.expect(")")
        return f"SasFunctions.{FUNCTIONS[name]}({', '.join(args)})"

    def raw_format(self) -> str:
        """El formato de `input`/`put` (`date9.`, `$10.`, `8.`) es un nombre, no una expresión."""
        parts, depth = [], 0
        while self.i < len(self.t):
            _kind, v = self.peek()
            if depth == 0 and v in (",", ")"):
                break
            depth += v == "("
            depth -= v == ")"
            parts.append(v.strip("'\""))
            self.i += 1
        return _java_string("'" + "".join(parts) + "'")


def _clean(text: str) -> str:
    """Quita lo que acompaña a una expresión de PROC SQL y no es parte de ella."""
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(?i)^(on|where|having)\s+", "", text)
    text = re.sub(r"(?i)^distinct\s+", "", text)
    text = re.sub(r"(?i)\s+(label|format|informat|length)\s*=\s*(\"[^\"]*\"|'[^']*'|\S+)\s*$", "", text)
    text = re.sub(r"(?i)\s+as\s+\w+\s*$", "", text)
    return text.strip()


def translate_with_routine(sas: str) -> Result:
    """Traduce una expresión SAS a Java con `SasFunctions`; `Unsupported` si no hay traducción segura."""
    text = _clean(sas)
    if not text:
        raise Unsupported("expresión vacía")
    parser = _P(_tokens(text))
    java = parser.expr()
    if parser.i != len(parser.t):
        raise Unsupported(f"texto sobrante: {parser.peek()[1]!r}")
    return Result(java, sorted(set(parser.cols)), sorted(parser.warnings))
