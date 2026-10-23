from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.talend_adapter.batch import collect_child_results, order_plans_for_batch


def _plan(program: str) -> JobPlan:
    return JobPlan(
        project_id="project-1",
        rules_version="rules-1",
        program=program,
        job_name=program.rsplit("/", 1)[-1].removesuffix(".sas"),
    )


def test_order_plans_follows_dependency_layers_then_appends_unlisted_paths_stably():
    plans = [
        _plan("z/extra.sas"),
        _plan("source/b.sas"),
        _plan("source/a.sas"),
        _plan("source/c.sas"),
    ]

    ordered = order_plans_for_batch(
        plans,
        [["source/b.sas", "source/a.sas"], ["source/c.sas", "source/a.sas"]],
    )

    assert [plan.program for plan in ordered] == [
        "source/a.sas",
        "source/b.sas",
        "source/c.sas",
        "z/extra.sas",
    ]


def test_child_results_flatten_depth_first_and_keep_job_folder_and_parent_identity():
    result = {
        "jobName": "orchestrator",
        "folderPath": "Process/project/root",
        "itemPath": "Process/project/root/orchestrator_0.1.item",
        "childJobs": [
            {
                "jobName": "transform",
                "folderPath": "Process/project/etl",
                "itemPath": "Process/project/etl/transform_0.1.item",
                "generatedComponents": 2,
                "reusedExisting": False,
                "childJobs": [
                    {
                        "jobName": "extract",
                        "folderPath": "Process/project/input",
                        "itemPath": "Process/project/input/extract_0.1.item",
                        "generatedComponents": 1,
                        "reusedExisting": False,
                        "childJobs": [],
                    }
                ],
            }
        ],
    }

    children = collect_child_results(result)

    assert [child["jobName"] for child in children] == ["extract", "transform"]
    assert children[0]["folderPath"] == "Process/project/input"
    assert children[0]["parentJobName"] == "transform"
    assert children[1]["parentJobName"] == "orchestrator"
    assert children[1]["generatedComponents"] == 2
    assert "childJobs" not in children[1]
