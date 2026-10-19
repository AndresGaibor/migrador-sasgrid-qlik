import json

import tools.build_talend_catalog as builder


def test_build_preserves_official_inventory(tmp_path, monkeypatch):
    source = tmp_path / "components"
    source.mkdir()
    inventory = {"release": "R2026-01", "count": 693, "components": []}
    existing_catalog = tmp_path / "components.json"
    existing_catalog.write_text(json.dumps({"official_inventory": inventory}))
    monkeypatch.setattr(builder, "OFFICIAL_INVENTORY_FILE", existing_catalog)

    catalog = builder.build(source, audit_file=tmp_path / "missing-audit.json")

    assert catalog["official_inventory"] == inventory
