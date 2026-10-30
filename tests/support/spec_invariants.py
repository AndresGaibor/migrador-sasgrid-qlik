"""Lo que cualquier Job generado por el portal debe cumplir, sea cual sea el proyecto SAS de origen.

Cada funcion devuelve una lista de problemas en texto (vacia si todo esta bien), para que una prueba pueda mostrar
todos los fallos de golpe y no solo el primero.
"""

import re
from collections import Counter
from collections.abc import Iterator
from typing import Any

from sas_grid_migrator.talend_adapter.best_practices import check_job_arguments
from sas_grid_migrator.talend_adapter.naming import MAX_FOLDER_CHARS, MAX_JOB_NAME, RESERVED_FOLDERS

JOB_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
COMPONENT_NAME = re.compile(r"^t[A-Za-z0-9_]+$")
UNIQUE_NAME = re.compile(r"^[A-Za-z_]\w*$")
CONTEXT_NAME = re.compile(r"^[A-Za-z_]\w*$")
CONNECTORS = {
    "FLOW", "FILTER", "UNIQUE", "DUPLICATE", "REJECT", "SUBJOB_OK", "SUBJOB_ERROR", "COMPONENT_OK", "COMPONENT_ERROR", "ITERATE", "RUN_IF",
}
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def walk(arguments: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """El Job y todos sus Jobs hijo, el padre primero."""
    yield arguments
    for child in arguments.get("childJobs") or []:
        yield from walk(child)


def _texts(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _texts(item)
    elif isinstance(value, list):
        for item in value:
            yield from _texts(item)


def job_problems(where: str, job: dict[str, Any], *, component_limit: int) -> list[str]:
    problems: list[str] = []
    name = str(job.get("jobName"))
    if not JOB_NAME.match(name):
        problems.append(f"{where}: nombre de Job invalido {name!r}")
    if len(name) > MAX_JOB_NAME:
        problems.append(f"{where}: nombre de Job de {len(name)} caracteres (maximo {MAX_JOB_NAME})")

    folder = str(job.get("folderPath", "")).replace("\\", "/")
    parts = [part for part in folder.split("/") if part]
    if not parts or parts[0] != "Process":
        problems.append(f"{where}/{name}: la carpeta no cuelga de Process: {folder!r}")
    if any(part in {".", ".."} for part in parts):
        problems.append(f"{where}/{name}: carpeta con . o ..: {folder!r}")
    reserved = sorted({part for part in parts if part.lower() in RESERVED_FOLDERS})
    if reserved:
        problems.append(f"{where}/{name}: carpeta reservada con Git {reserved} en {folder!r}")
    if any(len(part) > 60 for part in parts):
        problems.append(f"{where}/{name}: un segmento de carpeta pasa de 60 caracteres: {folder!r}")
    if len("/".join(parts[1:])) > MAX_FOLDER_CHARS + 70:
        problems.append(f"{where}/{name}: carpeta demasiado larga para Windows ({len(folder)}): {folder!r}")

    components = job.get("components") or []
    if len(components) > component_limit:
        problems.append(f"{where}/{name}: {len(components)} componentes (limite {component_limit})")
    names = [component.get("uniqueName") for component in components]
    for repeated, count in Counter(names).items():
        if count > 1:
            problems.append(f"{where}/{name}: uniqueName repetido {repeated!r}")
    for component in components:
        unique = component.get("uniqueName", "")
        if not UNIQUE_NAME.match(unique):
            problems.append(f"{where}/{name}: uniqueName invalido {unique!r}")
        if not COMPONENT_NAME.match(component.get("componentName", "")):
            problems.append(f"{where}/{name}/{unique}: componentName invalido {component.get('componentName')!r}")
        if not isinstance(component.get("label"), str) or not component["label"].strip():
            problems.append(f"{where}/{name}/{unique}: sin etiqueta")
        for key, value in (component.get("parameters") or {}).items():
            if not isinstance(value, str):
                problems.append(f"{where}/{name}/{unique}: el parametro {key} no es texto ({type(value).__name__})")
        if component.get("draftOnly") and not component.get("draftReason"):
            problems.append(f"{where}/{name}/{unique}: borrador sin motivo")
        for table_name, table in (component.get("tables") or {}).items():
            rows = table.get("rows") if isinstance(table, dict) else None
            if not isinstance(rows, list):
                problems.append(f"{where}/{name}/{unique}: la tabla {table_name} no tiene filas en lista")

    known = set(names)
    seen_labels: Counter[str] = Counter()
    for edge in job.get("connections") or []:
        source, target = edge.get("source"), edge.get("target")
        if source not in known or target not in known:
            problems.append(f"{where}/{name}: conexion a un nodo inexistente {source}->{target}")
        if source == target:
            problems.append(f"{where}/{name}: conexion de {source} a si mismo")
        if edge.get("connectorName") not in CONNECTORS:
            problems.append(f"{where}/{name}: conector desconocido {edge.get('connectorName')!r}")
        seen_labels[str(edge.get("label"))] += 1
    problems += [
        f"{where}/{name}: nombre de conexion repetido {label!r}" for label, count in seen_labels.items() if count > 1
    ]

    contexts = [context.get("name") for context in job.get("contexts") or []]
    problems += [f"{where}/{name}: variable de contexto repetida {c!r}" for c, n in Counter(contexts).items() if n > 1]
    problems += [
        f"{where}/{name}: variable de contexto invalida {c!r}" for c in contexts if not CONTEXT_NAME.match(str(c))
    ]

    for step in (job.get("instructions") or {}).get("steps") or []:
        unique = step.get("talendUniqueName")
        if unique is not None and unique not in known:
            problems.append(f"{where}/{name}: el paso {step.get('id')} apunta a un componente inexistente {unique!r}")

    own = {key: value for key, value in job.items() if key != "childJobs"}
    if any(CONTROL.search(text) for text in _texts(own)):
        problems.append(f"{where}/{name}: caracter de control en un texto")
    problems += [
        f"{where}/{name}: {finding.rule} {finding.message}"
        for finding in check_job_arguments(job)
        if finding.severity == "error"
    ]
    return problems


def tree_problems(where: str, arguments: dict[str, Any], *, component_limit: int) -> list[str]:
    problems: list[str] = []
    for job in walk(arguments):
        problems += job_problems(where, job, component_limit=component_limit)
    return problems


def project_problems(trees: dict[str, dict[str, Any]], *, component_limit: int) -> list[str]:
    """Problemas de cada Job y de la coherencia entre los Jobs de un mismo proyecto.

    Un Job hijo aparece en el arbol de su padre y tambien como programa propio, asi que lo que no puede pasar es que
    un mismo nombre vaya a dos carpetas, o que dos programas distintos den el mismo nombre de Job.
    """
    problems: list[str] = []
    folders: dict[str, set[str]] = {}
    top_level: Counter[str] = Counter()
    for where, arguments in trees.items():
        problems += tree_problems(where, arguments, component_limit=component_limit)
        top_level[str(arguments.get("jobName"))] += 1
        for job in walk(arguments):
            folders.setdefault(str(job.get("jobName")), set()).add(str(job.get("folderPath")))
    problems += [f"proyecto: dos programas dan el mismo Job {name!r}" for name, count in top_level.items() if count > 1]
    problems += [
        f"proyecto: el Job {name!r} va a {len(places)} carpetas distintas: {sorted(places)}"
        for name, places in folders.items()
        if len(places) > 1
    ]
    return problems
