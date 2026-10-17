import hashlib
import json
import stat
import zipfile
from pathlib import Path

import pytest
from apps.api.main import app as api
from fastapi.testclient import TestClient
from typer.testing import CliRunner

from sas_grid_migrator.cli.main import app as cli
from sas_grid_migrator.config import Settings
from sas_grid_migrator.domain.models import Manifest
from sas_grid_migrator.ingestion.importer import ImportError_, import_source, safe_relpath
from sas_grid_migrator.persistence.store import Store

ROOT = Path(__file__).parent.parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "sas"


def cfg(tmp_path, **kw) -> Settings:
    return Settings(data_dir=tmp_path / "data", **kw)


@pytest.mark.parametrize("bad", ["../x.sas", "/etc/passwd", "a/../../x", "C:\\x.sas", "a\0b", ""])
def test_safe_relpath_rejects(bad):
    assert safe_relpath(bad) is None


def test_safe_relpath_normalizes():
    assert safe_relpath("a\\b/./c.sas") == "a/b/c.sas"


def test_folder_import_hashes_and_skips(tmp_path):
    src = tmp_path / "src"
    (src / ".git").mkdir(parents=True)
    (src / ".git" / "config").write_text("x")
    (src / "a.sas").write_bytes("data x; run; /* ñ */".encode("cp1252"))
    (src / "big.sas").write_bytes(b"x" * 50)
    (src / "link.sas").symlink_to(src / "a.sas")
    files, skipped = import_source(src, tmp_path / "dest", cfg(tmp_path, max_file_bytes=40))
    by = {f.path: f for f in files}
    assert set(by) == {"a.sas"}
    assert by["a.sas"].encoding == "cp1252"
    assert by["a.sas"].sha256 == hashlib.sha256((src / "a.sas").read_bytes()).hexdigest()
    assert {s.path: s.reason for s in skipped} == {
        "big.sas": "supera max_file_bytes",
        "link.sas": "enlace simbólico",
    }
    assert (tmp_path / "dest" / "a.sas").exists()


def test_zip_slip_and_symlink_rejected(tmp_path):
    z = tmp_path / "b.zip"
    with zipfile.ZipFile(z, "w") as zf:
        zf.writestr("ok/p.sas", "data a; run;")
        zf.writestr("../evil.sas", "x")
        zf.writestr("/abs.sas", "x")
        info = zipfile.ZipInfo("lnk.sas")
        info.external_attr = (stat.S_IFLNK | 0o777) << 16
        zf.writestr(info, "/etc/passwd")
    files, skipped = import_source(z, tmp_path / "dest", cfg(tmp_path))
    assert [f.path for f in files] == ["ok/p.sas"]
    assert {s.reason for s in skipped} == {"ruta insegura", "enlace simbólico"}
    assert not (tmp_path / "evil.sas").exists()


def test_zip_bomb_entry_skipped(tmp_path):
    z = tmp_path / "b.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("big.sas", "0" * 10_000)
    files, skipped = import_source(z, tmp_path / "dest", cfg(tmp_path, max_file_bytes=100))
    assert not files and skipped[0].reason == "supera max_file_bytes"


def test_global_limits_reject_batch(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    for i in range(3):
        (src / f"{i}.sas").write_text("x")
    with pytest.raises(ImportError_):
        import_source(src, tmp_path / "dest", cfg(tmp_path, max_files=2))
    with pytest.raises(ImportError_):
        import_source(tmp_path / "nope", tmp_path / "dest", cfg(tmp_path))


def test_store_roundtrip_is_reproducible(tmp_path):
    s = Store(cfg(tmp_path))
    p = s.create_project("demo")
    m1 = s.import_batch(p.id, FIXTURES)
    m2 = s.import_batch(p.id, FIXTURES)  # reimportar reemplaza, no duplica
    assert m1 == m2 == s.get_manifest(p.id)
    assert s.get_project(p.id).name == "demo"
    assert any(f.path == "real/ts-sas-legacy-analytics/Config/autoexec.sas" for f in m1.files)


def test_cli_import_and_inventory(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    r = CliRunner().invoke(
        cli, ["import", str(FIXTURES / "real" / "ts-sas-legacy-analytics"), "-n", "legacy"]
    )
    assert r.exit_code == 0, r.output
    pid = r.stdout.split()[0]
    out = CliRunner().invoke(cli, ["inventory", pid]).stdout
    assert "sas" in out and "shell" not in out


def test_api_flow(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    c = TestClient(api)
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    assert c.get("/api/projects/zzz/inventory").status_code == 404
    assert (
        c.post(f"/api/projects/{pid}/imports", json={"path": str(tmp_path / "nope")}).status_code
        == 422
    )
    r = c.post(f"/api/projects/{pid}/imports", json={"path": str(FIXTURES / "inc")})
    assert r.status_code == 201
    inv = c.get(f"/api/projects/{pid}/inventory").json()
    assert inv["files"][0]["path"] == "macros_comunes.sas"


def test_manifest_schema_is_current():
    committed = json.loads((ROOT / "schemas" / "manifest.schema.json").read_text())
    assert committed == Manifest.model_json_schema()


def test_import_source_containing_data_dir(tmp_path):
    """La carpeta de datos dentro de la fuente no se copia a sí misma."""
    src = tmp_path / "proj"
    (src / "a").mkdir(parents=True)
    (src / "a" / "x.sas").write_text("data a; run;")
    st = Store(Settings(data_dir=src / "data"))
    p = st.create_project("t")
    first = st.import_batch(p.id, src)
    again = st.import_batch(p.id, src)  # segunda vez: ya existe la copia dentro de la fuente
    assert [f.path for f in first.files] == ["a/x.sas"] == [f.path for f in again.files]


def test_import_from_own_snapshot_is_refused(tmp_path):
    st = Store(Settings(data_dir=tmp_path / "data"))
    p = st.create_project("t")
    (tmp_path / "s").mkdir()
    (tmp_path / "s" / "x.sas").write_text("run;")
    st.import_batch(p.id, tmp_path / "s")
    with pytest.raises(ImportError_):
        st.import_batch(p.id, st.source_dir(p.id))
    assert (st.source_dir(p.id) / "x.sas").exists()
