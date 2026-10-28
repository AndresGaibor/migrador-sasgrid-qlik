"""Argumentos de `talend_jobs_create_batch` para una guía elegible por el motor offline.

`talend_jobs_create_from_spec` descarta `contexts` sin avisar; `talend_jobs_create_batch`
sí los escribe y usa la misma forma (`name`/`type`/`value`/`comment`) que el portal.
Se envía una plantilla con una sola fila vacía por Job.
"""

from typing import Any

from sas_grid_migrator.talend_adapter.eligibility import offline_blockers

_TEMPLATE_KEYS = ("jobName", "version", "folderPath", "description", "connections", "contexts")
_COMPONENT_KEYS = (
    "uniqueName",
    "componentName",
    "componentVersion",
    "label",
    "posX",
    "posY",
    "parameters",
    "schema",
)


def to_batch_arguments(spec: dict[str, Any]) -> dict[str, Any]:
    """Convierte `spec` (salida de `to_mcp_arguments`) en los argumentos de la tool.

    Lanza `ValueError` con los bloqueos si la guía no puede ir por offline.
    """
    blockers = offline_blockers(spec)
    if blockers:
        raise ValueError(f"La guía no es elegible para offline: {', '.join(blockers)}")
    template: dict[str, Any] = {key: spec[key] for key in _TEMPLATE_KEYS if spec.get(key) is not None}
    template["components"] = [
        {key: component[key] for key in _COMPONENT_KEYS if component.get(key) is not None}
        for component in spec.get("components") or []
    ]
    return {"template": template, "rows": [{}], "overwrite": False, "dryRun": False}
