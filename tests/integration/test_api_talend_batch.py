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
    async def custom_spec_status(self):
        return {"spec_supported": True, "spec_error": None}

    def __init__(
        self,
        *,
        failures: set[str] | None = None,
        conflicts: set[str] | None = None,
        warnings: set[str] | None = None,
        job_inventory: list[dict] | None = None,
        inventory_error: Exception | None = None,
    ):
        self.failures = failures or set()
        self.conflicts = conflicts or set()
        self.warning_programs = warnings or set()
        self.calls: list[dict] = []
        self.last_arguments: dict | None = None
        self.inspection_job_names: list[str] = []
        self.job_inventory = job_inventory or []
        self.inventory_error = inventory_error

    async def list_jobs(self) -> list[dict]:
        if self.inventory_error is not None:
            raise self.inventory_error
        return self.job_inventory

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

    async def inspect_job(self, job_path: str):
        from sas_grid_migrator.talend_adapter.adapter import ComponentRef, JobInspection

        names = [
            component.get("uniqueName", "")
            for component in (self.last_arguments or {}).get("components", [])
        ]
        self.inspection_job_names.append(job_path)
        return JobInspection(
            job_path=job_path,
            components=[
                ComponentRef(unique_name=name, component="tComponent", parameters=[])
                for name in names
                if name
            ],
            connections=0,
            contexts=[],
        )

    async def job_problems(self, job_name: str) -> dict:
        return {"clean": True, "problems": []}

    async def apply_custom_spec(self, arguments: dict) -> dict:
        self.calls.append(arguments)
        self.last_arguments = arguments
        source = arguments["instructions"]["source"]["program"]
        if source in self.conflicts:
            from sas_grid_migrator.talend_adapter.adapter import TalendError

            raise TalendError(f"ALREADY_EXISTS: target for {source}")
        if source in self.failures:
            from sas_grid_migrator.talend_adapter.adapter import TalendError

            raise TalendError(f"Bridge error for {source}")
        result = self._result(arguments)
        self.job_inventory.append({"name": arguments["jobName"], "path": result["itemPath"]})
        return result


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


def test_batch_summary_reports_totals_and_human_review(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Summary",
            [_plan("x", "alpha.sas", "job_alpha"), _plan("x", "beta.sas", "job_beta")],
        )
        summary = client.get(f"/api/projects/{project_id}/talend-apply-batch/summary")

    assert summary.status_code == 200, summary.text
    body = summary.json()
    assert body["total_jobs"] == 2
    assert [item["program"] for item in body["programs"]] == ["alpha.sas", "beta.sas"]
    assert body["total_contexts"] == sum(item["contexts"] for item in body["programs"])
    assert body["destination_root"].startswith("Process/")
    for item in body["programs"]:
        assert item["job_name"]
        assert item["folder_path"]
        assert isinstance(item["draft_components"], list)
        assert isinstance(item["pending"], list)


def test_batch_persists_each_phase_while_running_and_clears_it(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    phases: list[tuple[str, str | None]] = []

    class PhaseRecorder(FakeTalend):
        project_id: str = ""

        def _running_phase(self) -> str | None:
            state = api_module.store().get_talend_apply_batch_state(self.project_id)
            running = next((item for item in state["jobs"] if item["status"] == "running"), None)
            return running.get("phase") if running else None

        async def apply_custom_spec(self, arguments: dict) -> dict:
            phases.append(("apply", self._running_phase()))
            return await super().apply_custom_spec(arguments)

        async def job_problems(self, job_name: str) -> dict:
            phases.append(("problems", self._running_phase()))
            return await super().job_problems(job_name)

    fake = PhaseRecorder()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Phases",
            [_plan("x", "alpha.sas", "job_alpha"), _plan("x", "beta.sas", "job_beta")],
        )
        fake.project_id = project_id
        start = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        assert start.status_code == 202, start.text
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert phases == [
        ("apply", "applying"),
        ("problems", "inspecting"),
        ("apply", "applying"),
        ("problems", "inspecting"),
    ]
    assert [job["phase"] for job in state["jobs"]] == [None, None]


