"""Cliente del MCP de Talend con allowlist de lectura y creación confirmada.

Toda llamada pasa por `policy.assert_allowed`. La escritura usa la tool tipada
`talend_job_apply_custom_spec`; `inspect_*` reciben `jobPath` (ruta al .item).
"""

import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, Protocol

from pydantic import BaseModel

from sas_grid_migrator.talend_adapter.contract import load_contract
from sas_grid_migrator.talend_adapter.eligibility import offline_tree_blockers
from sas_grid_migrator.talend_adapter.offline_payload import to_batch_arguments
from sas_grid_migrator.talend_adapter.policy import assert_allowed


class TalendError(RuntimeError):
    pass


class _OfflinePreflightError(TalendError):
    """El dryRun falló antes de que el lote pudiera escribir artefactos."""


class McpClientUnavailable(TalendError):
    """El paquete `mcp` instalado no trae el cliente 2.x que usa este adaptador."""


CLIENT_HINT = "Falta el cliente MCP 2.x: ejecuta «uv sync» (mcp>=2.3)"

#: Qué hacer con cada diagnóstico. `ok` no lleva pista.
FIX_HINTS: dict[str, str | None] = {
    "ok": None,
    "mcp_down": "Arranca talend-mcp con «bun run start:server» en mcp/talend-mcp y vuelve a comprobar la conexión.",
    "client_incompatible": CLIENT_HINT,
    "tools_missing": (
        "Arranca el MCP con TALEND_MCP_FILTER=portal y vuelve a comprobar; si sigue faltando, "
        "actualiza el preset del servidor."
    ),
    "contract_incomplete": (
        "Actualiza mcp/talend-mcp: el contrato de talend_job_apply_custom_spec no trae los campos "
        "que el portal necesita."
    ),
    "bridge_down": (
        "Abre Talend Studio con el proyecto y el plugin del bridge instalado; luego vuelve a comprobar."
    ),
    "studio_blocked": (
        "Talend Studio tiene un diálogo modal abierto que bloquea el IDE. Ciérralo en Studio y "
        "vuelve a comprobar."
    ),
}


def _spec_status(
    diagnosis: str,
    error: str | None,
    *,
    tools: int | None,
    write_tool: bool | None,
    missing: tuple[str, ...] | list[str] = (),
) -> dict[str, Any]:
    """Estado del contrato con el diagnóstico y la pista de arreglo."""
    return {
        "spec_supported": diagnosis == "ok",
        "spec_error": error,
        "tools": tools,
        "write_tool": write_tool,
        "missing_tools": sorted(missing),
        "diagnosis": diagnosis,
        "fix_hint": FIX_HINTS[diagnosis],
    }


def _import_client() -> Any:
    """`from mcp import Client`, pero con un mensaje accionable si la versión es 1.x."""
    try:
        from mcp import Client
    except (ImportError, AttributeError) as e:
        raise McpClientUnavailable(CLIENT_HINT) from e
    return Client


#: El cliente MCP corta las lecturas HTTP a los 300 s aunque la llamada admita más; una operación
#: larga (montar un Job de cientos de componentes en Studio) necesita ampliar ese límite.
DEFAULT_HTTP_READ_SECONDS = 300.0


class Caller(Protocol):
    async def call(self, tool: str, args: dict[str, Any]) -> dict[str, Any]: ...


class CallerWithTools(Protocol):
    """Caller capaz de listar las tools publicadas (para comprobar contratos)."""

    async def list_tools(self) -> list[dict[str, Any]]: ...
    async def describe_tool(self, tool: str) -> dict[str, Any] | None: ...


#: Tool de escritura que el portal invoca para crear un Job.
SPEC_TOOL = "talend_job_apply_custom_spec"

#: Tool de escritura offline (sin Studio); el nombre sale del manifiesto del contrato.
OFFLINE_TOOL = load_contract().offline_write_tool or ""

