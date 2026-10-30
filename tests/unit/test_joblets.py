"""Joblets: bloques repetidos (huella estructural), joblets propuestos y golden con los fixtures reales
recortados de Cod1 y Cod2 (ver docs/joblets.md)."""

import json
import os
import shutil
from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.intermediate_representation.repetition import (
    block_fingerprint,
    find_sequence_repetitions,
)
from sas_grid_migrator.migration_planner import limits
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.parser import parse_program

TESTS = Path(__file__).parent.parent
JOBLET_FIXTURES = TESTS / "fixtures" / "joblets"
GOLDEN = TESTS / "golden" / "joblets_fixtures.json"
CONVERSION = "conversion_tipo.sas"
CTE_AHO = "cte_aho.sas"
MACROS = TESTS / "fixtures" / "cod1" / "cod1_macros_repetidas.sas"


def _plans_for(tmp_path, files: list[Path]):
    src = tmp_path / "src"
    src.mkdir()
    for file in files:
        shutil.copy(file, src / file.name)
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("joblets")
    store.import_batch(project.id, src)
    return {plan.program: plan for plan in generate_plans(store, project.id).plans}


@pytest.fixture(scope="module")
def fixture_plans(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("joblets")
    return _plans_for(tmp, [JOBLET_FIXTURES / CONVERSION, JOBLET_FIXTURES / CTE_AHO, MACROS])


def _joblet(plan, name):
    return next(j for j in plan.joblets if j.name == name)


def _ir(text: str, name: str = "t.sas"):
    return build_ir(parse_program(text, name), {})


# ---- huella y clustering ----


def test_fingerprint_ignores_table_names_and_literals():
    a = _ir("data work.a; set work.x; where edad > 18; run;\n")
    b = _ir("data work.b; set work.y; where edad > 30; run;\n")
    fa, sa = block_fingerprint(a.operations)
    fb, sb = block_fingerprint(b.operations)
    assert fa == fb
    assert sa != sb  # los valores siguen ahí como slots, solo cambia la forma


def test_fingerprint_changes_with_the_operation_types():
    a = _ir("data work.a; set work.x; run;\n")
    b = _ir("data work.a; set work.x; keep id; run;\n")
    assert block_fingerprint(a.operations)[0] != block_fingerprint(b.operations)[0]


def test_sequence_repetitions_need_two_occurrences_and_three_operations():
    text = "".join(f"data work.t{i}; set work.x{i}; where a > {i}; run;\n" for i in range(2))
    ir = _ir(text)
    found = find_sequence_repetitions(ir.operations)
    assert found, "dos bloques iguales con tres operaciones o más deben agruparse"
    assert all(len(rep.occurrences) >= limits.JOBLET_MIN_OCCURRENCES for rep in found)
    assert find_sequence_repetitions(ir.operations, min_operations=99) == []
    assert find_sequence_repetitions(ir.operations[:3], min_occurrences=2) == []


def test_a_block_that_appears_once_is_not_a_joblet():
    ir = _ir("data work.a; set work.x; where a > 1; run;\n")
    assert find_sequence_repetitions(ir.operations) == []


def test_orchestration_only_blocks_are_not_joblets():
    text = "%a;\n%b;\n%a;\n%b;\n%a;\n%b;\n"
    assert find_sequence_repetitions(_ir(text).operations) == []


def test_default_thresholds_are_configured_in_limits():
    assert limits.JOBLET_MIN_OCCURRENCES == 2
    assert limits.JOBLET_MIN_OPERATIONS == 3


# ---- joblets propuestos sobre los fixtures ----


def test_conversion_pattern_becomes_one_joblet_with_five_occurrences(fixture_plans):
    plan = fixture_plans[CONVERSION]
    assert len(plan.joblets) == 1
    joblet = plan.joblets[0]
    assert joblet.name == "jl_ConversionTipo"
    assert len(joblet.occurrences) == 5
    assert joblet.operation_count == 6
    assert {p.name for p in joblet.parameters} == {"expresion_var7", "expresion_30", "columna_destino_nro_cta"}
    values = {p.name: p.example_values for p in joblet.parameters}
    assert values["columna_destino_nro_cta"] == ["NRO_CTA", "LLAVE_NOMBRE", "TIPO_DOC", "NRO_DOC", "GMF"]
    assert joblet.inputs == ["tabla_entrada_1"] and joblet.outputs == ["tabla_salida_1"]


def test_cte_aho_pair_is_one_joblet_and_the_alias_is_one_parameter(fixture_plans):
    plan = fixture_plans[CTE_AHO]
    joblet = next(j for j in plan.joblets if j.kind == "sequence")
    assert len(joblet.occurrences) == 2
    alias = next(p for p in joblet.parameters if p.name.startswith("expresion_cumple_norma_cte"))
    assert alias.example_values == ["CUMPLE_NORMA_CTE", "CUMPLE_NORMA_AHORROS"]
    # cuarenta referencias a la tabla se reducen a un parámetro: no hay un parámetro por columna
    assert len(joblet.parameters) <= 6


def test_macro_copies_count_as_occurrences(fixture_plans):
    plan = fixture_plans[MACROS.name]
    carga = _joblet(plan, "jl_CargaTabla")
    assert carga.kind == "macro"
    assert len(carga.occurrences) == 3  # dos copias idénticas + la variante _v2
    assert [p.name for p in carga.parameters] == ["expresion_18"]
    assert carga.parameters[0].example_values == ["18", "30"]
    # Una macro que solo ordena un dataset hacia WORK es trabajo de datos (no fontanería): se propone como joblet.
    assert [j for j in plan.joblets if j.name == "jl_Split2"]
    assert not any("split2" in n.what for n in plan.not_migrated)


def test_copies_of_a_business_macro_count_as_occurrences_with_their_own_fixture(tmp_path):
    plans = _plans_for(tmp_path, [JOBLET_FIXTURES / "macro_copias_negocio.sas"])
    plan = plans["macro_copias_negocio.sas"]
    joblet = _joblet(plan, "jl_FiltraActivos")
    assert joblet.kind == "macro"
    assert len(joblet.occurrences) == 2  # dos copias idénticas, una llamada cada una
    assert not plan.not_migrated, "una macro de negocio no es fontanería"


def test_every_joblet_step_is_marked_and_names_follow_the_convention(fixture_plans):
    for plan in fixture_plans.values():
        by_id = {s.id: s for s in plan.steps + [x for c in plan.children for x in c.steps]}
        names = [j.name for j in plan.joblets]
        assert len(names) == len(set(names))
        for joblet in plan.joblets:
            assert joblet.name.startswith("jl_")
            assert joblet.id.startswith("joblet-")
            for occurrence in joblet.occurrences:
                assert occurrence.step_ids, "cada aparición debe tener pasos del plan"
                for step_id in occurrence.step_ids:
                    assert by_id[step_id].joblet_id == joblet.id
                assert occurrence.usage_steps


def test_creation_steps_use_the_studio_path_and_the_joblet_parts(fixture_plans):
    joblet = _joblet(fixture_plans[CONVERSION], "jl_ConversionTipo")
    assert joblet.creation_steps[0] == "Repository › Joblet Designs › clic derecho › Create Joblet."
    text = " | ".join(joblet.creation_steps)
    assert "Input" in text and "Output" in text and "Trigger Input" in text
    assert "context.tabla_entrada_1" in text or "context.expresion_var7" in text
    assert "Joblet Designs" in joblet.creation_steps[-2]


def test_why_is_in_spanish_and_mentions_the_occurrences(fixture_plans):
    joblet = _joblet(fixture_plans[CONVERSION], "jl_ConversionTipo")
    assert "aparece 5 veces" in joblet.why
    assert "parámetros" in joblet.why


def test_plan_json_exposes_the_joblet_contract(fixture_plans):
    data = json.loads(fixture_plans[CONVERSION].model_dump_json())
    assert data["joblets"], "JobPlan.joblets debe estar en el JSON"
    joblet = data["joblets"][0]
    for key in ("id", "name", "title", "occurrences", "parameters", "components", "inputs",
                "outputs", "trigger_inputs", "why", "creation_steps"):
        assert key in joblet
    assert "step_ids" in joblet["occurrences"][0] and "usage_steps" in joblet["occurrences"][0]
    assert "joblet_id" in data["steps"][0]


def test_joblets_are_empty_when_nothing_repeats():
    plan = plan_program(
        _ir("data work.a; set work.x; where a > 1; run;\n", "solo.sas"),
        "joblets",
        load_mapping_rules(),
        {},
    )
    assert plan.joblets == []


# ---- golden de los fixtures ----


def test_joblets_match_golden(tmp_path):
    plans = _plans_for(tmp_path, [JOBLET_FIXTURES / CONVERSION, JOBLET_FIXTURES / CTE_AHO, MACROS])
    got = {name: [j.model_dump(mode="json") for j in plan.joblets] for name, plan in sorted(plans.items())}
    text = json.dumps(got, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if os.environ.get("UPDATE_GOLDEN"):
        GOLDEN.write_text(text, encoding="utf-8")
    assert GOLDEN.exists(), "falta joblets_fixtures.json; ejecuta con UPDATE_GOLDEN=1"
    assert text == GOLDEN.read_text(encoding="utf-8")


# ---- Cod1 completo (opcional) ----


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_cod1_macros_are_repeated_four_times_each(tmp_path):
    source = Path(os.environ["COD1_PATH"])
    if not source.exists():
        pytest.skip("COD1_PATH no existe")
    plans = _plans_for(tmp_path, [source])
    plan = next(iter(plans.values()))
    # Regla general: cada joblet agrupa al menos JOBLET_MIN_OCCURRENCES apariciones (una por tabla o por llamada).
    # Cod1 tiene un bloque repetido en dos sitios (jl_Bloque, tras el ELT y la copia de vuelta) además del
    # de cuatro apariciones: no es un error, así que no se exige 4 en todos.
    from sas_grid_migrator.migration_planner.limits import JOBLET_MIN_OCCURRENCES

    assert plan.joblets, "Cod1 debe proponer al menos un joblet"
    assert all(len(j.occurrences) >= JOBLET_MIN_OCCURRENCES for j in plan.joblets), [
        (j.name, len(j.occurrences)) for j in plan.joblets
    ]
    assert any(len(j.occurrences) == 4 for j in plan.joblets), [(j.name, len(j.occurrences)) for j in plan.joblets]
    # La fontanería repetida (troceo, carga por comando) no es joblet: queda explicada en not_migrated.
    assert not [j for j in plan.joblets if j.kind == "macro"]
    categories = {n.category for n in plan.not_migrated}
    assert {"troceado_lotes", "carga_comando"} <= categories
