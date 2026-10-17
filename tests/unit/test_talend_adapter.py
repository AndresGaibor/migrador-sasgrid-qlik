import asyncio
from pathlib import Path

import apps.api.main as api_mod
import pytest
from apps.api.main import app as api
from fastapi.testclient import TestClient

from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.talend_adapter.adapter import TalendAdapter, TalendError
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
                        "schemas": [{"columns": [{}, {}]}],
                    },
                    {"uniqueName": "x", "componentName": ""},
                ],
                "connections": [{}],
            },
            "contexts": [{"name": "anio"}],
        }
    },
}


def run(coro):
    return asyncio.run(coro)


def test_inspect_job_parses_and_skips_empty():
    ad = TalendAdapter(Fake({"talend_inspect_job": JOB}))
    insp = run(ad.inspect_job("/w/j_0.1.item"))
    assert [c.component for c in insp.components] == ["tFilterRow"]
    assert insp.components[0].schema_columns == 2 and insp.contexts == ["anio"]


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
    ad = TalendAdapter(Fake({"talend_list_jobs": TalendError("caído")}))
    assert run(ad.health_check()) == {"available": False, "error": "caído"}
    ok = TalendAdapter(Fake({"talend_list_jobs": {"ok": True, "data": {"jobs": [{}]}}}))
    assert run(ok.health_check()) == {"available": True, "jobs": 1}


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
    fake = TalendAdapter(Fake({"talend_inspect_job": JOB, "talend_list_jobs": TalendError("off")}))
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
