import pytest
from apps.api import main as api_module
from fastapi.testclient import TestClient

from sas_grid_migrator.migration_planner.models import (
    ChildJob,
    ContextVariable,
    Expression,
    JobPlan,
    LibraryNeeded,
    MacroEntrypoint,
    PlanSet,
    PlanStep,
    Property,
    SchemaColumn,
)
from sas_grid_migrator.sas_parser.ast import Loc
from sas_grid_migrator.talend_adapter.adapter import TalendError
from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec


def step(
    step_id: str,
    component: str,
    *,
    verified: bool = True,
    pending: list[str] | None = None,
    from_step: str | None = None,
) -> PlanStep:
    return PlanStep(
        id=step_id,
        order=1,
        subjob="main",
        action="add_component",
        component_candidate=component,
        purpose=f"Aplicar {component}",
        properties=[Property(name="HEADER", value="1", origin="regla", verified=verified)],
        schema_columns=[SchemaColumn(name="id", talend_type="id_Integer", nullable=False)],
        connections=[] if from_step is None else [{"type": "Main", "from_step": from_step}],
        evidence=Loc(file="daily.sas", line=4, end_line=4),
        verified=verified,
        in_catalog=True,
        pending=pending or [],
    )


def plan(*steps: PlanStep) -> JobPlan:
    return JobPlan(
        project_id="project-1",
        rules_version="rules-7",
        program="daily.sas",
        sha256="source-hash",
        job_name="DailyJob",
        steps=list(steps),
    )


def test_build_apply_spec_maps_verified_steps_to_mcp_custom_job_spec():
    result = build_apply_spec(
        plan(step("read_1", "tFileInputDelimited")),
        folder_path="Process/Generated",
    )

    arguments = result.to_mcp_arguments()
    assert arguments["jobName"] == "DailyJob"
    assert arguments["folderPath"] == "Process/Generated"
    assert arguments["components"] == [
        {
            "uniqueName": "tFileInputDelimited_1",
            "componentName": "tFileInputDelimited",
            "posX": 160,
            "posY": 96,
            "label": "Aplicar tFileInputDelimited [read_1]",
            "parameters": {"HEADER": "1"},
            "schema": {
                "name": "tFileInputDelimited_1_schema",
                "connector": "FLOW",
                "columns": [{"name": "id", "type": "id_Integer", "nullable": False}],
            },
            "draftOnly": False,
        }
    ]
    assert arguments["connections"] == []
    assert arguments["contexts"] == []
    assert arguments["instructions"]["source"]["program"] == "daily.sas"
    assert "status" not in arguments["instructions"]["steps"][0]
    assert result.blocked_steps == []


def test_context_file_overrides_known_values_and_adds_per_job_parameters(tmp_path):
    migration = plan(step("read_1", "tFileInputDelimited"))
    migration.context_variables = [
        {"name": "year", "suggested": "context.year", "origin": "SAS", "sas_value": None}
    ]
    cpf = tmp_path / "daily.cpf"
    cpf.write_text("# parámetros del Job\nyear=2026\nsource_path=/data/in.csv\n", encoding="utf-8")

    contexts = build_apply_spec(migration, context_file=cpf).to_mcp_arguments()["contexts"]

    assert {item["name"]: item["value"] for item in contexts}["year"] == "2026"
    assert {item["name"]: item["value"] for item in contexts}["source_path"] == "/data/in.csv"


@pytest.mark.parametrize(
    ("filename", "content", "message"),
    [
        ("missing.cpf", None, "No existe"),
        ("daily.txt", "x=1", "extensión .cpf"),
        ("daily.cpf", "x=", "está vacío"),
        ("daily.cpf", "x=1\nX=2", "duplicado"),
        ("daily.cpf", "bad line", "Línea 1 inválida"),
    ],
)
def test_context_file_rejects_invalid_files(tmp_path, filename, content, message):
    path = tmp_path / filename
    if content is not None:
        path.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        build_apply_spec(plan(), context_file=path)


