from sas_grid_migrator.migration_planner.models import ChildJob, JobPlan, PlanSet, PlanStep
from sas_grid_migrator.migration_planner.progress import compute_progress, pending_groups
from sas_grid_migrator.sas_parser.ast import Loc


def _row(steps: int = 0, done: int = 0, studio_status: str = "not_checked") -> dict:
    return {"steps": steps, "done": done, "studio_status": studio_status}


def _stages(progress) -> dict:
    return {stage.key: stage for stage in progress.stages}


def _step(step_id: str, *, pending: list[str] | None = None, status: str = "propuesto") -> PlanStep:
    return PlanStep(
        id=step_id,
        order=1,
        subjob="main",
        action="configure",
        purpose="Paso de prueba",
        pending=pending or [],
        status=status,
        evidence=Loc(file="a.sas", line=1, end_line=1),
    )


def _plan_set(*plans: JobPlan) -> PlanSet:
    return PlanSet(project_id="p1", rules_version="rules-1", plans=list(plans), confirmation="")


def test_empty_project_points_to_upload():
    progress = compute_progress(files=0, processing_status=None, plan_rows=None, batch_status=None)

    stages = _stages(progress)
    assert stages["upload"].status == "current"
    assert all(stages[key].status == "todo" for key in ("analysis", "guides", "studio", "complete", "verify"))
    assert progress.next is not None
    assert progress.next.key == "upload"
    assert progress.next.tab == "importar"


def test_running_analysis_is_current_and_points_to_summary():
    progress = compute_progress(files=5, processing_status="running", plan_rows=None, batch_status=None)

    stages = _stages(progress)
    assert stages["upload"].status == "done"
    assert stages["analysis"].status == "current"
    assert stages["analysis"].detail == "en curso"
    assert progress.next is not None
    assert progress.next.key == "analysis"
    assert progress.next.tab == "resumen"


def test_queued_analysis_is_current():
    progress = compute_progress(files=5, processing_status="queued", plan_rows=None, batch_status=None)

    assert _stages(progress)["analysis"].status == "current"


def test_failed_analysis_is_blocked_and_is_next():
    progress = compute_progress(files=5, processing_status="failed", plan_rows=None, batch_status=None)

    stages = _stages(progress)
    assert stages["analysis"].status == "blocked"
    assert stages["guides"].status == "todo"
    assert progress.next is not None
    assert progress.next.key == "analysis"


def test_interrupted_analysis_is_blocked():
    progress = compute_progress(files=5, processing_status="interrupted", plan_rows=None, batch_status=None)

    assert _stages(progress)["analysis"].status == "blocked"


def test_guides_done_without_batch_points_to_studio():
    progress = compute_progress(
        files=5,
        processing_status="completed",
        plan_rows=[_row(steps=10, done=0)],
        batch_status=None,
    )

    stages = _stages(progress)
    assert stages["analysis"].status == "done"
    assert stages["guides"].status == "done"
    assert stages["studio"].status == "current"
    assert progress.next is not None
    assert progress.next.key == "studio"
    assert progress.next.tab == "planes"


def test_applied_batch_with_pending_steps_points_to_complete():
    progress = compute_progress(
        files=5,
        processing_status="completed",
        plan_rows=[_row(steps=10, done=3)],
        batch_status="applied",
    )

    stages = _stages(progress)
    assert stages["studio"].status == "done"
    assert stages["complete"].status == "current"
    assert stages["complete"].detail == "3 de 10 pasos"
    assert stages["verify"].status == "todo"
    assert progress.next is not None
    assert progress.next.key == "complete"


def test_everything_done_has_no_next_action():
    progress = compute_progress(
        files=5,
        processing_status="completed",
        plan_rows=[_row(steps=10, done=10, studio_status="verified"), _row(steps=0)],
        batch_status="applied",
    )

    assert all(stage.status == "done" for stage in progress.stages)
    assert progress.next is None


