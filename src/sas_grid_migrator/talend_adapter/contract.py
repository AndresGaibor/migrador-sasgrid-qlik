"""Contrato portal↔MCP: las tools que el portal necesita, en un solo manifiesto.

El manifiesto `contract/portal-tools.json` es la fuente única. La allowlist de
`policy.py`, el preset `portal` del MCP y la prueba de contrato se apoyan en él.
"""

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

#: Raíz del repositorio del portal (`src/sas_grid_migrator/talend_adapter/` → raíz).
REPO_ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = REPO_ROOT / "contract" / "portal-tools.json"


@dataclass(frozen=True)
class PortalContract:
    read_tools: frozenset[str]
    write_tool: str
    #: Escritura offline (sin Studio, ~1000 veces mas rapida). Opcional: sin ella todo va en vivo.
    offline_write_tool: str | None
    required_top_fields: frozenset[str]
    required_component_fields: frozenset[str]


@lru_cache(maxsize=4)
def load_contract(path: Path | None = None) -> PortalContract:
    """Lee y valida el manifiesto. Cacheada: se lee una vez por proceso y ruta."""
    raw = json.loads((path or CONTRACT_PATH).read_text(encoding="utf-8"))
    return PortalContract(
        read_tools=frozenset(raw["read_tools"]),
        write_tool=raw["write_tool"],
        offline_write_tool=raw.get("offline_write_tool"),
        required_top_fields=frozenset(raw["required_top_fields"]),
        required_component_fields=frozenset(raw["required_component_fields"]),
    )