def test_build_apply_spec_marks_unverified_steps_as_drafts_without_blocking_pending_notes():
    result = build_apply_spec(
        plan(
            step("unverified", "tMap", verified=False),
            step("pending", "tFilterRow", pending=["Confirmar filtro"]),
        )
    )

    assert [(item.component_name, item.draft_only) for item in result.components] == [
        ("tFilterRow", True),
        ("tMap", True),
    ]
    assert result.blocked_steps == []
    assert all(component.draft_only for component in result.components)


def test_transforming_tmap_is_a_draft_until_mapper_configuration_is_generated():
    mapping = step("project_1", "tMap")
    mapping.operation_type = "project"
    mapping.expressions = [Expression(sas="amount * 2", talend="row1.amount * 2", line=8, requires_semantic_validation=False)]

    component = build_apply_spec(plan(mapping)).components[0]

    assert component.draft_only is True
    assert component.mapper is None
    assert "no genera su configuración de mapper" in component.draft_reason


def test_build_apply_spec_keeps_known_downstream_component_connected_to_draft_source():
    result = build_apply_spec(
        plan(
            step("source", "tFileInputDelimited", verified=False),
            step("filter", "tFilterRow", from_step="source"),
        )
    )

    arguments = result.to_mcp_arguments()
    components = {item["componentName"]: item for item in arguments["components"]}
    assert set(components) == {"tFileInputDelimited", "tFilterRow"}
    assert components["tFileInputDelimited"]["draftOnly"] is True
    assert components["tFilterRow"]["draftOnly"] is False
    assert arguments["connections"] == [
        {
            "source": components["tFileInputDelimited"]["uniqueName"],
            "target": components["tFilterRow"]["uniqueName"],
            "label": "row_1_1",
            "connectorName": "FLOW",
            "uniqueName": "flow_1_1",
        }
    ]
    assert result.blocked_steps == []


def test_lookup_relationship_uses_the_source_data_connector_and_preserves_join_instruction():
    source = step("read_1", "tTeradataInput")
    join = step("join_1", "tMap", from_step="read_1")
    join.connections[0].type = "Lookup"

    arguments = build_apply_spec(plan(source, join)).to_mcp_arguments()

    assert arguments["connections"][0]["connectorName"] == "FLOW"
    instruction_steps = {item["id"]: item for item in arguments["instructions"]["steps"]}
    assert instruction_steps["join_1"]["dependencies"] == [
        {"type": "Lookup", "fromStep": "read_1", "label": None}
    ]


def test_build_apply_spec_keeps_identified_components_when_semantic_validation_is_pending():
    unsupported = step("manual", "tMap")
    unsupported.action = "manual_decision"
    unresolved = step("expression", "tMap")
    unresolved.expressions = [
        Expression(sas="x is missing", talend=None, line=8, requires_semantic_validation=True)
    ]

    result = build_apply_spec(plan(unsupported, unresolved))

    assert [(item.component_name, item.draft_only) for item in result.components] == [
        ("tMap", True), ("tMap", True)
    ]
    assert result.blocked_steps == []


def test_build_apply_spec_converts_context_variables_and_keeps_unmapped_features_in_context():
    migration = plan(step("read_1", "tFileInputDelimited"))
    migration.context_variables = [{"name": "year", "suggested": "context.year", "origin": "SAS", "sas_value": "2025"}]

    result = build_apply_spec(migration)

    assert result.components[0].component_name == "tFileInputDelimited"
    assert result.contexts[0].name == "year"
    assert result.contexts[0].value == "2025"
    assert result.to_mcp_arguments()["contexts"] == [
        {"name": "year", "type": "id_String", "value": "2025", "comment": "Importado desde SAS: SAS"}
    ]

    migration.libraries_needed = [{"sas_name": "DB", "suggested_connection": "tDBConnection"}]
    result = build_apply_spec(migration)
    assert result.components[0].component_name == "tFileInputDelimited"
    assert result.blocked_steps == []
    assert any("Biblioteca SAS DB" in item.comment for item in result.contexts)


def test_build_apply_spec_keeps_external_macro_steps_pending_in_context():
    macro_step = step("m:worker:read", "por_determinar", verified=False)
    migration = plan()
    migration.children = [ChildJob(name="worker", params=["range_id"], steps=[macro_step])]

    result = build_apply_spec(migration)

    assert result.components == []
    assert result.blocked_steps == []
    assert any("worker" in item.comment or "Identificar" in item.comment for item in result.contexts)


