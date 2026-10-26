import pytest
from tools.sync_talend_official_inventory import normalize_inventory


def test_normalize_groups_component_names_and_preserves_framework_availability():
    source = {
        "version": "8.0.1.test-patch",
        "brandings": "TP_ALL,QTC_E",
        "components": [
            {
                "componentName": "tDemo",
                "family": "Data/Mapping|Processing",
                "paletteType": "DI",
                "brandings": "QTC_E,TP_ALL",
            },
            {
                "componentName": "tDemo",
                "family": "Technical",
                "paletteType": "DI",
                "brandings": "TP_ALL",
            },
            {
                "componentName": "tDemo",
                "family": "Big Data/Storage",
                "paletteType": "SPARK",
                "brandings": "TP_ALL",
            },
            {
                "componentName": "cDemo",
                "family": "Messaging/AMQP",
                "paletteType": "CAMEL",
                "brandings": "QTC_E",
            },
        ],
    }

    manifest = normalize_inventory(source, "2026-10-20")
    components = {item["name"]: item for item in manifest["components"]}

    assert manifest["availability_snapshot_version"] == "8.0.1.test-patch"
    assert manifest["license_branding_labels"]["QTC_E"] == "Qlik Talend Cloud Enterprise Edition"
    assert manifest["counts"] == {
        "source_records": 4,
        "components": 2,
        "component_framework_pairs": 3,
        "components_by_framework": {"CAMEL": 1, "DI": 1, "SPARK": 1},
    }
    assert len(components["tDemo"]["availability"]) == 3
    assert components["tDemo"]["availability"][0]["framework_code"] == "DI"
    assert components["tDemo"]["availability"][0]["license_branding_codes"] == [
        "QTC_E",
        "TP_ALL",
    ]
    assert components["tDemo"]["availability"][0]["family"] == "Data/Mapping|Processing"
    assert components["tDemo"]["availability"][0]["documentation_route"] == "Jobs"
    assert "documentation_page_status" not in components["tDemo"]["availability"][0]
    assert components["cDemo"]["availability"][0]["framework_code"] == "CAMEL"
    assert components["cDemo"]["availability"][0]["documentation_route"] == "Routes"


def test_normalize_rejects_unrecognized_official_framework():
    source = {
        "version": "8.0.1.test-patch",
        "brandings": "TP_ALL",
        "components": [
            {
                "componentName": "tDemo",
                "family": "Processing",
                "paletteType": "NEW_PALETTE",
                "brandings": "TP_ALL",
            }
        ],
    }

    with pytest.raises(ValueError, match="Unknown Qlik palette type"):
        normalize_inventory(source, "2026-10-20")
