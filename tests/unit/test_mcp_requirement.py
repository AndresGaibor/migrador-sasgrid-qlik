"""La dependencia `mcp` debe ser 2.x: el cliente de `read_timeout_seconds` no existe en 1.x."""

import tomllib
from pathlib import Path

PYPROJECT = Path(__file__).resolve().parents[2] / "pyproject.toml"


def test_pyproject_requires_mcp_2():
    data = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    dependencies = data["project"]["dependencies"]
    mcp = next((dep for dep in dependencies if dep.replace(" ", "").startswith("mcp")), None)
    assert mcp is not None, "pyproject.toml no declara la dependencia mcp"
    assert mcp.replace(" ", "").startswith("mcp>=2"), f"se esperaba mcp>=2.x, hay {mcp!r}"