def test_program_macro_is_inlined_and_helper_calls_are_not_talend_child_jobs():
    migration = plan()
    migration.program = "analytics/daily.sas"
    migration.job_name = "job_daily"
    include = step("include_autoexec", "tRunJob", verified=False)
    include.operation_type = "include"
    include.properties = [Property(name="PROCESS", value='"/sas/autoexec.sas"', origin="SAS")]
    self_call = step("call_daily", "tRunJob", verified=False)
    self_call.operation_type = "macro_call"
    self_call.properties = [Property(name="PROCESS", value="daily", origin="SAS")]
    helper = step("call_parmv", "tRunJob", verified=False)
    helper.operation_type = "macro_call"
    helper.properties = [Property(name="PROCESS", value="parmv", origin="SAS")]
    body = step("filter_rows", "tFilterRow", verified=False, from_step="call_parmv")
    body.operation_type = "filter"
    migration.steps = [include, self_call]
    migration.children = [ChildJob(name="daily", params=["run_date"], steps=[helper, body])]

    arguments = build_apply_spec(migration).to_mcp_arguments()

    assert [component["componentName"] for component in arguments["components"]] == ["tFilterRow"]
    assert all(component["componentName"] != "tRunJob" for component in arguments["components"])
    assert any(context["name"] == "run_date" and context["value"] == "" for context in arguments["contexts"])
    assert any("parmv" in context["comment"] for context in arguments["contexts"])


def test_orchestrator_resolves_static_programs_to_child_jobs_and_sequential_triggers():
    parent = plan()
    parent.program = "ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas"
    parent.job_name = "job_run_daily_insurance"
    own_call = step("self_call", "tRunJob", verified=False)
    own_call.operation_type = "macro_call"
    own_call.properties = [Property(name="PROCESS", value="run_daily_insurance", origin="SAS")]
    calls = []
    for order, (name, source) in enumerate([
        ("claims_processing", "/opt/sas/custom/programs/Insurance/claims_processing.sas"),
        ("policy_valuation", "/opt/sas/custom/programs/Insurance/policy_valuation.sas"),
    ], start=1):
        call = step(f"run_step_{order}", "tRunJob", verified=False, from_step="self_call" if order == 1 else f"run_step_{order - 1}")
        call.operation_type = "macro_call"
        call.properties = [
            Property(name="PROCESS", value="run_step", origin="SAS"),
            Property(name="CONTEXTPARAMS", value=f"{order}, {name}, {source}", origin="SAS"),
        ]
        calls.append(call)
    parent.children = [ChildJob(name="run_daily_insurance", params=["run_date"], steps=[own_call, *calls])]

    child_plans = []
    for name, params in [("claims_processing", ["proc_date"]), ("policy_valuation", ["val_date", "lob"])]:
        child = plan()
        child.program = f"ts-sas-legacy-analytics/Programs/Insurance/{name}.sas"
        child.job_name = f"job_{name}"
        body = step(f"{name}_filter", "tFilterRow", verified=False)
        body.operation_type = "filter"
        child.children = [ChildJob(name=name, params=params, steps=[body])]
        child_plans.append(child)

    result = build_apply_spec(
        parent,
        "Process/PruebasWebSAS/ts-sas-legacy-analytics/BatchJobs",
        related_plans=child_plans,
        related_folder_paths={
            child.program: f"Process/PruebasWebSAS/{child.program.rsplit('/', 1)[0]}"
            for child in child_plans
        },
    )
    arguments = result.to_mcp_arguments()

    assert [item["jobName"] for item in arguments["childJobs"]] == [
        "job_claims_processing", "job_policy_valuation"
    ]
    assert [item["folderPath"] for item in arguments["childJobs"]] == [
        "Process/PruebasWebSAS/ts-sas-legacy-analytics/Programs/Insurance",
        "Process/PruebasWebSAS/ts-sas-legacy-analytics/Programs/Insurance",
    ]
    assert [component["parameters"]["PROCESS"] for component in arguments["components"]] == [
        "job_claims_processing", "job_policy_valuation"
    ]
    assert all(component["draftOnly"] is False for component in arguments["components"])
    assert arguments["connections"] == [{
        "source": arguments["components"][0]["uniqueName"],
        "target": arguments["components"][1]["uniqueName"],
        "label": "row_1_1",
        "connectorName": "SUBJOB_OK",
        "uniqueName": "subjob_ok_1_1",
    }]
    assert result.blocked_steps == []
    assert not any("Crear/identificar el Job hijo para %run_step" in item["comment"] for item in arguments["contexts"])


