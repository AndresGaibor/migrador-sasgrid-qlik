import io
import zipfile
from pathlib import Path

import apps.api.main as api_module
from fastapi.testclient import TestClient
from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.service import load_plans
from sas_grid_migrator.persistence.store import Store


def _archive(content: str | None = None) -> bytes:
    if content is None:
        content = (
            Path(__file__).parents[2]
            / "tests/fixtures/sas/p0_clientes_activos.sas"
        ).read_text(encoding="utf-8")
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("Banking/daily.sas", content)
    return buffer.getvalue()


def _new_project(client: TestClient, filename: str = "customers.zip") -> str:
    response = client.post(
        "/api/projects/uploads",
        files={"file": (filename, _archive(), "application/zip")},
    )
    assert response.status_code == 201, response.text
    return response.json()["project"]["id"]


def _preview(client: TestClient, project_id: str):
    return client.post(
        f"/api/projects/{project_id}/plans/Banking/daily.sas/talend-apply/preview"
    )


def _apply(client: TestClient, project_id: str):
    return client.post(f"/api/projects/{project_id}/plans/Banking/daily.sas/talend-apply")


class FakeTalend:
    def __init__(self, responses: list[dict] | None = None):
        self.responses = list(responses or [])
        self.arguments: list[dict] = []
        self.last_arguments: dict | None = None
        self.inspections: list[str] = []
        self.problems: dict[str, dict] = {}

    async def apply_custom_spec(self, arguments: dict) -> dict:
        self.arguments.append(arguments)
        self.last_arguments = arguments
        if self.responses:
            return self.responses.pop(0)
        return {
            "totalComponents": len(arguments["components"]),
            "connections": len(arguments["connections"]),
            "jobName": arguments["jobName"],
            "itemPath": f"{arguments['folderPath']}/{arguments['jobName']}_0.1.item",
        }

    async def inspect_job(self, job_path: str):
        from sas_grid_migrator.talend_adapter.adapter import ComponentRef, JobInspection

        self.inspections.append(job_path)
        names = [
            component.get("uniqueName", "")
            for component in (self.last_arguments or {}).get("components", [])
        ]
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
        return self.problems.get(job_name, {"clean": True, "problems": []})


def test_apply_destination_isolated_per_zip_and_matches_preview_and_mcp_payload(
    tmp_path, monkeypatch
):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        first_id = _new_project(client, "customers.zip")
        second_id = _new_project(client, "customers.zip")
        first_preview = _preview(client, first_id)
        second_preview = _preview(client, second_id)

        assert first_preview.status_code == 200, first_preview.text
        assert second_preview.status_code == 200, second_preview.text
        first_folder = first_preview.json()["identity"]["folder_path"]
        second_folder = second_preview.json()["identity"]["folder_path"]
        assert first_folder != second_folder
        assert first_id in first_folder and second_id in second_folder
        assert "Banking" in first_folder

        applied = _apply(client, first_id)
        assert applied.status_code == 200, applied.text
        assert fake.arguments[0]["folderPath"] == first_folder
        assert fake.arguments[0]["jobName"] == first_preview.json()["identity"]["job_name"]
        assert "contexts" in fake.arguments[0]
        assert "execute" not in fake.arguments[0]

        stored = client.get(
            f"/api/projects/{first_id}/plans/Banking/daily.sas/talend-apply"
        )
        assert stored.status_code == 200
        assert stored.json()["status"] == "applied"
        assert stored.json()["identity"]["folder_path"] == first_folder

        repeated = _apply(client, first_id)
        assert repeated.json() == applied.json()
        assert len(fake.arguments) == 1


