"""Versionado de datasets (forma SSA) para la etapa de fusión a corriente.

Cada escritura de un dataset crea una NUEVA VERSIÓN; cada lectura apunta a la versión vigente en ese
momento (la del último escritor anterior). Con eso, un dataset de WORK que se reescribe varias veces
(copia de vuelta, reasignaciones) no necesita una escritura y una lectura por versión:

(i)   `data X; set T;` sin cambios con T temporal = alias: la versión de T pasa a X sin pasos. Lo resuelve
      `pipeline.build_flow` al no tener el grupo más operaciones que la lectura y la escritura.
(ii)  Una reescritura en sitio X -> X' cuya versión anterior X solo consume esa reescritura se FUNDE en el
      productor de X (`merge_in_place_chains`): las operaciones del bloque pasan a la misma cadena, y las
      expresiones que leen una columna ya calculada en la cadena se sustituyen por su expresión
      (`inline`), para que la cadena no se corte. N bloques seguidos dan UN tMap con N expresiones.
(iii) Una versión con un consumidor: conexión directa. Con 2 a 4: tMap con salidas múltiples
      (`pipeline._replicate`). Con más de 4 (`HASH_FAN_OUT`): se materializa UNA vez con tHashOutput y cada
      consumidor lee con su tHashInput (excepción a «sin tHash» solo para alto fan-out).
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from sas_grid_migrator.intermediate_representation.models import IROperation

Item = tuple[IROperation, str]

#: Consumidores de una versión a partir de los que se materializa con tHashOutput/tHashInput.
HASH_FAN_OUT = 4


def is_plain(dataset: str) -> bool:
    """Nombre fijo `lib.nombre` (sin macro variables ni nombres dinámicos)."""
    return bool(dataset) and "&" not in dataset and "%" not in dataset and "." in dataset


def split_groups(items: Iterable[Item]) -> list[list[Item]]:
    """Grupos consecutivos del mismo paso SAS (mismo `step` y mismo prefijo de macro)."""
    groups: list[list[Item]] = []
    for op, prefix in items:
        if groups and groups[-1][0][1] == prefix and groups[-1][0][0].step == op.step:
            groups[-1].append((op, prefix))
        else:
            groups.append([(op, prefix)])
    return groups


def _writes(group: list[IROperation]) -> list[str]:
    """Datasets que el grupo crea como versión nueva. Un PROC SORT sin OUT= reescribe su propio dataset:
    su escritura (`write`, sin entradas) es una versión nueva, pero la operación de ordenar no lo es."""
    out: list[str] = []
    for op in group:
        for dataset in op.outputs:
            if dataset in op.inputs:
                continue
            if dataset not in out:
                out.append(dataset)
    return out


def intermediate_datasets(groups: list[list[IROperation]], shared: set[str] | frozenset[str]) -> set[str]:
    """Datasets intermedios: cada lectura tiene un escritor anterior, y no los usa otro programa o macro.

    Un dataset con una sola escritura es el caso clásico. Con varias (versiones), cada lector debe tener
    alguna escritura anterior: lee la última versión vigente.
    """
    writers: dict[str, list[int]] = {}
    readers: dict[str, list[int]] = {}
    for index, group in enumerate(groups):
        for dataset in _writes(group):
            writers.setdefault(dataset, []).append(index)
        for op in group:
            for dataset in op.inputs:
                readers.setdefault(dataset, []).append(index)
    result: set[str] = set()
    for dataset, where in writers.items():
        if dataset in shared or not is_plain(dataset):
            continue
        consumers = readers.get(dataset, [])
        if consumers and all(any(w < r for w in where) for r in consumers):
            result.add(dataset)
    return result


def version_info(
    groups: list[list[IROperation]], intermediates: set[str]
) -> dict[tuple[int, str], tuple[int, bool]]:
    """Por cada versión (grupo escritor, dataset): (número de grupos que la leen, si hay otra escritura después).

    La lectura cuenta para la versión vigente en su grupo. Un grupo que lee y escribe el mismo dataset lee la
    versión anterior: esa lectura la resuelve la cadena de su propio grupo, no cuenta aquí.
    """
    current: dict[str, int] = {}
    readers: dict[tuple[int, str], set[int]] = {}
    for index, group in enumerate(groups):
        produced = {d for op in group for d in op.outputs}
        for op in group:
            for dataset in op.inputs:
                if dataset in intermediates and dataset not in produced and dataset in current:
                    readers.setdefault((current[dataset], dataset), set()).add(index)
        for dataset in _writes(group):
            if dataset in intermediates:
                current[dataset] = index
    info: dict[tuple[int, str], tuple[int, bool]] = {}
    for dataset in intermediates:
        writes = [
            index
            for index, group in enumerate(groups)
            if dataset in _writes(group)
        ]
        for position, writer in enumerate(writes):
            later = position + 1 < len(writes)
            info[(writer, dataset)] = (len(readers.get((writer, dataset), set())), later)
    return info


# ---------------------------------------------------------------- (ii) fusión de reescrituras en sitio


def _targets(ops: list[IROperation]) -> list[str]:
    return [
        str(a.get("target", "")).lower()
        for op in ops
        if op.type == "compute"
        for a in op.details.get("assignments", [])
    ]


def _conditional_names(ops: list[IROperation]) -> set[str]:
    names: set[str] = set()
    for op in ops:
        if op.type == "compute":
            for c in op.details.get("conditionals", []):
                names |= {w.lower() for w in re.findall(r"[A-Za-z_]\w*", str(c.get("text", "")))}
    return names


def _in_place_write(group: list[Item]) -> IROperation | None:
    writes = [op for op, _ in group if op.type == "write" and op.details.get("in_place")]
    return writes[0] if len(writes) == 1 and len(writes[0].outputs) == 1 else None


def _can_merge(previous: list[Item], current: list[Item]) -> bool:
    """Una reescritura en sitio de X se funde en el grupo anterior si ese grupo solo produce X y X no se
    lee en otro sitio: la versión anterior la consume solo el bloque."""
    if not previous or not current or previous[0][1] != current[0][1]:
        return False
    write = _in_place_write(current)
    if write is None:
        return False
    target = write.outputs[0]
    cur_ops = [op for op, _ in current]
    prev_ops = [op for op, _ in previous]
    cur_reads = [op for op in cur_ops if op.type == "read"]
    if len(cur_reads) != 1 or cur_reads[0].inputs != [target]:
        return False
    if any(op.type == "write" and op is not write for op in cur_ops):
        return False
    prev_writes = [op for op in prev_ops if op.type == "write"]
    if not prev_writes or any(op.outputs != [target] for op in prev_writes):
        return False
    if any(op.type == "read" and target in op.inputs for op in prev_ops):
        return False
    if any(op.type == "stateful" for op in prev_ops + cur_ops):
        return False
    if any(a.get("accumulates") for op in prev_ops + cur_ops if op.type == "compute" for a in op.details.get("assignments", [])):
        return False  # una suma (x + y) depende del valor anterior de la misma variable en el DATA step
    names = _targets([op for op in cur_ops if op.type == "compute"])
    return not (_conditional_names(cur_ops) & set(names) | _conditional_names(prev_ops) & set(names))


def _drop_target(items: list[Item], target: str) -> list[Item]:
    """Quita la asignación anterior de una columna que una reasignación posterior sustituye (ya inlined)."""
    out: list[Item] = []
    for op, prefix in items:
        if op.type == "compute" and any(str(a.get("target", "")).lower() == target for a in op.details.get("assignments", [])):
            kept = [a for a in op.details.get("assignments", []) if str(a.get("target", "")).lower() != target]
            # La operación se conserva (sin expresiones y marcada) para que su id siga en `fused_from`.
            op = op.model_copy(
                update={"details": {**op.details, "assignments": kept, "superseded": not kept}}
            )
        out.append((op, prefix))
    return out


def inline(expression: str, known: dict[str, str]) -> tuple[str, bool]:
    """Sustituye las columnas ya calculadas en la cadena por su expresión (entre paréntesis)."""
    if not known:
        return expression, False
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(name) for name in sorted(known, key=len, reverse=True)) + r")\b",
        re.IGNORECASE,
    )
    changed = False

    def replace(match: re.Match) -> str:
        nonlocal changed
        changed = True
        return f"({known[match.group(1).lower()]})"

    return pattern.sub(replace, expression), changed


def _merge(previous: list[Item], current: list[Item]) -> list[Item]:
    write = _in_place_write(current)
    assert write is not None
    step = previous[0][0].step
    prefix = previous[0][1]
    known: dict[str, str] = {}
    base = [(op, p) for op, p in previous if op.type != "write"]
    for op, _ in base:
        if op.type == "compute":
            for a in op.details.get("assignments", []):
                if not a.get("accumulates"):
                    known[str(a.get("target", "")).lower()] = str(a.get("expression", ""))
    merged: list[Item] = list(base)
    for op, _ in current:
        if op.type == "read" and op.inputs == write.outputs:
            continue
        if op is write:
            op = op.model_copy(update={"details": {**op.details, "in_place": False}})
        elif op.type == "compute":
            assignments = []
            resolved = False
            for a in op.details.get("assignments", []):
                expression, changed = inline(str(a.get("expression", "")), known)
                resolved = resolved or changed
                assignments.append({**a, "expression": expression})
                target = str(a.get("target", "")).lower()
                # La reasignación sustituye a la anterior: la columna queda con su última expresión.
                merged = _drop_target(merged, target)
                known[target] = expression
            details = {**op.details, "assignments": assignments}
            if resolved:
                details["resolved_inputs"] = True
            op = op.model_copy(update={"details": details})
        elif op.type == "filter":
            expression, changed = inline(str(op.details.get("expression", "")), known)
            if changed:
                op = op.model_copy(update={"details": {**op.details, "expression": expression, "resolved_inputs": True}})
        # X ya no viene de fuera del grupo: su versión anterior la produce la propia cadena.
        op = op.model_copy(update={"step": step, "inputs": [d for d in op.inputs if d != write.outputs[0]]})
        merged.append((op, prefix))
    return merged


def merge_in_place_chains(items: list[Item]) -> list[Item]:
    """Funde cada reescritura en sitio con el grupo anterior que produce la versión que reescribe."""
    merged: list[list[Item]] = []
    for group in split_groups(items):
        if merged and _can_merge(merged[-1], group):
            merged[-1] = _merge(merged[-1], group)
        else:
            merged.append(group)
    return [item for group in merged for item in group]