def test_entry_macro_plan_passes_known_context_reference_to_resolved_child_job():
    parent = plan()
    parent.program = "BatchJobs/run_daily_insurance.sas"
    parent.job_name = "job_run_daily_insurance"
    parent.entry_macro = MacroEntrypoint(
        name="run_daily_insurance",
        params=["run_date"],
        arguments={"run_date": "&CURR_DT"},
    )
    parent.context_variables = [
        ContextVariable(name="CURR_DT", sas_value=None, suggested="context.CURR_DT", origin="SAS")
    ]
    child_call = step("run_step_claims", "tRunJob", verified=False)
    child_call.operation_type = "macro_call"
    child_call.properties = [
        Property(name="PROCESS", value="run_step", origin="SAS"),
        Property(
            name="CONTEXTPARAMS",
            value="1, claims_processing, /sas/Insurance/claims_processing.sas",
            origin="SAS",
        ),
    ]
    parent.steps = [child_call]

    child = plan()
    child.program = "Programs/Insurance/claims_processing.sas"
    child.job_name = "job_claims_processing"
    child.entry_macro = MacroEntrypoint(
        name="claims_processing",
        params=["proc_date"],
        arguments={"proc_date": "&CURR_DT"},
    )
    child.context_variables = [
        ContextVariable(name="proc_date", sas_value=None, suggested="context.proc_date", origin="SAS")
    ]

    arguments = build_apply_spec(
        parent,
        "Process/PruebasWebSAS/BatchJobs",
        related_plans=[child],
        related_folder_paths={child.program: "Process/PruebasWebSAS/Programs/Insurance"},
    ).to_mcp_arguments()

    child_spec = arguments["childJobs"][0]
    assert child_spec["contexts"][0]["name"] == "proc_date"
    assert child_spec["contexts"][0]["value"] == ""
    assert arguments["components"][0]["parameters"]["PROCESS"] == "job_claims_processing"
    assert arguments["components"][0]["tables"]["CONTEXTPARAMS"]["rows"] == [
        ["proc_date", "context.CURR_DT"]
    ]


def test_build_apply_spec_ignores_manual_progress_status_and_keeps_technical_warning():
    item = step("read_1", "tFileInputDelimited")
    item.status = "descartado"
    item.note = "No continuar por ahora"

    result = build_apply_spec(plan(item))
    arguments = result.to_mcp_arguments()

    assert [component.component_name for component in result.components] == ["tFileInputDelimited"]
    assert arguments["components"][0]["draftOnly"] is False
    assert "status" not in arguments["instructions"]["steps"][0]
    assert "note" not in arguments["instructions"]["steps"][0]


def test_pending_sas_information_is_kept_in_blank_job_contexts_without_invented_test_data():
    migration = plan()
    migration.program = "project/macros/load_customers.sas"
    migration.job_name = "load_customers"
    migration.context_variables = [
        ContextVariable(name="range_id", sas_value=None, suggested="context.range_id", origin="SAS")
    ]
    migration.unresolved = ["Confirmar formato físico del dataset"]
    migration.libraries_needed = [
        {"sas_name": "CUSTOMERS", "engine": "BASE", "path": None, "suggested_connection": "por determinar"}
    ]
    source = step("read_1", "por_determinar", verified=False, pending=["Identificar origen y esquema"])
    source.operation_id = "op_10_read_1"
    migration.children = [ChildJob(name="load_customers", params=["range_id"], steps=[source])]

    arguments = build_apply_spec(migration, "Process/PruebasWebSAS").to_mcp_arguments()

    assert arguments["components"] == []
    assert arguments["contexts"][0]["name"] == "range_id"
    assert arguments["contexts"][0]["value"] == ""
    pending_contexts = [item for item in arguments["contexts"] if item["name"].startswith("migration_todo_")]
    assert len(pending_contexts) < 10
    assert all(item["value"] == "" for item in pending_contexts)
    comments = "\n".join(item["comment"] for item in pending_contexts)
    assert "Identificar origen y esquema" in comments
    assert "Confirmar formato físico del dataset" in comments
    assert "CUSTOMERS" in comments
    serialized = str(arguments)
    assert "TEST_" not in serialized
    assert "synthetic_test_data" not in serialized
    assert "executionMode" not in arguments["instructions"]


