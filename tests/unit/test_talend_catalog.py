import json
from pathlib import Path

import pytest

from sas_grid_migrator.talend_adapter.catalog import current_profile_names, load_catalog

ROOT = Path(__file__).parent.parent.parent
RULES = json.loads((ROOT / "rules" / "mappings" / "talend-components.json").read_text())
_GUIDES = {
    item["name"]: item
    for item in json.loads(
        (ROOT / "rules" / "talend" / "component-documentation-index.json").read_text()
    )["components"]
}
_INVENTORY = json.loads(
    (ROOT / "rules" / "talend" / "official-component-inventory.json").read_text()
)
_CURRENT_FRAMEWORKS = {"DI", "SPARK", "STRUCTUREDSTREAMING", "CAMEL"}
CURRENT_COMPONENTS = {
    item["name"]
    for item in _INVENTORY["components"]
    if _GUIDES.get(item["name"], {}).get("lifecycle_status") == "current"
    and any(
        record["framework_code"] in _CURRENT_FRAMEWORKS
        and "TP_ALL" in record["license_branding_codes"]
        for record in item["availability"]
    )
}


def test_profile_index_must_match_selected_license():
    with pytest.raises(ValueError, match="Talend Data Fabric profile"):
        current_profile_names(
            {"components": []},
            {"license_profile": {"code": "OTHER_PROFILE"}, "components": []},
        )


def test_catalog_shape_contains_only_current_data_fabric_components():
    cat = load_catalog()
    assert len(CURRENT_COMPONENTS) == 870
    assert len(cat.components) > 500
    assert set(cat.components) <= CURRENT_COMPONENTS
    assert "official_inventory" not in cat.data
    assert "official_audit" not in cat.data
    assert cat.data["count"] == len(cat.components)
    f = cat.get("tFilterRow")
    assert f and "Processing" in f["families"]
    assert {"LOGICAL_OP", "CONDITIONS"} <= set(cat.params("tFilterRow"))
    assert cat.params("tFilterRow")["LOGICAL_OP"]["items"][0]["name"] in ("OR", "AND")
    assert any(c["type"] == "FLOW" and c.get("name") == "REJECT" for c in f["connectors"])
    oracle = cat.get("tOracleInput")
    assert oracle is not None
    assert oracle["imports"], "drivers requeridos"


def test_variants_group_by_technology():
    cat = load_catalog()
    sib = cat.variants_of("tOracleInput")
    assert "tMysqlInput" in sib and "tOracleOutput" not in sib
    assert cat.variants_of("tNoExiste") == []


def test_every_component_is_listable_and_has_lists():
    cat = load_catalog()
    assert len(cat.search("")) == len(cat.components)
    for n, c in cat.components.items():
        assert all(k in c for k in ("parameters", "connectors", "imports", "families")), n


def test_search():
    cat = load_catalog()
    assert any(r["name"] == "tFilterRow" for r in cat.search("filterrow"))
    assert all("Processing" in r["families"] for r in cat.search("", family="Processing"))


def test_plan_doc_urls_prefer_standard_properties_for_standard_components():
    cat = load_catalog()
    tmap = cat.get("tMap")
    fixed_flow = cat.get("tFixedFlowInput")
    assert tmap is not None and tmap["doc_url"].endswith("/tmap/tmap-standard-properties")
    assert fixed_flow is not None and fixed_flow["doc_url"].endswith(
        "/tfixedflowinput/tfixedflowinput-standard-properties"
    )


def test_mapping_rules_use_current_studio_components():
    """Las reglas solo nombran componentes vigentes; los campos se cotejan cuando hay metadatos."""
    cat = load_catalog()
    generic = set(RULES["generic_components"])
    scope = json.loads((ROOT / "rules" / "talend" / "migration-candidate-scope.json").read_text())
    archive = json.loads(
        (ROOT / "rules" / "archive" / "talend" / "studio8-default-install-exclusions.json").read_text()
    )
    archived = {item["name"] for item in archive["components"]}
    candidates = set(scope["core"]) | set(scope["alternatives"]) | generic
    candidates |= {name for roles in RULES["engines"].values() for name in roles.values()}
    candidates |= {
        name
        for rule in RULES["operations"].values()
        for name in [rule["component"], *rule.get("alternatives", [])]
        if name.startswith("t")
    }
    editor = RULES["editor_properties"]
    bad = [
        f"archived component used as migration candidate: {name}"
        for name in sorted(candidates & archived)
    ]
    bad += [f"archived component reached the runtime catalog: {name}" for name in sorted(archived) if cat.has(name)]
    for op, r in RULES["operations"].items():
        for comp in [r["component"], *r.get("alternatives", [])]:
            base = comp.split(" ")[0]
            if base.startswith("t") and base not in generic and base not in CURRENT_COMPONENTS:
                bad.append(f"{op}: componente fuera de Studio 8: {comp}")
        base = r["component"].split(" ")[0]
        if cat.has(base):
            known = set(cat.params(base)) | set(editor.get(base, []))
            bad += [f"{op}: {base}.{p}" for p in r.get("properties", []) if p not in known]
    ops = RULES["operations"]
    want = {
        "input": ops["read"]["properties"],
        "output": sorted({*ops["write"]["properties"], *ops["append"]["properties"]}),
    }
    for eng, roles in RULES["engines"].items():
        for role, comp in roles.items():
            if cat.has(comp):
                bad += [
                    f"engine {eng}: {comp}.{p}" for p in want[role] if p not in cat.params(comp)
                ]
    for eng, roles in RULES["engines"].items():
        bad += [
            f"engine {eng}: {c}"
            for c in roles.values()
            if c.startswith("t") and c not in generic and c not in CURRENT_COMPONENTS
        ]
    assert not bad, bad


