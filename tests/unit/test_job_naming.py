import pytest

from sas_grid_migrator.migration_planner.job_naming import (
    BulkRule,
    bulk_preview,
    render_job_name,
    validate_job_name,
    validate_template,
)
from sas_grid_migrator.migration_planner.models import JobPlan


def _plan(program: str, job_name: str) -> JobPlan:
    return JobPlan(project_id="p", rules_version="r", program=program, job_name=job_name)


def test_job_name_validation_checks_identifier_size_and_case_insensitive_duplicates():
    assert validate_job_name("job_a", taken=[]) is None
    assert validate_job_name("2abc", taken=[]) == (
        "El nombre debe empezar con una letra o guion bajo y usar solo letras, números y guion bajo."
    )
    assert validate_job_name("a" * 61, taken=[]) == "El nombre no puede pasar de 60 caracteres."
    assert validate_job_name("JOB_A", taken=["job_a"]) == "Ya existe otro Job con ese nombre."


def test_template_validation_and_name_rendering_use_project_and_source_path():
    assert validate_template("{proyecto}") == "La plantilla debe incluir {programa}."
    assert validate_template("job_{programa}_{foo}") == "Token desconocido: {foo}."
    assert validate_template("job_{programa}") is None
    assert render_job_name("job_{programa}", project="Finanzas", program="lz/Cod 2.sas") == "job_cod_2"
    assert render_job_name(
        "{proyecto}_{carpeta}_{programa}", project="Finanzas", program="lz/Cod 2.sas"
    ) == "finanzas_lz_cod_2"
    assert render_job_name("job_{programa}", project="Finanzas", program="a/x/run.sas", depth=1) == "job_x_run"


def test_bulk_preview_reports_duplicate_proposals_without_losing_other_rows():
    plans = [_plan("a.sas", "job_a"), _plan("b.sas", "job_b")]

    rows = bulk_preview(plans, BulkRule(mode="replace", find="job_", replace_with="same_"))

    assert [(row.program, row.proposed) for row in rows] == [
        ("a.sas", "same_a"), ("b.sas", "same_b")
    ]
    assert all(row.error is None for row in rows)
    with pytest.raises(ValueError, match="complejo"):
        bulk_preview(plans, BulkRule(mode="regex", find="(a+)+$", replace_with="x"))


@pytest.mark.parametrize("pattern", ["(a+)+$", "(a|aa)+$", "((a+)b)+", "((a))+x"])
def test_regex_guard_rejects_nested_quantifiers_that_backtrack(pattern):
    with pytest.raises(ValueError, match="complejo"):
        bulk_preview([_plan("a.sas", "job_a")], BulkRule(mode="regex", find=pattern, replace_with="x"))


@pytest.mark.parametrize("pattern", ["(abc)+", "(a|b)", "x(y)z", "[a-z]+", r"job_(\d+)", "^job_", r"(job)_(\d+)"])
def test_regex_guard_accepts_benign_patterns(pattern):
    rows = bulk_preview([_plan("a.sas", "job_a")], BulkRule(mode="regex", find=pattern, replace_with="x"))
    assert rows[0].error is None
