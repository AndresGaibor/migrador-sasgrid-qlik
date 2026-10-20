"""Snapshot Qlik Help's official Talend component availability inventory."""

import json
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "rules" / "talend" / "official-component-inventory.json"
AVAILABILITY_URL = "https://help.qlik.com/talend/en-US/studio-components-availability/8.0/"
DATA_URL = "https://help.qlik.com/talend/js/components/componentList.json"
MAX_BYTES = 5_000_000
BRANDING_LABELS_SOURCE = "https://help.qlik.com/talend/js/scripts.min.js?v=5.8.5.17"
BRANDING_LABELS = {
    "tos_bd": "Talend Open Studio for Big Data",
    "tos_di": "Talend Open Studio for Data Integration",
    "top": "Talend Open Studio for Data Quality",
    "tos_esb": "Talend Open Studio for ESB",
    "TBD": "Talend Big Data",
    "TDI": "Talend Data Integration",
    "ESB_EE": "Talend ESB",
    "TP_BD": "Talend Big Data Platform",
    "TP_DM": "Talend Data Management Platform",
    "TP_DS": "Talend Data Services Platform",
    "TP_DS_BDRT": "Talend Real-time Big Data Platform",
    "TP_MDM": "Talend MDM Platform",
    "TP_ALL": "Talend Data Fabric",
    "TC_DI": "Talend Cloud Data Integration",
    "TC_BD": "Talend Cloud Big Data",
    "TCP_BD": "Talend Cloud Big Data Platform",
    "TCP_DM": "Talend Cloud Data Management Platform",
    "TCP_RTBD": "Talend Cloud Data Fabric",
    "TCP_APIS": "Talend Cloud API Services Platform",
    "JETL": "TIBCOJaspersoftETL",
    "JETLBigData": "TIBCOJaspersoftETLExtendedBigData",
    "QTC_P": "Qlik Talend Cloud Premium Edition",
    "QTC_E": "Qlik Talend Cloud Enterprise Edition",
}
FRAMEWORKS = {
    "DI": "Standard",
    "SPARK": "Spark Batch",
    "SPARKSTREAMING": "Spark Streaming",
    "STRUCTUREDSTREAMING": "Structured Streaming",
    "CAMEL": "Camel",
}


def normalize_inventory(source: object, captured_at: str) -> dict[str, Any]:
    if not isinstance(source, dict):
        raise TypeError("Qlik component inventory must be a JSON object")
    version = source.get("version")
    codes = source.get("brandings")
    rows = source.get("components")
    if not isinstance(version, str):
        raise TypeError("Qlik component inventory version must be a string")
    if not version:
        raise ValueError("Qlik component inventory is missing its version")
    if not isinstance(codes, str):
        raise TypeError("Qlik component branding codes must be a string")
    if not codes:
        raise ValueError("Qlik component inventory is missing license branding codes")
    if not isinstance(rows, list):
        raise TypeError("Qlik component inventory records must be a list")
    if not rows:
        raise ValueError("Qlik component inventory has no component records")

    license_codes = {code.strip() for code in codes.split(",") if code.strip()}
    unknown_codes = license_codes - BRANDING_LABELS.keys()
    if unknown_codes:
        raise ValueError(f"Unknown Qlik license branding codes: {sorted(unknown_codes)}")
    by_name: dict[str, list[dict[str, object]]] = defaultdict(list)
    pair_names: set[tuple[str, str]] = set()
    framework_names: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, dict):
            raise TypeError("Qlik component inventory contains a non-object record")
        name, family, palette, branding = (
            row.get("componentName"),
            row.get("family"),
            row.get("paletteType"),
            row.get("brandings"),
        )
        if not isinstance(name, str) or not isinstance(family, str) or not isinstance(palette, str):
            raise TypeError("Qlik component name, family, and framework must be strings")
        if not name or not family or not palette:
            raise ValueError("Qlik component record is missing its name, family, or framework")
        if palette not in FRAMEWORKS:
            raise ValueError(f"Unknown Qlik palette type {palette!r} for {name}")
        if not isinstance(branding, str):
            raise TypeError(f"Qlik component license codes must be a string: {name}")
        row_codes = [code.strip() for code in branding.split(",") if code.strip()]
        if set(row_codes) - license_codes:
            raise ValueError(f"Qlik component record uses undeclared license codes: {name}")

        by_name[name].append(
            {
                "family": family,
                "framework_code": palette,
                "documentation_route": "Routes" if palette == "CAMEL" else "Jobs",
                "license_branding_codes": sorted(set(row_codes)),
            }
        )
        pair_names.add((name, palette))
        framework_names[palette].add(name)

    components = [
        {
            "name": name,
            "availability": sorted(
                entries,
                key=lambda entry: (
                    str(entry["framework_code"]),
                    str(entry["family"]),
                    str(entry["license_branding_codes"]),
                ),
            ),
        }
        for name, entries in sorted(by_name.items())
    ]
    return {
        "schema_version": 1,
        "documentation_target": "Talend Studio 8.0 R2026-09",
        "availability_snapshot_version": version,
        "captured_at": captured_at,
        "source": {
            "availability_page": AVAILABILITY_URL,
            "data_url": DATA_URL,
            "framework_labels": BRANDING_LABELS_SOURCE,
            "license_branding_labels": BRANDING_LABELS_SOURCE,
            "license_codes": AVAILABILITY_URL,
            "component_documentation_templates": {
                "Jobs": "https://help.qlik.com/talend/en-US/components/8.0/{name}",
                "Routes": "https://help.qlik.com/talend/en-US/mediation-components/8.0/{name}",
            },
        },
        "license_branding_codes": sorted(license_codes),
        "license_branding_labels": {code: BRANDING_LABELS[code] for code in sorted(license_codes)},
        "frameworks": FRAMEWORKS,
        "counts": {
            "source_records": len(rows),
            "components": len(components),
            "component_framework_pairs": len(pair_names),
            "components_by_framework": {
                code: len(names) for code, names in sorted(framework_names.items())
            },
        },
        "components": components,
    }


def fetch_inventory() -> dict:
    request = Request(DATA_URL, headers={"User-Agent": "migrador-sasgrid-qlik docs inventory sync"})
    try:
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise ValueError(f"Qlik inventory returned HTTP {response.status}")
            raw = response.read(MAX_BYTES + 1)
    except URLError as exc:
        raise RuntimeError(f"Could not fetch official Qlik inventory: {exc}") from exc
    if len(raw) > MAX_BYTES:
        raise ValueError("Qlik component inventory exceeded the 5 MB safety limit")
    try:
        return json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("Qlik component inventory was not valid JSON") from exc


def main() -> None:
    manifest = normalize_inventory(fetch_inventory(), datetime.now(UTC).date().isoformat())
    encoded = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(encoded, encoding="utf-8")
    temporary.replace(OUTPUT)
    counts = manifest["counts"]
    if not isinstance(counts, dict):
        raise TypeError("Normalized inventory is missing counts")
    print(
        f"Wrote {counts['components']} official component names "
        f"({counts['source_records']} availability records) to {OUTPUT.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
