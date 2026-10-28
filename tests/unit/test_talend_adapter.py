import asyncio
from pathlib import Path

import pytest
import apps.api.main as api_mod
from apps.api.main import app as api
from fastapi.testclient import TestClient

from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.talend_adapter.adapter import (
    CLIENT_HINT,
    SPEC_TOOL,
    McpCaller,
    McpClientUnavailable,
    TalendAdapter,
    TalendError,
)
from sas_grid_migrator.talend_adapter.contract import load_contract
from sas_grid_migrator.talend_adapter.policy import ToolNotAllowed
from sas_grid_migrator.talend_adapter.verification import Catalog, verify_plans
from tests.unit.test_planner import project

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"


class Fake:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    async def call(self, tool, args):
        self.calls.append((tool, args))
        r = self.responses[tool]
        if isinstance(r, Exception):
            raise r
        return r

    async def describe_tool(self, tool):
        return {"properties": {"childJobs": {}, "instructions": {}, "replaceManagedTodoContexts": {}, "components": {"items": {"properties": {"draftOnly": {}, "draftReason": {}, "tables": {}}}}}}


SPEC_SCHEMA = {
    "properties": {
        "childJobs": {},
        "instructions": {},
        "replaceManagedTodoContexts": {},
        "components": {"items": {"properties": {"draftOnly": {}, "draftReason": {}, "tables": {}}}},
    }
}


class ListingFake(Fake):
    """Caller que expone el inventario de tools y no acepta describe_tool."""

    def __init__(self, responses, tools):
        super().__init__(responses)
        self.tools = tools

    async def list_tools(self):
        return self.tools

    async def describe_tool(self, tool):
        raise AssertionError("list_tools es el camino esperado; describe_tool no debe usarse")


def listing(*, without=(), write_schema=SPEC_SCHEMA):
    """Inventario completo del contrato, con las tools indicadas fuera."""
    contract = load_contract()
    names = sorted((contract.read_tools | {contract.write_tool}) - set(without))
    return [
        {"name": name, "inputSchema": write_schema if name == contract.write_tool else {}}
        for name in names
    ]


DIALOGS_CLEAR = {"ok": True, "data": {"blocked": False, "dialogs": [], "blocking": []}}

JOB = {
    "ok": True,
    "data": {
        "inspection": {
            "job": {
                "components": [
                    {
                        "uniqueName": "tFilterRow_1",
                        "componentName": "tFilterRow",
                        "parameters": {"LOGICAL_OP": "&&", "CONDITIONS": "[]"},
                        "schemas": [{"name": "row1", "connector": "FLOW", "columns": [
                            {"name": "account_id", "type": "id_Integer", "nullable": False},
                            {"name": "balance", "type": "id_BigDecimal", "nullable": True},
                        ]}],
                    },
                    {"uniqueName": "x", "componentName": ""},
                ],
                "connections": [{"source": "tInput_1", "target": "tFilterRow_1", "connectorName": "FLOW", "label": "row1"}],
            },
            "contexts": [{"name": "anio"}],
            "connections": [{"source": "tInput_1", "target": "tFilterRow_1", "connectorName": "FLOW", "label": "row1"}],
            "mapperEntries": [{"componentUniqueName": "tMap_1", "table": "row2", "name": "fee", "expression": "row1.balance * 0.005", "type": "id_BigDecimal"}],
        }
    },
}


def run(coro):
    return asyncio.run(coro)


def test_mcp_caller_uses_the_configured_timeout_to_list_and_describe(monkeypatch):
    """`Client.list_tools` no acepta `read_timeout_seconds`: ese timeout va en el constructor."""
    import mcp as mcp_module

    recorded: dict[str, dict] = {}

    class FakeTool:
        name = "talend_jobs_list"

        def __init__(self):
            self.input_schema = {"properties": {"talend_jobs_list": {}}}

        def model_dump(self, **_kwargs):
            return {"name": self.name, "inputSchema": self.input_schema}

    class FakeResult:
        def __init__(self):
            self.tools = [FakeTool()]

    class FakeClient:
        def __init__(self, url, **kwargs):
            recorded["init"] = {"url": url, **kwargs}

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_exc):
            return False

        async def list_tools(self, **kwargs):
            recorded["list"] = kwargs
            return FakeResult()

    monkeypatch.setattr(mcp_module, "Client", FakeClient)
    caller = McpCaller("http://127.0.0.1:3927/mcp", timeout=12.5)

    tools = run(caller.list_tools())

    assert tools == [{"name": "talend_jobs_list", "inputSchema": {"properties": {"talend_jobs_list": {}}}}]
    assert recorded["init"]["read_timeout_seconds"] == 12.5
    assert recorded["list"] == {}

    schema = run(caller.describe_tool("talend_jobs_list"))

    assert schema == {"properties": {"talend_jobs_list": {}}}
    assert recorded["init"]["read_timeout_seconds"] == 12.5


