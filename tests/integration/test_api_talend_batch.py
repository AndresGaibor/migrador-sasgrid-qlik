from pathlib import Path

import apps.api.main as api_module
from fastapi.testclient import TestClient

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import DependencyReport
from sas_grid_migrator.migration_planner.models import (
    ContextVariable,
    Expression,
    JobPlan,
    PlanSet,
    PlanStep,
    Property,
    SchemaColumn,
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
        self.arguments_by_path: dict[str, dict] = {}
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
        result = {
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
        self.arguments_by_path[result["itemPath"]] = arguments
        return result

    async def inspect_job(self, job_path: str):
        from sas_grid_migrator.talend_adapter.adapter import ComponentRef, JobInspection

        arguments = self.arguments_by_path.get(job_path, self.last_arguments or {})
        self.inspection_job_names.append(job_path)
        components = [
            ComponentRef(
                unique_name=component.get("uniqueName", ""),
                component=component.get("componentName", ""),
                parameters=sorted((parameters := component.get("parameters") or {}).keys()),
                parameter_values=parameters,
                schemas=[component["schema"]] if component.get("schema") else [],
            )
            for component in arguments.get("components", [])
        ]
        mapper_entries = [
            {
                "componentUniqueName": component["uniqueName"],
                "table": table["name"],
                "name": column["name"],
                "expression": column["expression"],
                "type": column["type"],
                "nullable": column.get("nullable"),
            }
            for component in arguments.get("components", [])
            for table in (component.get("mapper") or {}).get("outputs", [])
            for column in table.get("columns", [])
        ]
        return JobInspection(
            job_path=job_path,
            components=components,
            connections=len(arguments.get("connections", [])),
            connection_details=arguments.get("connections", []),
            contexts=[],
            mapper_entries=mapper_entries,
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
        permission = client.patch("/api/integrations/talend/permissions", json={"write_enabled": False})
        assert permission.status_code == 200
        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")

    assert response.status_code == 403
    assert "Configuración" in response.json()["detail"]


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


def test_apply_reads_back_component_schema_and_connections_and_can_reverify(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)

    class ReadbackTalend(FakeTalend):
        def __init__(self):
            super().__init__()
            self.bad_schema = False
            self.aliases: dict[str, str] = {}

        async def apply_custom_spec(self, arguments: dict) -> dict:
            result = await super().apply_custom_spec(arguments)
            self.aliases = {
                component["uniqueName"]: f"{component['uniqueName']}_studio"
                for component in arguments.get("components", [])
            }
            result["componentAliases"] = self.aliases
            return result

        async def inspect_job(self, job_path: str):
            from sas_grid_migrator.talend_adapter.adapter import ComponentRef, JobInspection

            arguments = self.last_arguments or {}
            components = []
            for component in arguments.get("components", []):
                schema = component.get("schema")
                if schema and self.bad_schema and component["componentName"] == "tFileOutputDelimited":
                    schema = {**schema, "columns": [{**schema["columns"][0], "name": "tampered"}]}
                components.append(ComponentRef(
                    unique_name=self.aliases.get(component["uniqueName"], component["uniqueName"]),
                    component=component["componentName"],
                    parameters=sorted(component.get("parameters", {})),
                    parameter_values=component.get("parameters", {}),
                    schemas=[schema] if schema else [],
                ))
            mapper_entries = [
                {
                    "componentUniqueName": self.aliases.get(component["uniqueName"], component["uniqueName"]),
                    "table": table["name"],
                    "name": column["name"],
                    "expression": column["expression"],
                    "type": column["type"],
                    "nullable": column.get("nullable"),
                }
                for component in arguments.get("components", [])
                for table in (component.get("mapper") or {}).get("outputs", [])
                for column in table.get("columns", [])
            ]
            connections = [
                {
                    **connection,
                    "source": self.aliases.get(connection["source"], connection["source"]),
                    "target": self.aliases.get(connection["target"], connection["target"]),
                }
                for connection in arguments.get("connections", [])
            ]
            return JobInspection(
                job_path=job_path,
                components=components,
                connections=len(arguments.get("connections", [])),
                connection_details=connections,
                contexts=[],
                mapper_entries=mapper_entries,
            )

    source = PlanStep(
        id="read_accounts", order=1, subjob="main", action="add_component",
        operation_type="read_file", component_candidate="tFileInputDelimited",
        purpose="Leer cuentas", properties=[Property(name="HEADER", value="1", origin="test", verified=True)],
        schema_columns=[SchemaColumn(name="amount", talend_type="id_BigDecimal", nullable=False)],
        evidence=Loc(file="daily.sas", line=1, end_line=1), verified=True,
    )
    mapping = PlanStep(
        id="compute_fee", order=2, subjob="main", action="add_component",
        operation_type="compute", component_candidate="tMap", purpose="Calcular comisión",
        connections=[{"type": "Main", "from_step": "read_accounts"}],
        expressions=[Expression(sas="amount * 0.005", talend="(input_row.amount * 0.005)", target="service_fee", line=2, requires_semantic_validation=False)],
        schema_columns=[
            SchemaColumn(name="amount", talend_type="id_BigDecimal", nullable=False),
            SchemaColumn(name="service_fee", talend_type="id_BigDecimal", nullable=False),
        ],
        evidence=Loc(file="daily.sas", line=2, end_line=2),
    )
    target = PlanStep(
        id="write_accounts", order=3, subjob="main", action="add_component",
        operation_type="write_file", component_candidate="tFileOutputDelimited",
        purpose="Escribir cuentas", properties=[Property(name="ROWSEPARATOR", value="\\n", origin="test", verified=True)],
        schema_columns=[SchemaColumn(name="amount", talend_type="id_BigDecimal", nullable=False), SchemaColumn(name="service_fee", talend_type="id_BigDecimal", nullable=False)],
        connections=[{"type": "Main", "from_step": "compute_fee"}],
        evidence=Loc(file="daily.sas", line=3, end_line=3), verified=True,
    )
    migration = JobPlan(
        project_id="pending", rules_version="rules-1", program="daily.sas",
        job_name="job_daily", steps=[source, mapping, target],
    )
    fake = ReadbackTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Readback", [migration])
        applied = client.post(f"/api/projects/{project_id}/plans/daily.sas/talend-apply")
        plan = client.get(f"/api/projects/{project_id}/plans/daily.sas")
        rows = client.get(f"/api/projects/{project_id}/plans")
        fake.bad_schema = True
        checked_again = client.post(f"/api/projects/{project_id}/plans/daily.sas/talend-apply/verify")
        updated_plan = client.get(f"/api/projects/{project_id}/plans/daily.sas")
        updated_rows = client.get(f"/api/projects/{project_id}/plans")

    assert applied.status_code == 200, applied.text
    assert applied.json()["verification"]["configured_steps"] == 3
    assert applied.json()["verification"]["pending_steps"] == 0
    assert applied.json()["verification"]["steps"][1]["checks"]["mapper"]["status"] == "verified"
    assert applied.json()["verification"]["steps"][0]["studio_unique_name"].endswith("_studio")
    assert [item["studio_verification"]["status"] for item in plan.json()["steps"]] == ["verified", "verified", "verified"]
    assert rows.json()[0]["studio_verified"] == 3
    assert rows.json()[0]["done"] == 0  # la comprobación de Studio no modifica el avance manual
    assert checked_again.status_code == 200, checked_again.text
    assert checked_again.json()["verification"]["configured_steps"] == 2
    assert checked_again.json()["verification"]["pending_steps"] == 1
    assert updated_plan.json()["steps"][2]["studio_verification"]["checks"]["schema"]["status"] == "pending"
    assert updated_rows.json()[0]["studio_verified"] == 2
    assert len(fake.calls) == 1  # volver a comprobar no vuelve a aplicar ni ejecutar el Job


def test_unavailable_readback_is_retryable_and_stale_revision_is_not_reused(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)

    class TransientReadback(FakeTalend):
        fail_inspection = True

        async def inspect_job(self, job_path: str):
            if self.fail_inspection:
                from sas_grid_migrator.talend_adapter.adapter import TalendError

                raise TalendError("Bridge temporalmente sin respuesta")
            return await super().inspect_job(job_path)

    migration = _plan("pending", "daily.sas", "job_daily")
    migration.steps = [PlanStep(
        id="read_accounts", order=1, subjob="main", action="add_component",
        component_candidate="tFileInputDelimited", purpose="Leer cuentas",
        properties=[Property(name="HEADER", value="1", origin="SAS", verified=True)],
        schema_columns=[SchemaColumn(name="account_id", talend_type="id_String", nullable=False)],
        evidence=Loc(file="daily.sas", line=1, end_line=1), verified=True,
    )]
    fake = TransientReadback()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Retry readback", [migration])
        applied = client.post(f"/api/projects/{project_id}/plans/daily.sas/talend-apply")
        unavailable_plan = client.get(f"/api/projects/{project_id}/plans/daily.sas")
        fake.fail_inspection = False
        retried = client.post(f"/api/projects/{project_id}/plans/daily.sas/talend-apply/verify")
        verified_plan = client.get(f"/api/projects/{project_id}/plans/daily.sas")
        store = Store(Settings.from_env())
        saved = PlanSet.model_validate_json(store.plans_path(project_id).read_text(encoding="utf-8"))
        saved.plans[0].steps[0].properties[0].value = "0"
        store.plans_path(project_id).write_text(saved.model_dump_json(), encoding="utf-8")
        stale = client.post(f"/api/projects/{project_id}/plans/daily.sas/talend-apply/verify")
        stale_rows = client.get(f"/api/projects/{project_id}/plans")

    assert applied.status_code == 200, applied.text
    assert applied.json()["verification"]["status"] == "unavailable"
    assert unavailable_plan.json()["steps"][0]["studio_verification"]["status"] == "unavailable"
    assert retried.status_code == 200, retried.text
    assert retried.json()["verification"]["configured_steps"] == 1
    assert verified_plan.json()["steps"][0]["studio_verification"]["status"] == "verified"
    assert stale.status_code == 409
    assert stale_rows.json()[0]["studio_status"] == "not_checked"
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


def test_failed_unapplied_batch_can_retry_after_connector_revision_is_fixed(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Retry fixed connector",
            [_plan("pending", "daily.sas", "job_daily")],
        )
        store = Store(Settings.from_env())
        store.begin_talend_apply_batch(project_id, "old-revision", ["daily.sas"])
        store.update_talend_apply_batch_state(
            project_id,
            status="failed",
            jobs=[
                {
                    "program": "daily.sas",
                    "status": "failed",
                    "result": None,
                    "error": "El conector FLOW no admite salidas de tFilterRow.",
                }
            ],
            current_program=None,
            completed_count=1,
        )

        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202, response.text
    assert state["status"] == "applied"
    assert state["revision_hash"] != "old-revision"
    assert state["attempt_count"] == 2
    assert len(fake.calls) == 1


def test_conflicted_batch_with_failed_unapplied_job_can_retry_new_revision(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Retry stale operation revision",
            [_plan("pending", "daily.sas", "job_daily")],
        )
        store = Store(Settings.from_env())
        store.begin_talend_apply_batch(project_id, "old-batch-revision", ["daily.sas"])
        store.update_talend_apply_batch_state(
            project_id,
            status="conflict",
            jobs=[
                {
                    "program": "daily.sas",
                    "status": "conflict",
                    "result": None,
                    "error": "La revisión anterior quedó pendiente.",
                }
            ],
            current_program=None,
            completed_count=1,
        )
        store.save_talend_apply_state(
            project_id,
            "daily.sas",
            revision_hash="old-operation-revision",
            status="failed",
            identity={"program": "daily.sas"},
            error="Falló antes de crear el Job.",
        )

        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")
        state = client.get(f"/api/projects/{project_id}/talend-apply-batch").json()

    assert response.status_code == 202, response.text
    assert state["status"] == "applied"
    assert state["revision_hash"] != "old-batch-revision"
    assert state["jobs"][0]["status"] == "applied"
    assert len(fake.calls) == 1


def test_failed_job_with_prior_result_cannot_reset_revision_even_if_inventory_is_empty(
    tmp_path, monkeypatch
):
    _set_env(monkeypatch, tmp_path)
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Keep applied operation revision",
            [_plan("pending", "daily.sas", "job_daily")],
        )
        store = Store(Settings.from_env())
        store.begin_talend_apply_batch(project_id, "old-batch-revision", ["daily.sas"])
        store.update_talend_apply_batch_state(
            project_id,
            status="conflict",
            jobs=[
                {
                    "program": "daily.sas",
                    "status": "conflict",
                    "result": None,
                    "error": "La revisión anterior quedó pendiente.",
                }
            ],
            current_program=None,
            completed_count=1,
        )
        store.save_talend_apply_state(
            project_id,
            "daily.sas",
            revision_hash="old-operation-revision",
            status="failed",
            identity={"program": "daily.sas"},
            result={"itemPath": "Process/previous/job_daily_0.1.item"},
            error="Falló una operación posterior.",
        )

        response = client.post(f"/api/projects/{project_id}/talend-apply-batch")

    assert response.status_code == 409
    assert len(fake.calls) == 0


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
        # Forma real capturada de Studio: `node` y `description`, severidad en mayúsculas.
        async def job_problems(self, job_name: str) -> dict:
            return {
                "clean": False,
                "problems": [
                    {
                        "severity": "ERROR",
                        "node": "tFixedFlowInput_2",
                        "component": "tFixedFlowInput",
                        "description": "Parameter (Valores) must have at least one value.",
                        "type": "JOB",
                    },
                    {"severity": "WARNING", "node": "tLogRow_2", "description": "Sin etiqueta"},
                ],
            }

    monkeypatch.setattr(api_module, "_talend", lambda: StudioProblems())
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Studio issues", [_plan("x", "a.sas", "job_a")])
        result = client.post(f"/api/projects/{project_id}/plans/a.sas/talend-apply")

    assert result.status_code == 200, result.text
    body = result.json()
    assert body["status"] == "partially_applied"
    assert body["review_required"] is True
    assert body["design_errors"] == ["tFixedFlowInput_2: Parameter (Valores) must have at least one value."]
    assert any("tFixedFlowInput_2" in warning and "Valores" in warning for warning in body["warnings"])


def test_errors_reported_by_the_write_call_are_not_lost_when_the_problems_view_is_still_clean(
    tmp_path, monkeypatch
):
    _set_env(monkeypatch, tmp_path)

    class WriteReportsErrors(FakeTalend):
        async def apply_custom_spec(self, arguments: dict) -> dict:
            result = await super().apply_custom_spec(arguments)
            result["problems"] = {
                "errors": ["tFixedFlowInput_2: Parameter (Valores) must have at least one value."],
                "warnings": [],
                "clean": False,
            }
            return result

    monkeypatch.setattr(api_module, "_talend", lambda: WriteReportsErrors())
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Write errors", [_plan("x", "a.sas", "job_a")])
        body = client.post(f"/api/projects/{project_id}/plans/a.sas/talend-apply").json()

    assert body["status"] == "partially_applied"
    assert body["design_errors"] == ["tFixedFlowInput_2: Parameter (Valores) must have at least one value."]


def test_a_clean_job_has_no_design_errors(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)
    monkeypatch.setattr(api_module, "_talend", lambda: FakeTalend())
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(client, "Clean", [_plan("x", "a.sas", "job_a")])
        body = client.post(f"/api/projects/{project_id}/plans/a.sas/talend-apply").json()

    assert body["design_errors"] == []
    assert body["status"] == "applied"


def test_child_job_design_errors_are_checked_too(tmp_path, monkeypatch):
    _set_env(monkeypatch, tmp_path)

    class ChildHasErrors(FakeTalend):
        async def job_problems(self, job_name: str) -> dict:
            if job_name == "job_child":
                return {
                    "clean": False,
                    "problems": [{"severity": "ERROR", "node": "tMap_1", "description": "Falta el mapeo"}],
                }
            return {"clean": True, "problems": []}

    monkeypatch.setattr(api_module, "_talend", lambda: ChildHasErrors())
    with TestClient(api_module.app) as client:
        project_id = _project_with_plans(
            client,
            "Child errors",
            [_plan("x", "parent.sas", "job_parent", child_call=True), _plan("x", "child.sas", "job_child")],
            [["parent.sas"], ["child.sas"]],
        )
        client.post(f"/api/projects/{project_id}/talend-apply-batch")
        child = client.get(f"/api/projects/{project_id}/plans/child.sas/talend-apply").json()

    assert child["status"] == "partially_applied"
    assert child["result"]["design_errors"] == ["tMap_1: Falta el mapeo"]


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
