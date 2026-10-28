"""Nombres seguros de carpetas y Jobs de Talend.

Los nombres de un proyecto SAS no se pueden copiar tal cual: Talend con Git rechaza las carpetas `tests`, `target`
y `src`; los nombres con acentos, espacios o símbolos dan problemas en el código generado; y en Windows las rutas
del workspace de Studio (el `.item` y el código Java generado, que repite las carpetas y el nombre del Job) no pasan
de 260 caracteres. Todo lo de este módulo es determinista: el mismo nombre da siempre el mismo resultado.
"""

import hashlib
import re
import unicodedata
from pathlib import PurePosixPath

#: Con Git, un Job o carpeta con estos nombres no se sube al repositorio (guía de buenas prácticas de Talend).
RESERVED_FOLDERS = frozenset({"tests", "target", "src"})
MAX_SEGMENT = 40
MAX_FOLDER_CHARS = 110
MAX_FOLDER_DEPTH = 6
MAX_JOB_NAME = 60


def _hash(text: str, size: int = 6) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:size]


def _ascii(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def folder_segment(text: str) -> str:
    """Un segmento de carpeta seguro: ASCII, sin símbolos, sin nombres reservados y de longitud acotada."""
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", _ascii(text)).strip("._- ")
    cleaned = re.sub(r"_+", "_", cleaned)
    if not cleaned:
        return "carpeta"
    if cleaned.lower() in RESERVED_FOLDERS:
        cleaned = f"{cleaned}_sas"
    if len(cleaned) > MAX_SEGMENT:
        cleaned = f"{cleaned[: MAX_SEGMENT - 7]}_{_hash(cleaned)}"
    return cleaned


def folder_path(base: str, relative: str) -> str:
    """`base` más la carpeta del programa SAS, saneada y acotada para no pasar los límites de ruta de Windows."""
    parts = [
        folder_segment(part)
        for part in PurePosixPath(relative.replace("\\", "/")).parts
        if part not in {"", ".", "..", "/"}
    ]
    if len(parts) > MAX_FOLDER_DEPTH or len("/".join(parts)) > MAX_FOLDER_CHARS:
        # Las carpetas de más (las exteriores) se funden en una sola con un hash que las distingue.
        keep = min(len(parts), 3)
        merged = "/".join(parts[: len(parts) - keep]) if len(parts) > keep else "/".join(parts)
        tail = parts[len(parts) - keep :] if len(parts) > keep else []
        parts = [f"{merged.replace('/', '_')[: MAX_SEGMENT - 7]}_{_hash(merged)}", *tail]
        joined = "/".join(parts)
        if len(joined) > MAX_FOLDER_CHARS:
            parts = [f"{joined.replace('/', '_')[: MAX_SEGMENT - 7]}_{_hash(joined)}"]
    return "/".join([base.rstrip("/"), *parts]) if parts else base


def cap_job_name(name: str) -> str:
    """Un nombre de Job de longitud acotada; los largos conservan un sufijo con hash para seguir siendo únicos."""
    if len(name) <= MAX_JOB_NAME:
        return name
    return f"{name[: MAX_JOB_NAME - 9]}_{_hash(name, 8)}"
