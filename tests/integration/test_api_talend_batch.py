from pathlib import Path

import apps.api.main as api_module
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import DependencyReport
from sas_grid_migrator.migration_planner.models import (
    ContextVariable,
    JobPlan,
    PlanSet,
    PlanStep,
    Property,
)
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.ast import Loc


def _plan(project_id: str, program: str, job_name: str, *, child_call: bool = False) -> JobPlan:
    steps = []
    if child_call:
        steps.append(
            PlanStep(
                id="call-child",
                order=1,
                subjob="default",
                action="add_component",
                operation_type="macro_call",
                component_candidate="tRunJob",
                purpose="Invocar Job hijo",
                properties=[
                    Property(name="PROCESS", value="%child", origin="SAS", verified=True),
                    Property(
                        name="CONTEXTPARAMS",
                        value="C:/sas/child.sas",
                        origin="SAS",
                        verified=True,
                    ),
                ],
                evidence=Loc(file=program, line=1, end_line=1),
                verified=True,
            )
        )
    return JobPlan(
        project_id=project_id,
        rules_version="rules-1",
        program=program,
        job_name=job_name,
        steps=steps,
        context_variables=[
            ContextVariable(
                name="range_id",
                sas_value=None,
                suggested="context.range_id",
                origin=f"{program}:1",
            )
        ],
    )


def _project_with_plans(
    client: TestClient,
    project_name: str,
    plans: list[JobPlan],
    processing_order: list[list[str]] | None = None,
    cycles: list[list[str]] | None = None,
) -> str:
    response = client.post("/api/projects", json={"name": project_name})
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]
    for plan in plans:
        plan.project_id = project_id
    store = Store(Settings.from_env())
    plan_path = store.plans_path(project_id)
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(
        PlanSet(project_id=project_id, rules_version="rules-1", plans=plans).model_dump_json(),
        encoding="utf-8",
    )
    dependencies_path = store.dependencies_path(project_id)
    dependencies_path.write_text(
        DependencyReport(
            project_id=project_id,
            processing_order=processing_order or [],
            cycles=cycles or [],
        ).model_dump_json(),
        encoding="utf-8",
    )
    return project_id


class FakeTalend:
    def __init__(
        self,
        *,
        failures: set[str] | None = None,
        conflicts: set[str] | None = None,
        warnings: set[str] | None = None,
    ):
        self.failures = failures or set()
        self.conflicts = conflicts or set()
        self.warning_programs = warnings or set()
        self.calls: list[dict] = []

    def _result(self, arguments: dict) -> dict:
        children = [self._result(child) for child in arguments.get("childJobs", [])]
        program = arguments["instructions"]["source"]["program"]
        return {
            "jobName": arguments["jobName"],
            "folderPath": arguments["folderPath"],
            "itemPath": f"{arguments['folderPath']}/{arguments['jobName']}_0.1.item",
            "reusedExisting": False,
            "generatedComponents": len(arguments["components"]),
            "reusedComponents": 0,
            "generatedConnections": len(arguments["connections"]),
            "reusedConnections": 0,
            "generatedContexts": len(arguments["contexts"]),
            "updatedContexts": 0,
            "reusedContexts": 0,
            "removedContexts": 0,
            "totalComponents": len(arguments["components"]),
            "connections": len(arguments["connections"]),
            "warnings": ["resultado parcial de prueba"] if program in self.warning_programs else [],
            "childJobs": children,
        }

    async def apply_custom_spec(self, arguments: dict) -> dict:
        self.calls.append(arguments)
        source = arguments["instructions"]["source"]["program"]
        if source in self.conflicts:
            from sas_grid_migrator.talend_adapter.adapter import TalendError

            raise TalendError(f"ALREADY_EXISTS: target for {source}")
        if source in self.failures:
            from sas_grid_migrator.talend_adapter.adapter import TalendError

            raise TalendError(f"Bridge error for {source}")
        return self._result(arguments)


