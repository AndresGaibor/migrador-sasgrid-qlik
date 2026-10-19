from pathlib import Path

import pytest
from apps.api.main import app as api
from fastapi.testclient import TestClient

from sas_grid_migrator.grid_analysis.analyzer import shell_tasks
from sas_grid_migrator.sas_parser.ast import DataStep, GlobalStmt, MacroDef, ProcStep
from sas_grid_migrator.sas_parser.lexer import split_statements
from sas_grid_migrator.sas_parser.parser import parse_program
from sas_grid_migrator.semantic_analysis.classify import classify, load_rules

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"


def parse(name: str):
    p = FIXTURES / name
    return parse_program(p.read_text(), name)


def test_lexer_lines_comments_strings_and_datalines():
    src = "/* c; */\n* nota;\ndata a;\n  x = 'a;b'; /* ;; */\n  datalines;\n1 2\n;\nrun;\n"
    got = [(s.text, s.line) for s in split_statements(src)]
    assert got[0] == ("data a", 3)
    assert got[1] == ("x = 'a;b'", 4)
    assert got[2][0] == "datalines"
    assert got[3][0] == "<datalines>"
    assert got[-1][0] == "run"


def test_lexer_macro_call_without_semicolon_and_str():
    stmts = [s.text for s in split_statements("%m(a)\nrun;\n%put %str(a;b);\n")]
    assert stmts == ["%m(a)", "run", "%put %str(a;b)"]


def test_data_step_p0():
    prog = parse("p0_clientes_activos.sas")
    ds = next(n for n in prog.nodes if isinstance(n, DataStep))
    assert [o.raw for o in ds.outputs] == ["stg.clientes_activos"]
    assert ds.outputs[0].options == "keep=cliente_id nombre saldo segmento"
    assert [(i.lib, i.name) for i in ds.inputs] == [("dwh", "clientes")]
    assert ds.where == ["estado = 'A' and saldo > 0"]
    assert ds.n_conditionals == 3 and ds.drop == ["estado"]
    libs = [
        n.fields["name"] for n in prog.nodes if isinstance(n, GlobalStmt) and n.kind == "libname"
    ]
    assert libs == ["dwh", "stg"]
    sort = next(n for n in prog.nodes if isinstance(n, ProcStep))
    assert sort.name == "sort" and sort.by == ["cliente_id"]
    assert (
        sort.inputs[0].name == "clientes_activos" and sort.outputs[0].name == "clientes_activos_ord"
    )
    assert ds.loc.line == 5


def test_proc_sql_joins_group_by():
    prog = parse("p0_resumen_sql.sas")
    sql = next(n for n in prog.nodes if isinstance(n, ProcStep))
    q = sql.queries[0]
    assert q.kind == "create_table" and q.target.raw == "work.ventas_resumen"
    assert [(s.raw, s.alias) for s in q.sources] == [
        ("dwh.ventas", "v"),
        ("dwh.clientes", "c"),
        ("dwh.productos", "p"),
    ]
    assert [j.kind for j in q.joins] == ["inner join", "left join"]
    assert q.joins[0].on == "on v.cliente_id = c.id"
    assert q.group_by == "c.region, p.categoria"
    assert q.having == "calculated total_monto > 1000"
    assert {"sql_join", "sql_outer_join", "sql_group_by", "sql_calculated", "sql_aggregate"} <= set(
        q.constructs
    )


def test_macros_include_and_calls():
    inc = parse("inc/macros_comunes.sas")
    defs = [n for n in inc.nodes if isinstance(n, MacroDef)]
    assert [(d.name, [p.name for p in d.params]) for d in defs] == [
        ("limpiar_texto", ["var"]),
        ("cargar", ["tabla", "destino"]),
    ]
    assert defs[1].params[1].default == "work"
    assert any(isinstance(n, DataStep) for n in defs[1].body)
    prog = parse("p0_macro_include.sas")
    inc_stmt = next(n for n in prog.nodes if isinstance(n, GlobalStmt) and n.kind == "include")
    assert "include_static" in inc_stmt.constructs
    assert {c.name for c in prog.macro_calls} == {"include", "cargar", "limpiar_texto"} - {
        "include"
    }
    # la llamada sin ';' no se traga el `run;`
    ds = [n for n in prog.nodes if isinstance(n, DataStep)][-1]
    assert ds.loc.end_line == 10


def test_p1_constructs():
    ds = next(n for n in parse("p1_merge_first_last.sas").nodes if isinstance(n, DataStep))
    assert ds.input_kind == "merge" and ds.by == ["cliente_id"]
    assert [i.in_var for i in ds.inputs] == ["a", "b"]
    assert {"merge", "retain", "array", "first_last", "date_functions", "missing_handling"} <= set(
        ds.constructs
    )
    assert ds.subsetting_if == ["a"]