def test_pending_details_for_one_sas_step_share_one_blank_context():
    source = step(
        "read_1",
        "tFileInputDelimited",
        verified=False,
        pending=["Confirmar formato del archivo", "Definir esquema de columnas"],
    )
    source.operation_id = "op_12_read_1"
    source.expressions = [Expression(sas="&input_file", talend=None, line=12)]
    result = build_apply_spec(plan(source)).to_mcp_arguments()

    pending_contexts = [item for item in result["contexts"] if item["name"].startswith("migration_todo_")]
    assert len(pending_contexts) == 1
    assert pending_contexts[0]["value"] == ""
    assert "Confirmar formato del archivo" in pending_contexts[0]["comment"]
    assert "Definir esquema de columnas" in pending_contexts[0]["comment"]
    assert "op_12_read_1" in pending_contexts[0]["comment"]


def test_pending_notes_do_not_block_creating_a_verified_component_as_draft():
    item = step("filter_1", "tFilterRow", pending=["Confirmar condición de filtrado"])

    result = build_apply_spec(plan(item), "Process/PruebasWebSAS")
    arguments = result.to_mcp_arguments()

    assert [component["componentName"] for component in arguments["components"]] == ["tFilterRow"]
    assert arguments["components"][0]["draftOnly"] is True
    assert result.blocked_steps == []
    assert any(
        context["value"] == "" and "Confirmar condición de filtrado" in context["comment"]
        for context in arguments["contexts"]
    )


def test_empty_plan_keeps_source_identity_in_context_so_each_guide_can_create_its_job():
    migration = plan()

    result = build_apply_spec(migration, "Process/PruebasWebSAS")

    assert result.ready_for_creation is True
    assert result.components == []
    assert result.to_mcp_arguments()["contexts"] == [
        {
            "name": "migration_source_program",
            "type": "id_String",
            "value": "daily.sas",
            "comment": "Programa SAS de origen incluido en esta guía.",
        }
    ]


def test_talend_destination_folder_follows_the_zip_program_directories(monkeypatch):
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")

    assert api_module._talend_apply_folder("client/macros/daily.sas") == (
        "Process/PruebasWebSAS/client/macros"
    )


def test_mcp_instructions_keep_source_macros_evidence_and_unresolved_data_without_progress_fields():
    parent = plan(step("parent", "tMap"))
    child_step = step("child-read", "tFileInputDelimited", pending=["Identificar el dataset"])
    child_step.status = "validado_manualmente"
    child_step.note = "Aprobado por usuario"
    child_step.assumptions = ["El orden SAS es secuencial"]
    child_step.expressions = [
        Expression(sas="upcase(name)", talend="StringHandling.UPCASE(name)", line=9, requires_semantic_validation=False)
    ]
    parent.children = [ChildJob(name="load_customers", params=["range_id"], steps=[child_step])]
    parent.libraries_needed = [{"sas_name": "dictionary", "engine": "BASE", "suggested_connection": "por determinar"}]
    parent.unresolved = ["Resolver formato de origen"]

    instructions = build_apply_spec(parent).to_mcp_arguments()["instructions"]

    assert instructions["source"] == {
        "projectId": "project-1",
        "program": "daily.sas",
        "sha256": "source-hash",
        "rulesVersion": "rules-7",
    }
    assert instructions["macros"][0]["name"] == "load_customers"
    macro_step = instructions["macros"][0]["steps"][0]
    assert macro_step["evidence"] == {"file": "daily.sas", "line": 4, "end_line": 4}
    assert macro_step["expressions"][0]["sas"] == "upcase(name)"
    assert macro_step["assumptions"] == ["El orden SAS es secuencial"]
    assert "status" not in macro_step and "note" not in macro_step
    assert instructions["libraries"][0]["sas_name"] == "dictionary"
    assert instructions["unresolved"] == ["Resolver formato de origen"]


