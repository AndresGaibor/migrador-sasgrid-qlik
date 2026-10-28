from sas_grid_migrator.talend_adapter.apply_spec import (
    ApplyComponent,
    ApplyConnection,
    split_oversized_job,
)


def _component(name: str, x: int = 160, y: int = 96) -> ApplyComponent:
    return ApplyComponent(
        uniqueName=name, componentName=name.rsplit("_", 1)[0], posX=x, posY=y, label=f"Paso {name}", parameters={}
    )


def _edge(source: str, target: str) -> ApplyConnection:
    return ApplyConnection(
        source=source, target=target, label=f"row_{source}", connectorName="FLOW", uniqueName=f"flow_{source}"
    )


def _instructions(*step_names: str) -> dict:
    return {
        "source": {"program": "big.sas"},
        "steps": [{"id": f"s_{name}", "talendUniqueName": name} for name in step_names],
        "macros": [],
        "assumptions": ["supuesto"],
    }


def _split(components, connections, instructions=None, chunk_size=2, **kwargs):
    return split_oversized_job(
        "job_big", "Process/Prueba", components, connections, instructions or _instructions(),
        chunk_size=chunk_size, **kwargs,
    )


def test_independent_components_are_packed_into_child_jobs_of_the_chunk_size():
    names = [f"tLogRow_{i}" for i in range(1, 7)]

    parent_components, parent_connections, _instructions_out, children = _split(
        [_component(name) for name in names], []
    )

    assert [child["jobName"] for child in children] == ["job_big_p01", "job_big_p02", "job_big_p03"]
    assert [[c["uniqueName"] for c in child["components"]] for child in children] == [
        ["tLogRow_1", "tLogRow_2"], ["tLogRow_3", "tLogRow_4"], ["tLogRow_5", "tLogRow_6"],
    ]
    assert [(c.component_name, c.parameters) for c in parent_components] == [
        ("tRunJob", {"PROCESS": "job_big_p01"}),
        ("tRunJob", {"PROCESS": "job_big_p02"}),
        ("tRunJob", {"PROCESS": "job_big_p03"}),
    ]
    assert [(c.source, c.target, c.connector_name) for c in parent_connections] == [
        ("tRunJob_1", "tRunJob_2", "SUBJOB_OK"), ("tRunJob_2", "tRunJob_3", "SUBJOB_OK"),
    ]


def test_connected_components_never_end_up_in_different_children():
    components = [_component(name) for name in ("tMap_1", "tFilterRow_2", "tLogRow_3", "tLogRow_4")]

    _p, _c, _i, children = _split(components, [_edge("tMap_1", "tFilterRow_2")])

    chunks = [[c["uniqueName"] for c in child["components"]] for child in children]
    assert chunks == [["tMap_1", "tFilterRow_2"], ["tLogRow_3", "tLogRow_4"]]
    assert children[0]["connections"] == [
        {"source": "tMap_1", "target": "tFilterRow_2", "label": "row_tMap_1", "connectorName": "FLOW", "uniqueName": "flow_tMap_1"}
    ]
    assert children[1]["connections"] == []


def test_a_connected_group_larger_than_the_chunk_gets_its_own_child():
    components = [_component(f"tMap_{i}") for i in range(1, 4)] + [_component("tLogRow_9")]
    edges = [_edge("tMap_1", "tMap_2"), _edge("tMap_2", "tMap_3")]

    _p, _c, _i, children = _split(components, edges)

    assert [len(child["components"]) for child in children] == [3, 1]


def test_each_child_is_laid_out_without_overlapping_nodes():
    components = [_component(f"tLogRow_{i}", x=160 + i * 280) for i in range(1, 5)]

    _p, _c, _i, children = _split(components, [], chunk_size=4)

    positions = [(c["posX"], c["posY"]) for c in children[0]["components"]]
    assert len(set(positions)) == len(positions) == 4
    assert min(x for x, _y in positions) == 160 and min(y for _x, y in positions) == 96


def test_instructions_follow_their_components():
    components = [_component("tLogRow_1"), _component("tLogRow_2"), _component("tLogRow_3")]
    instructions = _instructions("tLogRow_1", "tLogRow_2", "tLogRow_3")
    instructions["steps"].append({"id": "s_pending", "talendUniqueName": None})
    instructions["macros"] = [{"name": "m", "parameters": [], "steps": [{"id": "s_macro", "talendUniqueName": "tLogRow_3"}]}]
    instructions["steps"] = [s for s in instructions["steps"] if s["talendUniqueName"] != "tLogRow_3"]

    _p, _c, parent, children = _split(components, [], instructions, chunk_size=2)

    assert [s["id"] for s in children[0]["instructions"]["steps"]] == ["s_tLogRow_1", "s_tLogRow_2"]
    assert [s["id"] for s in children[1]["instructions"]["steps"]] == ["s_macro"]
    assert children[0]["instructions"]["source"] == {"program": "big.sas"}
    assert [s["id"] for s in parent["steps"]] == ["s_pending"]
    assert parent["macros"][0]["steps"] == []
    assert parent["assumptions"] == ["supuesto"]
    assert [item["jobName"] for item in parent["split"]["children"]] == ["job_big_p01", "job_big_p02"]


def test_children_get_error_handling_when_requested():
    components = [_component("tFileInputDelimited_1"), _component("tLogRow_2")]

    _p, _c, _i, plain = _split(components, [], chunk_size=1)
    _p, _c, _i, handled = _split(components, [], chunk_size=1, error_handling=True)

    assert [c["componentName"] for c in plain[0]["components"]] == ["tFileInputDelimited"]
    assert [c["componentName"] for c in handled[0]["components"]] == [
        "tFileInputDelimited", "tLogCatcher", "tLogRow", "tDie",
    ]