def test_p2_constructs_and_findings():
    prog = parse("p2_codigo_dinamico.sas")
    classify(prog, load_rules())
    codes = {f.code for f in prog.findings}
    assert {"call_execute", "x_command", "systask", "macro_indirect_reference"} <= codes
    f = next(f for f in prog.findings if f.code == "call_execute")
    assert f.priority == "P2" and f.evidence.line == 4  # línea del CALL, no del DATA


def test_macro_defined_inside_data_step_does_not_close_it():
    prog = parse_program("data a;\n%macro m; x=1; %mend m;\nset b;\nrun;\n", "t.sas")
    ds = [n for n in prog.nodes if isinstance(n, DataStep)]
    assert len(ds) == 1 and ds[0].inputs[0].name == "b"


def test_corpus_smoke_recognizes_almost_everything():
    total = unrec = 0
    for p in FIXTURES.rglob("*.sas"):
        r = parse_program(p.read_text(errors="replace"), str(p))
        total += r.stats.statements
        unrec += r.stats.unrecognized
    assert total > 5000
    assert unrec / total < 0.01


@pytest.mark.parametrize("name", ["real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas"])
def test_legacy_batch_job_parses(name):
    prog = parse(name)
    assert prog.nodes and prog.stats.statements > 10


def test_grid_fixture_parses_supported_invocation_fields_and_evidence():
    path = FIXTURES / "grid" / "ejecutar_lote.sh"
    tasks = shell_tasks("grid/ejecutar_lote.sh", path.read_text(), [])
    assert [(t.kind, t.line) for t in tasks] == [
        ("sasgsub", 5),
        ("sasgsub", 6),
        ("sasgsub", 7),
    ]
    assert (tasks[0].program, tasks[0].job_name, tasks[0].waits) == (
        "/sas/prog/p0_clientes_activos.sas",
        "carga_clientes",
        True,
    )
    assert tasks[0].params["FECHA_PROC"] == "$FECHA_PROC"
    assert tasks[1].queue == "normal" and tasks[1].after == [tasks[0].id]
    assert tasks[2].condition == "previous_success" and tasks[2].after == [tasks[1].id]
    variants = FIXTURES / "grid" / "coverage_variants.sh"
    batch, unverified, bsub, bjobs, incomplete = shell_tasks("grid/coverage_variants.sh", variants.read_text(), [])
    assert batch.kind == "sas_batch" and batch.line == 3
    assert batch.program == "/sas/prog/program with spaces.sas"
    assert batch.params["FECHA_PROC"] == "20241019"
    assert unverified.program == "/sas/prog/p0_clientes_activos.sas"
    assert unverified.queue is None and unverified.job_name is None and not unverified.waits
    assert [t.kind for t in (bsub, bjobs)] == ["unsupported_scheduler", "unsupported_scheduler"]
    assert incomplete.incomplete_options == ["-gridqueue"]


def test_grid_parser_keeps_unknown_or_incomplete_options_unclaimed():
    tasks = shell_tasks(
        "grid/edge.sh",
        'sasgsub -unknown value -gridsubmitpgm "job one.sas" -gridqueue\n'
        'bsub -q normal job.sas\n',
        [],
    )
    assert len(tasks) == 2
    assert tasks[0].program == "job one.sas" and tasks[0].queue is None
    assert tasks[0].unknown_options == ["-unknown"]
    assert tasks[1].kind == "unsupported_scheduler" and tasks[1].match_status == "unsupported"


def test_api_analysis_flow(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    c = TestClient(api)
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    assert c.get(f"/api/projects/{pid}/programs").status_code == 409
    c.post(f"/api/projects/{pid}/imports", json={"path": str(FIXTURES / "inc")})
    c.post(f"/api/projects/{pid}/imports", json={"path": str(FIXTURES)})
    s = c.post(f"/api/projects/{pid}/analyses").json()
    assert s["programs"] >= 8 and s["unrecognized"] < 5
    assert any(e["tag"] == "proc:sql" and e["priority"] == "P0" for e in s["coverage"])
    progs = c.get(f"/api/projects/{pid}/programs").json()
    one = next(p["file"] for p in progs if p["file"].endswith("p0_resumen_sql.sas"))
    assert c.get(f"/api/projects/{pid}/programs/{one}").json()["nodes"]
    assert c.get(f"/api/projects/{pid}/programs/nope.sas").status_code == 404
