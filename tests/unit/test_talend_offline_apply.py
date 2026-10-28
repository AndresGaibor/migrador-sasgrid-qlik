import asyncio
from typing import Any

import pytest

from sas_grid_migrator.talend_adapter.adapter import TalendAdapter, TalendError
from sas_grid_migrator.talend_adapter.contract import load_contract
from sas_grid_migrator.talend_adapter.policy import assert_allowed

LIVE = "talend_job_apply_custom_spec"
OFFLINE = "talend_jobs_create_batch"


def run(coroutine):
    return asyncio.run(coroutine)


class Recorder:
    """Caller de prueba: responde por tool y recuerda cada llamada."""

    def __init__(self, responses: dict[str, Any]):
        self.responses = responses
        self.calls: list[tuple[str, dict]] = []

    async def call(self, tool, args):
        self.calls.append((tool, args))
        response = self.responses[tool]
        if callable(response):
            response = response(args)
        if isinstance(response, Exception):
            raise response
        return response

    async def describe_tool(self, tool):
        return {
            "properties": {
                "childJobs": {},
                "instructions": {},
                "replaceManagedTodoContexts": {},
                "components": {"items": {"properties": {"draftOnly": {}, "draftReason": {}, "tables": {}}}},
            }
        }

    def names(self) -> list[str]:
        return [tool for tool, _args in self.calls]


def real_writes(caller: "Recorder") -> list[str]:
    """Jobs que se escribieron de verdad (las validaciones con dryRun no cuentan)."""
    return [args["template"]["jobName"] for tool, args in caller.calls if tool == OFFLINE and not args["dryRun"]]


def dry_runs(caller: "Recorder") -> list[str]:
    return [args["template"]["jobName"] for tool, args in caller.calls if tool == OFFLINE and args["dryRun"]]


def batch_ok(args: dict, *, omitted: list[dict] | None = None) -> dict:
    name = args["template"]["jobName"]
    return {
        "ok": True,
        "data": {
            "total": 1,
            "correctos": 1,
            "escritos": 1,
            "fallos": [],
            "jobs": [{"job": name, "ok": True, "written": not args["dryRun"], "itemPath": f"C:/ws/process/{name}_0.1.item"}],
            **({"omitidos": omitted} if omitted else {}),
        },
    }


def job(name: str, components: int = 2, **extra) -> dict:
    return {
        "jobName": name,
        "version": "0.1",
        "folderPath": "Process/Pruebas",
        "components": [
            {"uniqueName": f"tLogRow_{index}", "componentName": "tLogRow", "posX": 160, "posY": 96, "label": "x", "parameters": {}}
            for index in range(1, components + 1)
        ],
        "connections": [
            {"source": "tLogRow_1", "target": "tLogRow_2", "label": "row1", "connectorName": "FLOW", "uniqueName": "row1"}
        ]
        if components > 1
        else [],
        "contexts": [{"name": "todo", "type": "id_String", "value": "", "comment": "pendiente"}],
        "childJobs": [],
        **extra,
    }


def test_the_offline_tool_is_part_of_the_contract_and_the_allowlist():
    contract = load_contract()

    assert contract.offline_write_tool == OFFLINE
    assert_allowed(OFFLINE)
    with pytest.raises(PermissionError):
        assert_allowed("talend_job_delete_in_studio")


def test_an_eligible_job_is_written_offline_with_the_live_result_shape():
    caller = Recorder({OFFLINE: batch_ok})

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert caller.names() == [OFFLINE, OFFLINE]
    assert dry_runs(caller) == ["job_a"] and real_writes(caller) == ["job_a"]
    assert result["jobName"] == "job_a"
    assert result["itemPath"] == "C:/ws/process/job_a_0.1.item"
    assert result["totalComponents"] == 2 and result["generatedComponents"] == 2
    assert result["connections"] == 1 and result["generatedConnections"] == 1
    assert result["componentAliases"] == {"tLogRow_1": "tLogRow_1", "tLogRow_2": "tLogRow_2"}
    assert result["childJobs"] == [] and result["warnings"] == []
    assert result["mode"] == "offline"


def test_offline_retry_reports_when_the_existing_portal_job_was_reused():
    def response(args):
        result = batch_ok(args)
        if not args["dryRun"]:
            result["data"]["jobs"][0]["reusedExisting"] = True
        return result

    caller = Recorder({OFFLINE: response})

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert result["reusedExisting"] is True


def test_child_jobs_are_written_first_each_one_as_its_own_job():
    caller = Recorder({OFFLINE: batch_ok})
    parent = job("job_padre", childJobs=[job("job_hijo_1"), job("job_hijo_2", childJobs=[job("job_nieto")])])

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(parent))

    order = ["job_hijo_1", "job_nieto", "job_hijo_2", "job_padre"]
    assert dry_runs(caller) == order and real_writes(caller) == order
    assert caller.names()[: len(order)] == [OFFLINE] * len(order)
    assert all(args["dryRun"] for _tool, args in caller.calls[: len(order)])
    assert [child["jobName"] for child in result["childJobs"]] == ["job_hijo_1", "job_hijo_2"]
    assert [grandchild["jobName"] for grandchild in result["childJobs"][1]["childJobs"]] == ["job_nieto"]


def test_translation_notices_from_the_mcp_become_warnings():
    caller = Recorder({OFFLINE: lambda args: {**batch_ok(args), "data": {**batch_ok(args)["data"], "avisos": ["tRaro: sin definicion"]}}})

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert result["warnings"] == ["tRaro: sin definicion"]


