import json
import re
import time
from functools import lru_cache
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException, Response

from sas_grid_migrator.talend_adapter.catalog import (
    LICENSE_PROFILE_CODE,
    LICENSE_PROFILE_LABEL,
    current_profile_names,
    profile_availability_records,
)

router = APIRouter(prefix="/api")
_STUDIO_COMPONENT_NAMES: tuple[float, frozenset[str]] | None = None


async def _installed_studio_component_names() -> frozenset[str]:
    global _STUDIO_COMPONENT_NAMES
    now = time.monotonic()
    if _STUDIO_COMPONENT_NAMES and now < _STUDIO_COMPONENT_NAMES[0]:
        return _STUDIO_COMPONENT_NAMES[1]

    from sas_grid_migrator.talend_adapter.adapter import TalendAdapter, TalendError

    try:
        names = await TalendAdapter.from_env().installed_component_names()
    except TalendError as exc:
        raise HTTPException(503, "no se pudo validar el catálogo contra Talend Studio") from exc
    installed = frozenset(names)
    _STUDIO_COMPONENT_NAMES = (now + 60, installed)
    return installed


@router.get("/talend/catalog/{name}/icon")
async def talend_component_icon(name: str) -> Response:
    if not re.fullmatch(r"[A-Za-z0-9]+", name):
        raise HTTPException(404, "icono de componente no disponible")
    from sas_grid_migrator.talend_adapter.adapter import TalendAdapter, TalendError

    try:
        svg = await TalendAdapter.from_env().component_icon(name)
    except TalendError as exc:
        raise HTTPException(503, "no se pudo consultar Talend Studio") from exc
    if svg is None:
        raise HTTPException(404, "el componente no tiene SVG de lienzo en Talend Studio")
    return Response(
        content=svg,
        media_type="image/svg+xml",
        headers={"Cache-Control": "public, max-age=3600", "X-Content-Type-Options": "nosniff"},
    )


