"""Catálogo estructurado de componentes Talend (rules/talend/components.json).

Fuente: definiciones XML de Talaxie (fork abierto de Talend Open Studio). Los nombres de parámetro
son los internos (los mismos que talend-mcp devuelve en un Job). Un nombre presente aquí es un nombre real de
Talend; solo `verified` (talend-mcp sobre un Job real) confirma que el paso concreto es válido.
"""

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
CATALOG_PATH = ROOT / "rules" / "talend" / "components.json"
CURRENT_GUIDE_INDEX = ROOT / "rules" / "talend" / "component-documentation-index.json"
CURRENT_INVENTORY = ROOT / "rules" / "talend" / "official-component-inventory.json"
CURRENT_FRAMEWORKS = {"DI", "SPARK", "STRUCTUREDSTREAMING", "CAMEL"}
LICENSE_PROFILE_CODE = "TP_ALL"
LICENSE_PROFILE_LABEL = "Talend Data Fabric"


def profile_availability_records(item: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        record
        for record in item.get("availability", [])
        if record.get("framework_code") in CURRENT_FRAMEWORKS
        and LICENSE_PROFILE_CODE in record.get("license_branding_codes", [])
    ]


def current_profile_names(inventory: dict[str, Any], guide_index: dict[str, Any]) -> set[str]:
    profile = guide_index.get("license_profile")
    if not isinstance(profile, dict) or profile.get("code") != LICENSE_PROFILE_CODE:
        raise ValueError("guide index is not for the Talend Data Fabric profile")
    guides = {item["name"]: item for item in guide_index["components"]}
    return {
        item["name"]
        for item in inventory["components"]
        if guides.get(item["name"], {}).get("lifecycle_status") == "current"
        and profile_availability_records(item)
    }


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
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        guide_index = json.loads(CURRENT_GUIDE_INDEX.read_text(encoding="utf-8"))
        inventory = json.loads(CURRENT_INVENTORY.read_text(encoding="utf-8"))
        current = {item["name"]: item for item in guide_index["components"]}
        current_names = current_profile_names(inventory, guide_index)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        raise RuntimeError(
            "Current Talend Studio 8 catalog indexes are missing or invalid"
        ) from exc
    data["components"] = {
        name: component for name, component in data["components"].items() if name in current_names
    }
    active_names = set(data["components"])
    data["families"] = {
        family: names
        for family, values in data.get("families", {}).items()
        if (names := sorted(set(values) & active_names))
    }
    data["variants"] = {
        role: technologies
        for role, groups in data.get("variants", {}).items()
        if (
            technologies := {
                technology: names
                for technology, values in groups.items()
                if (names := sorted(set(values) & active_names))
            }
        )
    }
    for name, component in data["components"].items():
        documentation = current[name]["documentation"]
        route_pages = [
            page
            for route in documentation.get("routes", [])
            for page in route.get("pages", [])
            if page.get("status") == "ok"
        ]
        config_pages = [
            page
            for page in documentation.get("configuration_pages", [])
            if page.get("status") == "ok"
        ]
        page = next(
            (item for item in route_pages if item.get("url") == component.get("doc_url")),
            None,
        )
        framework_codes = set(current[name].get("framework_codes", []))
        preferred_title = (
            "standard properties"
            if "DI" in framework_codes
            else "spark batch"
            if "SPARK" in framework_codes
            else "structured streaming"
            if "STRUCTUREDSTREAMING" in framework_codes
            else ""
        )
        page = (
            page
            or next(
                (
                    item
                    for item in config_pages
                    if preferred_title and preferred_title in str(item.get("title", "")).casefold()
                ),
                None,
            )
            or next(iter(config_pages or route_pages), None)
        )
        if documentation.get("status") == "documented" and page:
            component["doc_url"] = page["url"]
        else:
            component.pop("doc_url", None)
    data["count"] = len(data["components"])
    data.pop("official_inventory", None)
    data.pop("official_audit", None)
    return Catalog(data)
