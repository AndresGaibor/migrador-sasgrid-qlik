import sqlite3
from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.persistence.store import JobOverride, Store


def _store(tmp_path: Path) -> Store:
    return Store(Settings(data_dir=tmp_path / "data"))


def test_job_override_round_trip(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Overrides")

    store.set_job_override(project.id, "a.sas", "mi_job", "Carga diaria")

    assert store.get_job_overrides(project.id)["a.sas"] == JobOverride("mi_job", "Carga diaria")


def test_job_override_with_both_none_removes_the_row(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Overrides")
    store.set_job_override(project.id, "a.sas", "mi_job", "Carga diaria")

    store.set_job_override(project.id, "a.sas", None, None)

    assert "a.sas" not in store.get_job_overrides(project.id)


def test_expression_override_round_trip_and_clear(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Overrides")

    store.set_expression_override(project.id, "a.sas", "s1", 0, "x > 1", "input_row.x > 1")

    assert store.get_expression_overrides(project.id)[("a.sas", "s1", 0)] == (
        "x > 1",
        "input_row.x > 1",
    )

    store.set_expression_override(project.id, "a.sas", "s1", 0, "x > 1", None)

    assert ("a.sas", "s1", 0) not in store.get_expression_overrides(project.id)


def test_settings_default_and_update(tmp_path):
    store = _store(tmp_path)

    assert store.get_setting("k") is None
    assert store.get_setting("k", "d") == "d"

    store.set_setting("k", "v")

    assert store.get_setting("k") == "v"


def test_deleting_a_project_removes_its_overrides(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Doomed")
    store.set_job_override(project.id, "a.sas", "mi_job", None)
    store.set_expression_override(project.id, "a.sas", "s1", 0, "x > 1", "input_row.x > 1")

    assert store.delete_project(project.id) is True

    assert store.get_job_overrides(project.id) == {}
    assert store.get_expression_overrides(project.id) == {}


def test_has_active_talend_work(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Busy")
    assert store.has_active_talend_work(project.id) is False

    store.begin_talend_apply_batch(project.id, "revision-1", ["a.sas"])
    store.update_talend_apply_batch_state(
        project.id,
        status="running",
        jobs=[{"program": "a.sas", "status": "running", "result": None, "error": None}],
        current_program="a.sas",
        completed_count=0,
    )
    assert store.has_active_talend_work(project.id) is True

    store.update_talend_apply_batch_state(
        project.id,
        status="applied",
        jobs=[{"program": "a.sas", "status": "applied", "result": None, "error": None}],
        current_program=None,
        completed_count=1,
    )
    assert store.has_active_talend_work(project.id) is False


def test_bulk_job_overrides_write_all_rows_and_delete_empty_ones(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Overrides")
    store.set_job_override(project.id, "c.sas", "viejo", None)

    store.set_job_overrides_bulk(
        project.id, [("a.sas", "job_a2", "Carga"), ("b.sas", "job_b2", None), ("c.sas", None, None)]
    )

    assert store.get_job_overrides(project.id) == {
        "a.sas": JobOverride("job_a2", "Carga"),
        "b.sas": JobOverride("job_b2", None),
    }


def test_bulk_job_overrides_persist_nothing_when_one_item_fails(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Overrides")
    store.set_job_override(project.id, "a.sas", "previo", None)

    with pytest.raises(sqlite3.Error):
        store.set_job_overrides_bulk(
            project.id,
            [("a.sas", "nuevo", None), ("b.sas", ["no", "enlazable"], None)],  # type: ignore[list-item]
        )

    assert store.get_job_overrides(project.id) == {"a.sas": JobOverride("previo", None)}
