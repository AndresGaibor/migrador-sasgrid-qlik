import json

import apps.api.main as api_module
import pytest
from fastapi.testclient import TestClient
from tests.support.plan_api import FakeTalend, make_plan, project_with_plans

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import Expression, PlanStep
from sas_grid_migrator.persistence.store import Store
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


def _store() -> Store:
    return Store(Settings.from_env())


def _two_jobs(client, name="Edits"):
    return project_with_plans(
        client,
        name,
        [make_plan("pending", "a.sas", "job_a"), make_plan("pending", "b.sas", "job_b")],
    )


def _names(client, project_id) -> dict[str, str]:
    rows = client.get(f"/api/projects/{project_id}/plans").json()
    return {row["program"]: row["job_name"] for row in rows}


def _plan_with_expression(project_id: str):
    plan = make_plan(project_id, "calc.sas", "job_calc")
    plan.steps.append(
        PlanStep(
            id="calc-1",
            order=1,
            subjob="default",
            action="add_component",
            component_candidate="tMap",
            purpose="Calcular",
            expressions=[
                Expression(sas="x + 1", talend="(input_row.x + 1)", target="y", line=1),
            ],
            evidence=Loc(file="calc.sas", line=1, end_line=1),
        )
    )
    return plan


def test_rename_job_updates_the_plan_list_and_the_apply_spec(client):
    project_id = _two_jobs(client)

    response = client.patch(f"/api/projects/{project_id}/plans/a.sas/meta", json={"job_name": "mi_job"})
    assert response.status_code == 200, response.text
    assert response.json()["plan"]["job_name"] == "mi_job"
    assert response.json()["warnings"] == []

    assert _names(client, project_id)["a.sas"] == "mi_job"
    preview = client.post(f"/api/projects/{project_id}/plans/a.sas/talend-apply/preview")
    assert preview.status_code == 200, preview.text
    assert preview.json()["identity"]["job_name"] == "mi_job"


def test_rename_to_the_generated_name_or_empty_clears_the_override(client):
    project_id = _two_jobs(client)
    url = f"/api/projects/{project_id}/plans/a.sas/meta"
    client.patch(url, json={"job_name": "mi_job"})

    assert client.patch(url, json={"job_name": "job_a"}).status_code == 200
    assert _store().get_job_overrides(project_id) == {}
    assert _names(client, project_id)["a.sas"] == "job_a"

    client.patch(url, json={"job_name": "otro"})
    assert client.patch(url, json={"job_name": ""}).status_code == 200
    assert _store().get_job_overrides(project_id) == {}


def test_rename_rejects_invalid_and_duplicate_names(client):
    project_id = _two_jobs(client)
    url = f"/api/projects/{project_id}/plans/a.sas/meta"

    invalid = client.patch(url, json={"job_name": "2abc"})
    duplicate = client.patch(url, json={"job_name": "JOB_B"})

    assert invalid.status_code == 422
    assert duplicate.status_code == 422
    assert "Ya existe otro Job con ese nombre." in duplicate.text
    assert _names(client, project_id) == {"a.sas": "job_a", "b.sas": "job_b"}
    assert _store().get_job_overrides(project_id) == {}


def test_rename_after_studio_creation_warns(client):
    project_id = _two_jobs(client)
    _store().save_talend_apply_state(
        project_id,
        "a.sas",
        revision_hash="old",
        status="applied",
        identity={"job_name": "job_a"},
        result={},
    )

    response = client.patch(f"/api/projects/{project_id}/plans/a.sas/meta", json={"job_name": "mi_job"})

    assert response.status_code == 200, response.text
    assert response.json()["warnings"] == [
        (
            "Este Job ya se creó en Talend Studio con el nombre anterior (job_a). "
            "El portal no lo renombra en Studio: ese Job se conserva con el nombre anterior y la próxima "
            "aplicación puede pedir confirmar la nueva revisión."
        )
    ]