def test_partial_apply_can_retry_same_revision_but_changed_revision_conflicts(
    tmp_path, monkeypatch
):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    fake = FakeTalend(
        [
            {"totalComponents": 0, "connections": 0, "jobName": "job_daily"},
            {"totalComponents": 100, "connections": 100, "jobName": "job_daily"},
        ]
    )
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    data_dir = tmp_path / "data"
    with TestClient(api_module.app) as client:
        project_id = _new_project(client)
        preview = _preview(client, project_id)
        assert preview.status_code == 200
        assert preview.json()["components"]

        first = _apply(client, project_id)
        assert first.status_code == 200, first.text
        assert first.json()["status"] == "partially_applied"
        retry = _apply(client, project_id)
        assert retry.status_code == 200, retry.text
        assert retry.json()["status"] == "applied"
        assert len(fake.arguments) == 2

        plans = load_plans(Store(Settings(data_dir=data_dir)), project_id)
        assert plans is not None
        plans.plans[0].rules_version = "revision-changed"
        Store(Settings(data_dir=data_dir)).plans_path(project_id).write_text(
            plans.model_dump_json(), encoding="utf-8"
        )
        conflict = _apply(client, project_id)
        assert conflict.status_code == 409
        assert "revisión" in conflict.json()["detail"].lower()
        assert len(fake.arguments) == 2


def test_mcp_failure_is_persisted_for_the_job_guide(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")

    class FailedTalend:
        async def apply_custom_spec(self, _arguments: dict) -> dict:
            from sas_grid_migrator.talend_adapter.adapter import TalendError

            raise TalendError("Bridge no disponible")

    monkeypatch.setattr(api_module, "_talend", FailedTalend)
    with TestClient(api_module.app) as client:
        project_id = _new_project(client)
        failed = _apply(client, project_id)
        state = client.get(
            f"/api/projects/{project_id}/plans/Banking/daily.sas/talend-apply"
        )

    assert failed.status_code == 502
    assert state.status_code == 200
    assert state.json()["status"] == "failed"
    assert state.json()["error"] == "Bridge no disponible"


def test_mcp_target_collision_is_persisted_as_a_conflict(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")

    class CollidingTalend:
        def __init__(self):
            self.calls = 0

        async def apply_custom_spec(self, _arguments: dict) -> dict:
            from sas_grid_migrator.talend_adapter.adapter import TalendError

            self.calls += 1
            raise TalendError("Job already exists at target folder")

    fake = CollidingTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _new_project(client)
        failed = _apply(client, project_id)
        repeated = _apply(client, project_id)
        state = client.get(
            f"/api/projects/{project_id}/plans/Banking/daily.sas/talend-apply"
        )

    assert failed.status_code == 409
    assert repeated.status_code == 409
    assert fake.calls == 1
    assert state.status_code == 200
    assert state.json()["status"] == "conflict"
    assert state.json()["error"] == "Job already exists at target folder"


def test_apply_reports_studio_verification_after_writing(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    fake = FakeTalend()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _new_project(client)
        outcome = _apply(client, project_id).json()

    verification = outcome["verification"]
    assert outcome["status"] == "applied"
    assert verification["status"] == "inspected"
    assert verification["components_requested"] >= 1
    assert verification["components_created"] == verification["components_requested"]
    assert verification["missing_components"] == []
    assert verification["studio_problems"] == {"clean": True, "items": []}
    assert fake.inspections


def test_apply_marks_partial_when_studio_misses_requested_components(tmp_path, monkeypatch):
    class MissingComponents(FakeTalend):
        async def inspect_job(self, job_path):
            inspection = await super().inspect_job(job_path)
            inspection.components = inspection.components[:-1]
            return inspection

    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    fake = MissingComponents()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    with TestClient(api_module.app) as client:
        project_id = _new_project(client)
        outcome = _apply(client, project_id).json()

    verification = outcome["verification"]
    assert outcome["status"] == "partially_applied"
    assert verification["missing_components"]
    assert any("no contiene" in warning for warning in outcome["warnings"])


def test_apply_still_succeeds_when_studio_cannot_be_inspected(tmp_path, monkeypatch):
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    class BlindFake(FakeTalend):
        async def inspect_job(self, job_path):
            raise TalendError("talend-mcp no disponible: Bridge caído")

        async def job_problems(self, job_name):
            raise TalendError("talend-mcp no disponible: Bridge caído")

    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    monkeypatch.setattr(api_module, "_talend", lambda: BlindFake())
    with TestClient(api_module.app) as client:
        project_id = _new_project(client)
        outcome = _apply(client, project_id).json()

    verification = outcome["verification"]
    assert outcome["status"] == "applied"
    assert verification["status"] == "unavailable"
    assert verification["reason"]
    assert verification["studio_problems"] is None
