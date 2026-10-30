"""Buenas prácticas de Talend comprobables sobre la especificación de un Job.

Son recomendaciones: no cambian el estado de la aplicación. Cada regla tiene un
identificador estable que documenta `docs/talend-best-practices.md`.
"""

import re
from typing import Any, Literal

from pydantic import BaseModel

from sas_grid_migrator.migration_planner.limits import (
    DATABASE_ACCESS,
    DATABASE_CONNECTION,
    MAX_COMPONENTS_PER_JOB,
)

MAX_COMPONENTS = MAX_COMPONENTS_PER_JOB  # umbral único: migration_planner/limits.py
RESERVED_GIT_NAMES = frozenset({"tests", "target", "src"})
JOB_PREFIX = "job_"

_ENVIRONMENT_PARAMETERS = ("FILENAME", "DIRECTORY", "HOST", "PORT", "DBNAME", "URL")
_PASSWORD_PARAMETERS = ("PASS", "PASSWORD", "PASSPHRASE")
_CONTEXT_REFERENCE = re.compile(r"\bcontext\.\w+")
_DATABASE_ACCESS = DATABASE_ACCESS
_DATABASE_CONNECTION = DATABASE_CONNECTION
_ERROR_COMPONENTS = frozenset({"tDie", "tWarn", "tLogCatcher", "tStatCatcher", "tFlowMeterCatcher", "tAssertCatcher"})
_ERROR_CONNECTORS = frozenset({"SUBJOB_ERROR", "COMPONENT_ERROR", "REJECT"})


class PracticeFinding(BaseModel):
    rule: str
    severity: Literal["error", "warning", "info"]
    message: str
    component: str | None = None
    parameter: str | None = None


def _is_literal(value: Any) -> bool:
    text = str(value).strip() if value is not None else ""
    return bool(text) and not text.startswith("enc:") and not _CONTEXT_REFERENCE.search(text)


def check_job_arguments(arguments: dict[str, Any]) -> list[PracticeFinding]:
    """Revisa los argumentos de `talend_job_apply_custom_spec` de un Job (sin sus hijos)."""
    components = [item for item in arguments.get("components", []) if isinstance(item, dict)]
    connections = [item for item in arguments.get("connections", []) if isinstance(item, dict)]
    findings: list[PracticeFinding] = []

    job_name = str(arguments.get("jobName") or "")
    if job_name and not job_name.startswith(JOB_PREFIX):
        findings.append(PracticeFinding(
            rule="BP-NAME-01",
            severity="info",
            message=f"El Job '{job_name}' no empieza por '{JOB_PREFIX}'; la guía de Talend propone ese prefijo para distinguir Jobs de rutas, servicios y tareas.",
        ))
    folders = [part for part in str(arguments.get("folderPath") or "").replace("\\", "/").split("/") if part]
    reserved = [name for name in [job_name, *folders] if name.lower() in RESERVED_GIT_NAMES]
    if reserved:
        findings.append(PracticeFinding(
            rule="BP-NAME-02",
            severity="warning",
            message=f"El nombre '{reserved[0]}' está reservado con Git (tests, target, src): los cambios del Job no se suben al repositorio; renómbralo.",
        ))

    for component in components:
        unique_name = component.get("uniqueName")
        parameters = component.get("parameters") or {}
        for name in _ENVIRONMENT_PARAMETERS:
            if _is_literal(parameters.get(name)):
                findings.append(PracticeFinding(
                    rule="BP-CTX-01",
                    severity="warning",
                    component=unique_name,
                    parameter=name,
                    message=f"{unique_name}: {name} tiene un valor fijo; usa una variable de contexto para cambiar de entorno sin editar el Job.",
                ))
        for name in _PASSWORD_PARAMETERS:
            if _is_literal(parameters.get(name)):
                findings.append(PracticeFinding(
                    rule="BP-SEC-01",
                    severity="error",
                    component=unique_name,
                    parameter=name,
                    message=f"{unique_name}: {name} contiene una contraseña en claro; guárdala en una variable de contexto de tipo contraseña.",
                ))

    names = [str(item.get("componentName", "")) for item in components]
    has_connection = any(_DATABASE_CONNECTION.match(name) for name in names)
    database_access = [name for name in names if _DATABASE_ACCESS.match(name)]
    if len(database_access) >= 2 and not has_connection:
        findings.append(PracticeFinding(
            rule="BP-DB-01",
            severity="warning",
            message=f"El Job abre {len(database_access)} accesos a base de datos sin una conexión compartida; usa un componente de conexión con commit y cierre.",
        ))

    handles_errors = any(name in _ERROR_COMPONENTS for name in names) or any(
        item.get("connectorName") in _ERROR_CONNECTORS for item in connections
    )
    if len(components) >= 2 and not handles_errors:
        findings.append(PracticeFinding(
            rule="BP-ERR-01",
            severity="info",
            message="El Job no tiene manejo de errores (tDie, tWarn, tLogCatcher o una conexión de error); un fallo pasaría sin registro.",
        ))

    if len(components) > MAX_COMPONENTS:
        findings.append(PracticeFinding(
            rule="BP-SIZE-01",
            severity="warning",
            message=f"El Job tiene {len(components)} componentes (máximo recomendado {MAX_COMPONENTS}); divídelo en Jobs hijo con tRunJob.",
        ))
    return findings


