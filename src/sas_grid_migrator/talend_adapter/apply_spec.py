"""Deterministic conversion from migration plans to the talend-mcp custom-job contract."""

import hashlib
import re
from pathlib import PurePosixPath
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from sas_grid_migrator.migration_planner.models import (
    Connection,
    ContextVariable,
    JobPlan,
    PlanStep,
    Property,
)


class ApplyBlock(BaseModel):
    step_id: str
    reason: str


class ApplySchemaColumn(BaseModel):
    name: str
    type: str
    nullable: bool | None = None
    length: int | None = None
    precision: int | None = None


class ApplySchema(BaseModel):
    name: str
    connector: str = "FLOW"
    columns: list[ApplySchemaColumn]


class ApplyComponent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    unique_name: str = Field(alias="uniqueName")
    component_name: str = Field(alias="componentName")
    pos_x: int = Field(alias="posX")
    pos_y: int = Field(alias="posY")
    label: str
    parameters: dict[str, str]
    schema_: ApplySchema | None = Field(default=None, alias="schema")
    tables: dict[str, Any] | None = None
    mapper: dict[str, Any] | None = None
    draft_only: bool = Field(default=False, alias="draftOnly")
    draft_reason: str | None = Field(default=None, alias="draftReason")


class ApplyConnection(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    source: str
    target: str
    label: str
    connector_name: str = Field(alias="connectorName")
    unique_name: str = Field(alias="uniqueName")


class ApplyContext(BaseModel):
    name: str
    type: str = "id_String"
    value: str
    comment: str


class TalendApplySpec(BaseModel):
    contract_version: str = "1"
    project_id: str
    program: str
    source_sha256: str | None
    rules_version: str
    job_name: str
    folder_path: str
    components: list[ApplyComponent]
    connections: list[ApplyConnection]
    blocked_steps: list[ApplyBlock]
    contexts: list[ApplyContext] = []
    child_jobs: list[dict[str, Any]] = Field(default_factory=list)
    instructions: dict[str, Any]

    @property
    def ready_for_creation(self) -> bool:
        """A new Job can be created when it has at least one node or context variable."""
        return bool(self.components or self.contexts or self.child_jobs)

    def to_mcp_arguments(self) -> dict[str, Any]:
        """Return the typed plan that the MCP executes through Talend Studio."""
        return {
            "jobName": self.job_name,
            "version": "0.1",
            "defaultContext": "Default",
            "folderPath": self.folder_path,
            "description": f"Migrated from SAS program {self.program}",
            "purpose": f"Generated from migration plan {self.rules_version}",
            "components": [
                item.model_dump(
                    by_alias=True,
                    exclude_none=True,
                )
                for item in self.components
            ],
            "connections": [item.model_dump(by_alias=True) for item in self.connections],
            "contexts": [item.model_dump() for item in self.contexts],
            "replaceManagedTodoContexts": True,
            "childJobs": self.child_jobs,
            "instructions": self.instructions,
        }


_ALLOWED_ACTIONS = frozenset({"add_component", "configure"})
_CONNECTORS = {
    "Main": "FLOW",
    # Lookup describe el rol de entrada en tMap, pero Talend exige el
    # conector de salida real del componente origen (por ejemplo, FLOW en
    # tTeradataInput). Se conserva el rol Lookup en las instrucciones SAS.
    "Lookup": "FLOW",
    "Reject": "REJECT",
    "OnSubjobOk": "SUBJOB_OK",
    "OnComponentOk": "COMPONENT_OK",
    "Iterate": "ITERATE",
}

def _safe_folder_path(folder_path: str) -> str:
    normalized = folder_path.replace("\\", "/").strip("/")
    parts = normalized.split("/") if normalized else []
    if not parts or parts[0].casefold() != "process":
        raise ValueError("La carpeta Talend debe estar dentro de Process/.")
    if any(part in {".", ".."} or not re.fullmatch(r"[\w .-]+", part) for part in parts):
        raise ValueError("La carpeta Talend contiene una ruta no permitida.")
    return "/".join(parts)


def _instruction_step(step: PlanStep) -> dict[str, Any]:
    """Describe the SAS step without copying legacy user progress or notes."""
    return {
        "id": step.id,
        "order": step.order,
        "subjob": step.subjob,
        "action": step.action,
        "operationId": step.operation_id,
        "operationType": step.operation_type,
        "componentCandidate": step.component_candidate,
        "alternatives": step.alternatives,
        "purpose": step.purpose,
        "properties": [item.model_dump(mode="json") for item in step.properties],
        "expressions": [item.model_dump(mode="json") for item in step.expressions],
        "schema": [item.model_dump(mode="json") for item in step.schema_columns],
        "dependencies": [
            {"type": item.type, "fromStep": item.from_step, "label": item.label}
            for item in step.connections
        ],
        "assumptions": step.assumptions,
        "pending": step.pending,
        "tests": step.tests,
        "evidence": step.evidence.model_dump(mode="json"),
        "confidence": step.confidence,
        "verified": step.verified,
        "inCatalog": step.in_catalog,
        "docUrl": step.doc_url,
        "variants": step.variants,
        "requiresSemanticValidation": step.requires_semantic_validation,
    }


def _json_model(value: Any) -> Any:
    return value.model_dump(mode="json") if isinstance(value, BaseModel) else value


def _pending_details(plan: JobPlan, resolved_program_steps: set[str] | None = None) -> list[str]:
    steps = [*plan.steps, *(step for child in plan.children for step in child.steps)]
    source_macro = PurePosixPath(plan.program.replace("\\", "/")).stem.casefold()
    resolved_steps = resolved_program_steps or set()
    details: list[str] = []
    for step in steps:
        if step.operation_type == "macro_call":
            called_macro = (_step_property_value(step, "PROCESS") or "").strip().strip("\"'").lstrip("%").casefold()
            if called_macro == source_macro or step.id in resolved_steps:
                continue
        location = f"{step.evidence.file}:{step.evidence.line}"
        block_reason = _step_block_reason(step)
        if block_reason:
            details.append(f"Paso {step.operation_id or step.id} ({location}): {block_reason}")
        if not step.verified or step.confidence != "high":
            details.append(
                f"Paso {step.operation_id or step.id} ({location}): componente o configuración pendiente de validación; completar en Talend."
            )
        for pending in step.pending:
            details.append(f"Paso {step.operation_id or step.id} ({location}): {pending}")
        for prop in step.properties:
            if not prop.verified or prop.value is None:
                details.append(
                    f"Paso {step.operation_id or step.id} ({location}): propiedad {prop.name} "
                    f"sin valor verificado; origen indicado por el portal: {prop.origin}."
                )
        for expression in step.expressions:
            if expression.talend is None or expression.requires_semantic_validation:
                details.append(
                    f"Paso {step.operation_id or step.id} ({location}): expresión SAS "
                    f"{expression.sas} sin traducción Talend verificada."
                )
        for column in step.schema_columns:
            if not column.name or not column.talend_type:
                details.append(
                    f"Paso {step.operation_id or step.id} ({location}): falta definir el nombre "
                    "o tipo Talend de una columna del esquema."
                )
        if step.operation_type == "include":
            included = _step_property_value(step, "PROCESS")
            details.append(
                f"Include SAS {included or step.operation_id or step.id}: revisar como configuración o código compartido; no se creó un Job hijo."
            )
        elif step.operation_type == "macro_call":
            macro = _step_property_value(step, "PROCESS")
            arguments = _step_property_value(step, "CONTEXTPARAMS")
            called_macro = (macro or "").strip().strip("\"'").lstrip("%").casefold()
            if macro and called_macro != source_macro and not _static_sas_program(arguments or ""):
                details.append(
                    f"Macro auxiliar %{macro}: falta traducir su lógica o parámetros a Talend; no se creó un Job hijo."
                )

    details.extend(f"Pendiente del Job: {item}" for item in plan.unresolved)
    for item in plan.context_variables:
        variable = ContextVariable.model_validate(item)
        if variable.sas_value is None or variable.sas_value == "":
            details.append(
                f"Variable de contexto {variable.name}: el valor de SAS no está informado; "
                "completarlo en Talend cuando se confirme."
            )
    for library in plan.libraries_needed:
        library_data = _json_model(library)
        details.append(
            "Biblioteca SAS "
            f"{library_data.get('sas_name', 'sin nombre')}: motor={library_data.get('engine') or 'sin informar'}; "
            f"ruta={library_data.get('path') or 'sin informar'}; "
            f"conexión sugerida por el portal={library_data.get('suggested_connection') or 'sin informar'}."
        )
    for child in plan.children:
        if child.name.casefold() == PurePosixPath(plan.program.replace("\\", "/")).stem.casefold():
            for parameter in child.params:
                details.append(
                    f"Parámetro de macro {parameter}: completar el valor del contexto Talend cuando se confirme."
                )
    if plan.entry_macro:
        existing_context_names = {item.name.casefold() for item in plan.context_variables}
        for parameter in plan.entry_macro.params:
            if parameter.casefold() not in existing_context_names:
                details.append(
                    f"Parámetro de macro {parameter}: completar el valor del contexto Talend cuando se confirme."
                )
    for case in plan.validation_cases:
        details.append(f"Validación pendiente {case.kind}: {case.description}")
    details.extend(
        f"Orquestación SAS Grid: {item.instruction} {item.reason}".strip()
        for item in plan.orchestration.grid_recommendations
    )
    details.extend(f"Horario SAS pendiente: {item}" for item in plan.orchestration.schedules)
    return list(dict.fromkeys(detail for detail in details if detail.strip()))


def _pending_contexts(
    plan: JobPlan,
    existing_names: set[str],
    resolved_program_steps: set[str] | None = None,
) -> list[ApplyContext]:
    groups: dict[str, list[str]] = {}
    for detail in _pending_details(plan, resolved_program_steps):
        step = re.match(r"^Paso ([^ ]+) \([^)]+\):", detail)
        if step:
            group = f"step:{step.group(1)}"
        elif detail.startswith("Variable de contexto "):
            group = f"context:{detail.removeprefix('Variable de contexto ').split(':', 1)[0]}"
        elif detail.startswith("Biblioteca SAS "):
            group = f"library:{detail.removeprefix('Biblioteca SAS ').split(':', 1)[0]}"
        elif detail.startswith("Parámetro de macro "):
            group = f"macro-parameter:{detail.removeprefix('Parámetro de macro ').split(':', 1)[0]}"
        elif detail.startswith("Validación pendiente "):
            group = f"validation:{detail.removeprefix('Validación pendiente ').split(':', 1)[0]}"
        elif detail.startswith("Orquestación SAS Grid:"):
            group = "grid"
        elif detail.startswith("Horario SAS pendiente:"):
            group = "schedule"
        elif detail.startswith("Include SAS "):
            group = "includes"
        elif detail.startswith("Macro auxiliar "):
            group = "macro-helpers"
        else:
            group = "job"
        groups.setdefault(group, []).append(detail)

    contexts: list[ApplyContext] = []
    for group, details in groups.items():
        identity = f"{plan.program}\0{plan.sha256 or ''}\0{group}"
        suffix = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12]
        name = f"migration_todo_{suffix}"
        if name in existing_names:
            continue
        existing_names.add(name)
        body = "\n".join(f"- {detail}" for detail in details)
        contexts.append(
            ApplyContext(
                name=name,
                value="",
                comment=f"Información técnica pendiente del portal ({group}):\n{body}",
            )
        )
    return contexts


