from sas_grid_migrator.migration_planner.models import JobPlan, PlanSet, PlanStep
from sas_grid_migrator.migration_planner.progress import compute_progress, pending_groups


def test_progress_points_to_upload_before_anything_exists():
    progress = compute_progress(
        files=0, processing_status=None, plan_rows=None, batch_status=None
    )

    assert progress.next.key == "upload"
    assert progress.next.tab == "importar"
    assert [stage.status for stage in progress.stages] == [
        "current", "todo", "todo", "todo", "todo", "todo"
    ]


def test_progress_shows_processing_and_failed_analysis_as_current_or_blocked():
    running = compute_progress(
        files=5, processing_status="running", plan_rows=None, batch_status=None
    )
    failed = compute_progress(
        files=5, processing_status="failed", plan_rows=None, batch_status=None
    )

    assert running.stages[1].status == "current"
    assert running.next.key == "analysis"
    assert failed.stages[1].status == "blocked"
    assert failed.next.key == "analysis"


def test_progress_advances_through_guides_creation_and_manual_completion():
    rows = [
        {"steps": 10, "done": 3, "studio_status": "verified"},
        {"steps": 2, "done": 2, "studio_status": "pending"},
    ]
    progress = compute_progress(
        files=5, processing_status="completed", plan_rows=rows, batch_status="applied"
    )

    assert progress.next.key == "complete"
    assert progress.stages[3].status == "done"
    assert progress.stages[4].detail == "5 de 12 pasos"


def test_progress_marks_studio_conflict_blocked_and_all_done_has_no_next():
    blocked = compute_progress(
        files=2,
        processing_status="completed",
        plan_rows=[{"steps": 1, "done": 0, "studio_status": "not_checked"}],
        batch_status="conflict",
    )
    complete = compute_progress(
        files=1,
        processing_status="completed",
        plan_rows=[{"steps": 1, "done": 1, "studio_status": "verified"}],
        batch_status="applied",
    )

    assert blocked.stages[3].status == "blocked"
    assert blocked.next.key == "studio"
    assert complete.next is None
    assert all(stage.status == "done" for stage in complete.stages)


def test_pending_groups_count_each_reason_and_include_child_jobs():
    def step(step_id: str, reason: str, status: str = "propuesto") -> PlanStep:
        return PlanStep(
            id=step_id,
            order=1,
            subjob="",
            action="configure",
            purpose="Configurar",
            pending=[reason],
            status=status,
            evidence={"file": "a.sas", "line": 1, "end_line": 1},
        )

    plans = PlanSet(
        project_id="p",
        rules_version="r",
        plans=[
            JobPlan(
                project_id="p",
                rules_version="r",
                program="a.sas",
                job_name="job_a",
                steps=[step("a1", "definir destino")],
                children=[
                    {"name": "macro", "params": [], "steps": [step("a2", "definir destino")]}
                ],
            ),
            JobPlan(
                project_id="p",
                rules_version="r",
                program="b.sas",
                job_name="job_b",
                steps=[step("b1", "elegir delimitador"), step("b2", "ignorar", "descartado")],
            ),
        ],
    )

    groups = pending_groups(plans)

    assert [(group.reason, group.steps) for group in groups] == [
        ("definir destino", 2),
        ("elegir delimitador", 1),
    ]
    assert [(job.job_name, job.step_ids) for job in groups[0].programs] == [
        ("job_a", ["a1"]),
        ("macro", ["a2"]),
    ]
