import socket

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
