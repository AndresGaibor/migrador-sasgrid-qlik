from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.domain.redaction import redact, redact_other, redact_sas
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.reporting.exports import write_exports

SRC = """libname ora oracle user=scott password="Tiger123" path=PRODDB;
libname d2 db2 user=u pw=Sekret9 database=S;
%let dbpass = TopSecret77;
%let anio = 2025;
proc sql;
  connect to oracle (user=scott password='Tiger123' path=PRODDB);
quit;
data work.y; set ora.t; if pw = 5 then x = 1; run;
"""


def test_redact_sas_masks_credentials_only():
    out = redact_sas(SRC)
    for secret in ("Tiger123", "Sekret9", "TopSecret77"):
        assert secret not in out
    assert "user=scott" in out and "path=PRODDB" in out and "%let anio = 2025" in out
    assert "if pw = 5" in out  # lógica de datos intacta
    assert out.count("\n") == SRC.count("\n")


def test_redact_shell_and_dispatch():
    sh = 'export DB_PASSWORD="abc"\nsasgsub -password xyz -sysin a.sas\nAPI_TOKEN=t0k\n'
    out = redact_other(sh)
    assert "abc" not in out and "xyz" not in out and "t0k" not in out
    assert redact("x.sh", "x.sh") == "x.sh" and "***" in redact("libname a db2 pw=a;", "k.sas")


def test_no_secret_in_any_derived_output(tmp_path):
    src = tmp_path / "in"
    src.mkdir()
    (src / "s.sas").write_text(SRC)
    (src / "run.sh").write_text("export DB_PASSWORD=Hunter2\nsasgsub -sysin s.sas\n")
    data = tmp_path / "data"
    st = Store(Settings(data_dir=data))
    p = st.create_project("s")
    st.import_batch(p.id, src)
    write_exports(generate_plans(st, p.id), data / "out")
    blob = "".join(
        f.read_text(errors="ignore")
        for f in Path(data).rglob("*")
        if f.is_file() and "src" not in f.relative_to(data).parts and f.suffix != ".sqlite"
    )
    for secret in ("Tiger123", "Sekret9", "TopSecret77", "Hunter2"):
        assert secret not in blob


def test_api_import_roots(tmp_path, monkeypatch):
    from apps.api.main import app
    from fastapi.testclient import TestClient

    ok, bad = tmp_path / "ok", tmp_path / "bad"
    for d in (ok, bad):
        d.mkdir()
        (d / "a.sas").write_text("run;")
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("SGM_IMPORT_ROOTS", str(ok))
    c = TestClient(app)
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    assert c.post(f"/api/projects/{pid}/imports", json={"path": str(bad)}).status_code == 403
    assert (
        c.post(f"/api/projects/{pid}/imports", json={"path": str(ok / ".." / "bad")}).status_code
        == 403
    )
    assert c.post(f"/api/projects/{pid}/imports", json={"path": str(ok)}).status_code == 201


def test_api_upload_zip_and_static_ui(tmp_path, monkeypatch):
    import io
    import zipfile

    import apps.api.main as m
    from fastapi.testclient import TestClient

    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    c = TestClient(m.app)
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("a/x.sas", "data a; run;")
        z.writestr("../evil.sas", "x")
    r = c.post(f"/api/projects/{pid}/uploads", files={"file": ("p.zip", buf.getvalue())})
    assert r.status_code == 201
    m_ = r.json()
    assert [f["path"] for f in m_["files"]] == ["a/x.sas"]
    assert any(s["reason"] == "ruta insegura" for s in m_["skipped"])
    bad = c.post(f"/api/projects/{pid}/uploads", files={"file": ("p.zip", b"no es zip")})
    assert bad.status_code == 422
