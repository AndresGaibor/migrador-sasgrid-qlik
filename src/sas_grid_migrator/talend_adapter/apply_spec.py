"""Deterministic conversion from migration plans to the talend-mcp custom-job contract."""

import hashlib
import re
from pathlib import Path, PurePosixPath
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from sas_grid_migrator.migration_planner.expressions import is_simple_arithmetic_translation
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
    description: str | None = None
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
            "description": self.description or f"Migrated from SAS program {self.program}",
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


def _component_label(purpose: str, operation_identity: str, fallback_order: int) -> str:
    """Crea una etiqueta corta sin perder la referencia al paso SAS."""
    match = re.match(r"op_(\d+)_", operation_identity, flags=re.IGNORECASE)
    sas_reference = match.group(1) if match else str(fallback_order)
    suffix = f" · SAS {sas_reference}"
    compact_purpose = " ".join(purpose.split()).strip() or "Paso SAS"
    max_purpose_length = 64 - len(suffix)
    if len(compact_purpose) > max_purpose_length:
        compact_purpose = compact_purpose[: max_purpose_length - 1].rsplit(" ", 1)[0].rstrip(" ,;:-")
        if not compact_purpose:
            compact_purpose = purpose[: max_purpose_length - 1].rstrip()
        compact_purpose += "…"
    return f"{compact_purpose}{suffix}"


def _bigdecimal_expression(expression: str) -> str | None:
    """Translate basic +, - and * into compilable BigDecimal calls; division stays pending."""
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[()+*/-]", expression)
    if not tokens or "".join(tokens) != re.sub(r"\s+", "", expression) or "/" in tokens:
        return None
    index = 0

    def primary() -> str | None:
        nonlocal index
        if index >= len(tokens):
            return None
        token = tokens[index]
        if token in {"+", "-"}:
            index += 1
            child = primary()
            if child is None:
                return None
            return child if token == "+" else f"({child}).negate()"
        if token == "(":
            index += 1
            child = additive()
            if child is None or index >= len(tokens) or tokens[index] != ")":
                return None
            index += 1
            return f"({child})"
        index += 1
        if re.fullmatch(r"\d+(?:\.\d+)?", token):
            return f'new java.math.BigDecimal("{token}")'
        if "." in token:
            return f"new java.math.BigDecimal(String.valueOf({token}))"
        return None

    def multiplicative() -> str | None:
        nonlocal index
        value = primary()
        while value is not None and index < len(tokens) and tokens[index] in {"*", "/"}:
            operator = tokens[index]
            index += 1
            right = primary()
            if right is None or operator == "/":
                return None
            value = f"({value}).multiply({right})"
        return value

    def additive() -> str | None:
        nonlocal index
        value = multiplicative()
        while value is not None and index < len(tokens) and tokens[index] in {"+", "-"}:
            operator = tokens[index]
            index += 1
            right = multiplicative()
            if right is None:
                return None
            method = "add" if operator == "+" else "subtract"
            value = f"({value}).{method}({right})"
        return value

    value = additive()
    return value if value is not None and index == len(tokens) else None


