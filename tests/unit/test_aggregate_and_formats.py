"""PROC MEANS/SUMMARY/FREQ → tAggregateRow y PROC FORMAT → tabla de lookup (WP4).

Lo que el SAS dice se traduce; lo que necesita información que el programa no trae (todas las variables numéricas del
dataset, cruces de TABULATE, rangos de un formato) sigue pendiente con su motivo.
"""

import pytest

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import (
    _format_needs_logic,
    _proc_aggregate,
    load_mapping_rules,
    plan_program,
)
from sas_grid_migrator.sas_parser.parser import parse_program


def aggregate(source: str):
    ir = build_ir(parse_program(source, "programa.sas"))
    plan = plan_program(ir, "p", load_mapping_rules(), {})
    return next(step for step in plan.steps if step.operation_type == "aggregate")


def values(step) -> dict:
    return {p.name: p.value for p in step.properties}


def test_means_con_var_sale_con_grupos_y_estadisticas():
    step = aggregate(
        "proc means data=work.ventas;\n"
        "  class region;\n"
        "  var importe;\n"
        "  output out=work.resumen mean=media std=desv;\n"
        "run;\n"
    )
    assert step.pending == []
    props = values(step)
    assert props["GROUPBYS"] == "region"
    assert props["OPERATIONS"] == "media = avg(importe); desv = stddev(importe)"


def test_output_con_un_nombre_para_varias_variables_queda_pendiente():
    step = aggregate(
        "proc means data=work.ventas;\n  var importe unidades;\n  output out=work.r mean=media;\nrun;\n"
    )
    assert any("AUTONAME" in item for item in step.pending)


def test_means_sin_output_usa_las_estadisticas_por_defecto_de_sas():
    step = aggregate("proc means data=work.ventas;\n  var importe;\nrun;\n")
    assert step.pending == []
    assert values(step)["OPERATIONS"] == (
        "importe_N = count(importe); importe_Mean = avg(importe); importe_Std = stddev(importe); "
        "importe_Min = min(importe); importe_Max = max(importe)"
    )


def test_means_sin_var_queda_pendiente_porque_faltaria_el_esquema():
    step = aggregate("proc means data=work.ventas;\nrun;\n")
    assert any("sin VAR" in item for item in step.pending)


def test_means_con_una_estadistica_sin_equivalente_queda_pendiente():
    step = aggregate(
        "proc means data=work.ventas;\n  var importe;\n  output out=work.r median=mediana;\nrun;\n"
    )
    assert any("median" in item for item in step.pending)
    assert not values(step)["OPERATIONS"]


def test_freq_de_una_tabla_sale_con_el_conteo():
    step = aggregate("proc freq data=work.ventas;\n  tables region * canal;\nrun;\n")
    assert step.pending == []
    props = values(step)
    assert props["GROUPBYS"] == "region, canal"
    assert props["OPERATIONS"] == "COUNT = count(region)"


def test_freq_con_opciones_o_varias_tablas_queda_pendiente():
    step = aggregate("proc freq data=work.ventas;\n  tables region / nocol norow;\nrun;\n")
    assert any("PROC FREQ" in item for item in step.pending)


def test_tabulate_queda_pendiente_porque_no_es_una_fila_por_grupo():
    step = aggregate("proc tabulate data=work.ventas;\n  class region;\n  var importe;\nrun;\n")
    assert any("TABULATE" in item for item in step.pending)


def test_by_del_proc_entra_en_los_grupos():
    groups, operations, reason = _proc_aggregate(
        "means", {"by": ["region"], "statements": ["var importe;", "output out=r sum=total;"]}
    )
    assert reason is None
    assert groups == ["region"]
    assert operations == ["total = sum(importe)"]


@pytest.mark.parametrize("key", ["30-50", "51-high", "low-<13", "other", ""])
def test_claves_de_formato_que_no_son_un_valor_suelto_se_detectan(key):
    assert _format_needs_logic(key)


@pytest.mark.parametrize("key", ["1", "2", "F", "dx"])
def test_valores_sueltos_de_formato_no_se_marcan_como_rango(key):
    assert not _format_needs_logic(key)


def test_formato_de_valores_sueltos_no_deja_pendiente():
    source = (
        "proc format;\n"
        "  value $genero\n"
        "    'F' = 'Femenino'\n"
        "    'M' = 'Masculino';\n"
        "run;\n"
    )
    ir = build_ir(parse_program(source, "programa.sas"))
    plan = plan_program(ir, "p", load_mapping_rules(), {})
    step = next(s for s in plan.steps if s.operation_type == "format_definition")
    assert step.pending == []
    assert values(step)["INTABLE"] == "genero | F | Femenino\ngenero | M | Masculino"


def test_formato_con_rangos_queda_pendiente_con_el_motivo():
    source = "proc format;\n  value edad\n    low-<13 = 'nino'\n    13-high = 'adulto';\nrun;\n"
    ir = build_ir(parse_program(source, "programa.sas"))
    plan = plan_program(ir, "p", load_mapping_rules(), {})
    step = next(s for s in plan.steps if s.operation_type == "format_definition")
    assert any("rangos u OTHER" in item for item in step.pending)