def _portal_instructions(
    plan: JobPlan, folder_path: str, blocked_steps: list[ApplyBlock], pending: list[str]
) -> dict[str, Any]:
    all_steps = [*plan.steps, *(step for child in plan.children for step in child.steps)]
    assumptions = list(dict.fromkeys(assumption for step in all_steps for assumption in step.assumptions))
    return {
        "source": {
            "projectId": plan.project_id,
            "program": plan.program,
            "sha256": plan.sha256,
            "rulesVersion": plan.rules_version,
        },
        "job": {"name": plan.job_name, "folderPath": folder_path},
        "entryMacro": _json_model(plan.entry_macro) if plan.entry_macro else None,
        "steps": [_instruction_step(step) for step in sorted(plan.steps, key=lambda item: (item.order, item.id))],
        "macros": [
            {
                "name": child.name,
                "parameters": child.params,
                "steps": [_instruction_step(step) for step in sorted(child.steps, key=lambda item: (item.order, item.id))],
            }
            for child in plan.children
        ],
        "assumptions": assumptions,
        "contextVariables": [_json_model(item) for item in plan.context_variables],
        "libraries": [_json_model(item) for item in plan.libraries_needed],
        "orchestration": plan.orchestration.model_dump(mode="json"),
        "validationCases": [_json_model(item) for item in plan.validation_cases],
        "pending": pending,
        "unresolved": plan.unresolved,
        "blockedSteps": [item.model_dump(mode="json") for item in blocked_steps],
    }


