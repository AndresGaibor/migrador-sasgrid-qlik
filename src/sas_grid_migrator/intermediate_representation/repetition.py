"""Bloques repetidos de la representación intermedia (base de los joblets).

Dos bloques son "el mismo" si tienen la misma secuencia de tipos de operación y la misma forma en
sus entradas, salidas y detalles. Los nombres de tabla y los literales no cuentan: se sustituyen por
marcadores (`D1`, `D2`… para datasets; `lit` para valores) y cada valor concreto queda como un
*slot*. Los slots que cambian entre apariciones son los parámetros del joblet.

Dos fuentes de bloques:
- cuerpos de macro (`MacroIR`): cada macro es una unidad;
- ventanas de pasos SAS consecutivos del programa principal (operaciones de nivel superior).
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Literal

from sas_grid_migrator.intermediate_representation.models import IROperation, MacroIR
from sas_grid_migrator.migration_planner.limits import (
    JOBLET_MAX_WINDOW_STEPS,
    JOBLET_MIN_OCCURRENCES,
    JOBLET_MIN_OPERATIONS,
)

#: Claves de `details` que solo describen la posición en el código.
# `sql`: texto de un create/insert. Lo describen ya las operaciones de la consulta (filtros, joins,
# proyecciones), así que no entra en la huella; si entrara, cada tabla daría un literal distinto.
_POSITION_KEYS = frozenset({"line", "evidence", "loc", "sql"})
#: Claves de `details` que nombran un dataset: su valor es una referencia, no un parámetro propio
#: (el dataset ya entra por `inputs`/`outputs`).
_DATASET_KEYS = frozenset({"dataset", "table", "in_var", "alias"})
#: Valores de texto que definen el tipo de operación: se conservan tal cual, no se parametrizan.
_SEMANTIC_KEYS = frozenset(
    {
        "kind",
        "mode",
        "proc",
        "statement",
        "join_type_guess",
        "origin",
        "constructs",
        "name",
        "view",
        "in_place",
        "set_operations",
        "distinct",
    }
)
#: Operaciones que no generan paso propio (igual que en el planificador).
_SKIPPED_TYPES = frozenset({"include"})
#: Solo orquestan (llaman a macros o fijan variables): un bloque así no tiene lógica de datos que
#: convertir en joblet, aunque se repita.
_ORCHESTRATION_TYPES = frozenset({"macro_call", "set_variable", "include", "os_command"})


@dataclass(frozen=True)
class Slot:
    """Valor concreto de una posición parametrizable del bloque."""

    hint: str  # pista de nombre: "tabla_entrada", "compute.assignments.expression"…
    value: str
    kind: Literal["in", "out", "valor"]


@dataclass
class Occurrence:
    label: str  # "macro %nombre (línea 12)" o "pasos s12–s30"
    ops: list[IROperation]
    slots: list[Slot]
    macro: str | None = None  # nombre de la macro (solo unidades macro)


@dataclass
class Repetition:
    kind: Literal["macro", "sequence"]
    fingerprint: str
    template_types: list[str]
    occurrences: list[Occurrence] = field(default_factory=list)

    @property
    def operation_count(self) -> int:
        return len(self.occurrences[0].ops) if self.occurrences else 0


def _shape(value: Any, key: str, path: str, slots: list[Slot]) -> Any:
    """Forma normalizada de un valor de `details`; los literales van a `slots` y quedan como `lit`."""
    if isinstance(value, dict):
        return {
            k: _shape(v, k, f"{path}.{k}" if path else k, slots)
            for k, v in sorted(value.items())
            if k not in _POSITION_KEYS
        }
    if isinstance(value, list):
        return {"len": len(value), "items": [_shape(v, key, path, slots) for v in value]}
    if value is None or isinstance(value, bool):
        return value
    if key in _DATASET_KEYS:
        return "ref"
    if key in _SEMANTIC_KEYS and isinstance(value, str):
        return value
    slots.append(Slot(hint=path, value=" ".join(str(value).split()), kind="valor"))
    return "lit"


def block_fingerprint(ops: list[IROperation]) -> tuple[str, list[Slot]]:
    """Huella estructural de un bloque y sus valores concretos (slots) en orden fijo."""
    placeholders: dict[str, str] = {}
    slots: list[Slot] = []
    shape: list[Any] = []

    def placeholder(dataset: str, side: Literal["in", "out"]) -> str:
        if dataset not in placeholders:
            placeholders[dataset] = f"D{len(placeholders) + 1}"
            slots.append(
                Slot(hint=f"tabla_{'entrada' if side == 'in' else 'salida'}", value=dataset, kind=side)
            )
        return placeholders[dataset]

    for op in ops:
        ins = [placeholder(dataset, "in") for dataset in op.inputs]
        outs = [placeholder(dataset, "out") for dataset in op.outputs]
        details = _shape(op.details, "", op.type, slots)
        shape.append([op.type, ins, outs, details, len(op.constructs)])
    text = json.dumps(shape, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(text.encode("utf-8")).hexdigest(), slots


def _group_steps(ops: list[IROperation]) -> list[list[IROperation]]:
    """Agrupa operaciones consecutivas del mismo paso SAS (un DATA step o PROC SQL es un paso)."""
    groups: list[list[IROperation]] = []
    for op in ops:
        if op.type in _SKIPPED_TYPES:
            continue
        if groups and groups[-1][0].step == op.step:
            groups[-1].append(op)
        else:
            groups.append([op])
    return groups


def _orchestration_only(ops: list[IROperation]) -> bool:
    return all(op.type in _ORCHESTRATION_TYPES for op in ops)


def _step_range(ops: list[IROperation]) -> str:
    steps = list(dict.fromkeys(op.step for op in ops))
    return steps[0] if len(steps) == 1 else f"{steps[0]}–{steps[-1]}"


def _cluster_units(
    units: list[Occurrence], min_occurrences: int, min_operations: int
) -> list[Repetition]:
    buckets: dict[str, list[Occurrence]] = {}
    order: list[str] = []
    for unit in units:
        if len(unit.ops) < min_operations or _orchestration_only(unit.ops):
            continue
        fingerprint, slots = block_fingerprint(unit.ops)
        unit.slots = slots
        if fingerprint not in buckets:
            buckets[fingerprint] = []
            order.append(fingerprint)
        buckets[fingerprint].append(unit)
    result = []
    for fingerprint in order:
        occurrences = buckets[fingerprint]
        if len(occurrences) >= min_occurrences:
            result.append(
                Repetition(
                    kind="macro",
                    fingerprint=fingerprint,
                    template_types=[op.type for op in occurrences[0].ops],
                    occurrences=occurrences,
                )
            )
    return result


def find_macro_repetitions(
    macros: list[MacroIR],
    *,
    min_occurrences: int = JOBLET_MIN_OCCURRENCES,
    min_operations: int = JOBLET_MIN_OPERATIONS,
) -> list[Repetition]:
    """Macros cuyo cuerpo tiene la misma forma (incluidas las variantes `_v2`… con otra tabla)."""
    units: list[Occurrence] = []
    for macro in macros:
        # Las copias idénticas se colapsaron en el IR: cada una cuenta como aparición en el código.
        for line in [macro.loc.line, *macro.duplicate_lines]:
            units.append(
                Occurrence(
                    label=f"macro %{macro.name} (línea {line})",
                    ops=list(macro.operations),
                    slots=[],
                    macro=macro.name,
                )
            )
    return _cluster_units(units, min_occurrences, min_operations)


def find_sequence_repetitions(
    operations: list[IROperation],
    *,
    min_occurrences: int = JOBLET_MIN_OCCURRENCES,
    min_operations: int = JOBLET_MIN_OPERATIONS,
    max_window_steps: int = JOBLET_MAX_WINDOW_STEPS,
) -> list[Repetition]:
    """Secuencias de pasos SAS consecutivos del programa que se repiten.

    Se elige primero el bloque que cubre más pasos (apariciones × pasos), no el más largo: si un
    patrón de 3 pasos aparece 5 veces, gana frente a un patrón de 6 pasos que solo aparece 2. Un paso
    usado por un bloque no entra en otro."""
    groups = _group_steps(operations)
    count = len(groups)
    candidates: list[tuple[int, int, str, list[tuple[int, list[IROperation], list[Slot]]]]] = []
    for size in range(1, min(max_window_steps, count) + 1):
        buckets: dict[str, list[tuple[int, list[IROperation], list[Slot]]]] = {}
        for start in range(count - size + 1):
            ops = [op for group in groups[start : start + size] for op in group]
            if len(ops) < min_operations or _orchestration_only(ops):
                continue
            fingerprint, slots = block_fingerprint(ops)
            buckets.setdefault(fingerprint, []).append((start, ops, slots))
        for fingerprint, found in buckets.items():
            chosen: list[tuple[int, list[IROperation], list[Slot]]] = []
            next_free = 0
            for start, ops, slots in found:
                if start < next_free:
                    continue
                chosen.append((start, ops, slots))
                next_free = start + size
            if len(chosen) >= min_occurrences:
                candidates.append((len(chosen) * size, size, fingerprint, chosen))
    candidates.sort(key=lambda item: (-item[0], -item[1], item[3][0][0]))
    claimed = [False] * count
    result: list[Repetition] = []
    for _, size, fingerprint, chosen in candidates:
        free = [occ for occ in chosen if not any(claimed[occ[0] : occ[0] + size])]
        if len(free) < min_occurrences:
            continue
        for start, _, _ in free:
            for index in range(start, start + size):
                claimed[index] = True
        result.append(
            Repetition(
                kind="sequence",
                fingerprint=fingerprint,
                template_types=[op.type for op in free[0][1]],
                occurrences=[
                    Occurrence(label=f"pasos {_step_range(ops)}", ops=ops, slots=slots)
                    for _, ops, slots in free
                ],
            )
        )
    result.sort(key=lambda rep: rep.occurrences[0].ops[0].evidence.line)
    return result


def find_feed_repetitions(
    operations: list[IROperation],
    *,
    min_occurrences: int = JOBLET_MIN_OCCURRENCES,
    min_operations: int = JOBLET_MIN_OPERATIONS,
) -> list[Repetition]:
    """Bloques que producen una tabla WORK y la entregan al motor (transferencia `transfer`).

    La unidad es el paso que produce la tabla más la transferencia. Las unidades con la misma forma (y
    literales distintos, p. ej. la marca de un filtro) son un joblet: el productor y la transferencia no
    tienen que estar contiguos en el programa."""
    buckets: dict[str, list[Occurrence]] = {}
    order: list[str] = []
    for index, transfer in enumerate(operations):
        if not transfer.details.get("transfer") or not transfer.inputs:
            continue
        dataset = transfer.inputs[0].casefold()
        producer = next(
            (op for op in reversed(operations[:index]) if any(d.casefold() == dataset for d in op.outputs)),
            None,
        )
        if producer is None:
            continue
        unit = [op for op in operations[:index] if op.step == producer.step] + [transfer]
        if len(unit) < min_operations:
            continue
        fingerprint, slots = block_fingerprint(unit)
        if fingerprint not in buckets:
            buckets[fingerprint] = []
            order.append(fingerprint)
        buckets[fingerprint].append(Occurrence(label=f"paso {producer.step} -> transferencia", ops=unit, slots=slots))
    result = []
    for fingerprint in order:
        occurrences = buckets[fingerprint]
        if len(occurrences) >= min_occurrences:
            result.append(
                Repetition(
                    kind="feed",
                    fingerprint=fingerprint,
                    template_types=[op.type for op in occurrences[0].ops],
                    occurrences=occurrences,
                )
            )
    return result


def find_repetitions(
    macros: list[MacroIR],
    operations: list[IROperation],
    *,
    min_occurrences: int = JOBLET_MIN_OCCURRENCES,
    min_operations: int = JOBLET_MIN_OPERATIONS,
    max_window_steps: int = JOBLET_MAX_WINDOW_STEPS,
) -> list[Repetition]:
    """Repeticiones de macros, de transferencias al motor y de secuencias, en orden de aparición.

    Las operaciones que ya forman una repetición de transferencia no entran en las secuencias."""
    found = find_macro_repetitions(
        macros, min_occurrences=min_occurrences, min_operations=min_operations
    )
    feed = find_feed_repetitions(
        operations, min_occurrences=min_occurrences, min_operations=min_operations
    )
    found += feed
    claimed = {op.id for rep in feed for occ in rep.occurrences for op in occ.ops}
    operations = [op for op in operations if op.id not in claimed]
    found += find_sequence_repetitions(
        operations,
        min_occurrences=min_occurrences,
        min_operations=min_operations,
        max_window_steps=max_window_steps,
    )
    found.sort(key=lambda rep: rep.occurrences[0].ops[0].evidence.line if rep.occurrences[0].ops else 0)
    return found
