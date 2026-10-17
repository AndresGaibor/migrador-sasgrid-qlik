"""Cliente de solo lectura para talend-mcp. Opcional: el análisis SAS no depende de él.

Toda llamada pasa por `policy.assert_allowed`. Los esquemas de entrada/salida se tomaron del
código de talend-mcp (revisión 2026-10-17); `inspect_*` reciben `jobPath` (ruta al .item).
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
            raise TalendError(f"talend-mcp no disponible: {type(e).__name__}: {e}") from e
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
        return cls(McpCaller(os.environ.get("TALEND_MCP_URL", "http://127.0.0.1:3927/mcp")))

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
            data = await self._data("talend_list_jobs")
        except TalendError as e:
            return {"available": False, "error": str(e)}
        return {"available": True, "jobs": len(data.get("jobs", []))}

    async def list_jobs(self) -> list[dict[str, Any]]:
        return (await self._data("talend_list_jobs")).get("jobs", [])

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
