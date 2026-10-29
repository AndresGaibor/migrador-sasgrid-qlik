from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.persistence.store import JobOverride, Store


def _store(tmp_path: Path) -> Store:
    return Store(Settings(data_dir=tmp_path / "data"))


def test_job_override_round_trip_and_clear(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Finanzas")

    store.set_job_override(project.id, "daily.sas", "carga_diaria", "Carga diaria")
    assert store.get_job_overrides(project.id)["daily.sas"] == JobOverride("carga_diaria", "Carga diaria")

    store.set_job_override(project.id, "daily.sas", None, None)
    assert "daily.sas" not in store.get_job_overrides(project.id)


def test_expression_override_round_trip_and_clear(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Finanzas")

    store.set_expression_override(project.id, "daily.sas", "s1", 0, "x > 1", "input_row.x > 1")
    assert store.get_expression_overrides(project.id)[("daily.sas", "s1", 0)] == (
        "x > 1", "input_row.x > 1"
    )
    store.set_expression_override(project.id, "daily.sas", "s1", 0, "x > 1", None)
    assert store.get_expression_overrides(project.id) == {}


def test_settings_return_default_and_saved_value(tmp_path):
    store = _store(tmp_path)

    assert store.get_setting("naming") is None
    assert store.get_setting("naming", "default") == "default"
    store.set_setting("naming", "job_{programa}")
    assert store.get_setting("naming") == "job_{programa}"


def test_project_deletion_cleans_project_scoped_overrides(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Finanzas")
    store.set_job_override(project.id, "daily.sas", "carga_diaria", None)
    store.set_expression_override(project.id, "daily.sas", "s1", 0, "x", "row.x")

    assert store.delete_project(project.id)
    assert store.get_job_overrides(project.id) == {}
    assert store.get_expression_overrides(project.id) == {}


def test_has_active_talend_work_tracks_batch_state(tmp_path):
    store = _store(tmp_path)
    project = store.create_project("Finanzas")
    assert not store.has_active_talend_work(project.id)

    store.begin_talend_apply_batch(project.id, revision_hash="rev", programs=["daily.sas"])
    assert store.has_active_talend_work(project.id)
    store.update_talend_apply_batch_state(
        project.id,
        status="applied",
        jobs=[{"program": "daily.sas", "status": "applied", "result": {}, "error": None}],
        current_program=None,
        completed_count=1,
    )
    assert not store.has_active_talend_work(project.id)
