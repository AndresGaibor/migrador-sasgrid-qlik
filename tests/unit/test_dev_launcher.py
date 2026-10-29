import socket
import subprocess
from types import SimpleNamespace

from sas_grid_migrator.cli import dev as dev_module
from sas_grid_migrator.cli.dev import mcp_launch, port_in_use


def test_mcp_launch_uses_portal_preset_without_touching_studio(tmp_path):
    mcp = tmp_path / "mcp" / "talend-mcp"
    mcp.mkdir(parents=True)
    (mcp / "package.json").write_text("{}", encoding="utf-8")

    command, cwd, env = mcp_launch(tmp_path, "bun", {"PATH": "x"})

    assert command == ["bun", "run", "start:server"]
    assert cwd == mcp
    assert env["TALEND_MCP_FILTER"] == "portal"
    assert env["PATH"] == "x"


def test_mcp_launch_is_none_when_subtree_is_missing(tmp_path):
    assert mcp_launch(tmp_path, "bun", {}) is None


def test_port_in_use_detects_a_listening_socket():
    with socket.socket() as server:
        server.bind(("127.0.0.1", 0))
        server.listen()
        port = server.getsockname()[1]
        assert port_in_use("127.0.0.1", port)
    assert not port_in_use("127.0.0.1", port)


def test_windows_reload_process_has_no_console_to_interrupt_the_supervisor(monkeypatch, tmp_path):
    monkeypatch.setattr(dev_module, "IS_WINDOWS", True)
    monkeypatch.setattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x200, raising=False)
    monkeypatch.setattr(subprocess, "CREATE_NO_WINDOW", 0x8000000, raising=False)
    captured = {}

    def fake_popen(command, **kwargs):
        captured.update(kwargs)
        return SimpleNamespace(pid=1234)

    monkeypatch.setattr(dev_module.subprocess, "Popen", fake_popen)

    dev_module.spawn(["python", "-m", "uvicorn"], tmp_path, {}, None, no_console=True)

    assert captured["creationflags"] == 0x200 | 0x8000000