#: Tool que reinicia Studio; el nombre sale del manifiesto del contrato.
RESTART_TOOL = load_contract().restart_tool or ""

#: Heap de Studio (%) a partir del cual se recomienda reiniciarlo: tras muchos Jobs la interfaz deja de responder.
RESTART_RECOMMENDED_PERCENT = 75

#: Cerrar Studio (hasta 2 min, y forzarlo si no sale), arrancarlo y esperar al bridge puede tardar varios minutos.
RESTART_TIMEOUT_SECONDS = 600.0


def _offline_job_result(
    spec: dict[str, Any],
    written: dict[str, Any],
    omitted: list[dict[str, Any]],
    children: list[dict[str, Any]],
    notices: list[str] | None = None,
) -> dict[str, Any]:
    """Resultado de un Job escrito offline, con las mismas claves que devuelve Studio en vivo."""
    skipped = {item.get("uniqueName") for item in omitted}
    components = [item for item in spec.get("components") or [] if item.get("uniqueName") not in skipped]
    connections = [
        edge
        for edge in spec.get("connections") or []
        if edge.get("source") not in skipped and edge.get("target") not in skipped
    ]
    contexts = spec.get("contexts") or []
    item_path = str(written.get("itemPath") or "")
    return {
        "jobName": spec["jobName"],
        "folderPath": spec.get("folderPath"),
        "itemPath": item_path,
        "propertiesPath": item_path.removesuffix(".item") + ".properties" if item_path else "",
        "generatedComponents": len(components),
        "reusedComponents": 0,
        "totalComponents": len(components),
        "generatedConnections": len(connections),
        "reusedConnections": 0,
        "connections": len(connections),
        "generatedContexts": len(contexts),
        "updatedContexts": 0,
        "reusedContexts": 0,
        "removedContexts": 0,
        "reusedExisting": bool(written.get("reusedExisting")),
        "componentAliases": {item["uniqueName"]: item["uniqueName"] for item in components},
        "warnings": [f"{item.get('uniqueName')}: {item.get('motivo')}" for item in omitted] + list(notices or []),
        "childJobs": children,
        "mode": "offline",
    }


#: Segundos fijos y segundos por componente que se esperan a Studio al aplicar un Job (con sus hijos).
APPLY_BASE_SECONDS = 30.0
APPLY_SECONDS_PER_COMPONENT = 1.5


def count_components(arguments: dict[str, Any]) -> int:
    """Componentes de un Job y de todos sus Jobs hijo."""
    total = len(arguments.get("components") or [])
    for child in arguments.get("childJobs") or []:
        if isinstance(child, dict):
            total += count_components(child)
    return total


def apply_timeout(arguments: dict[str, Any]) -> float:
    """Tiempo que se espera a Studio: crecer con el tamaño evita cortar un montaje que sí avanza."""
    return APPLY_BASE_SECONDS + APPLY_SECONDS_PER_COMPONENT * count_components(arguments)


