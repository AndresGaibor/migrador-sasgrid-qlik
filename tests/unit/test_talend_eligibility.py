"""`offline_blockers`: qué impide aplicar una guía con el motor offline del MCP."""

from sas_grid_migrator.talend_adapter.eligibility import offline_blockers


def component(unique_name: str, name: str = "tFileInputDelimited", **extra) -> dict:
    return {
        "uniqueName": unique_name,
        "componentName": name,
        "posX": 0,
        "posY": 0,
        "label": unique_name,
        "parameters": {},
        **extra,
    }


def spec(components: list[dict], **extra) -> dict:
    return {
        "jobName": "job",
        "version": "0.1",
        "defaultContext": "Default",
        "folderPath": "Process/PruebasOffline",
        "description": "",
        "purpose": "",
        "components": components,
        "connections": [],
        "contexts": [],
        "replaceManagedTodoContexts": True,
        "childJobs": [],
        "instructions": {},
        **extra,
    }


def test_spec_without_mapper_or_tables_is_eligible():
    payload = spec([component("tFileInputDelimited_1"), component("tFilterRow_1", "tFilterRow")])
    assert offline_blockers(payload) == []


def test_mapper_blocks_offline():
    payload = spec([component("tMap_1", "tMap", mapper={"entries": []})])
    assert offline_blockers(payload) == ["mapper:tMap_1"]


def test_tables_blocks_offline():
    payload = spec([component("tOracleOutput_1", "tOracleOutput", tables={"TABLE": {"name": "T"}})])
    assert offline_blockers(payload) == ["tables:tOracleOutput_1"]
    assert offline_blockers(spec([component("tOracleOutput_1", tables={})])) == []


def test_child_jobs_block_offline():
    payload = spec([component("tRunJob_1", "tRunJob")], childJobs=[{"name": "hijo", "params": []}])
    assert offline_blockers(payload) == ["childJobs"]
