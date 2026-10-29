"""Ayudas compartidas por las pruebas de la API de planes (copiadas de test_api_talend_batch)."""

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


def make_plan(project_id: str, program: str, job_name: str, *, child_call: bool = False) -> JobPlan:
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


def project_with_plans(
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
        self.memory: dict = {"checked": True, "used_percent": 10, "restart_recommended": False}

    async def studio_memory(self) -> dict:
        return self.memory

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
