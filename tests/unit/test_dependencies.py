from pathlib import Path

from apps.api.main import app as api
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import build_dependencies
from sas_grid_migrator.grid_analysis.analyzer import shell_tasks
from sas_grid_migrator.macro_resolver.resolver import resolve_path, substitute
from sas_grid_migrator.persistence.store import Store

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"


def project(tmp_path, src: Path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    p = store.create_project("t")
    store.import_batch(p.id, src)
    return store, p.id


def test_resolve_path_rules():
    files = ["Programs/Banking/load.sas", "Config/autoexec.sas", "a/x.sas", "b/x.sas"]
    assert (
        resolve_path("/opt/custom/programs/banking/load.sas", files).file
        == "Programs/Banking/load.sas"
    )
    assert resolve_path("/opt/sas/SASApp/autoexec.sas", files).status == "candidate"
    assert resolve_path("x.sas", files).status == "ambiguous"
    assert resolve_path("/opt/nada/otro.sas", files).status == "external"


def test_substitute_only_known_constants():
    assert substitute("&root./data", {"root": "/d"}) == ("/d/data", True)
    assert substitute("&lib..t", {}) == ("&lib..t", False)
    assert substitute("a&&b", {"b": "1"})[1] is False


def test_shell_grid_script():
    text = (FIXTURES / "grid" / "ejecutar_lote.sh").read_text()
    files = ["p0_clientes_activos.sas", "sas/prog/p0_resumen_sql.sas"]
    t1, t2, t3 = shell_tasks("grid/ejecutar_lote.sh", text, files)
    assert (t1.kind, t1.job_name, t1.waits) == ("sasgsub", "carga_clientes", True)
    assert t1.program == "/sas/prog/p0_clientes_activos.sas"
    assert t1.params["FECHA_PROC"] and t1.after == []
    assert t2.queue == "normal" and t2.after == [t1.id]
    assert t3.condition == "previous_success" and t3.after == [t2.id]
    assert t3.line == 7


def test_processing_order_includes_before_includer(tmp_path):
    store, pid = project(tmp_path, FIXTURES / "inc")
    store.import_batch(pid, FIXTURES)  # rutas relativas: inc/... y p0_macro_include.sas
    r = build_dependencies(store, pid)
    inc = next(p for p in r.programs if p.file == "p0_macro_include.sas")
    assert inc.includes[0].status == "resolved" and inc.includes[0].file == "inc/macros_comunes.sas"
    flat = [f for layer in r.processing_order for f in layer]
    assert flat.index("inc/macros_comunes.sas") < flat.index("p0_macro_include.sas")
    # la llamada a %cargar y %limpiar_texto se resuelve contra las macros del proyecto
    assert not [
        u for u in r.unresolved if u.kind == "macro" and u.name in {"cargar", "limpiar_texto"}
    ]
    # el dataset dwh.&tabla. dentro de la macro es dinámico y se informa, no se inventa
    assert any(u.kind == "dataset_dynamic" for u in r.unresolved)


def test_data_edges_and_cycles(tmp_path):
    src = tmp_path / "b"
    src.mkdir()
    (src / "a.sas").write_text("data out.x; set raw.src; run;\n")
    (src / "b.sas").write_text("data out.y; set out.x; run;\n")
    (src / "c.sas").write_text("data out.z; set out.y; run;\n")
    store, pid = project(tmp_path, src)
    r = build_dependencies(store, pid)
    assert r.processing_order == [["a.sas"], ["b.sas"], ["c.sas"]] and not r.cycles
    roles = {d.id: d.role for d in r.datasets}
    assert roles == {
        "raw.src": "source",
        "out.x": "intermediate",
        "out.y": "intermediate",
        "out.z": "final",
    }
    (src / "a.sas").write_text("data out.x; set raw.src out.y; run;\n")
    store.import_batch(pid, src)
    r = build_dependencies(store, pid)
    assert r.cycles == [["a.sas", "b.sas"]]


def test_work_datasets_do_not_link_programs(tmp_path):
    src = tmp_path / "w"
    src.mkdir()
    (src / "a.sas").write_text("data t; set raw.s; run;\n")
    (src / "b.sas").write_text("data o.r; set t; run;\n")
    store, pid = project(tmp_path, src)
    r = build_dependencies(store, pid)
    assert not r.edges and [d.role for d in r.datasets if d.id == "work.t"] == ["temporary"]


def test_orchestrator_macro_and_schedule_on_real_batch(tmp_path):
    store, pid = project(tmp_path, FIXTURES / "real" / "ts-sas-legacy-analytics")
    r = build_dependencies(store, pid)
    banking = [t for t in r.orchestration.tasks if t.source_file.endswith("run_daily_banking.sas")]
    assert [t.params["step_num"] for t in banking] == ["1", "2", "3", "4"]
    assert all(t.resolved_program for t in banking)
    assert banking[1].after == [banking[0].id]
    assert banking[0].resolved_program.endswith("Programs/Banking/load_customer_accounts.sas")
    assert any("Control-M" in s.text for s in r.orchestration.schedules)
    assert any(lib.name == "STAGING" and lib.path == "/data/sas/staging" for lib in r.libraries)


def test_api_dependencies(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    c = TestClient(api)
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    c.post(f"/api/projects/{pid}/imports", json={"path": str(FIXTURES)})
    d = c.get(f"/api/projects/{pid}/dependencies").json()
    assert d["processing_order"] and d["orchestration"]["tasks"]
    assert any(t["kind"] == "sasgsub" for t in d["orchestration"]["tasks"])
    assert c.get("/api/projects/nope/dependencies").status_code == 404