def _step_property_value(step: PlanStep, name: str) -> str | None:
    return next((prop.value for prop in step.properties if prop.name == name and prop.value is not None), None)


def _static_sas_program(value: str) -> str | None:
    matches = re.findall(r"(?i)(?:[a-z]:[\\/]|/)[^,;\r\n\"']+?\.sas\b", value)
    return matches[-1].strip() if matches else None


def _step_block_reason(step: PlanStep) -> str | None:
    if step.action not in {*_ALLOWED_ACTIONS, "manual_decision"}:
        return "La acción de este paso requiere intervención manual."
    if step.component_candidate in {"", "por_determinar", "ninguno"}:
        return "No hay un componente Talend definido para este paso."
    return None


def _macro_arguments(plan: JobPlan) -> dict[str, str]:
    if plan.entry_macro:
        return {name.casefold(): value for name, value in plan.entry_macro.arguments.items()}
    source_macro = PurePosixPath(plan.program.replace("\\", "/")).stem.casefold()
    own_call = next(
        (
            step
            for step in plan.steps
            if step.operation_type == "macro_call"
            and (_step_property_value(step, "PROCESS") or "").strip().casefold() == source_macro
        ),
        None,
    )
    raw = _step_property_value(own_call, "CONTEXTPARAMS") if own_call else None
    if not raw:
        return {}
    return {
        name.casefold(): value.strip().strip("\"'")
        for name, value in re.findall(r"(?i)([a-z_]\w*)\s*=\s*([^,\r\n]+)", raw)
    }


