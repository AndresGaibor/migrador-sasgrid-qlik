"""Build a versioned index of official Talend component docs and configuration pages."""

import argparse
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "rules" / "talend" / "official-component-inventory.json"
DOC_INDEX = ROOT / "docs" / "reference" / "talend" / "index.json"
DOCS_DIR = ROOT / "docs" / "reference" / "talend"
OUTPUT = ROOT / "rules" / "talend" / "component-documentation-index.json"
INSTALLATION_EXCLUSIONS = ROOT / "rules" / "archive" / "talend" / "studio8-default-install-exclusions.json"
FETCHER_SCHEMA_VERSION = 5
SETTINGS_TITLE = re.compile(
    r"properties|settings|configuration|configuring|parameters", re.IGNORECASE
)
CONFIG_SECTION = re.compile(r"properties|settings|global variables|configuration", re.IGNORECASE)
DEPRECATED = re.compile(r"\bdeprecated\b", re.IGNORECASE)
CURRENT_FRAMEWORKS = {"DI", "SPARK", "STRUCTUREDSTREAMING", "CAMEL"}
LICENSE_PROFILE_CODE = "TP_ALL"
SOURCE_COMMENT = re.compile(r"^<!--\s*fuente:\s*(\S+)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
COMPONENT_NAME = re.compile(r"[A-Za-z0-9_]+\Z")


def _dict(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{label} must be a JSON object")
    return value


def _list(value: object, label: str) -> list:
    if not isinstance(value, list):
        raise TypeError(f"{label} must be a JSON array")
    return value


def _text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} must be a non-empty string")
    return value


def _official_url(value: object, label: str) -> str:
    url = _text(value, label)
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "help.qlik.com":
        raise ValueError(f"{label} must be an official HTTPS Qlik Help URL")
    return url


def _deprecated_availability(entry: dict[str, Any]) -> bool:
    families = [
        family.strip().casefold()
        for family in str(entry.get("family", "")).split("|")
        if family.strip()
    ]
    return bool(families) and all("(deprecated)" in family for family in families)


def _installation_exclusion_statuses(
    archive: object | None,
    documentation_target: str,
    inventory_version: str,
) -> dict[str, str]:
    if archive is None:
        return {}
    data = _dict(archive, "installation exclusion archive")
    if data.get("documentation_target") != documentation_target:
        raise ValueError("installation exclusion archive has a different documentation target")
    if data.get("availability_snapshot_version") != inventory_version:
        raise ValueError("installation exclusion archive has a different availability snapshot")
    profile = _dict(data.get("license_profile"), "installation exclusion archive.license_profile")
    if profile.get("code") != LICENSE_PROFILE_CODE:
        raise ValueError("installation exclusion archive has a different license profile")
    exclusions = {}
    for number, raw in enumerate(_list(data.get("components"), "installation exclusion archive.components")):
        item = _dict(raw, f"installation exclusion archive.components[{number}]")
        name = _text(item.get("name"), f"installation exclusion archive.components[{number}].name")
        if not COMPONENT_NAME.fullmatch(name):
            raise ValueError(f"Invalid archived component name: {name!r}")
        status = _text(item.get("status"), f"{name}.status")
        if status not in {"optional_install", "removed_from_target_release"}:
            raise ValueError(f"Invalid installation exclusion status for {name}: {status}")
        _official_url(item.get("source_url"), f"{name}.source_url")
        if name in exclusions:
            raise ValueError(f"Duplicate archived component: {name}")
        exclusions[name] = status
    return exclusions


def _page(page: object, label: str) -> dict[str, Any]:
    source = _dict(page, label)
    url = _official_url(source.get("url"), f"{label}.url")
    status = _text(source.get("status"), f"{label}.status")
    result: dict[str, Any] = {"url": url, "status": status}
    for key in ("title", "requested_url", "resolved_url"):
        value = source.get(key)
        if isinstance(value, str) and value:
            result[key] = value if key == "title" else _official_url(value, f"{label}.{key}")
    redirected = source.get("redirected")
    if isinstance(redirected, bool) or redirected is None:
        result["redirected"] = redirected
    return result


def _route(route: object, index: int) -> dict[str, Any]:
    source = _dict(route, f"routes[{index}]")
    result: dict[str, Any] = {
        "route": _text(source.get("route"), f"routes[{index}].route"),
        "status": _text(source.get("status"), f"routes[{index}].status"),
        "pages": [
            _page(page, f"routes[{index}].pages[{number}]")
            for number, page in enumerate(_list(source.get("pages"), f"routes[{index}].pages"))
            if not DEPRECATED.search(
                str(_dict(page, f"routes[{index}].pages[{number}]").get("title", ""))
            )
        ],
    }
    for key in ("requested_url", "resolved_url"):
        value = source.get(key)
        if isinstance(value, str) and value:
            result[key] = _official_url(value, f"routes[{index}].{key}")
    redirected = source.get("redirected")
    if isinstance(redirected, bool) or redirected is None:
        result["redirected"] = redirected
    return result


def _configuration_sections(markdown_path: Path) -> tuple[list[dict[str, Any]], bool]:
    source_url: str | None = None
    source_deprecated = False
    sections = []
    seen: set[tuple[str, str]] = set()
    missing_source = False
    for line in markdown_path.read_text(encoding="utf-8").splitlines():
        source_match = SOURCE_COMMENT.match(line)
        if source_match:
            source_url = _official_url(source_match.group(1), "local Markdown source")
            source_deprecated = False
            continue
        heading_match = HEADING.match(line)
        if not heading_match:
            continue
        if len(heading_match.group(1)) == 1:
            source_deprecated = bool(DEPRECATED.search(heading_match.group(2)))
        if source_deprecated or not CONFIG_SECTION.search(heading_match.group(2)):
            continue
        heading = heading_match.group(2).strip()
        if source_url is None:
            missing_source = True
            continue
        key = source_url, heading
        if key not in seen:
            seen.add(key)
            sections.append({"url": source_url, "heading": heading})
    return sections, missing_source


def _component_guide(
    component: dict[str, Any],
    row: dict[str, Any] | None,
    inventory_version: str,
    documentation_target: str,
    docs_dir: Path,
    lifecycle_status: str = "current",
) -> dict[str, Any]:
    name = _text(component.get("name"), "component.name")
    if not COMPONENT_NAME.fullmatch(name):
        raise ValueError(f"Invalid component name in official inventory: {name!r}")
    availability = _list(component.get("availability"), f"{name}.availability")
    frameworks = sorted(
        {
            _text(
                _dict(item, f"{name}.availability entry").get("framework_code"),
                f"{name}.framework_code",
            )
            for item in availability
        }
    )
    routes = (
        [
            _route(route, index)
            for index, route in enumerate(_list(row.get("routes"), f"{name}.routes"))
        ]
        if row
        else []
    )
    markdown_path = docs_dir / f"{name}.md"
    markdown_available = markdown_path.is_file() and markdown_path.stat().st_size > 0
    issues: list[str] = []
    if row is None:
        status = "not_fetched"
        issues.append("no_local_fetch_record")
    elif (
        row.get("fetcher_schema_version") != FETCHER_SCHEMA_VERSION
        or row.get("source_inventory_version") != inventory_version
        or row.get("documentation_target") != documentation_target
    ):
        status = "needs_refresh"
        issues.append("fetch_record_is_stale")
    elif row.get("status") != "ok" or not routes:
        status = "exception"
        issues.extend(route["status"] for route in routes if route["status"] != "ok")
        if not issues:
            issues.append(
                "missing_routes" if not routes else str(row.get("status", "unknown_status"))
            )
    elif any(not route["pages"] for route in routes) or any(
        route["status"] != "ok" or any(page["status"] != "ok" for page in route["pages"])
        for route in routes
    ):
        status = "exception"
        issues.append("one_or_more_documentation_pages_failed")
    elif not markdown_available:
        status = "needs_refresh"
        issues.append("local_markdown_missing")
    else:
        status = "documented"

    configuration_sections: list[dict[str, Any]] = []
    if status == "documented":
        configuration_sections, missing_source = _configuration_sections(markdown_path)
        indexed_urls = {
            urlsplit(url)._replace(query="", fragment="").geturl()
            for route in routes
            for page in route["pages"]
            for url in (page.get("url"), page.get("requested_url"), page.get("resolved_url"))
            if isinstance(url, str)
        }
        if missing_source or any(
            urlsplit(section["url"])._replace(query="", fragment="").geturl() not in indexed_urls
            for section in configuration_sections
        ):
            status = "needs_refresh"
            issues.append("configuration_source_missing")

    section_titles: dict[str, str] = {}
    for section in configuration_sections:
        key = urlsplit(section["url"])._replace(query="", fragment="").geturl()
        section_titles.setdefault(key, section["heading"])
    configuration_pages_by_url: dict[str, dict[str, Any]] = {}
    for route in routes:
        for page in route["pages"]:
            page_urls = [
                urlsplit(value)._replace(query="", fragment="").geturl()
                for value in (page.get("url"), page.get("requested_url"), page.get("resolved_url"))
                if isinstance(value, str)
            ]
            section_title = next(
                (section_titles[url] for url in page_urls if url in section_titles), None
            )
            page_title = page.get("title", "")
            if not SETTINGS_TITLE.search(page_title) and section_title is None:
                continue
            page_url = page.get("resolved_url") or page.get("requested_url") or page["url"]
            page_key = urlsplit(page_url)._replace(query="", fragment="").geturl()
            config_page = {"route": route["route"], **page, "url": page_url}
            if section_title is not None and not SETTINGS_TITLE.search(page_title):
                config_page["title"] = section_title
            configuration_pages_by_url.setdefault(page_key, config_page)
    configuration_pages = sorted(
        configuration_pages_by_url.values(),
        key=lambda page: (page["route"], page.get("title", ""), page["url"]),
    )
    return {
        "name": name,
        "framework_codes": frameworks,
        "lifecycle_status": lifecycle_status if availability else "unknown",
        "documentation": {
            "status": status,
            "source": "Qlik Help",
            "local_markdown_available": markdown_available,
            "routes": routes,
            "configuration_pages": configuration_pages,
            "configuration_sections": configuration_sections,
            "issues": sorted(set(issues)),
        },
    }


def build_component_documentation_index(
    inventory: object,
    local_index: object,
    docs_dir: Path,
    installation_exclusions: object | None = None,
) -> dict[str, Any]:
    manifest = _dict(inventory, "official inventory")
    inventory_version = _text(
        manifest.get("availability_snapshot_version"), "availability_snapshot_version"
    )
    documentation_target = _text(manifest.get("documentation_target"), "documentation_target")
    license_labels = _dict(
        manifest.get("license_branding_labels"), "official inventory.license_branding_labels"
    )
    license_profile = {
        "code": LICENSE_PROFILE_CODE,
        "label": _text(license_labels.get(LICENSE_PROFILE_CODE), LICENSE_PROFILE_CODE),
    }
    source = _dict(manifest.get("source"), "official inventory.source")
    _official_url(source.get("availability_page"), "official inventory.source.availability_page")
    components = _list(manifest.get("components"), "official inventory.components")
    index_rows = _list(local_index, "local documentation index")
    exclusion_statuses = _installation_exclusion_statuses(
        installation_exclusions, documentation_target, inventory_version
    )
    rows: dict[str, dict[str, Any]] = {}
    for number, raw in enumerate(index_rows):
        row = _dict(raw, f"local documentation index[{number}]")
        name = _text(row.get("name"), f"local documentation index[{number}].name")
        if name in rows:
            raise ValueError(f"Duplicate local documentation record: {name}")
        rows[name] = row

    guides = []
    names: set[str] = set()
    current_profile_names: set[str] = set()
    for number, raw in enumerate(components):
        component = _dict(raw, f"official inventory.components[{number}]")
        name = _text(component.get("name"), f"official inventory.components[{number}].name")
        if name in names:
            raise ValueError(f"Duplicate official component: {name}")
        names.add(name)
        availability = _list(component.get("availability"), f"{name}.availability")
        current_availability = [
            entry
            for item in availability
            if (
                (entry := _dict(item, f"{name}.availability entry"))["framework_code"]
                in CURRENT_FRAMEWORKS
                and LICENSE_PROFILE_CODE
                in _list(
                    entry.get("license_branding_codes"),
                    f"{name}.availability.license_branding_codes",
                )
                and not _deprecated_availability(entry)
            )
        ]
        row = rows.get(name)
        if not current_availability:
            continue
        current_profile_names.add(name)
        guides.append(
            _component_guide(
                {**component, "availability": current_availability},
                row,
                inventory_version,
                documentation_target,
                docs_dir,
                exclusion_statuses.get(name, "current"),
            )
        )

    unknown_exclusions = set(exclusion_statuses) - current_profile_names
    if unknown_exclusions:
        raise ValueError(
            "Installation exclusions outside the selected current profile: "
            + ", ".join(sorted(unknown_exclusions))
        )

    counts: dict[str, int] = {}
    lifecycle_counts: dict[str, int] = {}
    for guide in guides:
        status = guide["documentation"]["status"]
        counts[status] = counts.get(status, 0) + 1
        lifecycle = guide["lifecycle_status"]
        lifecycle_counts[lifecycle] = lifecycle_counts.get(lifecycle, 0) + 1
    return {
        "schema_version": 3,
        "documentation_target": documentation_target,
        "license_profile": license_profile,
        "availability_snapshot_version": inventory_version,
        "source": {
            "availability_page": source["availability_page"],
            "component_documentation": source.get("component_documentation_templates", {}),
        },
        "counts": {key: counts[key] for key in sorted(counts)},
        "lifecycle_counts": {key: lifecycle_counts[key] for key in sorted(lifecycle_counts)},
        "active_component_count": lifecycle_counts.get("current", 0),
        "installation_exclusions": {
            "source": "rules/archive/talend/studio8-default-install-exclusions.json",
            "count": len(exclusion_statuses),
        },
        "components": guides,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=INVENTORY)
    parser.add_argument("--doc-index", type=Path, default=DOC_INDEX)
    parser.add_argument("--docs-dir", type=Path, default=DOCS_DIR)
    parser.add_argument("--installation-exclusions", type=Path, default=INSTALLATION_EXCLUSIONS)
    parser.add_argument("--out", type=Path, default=OUTPUT)
    args = parser.parse_args()
    try:
        inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
        local_index = json.loads(args.doc_index.read_text(encoding="utf-8"))
        exclusions = json.loads(args.installation_exclusions.read_text(encoding="utf-8"))
        guide_index = build_component_documentation_index(
            inventory, local_index, args.docs_dir, exclusions
        )
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        parser.error(f"could not build component documentation index: {exc}")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.out.with_suffix(args.out.suffix + ".tmp")
    temporary.write_text(
        json.dumps(guide_index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(args.out)
    active = guide_index["active_component_count"]
    archived = guide_index["installation_exclusions"]["count"]
    summary = f"{active} active, {archived} archived by default"
    print(
        f"Wrote {len(guide_index['components'])} component guides ({summary}) "
        f"to {args.out.relative_to(ROOT)}"
        if args.out.is_relative_to(ROOT)
        else f"Wrote {len(guide_index['components'])} component guides ({summary}) to {args.out}"
    )


if __name__ == "__main__":
    main()
