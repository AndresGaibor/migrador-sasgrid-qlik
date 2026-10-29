"""Instantánea mínima del proyecto para el canal de eventos de la interfaz.

El evento no transporta el proyecto entero: solo lo que cambia lo que la persona ve. Quien lo recibe
vuelve a pedir sus datos por la ruta de siempre, así el canal sigue siendo un disparador y no una
segunda fuente de verdad.
"""

from __future__ import annotations

from typing import Any

from ..persistence.store import Store


def project_activity(s: Store, project_id: str) -> dict[str, Any]:
    """Estado observable del análisis y del lote, sin rutas, programas ni Jobs completos."""
    processing = s.get_processing(project_id)
    batch = s.get_talend_apply_batch_state(project_id)
    return {
        "processing": None
        if processing is None
        else {
            "status": processing.status,
            "stage": processing.stage,
            "message": processing.message,
            "updated_at": processing.updated_at.isoformat(),
        },
        "batch": None
        if batch is None
        else {
            "status": batch["status"],
            "completed_jobs": batch["completed_jobs"],
            "total_jobs": batch["total_jobs"],
            "current_program": batch["current_program"],
            "updated_at": batch["updated_at"],
        },
    }


def activity_changed(previous: dict[str, Any] | None, current: dict[str, Any]) -> bool:
    """El primer evento siempre se emite; después, solo cuando la instantánea cambia."""
    return previous is None or previous != current
