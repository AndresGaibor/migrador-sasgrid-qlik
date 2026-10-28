import pytest

from sas_grid_migrator.talend_adapter.eligibility import offline_blockers
from sas_grid_migrator.talend_adapter.offline_payload import to_batch_arguments


def spec(**overrides):
    base = {
        "jobName": "DailyJob",
        "version": "0.1",
        "folderPath": "Process/PruebasOffline",
        "description": "desc",
        "purpose": "propósito",
        "components": [
            {
                "uniqueName": "tFilterRow_1",
                "componentName": "tFilterRow",
                "label": "filtro",
                "parameters": {"LOGICAL_OP": "&&"},
                "draftOnly": True,
                "draftReason": "falta el esquema",
            }
        ],
        "connections": [],
        "contexts": [{"name": "run_date", "type": "id_String", "value": "2026-10-28", "comment": "SAS"}],
        "instructions": {"steps": []},
        "replaceManagedTodoContexts": True,
    }
    return {**base, **overrides}


def test_batch_arguments_use_one_empty_row_and_keep_contexts_as_the_portal_builds_them():
    args = to_batch_arguments(spec())

    assert args["rows"] == [{}]
    assert args["overwrite"] is False
    assert args["dryRun"] is False
    template = args["template"]
    assert template["jobName"] == "DailyJob"
    assert template["folderPath"] == "Process/PruebasOffline"
    assert template["contexts"] == [
        {"name": "run_date", "type": "id_String", "value": "2026-10-28", "comment": "SAS"}
    ]


def test_batch_template_drops_fields_the_offline_tool_does_not_know():
    template = to_batch_arguments(spec())["template"]

    assert set(template["components"][0]) == {"uniqueName", "componentName", "label", "parameters"}
    assert not {"purpose", "instructions", "replaceManagedTodoContexts", "childJobs"} & set(template)


def test_blocked_specs_are_rejected_with_the_reason():
    blocked = spec(components=[{"uniqueName": "tMap_1", "componentName": "tMap", "mapper": {"inputs": []}}])

    with pytest.raises(ValueError, match=r"mapper:tMap_1"):
        to_batch_arguments(blocked)


def test_placeholder_syntax_blocks_offline_because_the_template_engine_would_expand_it():
    risky = spec(
        components=[
            {
                "uniqueName": "tFilterRow_1",
                "componentName": "tFilterRow",
                "parameters": {"CONDITION": "name == '{{valor}}'"},
            }
        ]
    )

    assert offline_blockers(risky) == ["placeholder:tFilterRow_1"]
    risky_context = spec(contexts=[{"name": "x", "type": "id_String", "value": "{{x}}"}])
    assert offline_blockers(risky_context) == ["placeholder:contexts"]
