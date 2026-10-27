"""Cliente del MCP de Talend con allowlist de lectura y creación confirmada.

Toda llamada pasa por `policy.assert_allowed`. La escritura usa la tool tipada
`talend_job_apply_custom_spec`; `inspect_*` reciben `jobPath` (ruta al .item).
"""

import os
from typing import Any, Protocol

from pydantic import BaseModel

from sas_grid_migrator.talend_adapter.policy import assert_allowed


class TalendError(RuntimeError):
    pass


class Caller(Protocol):
    async def call(self, tool: str, args: dict[str, Any]) -> dict[str, Any]: ...


class CallerWithTools(Protocol):
    """Caller capaz de listar las tools publicadas (para comprobar contratos)."""

    async def list_tools(self) -> list[dict[str, Any]]: ...
    async def describe_tool(self, tool: str) -> dict[str, Any] | None: ...


#: Tool de escritura que el portal invoca para crear un Job.
SPEC_TOOL = "talend_job_apply_custom_spec"


class McpCaller:
    """Llama a talend-mcp por HTTP (`http://127.0.0.1:3927/mcp`). Una sesión por llamada."""

    def __init__(self, url: str, timeout: float = 30.0):
        self.url, self.timeout = url, timeout

    async def describe_tool(self, tool: str) -> dict[str, Any] | None:
        assert_allowed(tool)
        from mcp import Client

        try:
            async with Client(self.url, read_timeout_seconds=self.timeout) as client:
                result = await client.list_tools()
                found = next((item for item in result.tools if item.name == tool), None)
                return found.input_schema if found else None
        except Exception as e:
            raise TalendError(f"No se pudo comprobar el contrato MCP: {type(e).__name__}") from e

    async def call(self, tool: str, args: dict[str, Any]) -> dict[str, Any]:
        assert_allowed(tool)
        from mcp import Client

        try:
            async with Client(self.url) as client:
                res = await client.call_tool(tool, args, read_timeout_seconds=self.timeout)
        except Exception as e:  # red, sesión o protocolo
            cause = e
            while isinstance(cause, BaseExceptionGroup) and cause.exceptions:
                cause = cause.exceptions[0]
            raise TalendError(f"talend-mcp no disponible: {type(cause).__name__}: {cause}") from e
        if getattr(res, "is_error", False):
            detail = next((c.text for c in res.content if getattr(c, "text", None)), "error MCP")
            raise TalendError(f"{tool}: {detail}")
        data = getattr(res, "structured_content", None)
        if data is None:
            import json

            text = next((c.text for c in res.content if getattr(c, "text", None)), "{}")
            try:
                data = json.loads(text)
            except ValueError as e:
                raise TalendError("respuesta de talend-mcp no es JSON") from e
        return data

    async def list_tools(self) -> list[dict[str, Any]]:
        """Tools publicadas por el servidor MCP (read-only)."""
        from mcp import Client

        try:
            async with Client(self.url, read_timeout_seconds=self.timeout) as client:
                result = await client.list_tools()
        except Exception as e:
            cause = e
            while isinstance(cause, BaseExceptionGroup) and cause.exceptions:
                cause = cause.exceptions[0]
            raise TalendError(f"talend-mcp no disponible: {type(cause).__name__}: {cause}") from e
        tools: list[dict[str, Any]] = []
        for tool in getattr(result, "tools", []) or []:
            dump = getattr(tool, "model_dump", None)
            if callable(dump):
                tools.append(dump(by_alias=True, exclude_none=True))
            elif isinstance(tool, dict):
                tools.append(tool)
        return tools


class ComponentRef(BaseModel):
    unique_name: str
    component: str
    label: str | None = None
    parameters: list[str] = []
    parameter_values: dict[str, Any] = {}
    schemas: list[dict[str, Any]] = []
    schema_columns: int = 0


class JobInspection(BaseModel):
    job_path: str
    components: list[ComponentRef]
    connections: int
    connection_details: list[dict[str, Any]] = []
    contexts: list[str]
    mapper_entries: list[dict[str, Any]] = []


