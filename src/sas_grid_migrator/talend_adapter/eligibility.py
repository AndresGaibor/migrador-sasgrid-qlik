"""Elegibilidad de una guía para el motor offline de `talend_job_apply_custom_spec`.

El motor offline escribe `.item`/`.properties` sin Studio. Soporta parámetros, esquemas
y tablas (`tables`, p. ej. las condiciones de un `tFilterRow`; el MCP traduce los nombres de
las listas a sus valores), pero no el `mapper` de un `tMap`, que Studio configura al
conectarlo. Los `childJobs` se escriben como Jobs aparte. Esta función dice, antes de
enviar nada, si una especificación puede ir por ese camino.
"""

import re
from typing import Any

# `talend_jobs_create_batch` expande `{{variable}}` en todos los textos de la plantilla.
_PLACEHOLDER = re.compile(r"\{\{\s*[A-Za-z0-9_.-]+\s*\}\}")


def _has_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        return bool(_PLACEHOLDER.search(value))
    if isinstance(value, dict):
        return any(_has_placeholder(item) for item in value.values())
    if isinstance(value, list):
        return any(_has_placeholder(item) for item in value)
    return False


def offline_blockers(spec: dict[str, Any], *, allow_children: bool = False) -> list[str]:
    """Lista los motivos por los que `spec` no puede aplicarse offline.

    Vacía si la especificación es elegible. Cada bloqueo nombra el componente
    (`mapper:<uniqueName>`, `placeholder:<uniqueName>`) o el
    campo (`childJobs`, `placeholder:contexts`).
    """
    blockers: list[str] = []
    for component in spec.get("components") or []:
        if not isinstance(component, dict):
            continue
        unique_name = str(component.get("uniqueName") or "?")
        if component.get("mapper"):
            blockers.append(f"mapper:{unique_name}")
        if (
            _has_placeholder(component.get("parameters"))
            or _has_placeholder(component.get("schema"))
            or _has_placeholder(component.get("tables"))
        ):
            blockers.append(f"placeholder:{unique_name}")
    if spec.get("childJobs") and not allow_children:
        blockers.append("childJobs")
    if _has_placeholder(spec.get("contexts")):
        blockers.append("placeholder:contexts")
    return blockers


def offline_tree_blockers(spec: dict[str, Any]) -> list[str]:
    """Bloqueos de un Job y de todos sus Jobs hijo (cada uno se escribe offline por su cuenta)."""
    blockers = offline_blockers(spec, allow_children=True)
    for child in spec.get("childJobs") or []:
        if isinstance(child, dict):
            blockers.extend(f"{child.get('jobName', '?')}:{item}" for item in offline_tree_blockers(child))
    return blockers
