"""ELT: una sentencia SQL cuyo origen y destino son tablas del mismo motor se ejecuta en el motor.

Regla R45/ELT (docs/translation-rules.md): `create table <lib>.x as select ... from <lib>.y ...` con
`<lib>` un libname de motor (oracle, teradata, impala...) se sustituye por UN paso `sql_passthrough`
(componente Row del motor, p. ej. tOracleRow) con el SQL completo. No hay lectura ni escritura intermedias.

Condiciones (todas): el destino y cada origen son tablas con libref de un mismo motor con componente Row
en las reglas; todas las operaciones del grupo SQL son lectura, join, filtro, agregado, proyección,
orden, deduplicado o escritura; el SQL no contiene funciones ni macro variables que solo existen en SAS.
Si una condición falla, el grupo se deja como estaba (sin aviso: es el camino normal de datos).
"""

from __future__ import annotations

import re

from sas_grid_migrator.intermediate_representation.models import IROperation, LibraryRef

#: Tokens que solo existen en SAS: si aparecen, la sentencia no se empuja al motor.
SAS_ONLY = re.compile(
    r"\b(monotonic|calculated|input|put|ifn|ifc|catx|cats|cat|catt|substrn|intnx|intck|mdy|today|"
    r"datetime|informat|format|sysfunc|first|last)\s*\(|\bcalculated\b|&|%",
    re.IGNORECASE,
)
#: Operaciones que pueden formar parte de una sentencia SQL de motor.
ELT_TYPES = frozenset({"read", "join", "filter", "project", "aggregate", "dedupe", "sort", "union", "write"})
_REF = re.compile(r"^\s*([A-Za-z_]\w*)\.([A-Za-z_]\w*)\s*$")


def _lib(dataset: str) -> str | None:
    match = _REF.match(dataset or "")
    return match.group(1).lower() if match else None


def _engine_libs(libs: dict[str, LibraryRef], engines: dict[str, dict[str, str]]) -> dict[str, LibraryRef]:
    """Librerías con motor que tiene componente Row (las que ELT puede usar)."""
    out: dict[str, LibraryRef] = {}
    for name, ref in libs.items():
        engine = (ref.engine or "").lower()
        if engine and engines.get(engine, {}).get("row"):
            out[name.lower()] = ref
    return out


def _translate(sql: str, lib_schema: dict[str, str]) -> str:
    """Quita el libref de cada tabla y lo sustituye por su esquema (si el libname lo declara)."""
    out = sql
    for lib, schema in lib_schema.items():
        out = re.sub(rf"(?<![\w.]){re.escape(lib)}\.", f"{schema}." if schema else "", out, flags=re.IGNORECASE)
    return out


def fold_elt(
    items: list[tuple[IROperation, str]],
    libs: dict[str, LibraryRef],
    engines: dict[str, dict[str, str]],
) -> tuple[list[tuple[IROperation, str]], list[str]]:
    """Sustituye cada grupo SQL ELT por un `sql_passthrough`. Devuelve (items, avisos)."""
    engine_libs = _engine_libs(libs, engines)
    if not engine_libs:
        return items, []
    groups: dict[tuple, list[int]] = {}
    for index, (op, prefix) in enumerate(items):
        key = (prefix, op.step, op.evidence.line, op.evidence.end_line)
        groups.setdefault(key, []).append(index)

    replace: dict[int, IROperation] = {}
    drop: set[int] = set()
    notes: list[str] = []
    for indexes in groups.values():
        ops = [items[i][0] for i in indexes]
        writes = [op for op in ops if op.type == "write" and op.details.get("sql")]
        if len(writes) != 1 or any(op.type not in ELT_TYPES for op in ops):
            continue
        write = writes[0]
        target_lib = _lib(write.outputs[0]) if write.outputs else None
        if target_lib not in engine_libs:
            continue
        engine = (engine_libs[target_lib].engine or "").lower()
        sources = [d for op in ops if op.type != "write" for d in op.inputs]
        if not sources or any(_lib(d) is None or _lib(d) not in engine_libs for d in sources):
            continue
        if any((engine_libs[_lib(d)].engine or "").lower() != engine for d in sources):
            continue
        sql = write.details["sql"]
        if SAS_ONLY.search(sql):
            continue
        schemas = {lib: (engine_libs[lib].db_schema or "") for lib in {target_lib, *(_lib(d) for d in sources)}}
        translated = _translate(sql, schemas)
        replacement = IROperation(
            id=write.id,
            type="sql_passthrough",
            step=write.step,
            evidence=write.evidence,
            inputs=[],
            outputs=[write.outputs[0]],
            details={
                "statement": "execute",
                "engine": engine,
                "text": translated[:300],
                "sql": translated,
                "elt": True,
                "elt_ops": len(ops),
            },
            confidence="medium",
            notes=[
                "ELT: sentencia SAS sobre tablas de un mismo motor, ejecutada en el motor. "
                "El SQL se traslada tal cual: validar el dialecto y el esquema de cada tabla."
            ],
        )
        notes.append(f"ELT: {len(ops)} operaciones SQL de línea {write.evidence.line} resueltas en el motor {engine}")
        replace[indexes[-1]] = replacement
        drop.update(i for i in indexes if i != indexes[-1])

    if not replace:
        return items, []
    out: list[tuple[IROperation, str]] = []
    for index, (op, prefix) in enumerate(items):
        if index in drop:
            continue
        if index in replace:
            out.append((replace[index], prefix))
        else:
            out.append((op, prefix))
    return out, notes
