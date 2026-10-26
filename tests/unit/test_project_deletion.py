import sqlite3
from datetime import UTC, datetime

import pytest
from fastapi.testclient import TestClient

import apps.api.main as api_module
from sas_grid_migrator.config import Settings
from sas_grid_migrator.persistence.store import ProjectDeletionBlockedError, Store


def _project(tmp_path, name="Project"):
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project(name)
    return store, project


def test_delete_project_removes_portal_state_and_owned_directory(tmp_path):
    store, project = _project(tmp_path)
    project_root = store.settings.data_dir / "projects" / project.id
    project_root.mkdir(parents=True)
    (project_root / "analysis.json").write_text("{}", encoding="utf-8")
    (project_root / "exports").mkdir()
    store.set_step_state(project.id, "daily.sas", "step-1", "done", None)
    store.save_talend_apply_state(
        project.id,
        "daily.sas",
        revision_hash="revision",
        status="failed",
        identity={"job_name": "DailyJob"},
    )

    assert store.delete_project(project.id) is True

    assert store.get_project(project.id) is None
    assert not project_root.exists()
    with sqlite3.connect(store.db) as connection:
        for table in (
            "source_files",
            "step_state",
            "skipped",
            "project_processing",
            "talend_apply_operations",
            "talend_apply_batches",
        ):
            assert connection.execute(
                f"select count(*) from {table} where project_id=?", (project.id,)
            ).fetchone()[0] == 0
    assert store.delete_project(project.id) is False


def test_delete_project_rejects_active_portal_or_talend_work(tmp_path):
    store, project = _project(tmp_path)
    with sqlite3.connect(store.db) as connection:
        connection.execute(
            """insert into project_processing
            (project_id,status,stage,updated_at,message,retry_count)
            values (?, 'queued', 'queued', ?, 'En cola', 0)""",
            (project.id, datetime.now(UTC).isoformat()),
        )
    with pytest.raises(ProjectDeletionBlockedError, match="análisis"):
        store.delete_project(project.id)

    store.update_processing(
        project.id,
        status="completed",
        stage="completed",
        message="Análisis listo",
    )
    batch, _ = store.begin_talend_apply_batch(project.id, "revision", ["daily.sas"])
    with pytest.raises(ProjectDeletionBlockedError, match="Talend"):
        store.delete_project(project.id)

    store.update_talend_apply_batch_state(
        project.id,
        status="failed",
        jobs=[{"program": "daily.sas", "status": "failed"}],
        current_program=None,
        completed_count=0,
    )
    store.save_talend_apply_state(
        project.id,
        "daily.sas",
        revision_hash="revision",
        status="running",
        identity={"job_name": "DailyJob"},
    )
    with pytest.raises(ProjectDeletionBlockedError, match="Talend"):
        store.delete_project(project.id)


def test_delete_api_requires_exact_name_and_removes_only_portal_project(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    with TestClient(api_module.app) as client:
        created = client.post("/api/projects", json={"name": "Proyecto de prueba"})
        project_id = created.json()["id"]
        store = Store(Settings(data_dir=tmp_path / "data"))
        project_root = store.settings.data_dir / "projects" / project_id
        project_root.mkdir(parents=True)
        (project_root / "plans.json").write_text("{}", encoding="utf-8")

        rejected = client.request(
            "DELETE",
            f"/api/projects/{project_id}",
            json={"confirmation": "Otro nombre"},
        )
        assert rejected.status_code == 422
        assert client.get("/api/projects").json()[0]["id"] == project_id
        assert (project_root / "plans.json").exists()

        store.save_talend_apply_state(
            project_id,
            "daily.sas",
            revision_hash="revision",
            status="running",
            identity={"job_name": "DailyJob"},
        )
        active_rejection = client.request(
            "DELETE",
            f"/api/projects/{project_id}",
            json={"confirmation": "Proyecto de prueba"},
        )
        assert active_rejection.status_code == 409
        assert (project_root / "plans.json").exists()
        store.save_talend_apply_state(
            project_id,
            "daily.sas",
            revision_hash="revision",
            status="failed",
            identity={"job_name": "DailyJob"},
        )

        deleted = client.request(
            "DELETE",
            f"/api/projects/{project_id}",
            json={"confirmation": "Proyecto de prueba"},
        )
        assert deleted.status_code == 200, deleted.text
        assert deleted.json() == {
            "deleted": True,
            "project_id": project_id,
            "name": "Proyecto de prueba",
            "talend_jobs_untouched": True,
        }
        assert not project_root.exists()
        assert client.get("/api/projects").json() == []
