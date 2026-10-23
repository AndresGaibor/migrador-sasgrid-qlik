from datetime import datetime
from pathlib import Path
import sqlite3

from sas_grid_migrator.config import Settings
from sas_grid_migrator.domain.models import FileKind, SourceFile
from sas_grid_migrator.persistence.store import Store


def _store(tmp_path: Path) -> Store:
    return Store(Settings(data_dir=tmp_path / "data"))


def _source(path: str) -> SourceFile:
    return SourceFile(path=path, sha256="a" * 64, size=18, kind=FileKind.SAS)


def _zip_project(store: Store, tmp_path: Path, archive_name: str):
    staged = tmp_path / f"{archive_name}.staged" / "src"
    staged.mkdir(parents=True)
    (staged / "nested").mkdir()
    (staged / "nested" / "daily.sas").write_text("data daily; run;", encoding="utf-8")
    return store.create_zip_project(
        name=Path(archive_name).stem,
        archive_name=archive_name,
        archive_sha256="b" * 64,
        archive_size_bytes=128,
        staged_source_dir=staged,
        files=[_source("nested/daily.sas")],
        skipped=[],
    )


def test_existing_projects_remain_legacy_after_reopening_store(tmp_path):
    store = _store(tmp_path)
    existing = store.create_project("Legacy project")

    reopened = _store(tmp_path)
    project = reopened.get_project(existing.id)

    assert project is not None
    assert project.archive_name is None
    assert project.archive_sha256 is None
    assert project.processing is None


def test_store_migrates_an_existing_projects_table_in_place(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    connection = sqlite3.connect(data_dir / "sgm.sqlite")
    connection.execute(
        "create table projects(id text primary key, name text not null, created_at text not null)"
    )
    connection.execute(
        "insert into projects values (?,?,?)",
        ("legacy-id", "Legacy", "2025-01-01T00:00:00+00:00"),
    )
    connection.commit()
    connection.close()

    store = Store(Settings(data_dir=data_dir))

    project = store.get_project("legacy-id")
    assert project is not None and project.archive_name is None
    with sqlite3.connect(data_dir / "sgm.sqlite") as migrated:
        columns = {row[1] for row in migrated.execute("pragma table_info(projects)")}
    assert {
        "archive_name",
        "archive_sha256",
        "archive_size_bytes",
        "uploaded_at",
        "manifest_summary",
    } <= columns


def test_zip_registration_publishes_metadata_source_and_queued_state(tmp_path):
    store = _store(tmp_path)

    project, manifest = _zip_project(store, tmp_path, "insurance.zip")

    assert project.archive_name == "insurance.zip"
    assert project.archive_sha256 == "b" * 64
    assert project.archive_size_bytes == 128
    assert isinstance(project.uploaded_at, datetime)
    assert project.processing is not None
    assert project.processing.status == "queued"
    assert manifest.project_id == project.id
    assert [item.path for item in manifest.files] == ["nested/daily.sas"]
    assert (store.source_dir(project.id) / "nested" / "daily.sas").read_text() == "data daily; run;"


def test_processing_and_apply_state_survive_reopen_without_crossing_projects(tmp_path):
    store = _store(tmp_path)
    first, _ = _zip_project(store, tmp_path, "first.zip")
    second, _ = _zip_project(store, tmp_path, "second.zip")
    store.update_processing(
        first.id,
        status="running",
        stage="analysis",
        message="Analizando programas SAS",
    )
    store.save_talend_apply_state(
        first.id,
        "nested/daily.sas",
        revision_hash="revision-1",
        status="running",
        identity={"project_id": first.id, "folder_path": "Process/first/123/nested"},
    )

    reopened = _store(tmp_path)
    reopened.recover_interrupted_operations()

    first_state = reopened.get_project(first.id)
    second_state = reopened.get_project(second.id)
    apply_state = reopened.get_talend_apply_state(first.id, "nested/daily.sas")
    assert first_state is not None and first_state.processing is not None
    assert first_state.processing.status == "interrupted"
    assert first_state.processing.stage == "analysis"
    assert second_state is not None and second_state.processing is not None
    assert second_state.processing.status == "interrupted"
    assert apply_state is not None
    assert apply_state["status"] == "interrupted"
    assert apply_state["identity"]["project_id"] == first.id
    assert reopened.get_talend_apply_state(second.id, "nested/daily.sas") is None
