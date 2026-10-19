"""Contrato del plan de migración (JSON versionado). No es un formato de Talend."""

from typing import Literal

from pydantic import BaseModel

from sas_grid_migrator.domain.models import SCHEMA_VERSION
from sas_grid_migrator.sas_parser.ast import Loc

StepStatus = Literal["propuesto", "pendiente", "verificado", "validado_manualmente", "descartado"]


class Property(BaseModel):
    name: str  # nombre candidato; solo es exacto si verified
    value: str | None = None
    origin: str  # "SAS archivo:línea" | "regla mappings" | "usuario"
    verified: bool = False
    in_catalog: bool | None = None  # nombre existe en el catálogo oficial (None: no aplica/editor)
    label: str | None = None  # etiqueta del parámetro en Talend Studio
    options: list[str] = []  # valores admitidos si es una lista cerrada


class SchemaColumn(BaseModel):
    name: str
    talend_type: str | None = None
    nullable: bool | None = None
    length: int | None = None
    precision: int | None = None
    origin: str = ""


class Connection(BaseModel):
    type: Literal["Main", "Lookup", "Reject", "OnSubjobOk", "OnComponentOk", "Iterate"]
    from_step: str | None = None
    label: str | None = None


class Expression(BaseModel):
    sas: str
    talend: str | None = None
    line: int
    requires_semantic_validation: bool = True
    warnings: list[str] = []


class PlanStep(BaseModel):
    id: str
    order: int
    subjob: str
    action: str  # add_component | configure | manual_decision | define_context
    operation_id: str | None = None
    operation_type: str | None = None
    component_candidate: str = "por_determinar"
    alternatives: list[str] = []
    purpose: str
    properties: list[Property] = []
    schema_columns: list[SchemaColumn] = []
    connections: list[Connection] = []
    expressions: list[Expression] = []
    assumptions: list[str] = []
    pending: list[str] = []
    tests: list[str] = []  # ids de ValidationCase
    evidence: Loc
    confidence: Literal["high", "medium", "low"] = "high"
    status: StepStatus = "propuesto"
    note: str | None = None  # decisión humana
    verified: bool = False  # componente y propiedades contrastados con talend-mcp
    in_catalog: bool | None = None  # el componente existe en el catálogo oficial de Talend
    doc_url: str | None = None
    variants: list[str] = []  # componentes hermanos (otra tecnología)
    requires_semantic_validation: bool = False


class ValidationCase(BaseModel):
    id: str
    kind: str  # row_count | schema | nulls | duplicates | numeric | dates | ordering | aggregates | empty
    description: str
    applies_to: list[str]  # ids de pasos
    expected: str = "Resultado igual al de SAS"


class ContextVariable(BaseModel):
    name: str
    sas_value: str | None = None
    suggested: str
    origin: str


class LibraryNeeded(BaseModel):
    sas_name: str
    engine: str | None = None
    path: str | None = None
    suggested_connection: str  # componente de conexión / metadato a crear
    note: str = "Crear la conexión en Talend; no se copian credenciales"


class ChildJob(BaseModel):
    name: str  # macro
    params: list[str]
    steps: list[PlanStep]


class GridRecommendation(BaseModel):
    id: str
    pattern_id: str
    catalog_version: str
    status: Literal["supported", "partial", "unsupported"]
    instruction: str
    reason: str
    component_candidate: str | None = None
    doc_url: str | None = None
    required: list[str] = []
    dependencies: list[str] = []
    target_program: str | None = None
    evidence: Loc
    details: dict[str, object] = {}


class Orchestration(BaseModel):
    grid_tasks: list[str] = []
    grid_recommendations: list[GridRecommendation] = []
    schedules: list[str] = []
    upstream: list[str] = []  # programas de los que depende por datos
    downstream: list[str] = []


class JobPlan(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    rules_version: str
    program: str
    sha256: str | None = None
    job_name: str
    job_status: Literal["proposed", "needs_review"] = "needs_review"
    steps: list[PlanStep] = []
    children: list[ChildJob] = []
    validation_cases: list[ValidationCase] = []
    context_variables: list[ContextVariable] = []
    libraries_needed: list[LibraryNeeded] = []
    orchestration: Orchestration = Orchestration()
    unresolved: list[str] = []


class PlanSet(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    rules_version: str
    plans: list[JobPlan]
    grid_recommendations: list[GridRecommendation] = []
