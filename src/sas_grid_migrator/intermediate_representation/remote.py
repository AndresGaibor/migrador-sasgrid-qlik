"""Transferencias remotas (R50): `proc export` a local seguido de `proc upload` a la ruta remota.

Forma SAS: `proc export data=X outfile='A' ...;` y, después, `proc upload infile='A' outfile='B';` dentro de
un `rsubmit`. El resultado de Talend es una sola escritura directa a B (la ruta que ve el Remote Engine):
la copia local A y la subida se registran como fontanería (`transferencia_remota`) en not_migrated.

Solo se funde el par exacto (misma ruta A, subida posterior a la exportación). Una subida sin exportación
previa de la misma ruta queda como operación sin traducir, para revisión manual.
"""

from __future__ import annotations

import re
from dataclasses import asdict

from sas_grid_migrator.intermediate_representation.models import IROperation, ProgramIR

_OPTION = re.compile(r"""(infile|outfile)\s*=\s*(?:'([^']*)'|"([^"]*)"|(\S+))""", re.IGNORECASE)


def _norm(path: str) -> str:
    return path.replace("/", "\\").strip().casefold()


def _upload_paths(op: IROperation) -> tuple[str, str] | None:
    options = str(op.details.get("options") or "")
    found = {m.group(1).lower(): next(g for g in m.groups()[1:] if g) for m in _OPTION.finditer(options)}
    if "infile" in found and "outfile" in found:
        return found["infile"], found["outfile"]
    return None


def _fold_uploads(ops: list[IROperation]) -> None:
    from sas_grid_migrator.migration_planner.plumbing import Plumbing

    for upload in ops:
        if upload.type != "unsupported" or str(upload.details.get("proc", "")).lower() != "upload":
            continue
        paths = _upload_paths(upload)
        if paths is None:
            continue
        local, remote = paths
        exports = [
            op
            for op in ops
            if op.type == "write_file"
            and op.evidence.line < upload.evidence.line
            and _norm(str(op.details.get("file") or "")) == _norm(local)
        ]
        if not exports:
            continue
        export = exports[-1]
        export.details = {**export.details, "file": remote, "remote_from": local}
        export.notes = [
            *export.notes,
            f"Exportación con copia remota fundida: se escribe directamente en {remote}",
        ]
        upload.type = "infrastructure"
        upload.details = {
            **upload.details,
            "plumbing": asdict(
                Plumbing(
                    "transferencia_remota",
                    "copia del fichero exportado a la ruta remota (proc upload)",
                    "La subida solo copia el fichero ya exportado; no transforma filas.",
                    "tFileOutputDelimited escribe en la ruta remota del contexto; sin copia local ni sesión.",
                )
            ),
        }


def fold_remote_transfers(ir: ProgramIR) -> None:
    """Aplica el par export+upload a cada lista de operaciones del programa y de sus macros."""
    _fold_uploads(ir.operations)
    for macro in ir.macros:
        _fold_uploads(macro.operations)
