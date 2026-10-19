import io
import json
import zipfile

from apps.api.main import app
from fastapi.testclient import TestClient


def _project(client: TestClient) -> str:
    response = client.post("/api/projects", json={"name": "SAS Grid demo"})
    assert response.status_code == 201
    return response.json()["id"]


def test_uploaded_grid_zip_produces_persistent_exportable_guide(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(app)
    project_id = _project(client)
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w") as source:
        source.writestr(
            "grid/submit.sh",
            "sasgsub -gridsubmitpgm /sas/daily.sas -gridjobname daily "
            "-gridqueue normal -gridwaitresults -set RUN_DATE 2025-01-31\n",
        )
        source.writestr("sas/daily.sas", "data work.daily;\nset source.daily;\nrun;\n")

    uploaded = client.post(
        f"/api/projects/{project_id}/uploads",
        files={"file": ("project.zip", archive.getvalue(), "application/zip")},
    )
    assert uploaded.status_code == 201, uploaded.text
    assert {item["path"] for item in uploaded.json()["files"]} == {
        "grid/submit.sh",
        "sas/daily.sas",
    }

    analysis = client.post(f"/api/projects/{project_id}/analyses")
    assert analysis.status_code == 201, analysis.text
    dependencies = client.get(f"/api/projects/{project_id}/dependencies")
    assert dependencies.status_code == 200, dependencies.text
    task = dependencies.json()["orchestration"]["tasks"][0]
    assert task["kind"] == "sasgsub"
    assert task["resolved_program"] == "sas/daily.sas"
    assert task["job_name"] == "daily" and task["queue"] == "normal"

    generated = client.post(f"/api/projects/{project_id}/plans")
    assert generated.status_code == 201, generated.text
    plans = client.get(f"/api/projects/{project_id}/plans")
    assert plans.status_code == 200 and plans.json()[0]["program"] == "sas/daily.sas"
    plan_url = f"/api/projects/{project_id}/plans/sas/daily.sas"
    plan = client.get(plan_url)
    assert plan.status_code == 200, plan.text
    body = plan.json()
    assert body["orchestration"]["grid_tasks"] == [task["id"]]
    assert body["steps"]
    assert body["steps"][0]["evidence"] == {
        "file": "sas/daily.sas",
        "line": 1,
        "end_line": 3,
    }

    step_id = body["steps"][0]["id"]
    updated = client.patch(
        f"{plan_url}/steps/{step_id}",
        json={"status": "pendiente", "note": "Confirmar conexión de origen"},
    )
    assert updated.status_code == 200, updated.text
    reloaded = client.get(plan_url).json()
    step = next(step for step in reloaded["steps"] if step["id"] == step_id)
    assert (step["status"], step["note"]) == ("pendiente", "Confirmar conexión de origen")

    exported = client.post(f"/api/projects/{project_id}/exports")
    assert exported.status_code == 201, exported.text
    assert {"index.md", "steps.csv"} <= set(exported.json()["files"])
    export_dir = tmp_path / "data" / "projects" / project_id / "exports"
    plan_json = next(export_dir.glob("*.json"))
    exported_plan = json.loads(plan_json.read_text())
    assert exported_plan["program"] == "sas/daily.sas"
    assert next(step for step in exported_plan["steps"] if step["id"] == step_id)["status"] == "pendiente"


def test_upload_rejects_unsupported_extension(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(app)
    project_id = _project(client)

    response = client.post(
        f"/api/projects/{project_id}/uploads",
        files={"file": ("notes.txt", b"not a project", "text/plain")},
    )
    assert response.status_code == 422


def test_uploaded_single_sas_file_produces_plan(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(app)
    project_id = _project(client)

    uploaded = client.post(
        f"/api/projects/{project_id}/uploads",
        files={"file": ("daily.sas", b"data work.daily; set source.daily; run;", "text/plain")},
    )
    assert uploaded.status_code == 201, uploaded.text
    assert [item["path"] for item in uploaded.json()["files"]] == ["daily.sas"]
    analysis = client.post(f"/api/projects/{project_id}/analyses")
    assert analysis.status_code == 201, analysis.text
    generated = client.post(f"/api/projects/{project_id}/plans")
    assert generated.status_code == 201, generated.text
    plan = client.get(f"/api/projects/{project_id}/plans/daily.sas")
    assert plan.status_code == 200 and plan.json()["steps"]