def test_description_change_after_studio_creation_warns_only_when_it_changes(client):
    project_id = _two_jobs(client)
    _store().save_talend_apply_state(
        project_id, "a.sas", revision_hash="old", status="applied", identity={"job_name": "job_a"}, result={}
    )
    url = f"/api/projects/{project_id}/plans/a.sas/meta"

    changed = client.patch(url, json={"description": "Carga diaria"})
    unchanged = client.patch(url, json={"description": "Carga diaria"})
    other_job = client.patch(f"/api/projects/{project_id}/plans/b.sas/meta", json={"description": "x"})

    assert changed.json()["warnings"] == [
        (
            "Este Job ya se creó en Talend Studio; el cambio de descripción no se refleja allí hasta volver "
            "a aplicar y la aplicación puede pedir confirmar la nueva revisión."
        )
    ]
    assert unchanged.json()["warnings"] == []
    assert other_job.json()["warnings"] == []


def test_description_is_saved_and_sent_to_studio(client):
    project_id = _two_jobs(client)
    url = f"/api/projects/{project_id}/plans/a.sas/meta"

    response = client.patch(url, json={"description": "Carga diaria"})
    assert response.status_code == 200, response.text
    assert response.json()["plan"]["description"] == "Carga diaria"

    preview = client.post(f"/api/projects/{project_id}/plans/a.sas/talend-apply/preview").json()
    assert preview["arguments"]["description"] == "Carga diaria"

    too_long = client.patch(url, json={"description": "x" * 501})
    assert too_long.status_code == 422


def test_edits_are_blocked_while_a_batch_runs(client):
    project_id = _two_jobs(client)
    store = _store()
    store.begin_talend_apply_batch(project_id, "rev", ["a.sas", "b.sas"])
    store.update_talend_apply_batch_state(
        project_id, status="running", jobs=[], current_program="a.sas", completed_count=0
    )
    expected = "No se puede editar mientras Talend crea Jobs de este proyecto."

    meta = client.patch(f"/api/projects/{project_id}/plans/a.sas/meta", json={"job_name": "mi_job"})
    rename = client.post(
        f"/api/projects/{project_id}/plans/rename", json={"renames": [{"program": "a.sas", "job_name": "x1"}]}
    )
    expr = client.patch(
        f"/api/projects/{project_id}/plans/a.sas/steps/s1/expressions/0", json={"talend": "input_row.x"}
    )
    preview = client.post(f"/api/projects/{project_id}/plans/rename-preview", json={"mode": "prefix", "text": "p_"})

    assert [meta.status_code, rename.status_code, expr.status_code] == [409, 409, 409]
    assert meta.json()["detail"] == rename.json()["detail"] == expr.json()["detail"] == expected
    assert preview.status_code == 200
    assert store.get_job_overrides(project_id) == {}
    assert store.get_expression_overrides(project_id) == {}


def test_bulk_preview_and_apply_are_all_or_nothing(client):
    project_id = _two_jobs(client)
    base = f"/api/projects/{project_id}/plans"

    preview = client.post(f"{base}/rename-preview", json={"mode": "prefix", "text": "x_"})
    assert preview.status_code == 200, preview.text
    assert {row["program"]: row["proposed"] for row in preview.json()} == {"a.sas": "x_job_a", "b.sas": "x_job_b"}
    assert all(row["error"] is None for row in preview.json())

    bad = client.post(
        f"{base}/rename",
        json={"renames": [{"program": "a.sas", "job_name": "x_job_a"}, {"program": "b.sas", "job_name": "9bad"}]},
    )
    assert bad.status_code == 422
    assert _names(client, project_id) == {"a.sas": "job_a", "b.sas": "job_b"}

    good = client.post(
        f"{base}/rename",
        json={"renames": [{"program": "a.sas", "job_name": "x_job_a"}, {"program": "b.sas", "job_name": "x_job_b"}]},
    )
    assert good.status_code == 200, good.text
    assert good.json() == {"renamed": 2, "warnings": []}
    assert _names(client, project_id) == {"a.sas": "x_job_a", "b.sas": "x_job_b"}

    swap = client.post(
        f"{base}/rename",
        json={"renames": [{"program": "a.sas", "job_name": "job_b"}, {"program": "b.sas", "job_name": "job_a"}]},
    )
    # Un Job no puede tomar el nombre generado de otro: la superposición lo descartaría en silencio.
    assert swap.status_code == 422
    assert "Ya existe otro Job con ese nombre." in swap.text
    assert _names(client, project_id) == {"a.sas": "x_job_a", "b.sas": "x_job_b"}

    unknown = client.post(f"{base}/rename", json={"renames": [{"program": "nope.sas", "job_name": "zz"}]})
    assert unknown.status_code == 404

    bad_rule = client.post(f"{base}/rename-preview", json={"mode": "regex", "find": "("})
    assert bad_rule.status_code == 422
    complex_rule = client.post(
        f"{base}/rename-preview", json={"mode": "regex", "find": "(a+)+$", "replace_with": "x"}
    )
    assert complex_rule.status_code == 422
    assert complex_rule.json()["detail"] == "El patrón es demasiado complejo."


