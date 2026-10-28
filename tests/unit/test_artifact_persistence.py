from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import build_dependencies, load_dependencies
from sas_grid_migrator.migration_planner.service import generate_plans, load_plans
from sas_grid_migrator.persistence import artifacts
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import analyze_project, load_analysis


@pytest.mark.parametrize(
    ("build", "load", "artifact_path"),
    [
        (analyze_project, load_analysis, Store.analysis_path),
        (build_dependencies, load_dependencies, Store.dependencies_path),
        (generate_plans, load_plans, Store.plans_path),
    ],
)
def test_failed_artifact_replacement_keeps_the_previous_json_readable(
    tmp_path, monkeypatch, build, load, artifact_path
):
    source = tmp_path / "source"
    source.mkdir()
    (source / "daily.sas").write_text("data work.daily; set raw.source; run;", encoding="utf-8")
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("artifact")
    store.import_batch(project.id, source)
    build(store, project.id)
    path: Path = artifact_path(store, project.id)
    original = path.read_bytes()

    def failed_replace(_source, _target):
        raise OSError("injected atomic replace failure")

    monkeypatch.setattr(artifacts.os, "replace", failed_replace)
    with pytest.raises(OSError, match="injected atomic replace failure"):
        build(store, project.id)

    assert path.read_bytes() == original
    assert load(store, project.id) is not None
    assert not list(path.parent.glob(f".{path.name}.*.tmp"))
