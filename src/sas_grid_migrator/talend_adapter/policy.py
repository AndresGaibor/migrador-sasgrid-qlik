"""Allowlist de lectura y aplicación de guías para tools de talend-mcp.

La aplicación solo invoca writers tipados tras una confirmación del usuario.
Los nombres viven en `contract/portal-tools.json`; aquí se derivan.
"""

from sas_grid_migrator.talend_adapter.contract import load_contract

_CONTRACT = load_contract()

READ_TOOLS = _CONTRACT.read_tools
WRITE_TOOLS = frozenset({_CONTRACT.write_tool})


class ToolNotAllowed(PermissionError):
    pass


def assert_allowed(tool: str) -> None:
    if tool not in READ_TOOLS and tool not in WRITE_TOOLS:
        raise ToolNotAllowed(f"{tool} no está en la allowlist de lectura y creación")
