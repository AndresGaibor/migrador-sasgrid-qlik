"""API: estado estructurado de la guía, buenas prácticas del plan y snapshot de paneles Talend."""

import json

from apps.api import main as api_module
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import JobPlan, PlanSet, PlanStep, Property
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.ast import Loc


def _project(tmp_path, monkeypatch, note=None):
    data_dir = tmp_path / "data"
    monkeypatch.setenv("SGM_DATA_DIR", str(data_dir))
    store = Store(Settings(data_dir=data_dir))
    project = store.create_project("Guia")
    step = PlanStep(
        id="step-1",
        order=1,
        subjob="s1",
        action="add_component",
        component_candidate="tMysqlInput",
        purpose="Leer",
        evidence=Loc(file="daily.sas", line=1, end_line=1),
        note=note,
        properties=[Property(name="PASS", value='"secreto"', origin="SAS daily.sas:1")],
    )
    plans = PlanSet(
        project_id=project.id,
        rules_version="r1",
        plans=[JobPlan(project_id=project.id, rules_version="r1", program="daily.sas", job_name="job_daily", steps=[step])],
    )
    store.plans_path(project.id).parent.mkdir(parents=True, exist_ok=True)
    store.plans_path(project.id).write_text(plans.model_dump_json(), encoding="utf-8")
    return project.id


def test_legacy_note_is_read_as_guide_status(tmp_path, monkeypatch):
    project_id = _project(tmp_path, monkeypatch, note="[Estado de guía: completado]\n[Nota de trabajo: ok]")
    with TestClient(api_module.app) as client:
        plan = client.get(f"/api/projects/{project_id}/plans/daily.sas").json()

    assert plan["steps"][0]["guide_status"] == "completed"
    assert plan["steps"][0]["field_done"] == {}


def test_structured_guide_state_is_saved_and_merged(tmp_path, monkeypatch):
    project_id = _project(tmp_path, monkeypatch, note="[Estado de guía: completado]")
    url = f"/api/projects/{project_id}/plans/daily.sas/steps/step-1/guide"
    with TestClient(api_module.app) as client:
        first = client.patch(url, json={"guide_status": "in_progress", "field_done": {"FILENAME": True}})
        second = client.patch(url, json={"field_done": {"HOST": False}})
        plan = client.get(f"/api/projects/{project_id}/plans/daily.sas").json()
        bad = client.patch(url, json={"guide_status": "inventado"})

    assert first.status_code == 200, first.text
    assert second.json() == {"step_id": "step-1", "guide_status": "in_progress", "field_done": {"FILENAME": True, "HOST": False}}
    assert plan["steps"][0]["guide_status"] == "in_progress"
    assert bad.status_code == 422


def test_guide_state_rejects_unknown_step(tmp_path, monkeypatch):
    project_id = _project(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        response = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/steps/nope/guide", json={"guide_status": "completed"}
        )

    assert response.status_code == 422


def test_practices_endpoint_reports_plain_password(tmp_path, monkeypatch):
    project_id = _project(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        response = client.get(f"/api/projects/{project_id}/plans/daily.sas/practices")

    assert response.status_code == 200, response.text
    findings = response.json()
    assert any(item["id"] == "PLAN-SEC-01" and item["step_ids"] == ["step-1"] for item in findings)
    assert all(item["message"] for item in findings)


def test_component_panels_404_without_snapshot(tmp_path, monkeypatch):
    monkeypatch.setattr(api_module, "_PANELS_PATH", tmp_path / "missing.json")
    with TestClient(api_module.app) as client:
        response = client.get("/api/talend/component-panels")
        single = client.get("/api/talend/component-panels/tImpalaInput")

    assert response.status_code == 404
    assert "component-panels.json" in response.json()["detail"]
    assert single.status_code == 404


def test_component_panels_served_and_cached_by_mtime(tmp_path, monkeypatch):
    path = tmp_path / "component-panels.json"
    path.write_text(json.dumps({"version": 1, "components": {"tImpalaInput": {"title": "Impala Input"}}}), encoding="utf-8")
    monkeypatch.setattr(api_module, "_PANELS_PATH", path)
    with TestClient(api_module.app) as client:
        all_panels = client.get("/api/talend/component-panels").json()
        one = client.get("/api/talend/component-panels/tImpalaInput").json()
        missing = client.get("/api/talend/component-panels/tNoExiste")
        path.write_text(json.dumps({"version": 2, "components": {}}), encoding="utf-8")
        import os
        os.utime(path, (path.stat().st_atime, path.stat().st_mtime + 5))
        refreshed = client.get("/api/talend/component-panels").json()

    assert all_panels["version"] == 1
    assert one == {"name": "tImpalaInput", "panel": {"title": "Impala Input"}}
    assert missing.status_code == 404
    assert refreshed["version"] == 2
