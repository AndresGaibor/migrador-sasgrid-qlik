import json
import re
from pathlib import Path

from apps.api.main import app as api
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.expressions import translate
from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.migration_planner.service import (
    generate_plans,
    get_plan,
    load_plans,
    set_decision,
)
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.reporting.exports import render_plan_md, steps_csv, write_exports
from sas_grid_migrator.sas_parser.parser import parse_program

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"
ROOT = Path(__file__).parent.parent.parent


def project(tmp_path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    p = store.create_project("t")
    store.import_batch(p.id, FIXTURES)
    return store, p.id


def ir_of(name: str):
    return build_ir(parse_program((FIXTURES / name).read_text(), name), {})


def test_translate_supported_and_unsupported():
    t = translate("estado = 'A' and saldo > 0")
    assert "equals" in t.talend and "&&" in t.talend and t.columns == ["estado", "saldo"]
    assert translate("saldo > &min").talend == "(input_row.saldo > context.min)"
    assert translate("x is missing").talend is None
    assert translate("foo(x) > 1").talend is None


def test_ir_clientes_activos():
    ops = ir_of("p0_clientes_activos.sas").operations
    types = [o.type for o in ops]
    assert "read" in types and "write" in types and "sort" in types
    assert len({o.id for o in ops}) == len(ops)
    assert all(o.evidence.line > 0 for o in ops)


def test_plan_steps_have_contract(tmp_path):
    store, pid = project(tmp_path)
    ps = generate_plans(store, pid)
    plan = next(p for p in ps.plans if p.program == "p0_clientes_activos.sas")
    assert plan.job_status == "needs_review" and plan.steps
    ids = {s.id for s in plan.steps}
    for s in plan.steps:
        assert s.evidence.line > 0 and s.verified is False
        assert s.component_candidate
        assert all(c.from_step in ids for c in s.connections if c.from_step)
    assert any(c.kind == "row_count" for c in plan.validation_cases)
    # ningún componente puede declararse verificado sin talend-mcp
    assert not any(s.verified for p in ps.plans for s in p.steps)


def test_grid_recommendations_use_versioned_catalog_and_keep_unsupported_evidence(tmp_path):
    store, pid = project(tmp_path)
    ps = generate_plans(store, pid)
    assert ps.grid_recommendations
    patterns = {r.pattern_id: r for r in ps.grid_recommendations}
    catalog = json.loads((ROOT / "rules/sas/grid_catalog.json").read_text(encoding="utf-8"))
    assert {entry["id"] for entry in catalog["patterns"]} <= patterns.keys()
    assert all(
        r.reason and r.evidence.file and r.evidence.line > 0 for r in ps.grid_recommendations
    )
    assert {"sasgsub.submit", "sasgsub.job_options", "sasgsub.set_parameters"} <= patterns.keys()
    submit = patterns["sasgsub.submit"]
    assert submit.status == "partial" and submit.component_candidate == "tRunJob"
    assert submit.catalog_version == "1" and submit.doc_url and submit.evidence.line == 7
    assert submit.required and submit.reason and submit.instruction

    unknown = next(
        r for r in ps.grid_recommendations if r.pattern_id == "sasgsub.unverified_options"
    )
    assert unknown.status == "unsupported" and unknown.evidence.line == 4
    assert unknown.details["unknown_options"] == ["-grid", "-queue", "-name", "-wait"]
    lsf = [r for r in ps.grid_recommendations if r.pattern_id == "scheduler.lsf"]
    assert [(r.status, r.evidence.line) for r in lsf] == [("unsupported", 5), ("unsupported", 6)]
    missing = next(
        r for r in ps.grid_recommendations if r.pattern_id == "sasgsub.missing_option_value"
    )
    assert missing.status == "unsupported" and missing.details["incomplete_options"] == [
        "-gridqueue"
    ]
    batch = next(r for r in ps.grid_recommendations if r.pattern_id == "sas_batch.sysin")
    assert batch.evidence.line == 3 and batch.details["program"].endswith("program with spaces.sas")


def test_context_variables_from_let(tmp_path):
    store, pid = project(tmp_path)
    generate_plans(store, pid)
    plan = get_plan(store, pid, "p0_resumen_sql.sas")
    assert any(c.suggested == "context.anio" for c in plan.context_variables)


def test_decisions_survive_regeneration(tmp_path):
    store, pid = project(tmp_path)
    generate_plans(store, pid)
    plan = get_plan(store, pid, "p0_clientes_activos.sas")
    sid = plan.steps[0].id
    assert set_decision(store, pid, plan.program, sid, "verificado", "ok")
    assert not set_decision(store, pid, plan.program, sid, "inventado", None)
    assert not set_decision(store, pid, plan.program, "no_existe", "verificado", None)
    generate_plans(store, pid)
    step = next(s for s in get_plan(store, pid, plan.program).steps if s.id == sid)
    assert (step.status, step.note) == ("verificado", "ok")
    assert load_plans(store, pid) is not None


def test_reimport_clears_plans(tmp_path):
    store, pid = project(tmp_path)
    generate_plans(store, pid)
    store.import_batch(pid, FIXTURES)
    assert load_plans(store, pid) is None


def test_exports(tmp_path):
    store, pid = project(tmp_path)
    ps = generate_plans(store, pid)
    plan = next(p for p in ps.plans if p.program == "p0_resumen_sql.sas")
    md = render_plan_md(plan)
    assert "## Pasos" in md and "p0_resumen_sql.sas:" in md and "Checklist" in md
    rows = steps_csv(ps).splitlines()
    assert rows[0].startswith("job,programa,paso_id") and len(rows) > 10
    out_dir = tmp_path / "out"
    files = write_exports(ps, out_dir)
    names = {f.name for f in files}
    assert {"index.md", "steps.csv", "p0_resumen_sql.md", "p0_resumen_sql.json"} <= names
    index = (tmp_path / "out/index.md").read_text(encoding="utf-8")
    assert "scheduler.lsf" in index and "Documentacion oficial Talend" in index
    exported_md = (out_dir / "p0_resumen_sql.md").read_text(encoding="utf-8")
    icons = re.findall(r"!\[Icono Talend\]\(assets/talend-icons/([^)]+)\)", exported_md)
    assert icons and all((out_dir / "assets" / "talend-icons" / icon).is_file() for icon in icons)
    assert (out_dir / "assets" / "talend-icons" / "LICENSE").is_file()
    assert (out_dir / "assets" / "talend-icons" / "NOTICE.md").is_file()
    assert JobPlan.model_validate(json.loads((tmp_path / "out/p0_resumen_sql.json").read_text()))


def test_plan_schema_in_sync():
    path = ROOT / "schemas" / "migration-plan.schema.json"
    assert json.loads(path.read_text()) == JobPlan.model_json_schema()


def test_api_plans(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    c = TestClient(api)
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    c.post(f"/api/projects/{pid}/imports", json={"path": str(FIXTURES)})
    assert c.get(f"/api/projects/{pid}/plans").status_code == 409
    assert c.post(f"/api/projects/{pid}/plans").status_code == 201
    grid = c.get(f"/api/projects/{pid}/plans/grid-recommendations")
    assert grid.status_code == 200 and any(x["pattern_id"] == "sasgsub.submit" for x in grid.json())
    rows = c.get(f"/api/projects/{pid}/plans").json()
    assert any(r["program"] == "p0_clientes_activos.sas" for r in rows)
    plan = c.get(f"/api/projects/{pid}/plans/p0_clientes_activos.sas").json()
    sid = plan["steps"][0]["id"]
    r = c.patch(
        f"/api/projects/{pid}/plans/p0_clientes_activos.sas/steps/{sid}",
        json={"status": "descartado", "note": "n"},
    )
    assert r.status_code == 200 and r.json()["steps"][0]["status"] == "descartado"
    bad = c.patch(
        f"/api/projects/{pid}/plans/p0_clientes_activos.sas/steps/{sid}", json={"status": "x"}
    )
    assert bad.status_code == 422
    md = c.get(f"/api/projects/{pid}/plans/p0_clientes_activos.sas?format=md")
    assert md.status_code == 200 and md.text.startswith("# Job")
    assert c.get(f"/api/projects/{pid}/plans/nada.sas").status_code == 404
    e = c.post(f"/api/projects/{pid}/exports")
    assert e.status_code == 201 and "steps.csv" in e.json()["files"]


def test_format_rows_extracts_value_tables():
    from sas_grid_migrator.migration_planner.planner import _format_rows

    rows = _format_rows(
        [
            "value $ACCTTYPE\n    'CHK'  = 'Checking'\n    OTHER  = 'Unknown'\n  ",
            "value RISK\n 1 = 'Low'",
        ]
    )
    assert rows == [
        ("ACCTTYPE", "CHK", "Checking"),
        ("ACCTTYPE", "OTHER", "Unknown"),
        ("RISK", "1", "Low"),
    ]