def test_bulk_rename_after_studio_creation_warns_only_for_created_jobs(client):
    project_id = _two_jobs(client)
    _store().save_talend_apply_state(
        project_id,
        "a.sas",
        revision_hash="old",
        status="applied",
        identity={"job_name": "job_a"},
        result={},
    )

    response = client.post(
        f"/api/projects/{project_id}/plans/rename",
        json={
            "renames": [
                {"program": "a.sas", "job_name": "x_job_a"},
                {"program": "b.sas", "job_name": "x_job_b"},
            ]
        },
    )

    assert response.status_code == 200, response.text
    assert response.json()["renamed"] == 2
    assert response.json()["warnings"] == [
        (
            "Este Job ya se creó en Talend Studio con el nombre anterior (job_a). "
            "El portal no lo renombra en Studio: ese Job se conserva con el nombre anterior y la próxima "
            "aplicación puede pedir confirmar la nueva revisión."
        )
    ]


def test_bulk_rename_of_a_never_applied_job_has_no_warnings(client):
    project_id = _two_jobs(client)

    response = client.post(
        f"/api/projects/{project_id}/plans/rename",
        json={"renames": [{"program": "a.sas", "job_name": "x_job_a"}]},
    )

    assert response.status_code == 200, response.text
    assert response.json() == {"renamed": 1, "warnings": []}


def test_bulk_regex_with_catastrophic_pattern_is_rejected_with_422(client):
    project_id = _two_jobs(client)

    response = client.post(
        f"/api/projects/{project_id}/plans/rename-preview",
        json={"mode": "regex", "find": "(a|aa)+$", "replace_with": "x"},
    )

    assert response.status_code == 422
    assert response.json()["detail"] == "El patrón es demasiado complejo."


def test_expression_edit_round_trip(client):
    project_id = project_with_plans(client, "Expr", [_plan_with_expression("pending")])
    url = f"/api/projects/{project_id}/plans/calc.sas/steps/calc-1/expressions"

    edited = client.patch(f"{url}/0", json={"talend": "input_row.x > 1"})
    assert edited.status_code == 200, edited.text
    expression = edited.json()["steps"][0]["expressions"][0]
    assert expression["talend"] == "input_row.x > 1"
    assert expression["talend_edited"] is True

    restored = client.patch(f"{url}/0", json={"talend": None})
    assert restored.status_code == 200, restored.text
    expression = restored.json()["steps"][0]["expressions"][0]
    assert expression["talend"] == "(input_row.x + 1)"
    assert expression["talend_edited"] is False

    assert client.patch(f"{url}/99", json={"talend": "a"}).status_code == 404
    assert client.patch(f"{url}/-1", json={"talend": "a"}).status_code == 404
    assert client.patch(f"{url}/0", json={"talend": "x" * 2001}).status_code == 422
    assert client.patch(f"{url}/0", json={"talend": ""}).status_code == 422
    assert client.patch(f"{url}/0", json={"talend": "a\nb"}).status_code == 422
    unknown_step = client.patch(
        f"/api/projects/{project_id}/plans/calc.sas/steps/nope/expressions/0", json={"talend": "a"}
    )
    assert unknown_step.status_code == 404