class TalendAdapter:
    def __init__(self, caller: Caller, *, write_enabled: bool = True):
        self.caller = caller
        self.write_enabled = write_enabled

    @classmethod
    def from_env(cls, *, write_enabled: bool = True) -> "TalendAdapter":
        url = os.environ.get("TALEND_MCP_URL", "http://127.0.0.1:3927/mcp")
        timeout = float(os.environ.get("TALEND_MCP_TIMEOUT_SECONDS", "60"))
        return cls(McpCaller(url, timeout=timeout), write_enabled=write_enabled)

    async def _data(self, tool: str, args: dict[str, Any] | None = None) -> dict[str, Any]:
        assert_allowed(tool)
        env = await self.caller.call(tool, args or {})
        if not env.get("ok", True):
            err = env.get("error") or {}
            raise TalendError(
                f"{tool}: {err.get('code', 'ERROR')} {err.get('message', '')}".strip()
            )
        data = env.get("data")
        return data if isinstance(data, dict) else {"value": data}

    def _connection_config(self) -> dict[str, Any]:
        """Configuración activa del cliente, para mostrar en diagnóstico."""
        config: dict[str, Any] = {}
        url = getattr(self.caller, "url", None)
        timeout = getattr(self.caller, "timeout", None)
        if url:
            config["mcp_url"] = url
        if timeout is not None:
            config["timeout_seconds"] = timeout
        return config

    async def health_check(self) -> dict[str, Any]:
        config = self._connection_config()
        try:
            jobs = await self.list_jobs()
        except TalendError as e:
            return {"available": False, "mcp_available": False, "error": str(e), **config}
        job_count = len(jobs)
        try:
            bridge = await self._data("talend_bridge_ping")
        except TalendError as e:
            return {
                "available": False,
                "mcp_available": True,
                "bridge_available": False,
                "jobs": job_count,
                "error": str(e),
                **config,
            }
        if bridge.get("ok") is not True:
            return {
                "available": False,
                "mcp_available": True,
                "bridge_available": False,
                "jobs": job_count,
                "error": "Talend Studio Bridge no está disponible. Instala el plugin en Studio "
                "(bun run scripts/start.ts --install-bridge) y abre un proyecto.",
                **config,
            }
        return {
            "available": True,
            "mcp_available": True,
            "bridge_available": True,
            "bridge_mode": bridge.get("mode"),
            "unsafe_actions": bridge.get("unsafeActions", False),
            "jobs": job_count,
            **(await self.custom_spec_status()),
            **config,
        }

    async def list_jobs(self) -> list[dict[str, Any]]:
        """Return the complete Job inventory, failing if MCP cannot page it fully."""
        page_size = 100
        jobs: list[dict[str, Any]] = []
        seen: set[tuple[str, str]] = set()
        expected_total: int | None = None
        offset = 0

        for _ in range(1000):
            data = await self._data(
                "talend_jobs_list", {"limit": page_size, "offset": offset}
            )
            page = data.get("jobs")
            if not isinstance(page, list) or len(page) > page_size:
                raise TalendError("talend_jobs_list devolvió una página inválida; preflight incompleto.")

            reported_total = data.get("total")
            if reported_total is not None:
                if not isinstance(reported_total, int) or reported_total < 0:
                    raise TalendError("talend_jobs_list devolvió un total inválido; preflight incompleto.")
                if expected_total is not None and reported_total != expected_total:
                    raise TalendError("talend_jobs_list cambió el total entre páginas; preflight incompleto.")
                expected_total = reported_total

            if not page:
                if expected_total is not None and len(jobs) < expected_total:
                    raise TalendError("talend_jobs_list devolvió un inventario incompleto.")
                return jobs

            for job in page:
                if (
                    not isinstance(job, dict)
                    or not isinstance(job.get("name"), str)
                    or not job["name"].strip()
                    or not isinstance(job.get("path"), str)
                    or not job["path"].strip()
                ):
                    raise TalendError("talend_jobs_list devolvió un Job sin nombre o ruta; preflight incompleto.")
                key = (job["name"].casefold(), job["path"].replace("\\", "/").casefold())
                if key in seen:
                    raise TalendError("talend_jobs_list repitió una página; preflight incompleto.")
                seen.add(key)
                jobs.append(job)

            offset += len(page)
            if expected_total is not None:
                if len(jobs) > expected_total:
                    raise TalendError("talend_jobs_list devolvió más Jobs que el total informado.")
                if len(jobs) == expected_total:
                    return jobs
            if len(page) < page_size:
                if expected_total is not None and len(jobs) < expected_total:
                    raise TalendError("talend_jobs_list devolvió un inventario incompleto.")
                return jobs

        raise TalendError("talend_jobs_list excedió el límite de páginas; preflight incompleto.")
    async def _published_tools(self) -> list[dict[str, Any]] | None:
        """Inventario de tools publicadas; `None` si el caller no sabe listarlas."""
        lister = getattr(self.caller, "list_tools", None)
        return await lister() if callable(lister) else None

    async def custom_spec_status(self) -> dict[str, Any]:
        """Contrato de la tool de escritura más el inventario publicado por el MCP.

        `tools` y `write_tool` son `None` cuando el caller no puede listar las tools.
        """
        try:
            tools = await self._published_tools()
        except TalendError as e:
            return {
                "spec_supported": False,
                "spec_error": str(e),
                "tools": None,
                "write_tool": None,
            }
        status: dict[str, Any] = {
            "spec_supported": False,
            "spec_error": None,
            "tools": len(tools) if tools is not None else None,
            "write_tool": None,
        }
        if tools is not None:
            tool = next((item for item in tools if item.get("name") == SPEC_TOOL), None)
            status["write_tool"] = tool is not None
            if tool is None:
                status["spec_error"] = (
                    f"MCP incompatible con la migración: no publica {SPEC_TOOL}. "
                    "Actualiza el MCP antes de crear Jobs."
                )
                return status
            schema = tool.get("inputSchema") or tool.get("input_schema") or {}
        else:
            try:
                schema = await self.caller.describe_tool(SPEC_TOOL) or {}
            except TalendError as e:
                status["spec_error"] = str(e)
                return status
        properties = schema.get("properties", {})
        component = properties.get("components", {}).get("items", {}).get("properties", {})
        missing = sorted({"childJobs", "instructions", "replaceManagedTodoContexts"} - properties.keys())
        missing += sorted({"draftOnly", "draftReason", "tables"} - component.keys())
        if missing:
            status["spec_error"] = (
                f"MCP incompatible con la migración: faltan {', '.join(missing)}. "
                "Actualiza el MCP antes de crear Jobs."
            )
            return status
        status["spec_supported"] = True
        return status

    async def read_contexts(self, job_name: str) -> list[dict[str, Any]]:
        return (await self._data("talend_read_contexts", {"jobName": job_name})).get("contexts", [])

    async def inspect_job(self, job_path: str) -> JobInspection:
        if not job_path.endswith(".item"):
            raise TalendError("job_path debe apuntar a un archivo .item")
        data = (await self._data("talend_inspect_job", {"jobPath": job_path})).get("inspection", {})
        job = data.get("job") or {}
        raw_connections = data.get("connections") or job.get("connections") or []
        mapper_entries = data.get("mapperEntries") or job.get("mapperEntries") or []
        comps = [
            ComponentRef(
                unique_name=c.get("uniqueName", ""),
                component=c.get("componentName", ""),
                label=c.get("label"),
                parameters=sorted((parameter_values := c.get("parameters") or {}).keys()),
                parameter_values=parameter_values,
                schemas=list(c.get("schemas") or []),
                schema_columns=sum(len(schema.get("columns", [])) for schema in c.get("schemas") or []),
            )
            for c in (job.get("components") or data.get("components") or [])
            if c.get("componentName")
        ]
        return JobInspection(
            job_path=job_path,
            components=comps,
            connections=len(raw_connections),
            connection_details=list(raw_connections),
            contexts=[c.get("name", "") for c in data.get("contexts") or job.get("contexts") or []],
            mapper_entries=list(mapper_entries),
        )

    async def job_problems(self, job_name: str) -> dict[str, Any]:
        """Avisos de diseño del Job en la vista Problemas de Studio (requiere Bridge)."""
        data = await self._data("talend_job_problems", {"job": job_name})
        problems = data.get("problems")
        return {
            "clean": bool(data.get("clean", False)),
            "problems": [item for item in problems if isinstance(item, dict)]
            if isinstance(problems, list)
            else [],
        }

    async def apply_custom_spec(self, arguments: dict[str, Any]) -> dict[str, Any]:
        """Envía al MCP la instrucción completa para que Studio aplique el Job."""
        if not self.write_enabled:
            raise TalendError(
                "El portal está en modo solo lectura. Habilita la escritura desde Configuración para crear Jobs."
            )
        compatibility = await self.custom_spec_status()
        if not compatibility["spec_supported"]:
            raise TalendError(compatibility["spec_error"])
        return await self._studio_write(SPEC_TOOL, arguments)

    async def _studio_write(self, tool: str, args: dict[str, Any]) -> dict[str, Any]:
        assert_allowed(tool)
        env = await self.caller.call(tool, args)
        if not isinstance(env, dict) or env.get("ok") is not True:
            error = env.get("error") if isinstance(env, dict) else None
            if isinstance(error, dict):
                message = f"{error.get('code', 'ERROR')} {error.get('message', '')}".strip()
            else:
                message = "respuesta sin confirmación explícita de éxito"
            raise TalendError(f"{tool}: {message}")
        data = env.get("data")
        if not isinstance(data, dict):
            raise TalendError(f"{tool}: respuesta de éxito sin datos de resultado")
        if data.get("ok") is False:
            error = data.get("error")
            if isinstance(error, dict):
                message = f"{error.get('code', 'ERROR')} {error.get('message', '')}".strip()
            elif isinstance(error, str):
                message = error
            else:
                message = str(data.get("message") or "Talend Studio rechazó la operación")
            raise TalendError(f"{tool}: {message}")
        result = data.get("result")
        return result if isinstance(result, dict) else data
