import pytest

from sas_grid_migrator.migration_planner.job_naming import (
    DEFAULT_NAME_TEMPLATE,
    TEMPLATE_TOKENS,
    BulkRule,
    bulk_preview,
    render_job_name,
    validate_job_name,
    validate_template,
)
from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.migration_planner.planner import unique_job_names


def _plan(program: str, job_name: str) -> JobPlan:
    return JobPlan(project_id="p", rules_version="r", program=program, sha256="h", job_name=job_name)


def test_template_constants():
    assert DEFAULT_NAME_TEMPLATE == "job_{programa}"
    assert TEMPLATE_TOKENS == ("proyecto", "carpeta", "programa")


def test_validate_job_name_rejects_names_that_are_not_identifiers():
    assert validate_job_name("2abc", taken=[]) == (
        "El nombre debe empezar con una letra o guion bajo y usar solo letras, números y guion bajo."
    )


def test_validate_job_name_rejects_names_longer_than_60():
    assert validate_job_name("a" * 61, taken=[]) == "El nombre no puede pasar de 60 caracteres."


def test_validate_job_name_compares_with_casefold():
    assert validate_job_name("JOB_A", taken=["job_a"]) == "Ya existe otro Job con ese nombre."


def test_validate_job_name_accepts_a_free_valid_name():
    assert validate_job_name("job_a", taken=[]) is None


def test_render_default_template_uses_the_program_stem():
    assert render_job_name("job_{programa}", project="Finanzas", program="lz/Cod 2.sas") == "job_cod_2"


def test_render_project_folder_and_program_tokens():
    assert (
        render_job_name("{proyecto}_{carpeta}_{programa}", project="Finanzas", program="lz/Cod 2.sas")
        == "finanzas_lz_cod_2"
    )


def test_render_collapses_empty_tokens_without_double_underscores():
    assert (
        render_job_name("{proyecto}_{carpeta}_{programa}", project="Finanzas", program="cod2.sas")
        == "finanzas_cod2"
    )


def test_render_prefixes_a_name_that_starts_with_a_digit():
    assert render_job_name("{proyecto}_{programa}", project="2024", program="lz/Cod 2.sas").startswith("job_")


def test_render_with_depth_prefixes_the_parent_folders_like_the_default_naming():
    assert render_job_name("job_{programa}", project="P", program="a/x/run.sas", depth=1) == "job_x_run"


def test_validate_template_requires_programa():
    assert validate_template("{proyecto}") == "La plantilla debe incluir {programa}."


def test_validate_template_rejects_unknown_tokens():
    assert validate_template("job_{programa}_{foo}") == "Token desconocido: {foo}."


def test_validate_template_accepts_the_default():
    assert validate_template(DEFAULT_NAME_TEMPLATE) is None


def test_bulk_prefix_proposes_new_names_without_errors():
    plans = [_plan("p/job_a.sas", "job_a"), _plan("p/job_b.sas", "job_b")]

    rows = bulk_preview(plans, BulkRule(mode="prefix", text="fin_"))

    assert [(row.current, row.proposed, row.error) for row in rows] == [
        ("job_a", "fin_job_a", None),
        ("job_b", "fin_job_b", None),
    ]


def test_bulk_replace_reports_a_collision_with_an_existing_job():
    plans = [_plan("p/job_a.sas", "job_a"), _plan("p/a.sas", "a")]
    rule = BulkRule(mode="replace", find="job_", replace_with="")

    rows = bulk_preview(plans, rule)

    assert rows[0].proposed == "a"
    assert rows[0].error == "Ya existe otro Job con ese nombre."
    assert rows[1].proposed == "a"
    assert rows[1].error is None


def test_bulk_rows_that_collide_with_each_other_both_get_an_error():
    plans = [_plan("p/x_a.sas", "x_a"), _plan("p/y_a.sas", "y_a")]

    rows = bulk_preview(plans, BulkRule(mode="regex", find="^[xy]_", replace_with="z_"))

    assert [row.proposed for row in rows] == ["z_a", "z_a"]
    assert [row.error for row in rows] == ["Ya existe otro Job con ese nombre."] * 2


def test_bulk_unchanged_rows_keep_their_name_and_no_error():
    plans = [_plan("p/job_a.sas", "job_a")]

    rows = bulk_preview(plans, BulkRule(mode="prefix", text=""))

    assert rows[0].proposed == rows[0].current == "job_a"
    assert rows[0].error is None


def test_bulk_only_previews_the_requested_programs():
    plans = [_plan("p/job_a.sas", "job_a"), _plan("p/job_b.sas", "job_b")]

    rows = bulk_preview(plans, BulkRule(mode="prefix", text="fin_", programs=["p/job_b.sas"]))

    assert [row.program for row in rows] == ["p/job_b.sas"]
    assert rows[0].proposed == "fin_job_b"


def test_bulk_regex_rejects_nested_quantifiers_without_hanging():
    with pytest.raises(ValueError, match="El patrón es demasiado complejo."):
        bulk_preview([_plan("p/a.sas", "a")], BulkRule(mode="regex", find="(a+)+$"))


@pytest.mark.parametrize("find", ["(a|aa)+$", "((a+)b)+", "(a+)+$"])
def test_bulk_regex_rejects_catastrophic_nested_patterns(find):
    with pytest.raises(ValueError, match="El patrón es demasiado complejo."):
        bulk_preview([_plan("p/a.sas", "a")], BulkRule(mode="regex", find=find))


@pytest.mark.parametrize("find", ["(abc)+", "(a|b)", "x(y)z", "[a-z]+", r"job_(\d+)"])
def test_bulk_regex_accepts_benign_groups_and_quantifiers(find):
    rows = bulk_preview([_plan("p/job_1.sas", "job_1")], BulkRule(mode="regex", find=find, replace_with="k"))

    assert len(rows) == 1


def test_bulk_regex_rejects_patterns_longer_than_200_characters():
    with pytest.raises(ValueError, match="El patrón es demasiado complejo."):
        bulk_preview([_plan("p/a.sas", "a")], BulkRule(mode="regex", find="a" * 201))


def test_bulk_regex_that_does_not_compile_raises_value_error():
    with pytest.raises(ValueError):
        bulk_preview([_plan("p/a.sas", "a")], BulkRule(mode="regex", find="("))


def test_unique_job_names_uses_the_given_name_generator():
    def name_with_folders(parts: tuple[str, ...], depth: int) -> str:
        return f"x_{parts[-2].lower()}_{parts[-1].split('.')[0]}"

    plans = [_plan("DB2/bulkload.sas", "job_bulkload"), _plan("Hadoop/bulkload.sas", "job_bulkload")]

    unique_job_names(plans, name_with_folders)

    assert [plan.job_name for plan in plans] == ["x_db2_bulkload", "x_hadoop_bulkload"]
