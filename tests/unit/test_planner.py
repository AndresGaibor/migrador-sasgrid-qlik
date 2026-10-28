import json
import re
from pathlib import Path

from apps.api.main import app as api
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.intermediate_representation.models import IROperation, MacroIR, ProgramIR
from sas_grid_migrator.migration_planner.expressions import translate
from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.migration_planner.service import (
    generate_plans,
    get_plan,
    load_plans,
    set_decision,
)
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.reporting.exports import render_plan_md, steps_csv, write_exports
from sas_grid_migrator.sas_parser.ast import Loc, ProcStep
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


def test_compute_plan_keeps_each_assignment_target_for_tmap_configuration():
    ir = ProgramIR(
        file="daily.sas",
        operations=[
            IROperation(
                id="op_5_compute_1",
                type="compute",
                step="s5",
                evidence=Loc(file="daily.sas", line=5, end_line=5),
                inputs=["work.transactions"],
                outputs=["work.enriched"],
                details={"assignments": [{"target": "service_fee", "expression": "amount * 0.005", "line": 5}]},
            )
        ],
    )

    plan = plan_program(ir, "project-1", load_mapping_rules(), {})

    assert plan.steps[0].expressions[0].target == "service_fee"


def test_ir_clientes_activos():
    ops = ir_of("p0_clientes_activos.sas").operations
    types = [o.type for o in ops]
    assert "read" in types and "write" in types and "sort" in types
    assert len({o.id for o in ops}) == len(ops)
    assert all(o.evidence.line > 0 for o in ops)


def test_data_set_union_connects_every_input_to_tunite():
    parsed = parse_program("data result; set left right; run;", "union.sas")
    plan = plan_program(build_ir(parsed), "project-1", load_mapping_rules(), {})

    source_steps = [step for step in plan.steps if step.operation_type == "read"]
    union_step = next(step for step in plan.steps if step.operation_type == "union")

    assert [connection.from_step for connection in union_step.connections] == [
        step.id for step in source_steps
    ]


def test_proc_append_configures_target_table_not_source_table():
    parsed = parse_program(
        "proc append base=lib.target data=lib.source force; run;", "append.sas"
    )
    plan = plan_program(build_ir(parsed), "project-1", load_mapping_rules(), {})
    append_step = next(step for step in plan.steps if step.operation_type == "append")

    assert next(prop.value for prop in append_step.properties if prop.name == "TABLE") == "target"


def test_sql_intersect_and_except_remain_manual_instead_of_becoming_union():
    for operator in ("INTERSECT", "EXCEPT"):
        source = (
            "proc sql; create table result as select id from left_table "
            f"{operator} select id from right_table; quit;"
        )
        parsed = parse_program(source, "set-operation.sas")
        plan = plan_program(build_ir(parsed), "project-1", load_mapping_rules(), {})

        assert not any(step.operation_type == "union" for step in plan.steps)
        manual_step = next(
            step for step in plan.steps if step.operation_type == "unsupported"
        )
        assert manual_step.action == "manual_decision"
        assert any(operator in note for note in manual_step.assumptions)


def test_sql_union_variants_keep_their_tunite_candidate():
    for operator in ("UNION", "UNION ALL"):
        source = (
            "proc sql; create table result as select id from left_table "
            f"{operator} select id from right_table; quit;"
        )
        parsed = parse_program(source, "union.sas")
        plan = plan_program(build_ir(parsed), "project-1", load_mapping_rules(), {})

        assert any(step.operation_type == "union" for step in plan.steps)


def test_chained_sql_joins_stay_manual_until_topology_is_modeled():
    source = (
        "proc sql; create table result as select a.id from left_table as a "
        "left join middle_table as b on a.id=b.id "
        "inner join last_table as c on b.id=c.id; quit;"
    )
    parsed = parse_program(source, "chained-joins.sas")
    plan = plan_program(build_ir(parsed), "project-1", load_mapping_rules(), {})

    assert not any(step.operation_type == "join" for step in plan.steps)
    manual_step = next(step for step in plan.steps if step.operation_type == "unsupported")
    assert manual_step.action == "manual_decision"
    assert any("JOIN" in note and "encadenad" in note for note in manual_step.assumptions)


