from pathlib import Path

import sqlite3

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.persistence.store import Store


def _store(tmp_path: Path) -> Store:
    return Store(Settings(data_dir=tmp_path / "data"))


def test_batch_state_is_isolated_and_duplicate_start_reuses_running_batch(tmp_path):
    store = _store(tmp_path)
    first = store.create_project("First")
    second = store.create_project("Second")

    state, started = store.begin_talend_apply_batch(
        first.id, "revision-1", ["A/one.sas", "B/two.sas"]
    )
    repeated, repeated_started = store.begin_talend_apply_batch(
        first.id, "revision-1", ["A/one.sas", "B/two.sas"]
    )

    assert started is True
    assert repeated_started is False
    assert repeated["status"] == "queued"
    assert state["programs"] == ["A/one.sas", "B/two.sas"]
    assert state["completed_jobs"] == 0
    assert store.get_talend_apply_batch_state(second.id) is None


def test_batch_retry_preserves_completed_job_results_for_same_revision(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Retry")
    _state, _ = store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas", "b.sas"])
    jobs = [
        {"program": "a.sas", "status": "applied", "result": {"itemPath": "Process/a"}, "error": None},
        {"program": "b.sas", "status": "failed", "result": None, "error": "Bridge offline"},
    ]
    store.update_talend_apply_batch_state(
        project.id,
        status="partially_applied",
        jobs=jobs,
        current_program=None,
        completed_count=2,
    )

    retried, started = store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas", "b.sas"])

    assert started is True
    assert retried["status"] == "queued"
    assert retried["attempt_count"] == 2
    assert retried["jobs"] == [
        jobs[0],
        {"program": "b.sas", "status": "pending", "result": None, "error": None},
    ]
    assert retried["completed_jobs"] == 1


def test_completed_batch_is_reused_and_changed_revision_is_conflict(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Conflict")
    store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas"])
    store.update_talend_apply_batch_state(
        project.id,
        status="applied",
        jobs=[{"program": "a.sas", "status": "applied", "result": {"itemPath": "Process/a"}, "error": None}],
        current_program=None,
        completed_count=1,
    )

    completed, started = store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas"])
    assert started is False
    assert completed["status"] == "applied"
    with pytest.raises(ValueError, match="revisión"):
        store.begin_talend_apply_batch(project.id, "revision-2", ["a.sas"])
    assert store.get_talend_apply_batch_state(project.id)["revision_hash"] == "revision-1"


def test_conflict_batch_is_retryable_only_after_explicit_fresh_preflight(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Fresh preflight")
    _state, _ = store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas"])
    store.update_talend_apply_batch_state(
        project.id,
        status="conflict",
        jobs=[{"program": "a.sas", "status": "conflict", "result": None, "error": "old collision"}],
        current_program=None,
        completed_count=1,
    )

    stale, stale_started = store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas"])
    fresh, fresh_started = store.begin_talend_apply_batch(
        project.id, "revision-1", ["a.sas"], retry_conflicts=True
    )

    assert stale_started is False
    assert stale["status"] == "conflict"
    assert fresh_started is True
    assert fresh["status"] == "queued"
    assert fresh["attempt_count"] == 2
    assert fresh["jobs"] == [{"program": "a.sas", "status": "pending", "result": None, "error": None}]


def test_retry_programs_reopens_only_applied_jobs_missing_from_fresh_inventory(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Restore missing")
    store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas", "b.sas"])
    store.update_talend_apply_batch_state(
        project.id,
        status="applied",
        jobs=[
            {"program": "a.sas", "status": "applied", "result": {"job": "a"}, "error": None},
            {"program": "b.sas", "status": "applied", "result": {"job": "b"}, "error": None},
        ],
        current_program=None,
        completed_count=2,
    )

    retried, started = store.begin_talend_apply_batch(
        project.id,
        "revision-1",
        ["a.sas", "b.sas"],
        retry_programs={"b.sas"},
    )

    assert started is True
    assert [job["status"] for job in retried["jobs"]] == ["applied", "pending"]
    assert retried["completed_jobs"] == 1


def test_restarting_store_marks_queued_batch_interrupted(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Interrupted")
    store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas"])

    _store(tmp_path).recover_interrupted_operations()

    state = store.get_talend_apply_batch_state(project.id)
    assert state is not None
    assert state["status"] == "interrupted"
    assert "reiniciar" in state["error"].lower()


def test_restarting_store_marks_the_active_job_interrupted_and_clears_current_program(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Interrupted Job")
    store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas", "b.sas"])
    store.update_talend_apply_batch_state(
        project.id,
        status="running",
        jobs=[
            {"program": "a.sas", "status": "applied", "result": {"itemPath": "Process/a"}, "error": None},
            {"program": "b.sas", "status": "running", "result": None, "error": None},
        ],
        current_program="b.sas",
        completed_count=1,
    )

    _store(tmp_path).recover_interrupted_operations()

    state = store.get_talend_apply_batch_state(project.id)
    assert state is not None
    assert state["status"] == "interrupted"
    assert state["current_program"] is None
    assert [job["status"] for job in state["jobs"]] == ["applied", "interrupted"]
    assert "reiniciar" in state["jobs"][1]["error"].lower()


def test_existing_batch_table_is_migrated_with_warning_storage(tmp_path):
    settings = Settings(data_dir=tmp_path / "data")
    settings.data_dir.mkdir(parents=True)
    database = settings.data_dir / "sgm.sqlite"
    with sqlite3.connect(database) as connection:
        connection.execute(
            """create table talend_apply_batches(
            project_id text primary key, revision_hash text not null, status text not null,
            programs_json text not null, jobs_json text not null, current_program text,
            completed_jobs integer not null default 0, error text, attempt_count integer not null default 1,
            started_at text not null, updated_at text not null)"""
        )

    Store(settings)

    with sqlite3.connect(database) as connection:
        columns = {row[1] for row in connection.execute("pragma table_info(talend_apply_batches)")}
    assert "warnings_json" in columns


def test_batch_progress_update_persists_current_program_and_job_results(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Progress")
    store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas", "b.sas"])
    jobs = [
        {"program": "a.sas", "status": "applied", "result": {"itemPath": "Process/a"}, "error": None},
        {"program": "b.sas", "status": "running", "result": None, "error": None},
    ]

    state = store.update_talend_apply_batch_state(
        project.id,
        status="running",
        jobs=jobs,
        current_program="b.sas",
        completed_count=1,
    )

    assert state["current_program"] == "b.sas"
    assert state["completed_jobs"] == 1
    assert state["jobs"] == jobs
    assert store.get_talend_apply_batch_state(project.id) == state
