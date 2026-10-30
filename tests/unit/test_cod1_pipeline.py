"""Carga por transferencia al motor (Cod1, sin nombres propios): un joblet con una ocurrencia por tabla,
sin hijos, sin tHash y con el contexto mínimo. Las aserciones son de estructura, no de nombres."""

import os
import tempfile
from pathlib import Path

import pytest

from tests.support.cache import cached_planset

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "cod1" / "cod1_carga_impala.sas"


def _plan(source: Path, tmp_path: Path):
    # Caché de disco por contenido (tests/support/cache.py): el Cod1 completo se planifica una vez.
    return cached_planset(source).plans[0]


def _all_steps(plan):
    return plan.steps + [s for child in plan.children for s in child.steps]


def _counted_once(plan) -> int:
    """Pasos del plan con cada joblet contado una vez: su cuerpo (los pasos de una aparición) más un paso por
    cada uso (`Usa el joblet ...`). Las demás apariciones que conservan sus pasos no cuentan."""
    steps = _all_steps(plan)
    by_id = {step.id: step for step in steps}
    usage = {step.id for step in steps if step.alternatives == ["Joblet"]}
    body_ids: set[str] = set()
    for joblet in plan.joblets:
        for occurrence in joblet.occurrences:
            ids = [sid for sid in occurrence.step_ids if sid in by_id and sid not in usage]
            if ids:
                body_ids.update(ids)
                break
    return sum(1 for step in steps if (not step.joblet_id) or step.id in body_ids or step.id in usage)


def _transfer_joblet(plan):
    """El joblet que se repite más: en Cod1 es la transferencia al motor de cada tabla."""
    return max(plan.joblets, key=lambda joblet: len(joblet.occurrences))


def _assert_transfer_contract(plan, occurrences: int) -> None:
    assert not plan.children, [c.name for c in plan.children]
    assert not [s for s in _all_steps(plan) if s.component_candidate.startswith("tHash")]
    joblet = _transfer_joblet(plan)
    assert len(joblet.occurrences) == occurrences
    assert joblet.parameters, "las ocurrencias deben distinguirse por parámetros"
    # Ninguna tabla WORK intermedia se escribe ni se pasa al joblet.
    assert not [s for s in _all_steps(plan) if s.operation_type == "write" and "work." in s.purpose.lower()]
    assert len(plan.context_variables) <= 12


def test_fixture_transfers_are_one_joblet_without_children(tmp_path):
    plan = _plan(FIXTURE, tmp_path)
    _assert_transfer_contract(plan, occurrences=2)
    assert not plan.job_parts
    assert _counted_once(plan) <= 20


def test_fixture_transfer_occurrences_carry_their_values(tmp_path):
    plan = _plan(FIXTURE, tmp_path)
    joblet = _transfer_joblet(plan)
    values = {value for occurrence in joblet.occurrences for value in occurrence.values.values()}
    assert {"Acura", "BMW"} <= values, values


def test_fixture_fontaneria_is_not_migrated(tmp_path):
    plan = _plan(FIXTURE, tmp_path)
    categories = {entry.category for entry in plan.not_migrated}
    # La fontanería del cuerpo de la carga no genera pasos: queda registrada en not_migrated.
    assert len(categories) >= 2, categories


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_full_cod1_has_four_transfer_occurrences_and_no_children():
    source = Path(os.environ["COD1_PATH"])
    if not source.exists():
        pytest.skip("COD1_PATH no existe")
    plan = _plan(source, Path(tempfile.mkdtemp()))
    _assert_transfer_contract(plan, occurrences=4)
    assert len(plan.steps) <= 25, [s.id for s in plan.steps]
    assert not plan.job_parts


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_full_cod1_single_job_under_twenty_steps():
    source = Path(os.environ["COD1_PATH"])
    if not source.exists():
        pytest.skip("COD1_PATH no existe")
    plan = _plan(source, Path(tempfile.mkdtemp()))
    assert not plan.job_parts
    assert _counted_once(plan) <= 20
