"""Contrato portal↔MCP contra el servidor real.

Arranca `talend-mcp` con el preset `portal`, lee `tools/list` y compara con
`contract/portal-tools.json`. Si Bun no está instalado, se salta con motivo.
"""

import json
import os
import shutil
import socket
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

import pytest

from sas_grid_migrator.talend_adapter.adapter import McpCaller
from sas_grid_migrator.talend_adapter.contract import load_contract

ROOT = Path(__file__).resolve().parents[2]
MCP_DIR = ROOT / "mcp" / "talend-mcp"
BUN = shutil.which("bun")


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _wait_for_health(url: str, proc: subprocess.Popen, timeout: float = 30.0) -> None:
    deadline = time.monotonic() + timeout
    last: str = "sin respuesta"
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(f"el MCP terminó durante el arranque (código {proc.returncode})")
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                if response.status == 200:
                    return
                last = f"HTTP {response.status}"
        except (urllib.error.URLError, OSError) as error:
            last = str(error)
        time.sleep(0.2)
    raise RuntimeError(f"el MCP no respondió en {timeout:.0f} s: {last}")


class _Server:
    def __init__(self, preset: str, project: Path):
        self.port = _free_port()
        self.url = f"http://127.0.0.1:{self.port}/mcp"
        env = {
            **os.environ,
            "TALEND_MCP_FILTER": preset,
            "TALEND_MCP_PORT": str(self.port),
            "TALEND_MCP_HOST": "127.0.0.1",
            "TALEND_MCP_LOG": "quiet",
            "TALEND_DISABLE_AUTODETECT": "1",
            "TALEND_PROJECT": str(project),
        }
        self.proc = subprocess.Popen(
            [BUN, "run", "index.ts"],
            cwd=MCP_DIR,
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        _wait_for_health(f"http://127.0.0.1:{self.port}/healthz", self.proc)

    def stop(self) -> None:
        self.proc.terminate()
        try:
            self.proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.proc.kill()


@pytest.fixture(scope="module")
def mcp_server(tmp_path_factory):
    if BUN is None:
        pytest.skip("bun no está instalado")
    project = tmp_path_factory.mktemp("talend-project")
    (project / "talend.project").write_text("", encoding="utf-8")
    server = _Server("portal", project)
    try:
        yield server
    finally:
        server.stop()


@pytest.fixture(scope="module")
def agent_server(tmp_path_factory):
    if BUN is None:
        pytest.skip("bun no está instalado")
    project = tmp_path_factory.mktemp("talend-project-agent")
    (project / "talend.project").write_text("", encoding="utf-8")
    server = _Server("agent", project)
    try:
        yield server
    finally:
        server.stop()


def _published(mcp_server) -> list[dict]:
    import asyncio

    return asyncio.run(McpCaller(mcp_server.url).list_tools())


def test_published_tools_cover_the_contract(mcp_server):
    contract = load_contract()
    names = {tool["name"] for tool in _published(mcp_server)}
    missing = sorted((contract.read_tools | {contract.write_tool}) - names)
    assert not missing, f"el preset portal no publica: {', '.join(missing)}"


def test_write_tool_schema_has_required_fields(mcp_server):
    contract = load_contract()
    tools = {tool["name"]: tool for tool in _published(mcp_server)}
    schema = tools[contract.write_tool]["inputSchema"]
    properties = schema.get("properties", {})
    component = properties.get("components", {}).get("items", {}).get("properties", {})

    assert contract.required_top_fields <= properties.keys()
    assert contract.required_component_fields <= component.keys()


@pytest.mark.xfail(reason="missing_tools llega en la Tarea 9", strict=False)
def test_agent_preset_alone_is_reported_incomplete(agent_server):
    import asyncio

    status = asyncio.run(McpCaller(agent_server.url).custom_spec_status())
    assert status["missing_tools"], json.dumps(status, ensure_ascii=False)
