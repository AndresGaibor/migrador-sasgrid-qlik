"""Copia de vuelta (R23): mutación de X en sitio mediante un temporal.

Forma SAS que se detecta (cada bloque, en este orden):

    data T;  format c $n.;  set X(rename=(c=c_old));  c = expr(c_old);  drop c_old;  run;   (G1)
    data X;  set T;  run;                                                                    (G2)
    proc delete data=T;  run;                                                                (fontanería)

La forma sin `rename=` (`data T; set X; c = expr(c); run;`) también se acepta.

Se funde en UN bloque que escribe X en sitio: G1 pasa a escribir X (marcado `in_place`, que no cuenta
como productor nuevo) y G2 desaparece. Así X se encadena como cualquier intermedio: los bloques
sucesivos leen el resultado del anterior y no hay temporal, ni escritura ni lectura de T.

El `rename=` de la lectura no llega al tMap: el nombre nuevo (`c_old`) es el valor de entrada de la
columna `c`. Las expresiones de G1 que lo citan se reescriben con el nombre original, y los `drop` de
ese nombre desaparecen (no quitan nada: `c` lo recalcula el bloque).

Condiciones (todas): T y X son datasets simples (sin macro variables); T lo escribe solo G1 y lo lee solo
G2; G1 lee X solo con `rename=` (sin keep=, drop= ni where=); cada nombre nuevo del rename se elimina con
`drop` o queda fuera de un `keep` de G1 (si no, la columna sobreviviría y no se reproduce); G2 lee T sin
opciones; ningún otro grupo lee X entre G1 y G2 (vería el valor viejo); G1 y G2 no contienen escrituras
ni lecturas adicionales.
"""

from __future__ import annotations

import re

from sas_grid_migrator.intermediate_representation.builder import dataset_options
from sas_grid_migrator.intermediate_representation.models import IROperation

Item = tuple[IROperation, str]


def _plain(dataset: str) -> bool:
    return bool(dataset) and "&" not in dataset and "%" not in dataset and "." in dataset


def _group_key(op: IROperation, prefix: str) -> tuple[str, str]:
    return (prefix, op.step)


def _read_options_ok(read: IROperation) -> bool:
    """Una lectura de X solo puede llevar `rename=`: keep, drop y where cambian filas o columnas."""
    return set(dataset_options(read.details.get("options"))) <= {"rename"}


def _input_renames(group_ops: list[IROperation], target_x: str) -> list[IROperation]:
    """Renombres que vienen de la lectura de X (`set X(rename=...)`), no de una sentencia RENAME."""
    return [op for op in group_ops if op.type == "rename" and op.inputs == [target_x] and not op.outputs]


def _column_names(renames: list[IROperation]) -> dict[str, str]:
    """Nombre dentro del programa -> nombre de la columna de entrada (`rename=(c=c_old)`: c_old -> c)."""
    out: dict[str, str] = {}
    for op in renames:
        for column, program_name in op.details.get("mapping", {}).items():
            out[str(program_name)] = str(column)
    return out


def _renames_are_consumed(group_ops: list[IROperation], program_names: set[str]) -> bool:
    """Cada nombre nuevo debe desaparecer (drop) o quedar fuera de un keep del mismo grupo."""
    for name in program_names:
        for op in group_ops:
            if op.type != "select_columns":
                continue
            keep = [str(k).lower() for k in op.details.get("keep") or []]
            drop = [str(k).lower() for k in op.details.get("drop") or []]
            if name.lower() in drop or (keep and name.lower() not in keep):
                break
        else:
            return False
    return True