def test_api_catalog_exposes_only_current_studio_8_components(monkeypatch):
    import apps.api.integrations as integration_mod
    from apps.api.main import app
    from fastapi.testclient import TestClient
    from sas_grid_migrator.talend_adapter.adapter import TalendAdapter

    # El catálogo muestra lo instalado en Studio. Aquí Studio "tiene" todos los componentes oficiales
    # de Studio 8, así que la prueba no depende de qué palettes haya en este equipo.
    official = sorted(current_profile_names(_INVENTORY, {"license_profile": {"code": "TP_ALL"}, "components": list(_GUIDES.values())}))

    class FullStudioAdapter:
        async def installed_component_names(self):
            return official

    monkeypatch.setattr(TalendAdapter, "from_env", classmethod(lambda cls: FullStudioAdapter()))
    monkeypatch.setattr(integration_mod, "_STUDIO_COMPONENT_NAMES", None)
    c = TestClient(app)
    official_list = c.get("/api/talend/catalog", params={"q": "filterrow"}).json()
    filter_row = next(x for x in official_list["components"] if x["name"] == "tFilterRow")
    assert official_list["count"] == 870
    assert official_list["official_component_names"] == sorted(
        official_list["official_component_names"], key=str.casefold
    )
    assert len(official_list["official_component_names"]) == 870
    assert filter_row["documentation_status"] == "documented"
    assert filter_row["license_profile"] == {"code": "TP_ALL", "label": "Talend Data Fabric"}
    assert "catalog_entry_present" not in filter_row
    assert official_list["result_count"] == len(official_list["components"])
    assert official_list["has_more"] is False
    assert "official_inventory" not in official_list
    coverage = official_list["official_documentation_inventory"]
    assert coverage["license_profile"] == {"code": "TP_ALL", "label": "Talend Data Fabric"}
    assert coverage["count"] == 870
    assert coverage["documented"] + coverage["exception"] == 870
    family_list = c.get(
        "/api/talend/catalog",
        params={"q": "filterrow", "family": "Processing"},
    ).json()
    assert "tFilterRow" in {item["name"] for item in family_list["components"]}

    current_names = set(official_list["official_component_names"])
    assert current_names == CURRENT_COMPONENTS
    assert c.get("/api/talend/catalog/not-a-current-component").status_code == 404

    exclusions = json.loads(
        (ROOT / "rules" / "archive" / "talend" / "studio8-default-install-exclusions.json").read_text()
    )
    archived_name = exclusions["components"][0]["name"]
    assert archived_name not in current_names
    assert c.get(f"/api/talend/catalog/{archived_name}").status_code == 404

    filter_row_detail = c.get("/api/talend/catalog/tFilterRow").json()
    assert filter_row_detail["parameters"] == [] and filter_row_detail["doc_markdown"] is None
    assert filter_row_detail["official_availability"]["license_profile"] == {
        "code": "TP_ALL",
        "label": "Talend Data Fabric",
    }
    assert all(
        "TP_ALL" in record["license_branding_codes"]
        for record in filter_row_detail["official_availability"]["records"]
    )

    local_names = json.loads((ROOT / "rules" / "talend" / "components.json").read_text())[
        "components"
    ]
    assert "cConvertBodyTo" not in local_names
    unlisted_search = c.get("/api/talend/catalog", params={"q": "cConvertBodyTo"}).json()
    assert [item["name"] for item in unlisted_search["components"]] == ["cConvertBodyTo"]
    unlisted_response = c.get("/api/talend/catalog/cConvertBodyTo")
    assert unlisted_response.status_code == 200
    unlisted = unlisted_response.json()
    assert unlisted["official_documentation"]["status"] == "documented"
    assert any(
        page["title"] == "Configuring the components"
        for page in unlisted["official_documentation"]["configuration_pages"]
    )

    one = c.get("/api/talend/catalog/tFilterRow").json()
    assert one["name"] == "tFilterRow"
    assert one["parameters"] == [] and one["variants"] == []
    assert one["doc_markdown"] is None
    assert one["official_documentation"]["status"] == "documented"
    assert set(one["official_documentation"]["framework_codes"]) <= _CURRENT_FRAMEWORKS
    assert all(
        "deprecated" not in (page.get("title") or "").lower()
        for route in one["official_documentation"]["routes"]
        for page in route["pages"]
    )

    fixed_flow = c.get("/api/talend/catalog/tFixedFlowInput").json()["official_documentation"]
    assert set(fixed_flow["framework_codes"]) <= _CURRENT_FRAMEWORKS
    assert all(
        "deprecated" not in section["heading"].lower()
        for section in fixed_flow["configuration_sections"]
    )

    global_config = c.get("/api/talend/studio-configuration").json()
    assert global_config["target"] == "Talend Studio 8.0 R2026-09"
    assert "Setting Talend Studio preferences" in global_config["markdown"]
    assert c.get("/api/talend/catalog/..%2F..%2Fetc%2Fpasswd").status_code == 404
    assert c.get("/api/talend/catalog/tNoExiste").status_code == 404