def _build_tmap_mapper(
    step: PlanStep, candidate_steps: dict[str, PlanStep]
) -> tuple[dict[str, Any] | None, list[ApplySchemaColumn] | None, str | None]:
    """Build a tMap for one main input and output with explicit typed columns."""
    incoming = list(enumerate(step.connections, 1))
    if len(incoming) != 1 or incoming[0][1].type != "Main" or not incoming[0][1].from_step:
        return None, None, "El tMap requiere una sola conexión Main de entrada conocida."
    source_step = candidate_steps.get(incoming[0][1].from_step or "")
    if source_step is None:
        return None, None, "No se encontró el componente que alimenta el tMap."
    input_name = incoming[0][1].label or f"row_{step.order}_{incoming[0][0]}"
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", input_name):
        return None, None, "El nombre de la conexión de entrada del tMap no es válido."
    input_columns = {column.name: column for column in source_step.schema_columns if column.name}
    if not input_columns or any(not column.talend_type for column in input_columns.values()):
        return None, None, "El tMap requiere un esquema de entrada con tipos conocidos."
    if any(
        expression.requires_semantic_validation
        or expression.warnings
        or not is_simple_arithmetic_translation(expression.talend)
        for expression in step.expressions
    ):
        return None, None, "La expresión no pertenece al subconjunto seguro de referencias directas y aritmética simple."

    output_edges = [
        (target, edge, edge_index)
        for target in sorted(candidate_steps.values(), key=lambda item: (item.order, item.id))
        for edge_index, edge in enumerate(target.connections, 1)
        if edge.from_step == step.id
    ]
    if len(output_edges) != 1 or output_edges[0][1].type != "Main":
        return None, None, "El tMap requiere una sola conexión Main de salida conocida."
    output_target, output_edge, output_edge_index = output_edges[0]
    output_name = output_edge.label or f"row_{output_target.order}_{output_edge_index}"
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", output_name):
        return None, None, "El nombre de la conexión de salida del tMap no es válido."

    assignments: dict[str, Any] = {}
    for expression in step.expressions:
        if not expression.target or expression.target in assignments:
            return None, None, "Cada expresión del tMap debe tener una columna destino única."
        if expression.requires_semantic_validation or expression.warnings or not is_simple_arithmetic_translation(expression.talend):
            return None, None, "La expresión no pertenece al subconjunto seguro de referencias directas y aritmética simple."
        translated = (expression.talend or "").replace("input_row.", f"{input_name}.")
        references = re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\.([A-Za-z_][A-Za-z0-9_]*)", translated)
        if not references or any(table != input_name or column not in input_columns for table, column in references):
            return None, None, "La expresión del tMap usa una columna o tabla de entrada desconocida."
        reference_names = list(dict.fromkeys(column for _, column in references))
        target_column = next((item for item in step.schema_columns if item.name == expression.target), None)
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[()+*/-]", translated)
        has_arithmetic = any(token in {"+", "-", "*", "/"} for token in tokens)
        if has_arithmetic:
            numeric_types = {"id_Byte", "id_Short", "id_Integer", "id_Long", "id_Float", "id_Double", "id_BigDecimal"}
            if target_column is None or target_column.talend_type != "id_BigDecimal":
                return None, None, "La aritmética automática se limita a columnas destino id_BigDecimal para conservar un tipo compilable."
            if any(input_columns[name].talend_type not in numeric_types for name in reference_names):
                return None, None, "La aritmética del tMap requiere columnas numéricas con tipo conocido."
            if any(input_columns[name].nullable is not False for name in reference_names):
                return None, None, "La aritmética del tMap requiere columnas de entrada no nulas para evitar diferencias con SAS."
            compiled = _bigdecimal_expression(translated)
            if compiled is None:
                return None, None, "La división o la expresión requiere una regla de precisión/escala que debe confirmarse."
            translated = compiled
        assignments[expression.target] = (translated, reference_names)

    if not assignments:
        return None, None, "El plan no contiene asignaciones que se puedan mapear automáticamente."

    output_schema: list[ApplySchemaColumn] = []
    output_columns: list[dict[str, Any]] = []
    for column in step.schema_columns:
        if not column.name or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", column.name):
            return None, None, "El esquema de salida del tMap contiene una columna sin nombre válido."
        if column.name in assignments:
            expression, references = assignments[column.name]
        elif column.name in input_columns:
            expression, references = f"{input_name}.{column.name}", [column.name]
        else:
            return None, None, f"Falta una expresión segura para la columna de salida {column.name}."
        reference_types = {input_columns[name].talend_type for name in references}
        talend_type = column.talend_type or (next(iter(reference_types)) if len(reference_types) == 1 else None)
        if not talend_type:
            return None, None, f"No se pudo determinar el tipo Talend de la columna {column.name}."
        nullable = column.nullable
        if nullable is None:
            nullability = {input_columns[name].nullable for name in references}
            nullable = True if True in nullability else False if nullability == {False} else None
        output_schema.append(
            ApplySchemaColumn(
                name=column.name,
                type=talend_type,
                nullable=nullable,
                length=column.length,
                precision=column.precision,
            )
        )
        output_columns.append(
            {
                "name": column.name,
                "type": talend_type,
                **({"nullable": nullable} if nullable is not None else {}),
                "expression": expression,
            }
        )
    if not output_schema:
        return None, None, "El tMap requiere un esquema de salida explícito."

    return (
        {
            "inputs": [
                {
                    "name": input_name,
                    "columns": [
                        {"name": column.name, "type": column.talend_type, **({"nullable": column.nullable} if column.nullable is not None else {})}
                        for column in source_step.schema_columns
                    ],
                }
            ],
            "outputs": [{"name": output_name, "columns": output_columns}],
        },
        output_schema,
        None,
    )


