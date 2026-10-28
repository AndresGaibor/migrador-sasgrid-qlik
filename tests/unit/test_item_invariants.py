"""`item_problems` detecta lo que hace que Studio avise al abrir un Job, aunque el XML sea válido."""

from pathlib import Path

from tests.support.item_invariants import item_problems

ITEMS = Path(__file__).parent.parent / "fixtures" / "talend_items"


def test_the_item_studio_complained_about_is_detected():
    """El `.item` real que Studio rechazó: el tMap tenía las tablas `out1`/`row1` y la conexión se llamaba `flow_3_1`."""
    problems = item_problems(ITEMS / "tmap_tablas_sin_conexion.item")

    assert any("flow_3_1" in problem and "tabla de salida" in problem for problem in problems)
    assert any("flow_3_1" in problem and "metaname" in problem for problem in problems)


def test_a_tmap_whose_tables_follow_its_connections_is_clean(tmp_path):
    item = tmp_path / "limpio.item"
    item.write_text(
        '<talendfile:ProcessType xmlns:talendfile="x" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<node componentName="tMap"><elementParameter name="UNIQUE_NAME" value="tMap_1"/>'
        '<metadata connector="FLOW" name="flow_out"/>'
        '<nodeData><outputTables name="flow_out"/><inputTables name="flow_in"/></nodeData></node>'
        '<node componentName="tFixedFlowInput"><elementParameter name="UNIQUE_NAME" value="in_1"/></node>'
        '<node componentName="tLogRow"><elementParameter name="UNIQUE_NAME" value="log_2"/></node>'
        '<connection source="in_1" target="tMap_1" label="row_in" connectorName="FLOW">'
        '<elementParameter name="UNIQUE_NAME" value="flow_in"/></connection>'
        '<connection source="tMap_1" target="log_2" label="row_out" connectorName="FLOW" metaname="flow_out">'
        '<elementParameter name="UNIQUE_NAME" value="flow_out"/></connection>'
        "</talendfile:ProcessType>",
        encoding="utf-8",
    )

    assert item_problems(item) == []


def test_a_connection_to_a_node_that_does_not_exist_is_reported(tmp_path):
    item = tmp_path / "huerfana.item"
    item.write_text(
        '<ProcessType><node componentName="tLogRow"><elementParameter name="UNIQUE_NAME" value="log_1"/></node>'
        '<connection source="log_1" target="fantasma" label="row1" connectorName="FLOW"/></ProcessType>',
        encoding="utf-8",
    )

    assert any("fantasma" in problem for problem in item_problems(item))
