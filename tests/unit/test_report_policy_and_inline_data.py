"""Política de reportes (WP3) y datos incrustados (WP2) en el plan.

Ambos paquetes tienen que quitar el pendiente sin inventar nada: la política decide el componente y los `datalines` se
convierten en filas reales; lo que no encaja con el `INPUT` sigue como pendiente con su motivo.
"""

import pytest

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program


def plan(source: str, report_policy: str = "log"):
    ir = build_ir(parse_program(source, "programa.sas"))
    return plan_program(ir, "p", load_mapping_rules(), {}, report_policy=report_policy)


REPORT = "proc print data=work.ventas; run;\n"

INLINE = """data work.clientes;
   input nombre $ edad;
   datalines;
ana 34
luis 41
;
run;
"""

COLUMN_INPUT = """data work.direcciones;
   infile datalines truncover;
   input #1 nombre $40.
         #2 calle $40.;
datalines;
ana
calle 1
;
run;
"""


def step_of(plan_, operation: str):
    return next(step for step in plan_.steps if step.operation_type == operation)


@pytest.mark.parametrize(
    ("policy", "component", "pending"),
    [
        ("log", "tLogRow", []),
        ("csv", "tFileOutputDelimited", ["Ruta del archivo de salida del reporte (política CSV): crear la variable de contexto path_<reporte>"]),
        ("discard", "ninguno", []),
    ],
)
def test_politica_de_reportes_decide_el_componente(policy, component, pending):
    step = step_of(plan(REPORT, policy), "report")
    assert step.component_candidate == component
    assert step.pending == pending


def test_politica_de_reportes_log_no_llen_a_pendientes_y_marca_el_modo():
    step = step_of(plan(REPORT), "report")
    assert step.pending == []
    assert any(p.name == "BASIC_MODE" and p.value == "true" for p in step.properties)


def test_politica_descartar_deja_anotado_que_se_perdio():
    step = step_of(plan(REPORT, "discard"), "report")
    assert step.status == "descartado"
    assert step.note and "política de reportes" in step.note


def test_politica_desconocida_falla_en_vez_de_adivinar():
    with pytest.raises(ValueError, match="Política de reportes desconocida"):
        plan(REPORT, "excel")


def test_datos_incrustados_se_convierten_en_filas_y_esquema():
    plan_ = plan(INLINE)
    step = step_of(plan_, "inline_data")
    assert step.component_candidate == "tFixedFlowInput"
    assert step.pending == []
    table = step.component_tables["VALUES"]
    assert table["columns"] == ["nombre", "edad"]
    assert table["rows"] == [{"nombre": "ana", "edad": "34"}, {"nombre": "luis", "edad": "41"}]
    assert [(c.name, c.talend_type) for c in step.schema_columns] == [("nombre", "String"), ("edad", "Double")]


def test_datos_incrustados_no_generan_ademas_una_lectura_de_archivo():
    plan_ = plan(INLINE)
    assert [s.operation_type for s in plan_.steps].count("read_file") == 0


def test_entrada_por_columnas_queda_como_pendiente_sin_inventar_filas():
    step = step_of(plan(COLUMN_INPUT), "inline_data")
    assert step.pending and "@" not in step.pending[0]
    assert "revisión manual" in step.pending[0]
    assert "VALUES" not in step.component_tables


def test_sin_sentencia_input_no_se_adivinan_columnas():
    source = "data work.x;\n datalines;\n1 2\n;\nrun;\n"
    step = step_of(plan(source), "inline_data")
    assert step.pending and "INPUT" in step.pending[0]