def test_steps_zero_jobs_are_ignored_for_complete_and_verify():
    progress = compute_progress(
        files=1,
        processing_status="completed",
        plan_rows=[_row(steps=0), _row(steps=4, done=4, studio_status="verified")],
        batch_status=None,
    )

    stages = _stages(progress)
    assert stages["complete"].status == "done"
    assert stages["verify"].status == "done"


def test_only_zero_step_jobs_do_not_mark_the_project_done():
    progress = compute_progress(
        files=1,
        processing_status="completed",
        plan_rows=[_row(steps=0)],
        batch_status=None,
    )

    stages = _stages(progress)
    assert stages["complete"].status != "done"
    assert stages["verify"].status != "done"
    assert progress.next is not None
    assert progress.next.key != "verify"


def test_complete_done_marks_studio_done_without_batch():
    progress = compute_progress(
        files=1,
        processing_status="completed",
        plan_rows=[_row(steps=2, done=2, studio_status="pending")],
        batch_status=None,
    )

    stages = _stages(progress)
    assert stages["studio"].status == "done"
    assert stages["verify"].status == "current"
    assert progress.next is not None
    assert progress.next.key == "verify"


def test_conflicting_batch_blocks_studio():
    progress = compute_progress(
        files=5,
        processing_status="completed",
        plan_rows=[_row(steps=2, done=0)],
        batch_status="conflict",
    )

    stages = _stages(progress)
    assert stages["studio"].status == "blocked"
    assert progress.next is not None
    assert progress.next.key == "studio"


def test_running_batch_is_current_studio():
    progress = compute_progress(
        files=5,
        processing_status="completed",
        plan_rows=[_row(steps=2, done=0)],
        batch_status="running",
    )

    assert _stages(progress)["studio"].status == "current"


def test_pending_groups_group_exact_text_across_jobs_and_skip_discarded():
    first = JobPlan(
        project_id="p1",
        rules_version="rules-1",
        program="a.sas",
        job_name="job_a",
        steps=[
            _step("a-1", pending=["sistema y tabla de destino"]),
            _step("a-2", pending=["ruta, delimitador"]),
        ],
    )
    second = JobPlan(
        project_id="p1",
        rules_version="rules-1",
        program="b.sas",
        job_name="job_b",
        steps=[
            _step("b-1", pending=["sistema y tabla de destino"]),
            _step("b-2", pending=["ruta, delimitador"], status="descartado"),
        ],
    )

    groups = pending_groups(_plan_set(first, second))

    assert [(group.reason, group.steps) for group in groups] == [
        ("sistema y tabla de destino", 2),
        ("ruta, delimitador", 1),
    ]
    assert len(groups[0].programs) == 2
    assert [program.program for program in groups[0].programs] == ["a.sas", "b.sas"]
    assert groups[0].programs[0].job_name == "job_a"
    assert groups[0].programs[0].step_ids == ["a-1"]
    assert groups[1].programs[0].step_ids == ["a-2"]


def test_pending_groups_count_child_macro_steps():
    plan = JobPlan(
        project_id="p1",
        rules_version="rules-1",
        program="main.sas",
        job_name="job_main",
        steps=[_step("m-1", pending=["credenciales"])],
        children=[ChildJob(name="macro_x", params=[], steps=[_step("c-1", pending=["credenciales"])])],
    )

    groups = pending_groups(_plan_set(plan))

    assert len(groups) == 1
    assert groups[0].steps == 2
    assert groups[0].programs[0].step_ids == ["m-1", "c-1"]


def test_pending_groups_order_by_steps_then_reason():
    plan = JobPlan(
        project_id="p1",
        rules_version="rules-1",
        program="a.sas",
        job_name="job_a",
        steps=[
            _step("1", pending=["zeta"]),
            _step("2", pending=["alfa"]),
            _step("3", pending=["beta"]),
            _step("4", pending=["beta"]),
        ],
    )

    groups = pending_groups(_plan_set(plan))

    assert [group.reason for group in groups] == ["beta", "alfa", "zeta"]
