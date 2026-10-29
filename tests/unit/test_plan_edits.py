from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import (
    Expression,
    JobPlan,
    PlanSet,
    PlanStep,
)
from sas_grid_migrator.migration_planner.service import load_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.ast import Loc


def test_saved_job_and_expression_edits_overlay_only_when_source_matches(tmp_path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("Finanzas")
    plan = JobPlan(
        project_id=project.id,
        rules_version="r1",
        program="daily.sas",
        job_name="job_daily",
        steps=[
            PlanStep(
                id="step-1",
                order=1,
                subjob="",
                action="configure",
                purpose="Filtrar registros",
                evidence=Loc(file="daily.sas", line=1, end_line=1),
                expressions=[Expression(sas="amount > 0", talend="row.amount > 0", line=1)],
            )
        ],
    )
    store.plans_path(project.id).parent.mkdir(parents=True, exist_ok=True)
    store.plans_path(project.id).write_text(
        PlanSet(project_id=project.id, rules_version="r1", plans=[plan]).model_dump_json(),
        encoding="utf-8",
    )
    store.set_job_override(project.id, "daily.sas", "carga_diaria", "Carga diaria")
    store.set_expression_override(
        project.id, "daily.sas", "step-1", 0, "amount > 0", "input_row.amount > 0"
    )

    edited = load_plans(store, project.id)
    raw = load_plans(store, project.id, with_edits=False)

    assert edited is not None
    assert edited.plans[0].job_name == "carga_diaria"
    assert edited.plans[0].job_name_edited
    assert edited.plans[0].description == "Carga diaria"
    expression = edited.plans[0].steps[0].expressions[0]
    assert expression.talend == "input_row.amount > 0"
    assert expression.talend_edited
    assert raw is not None
    assert raw.plans[0].job_name == "job_daily"
    assert not raw.plans[0].job_name_edited
    assert raw.plans[0].steps[0].expressions[0].talend == "row.amount > 0"


def test_expression_edit_is_ignored_if_the_sas_source_changed(tmp_path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("Finanzas")
    plan = JobPlan(
        project_id=project.id,
        rules_version="r1",
        program="daily.sas",
        job_name="job_daily",
        steps=[
            PlanStep(
                id="step-1",
                order=1,
                subjob="",
                action="configure",
                purpose="Filtrar registros",
                evidence=Loc(file="daily.sas", line=1, end_line=1),
                expressions=[Expression(sas="amount > 5", talend="row.amount > 5", line=1)],
            )
        ],
    )
    store.plans_path(project.id).parent.mkdir(parents=True, exist_ok=True)
    store.plans_path(project.id).write_text(
        PlanSet(project_id=project.id, rules_version="r1", plans=[plan]).model_dump_json(),
        encoding="utf-8",
    )
    store.set_expression_override(
        project.id, "daily.sas", "step-1", 0, "amount > 0", "input_row.amount > 0"
    )

    edited = load_plans(store, project.id)

    assert edited is not None
    assert edited.plans[0].steps[0].expressions[0].talend == "row.amount > 5"
    assert not edited.plans[0].steps[0].expressions[0].talend_edited


def test_job_override_colliding_with_another_generated_name_is_ignored(tmp_path):
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("Finanzas")
    plans = PlanSet(
        project_id=project.id,
        rules_version="r1",
        plans=[
            JobPlan(project_id=project.id, rules_version="r1", program="a.sas", job_name="job_a"),
            JobPlan(project_id=project.id, rules_version="r1", program="b.sas", job_name="job_b"),
        ],
    )
    store.plans_path(project.id).parent.mkdir(parents=True, exist_ok=True)
    store.plans_path(project.id).write_text(plans.model_dump_json(), encoding="utf-8")
    store.set_job_override(project.id, "a.sas", "JOB_B", None)

    loaded = load_plans(store, project.id)

    assert loaded is not None
    assert loaded.plans[0].job_name == "job_a"
    assert loaded.plans[0].rename_ignored == "JOB_B"