def test_translator_endpoint_handles_hostile_input(client):
    assert client.post("/api/translator/translate", json={"sas": ""}).status_code == 422
    assert client.post("/api/translator/translate", json={"sas": "x" * 20001}).status_code == 422

    unterminated = client.post("/api/translator/translate", json={"sas": "x = 'abc"})
    assert unterminated.status_code == 200
    assert unterminated.json()["talend"] is None
    assert unterminated.json()["warnings"]

    unsupported = client.post("/api/translator/translate", json={"sas": "lag(x)"})
    assert unsupported.status_code == 200
    assert unsupported.json()["supported"] is False
    assert unsupported.json()["talend_engine_enabled"] is False

    nested = client.post("/api/translator/translate", json={"sas": "(" * 3000})
    assert nested.status_code == 200
    assert nested.json()["talend"] is None and nested.json()["warnings"]

    supported = client.post("/api/translator/translate", json={"sas": "upcase(nome) = 'A'"})
    assert supported.status_code == 200
    body = supported.json()
    assert body["supported"] is True
    assert body["talend"] == 'input_row.nome.toUpperCase().equals("A")'
    assert body["columns"] == ["nome"]
    assert body["engine"] == "inline"
    assert body["sas"] == "upcase(nome) = 'A'"


def test_translator_failure_is_logged_and_still_answers_200(client, monkeypatch, caplog):
    def boom(_sas):
        raise RuntimeError("fallo interno del traductor")

    monkeypatch.setattr(api_module, "translate", boom)

    with caplog.at_level("ERROR", logger="apps.api.main"):
        response = client.post("/api/translator/translate", json={"sas": "upcase(nome)"})

    assert response.status_code == 200
    assert response.json()["talend"] is None
    assert any(record.levelname == "ERROR" and record.exc_info for record in caplog.records)


def test_naming_settings_validate_and_apply_on_regenerate(client):
    current = client.get("/api/settings/naming")
    assert current.status_code == 200
    assert current.json()["template"] == current.json()["default"] == "job_{programa}"
    assert current.json()["tokens"] == ["proyecto", "carpeta", "programa"]

    assert client.patch("/api/settings/naming", json={"template": "{proyecto}"}).status_code == 422
    assert client.get("/api/settings/naming").json()["template"] == "job_{programa}"

    saved = client.patch("/api/settings/naming", json={"template": "{proyecto}_{programa}"})
    assert saved.status_code == 200
    assert saved.json()["template"] == "{proyecto}_{programa}"

    example = client.get("/api/settings/naming/example", params={"template": "{proyecto}_{programa}"})
    assert example.json() == {"example": "finanzas_cod2", "error": None}
    invalid = client.get("/api/settings/naming/example", params={"template": "{x}"})
    assert invalid.status_code == 200
    assert invalid.json()["example"] is None
    assert "Token desconocido" in invalid.json()["error"]
    assert client.get("/api/settings/naming/example").json()["example"] == "finanzas_cod2"


def test_verify_does_not_bake_edits_into_plans_json(client, monkeypatch):
    project_id = _two_jobs(client)
    monkeypatch.setattr(api_module, "_talend", lambda: FakeTalend())
    client.patch(f"/api/projects/{project_id}/plans/a.sas/meta", json={"job_name": "mi_job"})

    response = client.post(f"/api/projects/{project_id}/plans/verify", json={"job_paths": []})

    assert response.status_code == 200, response.text
    raw = json.loads(_store().plans_path(project_id).read_text(encoding="utf-8"))
    assert {plan["program"]: plan["job_name"] for plan in raw["plans"]} == {"a.sas": "job_a", "b.sas": "job_b"}
    assert _names(client, project_id)["a.sas"] == "mi_job"


def test_new_routes_are_not_swallowed_by_greedy_program_paths(client):
    project_id = project_with_plans(
        client,
        "Nested",
        [make_plan("pending", "lz/sub/cod.sas", "job_cod"), _plan_with_expression("pending")],
    )

    meta = client.patch(f"/api/projects/{project_id}/plans/lz/sub/cod.sas/meta", json={"description": "d"})
    assert meta.status_code == 200, meta.text
    assert meta.json()["plan"]["program"] == "lz/sub/cod.sas"
    assert client.patch(f"/api/projects/{project_id}/plans/zzz.sas/meta", json={"description": "d"}).status_code == 404
    assert client.post(f"/api/projects/{project_id}/plans/rename-preview", json={"mode": "prefix", "text": "p"}).status_code == 200
    assert client.get("/api/projects/missing/plans/a.sas/meta").status_code in (404, 405)
    assert client.patch("/api/projects/missing/plans/a.sas/meta", json={"description": "d"}).status_code == 404