def test_conditional_multi_output_data_step_stays_manual_until_routing_is_modeled():
    source = (
        "data active inactive; set source; "
        "if status = 'A' then output active; else output inactive; run;"
    )
    parsed = parse_program(source, "conditional-outputs.sas")
    plan = plan_program(build_ir(parsed), "project-1", load_mapping_rules(), {})

    assert not any(step.operation_type == "write" for step in plan.steps)
    manual_step = next(step for step in plan.steps if step.operation_type == "unsupported")
    assert manual_step.action == "manual_decision"
    assert any("OUTPUT" in note and "condicional" in note for note in manual_step.assumptions)


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


def test_plan_flattens_invoked_entry_macro_and_keeps_its_parameters_in_context():
    include = IROperation(
        id="op_2_include_1",
        type="include",
        step="s2",
        evidence={"file": "daily.sas", "line": 2, "end_line": 2},
        details={"path": "/sas/config/autoexec.sas"},
    )
    entry_call = IROperation(
        id="op_20_macro_call_1",
        type="macro_call",
        step="s20",
        evidence={"file": "daily.sas", "line": 20, "end_line": 20},
        details={"name": "daily", "args": "run_date=&CURR_DT"},
    )
    body_filter = IROperation(
        id="op_8_filter_1",
        type="filter",
        step="s8",
        evidence={"file": "daily.sas", "line": 8, "end_line": 8},
        inputs=["work.claims"],
        details={"expression": "amount > 0", "origin": "sentencia WHERE"},
    )
    helper_call = IROperation(
        id="op_12_macro_call_1",
        type="macro_call",
        step="s12",
        evidence={"file": "daily.sas", "line": 12, "end_line": 12},
        details={"name": "sendmail", "args": ""},
    )
    helper_body = IROperation(
        id="op_30_report_1",
        type="report",
        step="s30",
        evidence={"file": "daily.sas", "line": 30, "end_line": 30},
        details={"proc": "print"},
    )
    ir = ProgramIR(
        file="daily.sas",
        operations=[include, entry_call],
        macros=[
            MacroIR(name="daily", params=["run_date", "restart_from"], loc=Loc(file="daily.sas", line=3, end_line=19), operations=[body_filter, helper_call]),
            MacroIR(name="sendmail", params=[], loc=Loc(file="daily.sas", line=25, end_line=31), operations=[helper_body]),
        ],
        parameters={"CURR_DT": ""},
    )

    result = plan_program(ir, "project-1", load_mapping_rules(), {})

    assert [step.operation_id for step in result.steps] == ["op_8_filter_1", "op_12_macro_call_1"]
    assert all(step.operation_type not in {"include", "macro_call"} or step.operation_id == "op_12_macro_call_1" for step in result.steps)
    assert result.entry_macro is not None
    assert result.entry_macro.name == "daily"
    assert result.entry_macro.params == ["run_date", "restart_from"]
    assert result.entry_macro.arguments == {"run_date": "&CURR_DT"}
    assert [macro.name for macro in result.children] == ["sendmail"]
    assert {item.name for item in result.context_variables} >= {"run_date", "restart_from", "CURR_DT"}