def test_mcp_caller_reports_client_version_when_import_fails(monkeypatch):
    """Sin el cliente 2.x el error debe decir qué instalar, no `ImportError` ni «no disponible»."""
    import sys

    monkeypatch.setitem(sys.modules, "mcp", None)
    caller = McpCaller("http://127.0.0.1:3927/mcp")

    with pytest.raises(TalendError, match="uv sync"):
        run(caller.list_tools())


def test_inspect_job_parses_and_skips_empty():
    ad = TalendAdapter(Fake({"talend_inspect_job": JOB}))
    insp = run(ad.inspect_job("/w/j_0.1.item"))
    assert [c.component for c in insp.components] == ["tFilterRow"]
    assert insp.components[0].schema_columns == 2 and insp.contexts == ["anio"]
    assert insp.components[0].parameter_values["LOGICAL_OP"] == "&&"
    assert insp.components[0].schemas[0]["columns"][0]["name"] == "account_id"
    assert insp.connection_details[0]["label"] == "row1"
    assert insp.mapper_entries[0]["componentUniqueName"] == "tMap_1"


def test_inspect_rejects_non_item_and_error_envelope():
    ad = TalendAdapter(Fake({"talend_inspect_job": {"ok": False, "error": {"code": "X"}}}))
    with pytest.raises(TalendError):
        run(ad.inspect_job("/etc/passwd"))
    with pytest.raises(TalendError, match="X"):
        run(ad.inspect_job("/w/j.item"))


def test_policy_blocks_mutating_tools():
    ad = TalendAdapter(Fake({}))
    with pytest.raises(ToolNotAllowed):
        run(ad._data("talend_run_job"))
    with pytest.raises(ToolNotAllowed):
        run(ad._data("talend_add_connection"))


def test_health_unavailable_does_not_raise():
    ad = TalendAdapter(Fake({"talend_jobs_list": TalendError("caído")}))
    health = run(ad.health_check())
    assert health["available"] is False and health["mcp_available"] is False
    assert health["error"] == "caído"
    assert health["diagnosis"] == "mcp_down"
    assert "bun run start:server" in health["fix_hint"]
    ok = TalendAdapter(Fake({
        "talend_jobs_list": {"ok": True, "data": {"jobs": [{"name": "job", "path": "/process/job/job_0.1.item"}], "total": 1}},
        "talend_bridge_ping": {"ok": True, "data": {"ok": True, "mode": "readOnly", "unsafeActions": False}},
        "talend_studio_ui_dialogs": DIALOGS_CLEAR,
    }))
    health = run(ok.health_check())
    assert health["available"] is True
    assert health["mcp_available"] is True and health["bridge_available"] is True
    assert health["bridge_mode"] == "readOnly" and health["unsafe_actions"] is False
    assert health["jobs"] == 1
    assert health["spec_supported"] is True and health["spec_error"] is None
    assert health["tools"] is None and health["write_tool"] is None
    assert health["diagnosis"] == "ok" and health["fix_hint"] is None
    assert health["missing_tools"] == []


def test_spec_status_validates_the_contract_from_the_published_listing():
    ad = TalendAdapter(ListingFake({}, listing()))

    status = run(ad.custom_spec_status())

    assert status == {
        "spec_supported": True,
        "spec_error": None,
        "tools": len(load_contract().read_tools) + 1,
        "write_tool": True,
        "missing_tools": [],
        "diagnosis": "ok",
        "fix_hint": None,
    }


