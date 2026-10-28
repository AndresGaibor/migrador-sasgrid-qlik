"""Buenas prácticas de Talend comprobables sobre la especificación de un Job.

Son recomendaciones: no cambian el estado de la aplicación. Cada regla tiene un
identificador estable que documenta `docs/talend-best-practices.md`.
"""

import re
from typing import Any, Literal

from pydantic import BaseModel

MAX_COMPONENTS = 30

_ENVIRONMENT_PARAMETERS = ("FILENAME", "DIRECTORY", "HOST", "PORT", "DBNAME", "URL")
_PASSWORD_PARAMETERS = ("PASS", "PASSWORD", "PASSPHRASE")
_CONTEXT_REFERENCE = re.compile(r"\bcontext\.\w+")
_DATABASES = (
    "DB|Mysql|Oracle|Postgresql|Mssql|Teradata|Snowflake|Redshift|Vertica|Netezza|"
    "Db2|Informix|Sybase|MariaDB|SingleStore|Greenplum"
)
_DATABASE_ACCESS = re.compile(rf"^t(?:{_DATABASES})(?:Input|Output|Row|SP|BulkExec|OutputBulk|OutputBulkExec)$")
_DATABASE_CONNECTION = re.compile(rf"^t(?:{_DATABASES})Connection$")
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
