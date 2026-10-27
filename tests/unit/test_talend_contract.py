"""El manifiesto `contract/portal-tools.json` es la fuente única de las tools del portal."""

import re
from pathlib import Path

from sas_grid_migrator.talend_adapter import policy
from sas_grid_migrator.talend_adapter.contract import load_contract

ROOT = Path(__file__).resolve().parents[2]
CALL = re.compile(r'(?:_data|_studio_write|\.call)\(\s*"(talend_[a-z_]+)"', re.DOTALL)


def test_contract_matches_policy():
    contract = load_contract()
    assert contract.read_tools == policy.READ_TOOLS
    assert {contract.write_tool} == policy.WRITE_TOOLS


def test_manifest_covers_every_tool_the_portal_calls():
    contract = load_contract()
    allowed = set(contract.read_tools) | {contract.write_tool}
    used: set[str] = set()
    for folder in ("src", "apps/api"):
        for path in (ROOT / folder).rglob("*.py"):
            used.update(CALL.findall(path.read_text(encoding="utf-8")))
    assert used <= allowed, f"tools fuera del contrato: {sorted(used - allowed)}"


def test_required_fields_are_those_checked_by_health():
    contract = load_contract()
    assert contract.required_top_fields == {"childJobs", "instructions", "replaceManagedTodoContexts"}
    assert contract.required_component_fields == {"draftOnly", "draftReason", "tables"}