def test_spec_status_reports_when_the_write_tool_is_not_published():
    ad = TalendAdapter(ListingFake({}, listing(without=(SPEC_TOOL,))))

    status = run(ad.custom_spec_status())

    assert status["spec_supported"] is False
    assert status["write_tool"] is False
    assert status["missing_tools"] == [SPEC_TOOL]
    assert status["diagnosis"] == "tools_missing"


def test_spec_status_reports_missing_contract_fields_from_the_listing():
    outdated = {"properties": {
        "instructions": {},
        "replaceManagedTodoContexts": {},
        "components": {"items": {"properties": {"draftOnly": {}, "draftReason": {}, "tables": {}}}},
    }}
    ad = TalendAdapter(ListingFake({}, listing(write_schema=outdated)))

    status = run(ad.custom_spec_status())

    assert status["spec_supported"] is False
    assert status["write_tool"] is True
    assert status["missing_tools"] == []
    assert status["diagnosis"] == "contract_incomplete"
    assert "faltan" in status["spec_error"] and "childJobs" in status["spec_error"]
    assert "Actualiza" in status["fix_hint"]


def test_diagnosis_names_the_tool_missing_from_the_portal_preset():
    ad = TalendAdapter(ListingFake({}, listing(without=("talend_job_problems",))))

    status = run(ad.custom_spec_status())

    assert status["diagnosis"] == "tools_missing"
    assert status["missing_tools"] == ["talend_job_problems"]
    assert "TALEND_MCP_FILTER=portal" in status["fix_hint"]


def test_diagnosis_blames_the_client_when_the_mcp_package_is_old():
    class OldClient(ListingFake):
        async def list_tools(self):
            raise McpClientUnavailable(CLIENT_HINT)

    status = run(TalendAdapter(OldClient({}, [])).custom_spec_status())

    assert status["diagnosis"] == "client_incompatible"
    assert status["tools"] is None and status["write_tool"] is None
    assert "uv sync" in status["fix_hint"]


def test_health_reports_the_published_tool_inventory():
    adapter = TalendAdapter(ListingFake(
        {
            "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
            "talend_bridge_ping": {"ok": True, "data": {"ok": True, "mode": "readWrite", "unsafeActions": False}},
            "talend_studio_ui_dialogs": DIALOGS_CLEAR,
        },
        listing(),
    ))

    health = run(adapter.health_check())

    assert health["available"] is True
    assert health["tools"] == len(load_contract().read_tools) + 1
    assert health["write_tool"] is True
    assert health["spec_supported"] is True
    assert health["diagnosis"] == "ok"


def test_health_propagates_the_missing_tools_diagnosis():
    adapter = TalendAdapter(ListingFake(
        {
            "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
            "talend_bridge_ping": {"ok": True, "data": {"ok": True, "mode": "readWrite", "unsafeActions": False}},
            "talend_studio_ui_dialogs": DIALOGS_CLEAR,
        },
        listing(without=("talend_job_problems",)),
    ))

    health = run(adapter.health_check())

    assert health["diagnosis"] == "tools_missing"
    assert health["missing_tools"] == ["talend_job_problems"]
    assert "TALEND_MCP_FILTER=portal" in health["fix_hint"]


def test_health_reports_a_modal_dialog_that_blocks_studio():
    adapter = TalendAdapter(Fake({
        "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
        "talend_bridge_ping": {"ok": True, "data": {"ok": True, "mode": "readWrite", "unsafeActions": False}},
        "talend_studio_ui_dialogs": {
            "ok": True,
            "data": {
                "blocked": True,
                "dialogs": [],
                "blocking": [
                    {"title": "Network Issue Occured", "hint": "Ciérralo en Studio."},
                ],
            },
        },
    }))

    health = run(adapter.health_check())

    assert health["available"] is True
    assert health["spec_supported"] is True
    assert health["diagnosis"] == "studio_blocked"
    assert "Network Issue Occured" in health["fix_hint"]
    assert health["studio_dialogs"] == {
        "checked": True,
        "blocked": True,
        "blocking": [{"title": "Network Issue Occured", "hint": "Ciérralo en Studio."}],
    }


