"""Catálogo estructurado de componentes Talend (rules/talend/components.json).

Fuente: definiciones XML de Talaxie (fork abierto de Talend Open Studio). Los nombres de parámetro
son los internos (los mismos que talend-mcp devuelve en un Job). Un nombre presente aquí es un nombre real de
Talend; solo `verified` (talend-mcp sobre un Job real) confirma que el paso concreto es válido.
"""

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

CATALOG_PATH = Path(__file__).resolve().parents[3] / "rules" / "talend" / "components.json"


class Catalog:
    def __init__(self, data: dict[str, Any]):
        self.data = data
        self.components: dict[str, dict[str, Any]] = data["components"]

    def has(self, name: str) -> bool:
        return name in self.components

    def get(self, name: str) -> dict[str, Any] | None:
        return self.components.get(name)

    def params(self, name: str) -> dict[str, dict[str, Any]]:
        c = self.components.get(name)
        return {p["name"]: p for p in c.get("parameters", [])} if c else {}

    def search(self, q: str = "", family: str | None = None) -> list[dict[str, Any]]:
        q = q.lower()
        out = []
        for n, c in self.components.items():
            if family and family not in c.get("families", []):
                continue
            if q and q not in n.lower() and q not in c.get("description", "").lower():
                continue
            out.append(
                {
                    "name": n,
                    "description": c.get("description", ""),
                    "families": c.get("families", []),
                    "parameters": len(c.get("parameters", [])),
                }
            )
        return out

    def variants_of(self, name: str) -> list[str]:
        """Componentes hermanos (mismo rol, otra tecnología): tOracleInput → tMysqlInput, …"""
        for techs in self.data.get("variants", {}).values():
            for comps in techs.values():
                if name in comps:
                    return sorted(c for ts in techs.values() for c in ts if c != name)
        return []


@lru_cache(maxsize=1)
def load_catalog(path: Path = CATALOG_PATH) -> Catalog:
    return Catalog(json.loads(path.read_text(encoding="utf-8")))