def _set_env(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")


def test_batch_requires_plans_and_write_enabled_mcp(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    with TestClient(api_module.app) as client:
        empty = client.post("/api/projects", json={"name": "Empty"}).json()["id"]
        assert client.post(f"/api/projects/{empty}/talend-apply-batch").status_code == 409

        project_id = _project_with_plans(client, "Read only", [_plan("pending", "daily.sas", "daily")])
        monkeypatch.setenv("TALEND_MCP_READONLY", "true")
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")

    assert response.status_code == 403
    assert "solo lectura" in response.json()["detail"].lower()


def test_batch_orders_jobs_persists_progress_and_reuses_completed_batch(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Ordered",
            [
                _plan("pending", "alpha.sas", "job_alpha"),
                _plan("pending", "zeta.sas", "job_zeta"),
            ],
            [["zeta.sas"], ["alpha.sas"]],
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch")
        repeated = client.post(f"/api/projects/{project_id}/talend-apply-batch")

    assert response.status_code == 202, response.text
    assert [call["instructions"]["source"]["program"] for call in fake.calls] == [
        "zeta.sas",
        "alpha.sas",
    ]
    assert state.status_code == 200
    assert state.json()["status"] == "applied"
    assert state.json()["completed_jobs"] == state.json()["total_jobs"] == 2
    assert [job["status"] for job in state.json()["jobs"]] == ["applied", "applied"]
    assert repeated.json() == state.json()
    assert len(fake.calls) == 2


def test_batch_reports_cycles_without_failing_successful_job_creation(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Cycle",
            [_plan("pending", "a.sas", "job_a"), _plan("pending", "b.sas", "job_b")],
            [["a.sas", "b.sas"]],
            cycles=[["a.sas", "b.sas"]],
        )
        client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert state["status"] == "applied"
    assert len(state["warnings"]) == 1
    assert "ciclo" in state["warnings"][0].lower()
    assert "a.sas" in state["warnings"][0] and "b.sas" in state["warnings"][0]


def test_orchestrator_child_result_is_recorded_and_not_applied_again(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Nested",
            [
                _plan("pending", "orchestrator.sas", "job_orchestrator", child_call=True),
                _plan("pending", "child.sas", "job_child"),
            ],
            [["orchestrator.sas"], ["child.sas"]],
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()
        child_status = client.get(f"/api/projects/{project_id}/plans/child.sas/talend-apply")
        child_apply = client.post(f"/api/projects/{project_id}/plans/child.sas/talend-apply")

    assert response.status_code == 202, response.text
    assert len(fake.calls) == 1
    assert fake.calls[0]["instructions"]["source"]["program"] == "orchestrator.sas"
    child = next(job for job in state["jobs"] if job["program"] == "child.sas")
    assert child["status"] == "applied"
    assert child["result"]["result"]["itemPath"].endswith("job_child_0.1.item")
    assert state["completed_jobs"] == 2
    assert child_status.status_code == 200
    assert child_status.json()["status"] == "applied"
    assert child_apply.status_code == 200
    assert child_apply.json()["status"] == "applied"
    assert len(fake.calls) == 1


def test_recursive_parent_apply_rejects_child_with_a_different_saved_revision(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Changed child revision",
            [
                _plan("pending", "orchestrator.sas", "job_orchestrator", child_call=True),
                _plan("pending", "child.sas", "job_child"),
            ],
            [["orchestrator.sas"], ["child.sas"]],
        )
        _child_plan, child_spec = api_module._talend_apply_spec(project_id, "child.sas")
        child_identity = {
            "project_id": child_spec.project_id,
            "program": child_spec.program,
            "source_sha256": child_spec.source_sha256,
            "rules_version": child_spec.rules_version,
            "job_name": child_spec.job_name,
            "folder_path": child_spec.folder_path,
        }
        store = Store(Settings.from_env())
        store.save_talend_apply_state(
            project_id,
            "child.sas",
            revision_hash="older-child-revision",
            status="applied",
            identity=child_identity,
            result={"status": "applied", "identity": child_identity, "result": {"itemPath": "old"}},
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()
        child_state = store.get_talend_apply_state(project_id, "child.sas")

    assert response.status_code == 202
    assert fake.calls == []
    assert state["status"] == "conflict"
    assert [(job["program"], job["status"]) for job in state["jobs"]] == [
        ("orchestrator.sas", "conflict"),
        ("child.sas", "conflict"),
    ]
    assert child_state is not None
    assert child_state["revision_hash"] == "older-child-revision"
    assert child_state["result"]["result"]["itemPath"] == "old"


def test_partial_child_job_is_retried_without_reapplying_completed_parent(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(warnings={"child.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Retry partial child",
            [
                _plan("pending", "orchestrator.sas", "job_orchestrator", child_call=True),
                _plan("pending", "child.sas", "job_child"),
            ],
            [["orchestrator.sas"], ["child.sas"]],
        )
        first = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        first_state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()
        fake.warning_programs.clear()
        second = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        second_state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert first.status_code == 202
    assert first_state["status"] == "partially_applied"
    assert [(job["program"], job["status"]) for job in first_state["jobs"]] == [
        ("orchestrator.sas", "applied"),
        ("child.sas", "partially_applied"),
    ]
    assert second.status_code == 202
    assert second_state["status"] == "applied"
    assert [(call["instructions"]["source"]["program"]) for call in fake.calls] == [
        "orchestrator.sas",
        "child.sas",
    ]


def test_direct_apply_with_warnings_is_consistently_partial(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(warnings={"daily.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Warned", [_plan("pending", "daily.sas", "job_daily")])
        result = client.post(f"/api/projects/{project_id}/plans/daily.sas/talend-apply")
        stored = client.get(f"/api/projects/{project_id}/plans/daily.sas/talend-apply")

    assert result.status_code == 200
    assert result.json()["status"] == "partially_applied"
    assert stored.json()["status"] == "partially_applied"
    assert result.json()["warnings"] == ["resultado parcial de prueba"]


def test_batch_continues_after_one_job_fails_and_reports_each_outcome(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(failures={"a.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Partial",
            [_plan("pending", "a.sas", "job_a"), _plan("pending", "b.sas", "job_b")],
            [["a.sas"], ["b.sas"]],
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202, response.text
    assert [call["instructions"]["source"]["program"] for call in fake.calls] == ["a.sas", "b.sas"]
    assert state["status"] == "partially_applied"
    assert [(job["program"], job["status"]) for job in state["jobs"]] == [
        ("a.sas", "failed"),
        ("b.sas", "applied"),
    ]
    assert "Bridge error" in state["jobs"][0]["error"]


def test_failed_orchestrator_does_not_mark_unconfirmed_child_as_created(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(failures={"orchestrator.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Unconfirmed child",
            [
                _plan("pending", "orchestrator.sas", "job_orchestrator", child_call=True),
                _plan("pending", "child.sas", "job_child"),
            ],
            [["orchestrator.sas"], ["child.sas"]],
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202
    assert [call["instructions"]["source"]["program"] for call in fake.calls] == [
        "orchestrator.sas",
        "child.sas",
    ]
    assert [(item["program"], item["status"]) for item in state["jobs"]] == [
        ("orchestrator.sas", "failed"),
        ("child.sas", "applied"),
    ]
    assert state["status"] == "partially_applied"


def test_child_matching_uses_folder_when_job_names_repeat(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Repeated Job name",
            [
                _plan("pending", "orchestrator.sas", "job_orchestrator", child_call=True),
                _plan("pending", "folder-a/child.sas", "job_shared"),
                _plan("pending", "folder-b/other.sas", "job_shared"),
            ],
            [["orchestrator.sas"], ["folder-a/child.sas", "folder-b/other.sas"]],
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202
    assert [call["instructions"]["source"]["program"] for call in fake.calls] == [
        "orchestrator.sas",
        "folder-b/other.sas",
    ]
    repeated_name_jobs = [item for item in state["jobs"] if item["program"].endswith("child.sas") or item["program"].endswith("other.sas")]
    assert len(repeated_name_jobs) == 2
    assert all(item["status"] == "applied" for item in repeated_name_jobs)
    child = next(item for item in repeated_name_jobs if item["program"].endswith("child.sas"))
    assert "folder-a" in child["result"]["result"]["itemPath"]


def test_all_job_failures_produce_a_failed_batch_with_each_error(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(failures={"first.sas", "second.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "All failures",
            [_plan("pending", "first.sas", "job_first"), _plan("pending", "second.sas", "job_second")],
            [["first.sas"], ["second.sas"]],
        )
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202
    assert state["status"] == "failed"
    assert [item["status"] for item in state["jobs"]] == ["failed", "failed"]
    assert all("Bridge error" in item["error"] for item in state["jobs"])


def test_mcp_destination_conflict_is_reported_as_conflict_and_batch_continues(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(conflicts={"first.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "One destination conflict",
            [_plan("pending", "first.sas", "job_first"), _plan("pending", "second.sas", "job_second")],
            [["first.sas"], ["second.sas"]],
        )
        client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert state["status"] == "partially_applied"
    assert [(item["program"], item["status"]) for item in state["jobs"]] == [
        ("first.sas", "conflict"),
        ("second.sas", "applied"),
    ]


def test_batch_stops_if_project_plan_changes_mid_run(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Changed while running",
            [_plan("pending", "a.sas", "job_a"), _plan("pending", "b.sas", "job_b")],
            [["a.sas"], ["b.sas"]],
        )
        original_apply = fake.apply_custom_spec

        async def apply_then_change(arguments: dict) -> dict:
            result = await original_apply(arguments)
            if arguments["instructions"]["source"]["program"] == "a.sas":
                store = Store(Settings.from_env())
                plans = PlanSet.model_validate_json(store.plans_path(project_id).read_text(encoding="utf-8"))
                plans.plans[1].job_name = "changed_job_b"
                store.plans_path(project_id).write_text(plans.model_dump_json(), encoding="utf-8")
            return result

        fake.apply_custom_spec = apply_then_change
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202
    assert [call["instructions"]["source"]["program"] for call in fake.calls] == ["a.sas"]
    assert state["status"] == "conflict"
    assert state["jobs"][0]["status"] == "applied"
    assert state["jobs"][1]["status"] == "conflict"


def test_batch_retries_failures_but_conflicts_after_plan_revision_changes(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(failures={"a.sas"})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Retry", [_plan("pending", "a.sas", "job_a")])
        first = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        fake.failures.clear()
        second = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

        store = Store(Settings.from_env())
        plans = PlanSet.model_validate_json(store.plans_path(project_id).read_text(encoding="utf-8"))
        plans.plans[0].job_name = "job_changed"
        store.plans_path(project_id).write_text(plans.model_dump_json(), encoding="utf-8")
        conflict = client.post(f"/api/projects/{project_id}/talend-apply-batch")

    assert first.status_code == second.status_code == 202
    assert state["status"] == "applied"
    assert len(fake.calls) == 2
    assert conflict.status_code == 409
    assert "revisión" in conflict.json()["detail"].lower()
    assert len(fake.calls) == 2


def test_batch_state_is_scoped_to_project(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        first = _project_with_plans(client, "First", [_plan("pending", "a.sas", "job_a")])
        second = _project_with_plans(client, "Second", [_plan("pending", "a.sas", "job_a")])
        client.post(f"/api/projects/{first}/talend-apply-batch")
        second_state = client.get(f"/api/projects/{second}/talend-apply-batch")

    assert second_state.status_code == 200
    assert second_state.json()["status"] == "not_started"
    assert second_state.json()["jobs"] == []
