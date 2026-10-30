"""Golden de los planes: cambia solo si cambia a propósito (UPDATE_GOLDEN=1 para regenerar)."""

import os
from pathlib import Path

import pytest

from sas_grid_migrator.reporting.exports import render_plan_md
from tests.support.cache import cached_planset

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"
GOLDEN = Path(__file__).parent.parent / "golden"
PROGRAMS = [
    "p0_clientes_activos.sas",
    "p0_resumen_sql.sas",
    "p1_merge_first_last.sas",
    "p1_macro_parametrizada.sas",
    "p2_codigo_dinamico.sas",
]


@pytest.fixture(scope="session")
def plans():
    # Caché de disco por contenido de FIXTURES y del código: se recalcula solo si cambia algo de eso.
    return {pl.program: pl for pl in cached_planset(FIXTURES).plans}


@pytest.mark.parametrize("program", PROGRAMS)
def test_plan_markdown_matches_golden(plans, program):
    got = render_plan_md(plans[program])
    path = GOLDEN / f"{Path(program).stem}.plan.md"
    if os.environ.get("UPDATE_GOLDEN"):
        path.write_text(got, encoding="utf-8")
    assert path.exists(), f"falta {path.name}; ejecuta con UPDATE_GOLDEN=1"
    assert got == path.read_text(encoding="utf-8")