def _resolve_program_target(value: str, plans: list[JobPlan]) -> JobPlan | None:
    source = _static_sas_program(value)
    if not source:
        return None
    basename = PurePosixPath(source.replace("\\", "/")).name.casefold()
    matches = [
        candidate
        for candidate in plans
        if PurePosixPath(candidate.program.replace("\\", "/")).name.casefold() == basename
    ]
    return matches[0] if len(matches) == 1 else None


def _component_step(step: PlanStep, child_plan: JobPlan | None = None) -> PlanStep:
    converted = step.model_copy(deep=True)
    if child_plan is None:
        return converted
    converted.component_candidate = "tRunJob"
    converted.purpose = f"Ejecutar Job hijo {child_plan.job_name}"
    converted.action = "add_component"
    converted.properties = [prop for prop in converted.properties if prop.name not in {"PROCESS", "CONTEXTPARAMS"}]
    converted.properties.append(
        Property(name="PROCESS", value=child_plan.job_name, origin="Programa SAS hijo resuelto en el ZIP", verified=True)
    )
    converted.pending = []
    converted.confidence = "high"
    converted.verified = True
    return converted


def _child_context_table(parent: JobPlan, child: JobPlan, parameters: list[str]) -> dict[str, Any] | None:
    assignments = _macro_arguments(child)
    parent_contexts = {item.name.casefold() for item in (ContextVariable.model_validate(x) for x in parent.context_variables)}
    own_macro = next(
        (macro for macro in child.children if macro.name.casefold() == PurePosixPath(child.program.replace("\\", "/")).stem.casefold()),
        None,
    )
    names = set(
        child.entry_macro.params
        if child.entry_macro
        else own_macro.params
        if own_macro
        else parameters
    )
    rows: list[list[str]] = []
    for parameter in parameters:
        if parameter.casefold() not in names:
            continue
        value = assignments.get(parameter.casefold())
        if not value:
            continue
        variable = re.fullmatch(r"&([a-z_]\w*)\.?", value, flags=re.IGNORECASE)
        if variable:
            context_name = variable.group(1)
            if context_name.casefold() not in parent_contexts:
                continue
            value = f"context.{context_name}"
        elif value.startswith("&") or "%" in value:
            continue
        rows.append([parameter, value])
    if not rows:
        return None
    return {
        "CONTEXTPARAMS": {
            "columns": ["PARAM_NAME_COLUMN", "PARAM_VALUE_COLUMN"],
            "rows": rows,
        }
    }


