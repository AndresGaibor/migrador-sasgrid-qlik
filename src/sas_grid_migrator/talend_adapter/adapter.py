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


class McpCaller:
    """Llama a talend-mcp por HTTP (`http://127.0.0.1:3927/mcp`). Una sesión por llamada."""

    def __init__(self, url: str, timeout: float = 30.0):
        self.url, self.timeout = url, timeout

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


class ComponentRef(BaseModel):
    unique_name: str
    component: str
    label: str | None = None
    parameters: list[str] = []
    schema_columns: int = 0


class JobInspection(BaseModel):
    job_path: str
    components: list[ComponentRef]
    connections: int
    contexts: list[str]


class TalendAdapter:
    def __init__(self, caller: Caller):
        self.caller = caller

    @classmethod
    def from_env(cls) -> "TalendAdapter":
        url = os.environ.get("TALEND_MCP_URL", "http://127.0.0.1:3927/mcp")
        timeout = float(os.environ.get("TALEND_MCP_TIMEOUT_SECONDS", "60"))
        return cls(McpCaller(url, timeout=timeout))

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

    async def health_check(self) -> dict[str, Any]:
        try:
            jobs = await self.list_jobs()
        except TalendError as e:
            return {"available": False, "mcp_available": False, "error": str(e)}
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
            }
        if bridge.get("ok") is not True:
            return {
                "available": False,
                "mcp_available": True,
                "bridge_available": False,
                "jobs": job_count,
                "error": "Talend Studio Bridge no está disponible.",
            }
        return {
            "available": True,
            "mcp_available": True,
            "bridge_available": True,
            "bridge_mode": bridge.get("mode"),
            "unsafe_actions": bridge.get("unsafeActions", False),
            "jobs": job_count,
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

    async def read_contexts(self, job_name: str) -> list[dict[str, Any]]:
        return (await self._data("talend_read_contexts", {"jobName": job_name})).get("contexts", [])

    async def inspect_job(self, job_path: str) -> JobInspection:
        if not job_path.endswith(".item"):
            raise TalendError("job_path debe apuntar a un archivo .item")
        data = (await self._data("talend_inspect_job", {"jobPath": job_path})).get("inspection", {})
        job = data.get("job") or {}
        comps = [
            ComponentRef(
                unique_name=c.get("uniqueName", ""),
                component=c.get("componentName", ""),
                label=c.get("label"),
                parameters=sorted((c.get("parameters") or {}).keys()),
                schema_columns=sum(len(s.get("columns", [])) for s in c.get("schemas") or []),
            )
            for c in (job.get("components") or data.get("components") or [])
            if c.get("componentName")
        ]
        return JobInspection(
            job_path=job_path,
            components=comps,
            connections=len(data.get("connections") or job.get("connections") or []),
            contexts=[c.get("name", "") for c in data.get("contexts") or job.get("contexts") or []],
        )

    async def apply_custom_spec(self, arguments: dict[str, Any]) -> dict[str, Any]:
        """Envía al MCP la instrucción completa para que Studio aplique el Job."""
        write_enabled = os.environ.get("TALEND_MCP_READONLY", "false").strip().casefold() in {
            "false", "0", "no", "off"
        }
        if not write_enabled:
            raise TalendError(
                "talend-mcp está en modo solo lectura; configura TALEND_MCP_READONLY=false para habilitar creación explícita."
            )
        return await self._studio_write("talend_job_apply_custom_spec", arguments)

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