def test_apply_folder_normalizes_windows_separators_before_sending_to_mcp():
    result = build_apply_spec(plan(step("read_1", "tFileInputDelimited")), "Process\\PruebasWebSAS")

    assert result.to_mcp_arguments()["folderPath"] == "Process/PruebasWebSAS"


def test_api_previews_and_creates_a_context_only_job_when_no_components_are_eligible(monkeypatch):
    migration = plan()
    migration.context_variables = [
        ContextVariable(name="range_id", sas_value=None, suggested="context.range_id", origin="SAS")
    ]
    migration.libraries_needed = [
        {"sas_name": "dictionary", "suggested_connection": "por_determinar (metadatos de archivo o base de datos)"}
    ]
    migration.unresolved = ["dataset_dynamic &TableParts."]
    monkeypatch.delenv("TALEND_MCP_READONLY", raising=False)
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    client = TestClient(api_module.app)

    preview = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )
    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply",
    )

    assert preview.status_code == 200
    assert preview.json()["ready"] is True
    assert preview.json()["components"] == []
    assert preview.json()["contexts"][0] == {
        "name": "range_id", "type": "id_String", "value": "", "comment": "Importado desde SAS: SAS"
    }
    assert any(
        context["name"].startswith("migration_todo_") and context["value"] == ""
        for context in preview.json()["contexts"]
    )
    assert response.status_code == 200
    assert response.json()["status"] == "applied"
    assert fake.calls[0]["components"] == []
    assert fake.calls[0]["contexts"][0]["name"] == "range_id"
    assert any(context["name"].startswith("migration_todo_") for context in fake.calls[0]["contexts"])


def test_api_previews_mcp_payload_without_writing_to_talend(monkeypatch):
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/Generated")
    migration = plan(step("read_1", "tFileInputDelimited"))
    migration.steps[0].verified = False
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    client = TestClient(api_module.app)

    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["ready"] is True
    assert len(body["preview_id"]) == 64
    assert body["tools"] == ["talend_job_apply_custom_spec"]
    assert body["components"][0]["draftOnly"] is True
    assert body["blocked_steps"] == []
    assert any(item["name"].startswith("migration_todo_") for item in body["contexts"])
    assert body["arguments"]["folderPath"] == "Process/Generated"
    assert any(
        route.path == "/api/projects/{project_id}/plans/{program:path}/talend-apply"
        and "POST" in getattr(route, "methods", set())
        for route in api_module.app.routes
    )


def test_api_preview_keeps_pending_library_details_in_job_context(monkeypatch):
    migration = plan()
    migration.libraries_needed = [
        LibraryNeeded(
            sas_name="dictionary",
            engine="BASE",
            suggested_connection="por determinar",
            note="Definir origen después",
        )
    ]
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    client = TestClient(api_module.app)

    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )

    assert response.status_code == 200
    pending_contexts = [
        context for context in response.json()["contexts"]
        if context["name"].startswith("migration_todo_")
    ]
    assert pending_contexts
    assert all(context["value"] == "" for context in pending_contexts)
    assert any("dictionary" in context["comment"] and "BASE" in context["comment"] for context in pending_contexts)




class ApplyAdapterFake:
    def __init__(self, result=None):
        self.result = result or {"jobName": "DailyJob", "itemPath": "process/PruebasWebSAS/DailyJob_0.1.item"}
        self.calls = []

    async def apply_custom_spec(self, arguments):
        self.calls.append(arguments)
        return self.result

    async def inspect_job(self, job_path):
        raise TalendError("Inspección no disponible en este adaptador de prueba")

    async def job_problems(self, job_name):
        raise TalendError("Problemas de Studio no disponibles en este adaptador de prueba")