def test_preflight_uses_project_destination_and_dependency_order_without_mcp(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)

    def no_mcp():
        raise AssertionError("A preview must not contact or modify Talend Studio")

    monkeypatch.setattr(api_module, "_talend", no_mcp)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Preflight",
            [_plan("x", "first.sas", "job_first"), _plan("x", "last.sas", "job_last")],
            [["last.sas"], ["first.sas"]],
            cycles=[["first.sas", "last.sas"]],
        )
        response = client.get(f"/api/projects/{project_id}/talend-apply-batch/summary")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 200, response.text
    body = response.json()
    assert project_id in body["destination_root"]
    assert [item["program"] for item in body["programs"]] == ["last.sas", "first.sas"]
    assert all(item["folder_path"].startswith(body["destination_root"]) for item in body["programs"])
    assert body["creatable_jobs"] == 2
    assert all(item["ready_for_creation"] for item in body["programs"])
    assert body["cycles"] == [["first.sas", "last.sas"]]
    assert state["status"] == "not_started"


def test_preflight_distinguishes_context_only_jobs_from_generated_components(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    plan = _plan("x", "manual.sas", "job_manual")
    plan.context_variables = []
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Manual only", [plan])
        response = client.get(f"/api/projects/{project_id}/talend-apply-batch/summary")

    assert response.status_code == 200, response.text
    item = response.json()["programs"][0]
    assert item["components"] == 0
    assert item["contexts"] == 1
    assert item["creation_kind"] == "context_only"


def test_batch_rejects_outdated_confirmation_before_any_mcp_write(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Confirmed preview", [_plan("x", "a.sas", "job_a")])
        summary = client.get(f"/api/projects/{project_id}/talend-apply-batch/summary").json()
        s = Store(Settings.from_env())
        plans = PlanSet.model_validate_json(s.plans_path(project_id).read_text(encoding="utf-8"))
        plans.plans[0].job_name = "job_updated"
        s.plans_path(project_id).write_text(plans.model_dump_json(), encoding="utf-8")

        stale = client.post(
            f"/api/projects/{project_id}/talend-apply-batch",
            json={"expected_revision": summary["revision_hash"]},
        )
        assert stale.status_code == 409, stale.text
        assert fake.calls == []
        assert client.get(f"/api/projects/{project_id}/talend-apply-batch").json()["status"] == "not_started"

        fresh = client.get(f"/api/projects/{project_id}/talend-apply-batch/summary").json()
        accepted = client.post(
            f"/api/projects/{project_id}/talend-apply-batch",
            json={"expected_revision": fresh["revision_hash"]},
        )
        assert accepted.status_code == 202, accepted.text
        assert len(fake.calls) == 1


def test_studio_problems_prevent_a_clean_application_status(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)

    class StudioProblems(FakeTalend):
        async def job_problems(self, job_name: str) -> dict:
            return {"clean": False, "problems": [{"severity": "ERROR", "message": "Missing schema"}]}

    monkeypatch.setattr(api_module, "_talend", lambda: StudioProblems())
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Studio issues", [_plan("x", "a.sas", "job_a")])
        result = client.post(f"/api/projects/{project_id}/plans/a.sas/talend-apply")

    assert result.status_code == 200, result.text
    assert result.json()["status"] == "partially_applied"
    assert any("Studio" in warning for warning in result.json()["warnings"])


def test_nested_draft_job_remains_pending_human_review_after_mcp_creation(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    child = _plan("x", "child.sas", "job_child")
    child.steps = [PlanStep(
        id="draft", order=1, subjob="default", action="add_component",
        component_candidate="tRowGenerator", purpose="Generar filas",
        pending=["Confirmar esquema"], evidence=Loc(file="child.sas", line=1, end_line=1),
    )]
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client, "Draft child", [_plan("x", "parent.sas", "job_parent", child_call=True), child],
            [["parent.sas"], ["child.sas"]],
        )
        client.post(f"/api/projects/{project_id}/talend-apply-batch")
        child_state = client.get(f"/api/projects/{project_id}/plans/child.sas/talend-apply").json()

    assert child_state["status"] == "applied"
    assert child_state["result"]["review_required"] is True
    assert any("borrador" in warning for warning in child_state["result"]["review_warnings"])


def test_incompatible_mcp_is_rejected_before_scheduling_a_batch(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)

    class LegacyMcp(FakeTalend):
        async def custom_spec_status(self):
            return {"spec_supported": False, "spec_error": "MCP incompatible: falta childJobs"}

    fake = LegacyMcp()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Legacy MCP", [_plan("x", "a.sas", "job_a")])
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()
    assert response.status_code == 409
    assert "incompatible" in response.json()["detail"]
    assert state["status"] == "not_started"
    assert fake.calls == []


def test_write_permission_is_configured_and_persisted_through_the_api(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "UI permissions", [_plan("x", "a.sas", "job_a")])
        blocked = client.patch("/api/integrations/talend/permissions", json={"write_enabled": False})
        assert blocked.status_code == 200, blocked.text
        assert client.post(f"/api/projects/{project_id}/talend-apply-batch").status_code == 403
        assert fake.calls == []
    with TestClient(api_module.app) as client:
        assert client.get("/api/integrations/talend/permissions").json()["write_enabled"] is False
        # La variable antigua no decide el permiso de la interfaz.
        monkeypatch.setenv("TALEND_MCP_READONLY", "true")
        allowed = client.patch("/api/integrations/talend/permissions", json={"write_enabled": True})
        assert allowed.json()["write_enabled"] is True
        assert client.post(f"/api/projects/{project_id}/talend-apply-batch").status_code == 202
        assert len(fake.calls) == 1


def test_batch_blocks_all_writes_when_preflight_finds_external_homonym(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(job_inventory=[
        {"name": "job_alpha", "path": "C:/Talend/PRJ/process/OtherProject/job_alpha/job_alpha_0.1.item"}
    ])
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Collision", [_plan("pending", "a.sas", "job_alpha")])

        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 409
    assert "conflicto" in response.json()["detail"].lower()
    assert fake.calls == []
    assert state["status"] == "not_started"


def test_batch_rechecks_stored_conflict_and_retries_after_job_disappears(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Removed collision", [_plan("pending", "a.sas", "job_alpha")])
        ordered, specs, revision_hash = api_module._talend_batch_bundle(project_id)
        program = ordered[0].program
        store = Store(Settings.from_env())
        _batch, _started = store.begin_talend_apply_batch(project_id, revision_hash, [program])
        store.update_talend_apply_batch_state(
            project_id,
            status="conflict",
            jobs=[{"program": program, "status": "conflict", "result": None, "error": "old collision"}],
            current_program=None,
            completed_count=1,
        )
        spec = specs[program]
        identity = {
            "project_id": spec.project_id,
            "program": spec.program,
            "source_sha256": spec.source_sha256,
            "rules_version": spec.rules_version,
            "job_name": spec.job_name,
            "folder_path": spec.folder_path,
        }
        store.save_talend_apply_state(
            project_id,
            program,
            revision_hash=api_module._talend_apply_preview_id(spec),
            status="conflict",
            identity=identity,
            error="old collision",
        )

        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202
    assert state["status"] == "applied"
    assert state["attempt_count"] == 2
    assert len(fake.calls) == 1


def test_batch_recreates_a_deleted_job_without_reapplying_other_completed_jobs(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Restore missing Job",
            [
                _plan("pending", "present.sas", "job_present"),
                _plan("pending", "deleted.sas", "job_deleted"),
            ],
            [["present.sas"], ["deleted.sas"]],
        )
        ordered, specs, revision_hash = api_module._talend_batch_bundle(project_id)
        programs = [plan.program for plan in ordered]
        store = Store(Settings.from_env())
        store.begin_talend_apply_batch(project_id, revision_hash, programs)
        completed_jobs = []
        for program in programs:
            spec = specs[program]
            identity = {
                "project_id": spec.project_id,
                "program": spec.program,
                "source_sha256": spec.source_sha256,
                "rules_version": spec.rules_version,
                "job_name": spec.job_name,
                "folder_path": spec.folder_path,
            }
            result = {"status": "applied", "identity": identity, "result": {"itemPath": f"old/{spec.job_name}.item"}}
            store.save_talend_apply_state(
                project_id,
                program,
                revision_hash=api_module._talend_apply_preview_id(spec),
                status="applied",
                identity=identity,
                result=result,
            )
            completed_jobs.append({"program": program, "status": "applied", "result": result, "error": None})
        store.update_talend_apply_batch_state(
            project_id,
            status="applied",
            jobs=completed_jobs,
            current_program=None,
            completed_count=len(completed_jobs),
        )

        result_folder = specs["present.sas"].folder_path.removeprefix("Process/")
        fake.job_inventory = [
            {
                "name": "job_present",
                "path": f"C:/Talend/PRJ/process/{result_folder}/job_present/job_present_0.1.item",
            }
        ]
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202
    assert [call["instructions"]["source"]["program"] for call in fake.calls] == ["deleted.sas"]
    assert state["status"] == "applied"
    assert state["jobs"][0]["status"] == "applied"
    assert state["jobs"][1]["status"] == "applied"


def test_batch_rejects_plan_change_between_preflight_and_batch_snapshot(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    original_preflight = api_module._talend_batch_preflight

    async def stale_preflight(project_id: str) -> dict:
        result = await original_preflight(project_id)
        result["revision_hash"] = "stale-revision"
        return result

    monkeypatch.setattr(api_module, "_talend_batch_preflight", stale_preflight)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Plan changed", [_plan("pending", "a.sas", "job_alpha")])

        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 409
    assert "cambió" in response.json()["detail"].lower()
    assert fake.calls == []
    assert state["status"] == "not_started"


def test_batch_updates_existing_job_in_exact_destination_folder(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Update in place", [_plan("pending", "a.sas", "job_alpha")])
        _ordered, specs, _revision = api_module._talend_batch_bundle(project_id)
        spec = specs["a.sas"]
        exact_folder = spec.folder_path.removeprefix("Process/")
        fake.job_inventory = [{
            "name": "job_alpha",
            "path": f"C:/Talend/PRJ/process/{exact_folder}/job_alpha/job_alpha_0.1.item",
        }]

        preflight = client.get(f"/api/projects/{project_id}/talend-apply-batch/preflight")
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")

    assert preflight.status_code == 200, preflight.text
    assert preflight.json()["update_count"] == 1
    assert preflight.json()["conflict_count"] == 0
    assert response.status_code == 202, response.text
    assert len(fake.calls) == 1
    assert fake.calls[0]["folderPath"].casefold() == spec.folder_path.casefold()


def test_preflight_classifies_exact_destination_missing_and_external_jobs(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Preflight actions",
            [
                _plan("pending", "update.sas", "job_update"),
                _plan("pending", "create.sas", "job_create"),
                _plan("pending", "conflict.sas", "job_conflict"),
            ],
        )
        _ordered, specs, _revision = api_module._talend_batch_bundle(project_id)
        exact_folder = specs["update.sas"].folder_path.removeprefix("Process/")
        fake.job_inventory = [
            {
                "name": "job_update",
                "path": f"C:/Talend/PRJ/process/{exact_folder}/job_update/job_update_0.1.item",
            },
            {
                "name": "job_conflict",
                "path": "C:/Talend/PRJ/process/OtherProject/job_conflict/job_conflict_0.1.item",
            },
        ]

        response = client.get(f"/api/projects/{project_id}/talend-apply-batch/preflight")

    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["available"] is True
    assert (payload["create_count"], payload["update_count"], payload["conflict_count"]) == (1, 1, 1)
    assert {item["program"]: item["action"] for item in payload["jobs"]} == {
        "update.sas": "update",
        "create.sas": "create",
        "conflict.sas": "conflict",
    }


def test_preflight_fails_closed_when_mcp_inventory_is_unavailable(tmp_path, monkeypatch):
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend(inventory_error=TalendError("MCP caído"))
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Offline preflight", [_plan("pending", "a.sas", "job_alpha")])

        response = client.get(f"/api/projects/{project_id}/talend-apply-batch/preflight")

    assert response.status_code == 502
    assert "mcp caído" in response.json()["detail"].lower()