class PlanPracticeFinding(BaseModel):
    """Hallazgo de buenas prácticas sobre un `JobPlan`. `id` es estable; `step_ids` son los pasos afectados."""

    id: str
    severity: Literal["error", "warning", "info"]
    message: str
    job: str | None = None
    step_ids: list[str] = []


_PLAN_ENV_PARAMETERS = frozenset({"FILENAME", "DIRECTORY", "HOST", "PORT", "DBNAME", "URL", "PATH"})
_PLAN_PASSWORD_PARAMETERS = frozenset({"PASS", "PASSWORD", "PWD", "PASSPHRASE"})
_JAVA_COMPONENTS = frozenset({"tJava", "tJavaRow"})
_JAVA_LINES_LIMIT = 40
_JAVA_EXPRESSIONS_LIMIT = 15
_ERROR_STEP_COMPONENTS = frozenset({"tDie", "tWarn", "tLogCatcher"})


def _literal_value(value: Any) -> bool:
    return _is_literal(value) and not re.search(r"\$\w+|&\w+", str(value))


def evaluate_job_practices(plan: Any) -> list[PlanPracticeFinding]:
    """Reglas de buenas prácticas sobre un plan (`JobPlan`), agrupadas por Job.

    Cada hallazgo indica los pasos afectados. Son recomendaciones: no bloquean la aplicación.
    """
    findings: list[PlanPracticeFinding] = []
    # Un Job = pasos de una misma lista (principal o hijo) agrupados por parte: dos macros con el
    # mismo nombre (bloques repetidos) no se suman en un único Job.
    units: list[tuple[str, list[Any]]] = []
    for container, default in [(plan.steps, plan.job_name), *((c.steps, c.name) for c in plan.children)]:
        grouped: dict[str, list[Any]] = {}
        for step in container:
            grouped.setdefault(step.job_part or default, []).append(step)
        units.extend(grouped.items())

    for job, steps in units:
        ids = [step.id for step in steps]
        real = [step for step in steps if not step.recommended]

        if len(steps) > MAX_COMPONENTS:
            findings.append(PlanPracticeFinding(
                id="PLAN-SIZE-01", severity="warning", job=job, step_ids=ids,
                message=f"El Job {job} tiene {len(steps)} componentes (máximo {MAX_COMPONENTS}); "
                "divídelo en Jobs hijo con tRunJob.",
            ))

        database = [s for s in steps if _DATABASE_ACCESS.match(s.component_candidate)]
        names = {s.component_candidate for s in steps}
        has_connection = any(_DATABASE_CONNECTION.match(name) for name in names)
        if len(database) >= 2 and not has_connection:
            findings.append(PlanPracticeFinding(
                id="PLAN-DB-01", severity="warning", job=job,
                step_ids=[s.id for s in database],
                message=f"El Job {job} abre {len(database)} accesos a base de datos sin una conexión "
                "compartida; usa una conexión única con cierre al final.",
            ))

        if len(real) >= 2 and not (names & _ERROR_STEP_COMPONENTS) and not any(
            connection.type == "OnComponentError" for s in steps for connection in s.connections
        ):
            findings.append(PlanPracticeFinding(
                id="PLAN-ERR-01", severity="info", job=job, step_ids=ids,
                message=f"El Job {job} no maneja errores (tDie, tWarn, tLogCatcher u OnComponentError).",
            ))

        by_library: dict[str, list[Any]] = {}
        for step in database:
            if step.library:
                by_library.setdefault(step.library, []).append(step)
        for library, library_steps in by_library.items():
            if len(library_steps) >= 2:
                findings.append(PlanPracticeFinding(
                    id="PLAN-BI-01", severity="info", job=job,
                    step_ids=[s.id for s in library_steps],
                    message=f"La biblioteca {library} se usa en {len(library_steps)} pasos del Job {job} "
                    "con esquema incrustado; crea una metadata de Repository y reutilízala.",
                ))

        for step in steps:
            if step.recommended:
                continue
            if step.component_candidate in _JAVA_COMPONENTS and (
                step.evidence.end_line - step.evidence.line > _JAVA_LINES_LIMIT
                or len(step.expressions) > _JAVA_EXPRESSIONS_LIMIT
            ):
                findings.append(PlanPracticeFinding(
                    id="PLAN-JAVA-01", severity="warning", job=job, step_ids=[step.id],
                    message=f"{step.component_candidate} extenso en {job} ({step.id}): mueve la lógica a "
                    "una rutina de Talend o a un componente de transformación.",
                ))
            for prop in step.properties:
                if prop.name.upper() in _PLAN_PASSWORD_PARAMETERS and _literal_value(prop.value):
                    findings.append(PlanPracticeFinding(
                        id="PLAN-SEC-01", severity="error", job=job, step_ids=[step.id],
                        message=f"{step.id}: {prop.name} contiene una contraseña en claro; guárdala en "
                        "una variable de contexto de tipo id_Password.",
                    ))
                elif prop.name.upper() in _PLAN_ENV_PARAMETERS and _literal_value(prop.value):
                    findings.append(PlanPracticeFinding(
                        id="PLAN-CTX-01", severity="warning", job=job, step_ids=[step.id],
                        message=f"{step.id}: {prop.name} tiene un valor fijo; usa una variable de contexto "
                        "para cambiar de entorno sin editar el Job.",
                    ))

    for warning in plan.unresolved:
        if warning.startswith("Credencial en claro"):
            findings.append(PlanPracticeFinding(
                id="PLAN-SEC-02", severity="error", job=plan.job_name,
                message=warning,
            ))
    return findings
