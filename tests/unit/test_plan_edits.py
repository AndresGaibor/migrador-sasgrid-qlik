"""Las ediciones del usuario son capas que se aplican al cargar; plans.json nunca las recibe."""

import json

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import (
    Expression,
    JobPlan,
    PlanSet,
    PlanStep,
)
from sas_grid_migrator.migration_planner.service import (
    NAME_TEMPLATE_KEY,
    current_name_template,
    generate_plans,
    get_plan,
    load_plans,
)
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.ast import Loc


def _step(step_id: str, *expressions: Expression) -> PlanStep:
    return PlanStep(
        id=step_id,
        order=1,
        subjob="main",
        action="configure",
        purpose="Calcular",
        evidence=Loc(file="a.sas", line=1, end_line=1),
        expressions=list(expressions),
    )


def _plan(program: str, job_name: str, *steps: PlanStep) -> JobPlan:
    return JobPlan(
        project_id="x",
        rules_version="rules-1",
        program=program,
        job_name=job_name,
        steps=list(steps),
    )


def _project(tmp_path, *plans: JobPlan) -> tuple[Store, str]:
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("Proyecto Demo")
    for plan in plans:
        plan.project_id = project.id
    path = store.plans_path(project.id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        PlanSet(
            project_id=project.id, rules_version="rules-1", plans=list(plans)
        ).model_dump_json(),
        encoding="utf-8",
    )
    return store, project.id


def _source_project(tmp_path, name: str, files: dict[str, str]) -> tuple[Store, str]:
    source = tmp_path / "sas"
    for relative, content in files.items():
        path = source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project(name)
    store.import_batch(project.id, source)
    return store, project.id


def test_job_override_renames_the_plan_and_marks_it(tmp_path):
    store, pid = _project(tmp_path, _plan("a.sas", "job_a"))
    store.set_job_override(pid, "a.sas", "mi_job", None)

    plan = load_plans(store, pid).plans[0]
    assert plan.job_name == "mi_job"
    assert plan.job_name_edited is True
    assert plan.rename_ignored is None

    raw = load_plans(store, pid, with_edits=False).plans[0]
    assert raw.job_name == "job_a"
    assert raw.job_name_edited is False
    assert get_plan(store, pid, "a.sas", with_edits=False).job_name == "job_a"
    assert get_plan(store, pid, "a.sas").job_name == "mi_job"
    # el archivo en disco nunca recibe la edición
    on_disk = json.loads(store.plans_path(pid).read_text(encoding="utf-8"))
    assert on_disk["plans"][0]["job_name"] == "job_a"


def test_description_override_is_applied(tmp_path):
    store, pid = _project(tmp_path, _plan("a.sas", "job_a"))
    store.set_job_override(pid, "a.sas", None, "Carga diaria")

    assert load_plans(store, pid).plans[0].description == "Carga diaria"
    assert load_plans(store, pid, with_edits=False).plans[0].description is None


def test_override_colliding_with_a_generated_name_is_ignored(tmp_path):
    store, pid = _project(tmp_path, _plan("a.sas", "job_a"), _plan("b.sas", "job_b"))
    store.set_job_override(pid, "a.sas", "JOB_B", None)

    a, b = load_plans(store, pid).plans
    assert a.job_name == "job_a"
    assert a.job_name_edited is False
    assert a.rename_ignored == "JOB_B"
    assert b.job_name == "job_b"


def test_two_overrides_with_the_same_name_keep_only_the_first_by_program(tmp_path):
    store, pid = _project(tmp_path, _plan("a.sas", "job_a"), _plan("b.sas", "job_b"))
    store.set_job_override(pid, "b.sas", "Compartido", None)
    store.set_job_override(pid, "a.sas", "compartido", None)

    a, b = load_plans(store, pid).plans
    assert (a.job_name, a.job_name_edited) == ("compartido", True)
    assert (b.job_name, b.rename_ignored) == ("job_b", "Compartido")


def test_expression_override_applies_only_when_the_sas_matches(tmp_path):
    plan = _plan(
        "a.sas",
        "job_a",
        _step(
            "s1",
            Expression(sas="x + 1", talend="x + 1", line=3, requires_semantic_validation=True),
        ),
    )
    store, pid = _project(tmp_path, plan)
    store.set_expression_override(pid, "a.sas", "s1", 0, "x + 1", "row1.x + 1")

    expression = load_plans(store, pid).plans[0].steps[0].expressions[0]
    assert expression.talend == "row1.x + 1"
    assert expression.talend_edited is True
    assert expression.requires_semantic_validation is True

    # la fuente cambió: el override guardado ya no corresponde a esta expresión
    store.set_expression_override(pid, "a.sas", "s1", 0, "x + 2", "row1.x + 2")
    stale = load_plans(store, pid).plans[0].steps[0].expressions[0]
    assert stale.talend == "x + 1"
    assert stale.talend_edited is False