def _safe_folder_path(folder_path: str) -> str:
    normalized = folder_path.replace("\\", "/").strip("/")
    parts = normalized.split("/") if normalized else []
    if not parts or parts[0].casefold() != "process":
        raise ValueError("La carpeta Talend debe estar dentro de Process/.")
    if any(part in {".", ".."} or not re.fullmatch(r"[\w .-]+", part) for part in parts):
        raise ValueError("La carpeta Talend contiene una ruta no permitida.")
    return "/".join(parts)


def _load_context_file(path: Path) -> dict[str, str]:
    """Read the portal's UTF-8 .cpf format: one contextName=value per line."""
    if path.suffix.casefold() != ".cpf":
        raise ValueError("El archivo de parámetros debe tener extensión .cpf.")
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except FileNotFoundError as e:
        raise ValueError(f"No existe el archivo de parámetros: {path}") from e
    except (OSError, UnicodeError) as e:
        raise ValueError(f"No se pudo leer el archivo .cpf: {e}") from e

    values: dict[str, str] = {}
    for number, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith(("#", "!")):
            continue
        name, separator, value = line.partition("=")
        name, value = name.strip(), value.strip()
        if not separator or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            raise ValueError(f"Línea {number} inválida en .cpf; se esperaba nombre=valor.")
        if not value:
            raise ValueError(f"El parámetro {name} está vacío (línea {number} del .cpf).")
        if name.casefold() in {item.casefold() for item in values}:
            raise ValueError(f"Parámetro duplicado en .cpf: {name}.")
        values[name] = value
    return values


def _apply_context_file(contexts: list[ApplyContext], path: Path | None) -> list[ApplyContext]:
    if path is None:
        return contexts
    values = _load_context_file(path)
    by_name = {item.name.casefold(): item for item in contexts}
    for name, value in values.items():
        existing = by_name.get(name.casefold())
        if existing:
            existing.value = value
        else:
            context = ApplyContext(name=name, value=value, comment="Parámetro proporcionado por archivo .cpf.")
            contexts.append(context)
            by_name[name.casefold()] = context
    return contexts


def _instruction_step(
    step: PlanStep,
    *,
    talend_unique_name: str | None = None,
    configured_mapper: bool = False,
) -> dict[str, Any]:
    """Describe the SAS step without copying legacy user progress or notes."""
    result = {
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
        "componentTables": step.component_tables,
        "dependencies": [
            {"type": item.type, "fromStep": item.from_step, "label": item.label}
            for item in step.connections
        ],
        "assumptions": step.assumptions,
        "pending": [
            item for item in step.pending
            if not (configured_mapper and item == "Tipos de las columnas calculadas")
        ],
        "tests": step.tests,
        "evidence": step.evidence.model_dump(mode="json"),
        "confidence": step.confidence,
        "verified": step.verified,
        "mapperConfigured": configured_mapper,
        "offlineConfigured": step.offline_configured,
        "inCatalog": step.in_catalog,
        "docUrl": step.doc_url,
        "variants": step.variants,
        "requiresSemanticValidation": step.requires_semantic_validation and not configured_mapper,
    }
    if configured_mapper:
        for expression in result["expressions"]:
            expression["requires_semantic_validation"] = False
    if talend_unique_name:
        result["talendUniqueName"] = talend_unique_name
    return result


def _json_model(value: Any) -> Any:
    return value.model_dump(mode="json") if isinstance(value, BaseModel) else value


