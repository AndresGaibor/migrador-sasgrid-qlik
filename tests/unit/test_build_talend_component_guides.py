from pathlib import Path

import pytest
from tools.build_talend_component_guides import build_component_documentation_index


def _inventory() -> dict:
    return {
        "documentation_target": "Talend Studio 8.0 R2026-09",
        "availability_snapshot_version": "8.0.1.20261015_1208-patch",
        "license_branding_labels": {"TP_ALL": "Talend Data Fabric"},
        "source": {
            "availability_page": "https://help.qlik.com/talend/en-US/studio-components-availability/8.0/",
            "component_documentation_templates": {
                "Jobs": "https://help.qlik.com/talend/en-US/components/8.0/{name}",
                "Routes": "https://help.qlik.com/talend/en-US/mediation-components/8.0/{name}",
            },
        },
        "components": [
            {
                "name": "tFixedFlowInput",
                "availability": [
                    {
                        "framework_code": "DI",
                        "documentation_route": "Jobs",
                        "license_branding_codes": ["TP_ALL"],
                    },
                    {
                        "framework_code": "SPARK",
                        "documentation_route": "Jobs",
                        "license_branding_codes": ["TP_ALL"],
                    },
                ],
            },
            {
                "name": "cAWSMQBroker",
                "availability": [{"framework_code": "CAMEL", "license_branding_codes": ["TP_ALL"]}],
            },
            {
                "name": "tMap",
                "availability": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
            },
            {
                "name": "excluded_fixture",
                "availability": [
                    {"framework_code": "DI", "license_branding_codes": ["QTC_E", "QTC_P"]}
                ],
            },
            {
                "name": "tDeprecatedExample",
                "availability": [
                    {
                        "framework_code": "DI",
                        "family": "Databases/Legacy (Deprecated)",
                        "license_branding_codes": ["TP_ALL"],
                    }
                ],
            },
        ],
    }


def _row(name: str, *, status: str, routes: list[dict], version: int = 5) -> dict:
    return {
        "name": name,
        "status": status,
        "source_inventory_version": "8.0.1.20261015_1208-patch",
        "documentation_target": "Talend Studio 8.0 R2026-09",
        "fetcher_schema_version": version,
        "routes": routes,
    }


def test_builds_current_studio_guides_with_config_sources_and_exceptions(tmp_path: Path):
    (tmp_path / "tFixedFlowInput.md").write_text(
        "<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput -->\n"
        "## Standard properties\n## Advanced settings\n## Global Variables\n",
        encoding="utf-8",
    )
    index = [
        _row(
            "tFixedFlowInput",
            status="ok",
            routes=[
                {
                    "route": "Jobs",
                    "status": "ok",
                    "requested_url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput",
                    "resolved_url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput",
                    "redirected": False,
                    "pages": [
                        {
                            "url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput?id=31",
                            "title": "tFixedFlowInput",
                            "status": "ok",
                        },
                        {
                            "url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput-standard-properties",
                            "title": "tFixedFlowInput Standard properties",
                            "status": "ok",
                        },
                    ],
                }
            ],
        ),
        _row(
            "cAWSMQBroker",
            status="not_found",
            routes=[
                {
                    "route": "Routes",
                    "status": "not_found",
                    "requested_url": "https://help.qlik.com/talend/en-US/mediation-components/8.0/cawsmqbroker",
                    "resolved_url": "https://help.qlik.com/talend/en-US/mediation-components/8.0/cawsmqbroker",
                    "redirected": False,
                    "pages": [
                        {
                            "url": "https://help.qlik.com/talend/en-US/mediation-components/8.0/cawsmqbroker",
                            "status": "not_found",
                        }
                    ],
                }
            ],
        ),
    ]

    result = build_component_documentation_index(_inventory(), index, tmp_path)
    guides = {item["name"]: item for item in result["components"]}

    assert result["counts"] == {"documented": 1, "exception": 1, "not_fetched": 1}
    assert set(guides) == {"tFixedFlowInput", "cAWSMQBroker", "tMap"}
    assert result["license_profile"] == {"code": "TP_ALL", "label": "Talend Data Fabric"}
    assert all(
        set(guide["framework_codes"]) <= {"DI", "SPARK", "STRUCTUREDSTREAMING", "CAMEL"}
        for guide in guides.values()
    )
    assert guides["tFixedFlowInput"]["framework_codes"] == ["DI", "SPARK"]
    assert guides["tFixedFlowInput"]["documentation"]["status"] == "documented"
    assert any(
        page["title"] == "tFixedFlowInput Standard properties"
        for page in guides["tFixedFlowInput"]["documentation"]["configuration_pages"]
    )
    assert guides["tFixedFlowInput"]["documentation"]["configuration_sections"] == [
        {
            "url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput",
            "heading": "Standard properties",
        },
        {
            "url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput",
            "heading": "Advanced settings",
        },
        {
            "url": "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput",
            "heading": "Global Variables",
        },
    ]
    assert guides["cAWSMQBroker"]["documentation"]["issues"] == ["not_found"]
    assert guides["tMap"]["documentation"]["issues"] == ["no_local_fetch_record"]


