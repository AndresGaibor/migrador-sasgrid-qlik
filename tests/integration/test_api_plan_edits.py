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


def test_translator_survives_deeply_nested_or_long_hostile_input():
    with TestClient(api_module.app) as client:
        for sas in ["not " * 4000 + "x", "-" * 20000]:
            response = client.post("/api/translator/translate", json={"sas": sas})
            assert response.status_code == 200, response.text
            assert response.json()["supported"] is False
            assert response.json()["talend"] is None
            assert response.json()["warnings"]


def test_translator_failure_is_logged_and_still_answers_200(monkeypatch, caplog):
    def boom(_sas):
        raise RuntimeError("fallo interno del traductor")

    monkeypatch.setattr(api_module, "translate", boom)

    with TestClient(api_module.app) as client, caplog.at_level("ERROR", logger="apps.api.main"):
        response = client.post("/api/translator/translate", json={"sas": "upcase(nome)"})

    assert response.status_code == 200
    assert response.json()["talend"] is None
    assert response.json()["supported"] is False
    assert any(record.levelname == "ERROR" and record.exc_info for record in caplog.records)


def _store() -> Store:
    return Store(Settings.from_env())


CREATED_WARNING = (
    "Este Job ya se creó en Talend Studio con el nombre anterior (job_daily). "
    "El portal no lo renombra en Studio: ese Job se conserva con el nombre anterior y la próxima "
    "aplicación puede pedir confirmar la nueva revisión."
)
DESCRIPTION_WARNING = (
    "Este Job ya se creó en Talend Studio; el cambio de descripción no se refleja allí hasta volver "
    "a aplicar y la aplicación puede pedir confirmar la nueva revisión."
)


def _mark_created(project_id, program, job_name, status="applied"):
    _store().save_talend_apply_state(
        project_id, program, revision_hash="old", status=status, identity={"job_name": job_name}, result={}
    )


def test_meta_rename_after_studio_creation_warns_with_previous_name(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    _mark_created(project_id, "daily.sas", "job_daily", status="partially_applied")
    with TestClient(api_module.app) as client:
        renamed = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta", json={"job_name": "daily_load"}
        )

    assert renamed.status_code == 200, renamed.text
    assert renamed.json()["warnings"] == [CREATED_WARNING]


def test_meta_description_after_studio_creation_warns_only_when_it_changes(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    _mark_created(project_id, "daily.sas", "job_daily")
    url = f"/api/projects/{project_id}/plans/daily.sas/meta"
    with TestClient(api_module.app) as client:
        changed = client.patch(url, json={"description": "Carga diaria"})
        unchanged = client.patch(url, json={"description": "Carga diaria"})
        other_job = client.patch(f"/api/projects/{project_id}/plans/other.sas/meta", json={"description": "x"})

    assert changed.json()["warnings"] == [DESCRIPTION_WARNING]
    assert unchanged.json()["warnings"] == []
    assert other_job.json()["warnings"] == []


def test_meta_rename_of_a_job_never_applied_has_no_warning(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        response = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta", json={"job_name": "daily_load"}
        )

    assert response.status_code == 200, response.text
    assert response.json()["warnings"] == []


def test_meta_rename_of_a_job_created_by_a_batch_warns(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    store = _store()
    store.begin_talend_apply_batch(project_id, "rev", ["daily.sas"])
    store.update_talend_apply_batch_state(
        project_id,
        status="completed",
        jobs=[{"program": "daily.sas", "status": "applied", "identity": {"job_name": "job_daily"}}],
        current_program=None,
        completed_count=1,
    )
    with TestClient(api_module.app) as client:
        response = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta", json={"job_name": "daily_load"}
        )

    assert response.status_code == 200, response.text
    assert response.json()["warnings"] == [CREATED_WARNING]


def test_bulk_rename_warns_only_for_created_jobs_whose_name_changed(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    _mark_created(project_id, "daily.sas", "job_daily")
    with TestClient(api_module.app) as client:
        response = client.post(
            f"/api/projects/{project_id}/plans/rename",
            json={"renames": [
                {"program": "daily.sas", "job_name": "daily_load"},
                {"program": "other.sas", "job_name": "other_load"},
            ]},
        )
        unchanged = client.post(
            f"/api/projects/{project_id}/plans/rename",
            json={"renames": [{"program": "daily.sas", "job_name": "daily_load"}]},
        )

    assert response.status_code == 200, response.text
    assert response.json() == {"renamed": 2, "warnings": [CREATED_WARNING]}
    assert unchanged.json() == {"renamed": 0, "warnings": []}


def test_bulk_rename_of_never_applied_jobs_has_no_warnings(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        response = client.post(
            f"/api/projects/{project_id}/plans/rename",
            json={"renames": [{"program": "daily.sas", "job_name": "daily_load"}]},
        )

    assert response.status_code == 200, response.text
    assert response.json() == {"renamed": 1, "warnings": []}


def test_regex_rename_preview_rejects_catastrophic_pattern_with_422(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    with TestClient(api_module.app) as client:
        response = client.post(
            f"/api/projects/{project_id}/plans/rename-preview",
            json={"mode": "regex", "find": "(a|aa)+$", "replace_with": "x"},
        )

    assert response.status_code == 422
    assert response.json()["detail"] == "El patrón es demasiado complejo."


def test_meta_rename_and_expression_edits_are_blocked_while_a_batch_runs(tmp_path, monkeypatch):
    project_id = _project_with_plans(tmp_path, monkeypatch)
    store = _store()
    expected = "No se puede editar mientras Talend crea Jobs de este proyecto."
    # El lote se marca después de abrir el cliente: su arranque recupera operaciones interrumpidas.
    with TestClient(api_module.app) as client:
        store.begin_talend_apply_batch(project_id, "rev", ["daily.sas", "other.sas"])
        store.update_talend_apply_batch_state(
            project_id, status="running", jobs=[], current_program="daily.sas", completed_count=0
        )
        meta = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/meta", json={"job_name": "daily_load"}
        )
        rename = client.post(
            f"/api/projects/{project_id}/plans/rename",
            json={"renames": [{"program": "daily.sas", "job_name": "daily_load"}]},
        )
        expr = client.patch(
            f"/api/projects/{project_id}/plans/daily.sas/steps/step-1/expressions/0",
            json={"talend": "input_row.amount > 0"},
        )

    assert [meta.status_code, rename.status_code, expr.status_code] == [409, 409, 409]
    assert meta.json()["detail"] == rename.json()["detail"] == expr.json()["detail"] == expected
    assert store.get_job_overrides(project_id) == {}
    assert store.get_expression_overrides(project_id) == {}