def test_archived_catalog_is_separate_and_never_runtime_verified():
    from apps.api.main import app
    from fastapi.testclient import TestClient

    archive = json.loads(
        (ROOT / "rules" / "archive" / "talend" / "studio8-default-install-exclusions.json").read_text()
    )
    client = TestClient(app)
    response = client.get("/api/talend/catalog/archived")
    assert response.status_code == 200
    listing = response.json()
    names = [item["name"] for item in listing["components"]]
    assert listing["target"] == "Talend Studio 8.0 R2026-09"
    assert listing["count"] == len(archive["components"]) == 277
    assert names == sorted(names, key=str.casefold)
    assert set(names).isdisjoint(CURRENT_COMPONENTS)
    assert {
        status: sum(item["status"] == status for item in listing["components"])
        for status in archive["counts"]
    } == archive["counts"]

    optional = next(item for item in archive["components"] if item["status"] == "optional_install")
    optional_name = optional["name"]
    search = client.get("/api/talend/catalog/archived", params={"q": optional_name.casefold()}).json()
    assert [item["name"] for item in search["components"]] == [optional_name]
    detail = client.get(f"/api/talend/catalog/archived/{optional_name}").json()
    assert detail["status"] == "optional_install"
    assert detail["runtime_verified"] is False
    assert detail["source_url"] == optional["source_url"]
    assert client.get("/api/talend/catalog", params={"q": optional_name}).json()["components"] == []
    assert client.get(f"/api/talend/catalog/{optional_name}").status_code == 404

    removed = next(
        item for item in archive["components"] if item["status"] == "removed_from_target_release"
    )
    removed_detail = client.get(f"/api/talend/catalog/archived/{removed['name']}").json()
    assert removed_detail["status"] == "removed_from_target_release"
    assert removed_detail["source_url"] is None
    assert removed_detail["runtime_verified"] is False
    assert client.get("/api/talend/catalog/archived/not-archived").status_code == 404


def test_variants_only_for_technology_families():
    cat = load_catalog()
    assert cat.variants_of("tFilterRow") == []  # Processing: «Row» no es un rol de base de datos
    assert cat.variants_of("tSortRow") == []
    assert "tMysqlRow" in cat.variants_of("tOracleRow")


def test_planner_values_for_closed_lists_are_valid(tmp_path):
    """Todo valor que el planificador fija en una lista cerrada es una opción real del catálogo."""
    from pathlib import Path

    from sas_grid_migrator.config import Settings
    from sas_grid_migrator.migration_planner.service import generate_plans
    from sas_grid_migrator.persistence.store import Store

    st = Store(Settings(data_dir=tmp_path / "d"))
    p = st.create_project("c")
    st.import_batch(p.id, Path(__file__).parent.parent / "fixtures" / "sas")
    cat = load_catalog()
    bad = []
    for plan in generate_plans(st, p.id).plans:
        for s in plan.steps + [x for c in plan.children for x in c.steps]:
            known = cat.params(s.component_candidate.split(" ")[0])
            for pr in s.properties:
                spec = known.get(pr.name)
                if spec and spec.get("items") and pr.value:
                    ok = {i["name"] for i in spec["items"]} | {
                        i.get("value") for i in spec["items"]
                    }
                    if pr.value not in ok:
                        bad.append((s.component_candidate, pr.name, pr.value))
    assert not bad, bad[:5]
