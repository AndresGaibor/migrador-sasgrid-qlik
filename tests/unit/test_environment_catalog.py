"""Catálogo de entorno (WP5) y su efecto en el plan (WP6, parte de lectura/escritura).

El catálogo declara una vez por entorno lo que el SAS no trae: motor por `libname`, tabla o archivo por dataset y tipos
de columna. Lo que no declara sigue siendo un pendiente con su motivo.
"""

import json
from pathlib import Path

import pytest

from sas_grid_migrator.environment.catalog import (
    CatalogError,
    EnvironmentCatalog,
    load,
    load_if_present,
)
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program

ROOT = Path(__file__).parent.parent.parent
EXAMPLE = ROOT / "rules" / "environment" / "learning-sas-by-example.json"
ENGINES = set(load_mapping_rules().engines)


def catalog_json(**overrides) -> dict:
    base = {
        "schema_version": 1,
        "libraries": [{"name": "learn", "engine": "postgres", "connection": "ctx_learn"}],
        "datasets": [
            {
                "library": "learn",
                "name": "ventas",
                "kind": "table",
                "target": "ventas",
                "columns": [{"name": "id", "talend_type": "id_Integer"}],
            }
        ],
    }
    base.update(overrides)
    return base


def write_catalog(tmp_path: Path, data: dict) -> Path:
    path = tmp_path / "environment.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def plan_with(source: str, catalog: EnvironmentCatalog | None, table_action: str = "drop_create"):
    ir = build_ir(parse_program(source, "programa.sas"))
    return plan_program(
        ir, "p", load_mapping_rules(), {}, environment=catalog, table_action=table_action
    )


def test_el_esquema_del_catalogo_esta_en_sincronia_con_el_modelo():
    path = ROOT / "schemas" / "environment.schema.json"
    assert json.loads(path.read_text(encoding="utf-8")) == EnvironmentCatalog.model_json_schema()


def test_el_ejemplo_del_repositorio_es_valido():
    catalog = load(EXAMPLE, ENGINES)
    assert catalog.dataset("learn", "blood") is not None
    assert catalog.dataset("learn", "survey").delimiter == ","


def test_dataset_por_ruta_fisica():
    catalog = load(EXAMPLE, ENGINES)
    assert catalog.dataset_by_path("data\\in\\survey.csv").name == "survey"


def test_libreria_temporal_no_se_busca():
    catalog = load(EXAMPLE, ENGINES)
    assert catalog.dataset("work", "blood") is None


def test_motor_desconocido_se_rechaza_con_la_lista_de_admitidos(tmp_path):
    path = write_catalog(
        tmp_path, catalog_json(libraries=[{"name": "learn", "engine": "mongodb"}])
    )
    with pytest.raises(CatalogError, match="admitidos"):
        load(path, ENGINES)


def test_dataset_huerfano_se_rechaza(tmp_path):
    data = catalog_json()
    data["datasets"][0]["library"] = "otra"
    with pytest.raises(CatalogError, match="no está declarada"):
        load(write_catalog(tmp_path, data), ENGINES)


def test_dataset_delimitado_sin_delimitador_se_rechaza(tmp_path):
    data = catalog_json()
    data["datasets"][0]["kind"] = "delimited"
    with pytest.raises(CatalogError, match="delimitador"):
        load(write_catalog(tmp_path, data), ENGINES)


def test_tipo_de_columna_inventado_se_rechaza(tmp_path):
    data = catalog_json()
    data["datasets"][0]["columns"][0]["talend_type"] = "id_Text"
    with pytest.raises(CatalogError, match="tipo"):
        load(write_catalog(tmp_path, data), ENGINES)


def test_version_de_esquema_no_soportada(tmp_path):
    with pytest.raises(CatalogError, match="versión de esquema"):
        load(write_catalog(tmp_path, catalog_json(schema_version=2)), ENGINES)


def test_sin_catalogo_no_hay_error():
    assert load_if_present(Path("no-existe.json"), ENGINES) is None


def test_leer_con_catalogo_quita_los_pendientes_de_datos(tmp_path):
    catalog = load(write_catalog(tmp_path, catalog_json()), ENGINES)
    plan = plan_with("data work.resumen;\n set learn.ventas;\n x = 1;\nrun;\n", catalog)
    step = next(s for s in plan.steps if s.operation_type == "read")
    assert step.pending == []
    assert {p.name: p.value for p in step.properties}["TABLE"] == "ventas"
    assert [(c.name, c.talend_type) for c in step.schema_columns] == [("id", "id_Integer")]


def test_sin_catalogo_la_lectura_sigue_pidiendo_los_datos():
    plan = plan_with("data work.resumen;\n set learn.ventas;\n x = 1;\nrun;\n", None)
    step = next(s for s in plan.steps if s.operation_type == "read")
    assert step.pending


def test_escribir_con_catalogo_usa_la_accion_del_proyecto(tmp_path):
    catalog = load(write_catalog(tmp_path, catalog_json()), ENGINES)
    plan = plan_with("data learn.ventas;\n set work.base;\nrun;\n", catalog, table_action="truncate")
    step = next(s for s in plan.steps if s.operation_type == "write")
    props = {p.name: p.value for p in step.properties}
    assert step.pending == []
    assert props["TABLE"] == "ventas"
    assert (props["TABLE_ACTION"], props["DATA_ACTION"]) == ("CLEAR", "INSERT")


def test_accion_de_escritura_desconocida_queda_pendiente(tmp_path):
    catalog = load(write_catalog(tmp_path, catalog_json()), ENGINES)
    plan = plan_with("data learn.ventas;\n set work.base;\nrun;\n", catalog, table_action="upsert")
    step = next(s for s in plan.steps if s.operation_type == "write")
    assert any("Acción al escribir desconocida" in item for item in step.pending)