def _pending_details(
    plan: JobPlan,
    resolved_program_steps: set[str] | None = None,
    configured_mapper_steps: set[str] | None = None,
) -> list[str]:
    steps = [*plan.steps, *(step for child in plan.children for step in child.steps)]
    source_macro = PurePosixPath(plan.program.replace("\\", "/")).stem.casefold()
    resolved_steps = resolved_program_steps or set()
    mapped_steps = configured_mapper_steps or set()
    details: list[str] = []
    for step in steps:
        configured_mapper = step.id in mapped_steps
        if step.operation_type == "macro_call":
            called_macro = (_step_property_value(step, "PROCESS") or "").strip().strip("\"'").lstrip("%").casefold()
            if called_macro == source_macro or step.id in resolved_steps:
                continue
        location = f"{step.evidence.file}:{step.evidence.line}"
        block_reason = _step_block_reason(step)
        if block_reason:
            details.append(f"Paso {step.operation_id or step.id} ({location}): {block_reason}")
        if step.requires_semantic_validation:
            details.append(
                f"Paso {step.operation_id or step.id} ({location}): la equivalencia semántica SAS/Talend sigue pendiente de validación."
            )
        if (not step.verified or step.confidence != "high") and not step.offline_configured and not configured_mapper:
            details.append(
                f"Paso {step.operation_id or step.id} ({location}): componente o configuración pendiente de validación; completar en Talend."
            )
        for pending in step.pending:
            if configured_mapper and pending == "Tipos de las columnas calculadas":
                continue
            details.append(f"Paso {step.operation_id or step.id} ({location}): {pending}")
        for prop in step.properties:
            if configured_mapper and prop.name in {"Expressions", "Var table"}:
                continue
            if (not prop.verified or prop.value is None) and not (
                step.offline_configured and prop.value is not None
            ):
                details.append(
                    f"Paso {step.operation_id or step.id} ({location}): propiedad {prop.name} "
                    f"sin valor verificado; origen indicado por el portal: {prop.origin}."
                )
        for expression in step.expressions:
            if configured_mapper:
                continue
            if (
                expression.talend is None or expression.requires_semantic_validation
            ) and not step.offline_configured:
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
    configured_mapper_steps: set[str] | None = None,
) -> list[ApplyContext]:
    groups: dict[str, list[str]] = {}
    for detail in _pending_details(plan, resolved_program_steps, configured_mapper_steps):
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
    plan: JobPlan,
    folder_path: str,
    blocked_steps: list[ApplyBlock],
    pending: list[str],
    talend_unique_names: dict[str, str] | None = None,
    configured_mapper_steps: set[str] | None = None,
) -> dict[str, Any]:
    all_steps = [*plan.steps, *(step for child in plan.children for step in child.steps)]
    component_names = talend_unique_names or {}
    mapped_steps = configured_mapper_steps or set()
    assumptions = list(dict.fromkeys(assumption for step in all_steps for assumption in step.assumptions))
    return {
        "source": {
            "projectId": plan.project_id,
            "program": plan.program,
            "sha256": plan.sha256,
            "rulesVersion": plan.rules_version,
        },
        "job": {"name": plan.job_name, "folderPath": folder_path},
        "offlineConfiguration": {
            "configuredFromProjectFiles": any(step.offline_configured for step in all_steps),
            "verification": "pending-in-talend-studio",
            "note": "Las rutas, esquemas y filtros simples se infieren de los archivos del proyecto; verificar y ejecutar el Job en Studio antes de usarlo con datos reales.",
        },
        "entryMacro": _json_model(plan.entry_macro) if plan.entry_macro else None,
        "steps": [
            _instruction_step(
                step,
                talend_unique_name=component_names.get(step.id),
                configured_mapper=step.id in mapped_steps,
            )
            for step in sorted(plan.steps, key=lambda item: (item.order, item.id))
        ],
        "macros": [
            {
                "name": child.name,
                "parameters": child.params,
                "steps": [
                    _instruction_step(
                        step,
                        talend_unique_name=component_names.get(step.id),
                        configured_mapper=step.id in mapped_steps,
                    )
                    for step in sorted(child.steps, key=lambda item: (item.order, item.id))
                ],
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


_SUBJOB_START = re.compile(r"Input|RowGenerator")

#: Componentes de trabajo por Job hijo al partir un Job grande; con el manejo de errores quedan en 20,
#: el máximo que recomienda la guía de buenas prácticas de Talend.
CHUNK_SIZE = 17


def split_oversized_job(
    job_name: str,
    folder_path: str,
    components: list[ApplyComponent],
    connections: list[ApplyConnection],
    instructions: dict[str, Any],
    *,
    chunk_size: int = CHUNK_SIZE,
    error_handling: bool = False,
) -> tuple[list[ApplyComponent], list[ApplyConnection], dict[str, Any], list[dict[str, Any]]]:
    """Parte un Job demasiado grande en Jobs hijo y deja al padre como una cadena de `tRunJob`.

    Los componentes se agrupan por conexión (un flujo nunca se corta entre dos Jobs) y los grupos
    se empaquetan, en orden, en hijos de hasta `chunk_size` componentes; un grupo mayor ocupa un
    hijo propio. Cada hijo se redistribuye en el lienzo y se lleva sus instrucciones.

    Returns:
        Componentes, conexiones e instrucciones del padre, y los argumentos de cada hijo.
    """
    root = {item.unique_name: item.unique_name for item in components}

    def find(name: str) -> str:
        while root[name] != name:
            root[name] = root[root[name]]
            name = root[name]
        return name

    for edge in connections:
        if edge.source in root and edge.target in root:
            root[find(edge.source)] = find(edge.target)
    groups: dict[str, list[ApplyComponent]] = {}
    for item in components:
        groups.setdefault(find(item.unique_name), []).append(item)

    chunks: list[list[list[ApplyComponent]]] = []
    current: list[list[ApplyComponent]] = []
    size = 0
    for group in groups.values():
        if current and size + len(group) > chunk_size:
            chunks.append(current)
            current, size = [], 0
        current.append(group)
        size += len(group)
    if current:
        chunks.append(current)

    all_steps = list(instructions.get("steps") or [])
    for macro in instructions.get("macros") or []:
        all_steps.extend(macro.get("steps") or [])
    children: list[dict[str, Any]] = []
    parent_components: list[ApplyComponent] = []
    parent_connections: list[ApplyConnection] = []
    moved: set[str] = set()
    for number, chunk in enumerate(chunks, 1):
        child_name = f"{job_name}_p{number:02d}"
        child_components: list[ApplyComponent] = []
        for row, group in enumerate(chunk):
            for column, item in enumerate(group):
                child_components.append(
                    item.model_copy(update={"pos_x": 160 + 280 * column, "pos_y": 96 + 192 * row})
                )
        names = {item.unique_name for item in child_components}
        child_connections = [edge for edge in connections if edge.source in names]
        if error_handling:
            _add_error_handling(child_name, child_components, child_connections)
        moved |= names
        children.append(
            {
                "jobName": child_name,
                "version": "0.1",
                "defaultContext": "Default",
                "folderPath": folder_path,
                "description": f"Parte {number} de {len(chunks)} de {job_name}",
                "purpose": "Parte de un Job dividido por tamaño",
                "components": [item.model_dump(by_alias=True, exclude_none=True) for item in child_components],
                "connections": [edge.model_dump(by_alias=True) for edge in child_connections],
                "contexts": [],
                "replaceManagedTodoContexts": False,
                "childJobs": [],
                "instructions": {
                    "source": instructions.get("source"),
                    "job": {"name": child_name, "folderPath": folder_path},
                    "parentJob": job_name,
                    "steps": [step for step in all_steps if step.get("talendUniqueName") in names],
                    "macros": [],
                },
            }
        )
        index = number - 1
        parent_components.append(
            ApplyComponent(
                uniqueName=f"tRunJob_{number}", componentName="tRunJob",
                posX=160 + 280 * (index % 6), posY=96 + 192 * (index // 6),
                label=f"Ejecutar {child_name}", parameters={"PROCESS": child_name},
            )
        )
        if number > 1:
            parent_connections.append(
                ApplyConnection(
                    source=f"tRunJob_{number - 1}", target=f"tRunJob_{number}", label=f"on_ok_{number}",
                    connectorName="SUBJOB_OK", uniqueName=f"subjob_ok_{number}",
                )
            )

    parent_instructions = dict(instructions)
    parent_instructions["steps"] = [
        step for step in instructions.get("steps") or [] if step.get("talendUniqueName") not in moved
    ]
    parent_instructions["macros"] = [
        {**macro, "steps": [step for step in macro.get("steps") or [] if step.get("talendUniqueName") not in moved]}
        for macro in instructions.get("macros") or []
    ]
    parent_instructions["split"] = {
        "reason": f"El Job tenía {len(components)} componentes; se parte en Jobs hijo de hasta {chunk_size}.",
        "chunkSize": chunk_size,
        "children": [
            {"jobName": child["jobName"], "components": len(child["components"])} for child in children
        ],
    }
    return parent_components, parent_connections, parent_instructions, children


def _add_error_handling(
    job_name: str, components: list[ApplyComponent], connections: list[ApplyConnection]
) -> None:
    """Añade el manejo de errores básico: registro de fallos y, si se puede, corte del Job.

    `tLogCatcher` registra en un subjob aparte cualquier error o `tDie` del Job. El corte con
    `tDie` por `SUBJOB_ERROR` solo es válido desde un componente que inicia un subjob (una
    entrada sin flujo entrante); Studio rechaza ese enlace desde un `tMap` o un filtro. Si el
    Job no tiene un inicio así (por ejemplo, la lectura aún está por determinar), solo se
    añade el registro. Van en filas propias, bajo el flujo.
    """
    receiving = {item.target for item in connections}
    start = next(
        (
            item
            for item in sorted(components, key=lambda candidate: candidate.pos_x)
            if item.unique_name not in receiving and _SUBJOB_START.search(item.component_name)
        ),
        None,
    )
    catcher_y = max(item.pos_y for item in components) + 192
    count = len(components)
    catcher = f"tLogCatcher_{count + 1}"
    log_row = f"tLogRow_{count + 2}"
    components.extend(
        [
            ApplyComponent(
                uniqueName=catcher, componentName="tLogCatcher", posX=160, posY=catcher_y,
                label="Capturar errores del Job", parameters={},
            ),
            ApplyComponent(
                uniqueName=log_row, componentName="tLogRow", posX=440, posY=catcher_y,
                label="Registrar errores", parameters={},
            ),
        ]
    )
    connections.append(
        ApplyConnection(
            source=catcher, target=log_row, label="row_errors", connectorName="FLOW", uniqueName="flow_errors"
        )
    )
    if start is None:
        return
    die = f"tDie_{count + 3}"
    components.append(
        ApplyComponent(
            uniqueName=die, componentName="tDie", posX=160, posY=catcher_y + 192,
            label="Detener el Job ante un fallo",
            parameters={"MESSAGE": f'"Fallo en el Job {job_name}"'},
        )
    )
    connections.append(
        ApplyConnection(
            source=start.unique_name, target=die, label="on_error",
            connectorName="SUBJOB_ERROR", uniqueName="subjob_error_1",
        )
    )


def build_apply_spec(
    plan: JobPlan,
    folder_path: str = "Process",
    *,
    context_file: Path | None = None,
    related_plans: list[JobPlan] | None = None,
    related_folder_paths: dict[str, str] | None = None,
    error_handling: bool = False,
    max_components: int | None = None,
    _visited_programs: set[str] | None = None,
) -> TalendApplySpec:
    """Build a deterministic spec without filling missing SAS details with sample values."""
    safe_folder = _safe_folder_path(folder_path)
    eligible: dict[str, PlanStep] = {}
    draft_steps: dict[str, tuple[PlanStep, str]] = {}
    candidate_steps: dict[str, PlanStep] = {}
    configured_mappers: dict[str, dict[str, Any]] = {}
    configured_mapper_schemas: dict[str, list[ApplySchemaColumn]] = {}

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
        mapper_candidate = step.component_candidate == "tMap" and step.operation_type in {
            "join", "project", "compute", "rename"
        }
        mapper = None
        mapped_schema = None
        mapper_reason = None
        if mapper_candidate:
            mapper, mapped_schema, mapper_reason = _build_tmap_mapper(step, candidate_steps)
            if mapper is not None and mapped_schema is not None:
                configured_mappers[step.id] = mapper
                configured_mapper_schemas[step.id] = mapped_schema
        configured_mapper = step.id in configured_mappers
        mapper_pending = mapper_candidate and not configured_mapper
        step_properties_pending = any(
            (not prop.verified or prop.value is None)
            and not (configured_mapper and prop.name in {"Expressions", "Var table"})
            for prop in step.properties
        )
        step_expressions_pending = any(
            (expression.talend is None or expression.requires_semantic_validation)
            and not configured_mapper
            for expression in step.expressions
        )
        needs_draft = (
            step.requires_semantic_validation
            or bool([item for item in step.pending if not (configured_mapper and item == "Tipos de las columnas calculadas")])
            or mapper_pending
            or step.action == "manual_decision"
            or (not configured_mapper and not step.offline_configured and (not step.verified or step.confidence != "high"))
            or (not step.offline_configured and step_properties_pending)
            or (not step.offline_configured and step_expressions_pending)
            or any(
                not column.name or not column.type
                for column in (mapped_schema or [])
            )
            or (
                mapped_schema is None
                and any(not column.name or not column.talend_type for column in step.schema_columns)
            )
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
            if step.requires_semantic_validation:
                pending.append("La equivalencia semántica SAS/Talend sigue pendiente de validación.")
            if mapper_pending:
                pending.append(mapper_reason or "El plan propone tMap, pero su mapper no se pudo configurar automáticamente.")
            if step_properties_pending:
                pending.append("Hay propiedades sin valor confirmado; se conservarán en el contexto del Job.")
            if step_expressions_pending:
                pending.append("Hay expresiones SAS pendientes de traducción o validación semántica.")
            schema_pending = (
                any(not column.name or not column.type for column in mapped_schema)
                if mapped_schema is not None
                else any(not column.name or not column.talend_type for column in step.schema_columns)
            )
            if schema_pending:
                pending.append("Faltan nombres o tipos Talend para completar el esquema.")
            if not configured_mapper and (step.confidence != "high" or not step.verified):
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
        columns = configured_mapper_schemas.get(step.id) or [
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
            if (prop.verified or step.offline_configured)
            and prop.value is not None
            and not (prop.name == "CONDITIONS" and "CONDITIONS" in step.component_tables)
        }
        if step.component_tables:
            component_tables[step.id] = dict(step.component_tables)
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
                label=_component_label(step.purpose, operation_identity, step.order),
                parameters=verified_parameters,
                tables=component_tables.get(step.id),
                schema_=schema,
                mapper=configured_mappers.get(step.id),
                draftOnly=is_draft,
                draftReason=draft_reason,
            )
        )
        for edge_index, edge in enumerate(step.connections, 1):
            if edge.from_step not in unique_names or edge.type not in _CONNECTORS:
                continue
            source_step = candidate_steps.get(edge.from_step)
            connector = (
                "FILTER"
                if edge.type == "Main"
                and source_step is not None
                and source_step.component_candidate.casefold() == "tfilterrow"
                else _CONNECTORS[edge.type]
            )
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
            error_handling=error_handling,
            max_components=max_components,
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
    configured_mapper_steps = set(configured_mappers)
    pending_contexts = _pending_contexts(
        plan, context_names, set(resolved_children_by_step), configured_mapper_steps
    )
    contexts.extend(pending_contexts)
    contexts = _apply_context_file(contexts, context_file)
    pending_details = [context.comment for context in pending_contexts]
    if not components and not contexts:
        contexts.append(
            ApplyContext(
                name="migration_source_program",
                value=plan.program,
                comment="Programa SAS de origen incluido en esta guía.",
            )
        )

    instructions = _portal_instructions(
        plan,
        safe_folder,
        blocked_steps,
        pending_details,
        talend_unique_names=unique_names,
        configured_mapper_steps=configured_mapper_steps,
    )
    include_error_handling = error_handling
    error_component_count = 3 if include_error_handling and components else 0
    can_split = max_components is None or max_components >= 5 or not error_handling
    if (
        max_components is not None
        and can_split
        and len(components) + error_component_count > max_components
    ):
        components, connections, instructions, split_children = split_oversized_job(
            plan.job_name,
            safe_folder,
            components,
            connections,
            instructions,
            chunk_size=min(CHUNK_SIZE, max(1, max_components - error_component_count)),
            error_handling=include_error_handling,
        )
        child_jobs.extend(split_children)
    if include_error_handling and components:
        _add_error_handling(plan.job_name, components, connections)

    return TalendApplySpec(
        project_id=plan.project_id,
        program=plan.program,
        source_sha256=plan.sha256,
        rules_version=plan.rules_version,
        job_name=plan.job_name,
        description=plan.description,
        folder_path=safe_folder,
        components=components,
        connections=connections,
        contexts=contexts,
        child_jobs=child_jobs,
        blocked_steps=blocked_steps,
        instructions=instructions,
    )
