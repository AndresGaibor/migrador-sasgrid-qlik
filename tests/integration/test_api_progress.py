import apps.api.main as api_module
import pytest
from fastapi.testclient import TestClient
from tests.support.plan_api import make_plan, project_with_plans

from sas_grid_migrator.migration_planner.models import PlanStep
from sas_grid_migrator.sas_parser.ast import Loc


@pytest.fixture(autouse=True)
def _env(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    monkeypatch.delenv("SGM_TALEND_EXPRESSIONS", raising=False)


@pytest.fixture
def client():
    with TestClient(api_module.app) as c:
        yield c


def _plan_with_pending(project_id: str):
    plan = make_plan(project_id, "a.sas", "job_a", child_call=True)
    plan.steps.append(
        PlanStep(
            id="pending-1",
            order=2,
            subjob="default",
            action="configure",
            purpose="Configurar origen",
            pending=["ruta, delimitador"],
            evidence=Loc(file="a.sas", line=2, end_line=2),
        )
    )
    return plan


def test_progress_with_plans_reports_guides_done(client):
    project_id = project_with_plans(client, "Progreso", [_plan_with_pending("pending")])

    response = client.get(f"/api/projects/{project_id}/progress")

    assert response.status_code == 200, response.text
    body = response.json()
    stages = {stage["key"]: stage for stage in body["stages"]}
    assert stages["guides"]["status"] == "done"
    assert stages["complete"]["detail"] == "0 de 2 pasos"
    assert body["next"]["key"] == "upload"


def test_progress_without_plans_leaves_guides_undone(client):
    project_id = client.post("/api/projects", json={"name": "Sin planes"}).json()["id"]

    response = client.get(f"/api/projects/{project_id}/progress")

    assert response.status_code == 200, response.text
    stages = {stage["key"]: stage for stage in response.json()["stages"]}
    assert stages["guides"]["status"] != "done"


def test_progress_unknown_project_is_404(client):
    response = client.get("/api/projects/no-existe/progress")

    assert response.status_code == 404


def test_pending_summary_groups_pending_steps(client):
    project_id = project_with_plans(client, "Pendientes", [_plan_with_pending("pending")])

    response = client.get(f"/api/projects/{project_id}/pending-summary")

    assert response.status_code == 200, response.text
    groups = response.json()
    assert len(groups) == 1
    assert groups[0]["reason"] == "ruta, delimitador"
    assert groups[0]["steps"] == 1
    assert groups[0]["programs"] == [
        {"program": "a.sas", "job_name": "job_a", "step_ids": ["pending-1"]}
    ]


def test_pending_summary_without_plans_is_409(client):
    project_id = client.post("/api/projects", json={"name": "Sin planes"}).json()["id"]

    response = client.get(f"/api/projects/{project_id}/pending-summary")

    assert response.status_code == 409


def test_pending_summary_unknown_project_is_404(client):
    response = client.get("/api/projects/no-existe/pending-summary")

    assert response.status_code == 404
