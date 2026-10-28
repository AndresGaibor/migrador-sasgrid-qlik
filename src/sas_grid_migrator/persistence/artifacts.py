"""Escritura atómica de artefactos derivados del proyecto."""

import os
import tempfile
from pathlib import Path


def write_text_atomic(path: Path, content: str) -> None:
    """Reemplaza un archivo de texto sin exponer un contenido parcial."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
