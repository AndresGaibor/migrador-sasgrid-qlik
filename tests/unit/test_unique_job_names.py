from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.migration_planner.planner import unique_job_names


def _plan(program: str, job_name: str) -> JobPlan:
    return JobPlan(project_id="p", rules_version="r", program=program, sha256="h", job_name=job_name)


def test_unique_names_are_left_untouched():
    plans = [_plan("Programs/a.sas", "job_a"), _plan("Programs/b.sas", "job_b")]

    unique_job_names(plans)

    assert [plan.job_name for plan in plans] == ["job_a", "job_b"]


def test_same_file_name_in_different_folders_is_disambiguated_with_the_folder():
    plans = [
        _plan("SAS_Foundation/DB2/bulkload.sas", "job_bulkload"),
        _plan("SAS_Foundation/Greenplum/bulkload.sas", "job_bulkload"),
        _plan("Programs/other.sas", "job_other"),
    ]

    unique_job_names(plans)

    assert [plan.job_name for plan in plans] == ["job_db2_bulkload", "job_greenplum_bulkload", "job_other"]


def test_it_goes_up_the_folders_until_the_names_differ():
    plans = [_plan("a/x/run.sas", "job_run"), _plan("b/x/run.sas", "job_run")]

    unique_job_names(plans)

    assert [plan.job_name for plan in plans] == ["job_a_x_run", "job_b_x_run"]


def test_a_renamed_job_never_collides_with_an_existing_one():
    plans = [
        _plan("DB2/bulkload.sas", "job_bulkload"),
        _plan("Hadoop/bulkload.sas", "job_bulkload"),
        _plan("x/db2_bulkload.sas", "job_db2_bulkload"),
    ]

    unique_job_names(plans)

    names = [plan.job_name for plan in plans]
    assert len(set(names)) == 3
    assert names[2] == "job_db2_bulkload"


def test_windows_separators_and_identical_paths_still_end_up_unique():
    plans = [_plan("a\run.sas", "job_run"), _plan("b\run.sas", "job_run"), _plan("b/run.sas", "job_run")]

    unique_job_names(plans)

    assert len({plan.job_name for plan in plans}) == 3


def test_unique_names_use_the_custom_folder_aware_namer():
    plans = [_plan("DB2/bulkload.sas", "job_bulkload"), _plan("Hadoop/bulkload.sas", "job_bulkload")]

    unique_job_names(plans, lambda parts, depth: f"x_{parts[-2].lower()}_{parts[-1].split('.')[0]}")

    assert [plan.job_name for plan in plans] == ["x_db2_bulkload", "x_hadoop_bulkload"]
