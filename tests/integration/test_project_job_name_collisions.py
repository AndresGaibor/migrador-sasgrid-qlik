"""Project-level regression: equal SAS basenames must produce distinct Talend Jobs."""

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store


def test_project_planning_disambiguates_repeated_bulkload_names(tmp_path):
    source = tmp_path / "sas"
    programs = {
        "SAS_Foundation/DB2/bulkload.sas": "data work.db2_output; set db2.bulkload; run;",
        "SAS_Foundation/Greenplum/bulkload.sas": "data work.gp_output; set gp.bulkload; run;",
    }
    for relative_path, content in programs.items():
        path = source / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("duplicate SAS basenames")
    store.import_batch(project.id, source)
    plans = generate_plans(store, project.id)

    names = {plan.program: plan.job_name for plan in plans.plans}
    assert names == {
        "SAS_Foundation/DB2/bulkload.sas": "job_db2_bulkload",
        "SAS_Foundation/Greenplum/bulkload.sas": "job_greenplum_bulkload",
    }
    assert len(set(names.values())) == len(programs)