def test_health_keeps_the_contract_diagnosis_when_dialogs_cannot_be_checked():
    adapter = TalendAdapter(ListingFake(
        {
            "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
            "talend_bridge_ping": {"ok": True, "data": {"ok": True, "mode": "readWrite", "unsafeActions": False}},
            "talend_studio_ui_dialogs": TalendError("la sonda no respondió"),
        },
        listing(without=("talend_job_problems",)),
    ))

    health = run(adapter.health_check())

    assert health["studio_dialogs"] == {
        "checked": False,
        "blocked": False,
        "blocking": [],
        "error": "la sonda no respondió",
    }
    assert health["diagnosis"] == "tools_missing"


def test_health_reports_bridge_offline_even_when_mcp_server_is_reachable():
    adapter = TalendAdapter(ListingFake(
        {
            "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
            "talend_bridge_ping": {"ok": True, "data": {"ok": False}},
        },
        listing(),
    ))

    health = run(adapter.health_check())
    assert health["available"] is False
    assert health["mcp_available"] is True and health["bridge_available"] is False
    assert health["jobs"] == 0
    assert health["diagnosis"] == "bridge_down"
    assert "Talend Studio" in health["fix_hint"]
    assert health["error"].startswith("Talend Studio Bridge no está disponible.")


def test_health_exposes_active_connection_config_for_diagnostics():
    class ConfiguredFake(Fake):
        def __init__(self, responses):
            super().__init__(responses)
            self.url = "http://127.0.0.1:4927/mcp"
            self.timeout = 7.5

    ad = TalendAdapter(ConfiguredFake({
        "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
        "talend_bridge_ping": {"ok": True, "data": {"ok": False}},
    }))
    health = run(ad.health_check())
    assert health["mcp_url"] == "http://127.0.0.1:4927/mcp"
    assert health["timeout_seconds"] == 7.5
    assert "--install-bridge" in health["error"]

    down = TalendAdapter(ConfiguredFake({"talend_jobs_list": TalendError("caído")}))
    health = run(down.health_check())
    assert health["available"] is False and health["mcp_url"] == "http://127.0.0.1:4927/mcp"


def test_list_jobs_reads_every_mcp_page_when_inventory_exceeds_default_page_size():
    jobs = [
        {"name": f"job_{index}", "path": f"C:/workspace/process/job_{index}/job_{index}_0.1.item"}
        for index in range(101)
    ]

    class PagedCaller:
        def __init__(self):
            self.offsets = []

        async def call(self, tool, args):
            self.offsets.append(args["offset"])
            start = args["offset"]
            page = jobs[start : start + args["limit"]]
            return {"ok": True, "data": {"jobs": page, "count": len(page), "total": len(jobs)}}

    caller = PagedCaller()
    result = run(TalendAdapter(caller).list_jobs())

    assert caller.offsets == [0, 100]
    assert result == jobs


def test_list_jobs_rejects_an_incomplete_mcp_inventory():
    page = [
        {"name": f"job_{index}", "path": f"C:/workspace/process/job_{index}/job_{index}_0.1.item"}
        for index in range(100)
    ]

    class IncompleteCaller:
        async def call(self, _tool, args):
            if args["offset"] == 0:
                return {"ok": True, "data": {"jobs": page, "total": 101}}
            return {"ok": True, "data": {"jobs": [], "total": 101}}

    with pytest.raises(TalendError, match="inventario incompleto"):
        run(TalendAdapter(IncompleteCaller()).list_jobs())


def test_verify_plans_is_conservative(tmp_path):
    store, pid = project(tmp_path)
    ps = generate_plans(store, pid)
    cat = Catalog()
    cat.add(run(TalendAdapter(Fake({"talend_inspect_job": JOB})).inspect_job("/w/j.item")))
    stats = verify_plans(ps, cat)
    steps = [s for p in ps.plans for s in p.steps + [x for c in p.children for x in c.steps]]
    assert stats["verified"] + stats["component_known"] == sum(
        1 for s in steps if s.component_candidate == "tFilterRow"
    )
    # ningún componente ausente del catálogo se verifica
    assert not any(s.verified for s in steps if s.component_candidate != "tFilterRow")
    assert all(
        s.verified is False
        for s in steps
        if s.properties and not all(p.verified for p in s.properties)
    )


