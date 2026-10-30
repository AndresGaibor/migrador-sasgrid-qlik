"""Condicionales IF/THEN/ELSE de un DATA step (WP7, parte de `compute`).

Un condicional que no se traduce tiene que quedar como pendiente: antes se quedaba dentro del paso con `talend=None` y el
paso contaba como automatizado, que es justo el hueco silencioso que el plan prohíbe.
"""

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program


def compute(source: str):
    ir = build_ir(parse_program(source, "programa.sas"))
    plan = plan_program(ir, "p", load_mapping_rules(), {})
    return next(step for step in plan.steps if step.operation_type == "compute")


def test_condicional_con_condicion_traducible_sale_como_ternaria():
    step = compute(
        "data work.b;\n set work.a;\n if 2 > 1 then y = 5;\n else y = 6;\nrun;\n"
    )
    assert step.pending == []
    assert [e.talend for e in step.expressions] == ["((2 > 1) ? 5 : 6)"]


def test_condicional_sin_else_deja_el_perdido_como_alternativa():
    step = compute("data work.b;\n set work.a;\n if 2 > 1 then y = 5;\nrun;\n")
    assert step.pending == []
    assert [e.talend for e in step.expressions] == ["((2 > 1) ? 5 : null)"]
    # Sin ELSE el tipo lo manda la rama verdadera: numérico.
    assert [(c.name, c.talend_type) for c in step.schema_columns if c.name == "y"] == [("y", "Double")]


def test_condicional_sobre_columna_sin_tipo_igualdad_traducida_con_aviso():
    """Política acordada: igualdad/IN contra un literal de TEXTO se traduce null-safe (`"lit".equals(col)`), asumiendo
    texto con aviso «tipo no confirmado» y validación semántica requerida. El orden (`<`/`>`) sobre texto NO se traduce."""
    step = compute(
        "data work.b;\n set work.a;\n if estado = 'IN' then activo = 'S';\n else activo = 'N';\nrun;\n"
    )
    assert step.pending == []
    assert step.requires_semantic_validation
    assert len(step.expressions) == 1
    assert step.expressions[0].talend == '("IN".equals(input_row.estado) ? "S" : "N")'
    assert step.expressions[0].requires_semantic_validation
    assert any("tipo no confirmado" in w for w in step.expressions[0].warnings)


def test_orden_sobre_texto_sin_tipo_queda_pendiente():
    """El orden `<` sobre una columna de tipo desconocido no tiene traducción automática segura: queda pendiente."""
    step = compute(
        "data work.b;\n set work.a;\n if estado < 'IN' then activo = 'S';\n else activo = 'N';\nrun;\n"
    )
    assert step.pending == ["Condicional IF/ELSE sin traducción automática: revisar a mano"]
    assert all(e.talend is None for e in step.expressions)


def test_el_else_no_se_pierde_cuando_el_condicional_no_se_traduce():
    step = compute(
        "data work.b;\n set work.a;\n if estado = 'IN' then activo = 'S';\n else activo = 'N';\nrun;\n"
    )
    assert len(step.expressions) == 1
    assert "activo = 'S'" in step.expressions[0].sas
    assert "activo = 'N'" in step.expressions[0].sas


def test_then_do_queda_pendiente():
    step = compute(
        "data work.b;\n set work.a;\n if 2 > 1 then do;\n  y = 1;\n end;\nrun;\n"
    )
    assert any("Condicional" in item for item in step.pending)
