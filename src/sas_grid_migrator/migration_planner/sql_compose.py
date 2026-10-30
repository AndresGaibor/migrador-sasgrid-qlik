"""Composición SQL: una cadena de `create table W as select ...` se funde en UNA sentencia.

Si la tabla intermedia W la crea una sentencia y la lee UNA sola sentencia posterior, la consumidora usa la
definición de W como CTE (`create table T as with w_cte as (select ...) select ... from w_cte`). El resultado
es una sentencia con su consulta completa: si todas sus tablas son de un mismo motor, `elt.fold_elt` la
convierte en UN paso del motor (tXxxRow con el SQL en QUERY).

Dos niveles, que deben coincidir:

1. Texto (`compose_statements`): la consulta compuesta, con los CTE en orden de dependencias.
2. Operaciones IR (`compose_items`): los pasos de la productora pasan a la misma cadena que la consumidora,
   con el mismo paso y evidencia, y la escritura de W desaparece. Así la fusión a corriente (`build_flow`)
   y el ELT ven UN grupo SQL.

Límites (no se compone; `compose_items` devuelve el motivo en `notes`):
- Productora o consumidora con operaciones fuera de `COMPOSABLE_TYPES` (intersect/except, pass-through, etc.).
- Funciones SAS sin equivalente (`rules/sas/sql-functions.json`, estado `sas_only`), `calculated`, `into :macro`,
  `&`/`%` en la consulta productora, `order by` en la productora (un CTE con ORDER BY no es portable).
- W con varios escritores o varios lectores, W compartida con otro programa o macro, W que es salida final.
- Consumidora con JOIN o UNION cuando no todas sus tablas son de un mismo motor con componente Row.
- Una escritura entre la productora y la consumidora que cambia una tabla que la productora lee.

Lo que no se compone sigue como antes: el planificador no cambia de comportamiento para esas sentencias.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from sas_grid_migrator.intermediate_representation.models import IROperation, LibraryRef
from sas_grid_migrator.migration_planner.elt import SAS_ONLY
from sas_grid_migrator.migration_planner.versions import is_plain

RULES_PATH = Path(__file__).resolve().parents[3] / "rules" / "sas" / "sql-functions.json"

#: Tipos de operación que puede producir una sentencia SQL de tipo create table.
COMPOSABLE_TYPES = frozenset(
    {"read", "join", "filter", "project", "aggregate", "dedupe", "sort", "union", "write"}
)
#: Palabras que el SQL escribe seguidas de paréntesis y que no son funciones.
SQL_KEYWORDS = frozenset(
    {
        "in",
        "exists",
        "not",
        "and",
        "or",
        "on",
        "using",
        "over",
        "as",
        "select",
        "from",
        "where",
        "when",
        "then",
        "else",
        "case",
        "end",
        "distinct",
        "union",
        "all",
        "like",
        "between",
        "is",
        "null",
        "by",
        "group",
        "having",
        "order",
        "join",
        "with",
        "values",
        "any",
        "some",
        "into",
        "table",
        "create",
    }
)

_CALL = re.compile(r"(?<![\w.])([A-Za-z_]\w*)\s*\(")
_CREATE = re.compile(r"^\s*create\s+table\s+([A-Za-z_][\w.]*)\s+as\s+", re.IGNORECASE)
_WITH = re.compile(r"with\s+(?!recursive\b)", re.IGNORECASE)
_CTE_HEAD = re.compile(r"\s*([A-Za-z_]\w*)\s+as\s*\(", re.IGNORECASE)
_SEP = re.compile(r"\s*,")
#: Dentro de la consulta productora: nada que un CTE no admita o que tenga sentido solo en SAS.
_UNSAFE_PRODUCER = re.compile(
    r"\border\s+by\b|\bintersect\b|\bexcept\b|\binto\s*:|\bcalculated\b|[&%]", re.IGNORECASE
)


def mask(sql: str) -> str:
    """Misma longitud que `sql`; el contenido de literales, identificadores entrecomillados y comentarios
    se sustituye por '_'. Las búsquedas de palabras y paréntesis se hacen sobre el texto enmascarado."""
    out: list[str] = []
    i, n = 0, len(sql)
    while i < n:
        ch = sql[i]
        if ch in "'\"":
            j = i + 1
            while j < n:
                if sql[j] == ch:
                    if j + 1 < n and sql[j + 1] == ch:
                        j += 2
                        continue
                    break
                j += 1
            end = min(j + 1, n)
        elif sql.startswith("/*", i):
            end = sql.find("*/", i + 2)
            end = n if end < 0 else end + 2
        elif sql.startswith("--", i):
            end = sql.find("\n", i)
            end = n if end < 0 else end
        else:
            out.append(ch)
            i += 1
            continue
        out.append("_" * (end - i))
        i = end
    return "".join(out)


def _close(masked: str, open_at: int) -> int | None:
    """Índice del paréntesis que cierra el de `open_at` (texto enmascarado)."""
    depth = 0
    for k in range(open_at, len(masked)):
        if masked[k] == "(":
            depth += 1
        elif masked[k] == ")":
            depth -= 1
            if depth == 0:
                return k
    return None


@lru_cache(maxsize=1)
def sql_functions() -> dict[str, dict]:
    """Diccionario de funciones (rules/sas/sql-functions.json)."""
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))["functions"]


def unknown_functions(sql: str, engine: str | None = None) -> set[str]:
    """Funciones de la consulta que no se pueden componer: sin estado `portable` ni traducción para el motor.

    Un nombre seguido de paréntesis que va tras `AS` (p. ej. `cast(x as decimal(10,2))`) es un tipo, no una función."""
    table = sql_functions()
    masked = mask(sql)
    bad: set[str] = set()
    for match in _CALL.finditer(masked):
        name = match.group(1).lower()
        if name in SQL_KEYWORDS or re.search(r"\bas\s*$", masked[: match.start()], re.IGNORECASE):
            continue
        entry = table.get(name)
        if entry and entry.get("status") == "portable":
            continue
        if (
            entry
            and entry.get("status") == "translated"
            and engine
            and engine in entry.get("engines", {})
        ):
            continue
        bad.add(name)
    return bad


def translate_functions(sql: str, engine: str) -> str:
    """Sustituye las funciones `translated` por su nombre en el motor (solo las que el diccionario declara)."""
    table = sql_functions()
    masked = mask(sql)
    pieces: list[tuple[int, int, str]] = []
    for match in _CALL.finditer(masked):
        entry = table.get(match.group(1).lower())
        if entry and entry.get("status") == "translated" and engine in entry.get("engines", {}):
            pieces.append((match.start(1), match.end(1), entry["engines"][engine]))
    out, last = [], 0
    for start, end, text in pieces:
        out.append(sql[last:start])
        out.append(text)
        last = end
    out.append(sql[last:])
    return "".join(out)


def split_create(sql: str) -> tuple[str, str, str] | None:
    """(cabecera, consulta select/with, tabla destino) de `create table T as <consulta>`; None si no es así."""
    m = _CREATE.match(sql)
    if not m:
        return None
    select = sql[m.end() :].strip().rstrip(";").strip()
    if not re.match(r"(select|with)\b", select, re.IGNORECASE):
        return None
    return sql[: m.end()].rstrip(), select, m.group(1)


def split_with(select: str) -> tuple[list[tuple[str, str]], str] | None:
    """(CTE [(nombre, cuerpo)], consulta principal) de una consulta; None si su WITH no se puede leer."""
    masked = mask(select)
    m = _WITH.match(masked)
    if not m:
        return [], select
    pos, ctes = m.end(), []
    while True:
        head = _CTE_HEAD.match(masked, pos)
        if not head:
            return None
        open_at = head.end() - 1
        close = _close(masked, open_at)
        if close is None:
            return None
        ctes.append((head.group(1), select[open_at + 1 : close]))
        pos = close + 1
        sep = _SEP.match(masked, pos)
        if sep:
            pos = sep.end()
            continue
        return ctes, select[pos:].strip()


def rewrite_refs(sql: str, lib: str, name: str, cte: str) -> tuple[str, int]:
    """Sustituye las referencias a `lib.name` (y, si lib es work, `name` tras FROM/JOIN, y `name.columna`) por el CTE.

    Devuelve (texto, número de referencias FROM/JOIN sustituidas). Las literales no se tocan."""
    masked = mask(sql)
    # (inicio, fin, texto de sustitución, es referencia FROM/JOIN)
    spans: list[tuple[int, int, str, bool]] = []
    full = re.compile(rf"(?<![\w.]){re.escape(lib)}\.{re.escape(name)}(?!\w)", re.IGNORECASE)
    spans += [(m.start(), m.end(), cte, True) for m in full.finditer(masked)]
    if lib == "work":
        bare = re.compile(rf"((?:\bfrom|\bjoin)\s+)({re.escape(name)})(?![\w.(])", re.IGNORECASE)
        spans += [(m.start(2), m.end(2), cte, True) for m in bare.finditer(masked)]
    qualifier = re.compile(rf"(?<![\w.]){re.escape(name)}\.(?=\w)", re.IGNORECASE)
    spans += [(m.start(), m.end(), cte + ".", False) for m in qualifier.finditer(masked)]
    refs = sum(1 for *_, is_ref in spans if is_ref)
    for start, end, replacement, _ in sorted(spans, key=lambda s: s[0], reverse=True):
        sql = sql[:start] + replacement + sql[end:]
    return sql, refs


def _cte_name(name: str, taken: str) -> str:
    base = re.sub(r"\W", "_", name.lower()) + "_cte"
    candidate, k = base, 1
    while re.search(rf"\b{re.escape(candidate)}\b", taken, re.IGNORECASE):
        k += 1
        candidate = f"{base}{k}"
    return candidate


def compose_statements(
    producer_sql: str,
    consumer_sql: str,
    dataset: str,
    expected_refs: int,
    engine: str | None = None,
) -> tuple[str | None, str]:
    """(consulta única, ""), o (None, motivo) si la composición no es segura. Motivo en español, para el plan."""
    prod = split_create(producer_sql)
    cons = split_create(consumer_sql)
    if prod is None or cons is None:
        return None, "la productora o la consumidora no es un create table ... as select"
    _, p_select, _ = prod
    c_head, c_select, _ = cons
    for label, select in (("productora", p_select), ("consumidora", c_select)):
        only_sas = SAS_ONLY.search(select)
        if only_sas:
            return None, f"la {label} usa sintaxis solo SAS ({only_sas.group(0).strip()})"
        masked = mask(select)
        if re.search(r"\bouter\s+union\b|\bcorr\b", masked, re.IGNORECASE):
            return None, f"la {label} usa OUTER UNION CORR, que es de SAS y no de los motores"
        if re.search(r"\bconnection\s+to\b", masked, re.IGNORECASE):
            return None, f"la {label} contiene un pass-through `connection to` de SAS"
        if re.search(r"\binto\s*:", select, re.IGNORECASE):
            return None, f"la {label} asigna macro variables con INTO"
    if _UNSAFE_PRODUCER.search(mask(p_select)):
        return (
            None,
            "la productora tiene ORDER BY, INTERSECT o EXCEPT, que un CTE no admite de forma portable",
        )
    unknown = unknown_functions(p_select, engine) | unknown_functions(c_select, engine)
    if unknown:
        return None, "funciones sin equivalente verificado: " + ", ".join(sorted(unknown))
    lib, _, name = dataset.partition(".")
    if not name:
        return None, "nombre de tabla no plano"
    cte = _cte_name(name, producer_sql + consumer_sql)
    rewritten, refs = rewrite_refs(c_select, lib, name, cte)
    if refs != expected_refs or refs == 0:
        return None, "no se localizan todas las referencias a la tabla intermedia en el FROM/JOIN"
    p_split = split_with(p_select)
    c_split = split_with(rewritten)
    if p_split is None or c_split is None:
        return None, "WITH con una forma que no se puede leer"
    p_ctes, p_main = p_split
    c_ctes, c_main = c_split
    ctes = [*p_ctes, (cte, p_main), *c_ctes]
    names = [n.lower() for n, _ in ctes]
    if len(set(names)) != len(names):
        return None, "nombres de CTE repetidos"
    if engine:
        ctes = [(n, translate_functions(b, engine)) for n, b in ctes]
        c_main = translate_functions(c_main, engine)
    text = f"{c_head} with " + ", ".join(f"{n} as ({b.strip()})" for n, b in ctes) + f" {c_main}"
    if rewrite_refs(text, lib, name, cte)[1] != 0 or re.search(
        rf"(?<![\w.]){re.escape(lib)}\.{re.escape(name)}(?!\w)", mask(text), re.IGNORECASE
    ):
        return None, "quedan referencias a la tabla intermedia tras componer"
    return text, ""


# ---------------------------------------------------------------- nivel de operaciones IR

Item = tuple[IROperation, str]


@dataclass
class _Unit:
    """Sentencias que comparten paso, prefijo y líneas; tras una composición, la cadena ya fundida."""

    prefix: str
    ops: list[IROperation]
    first: int  # índice original de la primera sentencia que contiene
    key: tuple
    absorbed: bool = False
    composed_from: list[str] = field(default_factory=list)


def _statements(items: list[Item]) -> list[_Unit]:
    units: list[_Unit] = []
    for op, prefix in items:
        key = (prefix, op.step, op.evidence.line, op.evidence.end_line)
        if units and units[-1].key == key:
            units[-1].ops.append(op)
        else:
            index = len(units)
            units.append(_Unit(prefix=prefix, ops=[op], first=index, key=key))
    return units


def _sql_write(unit: _Unit) -> IROperation | None:
    """La escritura `create table <dataset plano> as` de la sentencia, si es la única escritura de la unidad."""
    writes = [op for op in unit.ops if op.type == "write"]
    if len(writes) != 1:
        return None
    write = writes[0]
    if (
        write.details.get("view")
        or write.details.get("mode") != "replace"
        or not write.details.get("sql")
    ):
        return None
    if len(write.outputs) != 1 or not is_plain(write.outputs[0]):
        return None
    return write


def _engine_of(
    dataset: str, libs: dict[str, LibraryRef], engines: dict[str, dict[str, str]]
) -> str | None:
    """Motor de la librería de `dataset` si tiene componente Row (el mismo criterio que elt.fold_elt)."""
    lib = dataset.partition(".")[0].lower() if "." in dataset else ""
    ref = libs.get(lib)
    engine = (ref.engine or "").lower() if ref else ""
    return engine if engine and engines.get(engine, {}).get("row") else None


def _single_engine(
    datasets: list[str], libs: dict[str, LibraryRef], engines: dict[str, dict[str, str]]
) -> str | None:
    found = {_engine_of(d, libs, engines) for d in datasets}
    if len(found) != 1 or None in found:
        return None
    return found.pop()


def _interferes(units: list[_Unit], start: int, end: int, inputs: set[str]) -> bool:
    """¿Escribe alguna sentencia entre `start` (incluida) y `end` (excluida) una tabla que la productora lee?"""
    for k in range(start, end):
        if any(set(op.outputs) & inputs for op in units[k].ops):
            return True
    return False


def _merge(
    producer: _Unit, pw: IROperation, consumer: _Unit, cw: IROperation, dataset: str, composed: str
) -> None:
    """Pasa las operaciones de la productora (sin su escritura) al inicio de la consumidora, con su paso y evidencia.
    La lectura de `dataset` desaparece; sus fuentes pasan a ser entradas de la consumidora."""
    moved = [
        op.model_copy(
            update={
                "step": cw.step,
                "evidence": cw.evidence,
                "details": {**op.details, "origin_line": op.evidence.line},
            }
        )
        for op in producer.ops
        if op is not pw
    ]
    p_inputs = list(dict.fromkeys(d for op in producer.ops for d in op.inputs if d != dataset))
    new_write = cw.model_copy(
        update={
            "details": {
                **cw.details,
                "sql": composed,
                "composed_from": [*producer.composed_from, pw.id],
            }
        }
    )
    kept: list[IROperation] = []
    for op in consumer.ops:
        if op is cw:
            kept.append(new_write)
            continue
        if op.type == "read" and op.inputs == [dataset]:
            continue
        if dataset in op.inputs:
            inputs = [d for d in op.inputs if d != dataset]
            inputs += [d for d in p_inputs if d not in inputs]
            op = op.model_copy(update={"inputs": inputs})
        kept.append(op)
    consumer.ops = [*moved, *kept]
    consumer.composed_from = [*producer.composed_from, pw.id]
    consumer.first = min(consumer.first, producer.first)
    producer.absorbed = True


def compose_items(
    items: list[Item],
    shared: set[str] | frozenset[str],
    libs: dict[str, LibraryRef],
    engines: dict[str, dict[str, str]],
) -> tuple[list[Item], list[str]]:
    """Compone cadenas de sentencias create table. Devuelve (items, notas: qué se compuso y qué no, y por qué).

    Recorre las sentencias en orden: cada consumidora absorbe a sus productoras (ya compuestas, si lo son) mientras
    la composición sea segura. La unidad absorbida desaparece del resultado; su contenido viaja con la consumidora."""
    units = _statements(items)
    notes: list[str] = []
    writers: dict[str, list[int]] = {}
    readers: dict[str, set[int]] = {}
    for index, unit in enumerate(units):
        for op in unit.ops:
            for dataset in op.outputs:
                if index not in writers.setdefault(dataset, []):
                    writers[dataset].append(index)
            for dataset in op.inputs:
                readers.setdefault(dataset, set()).add(index)
    composable = [
        all(op.type in COMPOSABLE_TYPES for op in unit.ops) and _sql_write(unit) is not None
        for unit in units
    ]
    texts: dict[int, str] = {
        index: _sql_write(unit).details["sql"]  # type: ignore[union-attr]
        for index, unit in enumerate(units)
        if composable[index]
    }

    for j, consumer in enumerate(units):
        if not composable[j] or consumer.absorbed:
            continue
        merged = True
        while merged:
            merged = False
            cw = _sql_write(consumer)
            if cw is None:
                break
            datasets = [
                op.inputs[0] for op in consumer.ops if op.type == "read" and len(op.inputs) == 1
            ]
            for dataset in dict.fromkeys(datasets):
                if not is_plain(dataset) or dataset in shared or dataset in cw.outputs:
                    continue
                ws = writers.get(dataset, [])
                if len(ws) != 1 or ws[0] >= j or readers.get(dataset) != {j}:
                    continue
                p = ws[0]
                producer = units[p]
                if not composable[p] or producer.absorbed:
                    continue
                pw = _sql_write(producer)
                if pw is None or pw.outputs != [dataset]:
                    continue
                p_inputs = {d for op in producer.ops for d in op.inputs if d != dataset}
                if _interferes(units, producer.first, j, p_inputs):
                    notes.append(
                        f"No se compone {dataset}: una sentencia intermedia reescribe una tabla que la productora lee"
                    )
                    continue
                expected = sum(
                    1 for op in consumer.ops if op.type == "read" and op.inputs == [dataset]
                )
                others = {
                    d for op in consumer.ops if op.type == "read" for d in op.inputs if d != dataset
                }
                joins = any(op.type in ("join", "union") for op in consumer.ops)
                # Sin JOIN, la consumidora solo puede tener como fuente a W: si tiene otras fuentes, solo se
                # compone cuando todas son del mismo motor (la consulta entera irá al motor).
                engine = _single_engine([*sorted(p_inputs | others), cw.outputs[0]], libs, engines)
                if (joins or others) and engine is None:
                    notes.append(
                        f"No se compone {dataset}: la consumidora usa otras tablas que no son todas de un mismo motor"
                    )
                    continue
                composed, reason = compose_statements(
                    texts[p], texts[j], dataset, expected_refs=expected, engine=engine
                )
                if composed is None:
                    notes.append(f"No se compone {dataset}: {reason}")
                    continue
                _merge(producer, pw, consumer, cw, dataset, composed)
                texts[j] = composed
                writers[dataset] = []
                notes.append(f"Compuesta {dataset} en la sentencia de línea {cw.evidence.line}")
                merged = True
                break

    out: list[Item] = []
    for unit in units:
        if not unit.absorbed:
            out.extend((op, unit.prefix) for op in unit.ops)
    return out, notes