def test_grid_recommendations_use_versioned_catalog_and_keep_unsupported_evidence(tmp_path):
    store, pid = project(tmp_path)
    ps = generate_plans(store, pid)
    assert ps.grid_recommendations
    all_patterns = {r.pattern_id: r for r in ps.grid_recommendations}
    # Mantén las aserciones de línea ligadas al fixture que define estos casos.
    # Otros proyectos sintéticos pueden incluir los mismos patrones con evidencia distinta.
    coverage_recommendations = [
        r for r in ps.grid_recommendations if r.evidence.file == "grid/coverage_variants.sh"
    ]
    patterns = {r.pattern_id: r for r in coverage_recommendations}
    catalog = json.loads((ROOT / "rules/sas/grid_catalog.json").read_text(encoding="utf-8"))
    assert {entry["id"] for entry in catalog["patterns"]} <= all_patterns.keys()
    assert all(r.reason and r.evidence.file and r.evidence.line > 0 for r in ps.grid_recommendations)
    assert {"sasgsub.submit", "sasgsub.job_options"} <= patterns.keys()
    assert "sasgsub.set_parameters" in all_patterns
    submit = patterns["sasgsub.submit"]
    assert submit.status == "partial" and submit.component_candidate == "tRunJob"
    assert submit.catalog_version == "1" and submit.doc_url and submit.evidence.line == 7
    assert submit.required and submit.reason and submit.instruction

    unknown = next(
        r for r in ps.grid_recommendations if r.pattern_id == "sasgsub.unverified_options"
    )
    assert unknown.status == "unsupported" and unknown.evidence.line == 4
    assert unknown.details["unknown_options"] == ["-grid", "-queue", "-name", "-wait"]
    lsf = [r for r in coverage_recommendations if r.pattern_id == "scheduler.lsf"]
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
    plan.steps[0].status = "descartado"
    plan.steps[0].note = "No usar este estado manual"
    md = render_plan_md(plan)
    assert "## Pasos" in md and "p0_resumen_sql.sas:" in md and "Checklist" in md
    assert "descartado" not in md and "No usar este estado manual" not in md
    rows = steps_csv(ps).splitlines()
    assert rows[0].startswith("job,programa,paso_id") and len(rows) > 10
    assert "estado" not in rows[0] and "descartado" not in "\n".join(rows)
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
    exported_plan = json.loads((tmp_path / "out/p0_resumen_sql.json").read_text())
    assert "job_status" not in exported_plan
    assert "status" not in exported_plan["steps"][0] and "note" not in exported_plan["steps"][0]
    assert JobPlan.model_validate(json.loads((tmp_path / "out/p0_resumen_sql.json").read_text()))


def test_plan_schema_in_sync():
    path = ROOT / "schemas" / "migration-plan.schema.json"
    assert json.loads(path.read_text(encoding="utf-8")) == JobPlan.model_json_schema()


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


def test_long_proc_format_statement_reaches_format_row_parser():
    from sas_grid_migrator.migration_planner.planner import _format_rows

    entries = [f"'{i:03}' = 'Label {i:03}'" for i in range(50)]
    source = "proc format;\nvalue $LONG\n" + "\n".join(entries) + ";\nrun;"
    proc = next(
        n for n in parse_program(source, "long-format.sas").nodes if isinstance(n, ProcStep)
    )
    statement = next(s.text for s in proc.statements if s.kw == "value")
    rows = _format_rows([statement])

    assert len(statement) > 600
    assert len(rows) == 50
    assert rows[0] == ("LONG", "000", "Label 000")
    assert rows[-1] == ("LONG", "049", "Label 049")


def test_banking_format_uses_documented_inline_table_mapping_with_all_rows(tmp_path):
    store, pid = project(tmp_path)
    plans = generate_plans(store, pid)
    plan = next(
        p
        for p in plans.plans
        if p.program == "real/ts-sas-legacy-analytics/Formats/banking_formats.sas"
    )
    step = next(s for s in plan.steps if s.operation_type == "format_definition")
    properties = {p.name: p for p in step.properties}

    assert properties["USE_INTABLE"].value == "true"
    assert properties["USE_INTABLE"].label == "Use Inline Table"
    assert properties["INTABLE"].label == "Inline Table"
    table = properties["INTABLE"].value
    assert table is not None
    rows = table.splitlines()
    assert len(rows) == 79
    assert all(len(row.split(" | ")) == 3 for row in rows)
    assert "BALRANGE | LOW-<0 | Negative" in rows
    assert "ACCTTYPE | OTHER | Unknown" in rows
    assert [c.name for c in step.schema_columns] == ["FORMAT", "CODE", "LABEL"]
    assert all(c.talend_type == "String" for c in step.schema_columns)
    assert any("rangos y OTHER" in item for item in step.pending)