class McpCaller:
    """Llama a talend-mcp por HTTP (`http://127.0.0.1:3927/mcp`). Una sesión por llamada."""

    def __init__(self, url: str, timeout: float = 30.0):
        self.url, self.timeout = url, timeout

    def with_timeout(self, timeout: float) -> "McpCaller":
        """Copia con otro tiempo límite (nunca menor que el actual) para una operación larga."""
        return McpCaller(self.url, max(self.timeout, timeout))

    async def describe_tool(self, tool: str) -> dict[str, Any] | None:
        assert_allowed(tool)
        Client = _import_client()

        try:
            async with Client(self.url, read_timeout_seconds=self.timeout) as client:
                result = await client.list_tools()
                found = next((item for item in result.tools if item.name == tool), None)
                return found.input_schema if found else None
        except Exception as e:
            raise TalendError(f"No se pudo comprobar el contrato MCP: {type(e).__name__}") from e

    @asynccontextmanager
    async def _session(self, Client: Any) -> AsyncIterator[Any]:
        """Cliente MCP; con tiempos largos, con la lectura HTTP ampliada hasta `self.timeout`."""
        if self.timeout <= DEFAULT_HTTP_READ_SECONDS:
            async with Client(self.url) as client:
                yield client
            return
        import httpx2
        from mcp.client.streamable_http import streamable_http_client
        from mcp.shared._httpx_utils import MCP_DEFAULT_TIMEOUT, create_mcp_http_client

        http = create_mcp_http_client(timeout=httpx2.Timeout(MCP_DEFAULT_TIMEOUT, read=self.timeout))
        try:
            async with Client(streamable_http_client(self.url, http_client=http)) as client:
                yield client
        finally:
            await http.aclose()

    async def call(self, tool: str, args: dict[str, Any]) -> dict[str, Any]:
        assert_allowed(tool)
        Client = _import_client()

        try:
            async with self._session(Client) as client:
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
        Client = _import_client()

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
    def __init__(self, caller: Caller, *, write_enabled: bool = True, offline: bool = False):
        self.caller = caller
        self.write_enabled = write_enabled
        #: Escribir los Jobs offline cuando se pueda (Studio en vivo para lo que lo necesite o si falla).
        self.offline = offline

    @classmethod
    def from_env(cls, *, write_enabled: bool = True) -> "TalendAdapter":
        url = os.environ.get("TALEND_MCP_URL", "http://127.0.0.1:3927/mcp")
        timeout = float(os.environ.get("TALEND_MCP_TIMEOUT_SECONDS", "60"))
        # TALEND_APPLY_MODE: `auto` (por defecto) escribe offline lo que pueda y el resto en vivo; `live` todo en vivo.
        offline = os.environ.get("TALEND_APPLY_MODE", "auto").strip().lower() != "live"
        return cls(McpCaller(url, timeout=timeout), write_enabled=write_enabled, offline=offline)

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
        except McpClientUnavailable as e:
            return {
                "available": False,
                "mcp_available": False,
                "error": str(e),
                **_spec_status("client_incompatible", str(e), tools=None, write_tool=None),
                **config,
            }
        except TalendError as e:
            return {
                "available": False,
                "mcp_available": False,
                "error": str(e),
                **_spec_status("mcp_down", str(e), tools=None, write_tool=None),
                **config,
            }
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
                "diagnosis": "bridge_down",
                "fix_hint": FIX_HINTS["bridge_down"],
                "missing_tools": [],
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
                "diagnosis": "bridge_down",
                "fix_hint": FIX_HINTS["bridge_down"],
                "missing_tools": [],
                **config,
            }
        status = await self.custom_spec_status()
        dialogs = await self._studio_dialogs()
        memory = await self.studio_memory()
        if dialogs["blocked"] and status["diagnosis"] == "ok":
            titles = ", ".join(f"«{item['title']}»" for item in dialogs["blocking"])
            status = {
                **status,
                "diagnosis": "studio_blocked",
                "fix_hint": (
                    f"Talend Studio tiene abierto un diálogo modal que bloquea el IDE: {titles}. "
                    "Ciérralo en Studio y vuelve a comprobar."
                ),
            }
        return {
            "available": True,
            "mcp_available": True,
            "bridge_available": True,
            "bridge_mode": bridge.get("mode"),
            "unsafe_actions": bridge.get("unsafeActions", False),
            "jobs": job_count,
            "studio_dialogs": dialogs,
            "studio_memory": memory,
            **status,
            **config,
        }

    async def _studio_dialogs(self) -> dict[str, Any]:
        """Diálogos abiertos en Studio; un modal detiene el hilo de la interfaz.

        Solo informa: un diálogo bloqueante no impide crear ni leer Jobs, que no pasan por la UI.
        Si la comprobación falla, se devuelve `checked: false` y no cambia el diagnóstico.
        """
        try:
            data = await self._data("talend_studio_ui_dialogs")
        except TalendError as e:
            return {"checked": False, "blocked": False, "blocking": [], "error": str(e)}
        raw = data.get("blocking")
        blocking = [
            {"title": str(item.get("title") or "sin título"), "hint": str(item.get("hint") or "")}
            for item in (raw if isinstance(raw, list) else [])
            if isinstance(item, dict)
        ]
        return {
            "checked": True,
            "blocked": bool(data.get("blocked")) or bool(blocking),
            "blocking": blocking,
        }

    async def studio_memory(self) -> dict[str, Any]:
        """Heap que lleva usado Studio. Si la comprobación falla, `checked: false` y no cambia el diagnóstico."""
        try:
            data = await self._data("talend_studio_memory")
        except TalendError as e:
            return {"checked": False, "error": str(e)}
        percent = data.get("usedPercent")
        if not isinstance(percent, int | float):
            return {"checked": False, "error": "Studio no informó de su memoria"}
        return {
            "checked": True,
            "used_percent": int(percent),
            "used_mb": data.get("usedMb"),
            "max_mb": data.get("maxMb"),
            "restart_recommended": percent >= RESTART_RECOMMENDED_PERCENT,
        }

    async def restart_studio(self, *, only_if_memory_above: int | None = None, force: bool = True) -> dict[str, Any]:
        """Reinicia Studio: cierra sus diálogos, la ventana principal y, si no sale, el proceso.

        Libera la memoria que Studio retiene tras crear muchos Jobs. Cierra el IDE del usuario (los editores sin
        guardar se pierden y Talend Cloud puede pedir volver a iniciar sesión), por eso exige el permiso de escritura.
        """
        if not self.write_enabled:
            raise TalendError(
                "El portal está en modo solo lectura. Habilita la escritura desde Configuración para reiniciar Studio."
            )
        args: dict[str, Any] = {"force": force}
        if only_if_memory_above is not None:
            args["onlyIfMemoryAbove"] = only_if_memory_above
        return await self._studio_write(RESTART_TOOL, args, timeout=RESTART_TIMEOUT_SECONDS)

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
        except McpClientUnavailable as e:
            return _spec_status("client_incompatible", str(e), tools=None, write_tool=None)
        except TalendError as e:
            return _spec_status("mcp_down", str(e), tools=None, write_tool=None)

        contract = load_contract()
        if tools is not None:
            published = {item.get("name") for item in tools}
            missing = sorted((contract.read_tools | {contract.write_tool}) - published)
            write_tool = contract.write_tool in published
            if missing:
                return _spec_status(
                    "tools_missing",
                    "MCP incompatible con la migración: no publica "
                    f"{', '.join(missing)}. Arranca el MCP con TALEND_MCP_FILTER=portal.",
                    tools=len(tools),
                    write_tool=write_tool,
                    missing=missing,
                )
            tool = next(item for item in tools if item.get("name") == SPEC_TOOL)
            schema = tool.get("inputSchema") or tool.get("input_schema") or {}
        else:
            write_tool = None
            try:
                schema = await self.caller.describe_tool(SPEC_TOOL) or {}
            except McpClientUnavailable as e:
                return _spec_status("client_incompatible", str(e), tools=None, write_tool=None)
            except TalendError as e:
                return _spec_status("mcp_down", str(e), tools=None, write_tool=None)

        properties = schema.get("properties", {})
        component = properties.get("components", {}).get("items", {}).get("properties", {})
        missing_fields = sorted(contract.required_top_fields - properties.keys())
        missing_fields += sorted(contract.required_component_fields - component.keys())
        if missing_fields:
            return _spec_status(
                "contract_incomplete",
                f"MCP incompatible con la migración: faltan {', '.join(missing_fields)}. "
                "Actualiza el MCP antes de crear Jobs.",
                tools=len(tools) if tools is not None else None,
                write_tool=write_tool,
            )
        return _spec_status(
            "ok", None, tools=len(tools) if tools is not None else None, write_tool=write_tool
        )

    async def read_contexts(self, job_name: str) -> list[dict[str, Any]]:
        return (await self._data("talend_read_contexts", {"jobName": job_name})).get("contexts", [])

    async def component_icon(self, name: str) -> str | None:
        data = await self._data("talend_component_icon", {"name": name})
        svg = data.get("svg")
        return svg if data.get("available") and isinstance(svg, str) else None

    async def installed_component_names(self) -> list[str]:
        data = await self._data(
            "talend_studio_list_components", {"limit": 100000, "paletteType": "*"}
        )
        result = data.get("result")
        names = result.get("components") if isinstance(result, dict) else None
        if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
            raise TalendError("talend_studio_list_components devolvió un inventario incompleto")
        if result.get("count") != len(names):
            raise TalendError("talend_studio_list_components devolvió un inventario truncado")
        return sorted(set(names), key=str.casefold)

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
        result = data.get("result")
        if isinstance(result, dict):
            data = result
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
        fallback_note: str | None = None
        if self.offline and not offline_tree_blockers(arguments):
            try:
                return await self._apply_offline(arguments)
            except _OfflinePreflightError as error:
                fallback_note = f"El modo offline no pudo aplicar el Job ({error}); se usó Studio en vivo."
        compatibility = await self.custom_spec_status()
        if not compatibility["spec_supported"]:
            raise TalendError(compatibility["spec_error"])
        result = await self._studio_write(SPEC_TOOL, arguments, timeout=apply_timeout(arguments))
        if fallback_note:
            result.setdefault("warnings", []).append(fallback_note)
        return result

    async def _apply_offline(self, arguments: dict[str, Any]) -> dict[str, Any]:
        """Escribe el Job y sus hijos sin Studio, con la forma del resultado en vivo.

        Primero se valida todo el árbol con `dryRun`: si algo falla no se escribe nada, y el Job puede
        pasar a Studio en vivo sin encontrarse a medias los hijos ya escritos.
        """
        try:
            await self._write_offline(arguments, dry_run=True)
        except TalendError as error:
            raise _OfflinePreflightError(str(error)) from error
        return await self._write_offline(arguments, dry_run=False)

    async def _write_offline(self, spec: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
        children = [await self._write_offline(child, dry_run=dry_run) for child in spec.get("childJobs") or []]
        payload = to_batch_arguments({**spec, "childJobs": []})
        payload["dryRun"] = dry_run
        data = await self._offline_call(payload)
        name = spec["jobName"]
        written = next((item for item in data.get("jobs") or [] if item.get("job") == name), None)
        if written is None or not written.get("ok", False):
            raise TalendError(f"{OFFLINE_TOOL}: {name}: sin confirmación de escritura")
        return _offline_job_result(spec, written, data.get("omitidos") or [], children, data.get("avisos") or [])

    async def _offline_call(self, payload: dict[str, Any]) -> dict[str, Any]:
        assert_allowed(OFFLINE_TOOL)
        env = await self.caller.call(OFFLINE_TOOL, payload)
        if not isinstance(env, dict) or env.get("ok") is not True:
            error = env.get("error") if isinstance(env, dict) else None
            message = f"{error.get('code', 'ERROR')} {error.get('message', '')}".strip() if isinstance(error, dict) else "respuesta sin confirmación"
            raise TalendError(f"{OFFLINE_TOOL}: {message}")
        data = env.get("data")
        if not isinstance(data, dict):
            raise TalendError(f"{OFFLINE_TOOL}: respuesta sin datos")
        failures = data.get("fallos") or []
        if failures:
            first = failures[0]
            raise TalendError(f"{first.get('job', '?')}: {first.get('error', 'error desconocido')}")
        return data

    async def _studio_write(
        self, tool: str, args: dict[str, Any], *, timeout: float | None = None
    ) -> dict[str, Any]:
        assert_allowed(tool)
        caller = self.caller
        if timeout is not None and hasattr(caller, "with_timeout"):
            caller = caller.with_timeout(timeout)
        env = await caller.call(tool, args)
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
