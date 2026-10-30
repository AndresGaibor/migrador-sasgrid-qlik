"""Plegado de regiones largas repetidas del Job principal.

`joblets.py` solo ve bloques de hasta `JOBLET_MAX_WINDOW_STEPS` pasos y deja listados todos los pasos
de cada aparición. Aquí un tramo de pasos de cualquier longitud que se repite (p. ej. la misma cadena
de transformaciones una vez por segmento de negocio) se convierte en UN joblet, y cada copia posterior
se sustituye por UN paso de uso.

Cómo funciona:

1. Huella estructural por paso: tipo de componente, forma de sus conexiones (tipo y distancia al paso
   origen), forma abstracta de sus propiedades y expresiones (identificadores, cadenas y números
   sustituidos por marcadores) y número de columnas. Dos pasos con la misma huella son el mismo paso
   salvo sus valores.
2. Búsqueda de copias: semillas de pasos iguales consecutivos, extendidas hacia los dos lados con una
   alineación tolerante a pequeñas divergencias (saltos de un paso en una u otra copia, sustituciones).
   Cada alineación se confirma con `difflib.SequenceMatcher` (similitud >= `REGION_MIN_SIMILARITY`).
3. Clúster y elección: las alineaciones que comparten una copia forman una familia. El cuerpo es la
   copia más larga; se eligen copias no solapadas y, entre familias, la de mayor ahorro
   (pasos ahorrados = suma de copias - cuerpo - (copias - 1) pasos de uso).
4. Parámetros: las diferencias entre copias se explican como reemplazos de sub-tokens de los
   identificadores (`CTE` por `AHORROS`, segmentos de negocio) que son consistentes en todas las copias,
   que pasan a ser UN parámetro por sub-token; los literales que cambian son un parámetro por posición;
   un paso que solo está en algunas copias es un parámetro booleano (`paso_opcional_N`).
5. Plegado: la copia más larga conserva sus pasos (son el cuerpo del joblet, contados una vez); cada
   copia restante se sustituye por un paso `Usa el joblet <nombre> (valores)` con `joblet_id`. Las
   divergencias estructurales entre copias se avisan en `plan.unresolved` y en el `why` del joblet.

Límites: solo se pliegan regiones de nivel superior (un joblet que contiene a otro no se anida), y solo
dentro de la secuencia del Job principal antes de repartirlo en partes.
"""

from __future__ import annotations

import difflib
import json
import re
from dataclasses import dataclass

from sas_grid_migrator.migration_planner import limits
from sas_grid_migrator.migration_planner.joblets import (
    ROLE_BY_TYPE,
    ROLE_PRIORITY,
    _creation_steps,
    _unique,
)
from sas_grid_migrator.migration_planner.models import (
    Connection,
    JobletOccurrence,
    JobletParameter,
    JobletPlan,
    JobPlan,
    PlanStep,
)

