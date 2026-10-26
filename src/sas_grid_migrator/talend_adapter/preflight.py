"""Clasifica los destinos de Talend antes de aplicar un proyecto."""

from typing import Any

from sas_grid_migrator.talend_adapter.apply_spec import TalendApplySpec


def _path_parts(value: str) -> list[str]:
    return [part for part in value.replace("\\", "/").split("/") if part]


def _target_folder(folder_path: str) -> str:
    parts = [part.casefold() for part in _path_parts(folder_path)]
    if not parts or parts[0] != "process":
        parts.insert(0, "process")
    return "/".join(parts)


def _job_folder(job: dict[str, Any]) -> str | None:
    name = job.get("name")
    path = job.get("path")
    if not isinstance(name, str) or not isinstance(path, str):
        return None

    name_key = name.casefold()
    parts = [part.casefold() for part in _path_parts(path)]
    process_index = next(
        (index for index in range(len(parts) - 1, -1, -1) if parts[index] == "process"),
        None,
    )
    if process_index is None:
        return None

    relative = parts[process_index + 1 :]
    if not relative or not relative[-1].endswith(".item"):
        return None
    filename = relative[-1][:-5]
    if len(relative) >= 2 and relative[-2] == name_key and filename.startswith(f"{name_key}_"):
        folder_parts = relative[:-2]
    elif filename.startswith(f"{name_key}_"):
        folder_parts = relative[:-1]
    else:
        return None
    return "/".join(["process", *folder_parts])


def classify_jobs(
    specs: list[TalendApplySpec], inventory: list[dict[str, Any]]
) -> dict[str, Any]:
    """Indica si cada Job debe crearse, actualizarse o resolverse por colisión."""
    actions: list[dict[str, Any]] = []
    for spec in specs:
        name_key = spec.job_name.casefold()
        same_name = [
            item
            for item in inventory
            if isinstance(item.get("name"), str) and item["name"].casefold() == name_key
        ]
        target = _target_folder(spec.folder_path)
        exact = [item for item in same_name if _job_folder(item) == target]

        if len(exact) == 1:
            action = "update"
            existing_path = exact[0].get("path")
            reason = None
        elif len(exact) > 1:
            action = "conflict"
            existing_path = exact[0].get("path")
            reason = f"Hay más de un Job {spec.job_name} en la carpeta de destino."
        elif same_name:
            action = "conflict"
            existing_path = same_name[0].get("path")
            reason = f"Ya existe un Job {spec.job_name} fuera de la carpeta configurada."
        else:
            action = "create"
            existing_path = None
            reason = None

        actions.append(
            {
                "program": spec.program,
                "job_name": spec.job_name,
                "folder_path": spec.folder_path,
                "action": action,
                "existing_path": existing_path,
                "reason": reason,
            }
        )

    return {
        "jobs": actions,
        "create_count": sum(item["action"] == "create" for item in actions),
        "update_count": sum(item["action"] == "update" for item in actions),
        "conflict_count": sum(item["action"] == "conflict" for item in actions),
    }
