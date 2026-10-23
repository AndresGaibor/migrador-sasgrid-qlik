import io
import zipfile
from concurrent.futures import ThreadPoolExecutor
from threading import Event

import apps.api.main as api_module
from fastapi.testclient import TestClient
from sas_grid_migrator.config import Settings
from sas_grid_migrator.persistence.store import Store


def _zip(files: dict[str, str]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        for path, source in files.items():
            archive.writestr(path, source)
    return output.getvalue()


def _upload(client: TestClient, name: str, content: bytes, display_name: str | None = None):
    form = {"name": display_name} if display_name else None
    return client.post(
        "/api/projects/uploads",
        data=form,
        files={"file": (name, content, "application/zip")},
    )


def test_health_reports_configured_pipeline_capacity(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("SGM_MAX_PIPELINE_CONCURRENCY", "3")
    monkeypatch.setenv("SGM_MAX_QUEUED_PIPELINES", "7")
    with TestClient(api_module.app) as client:
        health = client.get("/api/health").json()

    assert health["max_pipeline_concurrency"] == 3
    assert health["max_queued_pipelines"] == 7


def test_zip_upload_creates_an_isolated_project_and_runs_the_static_pipeline(
    tmp_path, monkeypatch
):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setattr(
        api_module,
        "_talend",
        lambda: (_ for _ in ()).throw(AssertionError("upload must not call the MCP")),
        raising=False,
    )
    with TestClient(api_module.app) as client:
        first = _upload(
            client,
            "analytics.zip",
            _zip({"Banking/daily.sas": "data work.daily; run;", "README.md": "first"}),
        )
        second = _upload(
            client,
            "analytics.zip",
            _zip({"Banking/daily.sas": "data work.daily; set other; run;"}),
        )

        assert first.status_code == 201, first.text
        assert second.status_code == 201, second.text
        first_data, second_data = first.json(), second.json()
        first_project, second_project = first_data["project"], second_data["project"]
        assert first_project["id"] != second_project["id"]
        assert first_project["archive_name"] == second_project["archive_name"] == "analytics.zip"
        assert first_project["archive_sha256"] != second_project["archive_sha256"]
        assert first_project["manifest_summary"] == {
            "files": 2,
            "programs": 1,
            "folders": 1,
            "skipped": 0,
        }
        assert first_data["processing"]["status"] == "queued"

        first_id, second_id = first_project["id"], second_project["id"]
        assert client.get(f"/api/projects/{first_id}/processing").json()["status"] == "completed"
        assert client.get(f"/api/projects/{second_id}/processing").json()["status"] == "completed"
        first_summary = client.get(f"/api/projects/{first_id}/analyses")
        second_summary = client.get(f"/api/projects/{second_id}/analyses")
        assert first_summary.status_code == second_summary.status_code == 200
        assert first_summary.json()["programs"] == second_summary.json()["programs"] == 1
        assert client.get(f"/api/projects/{first_id}/programs").json()[0]["file"] == "Banking/daily.sas"
        assert client.get(f"/api/projects/{second_id}/programs").json()[0]["file"] == "Banking/daily.sas"
        first_source = client.get(f"/api/projects/{first_id}/source/Banking/daily.sas?line=1").text
        second_source = client.get(f"/api/projects/{second_id}/source/Banking/daily.sas?line=1").text
        assert "set other" not in first_source
        assert "set other" in second_source


def test_analysis_summary_is_retrievable_after_refresh_and_requires_analysis(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    with TestClient(api_module.app) as client:
        legacy = client.post("/api/projects", json={"name": "Legacy"}).json()
        assert client.get(f"/api/projects/{legacy['id']}/analyses").status_code == 409

        uploaded = _upload(client, "persisted.zip", _zip({"daily.sas": "data a; run;"}))
        project_id = uploaded.json()["project"]["id"]
        summary = client.get(f"/api/projects/{project_id}/analyses")

        assert summary.status_code == 200, summary.text
        assert summary.json()["programs"] == 1


def test_invalid_zip_does_not_publish_an_empty_project(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    with TestClient(api_module.app) as client:
        response = _upload(client, "broken.zip", b"not a zip")

        assert response.status_code == 422
        assert client.get("/api/projects").json() == []
        assert not (tmp_path / "data" / "projects").exists()


def test_existing_project_rejects_replacement_imports(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    with TestClient(api_module.app) as client:
        created = client.post("/api/projects", json={"name": "Legacy"})
        project_id = created.json()["id"]
        first = client.post(
            f"/api/projects/{project_id}/uploads",
            files={"file": ("one.zip", _zip({"daily.sas": "data a; run;"}), "application/zip")},
        )
        second = client.post(
            f"/api/projects/{project_id}/uploads",
            files={"file": ("two.zip", _zip({"daily.sas": "data b; run;"}), "application/zip")},
        )
        replacement = tmp_path / "replacement"
        replacement.mkdir()
        (replacement / "daily.sas").write_text("data c; run;", encoding="utf-8")
        imported = client.post(
            f"/api/projects/{project_id}/imports",
            json={"path": str(replacement)},
        )
        source = client.get(f"/api/projects/{project_id}/source/daily.sas?line=1")

        assert first.status_code == 201
        assert second.status_code == 409
        assert "ya tiene un lote" in second.json()["detail"].lower()
        assert imported.status_code == 409
        assert "data a" in source.text and "data b" not in source.text


def test_failed_pipeline_can_be_retried_from_the_retained_snapshot(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    monkeypatch.setenv("SGM_DATA_DIR", str(data_dir))
    with TestClient(api_module.app) as client:
        uploaded = _upload(client, "retry.zip", _zip({"daily.sas": "data a; run;"}))
        project_id = uploaded.json()["project"]["id"]
        store = Store(Settings(data_dir=data_dir))
        store.update_processing(
            project_id,
            status="failed",
            stage="analysis",
            message="El análisis falló.",
            error="Error temporal",
        )
        retry = client.post(f"/api/projects/{project_id}/processing/retry")

        assert retry.status_code == 202, retry.text
        assert retry.json()["status"] == "queued"
        assert client.get(f"/api/projects/{project_id}/processing").json()["status"] == "completed"
        assert client.get(f"/api/projects/{project_id}/inventory").status_code == 200
        assert Store(Settings(data_dir=data_dir)).get_processing(project_id).retry_count == 1


def test_api_startup_recovers_a_running_project_pipeline(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    monkeypatch.setenv("SGM_DATA_DIR", str(data_dir))
    with TestClient(api_module.app) as client:
        uploaded = _upload(client, "interrupted.zip", _zip({"daily.sas": "data a; run;"}))
        project_id = uploaded.json()["project"]["id"]
        Store(Settings(data_dir=data_dir)).update_processing(
            project_id,
            status="running",
            stage="dependencies",
            message="Construyendo dependencias.",
        )

    with TestClient(api_module.app) as reopened:
        state = reopened.get(f"/api/projects/{project_id}/processing").json()

    assert state["status"] == "interrupted"
    assert state["stage"] == "dependencies"


def test_pipeline_concurrency_limit_rejects_upload_when_capacity_is_full(
    tmp_path, monkeypatch
):
    data_dir = tmp_path / "data"
    monkeypatch.setenv("SGM_DATA_DIR", str(data_dir))
    monkeypatch.setenv("SGM_MAX_PIPELINE_CONCURRENCY", "1")
    monkeypatch.setenv("SGM_MAX_QUEUED_PIPELINES", "0")
    entered_analysis, release_analysis = Event(), Event()
    original = api_module.analyze_project

    def blocked_analysis(store, project_id):
        entered_analysis.set()
        assert release_analysis.wait(10), "test did not release the pipeline"
        return original(store, project_id)

    monkeypatch.setattr(api_module, "analyze_project", blocked_analysis)
    with TestClient(api_module.app) as first_client, TestClient(api_module.app) as second_client:
        with ThreadPoolExecutor(max_workers=1) as pool:
            first_request = pool.submit(
                _upload,
                first_client,
                "first.zip",
                _zip({"first.sas": "data a; run;"}),
            )
            try:
                assert entered_analysis.wait(5), "first pipeline never started"
                second = _upload(
                    second_client,
                    "second.zip",
                    _zip({"second.sas": "data b; run;"}),
                )
                assert second.status_code == 429
                assert "capacidad" in second.json()["detail"].lower()
            finally:
                release_analysis.set()
            assert first_request.result(timeout=15).status_code == 201