#: Palabras SAS/SQL que definen la forma de una expresión: se conservan, no son identificadores.
_KEYWORDS = frozenset(
    ["and", "or", "not", "if", "then", "else", "is", "missing", "in", "between", "case", "when", "end", "like", "null", "as", "from", "where", "select", "by", "on", "left", "right", "inner", "outer", "join", "sum", "count", "max", "min", "avg", "cat", "input", "put", "substr", "strip", "trim", "upcase", "lowcase", "round", "int", "year", "month", "day", "today", "datetime", "nmiss", "coalesce", "distinct", "group", "having", "order"]
)
_TOKEN = re.compile(r"'[^']*'|\"[^\"]*\"|[A-Za-z_][A-Za-z0-9_.]*|\d+(?:\.\d+)?")
_SUBTOKEN = re.compile(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|\d+")
MAX_EXAMPLES = 5


def subtokens(identifier: str) -> list[str]:
    """Sub-tokens de un identificador: se parte por `_`, mayúsculas/minúsculas y dígitos."""
    out: list[str] = []
    for part in identifier.split("_"):
        out += _SUBTOKEN.findall(part)
    return [token.upper() for token in out]


def abstract_text(text: str) -> str:
    """Forma de un texto: cadenas a `S`, números a `#`, identificadores a `ID` (palabras SAS se conservan)."""

    def replace(match: re.Match[str]) -> str:
        token = match.group(0)
        if token[0] in "'\"":
            return "S"
        if token[0].isdigit():
            return "#"
        return token.lower() if token.lower() in _KEYWORDS else "ID"

    return _TOKEN.sub(replace, text)


def _identifiers(text: str) -> list[str]:
    return [
        token for token in _TOKEN.findall(text)
        if token[0].isalpha() or token[0] == "_"
        if token.lower() not in _KEYWORDS
    ]


def _literals(text: str) -> list[str]:
    return [token for token in _TOKEN.findall(text) if token[0] in "'\"" or token[0].isdigit()]


def _shape(step: PlanStep, position: int, positions: dict[str, int]) -> str:
    """Huella de un paso: componente, conexiones (tipo y distancia al origen), propiedades, expresiones."""
    links = sorted(
        f"{c.type}@{position - positions[c.from_step] if c.from_step in positions else 'ext'}"
        for c in step.connections
    )
    shape = [
        step.component_candidate,
        step.operation_type or "",
        step.action,
        links,
        [[p.name, abstract_text(p.value or "")] for p in step.properties],
        [abstract_text(e.sas) for e in step.expressions],
        len(step.schema_columns),
        sorted(step.alternatives),
    ]
    return json.dumps(shape, ensure_ascii=False, sort_keys=True)


@dataclass
class Sequence:
    """Pasos del plan en orden, como tokens: >= 0 es la huella de un paso; < 0 es un separador (no se
    alinea a través de él: pasos recomendados, pasos de joblet, cambio de Job)."""

    tokens: list[int]
    plan_index: list[int | None]  # índice en plan.steps de cada token (None en los separadores)


def build_sequence(steps: list[PlanStep]) -> Sequence:
    layout: list[int | None] = []
    for index, step in enumerate(steps):
        eligible = not step.recommended and not step.joblet_id
        if not eligible:
            if layout and layout[-1] is not None:
                layout.append(None)
            continue
        previous = layout[-1] if layout else None
        if previous is not None and steps[previous].job_part != step.job_part:
            layout.append(None)
        layout.append(index)
    positions: dict[str, int] = {}
    for position, index in enumerate(layout):
        if index is not None:
            positions[steps[index].id] = position
    interned: dict[str, int] = {}
    tokens: list[int] = []
    separators = 0
    for position, index in enumerate(layout):
        if index is None:
            separators += 1
            tokens.append(-separators)
            continue
        key = _shape(steps[index], position, positions)
        tokens.append(interned.setdefault(key, len(interned)))
    return Sequence(tokens=tokens, plan_index=layout)


def _sim(a: list[int], b: list[int]) -> float:
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def _extend(
    tokens: list[int], x: int, y: int, base: int, max_divergence: float, limit_x: int | None = None, limit_y: int | None = None
) -> tuple[int, int]:
    """Alinea hacia la derecha desde (x, y). Devuelve cuántos tokens consume cada copia en el mejor
    punto (que acaba en coincidencia) antes de que la divergencia supere `max_divergence`. `limit_x` y
    `limit_y` frenan cada copia antes de esa posición (para que las dos copias no se solapen)."""
    n = len(tokens)
    limit_x = n if limit_x is None else limit_x
    limit_y = n if limit_y is None else limit_y
    start_x, start_y = x, y
    matches, edits = base, 0
    best = (0, 0)

    def same(p: int, q: int) -> bool:
        return 0 <= p < n and 0 <= q < n and tokens[p] >= 0 and tokens[p] == tokens[q]

    while x < limit_x and y < limit_y and tokens[x] >= 0 and tokens[y] >= 0:
        if tokens[x] == tokens[y]:
            x += 1
            y += 1
            matches += 1
            if edits <= max_divergence * (matches + edits):
                best = (x - start_x, y - start_y)
            continue
        # Re-enganche: un bloque de pasos sobra en una copia y, tras él, tres pasos vuelven a coincidir.
        gap_a = next((g for g in range(1, limits.REGION_MAX_GAP + 1) if same(x + g, y) and same(x + g + 1, y + 1) and same(x + g + 2, y + 2)), None)
        gap_b = next((g for g in range(1, limits.REGION_MAX_GAP + 1) if same(x, y + g) and same(x + 1, y + g + 1) and same(x + 2, y + g + 2)), None)
        if gap_a is not None and (gap_b is None or gap_a <= gap_b):
            x += gap_a
            edits += gap_a
        elif gap_b is not None:
            y += gap_b
            edits += gap_b
        else:  # paso distinto en las dos
            x += 1
            y += 1
            edits += 1
        if edits > max_divergence * (matches + edits):
            break
    return best


def _grow(tokens, reverse, i, j, seed, max_divergence, min_steps, min_similarity):
    n = len(tokens)
    # Hacia la derecha la primera copia no puede pasar del inicio de la segunda (copias contiguas).
    right_a, right_b = _extend(tokens, i + seed, j + seed, seed, max_divergence, limit_x=j)
    a1 = i + seed + right_a
    # Hacia la izquierda: la misma extensión sobre la secuencia invertida (el token i-1 es el n-i de ella).
    # La segunda copia no puede empezar antes del final de la primera.
    left_a, left_b = _extend(reverse, n - i, n - j, seed, max_divergence, limit_y=n - a1)
    a0 = i - left_a
    b0, b1 = j - left_b, j + seed + right_b
    if a1 > b0 or a1 - a0 < min_steps or b1 - b0 < min_steps:
        return None
    if _sim(tokens[a0:a1], tokens[b0:b1]) < min_similarity:
        return None
    return (a0, a1, b0, b1)


def _alignments(tokens, *, min_steps, min_similarity, seed, max_seed_occurrences, max_divergence):
    """Pares de copias alineadas (a0, a1, b0, b1) a partir de semillas iguales."""
    reverse = tokens[::-1]
    grams: dict[tuple[int, ...], list[int]] = {}
    for p in range(len(tokens) - seed + 1):
        window = tokens[p : p + seed]
        if min(window) >= 0:
            grams.setdefault(tuple(window), []).append(p)
    accepted: list[tuple[int, int, int, int]] = []
    for positions in grams.values():
        if len(positions) < 2 or len(positions) > max_seed_occurrences:
            continue
        for k, i in enumerate(positions):
            for j in positions[k + 1 :]:
                if any(a0 <= i < a1 and b0 <= j < b1 for a0, a1, b0, b1 in accepted):
                    continue  # ya cubierta por una alineación
                found = _grow(tokens, reverse, i, j, seed, max_divergence, min_steps, min_similarity)
                if found:
                    accepted.append(found)
    return accepted


def _families(alignments) -> list[list[tuple[int, int]]]:
    """Agrupa los tramos de las alineaciones que son la misma copia (solapan >= 80 %)."""
    nodes: list[tuple[int, int]] = []
    parent: list[int] = []

    def node(span: tuple[int, int]) -> int:
        for k, (s, e) in enumerate(nodes):
            overlap = min(e, span[1]) - max(s, span[0])
            if overlap >= 0.8 * min(e - s, span[1] - span[0]):
                return k
        nodes.append(span)
        parent.append(len(nodes) - 1)
        return len(nodes) - 1

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a0, a1, b0, b1 in alignments:
        x, y = find(node((a0, a1))), find(node((b0, b1)))
        if x != y:
            parent[y] = x
    groups: dict[int, list[tuple[int, int]]] = {}
    for k in range(len(nodes)):
        groups.setdefault(find(k), []).append(nodes[k])
    return list(groups.values())


@dataclass(frozen=True)
class Region:
    """Copias de un mismo tramo en la secuencia: intervalos [inicio, fin) ordenados."""

    spans: tuple[tuple[int, int], ...]
    body: int  # índice en `spans` de la copia más larga (cuerpo del joblet)
    savings: int  # pasos que se ahorran al plegar


def _scan_copies(tokens, template, chosen, *, min_steps, min_similarity, seed) -> list[tuple[int, int]]:
    """Copias del cuerpo que la alineación no encontró. Se buscan las posiciones donde aparece un tramo de
    `seed` pasos del cuerpo (en cualquier desplazamiento) y, alrededor de cada una, se compara cada ventana
    de longitud L-3..L+3 que empieza hasta 3 pasos antes o después. Entre las ventanas casi igual de buenas
    (0,05 de similitud) se toma la que empieza antes, para no soltar el primer paso de la copia."""
    n = len(tokens)
    start, end = template
    length = end - start
    body = tokens[start:end]
    if length < seed:
        return []
    anchors: set[int] = set()
    for offset in range(min(length - seed, 25) + 1):
        head = body[offset : offset + seed]
        if min(head) < 0:
            continue
        for p in range(n - seed + 1):
            if tokens[p : p + seed] == head:
                anchors.add(p - offset)
    found: list[tuple[int, int]] = []
    for s in sorted(anchors):
        if s < 0 or any(a <= s < b for a, b in chosen + found):
            continue
        options: list[tuple[float, int, int]] = []
        for ss in range(max(0, s - 3), s + 4):
            for size in range(max(min_steps, length - 3), length + 4):
                if ss + size > n or min(tokens[ss : ss + size]) < 0:
                    continue
                if any(a < ss + size and ss < b for a, b in chosen + found):
                    continue
                options.append((_sim(body, tokens[ss : ss + size]), ss, size))
        if not options:
            continue
        top = max(ratio for ratio, _, _ in options)
        if top < min_similarity:
            continue
        _ratio, ss, size = min((o for o in options if o[0] >= top - 0.05), key=lambda o: (o[1], -o[0]))
        found.append((ss, ss + size))
    return found


def _best_region(tokens, members, *, min_steps, min_occurrences, min_similarity, seed) -> Region | None:
    spans = sorted(members, key=lambda s: (-(s[1] - s[0]), s[0]))
    template = spans[0]
    if template[1] - template[0] < min_steps:
        return None
    chosen = [template]
    for span in spans[1:]:
        if any(span[0] < c[1] and c[0] < span[1] for c in chosen):
            continue
        if _sim(tokens[template[0] : template[1]], tokens[span[0] : span[1]]) >= min_similarity:
            chosen.append(span)
    chosen += _scan_copies(
        tokens, template, chosen, min_steps=min_steps, min_similarity=min_similarity, seed=seed
    )
    if len(chosen) < min_occurrences:
        return None
    chosen.sort()
    lengths = [end - start for start, end in chosen]
    body = max(range(len(chosen)), key=lambda k: (lengths[k], -k))  # la copia más larga, la primera si empatan
    savings = sum(lengths) - (lengths[body] + len(chosen) - 1)
    return Region(spans=tuple(chosen), body=body, savings=savings)


def find_regions(
    tokens: list[int],
    *,
    min_steps: int = limits.REGION_MIN_STEPS,
    min_occurrences: int = limits.REGION_MIN_OCCURRENCES,
    min_similarity: float = limits.REGION_MIN_SIMILARITY,
    max_divergence: float = limits.REGION_MAX_DIVERGENCE,
    seed: int = limits.REGION_SEED_STEPS,
    max_seed_occurrences: int = limits.REGION_MAX_SEED_OCCURRENCES,
) -> list[Region]:
    """Regiones repetidas no solapadas, por ahorro decreciente. Determinista: el orden de las semillas
    es el de aparición en la secuencia."""
    alignments = _alignments(
        tokens,
        min_steps=min_steps,
        min_similarity=min_similarity,
        seed=seed,
        max_seed_occurrences=max_seed_occurrences,
        max_divergence=max_divergence,
    )
    candidates = []
    for members in _families(alignments):
        region = _best_region(
            tokens,
            members,
            min_steps=min_steps,
            min_occurrences=min_occurrences,
            min_similarity=min_similarity,
            seed=seed,
        )
        if region:
            candidates.append(region)
    candidates.sort(key=lambda r: (-r.savings, r.spans[0][0]))
    claimed = [False] * len(tokens)
    result: list[Region] = []
    for region in candidates:
        free = [s for s in region.spans if not any(claimed[s[0] : s[1]])]
        if len(free) < min_occurrences:
            continue
        template = region.spans[region.body]
        if template not in free:
            continue  # el cuerpo ya lo usa otra región: esta familia no se pliega
        free.sort()
        lengths = [end - start for start, end in free]
        body = free.index(template)
        savings = sum(lengths) - (lengths[body] + len(free) - 1)
        if savings <= 0:
            continue
        for start, end in free:
            for p in range(start, end):
                claimed[p] = True
        result.append(Region(spans=tuple(free), body=body, savings=savings))
    result.sort(key=lambda r: r.spans[0][0])
    return result


# ---- parámetros ----


def _fields(step: PlanStep) -> dict[str, str]:
    values = {f"propiedad {p.name}": p.value or "" for p in step.properties}
    values.update({f"expresion {k}": e.sas for k, e in enumerate(step.expressions, 1)})
    return values


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _subtoken_renames(ref: str, other: str) -> dict[str, str] | None:
    """Sub-tokens de los identificadores de `ref` que cambian en `other`; None si el texto cambia de otra forma."""
    if abstract_text(ref) != abstract_text(other) or _literals(ref) != _literals(other):
        return None
    renames: dict[str, str] = {}
    for a, b in zip(_identifiers(ref), _identifiers(other), strict=True):
        if a == b:
            continue
        sub_a, sub_b = subtokens(a), subtokens(b)
        if len(sub_a) != len(sub_b):
            return None
        for x, y in zip(sub_a, sub_b, strict=True):
            if x != y:
                renames[x] = y
    return renames


def _pairs(body: list[int], copy: list[int]) -> tuple[dict[int, int], list[str]]:
    """Pasos del cuerpo que tienen pareja en la copia (índice cuerpo -> índice copia) y avisos."""
    pairs: dict[int, int] = {}
    notes: list[str] = []
    matcher = difflib.SequenceMatcher(None, body, copy, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            pairs.update({i1 + k: j1 + k for k in range(i2 - i1)})
        elif tag == "replace" and i2 - i1 == j2 - j1:
            pairs.update({i1 + k: j1 + k for k in range(i2 - i1)})
            notes.append(f"{i2 - i1} paso(s) con otra forma que en el cuerpo")
        elif tag == "replace":
            notes.append(f"{j2 - j1} paso(s) distintos en lugar de {i2 - i1} del cuerpo")
        elif tag == "insert":
            notes.append(f"{j2 - j1} paso(s) extra que el joblet no incluye")
        elif tag == "delete":
            notes.append(f"{i2 - i1} paso(s) del cuerpo que la copia no tiene (parámetro opcional)")
    return pairs, notes


@dataclass
class _Layout:
    """Lo que hace falta para plegar una región; se calcula sin tocar el plan."""

    params: list[JobletParameter]
    values: list[dict[str, str]]  # valor de cada parámetro en cada copia (mismo orden que las copias)
    divergences: list[str]


def _layout(occurrences: list[list[PlanStep]], tokens: list[list[int]], body: int) -> _Layout:
    count = len(occurrences)
    ref = occurrences[body]
    divergences: list[str] = []
    present = [[False] * len(ref) for _ in range(count)]
    values_of: list[dict[tuple[int, str], str]] = [{} for _ in range(count)]
    for m, steps in enumerate(occurrences):
        if m == body:
            pairs = {i: i for i in range(len(ref))}
        else:
            pairs, notes = _pairs(tokens[body], tokens[m])
            divergences += [f"copia {m + 1}: {note}" for note in notes]
        for i, j in pairs.items():
            present[m][i] = True
            for field_name, text in _fields(steps[j]).items():
                values_of[m][(i, field_name)] = text
    keys = sorted({key for d in values_of for key in d})
    columns = {key: [d.get(key) for d in values_of] for key in keys}
    differing = [key for key in keys if len({c for c in columns[key]}) > 1]
    # Un campo que cambia solo en sub-tokens de identificadores se explica con renombrados.
    renamable: dict[tuple[int, str], dict[int, dict[str, str]]] = {}
    for key in differing:
        texts = [c if c is not None else "" for c in columns[key]]
        maps: dict[int, dict[str, str]] | None = {}
        for m in range(count):
            if m == body or texts[m] == texts[body]:
                continue
            renames = _subtoken_renames(texts[body], texts[m])
            if renames is None:
                maps = None
                break
            maps[m] = renames
        if maps:
            renamable[key] = maps
    merged: list[dict[str, str]] = [{} for _ in range(count)]
    coherent = True
    for maps in renamable.values():
        for m, renames in maps.items():
            for old, new in renames.items():
                if merged[m].setdefault(old, new) != new:
                    coherent = False
    if not coherent:
        renamable, merged = {}, [{} for _ in range(count)]  # reemplazos incoherentes: todo literal

    used: set[str] = set()
    params: list[JobletParameter] = []
    values: list[dict[str, str]] = [{} for _ in range(count)]

    def add(name: str, per_copy: list[str]) -> None:
        final = _unique(name, used)
        params.append(
            JobletParameter(
                name=final,
                context_variable=f"context.{final}",
                example_values=list(dict.fromkeys(per_copy))[:MAX_EXAMPLES],
            )
        )
        for m in range(count):
            values[m][final] = per_copy[m]

    for token in sorted({old for d in merged for old in d}):
        per_copy = [merged[m].get(token, token) for m in range(count)]
        if len(set(per_copy)) > 1:
            add(f"identificador_{token.lower()}", per_copy)
    for key in differing:
        if key in renamable:
            continue
        i, field_name = key
        per_copy = [c if c is not None else "" for c in columns[key]]
        add(f"valor_paso{i + 1}_{_slug(field_name)}", per_copy)
    for i in range(len(ref)):
        flags = [present[m][i] for m in range(count)]
        if not all(flags):
            add(f"paso_opcional_{i + 1}", ["true" if flag else "false" for flag in flags])
    return _Layout(params=params, values=values, divergences=divergences)


# ---- plegado ----

_ROLE_TEXT_DEFAULT = "Bloque"


def _role_of(steps: list[PlanStep]) -> str:
    present = {step.operation_type for step in steps if step.operation_type}
    for kind in ROLE_PRIORITY:
        if kind in present:
            return ROLE_BY_TYPE[kind]
    return _ROLE_TEXT_DEFAULT


def _body_text(name: str, job: str) -> list[str]:
    return [f"Este es el bloque de origen en {job}: se convierte en el joblet {name} (ver «Cómo crearlo»)."]


def _use_text(name: str, job: str, label: str, values: dict[str, str]) -> list[str]:
    steps = [f"En {job}, sustituye el bloque {label} por el joblet {name}."]
    steps.append(
        f"Arrástralo desde Repository › Joblet Designs al lienzo de {job}: Main desde el paso "
        "anterior hacia su entrada, y su salida hacia el paso siguiente."
    )
    if values:
        steps.append("Asigna en el contexto del Job: " + ", ".join(f"{k} = {v}" for k, v in values.items()) + ".")
    return steps


def _dedupe(connections: list[Connection]) -> list[Connection]:
    seen: set[tuple[str, str | None]] = set()
    out: list[Connection] = []
    for connection in connections:
        key = (connection.type, connection.from_step)
        if key not in seen:
            seen.add(key)
            out.append(connection)
    return out


def _fold(plan: JobPlan, occurrences: list[list[PlanStep]], body: int, layout: _Layout) -> list[str]:
    """Pliega una región: el cuerpo conserva sus pasos y cada copia restante pasa a un paso de uso."""
    jid = f"joblet-{len(plan.joblets) + 1:02d}"
    name = _unique(f"jl_{_role_of(occurrences[body])}", {j.name for j in plan.joblets})
    member_ids = [{s.id for s in steps} for steps in occurrences]
    all_members = set().union(*member_ids)
    job = plan.job_name
    body_steps = occurrences[body]
    body_ids = {s.id for s in body_steps}

    consumers = {
        s.id for s in plan.steps
        if s.id not in all_members and any(c.from_step in all_members for c in s.connections)
    }
    external = {
        c.from_step
        for steps in occurrences for s in steps for c in s.connections
        if c.from_step is not None and c.from_step not in all_members
    }
    inputs = [f"tabla_entrada_{i}" for i in range(1, len(external) + 1)]
    outputs = [f"tabla_salida_{i}" for i in range(1, len(consumers) + 1)]

    owner: dict[str, str] = {sid: sid for sid in body_ids}
    for m, steps in enumerate(occurrences):
        if m != body:
            owner.update({s.id: f"{jid}-uso{m + 1}" for s in steps})
    use_step: dict[int, PlanStep] = {}
    for m, steps in enumerate(occurrences):
        if m == body:
            continue
        uid = f"{jid}-uso{m + 1}"
        incoming = [c for s in steps for c in s.connections if c.from_step not in member_ids[m]]
        values = layout.values[m]
        purpose = f"Usa el joblet {name}" + (
            " (" + ", ".join(f"{k}={v}" for k, v in values.items()) + ")." if values else "."
        )
        first = steps[0]
        step = PlanStep(
            id=uid,
            order=first.order,
            subjob=first.subjob,
            action="add_component",
            component_candidate="por_determinar",
            alternatives=["Joblet"],
            purpose=purpose,
            evidence=first.evidence,
            joblet_id=jid,
            why=(
                f"Copia {m + 1} de un bloque de {len(body_steps)} pasos repetido {len(occurrences)} veces: "
                "el joblet evita copiar sus componentes en cada aparición."
            ),
        )
        step.connections = _dedupe(
            [c.model_copy(update={"from_step": owner.get(c.from_step, c.from_step)}) for c in incoming]
        )
        use_step[m] = step
    removed = {sid for sid in owner if owner[sid] != sid}
    first_of = {steps[0].id: m for m, steps in enumerate(occurrences) if m != body}

    new_steps: list[PlanStep] = []
    for step in plan.steps:
        if step.id in first_of:
            new_steps.append(use_step[first_of[step.id]])
        if step.id in removed:
            continue
        for connection in step.connections:
            if connection.from_step in owner:
                connection.from_step = owner[connection.from_step]
        step.connections = _dedupe(step.connections)
        if step.id in body_ids:
            step.joblet_id = jid
        new_steps.append(step)
    plan.steps = new_steps
    for case in plan.validation_cases:
        case.applies_to = list(dict.fromkeys(owner.get(sid, sid) for sid in case.applies_to))

    components = [s.component_candidate for s in body_steps]
    pending = sum(1 for s in body_steps if s.action == "manual_decision")
    occurrence_plans = []
    for m, steps in enumerate(occurrences):
        label = f"líneas {steps[0].evidence.line}–{steps[-1].evidence.line}"
        if m == body:
            step_ids = [s.id for s in steps]
            usage = _body_text(name, job)
        else:
            step_ids = [use_step[m].id]
            usage = _use_text(name, job, label, layout.values[m])
        occurrence_plans.append(
            JobletOccurrence(job=job, label=label, step_ids=step_ids, values=layout.values[m], usage_steps=usage)
        )
    why = f"El mismo tramo de {len(body_steps)} pasos aparece {len(occurrences)} veces con la misma estructura. "
    why += (
        f"Solo cambian {len(layout.params)} valor(es) entre copias; se propone un joblet con esos valores como parámetros."
        if layout.params
        else "Las copias son iguales: un joblet evita mantener copias."
    )
    notices: list[str] = []
    if layout.divergences:
        why += " Divergencia entre copias: " + "; ".join(layout.divergences) + "."
        notices = [f"Joblet {name}: divergencia entre copias: " + "; ".join(layout.divergences)]
    plan.joblets.append(
        JobletPlan(
            id=jid,
            name=name,
            title=f"Bloque de {len(body_steps)} pasos repetido en {len(occurrences)} copias",
            kind="sequence",
            occurrences=occurrence_plans,
            parameters=layout.params,
            components=components,
            inputs=inputs,
            outputs=outputs,
            trigger_inputs=["inicio"],
            why=why,
            creation_steps=_creation_steps(name, components, inputs, outputs, layout.params, pending),
            operation_count=len(body_steps),
        )
    )
    if notices:
        plan.unresolved += notices
        plan.job_status = "needs_review"
    return notices


def fold_regions(plan: JobPlan) -> list[str]:
    """Pliega las regiones largas repetidas de la secuencia del Job principal (antes de repartirlo en
    partes). Devuelve los avisos de divergencia entre copias."""
    sequence = build_sequence(plan.steps)
    planned = []
    for region in find_regions(sequence.tokens):
        occurrences: list[list[PlanStep]] = []
        tokens: list[list[int]] = []
        for start, end in region.spans:
            occurrences.append([plan.steps[sequence.plan_index[p]] for p in range(start, end)])
            tokens.append(sequence.tokens[start:end])
        layout = _layout(occurrences, tokens, region.body)
        if len(layout.params) <= limits.REGION_MAX_PARAMETERS:
            planned.append((occurrences, region.body, layout))
    notices: list[str] = []
    for occurrences, body, layout in planned:
        notices += _fold(plan, occurrences, body, layout)
    return notices


def place_region_jobs(plan: JobPlan) -> None:
    """Tras repartir el plan en Jobs: cada aparición de joblet indica el Job donde está su paso."""
    by_id = {step.id: step for step in plan.steps}
    for joblet in plan.joblets:
        for occurrence in joblet.occurrences:
            step = next((by_id[sid] for sid in occurrence.step_ids if sid in by_id), None)
            if step is None or not step.job_part or step.job_part == occurrence.job:
                continue
            occurrence.job = step.job_part
            if step.alternatives == ["Joblet"]:
                occurrence.usage_steps = _use_text(joblet.name, step.job_part, occurrence.label, occurrence.values)
            else:
                occurrence.usage_steps = _body_text(joblet.name, step.job_part)
