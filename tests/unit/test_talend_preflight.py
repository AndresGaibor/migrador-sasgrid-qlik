from sas_grid_migrator.talend_adapter.apply_spec import TalendApplySpec

try:
    from sas_grid_migrator.talend_adapter.preflight import classify_jobs
except ImportError:
    classify_jobs = None


def _spec(job_name: str, folder_path: str) -> TalendApplySpec:
    return TalendApplySpec(
        project_id="project-1",
        program=f"{job_name}.sas",
        source_sha256=None,
        rules_version="rules-1",
        job_name=job_name,
        folder_path=folder_path,
        components=[],
        connections=[],
        blocked_steps=[],
        instructions={},
    )


def test_preflight_updates_exact_destination_creates_missing_and_blocks_external_homonym():
    specs = [
        _spec("job_update", "Process/PruebasWebSAS/zip-a/Programs/Banking"),
        _spec("job_create", "Process/PruebasWebSAS/zip-a/Programs/Banking"),
        _spec("job_conflict", "Process/PruebasWebSAS/zip-a/Programs/Banking"),
    ]
    inventory = [
        {
            "name": "JOB_UPDATE",
            "path": r"C:\Talend\PRJ\process\PruebasWebSAS\zip-a\Programs\Banking\job_update\job_update_0.1.item",
        },
        {
            "name": "job_conflict",
            "path": r"C:\Talend\PRJ\process\OtherProject\job_conflict\job_conflict_0.1.item",
        },
    ]

    assert callable(classify_jobs), "La clasificación de preflight debe estar disponible."
    result = classify_jobs(specs, inventory)

    assert [item["action"] for item in result["jobs"]] == ["update", "create", "conflict"]
    assert result["jobs"][0]["existing_path"].endswith("job_update_0.1.item")
    assert result["jobs"][1]["existing_path"] is None
    assert "fuera" in result["jobs"][2]["reason"].lower()
    assert result["create_count"] == 1
    assert result["update_count"] == 1
    assert result["conflict_count"] == 1


def test_preflight_does_not_treat_an_item_without_process_path_as_exact_destination():
    assert callable(classify_jobs), "La clasificación de preflight debe estar disponible."
    result = classify_jobs(
        [_spec("job_same", "Process/PruebasWebSAS/zip-a")],
        [{"name": "job_same", "path": r"C:\Talend\PRJ\job_same\job_same_0.1.item"}],
    )

    assert result["jobs"][0]["action"] == "conflict"