@lru_cache(maxsize=1)
def _talend_documentation_data() -> tuple[
    dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]
]:
    root = Path(__file__).resolve().parents[2]
    try:
        availability = json.loads(
            (root / "rules/talend/official-component-inventory.json").read_text()
        )
        guides = json.loads((root / "rules/talend/component-documentation-index.json").read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError("Official Talend documentation indexes are missing or invalid") from exc
    try:
        guides_by_name = {item["name"]: item for item in guides["components"]}
        current_names = current_profile_names(availability, guides)
    except (KeyError, TypeError, ValueError) as exc:
        raise RuntimeError("Official Talend documentation indexes are missing or invalid") from exc
    available_by_name = {}
    for item in availability["components"]:
        records = profile_availability_records(item)
        if item["name"] in current_names:
            available_by_name[item["name"]] = {**item, "availability": records}
    return availability, guides, available_by_name, guides_by_name


@lru_cache(maxsize=1)
def _talend_installation_exclusions() -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    root = Path(__file__).resolve().parents[2]
    try:
        archive = json.loads(
            (root / "rules/archive/talend/studio8-default-install-exclusions.json").read_text()
        )
        components = {item["name"]: item for item in archive["components"]}
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise RuntimeError("Talend Studio 8 installation archive is missing or invalid") from exc
    return archive, components


def _archived_component(item: dict[str, Any], source: str) -> dict[str, Any]:
    return {
        "name": item["name"],
        "status": item["status"],
        "reason": item["reason"],
        "families": item["families"],
        "framework_codes": item["framework_codes"],
        "source_url": item.get("source_url") if item["status"] == "optional_install" else None,
        "availability_source": source,
        "runtime_verified": False,
    }


@lru_cache(maxsize=4096)
def _official_component_description(root: Path, name: str, status: str) -> str:
    if status != "documented":
        return "Ficha vigente de Talend Studio 8 aún no localizada."
    path = root / "docs/reference/talend" / f"{name}.md"
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return "Consulta la referencia oficial de este componente en Talend Studio 8."
    paragraph: list[str] = []
    for line in lines:
        text = line.strip()
        if not text:
            if paragraph:
                break
            continue
        if (
            text.startswith(("<!--", "#", "---", "|", "* [", "[##", "**"))
            or text.lower().startswith("last updated:")
            or "deprecated" in text.casefold()
        ):
            continue
        paragraph.append(text)
    if paragraph:
        return " ".join(paragraph)
    return "Consulta la referencia oficial de este componente en Talend Studio 8."


@router.get("/talend/catalog")
async def talend_catalog(q: str = "", family: str | None = None) -> dict:
    availability, _, available_by_name, guides_by_name = _talend_documentation_data()
    installed_names = await _installed_studio_component_names()
    root = Path(__file__).resolve().parents[2]
    rows = []
    family_counts: dict[str, int] = {}
    license_profile = {
        "code": LICENSE_PROFILE_CODE,
        "label": availability["license_branding_labels"][LICENSE_PROFILE_CODE],
    }
    for name, official in available_by_name.items():
        if name not in installed_names:
            continue
        records = official["availability"]
        item_families = sorted(
            {
                part.strip()
                for record in records
                for part in record.get("family", "").split("|")
                if part.strip()
            }
        )
        framework_codes = sorted({record["framework_code"] for record in records})
        frameworks = [availability["frameworks"].get(code, code) for code in framework_codes]
        guide = guides_by_name[name]
        doc = guide["documentation"]
        row = {
            "name": name,
            "description": _official_component_description(root, name, doc["status"]),
            "families": item_families,
            "documentation_status": doc["status"],
            "lifecycle_status": guide["lifecycle_status"],
            "frameworks": frameworks,
            "license_profile": license_profile,
            "search_terms": [*framework_codes, *frameworks],
        }
        rows.append(row)
        for item_family in item_families:
            family_counts[item_family] = family_counts.get(item_family, 0) + 1
    rows.sort(key=lambda item: item["name"].casefold())
    query = q.casefold().strip()
    filtered = [
        item
        for item in rows
        if (
            not query
            or query
            in " ".join(
                [item["name"], item["description"], *item["families"], *item["search_terms"]]
            ).casefold()
        )
        and (not family or family.casefold() in {value.casefold() for value in item["families"]})
    ]
    documentation_statuses = [guides_by_name[item["name"]]["documentation"]["status"] for item in rows]
    return {
        "count": len(rows),
        "result_count": len(filtered),
        "has_more": len(filtered) > 300,
        "families": dict(sorted(family_counts.items())),
        "components": filtered[:300],
        "official_component_names": [item["name"] for item in rows],
        "official_documentation_inventory": {
            "target": availability["documentation_target"],
            "snapshot_version": availability["availability_snapshot_version"],
            "source": availability["source"]["availability_page"],
            "license_profile": license_profile,
            "count": len(rows),
            "not_installed": len(available_by_name) - len(rows),
            "documented": documentation_statuses.count("documented"),
            "exception": documentation_statuses.count("exception"),
        },
    }


@router.get("/talend/catalog/archived")
def talend_archived_catalog(q: str = "") -> dict:
    archive, components_by_name = _talend_installation_exclusions()
    rows = [
        _archived_component(item, archive["source"])
        for item in sorted(components_by_name.values(), key=lambda item: item["name"].casefold())
    ]
    query = q.casefold().strip()
    filtered = [
        item
        for item in rows
        if not query
        or query
        in " ".join(
            [item["name"], item["status"], item["reason"], *item["families"], *item["framework_codes"]]
        ).casefold()
    ]
    return {
        "target": archive["documentation_target"],
        "source": archive["source"],
        "count": len(rows),
        "result_count": len(filtered),
        "components": filtered,
    }


@router.get("/talend/catalog/archived/{name}")
def talend_archived_component(name: str) -> dict:
    archive, components_by_name = _talend_installation_exclusions()
    item = components_by_name.get(name)
    if item is None:
        raise HTTPException(404, "componente no encontrado en el archivo de instalación")
    return {
        "target": archive["documentation_target"],
        **_archived_component(item, archive["source"]),
    }


@router.get("/talend/studio-configuration")
def talend_studio_configuration() -> dict:
    root = Path(__file__).resolve().parents[2]
    guide = root / "docs/reference/talend/studio-configuration.md"
    try:
        markdown = guide.read_text(encoding="utf-8")
    except OSError as exc:
        raise HTTPException(
            503, "guía de configuración global de Talend Studio no disponible"
        ) from exc
    return {
        "target": "Talend Studio 8.0 R2026-09",
        "source": "https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/appendices",
        "markdown": markdown,
    }


@router.get("/talend/catalog/{name}")
async def talend_component(name: str) -> dict:
    installed_names = await _installed_studio_component_names()
    if name not in installed_names:
        raise HTTPException(404, "componente no instalado en Talend Studio")
    availability, guides, available_by_name, guides_by_name = _talend_documentation_data()
    official = available_by_name.get(name)
    guide = guides_by_name.get(name)
    if official is None or guide is None:
        raise HTTPException(404, "componente no disponible en Talend Studio 8")
    records = official["availability"]
    families = sorted(
        {
            part.strip()
            for record in records
            for part in record.get("family", "").split("|")
            if part.strip()
        }
    )
    framework_codes = sorted({record["framework_code"] for record in records})
    root = Path(__file__).resolve().parents[2]
    doc = guide["documentation"]
    return {
        "name": name,
        "description": _official_component_description(root, name, doc["status"]),
        "families": families,
        "parameters": [],
        "connectors": [],
        "imports": [],
        "variants": [],
        "doc_markdown": None,
        "official_availability": {
            "license_profile": {"code": LICENSE_PROFILE_CODE, "label": LICENSE_PROFILE_LABEL},
            "source": availability["source"]["availability_page"],
            "snapshot_version": availability["availability_snapshot_version"],
            "records": [
                {
                    "family": record["family"],
                    "framework_code": record["framework_code"],
                    "documentation_route": record["documentation_route"],
                    "license_branding_codes": [LICENSE_PROFILE_CODE],
                    "license_branding_labels": [LICENSE_PROFILE_LABEL],
                }
                for record in records
            ],
            "frameworks": [
                {"code": code, "label": availability["frameworks"].get(code, code)}
                for code in framework_codes
            ],
        },
        "official_documentation": {
            "target": guides["documentation_target"],
            "framework_codes": guide["framework_codes"],
            "lifecycle_status": guide["lifecycle_status"],
            **doc,
        },
    }
