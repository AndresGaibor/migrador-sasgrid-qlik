"""Golden de los planes: cambia solo si cambia a propósito (UPDATE_GOLDEN=1 para regenerar)."""

import os
from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.reporting.exports import render_plan_md

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"
GOLDEN = Path(__file__).parent.parent / "golden"
PROGRAMS = [
    "p0_clientes_activos.sas",
    "p0_resumen_sql.sas",
    "p1_merge_first_last.sas",
    "p1_macro_parametrizada.sas",
    "p2_codigo_dinamico.sas",
]


@pytest.fixture(scope="module")
def plans(tmp_path_factory):
    store = Store(Settings(data_dir=tmp_path_factory.mktemp("g") / "data"))
    p = store.create_project("g")
    store.import_batch(p.id, FIXTURES)
    return {pl.program: pl for pl in generate_plans(store, p.id).plans}


@pytest.mark.parametrize("program", PROGRAMS)
def test_plan_markdown_matches_golden(plans, program):
    got = render_plan_md(plans[program])
    path = GOLDEN / f"{Path(program).stem}.plan.md"
    if os.environ.get("UPDATE_GOLDEN"):
        path.write_text(got, encoding="utf-8")
    assert path.exists(), f"falta {path.name}; ejecuta con UPDATE_GOLDEN=1"
    assert got == path.read_text(encoding="utf-8")