def test_expression_override_with_unknown_index_is_ignored(tmp_path):
    plan = _plan("a.sas", "job_a", _step("s1", Expression(sas="x", talend="x", line=1)))
    store, pid = _project(tmp_path, plan)
    store.set_expression_override(pid, "a.sas", "s1", 5, "x", "otro")

    assert load_plans(store, pid).plans[0].steps[0].expressions[0].talend == "x"


def test_overrides_survive_regenerating_the_plans(tmp_path):
    store, pid = _source_project(
        tmp_path, "Demo", {"carga.sas": "data work.out; set work.in; run;"}
    )
    store.set_job_override(pid, "carga.sas", "mi_carga", None)

    generate_plans(store, pid)

    assert [p.job_name for p in load_plans(store, pid).plans] == ["mi_carga"]
    assert load_plans(store, pid, with_edits=False).plans[0].job_name == "job_carga"


def _expression_step(ps: PlanSet) -> PlanStep:
    return next(step for plan in ps.plans for step in plan.steps if step.expressions)


def _rewrite_sources(tmp_path, store: Store, pid: str, files: dict[str, str]) -> None:
    source = tmp_path / "sas"
    for relative, content in files.items():
        (source / relative).write_text(content, encoding="utf-8")
    store.import_batch(pid, source)


def test_expression_override_is_ignored_after_regeneration_changes_its_sas(tmp_path):
    body = "data work.out;\n  set work.in;\n  y = x + {n};\nrun;\n"
    store, pid = _source_project(tmp_path, "Demo", {"calc.sas": body.format(n=1)})
    generate_plans(store, pid)
    step = _expression_step(load_plans(store, pid, with_edits=False))
    store.set_expression_override(pid, "calc.sas", step.id, 0, "x + 1", "row.x + 1")
    assert _expression_step(load_plans(store, pid)).expressions[0].talend == "row.x + 1"

    _rewrite_sources(tmp_path, store, pid, {"calc.sas": body.format(n=2)})
    generate_plans(store, pid)

    expression = _expression_step(load_plans(store, pid)).expressions[0]
    assert expression.sas == "x + 2"
    assert expression.talend == "(input_row.x + 2)"
    assert expression.talend_edited is False


def test_rename_that_collides_after_regeneration_is_ignored_and_reported(tmp_path):
    body = "data work.o; set work.i; run;"
    store, pid = _source_project(tmp_path, "Demo", {"a.sas": body, "b.sas": body})
    generate_plans(store, pid)
    store.set_job_override(pid, "a.sas", "job_c", None)
    assert {p.program: p.job_name for p in load_plans(store, pid).plans}["a.sas"] == "job_c"

    _rewrite_sources(tmp_path, store, pid, {"c.sas": body})
    generate_plans(store, pid)

    a = {p.program: p for p in load_plans(store, pid).plans}["a.sas"]
    assert a.job_name == "job_a"
    assert a.job_name_edited is False
    assert a.rename_ignored == "job_c"


def test_generate_plans_uses_the_saved_name_template(tmp_path):
    store, pid = _source_project(
        tmp_path, "Proyecto Demo", {"carga.sas": "data work.out; set work.in; run;"}
    )

    assert current_name_template(store) == "job_{programa}"
    assert generate_plans(store, pid).plans[0].job_name == "job_carga"

    store.set_setting(NAME_TEMPLATE_KEY, "{proyecto}_{programa}")
    assert current_name_template(store) == "{proyecto}_{programa}"
    assert generate_plans(store, pid).plans[0].job_name == "proyecto_demo_carga"


def test_unique_names_follow_the_template(tmp_path):
    body = "data work.o; set work.i; run;"
    store, pid = _source_project(
        tmp_path, "Demo", {"DB2/bulkload.sas": body, "Hadoop/bulkload.sas": body}
    )

    names = {p.program: p.job_name for p in generate_plans(store, pid).plans}

    assert names == {
        "DB2/bulkload.sas": "job_db2_bulkload",
        "Hadoop/bulkload.sas": "job_hadoop_bulkload",
    }