def test_api_applies_ready_and_draft_components_in_one_request(monkeypatch):
    migration = plan(
        step("ready", "tFileInputDelimited"),
        step("pending", "tFilterRow", pending=["Confirmar filtro"]),
    )
    migration.steps[1].order = 2
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    client = TestClient(api_module.app)

    preview = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )
    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply",
    )

    assert preview.status_code == 200
    assert preview.json()["identity"]["folder_path"] == "Process/PruebasWebSAS"
    assert preview.json()["arguments"]["replaceManagedTodoContexts"] is True
    assert response.status_code == 200
    assert response.json()["status"] == "applied"
    assert response.json()["blocked_steps"] == []
    assert any(
        context["name"].startswith("migration_todo_") and "Confirmar filtro" in context["comment"]
        for context in fake.calls[0]["contexts"]
    )
    assert fake.calls[0]["folderPath"] == "Process/PruebasWebSAS"
    assert [item["uniqueName"] for item in fake.calls[0]["components"]] == [
        "tFileInputDelimited_1",
        "tFilterRow_2",
    ]
    assert fake.calls[0]["components"][1]["draftOnly"] is True


def test_api_marks_partial_only_when_the_mcp_did_not_create_every_requested_component(monkeypatch):
    migration = plan(
        step("source", "tFileInputDelimited"),
        step("filter", "tFilterRow", from_step="source"),
    )
    migration.steps[1].order = 2
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake(result={"totalComponents": 1, "connections": 0})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)

    response = TestClient(api_module.app).post(
        "/api/projects/project-1/plans/daily.sas/talend-apply",
    )

    assert response.status_code == 200
    assert response.json()["status"] == "partially_applied"


def test_api_rebuilds_the_current_plan_at_apply_time(monkeypatch):
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    migration = plan(step("ready", "tFileInputDelimited"))
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    client = TestClient(api_module.app)
    client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )
    migration.steps[0].purpose = "Cambio después del preview"

    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply",
    )

    assert response.status_code == 200
    assert len(fake.calls) == 1
    assert fake.calls[0]["instructions"]["steps"][0]["purpose"] == "Cambio después del preview"


def test_api_sends_known_component_as_draft_when_technical_data_is_missing(monkeypatch):
    migration = plan(step("unverified", "tFileInputDelimited", verified=False))
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    client = TestClient(api_module.app)
    client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )

    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply",
    )

    assert response.status_code == 200
    assert len(fake.calls) == 1
    assert fake.calls[0]["components"][0]["draftOnly"] is True



def test_api_rejects_apply_in_readonly_mode(monkeypatch):
    monkeypatch.setenv("TALEND_MCP_READONLY", "true")
    migration = plan(step("ready", "tFileInputDelimited"))
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake()
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    client = TestClient(api_module.app)
    client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={},
    )

    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply",
    )

    assert response.status_code == 403
    assert fake.calls == []


def test_api_uses_server_configured_folder_not_browser_folder(monkeypatch):
    monkeypatch.setenv("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS")
    migration = plan(step("ready", "tFileInputDelimited"))
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    client = TestClient(api_module.app)

    response = client.post(
        "/api/projects/project-1/plans/daily.sas/talend-apply/preview",
        json={"folder_path": "Process/Other"},
    )

    assert response.status_code == 200
    assert response.json()["identity"]["folder_path"] == "Process/PruebasWebSAS"


def test_api_applies_current_plan_without_preview_token_or_manual_status(monkeypatch):
    migration = plan(step("read_1", "tFileInputDelimited"))
    migration.steps[0].status = "descartado"
    migration.steps[0].note = "No continuar"
    monkeypatch.setenv("TALEND_MCP_READONLY", "false")
    monkeypatch.setattr(
        api_module,
        "_plans",
        lambda _project_id: PlanSet(project_id="project-1", rules_version="rules-7", plans=[migration]),
    )
    fake = ApplyAdapterFake({"jobName": "DailyJob", "generatedComponents": 1, "warnings": []})
    monkeypatch.setattr(api_module, "_talend", lambda: fake)
    client = TestClient(api_module.app)

    response = client.post("/api/projects/project-1/plans/daily.sas/talend-apply")

    assert response.status_code == 200
    assert len(fake.calls) == 1
    assert fake.calls[0]["instructions"]["source"]["program"] == "daily.sas"
    assert fake.calls[0]["components"][0]["componentName"] == "tFileInputDelimited"
    assert "status" not in fake.calls[0]["instructions"]["steps"][0]
