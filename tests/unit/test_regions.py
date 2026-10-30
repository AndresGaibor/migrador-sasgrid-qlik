"""Regiones largas repetidas (plegado a joblets de cualquier longitud): pruebas sintéticas y genéricas.

Los pasos son sintéticos: no dependen de ningún script concreto. Cada copia de una cadena tiene la misma
estructura; lo que cambia entre copias es un sub-token de un identificador (el segmento) o un paso extra.
"""

from sas_grid_migrator.migration_planner import regions as R
from sas_grid_migrator.migration_planner.models import Connection, Expression, JobPlan, PlanStep
from sas_grid_migrator.sas_parser.ast import Loc

SEGMENTS = ["AHO", "CTE", "NEQ"]


def _step(key: str, line: int, *, prev: str | None, expr: str, comp: str = "tMap", optype: str = "compute") -> PlanStep:
    return PlanStep(
        id=key,
        order=line,
        subjob="bloque",
        action="add_component",
        component_candidate=comp,
        operation_type=optype,
        purpose=f"paso {key}",
        evidence=Loc(file="x.sas", line=line, end_line=line),
        connections=[Connection(type="Main", from_step=prev)] if prev else [],
        expressions=[Expression(sas=expr, line=line)],
    )


def _chain(prefix: str, first_line: int, length: int, *, segment: str, extra_at: int | None = None) -> list[PlanStep]:
    """Cadena de `length` pasos. El identificador lleva el segmento; `extra_at` inserta un paso distinto."""
    steps: list[PlanStep] = []
    prev: str | None = None
    line = first_line
    for k in range(length):
        key = f"{prefix}-{k}"
        # Cada posición tiene una forma distinta (k+1 términos); el segmento es el único cambio entre copias.
        steps.append(_step(key, line, prev=prev, expr=f"SALDO_{segment} " + " ".join(["+ X"] * (k + 1))))
        prev, line = key, line + 1
        if extra_at == k:
            extra = f"{prefix}-extra"
            steps.append(_step(extra, line, prev=prev, expr="CONTEO_EXTRA + 9", comp="tFilterRow", optype="filter"))
            prev, line = extra, line + 1
    return steps


def _plan(steps: list[PlanStep]) -> JobPlan:
    return JobPlan(project_id="p", rules_version="r", program="x.sas", job_name="job_x", steps=steps)


def _three_copies(length: int = 10, extra_in_copy: int | None = None) -> list[PlanStep]:
    steps: list[PlanStep] = []
    line = 1
    for index, segment in enumerate(SEGMENTS):
        extra = 3 if index == extra_in_copy else None
        chain = _chain(f"c{index}", line, length, segment=segment, extra_at=extra)
        steps += chain
        line += len(chain) + 5
    return steps


def test_three_identical_chains_are_one_joblet_with_two_uses():
    plan = _plan(_three_copies())
    notices = R.fold_regions(plan)
    assert notices == []
    assert len(plan.joblets) == 1
    joblet = plan.joblets[0]
    assert len(joblet.occurrences) == 3
    # El cuerpo (10 pasos) conserva sus pasos; cada una de las otras dos copias es un paso de uso.
    assert len(plan.steps) == 12
    uses = [s for s in plan.steps if s.alternatives == ["Joblet"]]
    assert len(uses) == 2
    assert all(s.component_candidate == "por_determinar" and s.joblet_id == joblet.id for s in uses)
    assert all(s.purpose.startswith(f"Usa el joblet {joblet.name}") for s in uses)
    body = [s for s in plan.steps if s.joblet_id == joblet.id and s.alternatives != ["Joblet"]]
    assert len(body) == 10


def test_segment_sub_token_becomes_one_parameter_with_one_value_per_copy():
    plan = _plan(_three_copies())
    R.fold_regions(plan)
    joblet = plan.joblets[0]
    assert len(joblet.parameters) == 1
    parameter = joblet.parameters[0]
    assert parameter.name == "identificador_aho"
    assert [occ.values[parameter.name] for occ in joblet.occurrences] == ["AHO", "CTE", "NEQ"]
    assert parameter.context_variable == "context.identificador_aho"


def test_one_extra_step_in_a_copy_is_an_optional_parameter_and_a_notice():
    plan = _plan(_three_copies(extra_in_copy=1))
    notices = R.fold_regions(plan)
    assert len(plan.joblets) == 1
    joblet = plan.joblets[0]
    names = {p.name for p in joblet.parameters}
    assert any(name.startswith("paso_opcional_") for name in names)
    optional = next(p for p in joblet.parameters if p.name.startswith("paso_opcional_"))
    assert sorted(occ.values[optional.name] for occ in joblet.occurrences) == ["false", "false", "true"]
    assert notices and "divergencia entre copias" in notices[0]
    assert plan.job_status == "needs_review"
    assert any("divergencia entre copias" in text for text in plan.unresolved)
    assert "Divergencia entre copias" in joblet.why


def test_non_repeated_steps_are_left_intact():
    steps = [
        _step(f"u{k}", k + 1, prev=f"u{k - 1}" if k else None, expr=f"VALOR_{k} * {k + 2}", comp="tMap", optype="compute")
        for k in range(12)
    ]
    steps = [s.model_copy(update={"component_candidate": f"comp_{k}", "operation_type": f"tipo_{k}"}) for k, s in enumerate(steps)]
    plan = _plan(steps)
    before = [s.model_dump() for s in plan.steps]
    notices = R.fold_regions(plan)
    assert notices == []
    assert plan.joblets == []
    assert [s.model_dump() for s in plan.steps] == before


def test_find_regions_are_disjoint_and_ordered():
    block = [1, 2, 3, 4, 5, 6, 7]
    tokens = block + [100] + block + [200] + block
    found = R.find_regions(tokens, min_steps=6)
    assert len(found) == 1
    spans = found[0].spans
    assert len(spans) == 3
    covered = [p for start, end in spans for p in range(start, end)]
    assert len(covered) == len(set(covered))
    assert [start for start, _ in spans] == sorted(start for start, _ in spans)


def test_overlapping_repetitions_claim_each_step_once():
    tokens = [1, 2, 3, 4, 5, 6, 7, 8] * 2 + [9] + [1, 2, 3, 4, 5, 6, 7, 8]
    found = R.find_regions(tokens, min_steps=6)
    claimed: list[int] = []
    for region in found:
        for start, end in region.spans:
            claimed += list(range(start, end))
    assert len(claimed) == len(set(claimed))


def test_fold_is_deterministic():
    first = _plan(_three_copies(extra_in_copy=2))
    second = _plan(_three_copies(extra_in_copy=2))
    R.fold_regions(first)
    R.fold_regions(second)
    assert first.model_dump_json() == second.model_dump_json()


def test_sub_tokens_split_by_underscore_case_and_digits():
    assert R.subtokens("cte_ahorros2") == ["CTE", "AHORROS", "2"]
    assert R.subtokens("NormaCte_1") == ["NORMA", "CTE", "1"]


def test_abstract_text_keeps_keywords_and_hides_identifiers_and_literals():
    assert R.abstract_text("CUMPLE_NORMA_CTE = 'A' and x > 10") == "ID = S and ID > #"
