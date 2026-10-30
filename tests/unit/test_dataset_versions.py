"""Versiones de datasets (SSA) y copia de vuelta con la forma real (R23), con casos sintéticos genéricos.

Cada caso es un SAS mínimo con nombres inventados. Las aserciones son estructurales: conteos de pasos,
ausencia de escrituras y lecturas de WORK, un solo tMap con N expresiones, tHash solo en alto fan-out.
Nunca se comparan nombres de scripts reales.
"""

from __future__ import annotations

import pytest

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program


def _plan(text: str):
    program = parse_program(text, "versiones_sinteticas.sas")
    return plan_program(build_ir(program), "versiones", load_mapping_rules(), {}, source_text=text)


def _steps(plan):
    return plan.steps + [s for child in plan.children for s in child.steps]


def _real_steps(plan):
    """Pasos sin el tDie de seguridad ni la conexión compartida (la estructura del Job los añade)."""
    return [
        s
        for s in _steps(plan)
        if s.component_candidate not in ("tDie", "")
        and s.action != "manual_decision"
        and not (s.component_candidate == "por_determinar" and "onexi" in s.purpose)
        and not (s.component_candidate == "por_determinar" and "Cierra" in s.purpose)
    ]


def _candidates(plan) -> list[str]:
    return [s.component_candidate for s in _steps(plan)]


def _work_io(plan):
    """Escrituras y lecturas de WORK que el plan conserva como pasos propios."""
    return [
        s
        for s in _steps(plan)
        if s.operation_type in ("read", "write") and "work." in (s.purpose or "").lower()
    ]


def _expression_targets(plan) -> list[str]:
    return [e.target for s in _steps(plan) if s.component_candidate == "tMap" for e in s.expressions if e.target]


def _column_block(column: str, table: str = "work.base", temp: str = "work.tmp") -> str:
    """Bloque de copia de vuelta con la forma real: format, rename=, asignación, drop y proc delete."""
    return (
        f"data {temp};\n"
        f"  format {column} $10.;\n"
        f"  set {table}(rename={column}={column}_old);\n"
        f"  {column} = compress(input(left({column}_old), 10.));\n"
        f"  drop {column}_old;\n"
        "run;\n"
        f"data {table};\n"
        f"  set {temp};\n"
        "run;\n"
        f"proc delete data={temp};\n"
        "run;\n"
    )


# ---------------------------------------------------------------- (a) forma real, un bloque


def test_a_real_copy_back_block_once_leaves_one_tmap_and_no_work_io():
    plan = _plan(
        "data work.base; set src.clientes; run;\n"
        + _column_block("colA")
        + "data out.final; set work.base; run;\n"
    )
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert _candidates(plan).count("tMap") == 1, _candidates(plan)
    assert _expression_targets(plan) == ["colA"], _expression_targets(plan)
    assert len(_real_steps(plan)) <= 3, [(s.component_candidate, s.purpose) for s in _real_steps(plan)]


# ---------------------------------------------------------------- (b) tres bloques encadenados


def test_b_three_chained_blocks_on_one_table_become_one_tmap_with_three_expressions():
    plan = _plan(
        "data work.base; set src.clientes; run;\n"
        + _column_block("colA")
        + _column_block("colB")
        + _column_block("colC")
        + "data out.final; set work.base; run;\n"
    )
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert _candidates(plan).count("tMap") == 1, _candidates(plan)
    assert sorted(_expression_targets(plan)) == ["colA", "colB", "colC"], _expression_targets(plan)
    assert len(_real_steps(plan)) <= 3, [(s.component_candidate, s.purpose) for s in _real_steps(plan)]


def test_b2_chained_block_that_reads_a_column_computed_before_is_still_one_tmap():
    """La segunda asignación lee la columna que calculó la primera: se sustituye, no se corta la cadena."""
    plan = _plan(
        "data work.base; set src.clientes; run;\n"
        + _column_block("colA")
        + "data work.tmp;\n"
        "  set work.base;\n"
        "  colB = colA || 'x';\n"
        "run;\n"
        "data work.base; set work.tmp; run;\n"
        "proc delete data=work.tmp; run;\n"
        "data out.final; set work.base; run;\n"
    )
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert _candidates(plan).count("tMap") == 1, _candidates(plan)
    assert sorted(_expression_targets(plan)) == ["colA", "colB"], _expression_targets(plan)


# ---------------------------------------------------------------- (c) alias sin cambios


def test_c_alias_without_changes_adds_no_steps():
    plan = _plan(
        "data work.tmp; set src.a; run;\n"
        "data work.y; set work.tmp; run;\n"
        "proc delete data=work.tmp; run;\n"
        "data out.z; set work.y; run;\n"
    )
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert _candidates(plan).count("tMap") == 0, _candidates(plan)
    assert len(_real_steps(plan)) == 2, [(s.component_candidate, s.purpose) for s in _real_steps(plan)]


# ---------------------------------------------------------------- (d) dos consumidores contiguos


def test_d_dataset_read_by_two_contiguous_consumers_gets_multi_output_tmap_without_hash():
    plan = _plan(
        "data work.base; set src.a; x = a * 2; run;\n"
        "proc sql; create table stg.u as select * from work.base where x > 1; quit;\n"
        "proc sql; create table stg.v as select * from work.base where x < 1; quit;\n"
    )
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert not [c for c in _candidates(plan) if c.startswith("tHash")], _candidates(plan)
    assert [s.operation_type for s in _real_steps(plan)].count("write") == 2


# ---------------------------------------------------------------- (e) ocho consumidores dispersos


def test_e_dataset_read_by_eight_scattered_consumers_is_materialized_once_with_hash():
    parts = ["data work.base; set src.a; x = a * 2; run;\n"]
    for n in range(1, 9):
        parts.append(f"proc sql; create table stg.c{n} as select * from work.base where x > {n}; quit;\n")
        parts.append(f"data stg.k{n}; set src.b{n}; run;\n")
    plan = _plan("".join(parts))
    candidates = _candidates(plan)
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert candidates.count("tHashOutput") == 1, candidates
    assert candidates.count("tHashInput") == 8, candidates
    hashes = [s for s in _steps(plan) if s.component_candidate == "tHashInput"]
    assert all("8" in (s.why or "") for s in hashes), [s.why for s in hashes]


# ---------------------------------------------------------------- (f) tabla externa reescrita en sitio


def test_f_rewrite_in_place_of_external_table_keeps_the_final_write():
    plan = _plan(
        "libname src oracle user=etl path='ORCLX' schema=esq;\n"
        "data work.tmp; set src.cuentas(rename=(saldo=saldo_old)); saldo = saldo_old * 2; drop saldo_old; run;\n"
        "data src.cuentas; set work.tmp; run;\n"
        "proc delete data=work.tmp; run;\n"
    )
    assert not _work_io(plan), [s.purpose for s in _work_io(plan)]
    assert _candidates(plan).count("tOracleOutput") == 1, _candidates(plan)