def _find_block(items: list[Item]) -> tuple[int, int] | None:
    """(índice de la escritura de G1, índice de la escritura de G2) del primer bloque fundible."""
    groups: dict[tuple[str, str], list[int]] = {}
    for index, (op, prefix) in enumerate(items):
        groups.setdefault(_group_key(op, prefix), []).append(index)
    for index2, (write2, prefix2) in enumerate(items):
        if write2.type != "write" or write2.details.get("in_place") or write2.details.get("sql"):
            continue
        if len(write2.outputs) != 1 or not _plain(write2.outputs[0]):
            continue
        target_x = write2.outputs[0]
        g2 = groups[_group_key(write2, prefix2)]
        ops2 = [items[j][0] for j in g2]
        reads2 = [items[j][0] for j in g2 if items[j][0].type == "read"]
        if len(reads2) != 1 or len(reads2[0].inputs) != 1 or reads2[0].details.get("options"):
            continue
        if any(op.type not in ("read", "write", "infrastructure") for op in ops2):
            continue
        if any(op.type == "write" and op is not write2 for op in ops2):
            continue
        temp = reads2[0].inputs[0]
        if temp.casefold() == target_x.casefold() or not _plain(temp) or not temp.lower().startswith("work."):
            continue
        # El temporal se reutiliza en cada bloque (p. ej. WORK.TEMPORAL): G1 es el último escritor de T
        # antes de G2, y nadie más lo escribe entre G1 y G2.
        writers = [k for k, (op, _) in enumerate(items) if op.type == "write" and temp in op.outputs]
        before = [k for k in writers if k < index2]
        if not before:
            continue
        index1 = before[-1]
        write1, prefix1 = items[index1]
        if prefix1 != prefix2 or write1.details.get("sql"):
            continue
        g1 = groups[_group_key(write1, prefix1)]
        ops1 = [items[j][0] for j in g1]
        reads1 = [op for op in ops1 if op.type == "read"]
        if len(reads1) != 1 or reads1[0].inputs != [target_x] or not _read_options_ok(reads1[0]):
            continue
        if any(op.type == "write" and op is not write1 for op in ops1):
            continue
        renames = _input_renames(ops1, target_x)
        if not _renames_are_consumed(ops1, set(_column_names(renames))):
            continue
        # T solo lo lee G2 (la limpieza de WORK no cuenta como lectura de datos).
        following = [k for k in writers if k > index1]
        limit = following[0] if following else len(items)
        readers = [
            k for k, (op, _) in enumerate(items)
            if index1 < k < limit and temp in op.inputs and op.type != "infrastructure" and k not in g2
        ]
        if readers:
            continue
        # Nadie lee X entre G1 y G2 (vería el valor anterior al bloque).
        if any(
            target_x in op.inputs and k not in g1 and k not in g2
            for k, (op, _) in enumerate(items)
            if index1 < k < index2
        ):
            continue
        if any(
            target_x in op.outputs and k not in g1 and k not in g2
            for k, (op, _) in enumerate(items)
            if index1 < k < index2
        ):
            continue
        return index1, index2
    return None


def _substitute(text: str, names: dict[str, str]) -> str:
    """Cambia cada nombre del programa por el nombre de la columna de entrada."""
    for program_name, column in names.items():
        text = re.sub(rf"\b{re.escape(program_name)}\b", column, text, flags=re.IGNORECASE)
    return text


def _rewrite_group(ops: list[IROperation], target_x: str, names: dict[str, str]) -> list[IROperation]:
    """G1 sin el rename de entrada: sus expresiones leen la columna original y los nombres nuevos se van."""
    dropped = {name.lower() for name in names}
    out: list[IROperation] = []
    for op in ops:
        if op.type == "rename" and op.inputs == [target_x] and not op.outputs:
            continue
        details = dict(op.details)
        if op.type == "read":
            details["options"] = None
        elif op.type == "compute":
            details["assignments"] = [
                {**a, "expression": _substitute(str(a.get("expression", "")), names)}
                for a in op.details.get("assignments", [])
            ]
            details["conditionals"] = [
                {**c, "text": _substitute(str(c.get("text", "")), names)}
                for c in op.details.get("conditionals", [])
            ]
        elif op.type == "filter":
            details["expression"] = _substitute(str(op.details.get("expression", "")), names)
        elif op.type == "select_columns":
            if op.details.get("drop"):
                details["drop"] = [k for k in op.details["drop"] if str(k).lower() not in dropped]
            if op.details.get("keep"):
                details["keep"] = [names.get(str(k), str(k)) for k in op.details["keep"]]
        if op.type == "select_columns" and not details.get("keep") and not details.get("drop"):
            continue  # el único drop era el nombre nuevo del rename: no quita nada
        out.append(op.model_copy(update={"details": details}))
    return out


def fold_copy_back(items: list[Item]) -> tuple[list[Item], int]:
    """Funde cada bloque de copia de vuelta. Devuelve (items, número de bloques fundidos)."""
    folded = 0
    while True:
        block = _find_block(items)
        if block is None:
            return items, folded
        index1, index2 = block
        _, prefix1 = items[index1]
        target_x = items[index2][0].outputs[0]
        g1_indices = sorted(_group_members(items, index1))
        g1_ops = [items[k][0] for k in g1_indices]
        names = _column_names(_input_renames(g1_ops, target_x))
        rewritten = _rewrite_group(g1_ops, target_x, names)
        # La escritura de G1 pasa a ser la escritura en sitio de X.
        rewritten = [
            op.model_copy(
                update={
                    "outputs": [target_x],
                    "details": {**op.details, "in_place": True, "dataset": target_x},
                    "notes": [*op.notes, f"Copia de vuelta fundida: escritura en sitio sobre {target_x}"],
                }
            )
            if op.type == "write"
            else op
            for op in rewritten
        ]
        drop = _group_members(items, index2)
        new_items: list[Item] = []
        for k, item in enumerate(items):
            if k == g1_indices[0]:
                new_items.extend((op, prefix1) for op in rewritten)
            elif k in g1_indices or k in drop:
                continue
            else:
                new_items.append(item)
        items = new_items
        folded += 1


def _group_members(items: list[Item], index: int) -> set[int]:
    """Índices de las operaciones que forman el mismo grupo SAS que items[index]."""
    op, prefix = items[index]
    return {k for k, (other, p) in enumerate(items) if p == prefix and other.step == op.step}