def test_tables_travel_to_the_offline_tool():
    caller = Recorder({OFFLINE: batch_ok})
    spec = job("job_a")
    spec["components"][0]["tables"] = {"CONDITIONS": {"columns": ["INPUT_COLUMN"], "rows": [["edad"]]}}

    run(TalendAdapter(caller, offline=True).apply_custom_spec(spec))

    sent = caller.calls[-1][1]["template"]["components"][0]
    assert sent["tables"] == {"CONDITIONS": {"columns": ["INPUT_COLUMN"], "rows": [["edad"]]}}


def test_omitted_drafts_are_reported_and_not_counted_as_created():
    omitted = [{"uniqueName": "tLogRow_2", "componentName": "tLogRow", "motivo": "'tLogRow' no esta en el catalogo local"}]
    caller = Recorder({OFFLINE: lambda args: batch_ok(args, omitted=omitted)})

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert result["totalComponents"] == 1 and result["generatedComponents"] == 1
    assert result["connections"] == 0
    assert "tLogRow_2" in result["warnings"][0] and "catalogo" in result["warnings"][0]


@pytest.mark.parametrize("blocker", [{"mapper": {"inputs": []}}])
def test_a_job_that_needs_studio_goes_live(blocker):
    caller = Recorder({LIVE: {"ok": True, "data": {"jobName": "job_a", "itemPath": "x.item"}}})
    spec = job("job_a")
    spec["components"][0].update(blocker)

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(spec))

    assert caller.names() == [LIVE]
    assert result["itemPath"] == "x.item"


def test_a_failed_offline_write_falls_back_to_studio_with_a_warning():
    failure = {"ok": True, "data": {"total": 1, "correctos": 0, "escritos": 0, "fallos": [{"job": "job_a", "error": "El job ya existe (usa overwrite)"}], "jobs": []}}
    caller = Recorder({OFFLINE: failure, LIVE: {"ok": True, "data": {"jobName": "job_a", "itemPath": "x.item", "warnings": ["w"]}}})

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert caller.names() == [OFFLINE, LIVE]
    assert result["warnings"][0] == "w"
    assert any("offline" in warning.lower() and "ya existe" in warning for warning in result["warnings"])


def test_ambiguous_failure_during_offline_write_never_retries_through_studio():
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    def response(args):
        if args["dryRun"]:
            return batch_ok(args)
        return {
            "ok": True,
            "data": {
                "total": 1,
                "correctos": 0,
                "escritos": 0,
                "fallos": [{"job": "job_a", "error": "fallo de escritura"}],
                "jobs": [],
            },
        }

    caller = Recorder({
        OFFLINE: response,
        LIVE: {"ok": True, "data": {"jobName": "job_a", "itemPath": "x.item"}},
    })

    with pytest.raises(TalendError, match="fallo de escritura"):
        run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert caller.names() == [OFFLINE, OFFLINE]


def test_a_tool_level_error_also_falls_back():
    caller = Recorder({
        OFFLINE: {"ok": False, "error": {"code": "NO_PROJECT", "message": "sin proyecto"}},
        LIVE: {"ok": True, "data": {"jobName": "job_a", "itemPath": "x.item"}},
    })

    result = run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_a")))

    assert caller.names() == [OFFLINE, LIVE]
    assert any("sin proyecto" in warning for warning in result["warnings"])


def test_offline_disabled_never_touches_the_offline_tool():
    caller = Recorder({LIVE: {"ok": True, "data": {"jobName": "job_a", "itemPath": "x.item"}}})

    run(TalendAdapter(caller, offline=False).apply_custom_spec(job("job_a")))

    assert caller.names() == [LIVE]


def test_a_failure_in_a_child_is_found_before_writing_anything_and_goes_live_for_the_whole_tree():
    def child_fails(args):
        if args["template"]["jobName"] == "job_hijo" and args["dryRun"]:
            return {"ok": True, "data": {"total": 1, "correctos": 0, "escritos": 0, "fallos": [{"job": "job_hijo", "error": "boom"}], "jobs": []}}
        return batch_ok(args)

    caller = Recorder({OFFLINE: child_fails, LIVE: {"ok": True, "data": {"jobName": "job_padre", "itemPath": "x.item"}}})

    run(TalendAdapter(caller, offline=True).apply_custom_spec(job("job_padre", childJobs=[job("job_hijo")])))

    assert caller.names() == [OFFLINE, LIVE]
    assert real_writes(caller) == []
    assert caller.calls[1][1]["jobName"] == "job_padre"


def test_the_mode_comes_from_the_environment(monkeypatch):
    monkeypatch.delenv("TALEND_APPLY_MODE", raising=False)
    assert TalendAdapter.from_env().offline is True
    monkeypatch.setenv("TALEND_APPLY_MODE", "live")
    assert TalendAdapter.from_env().offline is False
    monkeypatch.setenv("TALEND_APPLY_MODE", "auto")
    assert TalendAdapter.from_env().offline is True


def test_read_only_mode_blocks_offline_writes_too():
    caller = Recorder({OFFLINE: batch_ok})

    with pytest.raises(TalendError, match="solo lectura"):
        run(TalendAdapter(caller, write_enabled=False, offline=True).apply_custom_spec(job("job_a")))
    assert caller.calls == []
