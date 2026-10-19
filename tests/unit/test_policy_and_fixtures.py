import json
from pathlib import Path

import pytest

from sas_grid_migrator.talend_adapter.policy import ToolNotAllowed, assert_allowed

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"
ROOT = Path(__file__).parent.parent.parent


@pytest.mark.parametrize(
    "tool",
    [
        "talend_run_job",
        "talend_delete_job",
        "talend_update_component_parameter",
        "talend_repo_pull",
    ],
)
def test_mutating_tools_denied(tool):
    with pytest.raises(ToolNotAllowed):
        assert_allowed(tool)


def test_read_tool_allowed():
    assert_allowed("talend_list_jobs")


def test_every_fixture_declares_priority():
    files = [
        p for p in FIXTURES.rglob("*") if "real" not in p.parts and p.suffix in {".sas", ".sh"}
    ]
    assert files
    for p in files:
        head = "\n".join(p.read_text().splitlines()[:2])
        assert "priority: P" in head, p


def test_grid_catalog_entries_have_real_fixture_evidence_or_explicit_unsupported_status():
    catalog = json.loads((ROOT / "rules/sas/grid_catalog.json").read_text())
    assert catalog["version"] and catalog["patterns"]
    assert catalog["change_policy"]
    ids = set()
    for entry in catalog["patterns"]:
        assert entry["id"] not in ids
        ids.add(entry["id"])
        assert entry["status"] in {"supported", "partial", "unsupported"}
        assert entry["limitations"]
        if entry["status"] == "unsupported":
            assert entry["talend_pattern"] is None
        if entry["fixture"]:
            fixture = entry["fixture"]
            lines = (ROOT / fixture["path"]).read_text().splitlines()
            assert all(1 <= n <= len(lines) for n in fixture["lines"])
        if entry["status"] != "unsupported":
            assert entry["fixture"] and entry["talend_pattern"]
        assert entry["prerequisites"]
    assert not [entry for entry in catalog["patterns"] if entry["status"] == "supported"]
    assert catalog["counts"] == {
        "unit": "catalog entries by status",
        **{status: sum(x["status"] == status for x in catalog["patterns"]) for status in ("supported", "partial", "unsupported")},
    }


def test_grid_mappings_match_catalog_and_use_existing_talend_components():
    from sas_grid_migrator.talend_adapter.catalog import load_catalog

    catalog = json.loads((ROOT / "rules/sas/grid_catalog.json").read_text())
    mappings = json.loads((ROOT / "rules/mappings/talend-components.json").read_text())["grid"]
    talend = load_catalog()
    assert mappings.keys() == {entry["id"] for entry in catalog["patterns"]}
    for key, mapping in mappings.items():
        assert mapping["status"] == next(x["status"] for x in catalog["patterns"] if x["id"] == key)
        if mapping["component"]:
            assert talend.has(mapping["component"]), key
        if mapping.get("connection"):
            assert any(c.get("type") == mapping["connection"] for c in talend.get("tRunJob")["connectors"])
        assert mapping["reason"] and mapping["required"] and mapping["instruction"]