def test_marks_optional_components_as_archived(tmp_path: Path):
    inventory = _inventory()
    inventory["components"].append(
        {
            "name": "tOptionalFixture",
            "availability": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
        }
    )
    archive = {
        "documentation_target": "Talend Studio 8.0 R2026-09",
        "availability_snapshot_version": "8.0.1.20261015_1208-patch",
        "license_profile": {"code": "TP_ALL"},
        "components": [
            {
                "name": "tOptionalFixture",
                "status": "optional_install",
                "source_url": "https://help.qlik.com/talend/en-US/components/8.0/toptionalfixture",
            }
        ],
    }
    result = build_component_documentation_index(inventory, [], tmp_path, archive)
    guides = {item["name"]: item for item in result["components"]}

    assert guides["tOptionalFixture"]["lifecycle_status"] == "optional_install"
    assert result["active_component_count"] == 3
    assert result["installation_exclusions"]["count"] == 1


def test_uses_resolved_subpage_url_for_configuration_source(tmp_path: Path):
    root_url = "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput"
    settings_url = f"{root_url}/tfixedflowinput"
    (tmp_path / "tFixedFlowInput.md").write_text(
        f"<!-- fuente: {settings_url} -->\n"
        "# tFixedFlowInput\n## Standard properties\n## Basic settings\n",
        encoding="utf-8",
    )
    index = [
        _row(
            "tFixedFlowInput",
            status="ok",
            routes=[
                {
                    "route": "Jobs",
                    "status": "ok",
                    "pages": [
                        {"url": root_url, "resolved_url": root_url, "title": "tFixedFlowInput", "status": "ok"},
                        {
                            "url": root_url,
                            "requested_url": settings_url,
                            "resolved_url": settings_url,
                            "title": "tFixedFlowInput",
                            "status": "ok",
                        },
                    ],
                }
            ],
        )
    ]

    result = build_component_documentation_index(_inventory(), index, tmp_path)
    guide = next(item for item in result["components"] if item["name"] == "tFixedFlowInput")
    documentation = guide["documentation"]

    assert documentation["status"] == "documented"
    assert documentation["configuration_sections"][0]["url"] == settings_url
    config_page = documentation["configuration_pages"][0]
    assert config_page["route"] == "Jobs"
    assert config_page["url"] == settings_url
    assert config_page["status"] == "ok"
    assert config_page["title"] == "Standard properties"


def test_marks_stale_index_and_missing_markdown_for_refresh(tmp_path: Path):
    index = [
        _row("tFixedFlowInput", status="ok", routes=[], version=2),
        _row("cAWSMQBroker", status="ok", routes=[]),
    ]

    result = build_component_documentation_index(_inventory(), index, tmp_path)
    guides = {item["name"]: item for item in result["components"]}

    assert guides["tFixedFlowInput"]["documentation"]["status"] == "needs_refresh"
    assert guides["tFixedFlowInput"]["documentation"]["issues"] == ["fetch_record_is_stale"]
    assert guides["cAWSMQBroker"]["documentation"]["status"] == "exception"
    assert guides["cAWSMQBroker"]["documentation"]["issues"] == ["missing_routes"]


def test_rejects_duplicate_official_names_unsafe_paths_and_external_urls(tmp_path: Path):
    inventory = _inventory()
    inventory["components"].append(inventory["components"][0])
    with pytest.raises(ValueError, match="Duplicate official component"):
        build_component_documentation_index(inventory, [], tmp_path)

    inventory = _inventory()
    inventory["components"][0]["name"] = "../secret"
    with pytest.raises(ValueError, match="Invalid component name"):
        build_component_documentation_index(inventory, [], tmp_path)

    index = [
        _row(
            "tFixedFlowInput",
            status="ok",
            routes=[
                {
                    "route": "Jobs",
                    "status": "ok",
                    "pages": [{"url": "https://attacker.invalid/tFixedFlowInput", "status": "ok"}],
                }
            ],
        )
    ]
    with pytest.raises(ValueError, match="official HTTPS Qlik Help URL"):
        build_component_documentation_index(_inventory(), index, tmp_path)
