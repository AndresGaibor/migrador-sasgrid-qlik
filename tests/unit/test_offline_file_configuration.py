from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.offline_files import configure_offline_file_operations
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.parser import parse_program
from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec

FIXTURES = Path(__file__).parents[1] / "fixtures" / "sas"


def test_offline_file_job_uses_project_context_schema_and_filter_table(tmp_path: Path):
    source = tmp_path / "sas-project"
    data = source / "Data" / "input"
    data.mkdir(parents=True)
    (data / "customers.csv").write_text(
        "customer_id;status;balance\nC001;ACTIVE;250.50\nC002;INACTIVE;80.00\n",
        encoding="utf-8",
    )
    output = source / "Data" / "output"
    output.mkdir()
    (output / ".keep").write_text("", encoding="utf-8")
    (source / "load_customers.sas").write_text(
        "%let DATA_ROOT=Data;\n"
        "data _null_;\n"
        "    infile \"&DATA_ROOT./input/customers.csv\" dsd dlm=';' firstobs=2 truncover;\n"
        "    input customer_id : $12. status : $10. balance 12.2;\n"
        "    if status = 'ACTIVE';\n"
        "    file \"&DATA_ROOT./output/active_customers.csv\" dsd dlm=';';\n"
        "    put customer_id status balance;\n"
        "run;\n",
        encoding="utf-8",
    )

    store = Store(Settings(data_dir=tmp_path / "state"))
    project = store.create_project("offline-files")
    store.import_batch(project.id, source)
    plans = generate_plans(store, project.id, fresh=True)
    plan = next(item for item in plans.plans if item.program == "load_customers.sas")
    spec = build_apply_spec(plan, "Process/OfflineTest").to_mcp_arguments()
    components = {item["componentName"]: item for item in spec["components"]}

    reader = components["tFileInputDelimited"]
    assert reader["parameters"]["FILENAME"] == 'context.DATA_ROOT + "/input/customers.csv"'
    assert reader["parameters"]["FIELDSEPARATOR"] == ";"
    assert reader["parameters"]["HEADER"] == "1"
    assert reader["schema"]["columns"] == [
        {"name": "customer_id", "type": "id_String", "nullable": False},
        {"name": "status", "type": "id_String", "nullable": False},
        {"name": "balance", "type": "id_Double", "nullable": False},
    ]

    filter_component = components["tFilterRow"]
    assert filter_component["parameters"]["LOGICAL_OP"] == "AND"
    assert "CONDITIONS" not in filter_component["parameters"]
    assert filter_component["tables"]["CONDITIONS"]["rows"] == [
        {
            "INPUT_COLUMN": "status",
            "FUNCTION": "",
            "OPERATOR": "==",
            "RVALUE": "ACTIVE",
        }
    ]
    assert filter_component["schema"]["columns"] == reader["schema"]["columns"]

    writer = components["tFileOutputDelimited"]
    assert writer["parameters"]["FILENAME"] == 'context.DATA_ROOT + "/output/active_customers.csv"'
    assert writer["parameters"]["FIELDSEPARATOR"] == ";"
    assert writer["parameters"]["INCLUDEHEADER"] == "false"
    assert "CREATE_HEADER" not in writer["parameters"]
    assert writer["parameters"]["FILE_EXIST_EXCEPTION"] == "false"
    assert writer["schema"]["columns"] == reader["schema"]["columns"]
    assert all(not component["draftOnly"] for component in spec["components"])
    assert [(edge["source"], edge["target"]) for edge in spec["connections"]] == [
        (reader["uniqueName"], filter_component["uniqueName"]),
        (filter_component["uniqueName"], writer["uniqueName"]),
    ]
    assert all(step.verified is False for step in plan.steps)
    assert {context["name"]: context["value"] for context in spec["contexts"]}[
        "DATA_ROOT"
    ] == "Data"
    assert (
        spec["instructions"]["offlineConfiguration"]["verification"] == "pending-in-talend-studio"
    )


def test_real_sas_files_with_external_paths_remain_pending_offline():
    source_root = FIXTURES / "real"
    program = source_root / "learning-sas-by-example" / "Example_code" / "Create_Datasets.sas"
    relative_program = program.relative_to(source_root).as_posix()
    ir = build_ir(parse_program(program.read_text(encoding="cp1252"), relative_program), {})

    configure_offline_file_operations(ir, source_root)

    file_operations = [
        operation for operation in ir.operations if operation.type in {"read_file", "write_file"}
    ]
    assert file_operations
    assert not any(
        operation.details.get("offline_file_config", {}).get("ready")
        for operation in file_operations
    )


def test_repository_synthetic_bank_import_is_configured_from_its_csv(tmp_path: Path):
    source = FIXTURES / "synthetic" / "bancolombia_sas_synthetic_orchestration"
    store = Store(Settings(data_dir=tmp_path / "state"))
    project = store.create_project("synthetic-bank")
    store.import_batch(project.id, source)
    plans = generate_plans(store, project.id, fresh=True)
    plan = next(
        item
        for item in plans.plans
        if item.program.endswith("Programs/Banking/01_load_customers.sas")
    )
    arguments = build_apply_spec(plan, "Process/OfflineTest").to_mcp_arguments()
    reader = next(
        component
        for component in arguments["components"]
        if component["componentName"] == "tFileInputDelimited"
    )

    assert reader["parameters"]["FILENAME"] == 'context.SAS_PROJECT_ROOT + "/data/customers.csv"'
    assert reader["parameters"]["FIELDSEPARATOR"] == ";"
    assert reader["parameters"]["HEADER"] == "1"
    assert reader["schema"]["columns"][0]["name"] == "customer_id"
    assert reader["draftOnly"] is False


def test_zip_project_resolves_paths_below_the_enclosing_folder(tmp_path: Path):
    archive = FIXTURES / "synthetic" / "bancolombia_sas_synthetic_orchestration.zip"
    store = Store(Settings(data_dir=tmp_path / "state"))
    project = store.create_project("synthetic-bank-zip")
    store.import_batch(project.id, archive)
    plans = generate_plans(store, project.id, fresh=True)
    plan = next(
        item
        for item in plans.plans
        if item.program.endswith("Programs/Banking/01_load_customers.sas")
    )
    arguments = build_apply_spec(plan, "Process/OfflineTest").to_mcp_arguments()
    components = {item["componentName"]: item for item in arguments["components"]}
    root = "/bancolombia_sas_synthetic_orchestration"

    reader = components["tFileInputDelimited"]
    assert (
        reader["parameters"]["FILENAME"]
        == f'context.SAS_PROJECT_ROOT + "{root}/data/customers.csv"'
    )
    assert reader["parameters"]["HEADER"] == "1"
    assert [column["name"] for column in reader["schema"]["columns"]][:2] == [
        "customer_id",
        "customer_name",
    ]
    assert reader["draftOnly"] is False

    writer = components["tFileOutputDelimited"]
    assert (
        writer["parameters"]["FILENAME"]
        == f'context.SAS_PROJECT_ROOT + "{root}/data/stage/customers_active.csv"'
    )
    assert writer["draftOnly"] is False
