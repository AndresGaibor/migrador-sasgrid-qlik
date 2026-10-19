import json
from pathlib import Path

from sas_grid_migrator.talend_adapter.catalog import load_catalog

ROOT = Path(__file__).parent.parent.parent
RULES = json.loads((ROOT / "rules" / "mappings" / "talend-components.json").read_text())


def test_catalog_shape():
    cat = load_catalog()
    inventory = cat.data["official_inventory"]
    assert inventory["release"] == "R2026-01"
    assert len(inventory["components"]) == 693
    assert "tMilvusInput" in inventory["components"]
    assert "tMilvusInput" not in cat.components  # inventory oficial ≠ esquema de parámetros
    assert len(cat.components) > 500
    f = cat.get("tFilterRow")
    assert f and "Processing" in f["families"]
    assert {"LOGICAL_OP", "CONDITIONS"} <= set(cat.params("tFilterRow"))
    assert cat.params("tFilterRow")["LOGICAL_OP"]["items"][0]["name"] in ("OR", "AND")
    assert any(c["type"] == "FLOW" and c.get("name") == "REJECT" for c in f["connectors"])
    assert cat.get("tOracleInput")["imports"], "drivers requeridos"


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


def test_mapping_rules_match_official_catalog():
    """Todo componente y propiedad de las reglas existe en el catálogo (salvo genéricos y editor de tMap)."""
    cat = load_catalog()
    generic = set(RULES["generic_components"])
    editor = RULES["editor_properties"]
    bad = []
    for op, r in RULES["operations"].items():
        for comp in [r["component"], *r.get("alternatives", [])]:
            base = comp.split(" ")[0]
            if base.startswith("t") and base not in generic and not cat.has(base):
                bad.append(f"{op}: componente {comp}")
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
            if c.startswith("t") and c not in generic and not cat.has(c)
        ]
    assert not bad, bad


def test_api_catalog(monkeypatch, tmp_path):
    from apps.api.main import app
    from fastapi.testclient import TestClient

    c = TestClient(app)
    lst = c.get("/api/talend/catalog", params={"q": "oracleinput"}).json()
    assert lst["count"] > 500 and any(x["name"] == "tOracleInput" for x in lst["components"])
    inventory = c.get("/api/talend/catalog", params={"q": "milvus"}).json()["official_inventory"]
    assert inventory["release"] == "R2026-01"
    assert any(x["name"] == "tMilvusInput" for x in inventory["components"])
    one = c.get("/api/talend/catalog/tFilterRow").json()
    assert one["name"] == "tFilterRow" and one["parameters"] and "variants" in one
    assert c.get("/api/talend/catalog/..%2F..%2Fetc%2Fpasswd").status_code == 404
    assert c.get("/api/talend/catalog/tNoExiste").status_code == 404


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
