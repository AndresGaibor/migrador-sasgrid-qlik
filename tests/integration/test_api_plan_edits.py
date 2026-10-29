from apps.api import main as api_module
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import Expression, JobPlan, PlanSet, PlanStep
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.ast import Loc


def _project_with_plans(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    monkeypatch.setenv("SGM_DATA_DIR", str(data_dir))
    store = Store(Settings(data_dir=data_dir))
    project = store.create_project("Finanzas")
    plans = PlanSet(
        project_id=project.id,
        rules_version="r1",
        plans=[
            JobPlan(
                project_id=project.id,
                rules_version="r1",
                program="daily.sas",
                job_name="job_daily",
                steps=[
                    PlanStep(
                        id="step-1",
                        order=1,
                        subjob="",
                        action="configure",
                        purpose="Filtrar registros",
                        evidence=Loc(file="daily.sas", line=1, end_line=1),
                        expressions=[Expression(sas="amount > 0", talend="row.amount > 0", line=1)],
                    )
                ],
            ),
            JobPlan(
                project_id=project.id,
                rules_version="r1",
                program="other.sas",
                job_name="job_other",
            ),
        ],
    )
    store.plans_path(project.id).parent.mkdir(parents=True, exist_ok=True)
    store.plans_path(project.id).write_text(plans.model_dump_json(), encoding="utf-8")
    return project.id


def test_job_meta_changes_name_and_description_seen_by_plan_api(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        response = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta",
            json={"job_name": "daily_load", "description": "Carga diaria"},
        )
        plan = client.get(f"/api/projects/{project_id}/plans/daily.sas")
        rows = client.get(f"/api/projects/{project_id}/plans")

    assert response.status_code == 200, response.text
    assert plan.json()["job_name"] == "daily_load"
    assert plan.json()["description"] == "Carga diaria"
    assert rows.json()[0]["job_name"] == "daily_load"
    assert rows.json()[0]["description"] == "Carga diaria"


def test_job_meta_rejects_invalid_or_taken_names_without_saving(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        invalid = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta",
            json={"job_name": "2invalid", "description": None},
        )
        duplicate = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta",
            json={"job_name": "JOB_OTHER", "description": None},
        )
        rows = client.get(f"/api/projects/{project_id}/plans").json()

    assert invalid.status_code == 422
    assert duplicate.status_code == 422
    assert rows[0]["job_name"] == "job_daily"


def test_expression_edit_saves_and_clears_a_guarded_override(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    path = f"/api/projects/{project_id}/plans/daily.sas/steps/step-1/expressions/0"
    with TestClient(api_module.app) as client:
        changed = client.patch(path, json={"talend": "input_row.amount > 0"})
        cleared = client.patch(path, json={"talend": None})

    assert changed.status_code == 200, changed.text
    assert changed.json()["steps"][0]["expressions"][0]["talend"] == "input_row.amount > 0"
    assert changed.json()["steps"][0]["expressions"][0]["talend_edited"] is True
    assert cleared.status_code == 200, cleared.text
    assert cleared.json()["steps"][0]["expressions"][0]["talend"] == "row.amount > 0"
    assert cleared.json()["steps"][0]["expressions"][0]["talend_edited"] is False


def test_translator_api_returns_result_and_rejects_empty_or_oversized_input():
    with TestClient(api_module.app) as client:
        translated = client.post("/api/translator/translate", json={"sas": "upcase(nome)"})
        unsupported = client.post("/api/translator/translate", json={"sas": "lag(nome)"})
        empty = client.post("/api/translator/translate", json={"sas": ""})
        oversized = client.post("/api/translator/translate", json={"sas": "x" * 20001})

    assert translated.status_code == 200
    assert translated.json()["talend"] == "input_row.nome.toUpperCase()"
    assert translated.json()["columns"] == ["nome"]
    assert translated.json()["supported"] is True
    assert unsupported.status_code == 200
    assert unsupported.json()["talend"] is None
    assert unsupported.json()["supported"] is False
    assert empty.status_code == 422
    assert oversized.status_code == 422


def test_bulk_rename_previews_and_applies_all_or_nothing(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    base = f"/api/projects/{project_id}/plans"
    with TestClient(api_module.app) as client:
        preview = client.post(f"{base}/rename-preview", json={"mode": "prefix", "text": "fin_"})
        before = client.get(base).json()
        invalid = client.post(
            f"{base}/rename",
            json={"renames": [
                {"program": "daily.sas", "job_name": "fin_daily"},
                {"program": "other.sas", "job_name": "not-valid"},
            ]},
        )
        after_invalid = client.get(base).json()
        applied = client.post(
            f"{base}/rename",
            json={"renames": [
                {"program": "daily.sas", "job_name": "fin_daily"},
                {"program": "other.sas", "job_name": "fin_other"},
            ]},
        )
        after_apply = client.get(base).json()

    assert preview.status_code == 200
    assert {row["proposed"] for row in preview.json()} == {"fin_job_daily", "fin_job_other"}
    assert invalid.status_code == 422
    assert [row["job_name"] for row in after_invalid] == [row["job_name"] for row in before]
    assert applied.status_code == 200
    assert applied.json()["renamed"] == 2
    assert {row["job_name"] for row in after_apply} == {"fin_daily", "fin_other"}


def test_naming_template_validates_previews_and_persists(tmp_path, monkeypatch):
    _project_with_plans(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        initial = client.get("/api/settings/naming")
        preview = client.post(
            "/api/settings/naming/preview", json={"template": "{proyecto}_{programa}"}
        )
        missing_program = client.post(
            "/api/settings/naming/preview", json={"template": "{proyecto}"}
        )
        unknown_token = client.post(
            "/api/settings/naming/preview", json={"template": "job_{foo}"}
        )
        saved = client.put("/api/settings/naming", json={"template": "fin_{programa}"})
        rejected = client.put("/api/settings/naming", json={"template": "{carpeta}"})
        after = client.get("/api/settings/naming")

    assert initial.json()["template"] == "job_{programa}"
    assert initial.json()["tokens"] == ["proyecto", "carpeta", "programa"]
    assert preview.status_code == 200
    assert preview.json()["name"] == "finanzas_cod_2"
    assert missing_program.status_code == 422
    assert unknown_token.status_code == 422
    assert saved.status_code == 200
    assert saved.json()["example_name"] == "fin_cod_2"
    assert rejected.status_code == 422
    assert after.json()["template"] == "fin_{programa}"