def build_apply_spec(
    plan: JobPlan,
    folder_path: str = "Process",
    *,
    related_plans: list[JobPlan] | None = None,
    related_folder_paths: dict[str, str] | None = None,
    _visited_programs: set[str] | None = None,
) -> TalendApplySpec:
    """Build a deterministic spec without filling missing SAS details with sample values."""
    safe_folder = _safe_folder_path(folder_path)
    eligible: dict[str, PlanStep] = {}
    draft_steps: dict[str, tuple[PlanStep, str]] = {}
    candidate_steps: dict[str, PlanStep] = {}

    source_macro = PurePosixPath(plan.program.replace("\\", "/")).stem.casefold()
    inline_children = [
        child
        for child in plan.children
        if plan.entry_macro is None and child.name.casefold() == source_macro
    ]
    plans = related_plans or []
    visited = set(_visited_programs or set())
    visited.add(plan.program.casefold())
    inline_steps = [step for child in inline_children for step in child.steps]
    source_steps = [*plan.steps, *inline_steps]
    resolved_children_by_step: dict[str, JobPlan] = {}
    child_call_steps: list[PlanStep] = []
    for step in source_steps:
        if step.operation_type == "include":
            continue
        if step.operation_type == "macro_call":
            called_macro = (_step_property_value(step, "PROCESS") or "").strip().strip("\"'").lstrip("%").casefold()
            if called_macro == source_macro:
                continue
            arguments = _step_property_value(step, "CONTEXTPARAMS") or ""
            target = _resolve_program_target(arguments, plans)
            if target and target.program in (related_folder_paths or {}) and target.program.casefold() not in visited:
                resolved_children_by_step[step.id] = target
                child_call_steps.append(step)
                continue
            continue
        candidate_steps[step.id] = step

    # `%run_step` es una envoltura SAS; los programas resueltos se ejecutan en
    # secuencia como Jobs hijos y no como macros SAS llamadas por tRunJob.
    for index, step in enumerate(child_call_steps):
        child_plan = resolved_children_by_step[step.id]
        converted = _component_step(step, child_plan)
        if index:
            converted.connections = [
                Connection(type="OnSubjobOk", from_step=child_call_steps[index - 1].id)
            ]
        else:
            converted.connections = []
        candidate_steps[step.id] = converted

    def include_step(step: PlanStep) -> None:
        reason = _step_block_reason(step)
        needs_draft = (
            bool(step.pending)
            or step.action == "manual_decision"
            or not step.verified
            or step.confidence != "high"
            or any(not prop.verified or prop.value is None for prop in step.properties)
            or any(expression.talend is None or expression.requires_semantic_validation for expression in step.expressions)
            or any(not column.name or not column.talend_type for column in step.schema_columns)
        )
        if reason is None and not needs_draft:
            eligible[step.id] = step
            return

        can_create_draft = (
            step.action in {*_ALLOWED_ACTIONS, "manual_decision"}
            and step.component_candidate not in {"", "por_determinar"}
            and step.component_candidate != "ninguno"
        )
        if can_create_draft:
            pending = [*step.pending]
            if any(not prop.verified or prop.value is None for prop in step.properties):
                pending.append("Hay propiedades sin valor confirmado; se conservarán en el contexto del Job.")
            if any(expression.talend is None or expression.requires_semantic_validation for expression in step.expressions):
                pending.append("Hay expresiones SAS pendientes de traducción o validación semántica.")
            if any(not column.name or not column.talend_type for column in step.schema_columns):
                pending.append("Faltan nombres o tipos Talend para completar el esquema.")
            if step.confidence != "high" or not step.verified:
                pending.append("El componente o su configuración aún no está verificado en Studio.")
            draft_reason = reason or f"Información técnica pendiente: {'; '.join(dict.fromkeys(pending)) or 'completar en Studio'}"
            draft_steps[step.id] = (step, draft_reason)

    positioned_source_steps = sorted(
        [step for step in source_steps if step.operation_type not in {"include", "macro_call"}],
        key=lambda item: (item.order, item.id),
    )
    for step in positioned_source_steps:
        candidate = candidate_steps.get(step.id)
        if candidate:
            include_step(candidate)
    for step in child_call_steps:
        include_step(candidate_steps[step.id])

    ordered_steps = sorted(eligible.values(), key=lambda item: (item.order, item.id))
    ordered_drafts = sorted(
        draft_steps.values(), key=lambda item: (item[0].order, item[0].id)
    )
    positioned_steps = sorted(
        [*eligible.values(), *(step for step, _ in ordered_drafts)],
        key=lambda item: (item.order, item.id),
    )
    positions = {step.id: index for index, step in enumerate(positioned_steps)}
    unique_names = {step.id: f"{step.component_candidate}_{index}" for index, step in enumerate(ordered_steps, 1)}
    unique_names.update(
        {
            step.id: f"{step.component_candidate}_{len(ordered_steps) + index}"
            for index, (step, _) in enumerate(ordered_drafts, 1)
        }
    )
    components: list[ApplyComponent] = []
    connections: list[ApplyConnection] = []

    component_tables: dict[str, dict[str, Any]] = {}
    for step in positioned_steps:
        unique_name = unique_names[step.id]
        is_draft = step.id in draft_steps
        draft_reason = draft_steps[step.id][1] if is_draft else None
        columns = [
            ApplySchemaColumn(
                name=column.name,
                type=column.talend_type or "",
                nullable=column.nullable,
                length=column.length,
                precision=column.precision,
            )
            for column in step.schema_columns
        ]
        has_complete_schema = bool(columns) and all(column.name and column.type for column in columns)
        schema = (
            ApplySchema(name=f"{unique_name}_schema", columns=columns)
            if has_complete_schema
            else None
        )
        verified_parameters = {
            prop.name: prop.value
            for prop in step.properties
            if prop.verified and prop.value is not None
        }
        child_plan = resolved_children_by_step.get(step.id)
        if child_plan:
            verified_parameters["PROCESS"] = child_plan.job_name
            if child_plan.entry_macro:
                table = _child_context_table(plan, child_plan, child_plan.entry_macro.params)
                if table:
                    component_tables[step.id] = table
            macro = next(
                (item for item in child_plan.children if item.name.casefold() == PurePosixPath(child_plan.program.replace("\\", "/")).stem.casefold()),
                None,
            )
            if macro and not child_plan.entry_macro:
                table = _child_context_table(plan, child_plan, macro.params)
                if table:
                    component_tables[step.id] = table
        operation_identity = step.operation_id or step.id
        components.append(
            ApplyComponent(
                uniqueName=unique_name,
                componentName=step.component_candidate,
                posX=160 + positions[step.id] * 280,
                posY=96,
                label=f"{step.purpose} [{operation_identity}]",
                parameters=verified_parameters,
                tables=component_tables.get(step.id),
                schema_=schema,
                draftOnly=is_draft,
                draftReason=draft_reason,
            )
        )
        for edge_index, edge in enumerate(step.connections, 1):
            if edge.from_step not in unique_names or edge.type not in _CONNECTORS:
                continue
            connector = _CONNECTORS[edge.type]
            connections.append(
                ApplyConnection(
                    source=unique_names[edge.from_step],
                    target=unique_name,
                    label=edge.label or f"row_{step.order}_{edge_index}",
                    connectorName=connector,
                    uniqueName=f"{connector.lower()}_{step.order}_{edge_index}",
                )
            )

    child_jobs: list[dict[str, Any]] = []
    folder_paths = related_folder_paths or {}
    included_child_programs: set[str] = set()
    for step in child_call_steps:
        child_plan = resolved_children_by_step[step.id]
        program_key = child_plan.program.casefold()
        if program_key in included_child_programs:
            continue
        included_child_programs.add(program_key)
        child_folder = folder_paths.get(child_plan.program)
        if not child_folder:
            continue
        child_spec = build_apply_spec(
            child_plan,
            child_folder,
            related_plans=plans,
            related_folder_paths=folder_paths,
            _visited_programs=visited,
        )
        child_jobs.append(child_spec.to_mcp_arguments())

    blocked_steps: list[ApplyBlock] = []
    contexts = [
        ApplyContext(
            name=variable.name,
            value=variable.sas_value or "",
            comment=f"Importado desde SAS: {variable.origin}",
        )
        for variable in (ContextVariable.model_validate(item) for item in plan.context_variables)
    ]
    context_names = {context.name for context in contexts}
    for child in inline_children:
        for parameter in child.params:
            if parameter.casefold() in {name.casefold() for name in context_names}:
                continue
            contexts.append(
                ApplyContext(
                    name=parameter,
                    value="",
                    comment=f"Parámetro de la macro SAS {child.name}; completar en Talend cuando se confirme.",
                )
            )
            context_names.add(parameter)
    if plan.entry_macro:
        for parameter in plan.entry_macro.params:
            if parameter.casefold() in {name.casefold() for name in context_names}:
                continue
            contexts.append(
                ApplyContext(
                    name=parameter,
                    value="",
                    comment=f"Parámetro de la macro SAS {plan.entry_macro.name}; completar en Talend cuando se confirme.",
                )
            )
            context_names.add(parameter)
    pending_contexts = _pending_contexts(plan, context_names, set(resolved_children_by_step))
    contexts.extend(pending_contexts)
    pending_details = [context.comment for context in pending_contexts]
    if not components and not contexts:
        contexts.append(
            ApplyContext(
                name="migration_source_program",
                value=plan.program,
                comment="Programa SAS de origen incluido en esta guía.",
            )
        )

    return TalendApplySpec(
        project_id=plan.project_id,
        program=plan.program,
        source_sha256=plan.sha256,
        rules_version=plan.rules_version,
        job_name=plan.job_name,
        folder_path=safe_folder,
        components=components,
        connections=connections,
        contexts=contexts,
        child_jobs=child_jobs,
        blocked_steps=blocked_steps,
        instructions=_portal_instructions(plan, safe_folder, blocked_steps, pending_details),
    )
