"""Contrato del plan de migración (JSON versionado). No es un formato de Talend."""

from typing import Literal

from pydantic import BaseModel

from sas_grid_migrator.domain.models import SCHEMA_VERSION
from sas_grid_migrator.sas_parser.ast import Loc

StepStatus = Literal["propuesto", "pendiente", "verificado", "validado_manualmente", "descartado"]
# Estado de la guía (trabajo del desarrollador). Sustituye al texto legado `[Estado de guía: ...]` de `note`.
GuideStatus = Literal["pending", "in_progress", "completed", "blocked"]


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
    type: Literal[
        "Main", "Lookup", "Reject", "OnSubjobOk", "OnComponentOk", "OnComponentError", "Iterate"
    ]
    from_step: str | None = None
    label: str | None = None


class Expression(BaseModel):
    sas: str
    talend: str | None = None
    talend_edited: bool = False
    target: str | None = None
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
    component_tables: dict[str, object] = {}
    offline_configured: bool = False
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
    # Paso recomendado por el portal (buenas prácticas), no traducido desde SAS.
    recommended: bool = False
    why: str | None = None  # por qué se recomienda, en español
    job_part: str | None = None  # Job que contiene el paso (padre o hijo de partición)
    business_subjob: str | None = None  # título de negocio (etiqueta del SAS) del subjob
    library: str | None = None  # biblioteca SAS del dataset (LIB de LIB.TABLA), para detectar Built-In repetidos
    guide_status: GuideStatus = "pending"
    field_done: dict[str, bool] = {}
    joblet_id: str | None = None  # joblet que agrupa este paso (repetido en el programa), si lo hay
    # Operaciones SAS fundidas en este paso (un tMap que reúne filtro, cálculos y renombres).
    # Vacío si el paso traduce una sola operación; `operation_id` es la primera de la lista.
    fused_from: list[str] = []


class ValidationCase(BaseModel):
    id: str
    kind: str  # row_count | schema | nulls | duplicates | numeric | dates | ordering | aggregates | empty
    description: str
    applies_to: list[str]  # ids de pasos
    expected: str = "Resultado igual al de SAS"


class ContextVariable(BaseModel):
    name: str
    sas_value: str | None = None  # nunca contiene el valor de un secreto
    suggested: str
    origin: str
    talend_type: str = "id_String"  # id_String | id_Integer | id_Boolean | id_Date | id_Password
    is_secret: bool = False
    needs_value: bool = False  # placeholder sin resolver, vacío o secreto: el valor lo aporta el entorno
    sas_line: int | None = None  # línea del %LET o del primer uso en el SAS
    # Valor por ambiente {DEV, QA, PROD}; None = desconocido. Solo cuando el programa cambia la variable según el ambiente.
    group_values: dict[str, str | None] | None = None


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


class JobPart(BaseModel):
    """Job hijo en que se reparte el plan cuando supera MAX_COMPONENTS_PER_JOB."""

    name: str
    title: str  # título de negocio legible (etiquetas del SAS)
    of: str  # Job que se reparte: el programa principal o un hijo (macro)
    step_ids: list[str] = []
    component_count: int = 0  # pasos del Job, recomendados incluidos


class JobletOccurrence(BaseModel):
    """Una aparición del bloque repetido: en qué Job y qué pasos del plan lo forman."""

    job: str  # Job donde aparece (programa, parte o Job hijo de macro)
    label: str  # origen legible: "macro %nombre" o "pasos s12–s30"
    step_ids: list[str] = []
    values: dict[str, str] = {}  # valor concreto de cada parámetro en esta aparición
    usage_steps: list[str] = []  # cómo usar el joblet en este Job, en español


class JobletParameter(BaseModel):
    name: str  # nombre del parámetro (y de la variable de contexto sin el prefijo)
    context_variable: str  # p. ej. "context.tabla_entrada_1"
    example_values: list[str] = []  # valores distintos vistos (máximo 5)


class JobletPlan(BaseModel):
    """Joblet propuesto: bloque repetido que se crea una vez y se usa en cada aparición."""

    id: str  # estable dentro del plan: "joblet-01", "joblet-02"…
    name: str  # nombre en Talend: "jl_<Rol>"
    title: str
    kind: Literal["macro", "sequence", "feed"] = "sequence"
    occurrences: list[JobletOccurrence] = []
    parameters: list[JobletParameter] = []
    components: list[str] = []  # component_candidate de cada paso del bloque, en orden
    inputs: list[str] = []  # nombres de los Input (tablas de entrada)
    outputs: list[str] = []  # nombres de los Output (tablas de salida)
    trigger_inputs: list[str] = []  # Trigger Input (inicio del joblet)
    why: str  # por qué se propone, en español
    creation_steps: list[str] = []  # pasos en Studio para crear el joblet
    operation_count: int = 0  # operaciones por aparición


class RunJobCall(BaseModel):
    job: str
    order: int
    title: str
    transmit_context: bool = True  # tRunJob con transmisión de todo el contexto


class OrchestratorJob(BaseModel):
    """Job padre con una cadena de tRunJob que llama a las partes y a las macros."""

    name: str
    run_jobs: list[RunJobCall] = []


class MacroEntrypoint(BaseModel):
    """Macro principal invocada por el programa; su cuerpo pertenece al Job del archivo."""

    name: str
    params: list[str] = []
    arguments: dict[str, str] = {}


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


class NotMigrated(BaseModel):
    """Fontanería de SAS que no genera pasos: por qué no hace falta y qué hace Talend en su lugar."""

    category: str  # shell_auxiliar | espera | mensajes | medicion | conteo | limpieza_tablas | ...
    lines: list[int] = []  # líneas SAS donde aparece
    what: str  # qué es, en español
    reason: str  # por qué no hace falta migrarlo
    talend_equivalent: str  # qué hace Talend en su lugar


class JobPlan(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    rules_version: str
    program: str
    sha256: str | None = None
    job_name: str
    description: str | None = None
    job_name_edited: bool = False
    rename_ignored: str | None = None
    job_status: Literal["proposed", "needs_review"] = "needs_review"
    steps: list[PlanStep] = []
    entry_macro: MacroEntrypoint | None = None
    children: list[ChildJob] = []
    validation_cases: list[ValidationCase] = []
    context_variables: list[ContextVariable] = []
    libraries_needed: list[LibraryNeeded] = []
    orchestration: Orchestration = Orchestration()
    unresolved: list[str] = []
    job_parts: list[JobPart] = []  # vacío: el programa cabe en un Job
    orchestrator: OrchestratorJob | None = None  # solo con partes o varias macros
    joblets: list[JobletPlan] = []  # bloques repetidos que conviene convertir en joblet
    not_migrated: list[NotMigrated] = []  # fontanería de SAS detectada y no traducida


class PlanSet(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    rules_version: str
    plans: list[JobPlan]
    grid_recommendations: list[GridRecommendation] = []
