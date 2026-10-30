"""Macros repetidas en un mismo programa (Cod1): una entrada por definición distinta en el IR y en el plan."""

import shutil
from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.intermediate_representation.builder import build_ir, macro_fingerprint
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.parser import parse_program

FIXTURE = Path(__file__).parent.parent / "fixtures" / "cod1" / "cod1_macros_repetidas.sas"


def _lines_of(text: str, needle: str) -> list[int]:
    return [i for i, line in enumerate(text.splitlines(), start=1) if line.startswith(needle)]


def test_identical_macro_copies_collapse_into_one_entry():
    text = FIXTURE.read_text(encoding="utf-8")
    ir = build_ir(parse_program(text, FIXTURE.name), {})

    by_name = {m.name: m for m in ir.macros}
    assert [m.name for m in ir.macros] == ["carga_tabla", "split2", "carga_tabla_v2"]
    assert by_name["split2"].copies == 2
    assert by_name["split2"].duplicate_lines == _lines_of(text, "%macro split2")[1:]
    assert by_name["split2"].source_name is None
    assert by_name["split2"].notes == []


def test_distinct_definition_with_same_name_keeps_both_with_stable_suffix():
    text = FIXTURE.read_text(encoding="utf-8")
    ir = build_ir(parse_program(text, FIXTURE.name), {})

    first, variant = ir.macros[0], ir.macros[2]
    assert first.name == "carga_tabla" and first.copies == 2
    assert variant.name == "carga_tabla_v2"
    assert variant.source_name == "carga_tabla"
    assert variant.loc.line == _lines_of(text, "%macro carga_tabla")[2]
    assert any("cuerpo distinto" in note for note in variant.notes)


def test_fingerprint_ignores_position_but_not_body():
    text = FIXTURE.read_text(encoding="utf-8")
    nodes = [n for n in parse_program(text, FIXTURE.name).nodes if getattr(n, "name", "") == "split2"]
    assert len(nodes) == 2
    assert nodes[0].loc.line != nodes[1].loc.line
    assert macro_fingerprint(nodes[0]) == macro_fingerprint(nodes[1])

    carga = [n for n in parse_program(text, FIXTURE.name).nodes if getattr(n, "name", "") == "carga_tabla"]
    assert len(carga) == 3
    assert macro_fingerprint(carga[0]) == macro_fingerprint(carga[1])
    assert macro_fingerprint(carga[0]) != macro_fingerprint(carga[2])


def test_plan_has_one_child_job_per_distinct_macro(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    shutil.copy(FIXTURE, src / FIXTURE.name)
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("cod1_macros")
    store.import_batch(project.id, src)
    plans = generate_plans(store, project.id).plans

    assert len(plans) == 1
    names = [child.name for child in plans[0].children]
    # split2 ordena datos: es joblet, no hijo.
    assert names == ["carga_tabla", "carga_tabla_v2"]
    assert len(names) == len(set(names))
    # La macro que ordena un dataset es trabajo de datos: se propone como joblet, no como fontanería.
    assert any(j.name == "jl_Split2" for j in plans[0].joblets)
    for child in plans[0].children:
        step_ids = [step.id for step in child.steps]
        assert len(step_ids) == len(set(step_ids))
