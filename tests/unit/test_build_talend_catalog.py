import json

import tools.build_talend_catalog as builder


def test_build_only_parses_current_studio_components(tmp_path, monkeypatch):
    source = tmp_path / "components"
    source.mkdir()
    current_index = tmp_path / "component-documentation-index.json"
    current_index.write_text(
        json.dumps(
            {
                "documentation_target": "Talend Studio 8.0 R2026-09",
                "license_profile": {"code": "TP_ALL", "label": "Talend Data Fabric"},
                "components": [
                    {"name": "tMap", "lifecycle_status": "current"},
                    {"name": "tDeprecatedFixture", "lifecycle_status": "deprecated"},
                ],
            }
        )
    )
    monkeypatch.setattr(builder, "CURRENT_GUIDE_INDEX_FILE", current_index)

    for name in ("tMap", "tExcludedFixture", "tDeprecatedFixture"):
        component = source / name
        component.mkdir()
        (component / f"{name}_java.xml").write_text(
            '<COMPONENT><HEADER STATUS="RELEASED" VERSION="1" STARTABLE="true" />'
            "<FAMILIES><FAMILY>Processing</FAMILY></FAMILIES></COMPONENT>"
        )

    catalog = builder.build(source)

    assert set(catalog["components"]) == {"tMap"}
    assert catalog["count"] == 1
    assert catalog["license_profile"] == {"code": "TP_ALL", "label": "Talend Data Fabric"}
    assert "official_inventory" not in catalog
    assert "official_audit" not in catalog
    assert "doc_url" not in catalog["components"]["tMap"]
