from pathlib import Path

from apps.api import main as api_module
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.domain.models import FileKind, SourceFile
from sas_grid_migrator.migration_planner.activity import activity_changed, project_activity
from sas_grid_migrator.persistence.store import Store


def _zip_project(tmp_path: Path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    staged = tmp_path / "staged" / "src"
    staged.mkdir(parents=True)
    (staged / "daily.sas").write_text("data daily; run;", encoding="utf-8")
    project, _ = store.create_zip_project(
        name="Eventos",
        archive_name="eventos.zip",
        archive_sha256="c" * 64,
        archive_size_bytes=64,
        staged_source_dir=staged,
        files=[SourceFile(path="daily.sas", sha256="d" * 64, size=16, kind=FileKind.SAS)],
        skipped=[],
    )
    return store, project


def test_activity_is_empty_for_projects_without_automatic_processing(tmp_path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("Manual")

    assert project_activity(store, project.id) == {"processing": None, "batch": None}


def test_activity_changes_with_processing_and_batch_state(tmp_path):
    store, project = _zip_project(tmp_path)
    queued = project_activity(store, project.id)
    assert queued["processing"]["status"] == "queued"
    assert queued["batch"] is None
    assert activity_changed(None, queued)

    store.update_processing(project.id, status="running", stage="analysis", message="Analizando")
    running = project_activity(store, project.id)
    assert activity_changed(queued, running)
    assert running["processing"]["status"] == "running"
    assert running["processing"]["stage"] == "analysis"

    assert not activity_changed(running, project_activity(store, project.id))

    store.begin_talend_apply_batch(project.id, "revision-1", ["daily.sas"])
    with_batch = project_activity(store, project.id)
    assert activity_changed(running, with_batch)
    assert with_batch["batch"]["total_jobs"] == 1
    assert with_batch["batch"]["completed_jobs"] == 0

def test_events_endpoint_rejects_an_unknown_project(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    with TestClient(api_module.app) as client:
        response = client.get("/api/projects/does-not-exist/events")

    assert response.status_code == 404
