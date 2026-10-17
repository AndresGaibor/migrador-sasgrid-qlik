from pathlib import Path

import pytest

from sas_grid_migrator.talend_adapter.policy import ToolNotAllowed, assert_allowed

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"


@pytest.mark.parametrize(
    "tool",
    [
        "talend_run_job",
        "talend_delete_job",
        "talend_update_component_parameter",
        "talend_repo_pull",
    ],
)
def test_mutating_tools_denied(tool):
    with pytest.raises(ToolNotAllowed):
        assert_allowed(tool)


def test_read_tool_allowed():
    assert_allowed("talend_list_jobs")


def test_every_fixture_declares_priority():
    files = [
        p for p in FIXTURES.rglob("*") if "real" not in p.parts and p.suffix in {".sas", ".sh"}
    ]
    assert files
    for p in files:
        head = "\n".join(p.read_text().splitlines()[:2])
        assert "priority: P" in head, p