def test_api_talend(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    fake = TalendAdapter(Fake({"talend_inspect_job": JOB, "talend_jobs_list": TalendError("off")}))
    monkeypatch.setattr(api_mod, "_talend", lambda: fake)
    c = TestClient(api)
    assert c.get("/api/integrations/talend/health").json()["available"] is False
    r = c.post("/api/integrations/talend/inspect", json={"job_path": "/w/j.item"})
    assert r.json()["components"][0]["component"] == "tFilterRow"
    assert c.post("/api/integrations/talend/inspect", json={"job_path": "/w/j"}).status_code == 502
    pid = c.post("/api/projects", json={"name": "x"}).json()["id"]
    c.post(f"/api/projects/{pid}/imports", json={"path": str(FIXTURES)})
    c.post(f"/api/projects/{pid}/plans")
    v = c.post(f"/api/projects/{pid}/plans/verify", json={"job_paths": ["/w/j.item"]})
    assert v.status_code == 200 and v.json()["catalog_components"] == ["tFilterRow"]


def test_apply_custom_spec_delegates_the_complete_plan_to_the_mcp_executor(monkeypatch):
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    arguments = {
        "jobName": "DailyJob",
        "folderPath": "Process/PruebasWebSAS",
        "components": [
            {
                "uniqueName": "tFileInputDelimited_1",
                "componentName": "tFileInputDelimited",
                "posX": 160,
                "posY": 96,
                "label": "Leer archivo",
                "parameters": {"FILENAME": "input.csv"},
                "schema": {"name": "input_schema", "connector": "FLOW", "columns": []},
            },
            {
                "uniqueName": "tLogRow_2",
                "componentName": "tLogRow",
                "posX": 460,
                "posY": 96,
                "label": "Mostrar filas",
                "parameters": {},
            },
        ],
        "connections": [
            {
                "source": "tFileInputDelimited_1",
                "target": "tLogRow_2",
                "label": "row1",
                "connectorName": "FLOW",
                "uniqueName": "flow_1_1",
            }
        ],
    }
    fake = Fake({
        "talend_job_apply_custom_spec": {
            "ok": True,
            "data": {
                "jobName": "DailyJob",
                "itemPath": "process/PruebasWebSAS/DailyJob_0.1.item",
                "generatedComponents": 2,
                "connections": 1,
                "studioApi": True,
            },
        }
    })
    adapter = TalendAdapter(fake)

    result = run(adapter.apply_custom_spec(arguments))

    assert fake.calls == [("talend_job_apply_custom_spec", arguments)]
    assert result["itemPath"] == "process/PruebasWebSAS/DailyJob_0.1.item"
    assert result["studioApi"] is True
    assert result["generatedComponents"] == 2


def test_apply_custom_spec_rejects_success_envelope_without_explicit_ok(monkeypatch):
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    fake = Fake({"talend_job_apply_custom_spec": {"data": {"itemPath": "job.item"}}})

    with pytest.raises(TalendError, match="sin confirmación explícita de éxito"):
        run(TalendAdapter(fake).apply_custom_spec({"jobName": "DailyJob", "components": []}))


def test_apply_custom_spec_creates_context_only_job_and_reports_context_count(monkeypatch):
    monkeypatch.delenv("TALEND_MCP_READONLY", raising=False)
    arguments = {
        "jobName": "DailyJob",
        "folderPath": "Process/PruebasWebSAS",
        "components": [],
        "contexts": [{"name": "range_id", "type": "id_String", "value": "", "comment": "Rango"}],
    }
    fake = Fake({
        "talend_job_apply_custom_spec": {
            "ok": True,
            "data": {"generatedComponents": 0, "generatedContexts": 1},
        }
    })

    result = run(
        TalendAdapter(fake).apply_custom_spec(arguments)
    )

    assert fake.calls == [("talend_job_apply_custom_spec", arguments)]
    assert result["generatedComponents"] == 0
    assert result["generatedContexts"] == 1


def test_apply_custom_spec_reports_nested_studio_failure_from_mcp_executor(monkeypatch):
    monkeypatch.delenv("TALEND_MCP_READONLY", raising=False)
    arguments = {
        "jobName": "DailyJob",
        "folderPath": "Process/PruebasWebSAS",
        "components": [],
        "contexts": [{"name": "range_id", "type": "id_String", "value": "", "comment": "Rango"}],
    }
    fake = Fake({
        "talend_job_apply_custom_spec": {
            "ok": True,
            "data": {
                "ok": False,
                "error": {"code": "OPERATION_FAILED", "message": "Studio no guardó el contexto"},
            },
        }
    })

    with pytest.raises(TalendError, match="Studio no guardó el contexto"):
        run(
            TalendAdapter(fake).apply_custom_spec(arguments)
        )

    assert fake.calls == [("talend_job_apply_custom_spec", arguments)]


def test_adapter_from_env_reads_mcp_url_and_timeout(monkeypatch):
    monkeypatch.setenv("TALEND_MCP_URL", "http://127.0.0.1:4927/mcp")
    monkeypatch.setenv("TALEND_MCP_TIMEOUT_SECONDS", "7.5")

    adapter = TalendAdapter.from_env()

    assert adapter.caller.url == "http://127.0.0.1:4927/mcp"
    assert adapter.caller.timeout == 7.5



def test_apply_custom_spec_is_blocked_when_write_permission_is_off():
    fake = Fake({})
    adapter = TalendAdapter(fake, write_enabled=False)

    with pytest.raises(TalendError, match="solo lectura"):
        run(adapter.apply_custom_spec({"jobName": "DailyJob"}))

    assert fake.calls == []


def test_apply_custom_spec_ignores_readonly_env_when_permission_is_on(monkeypatch):
    monkeypatch.setenv("TALEND_MCP_READONLY", "true")
    fake = Fake({"talend_job_apply_custom_spec": {"ok": True, "data": {"jobName": "DailyJob"}}})
    adapter = TalendAdapter(fake, write_enabled=True)

    run(adapter.apply_custom_spec({"jobName": "DailyJob"}))

    assert fake.calls[0][0] == "talend_job_apply_custom_spec"


def test_apply_custom_spec_sends_the_complete_instruction_in_one_mcp_call(monkeypatch):
    monkeypatch.delenv("TALEND_MCP_READONLY", raising=False)
    arguments = {
        "jobName": "DailyJob",
        "folderPath": "Process/PruebasWebSAS",
        "components": [{"uniqueName": "tMap_1", "componentName": "tMap", "draftOnly": True}],
        "connections": [],
        "contexts": [],
        "instructions": {
            "source": {"program": "daily.sas", "sha256": "abc"},
            "steps": [{"id": "append", "evidence": {"line": 7}}],
            "unresolved": ["schema"],
        },
    }
    fake = Fake({
        "talend_job_apply_custom_spec": {
            "ok": True,
            "data": {"jobName": "DailyJob", "generatedComponents": 1, "warnings": ["schema"]},
        }
    })

    result = run(TalendAdapter(fake).apply_custom_spec(arguments))

    assert fake.calls == [("talend_job_apply_custom_spec", arguments)]
    assert result["generatedComponents"] == 1


def test_api_talend_health_reports_persisted_write_permission(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    adapter = TalendAdapter(Fake({
        "talend_jobs_list": {"ok": True, "data": {"jobs": []}},
        "talend_bridge_ping": {"ok": True, "data": {"ok": True, "mode": "readOnly", "unsafeActions": False}},
        "talend_studio_ui_dialogs": DIALOGS_CLEAR,
    }))
    monkeypatch.setattr(api_mod, "_talend", lambda: adapter)
    client = TestClient(api)

    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    assert client.patch("/api/integrations/talend/permissions", json={"write_enabled": False}).status_code == 200
    readonly = TestClient(api).get("/api/integrations/talend/health").json()
    monkeypatch.setenv("TALEND_MCP_READONLY", "true")
    assert client.patch("/api/integrations/talend/permissions", json={"write_enabled": True}).status_code == 200
    writable = TestClient(api).get("/api/integrations/talend/health").json()

    assert readonly["write_enabled"] is False
    assert writable["write_enabled"] is True


def test_job_problems_unwraps_clean_flag_and_items():
    ad = TalendAdapter(Fake({
        "talend_job_problems": {
            "ok": True,
            "data": {"clean": False, "problems": [{"severity": "warn", "message": "sin esquema"}], "extra": 1},
        },
    }))
    result = run(ad.job_problems("job_daily"))
    assert result == {"clean": False, "problems": [{"severity": "warn", "message": "sin esquema"}]}
    assert ad.caller.calls == [("talend_job_problems", {"job": "job_daily"})]
