"""Elegibilidad de una guía para el motor offline de `talend_job_apply_custom_spec`.

El motor offline escribe `.item`/`.properties` sin Studio y no soporta `mapper`
(tMap), `tables` (parámetros de tipo TABLE) ni `childJobs`. Esta función dice,
antes de enviar nada, si una especificación puede ir por ese camino.
"""

from typing import Any


def offline_blockers(spec: dict[str, Any]) -> list[str]:
    """Lista los motivos por los que `spec` no puede aplicarse offline.

    Vacía si la especificación es elegible. Cada bloqueo nombra el componente
    (`mapper:<uniqueName>`, `tables:<uniqueName>`) o el campo (`childJobs`).
    """
    blockers: list[str] = []
    for component in spec.get("components") or []:
        if not isinstance(component, dict):
            continue
        unique_name = str(component.get("uniqueName") or "?")
        if component.get("mapper"):
            blockers.append(f"mapper:{unique_name}")
        if component.get("tables"):
            blockers.append(f"tables:{unique_name}")
    if spec.get("childJobs"):
        blockers.append("childJobs")
    return blockers
