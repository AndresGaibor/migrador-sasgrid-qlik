export type ProjectProcessingStatus = "queued" | "running" | "completed" | "failed" | "interrupted";
export type ProjectProcessing = {
  status: ProjectProcessingStatus;
  stage: string;
  started_at: string | null;
  stage_started_at: string | null;
  updated_at: string;
  message: string | null;
  error: string | null;
  retry_count: number;
};
export type Project = {
  id: string;
  name: string;
  created_at: string;
  archive_name?: string | null;
  archive_sha256?: string | null;
  archive_size_bytes?: number | null;
  uploaded_at?: string | null;
  manifest_summary?: { files: number; programs: number; folders: number; skipped: number } | null;
  processing?: ProjectProcessing | null;
};
export type ProjectUploadResponse = { project: Project; processing: ProjectProcessing };
export type SourceFile = { path: string; sha256: string; size: number; kind: string; encoding: string | null };
export type Manifest = { files: SourceFile[]; skipped: { path: string; reason: string }[] };
export type Coverage = { tag: string; priority: string; count: number };
export type Summary = {
  programs: number;
  statements: number;
  unrecognized: number;
  macro_fragments: number;
  findings_by_priority: Record<string, number>;
  coverage: Coverage[];
};
export type ProgramRow = { file: string; statements: number; findings: number };
export type Finding = {
  code: string;
  severity: string;
  message: string;
  priority: "P0" | "P1" | "P2" | null;
  evidence: { file: string; line: number };
};
export type Program = { file: string; findings: Finding[]; stats: { statements: number; unrecognized: number }; nodes?: import("./guided").SourceNode[] };
export type DatasetInfo = { id: string; role: string; producers: string[]; consumers: string[] };
export type DataEdge = { source: string; target: string; datasets: string[]; kind: string };
export type GridTask = {
  id: string;
  kind: string;
  source_file: string;
  line: number;
  resolved_program: string | null;
  match_status: string | null;
  queue: string | null;
  waits: boolean;
  after: string[];
  unknown_options: string[];
  incomplete_options: string[];
};
export type GridRecommendation = {
  id: string;
  pattern_id: string;
  catalog_version: string;
  status: "supported" | "partial" | "unsupported";
  instruction: string;
  reason: string;
  component_candidate: string | null;
  doc_url: string | null;
  required: string[];
  dependencies: string[];
  target_program: string | null;
  evidence: { file: string; line: number; end_line: number };
  details: Record<string, unknown>;
};
export type Deps = {
  datasets: DatasetInfo[];
  edges: DataEdge[];
  processing_order: string[][];
  cycles: string[][];
  unresolved: { kind: string; name: string; file: string; line: number; detail: string }[];
  orchestration: { tasks: GridTask[]; schedules: { file: string; line: number; text: string }[]; order: string[] };
};
export type PlanRow = { program: string; job_name: string; description?: string | null; job_status: string; steps: number; pending: number; done: number; studio_verified?: number; studio_pending?: number; studio_status?: "not_checked" | "verified" | "pending" | "unavailable" };
export type ProjectProgress = {
  stages: { key: string; label: string; status: "done" | "current" | "todo" | "blocked"; detail: string; tab: string }[];
  next: { key: string; label: string; tab: string } | null;
};
export type PendingSummary = {
  reason: string;
  steps: number;
  programs: { program: string; job_name: string; step_ids: string[] }[];
};
export type TalendStepVerification = {
  status: "verified" | "pending" | "unavailable";
  reason: string | null;
  checked_at?: string;
  talend_unique_name: string | null;
  studio_unique_name?: string | null;
  checks: Record<string, { status: "verified" | "pending" | "unavailable" | "not_required"; reason?: string | null; expected?: unknown; actual?: unknown }>;
};
export type Step = {
  id: string;
  order: number;
  subjob: string;
  action: string;
  component_candidate: string;
  alternatives: string[];
  purpose: string;
  properties: { name: string; value: string | null; origin: string; verified: boolean; in_catalog?: boolean | null; label?: string | null; options?: string[] }[];
  connections: { type: string; from_step: string | null }[];
  operation_id?: string | null;
  operation_type?: string | null;
  schema_columns?: { name: string; talend_type: string | null }[];
  expressions: { sas: string; talend: string | null; talend_edited?: boolean; line: number; warnings: string[] }[];
  assumptions: string[];
  pending: string[];
  tests: string[];
  status: string;
  note: string | null;
  evidence: { file: string; line: number };
  confidence: string;
  verified: boolean;
  in_catalog?: boolean | null;
  doc_url?: string | null;
  variants?: string[];
  requires_semantic_validation?: boolean;
  studio_verification?: TalendStepVerification;
  /** Paso de buena práctica que no viene del SAS (conexión compartida, manejo de errores…). */
  recommended?: boolean;
  /** Por qué se hace así, en español. */
  why?: string | null;
  job_part?: string | null;
  business_subjob?: string | null;
  guide_status?: "pending" | "in_progress" | "completed" | "blocked";
  /** Campos del panel de Studio que el usuario ya dejó configurados. */
  field_done?: Record<string, boolean>;
  /** Operaciones SAS que este paso absorbe (p. ej. varias en un solo tMap). */
  fused_from?: string[];
  joblet_id?: string | null;
};
export type JobPart = { name: string; title: string; of: string; step_ids: string[]; component_count: number };
/** Fontanería de SAS detectada y no traducida (troceado, esperas, conteos…). */
export type NotMigrated = {
  category: string;
  lines: number[];
  what: string;
  reason: string;
  talend_equivalent: string;
};
/** Una aparición de un bloque repetido: en qué Job y qué pasos lo forman. */
export type JobletOccurrence = {
  job: string;
  label: string;
  step_ids: string[];
  /** Valor concreto de cada parámetro en esta aparición (clave: nombre del parámetro). */
  values: Record<string, string>;
  usage_steps: string[];
};
export type JobletParameter = { name: string; context_variable: string; example_values: string[] };
/** Joblet propuesto: bloque repetido que se crea una vez en Studio y se reutiliza. */
export type JobletPlan = {
  id: string;
  name: string;
  title: string;
  kind: "macro" | "sequence";
  occurrences: JobletOccurrence[];
  parameters: JobletParameter[];
  components: string[];
  inputs: string[];
  outputs: string[];
  trigger_inputs: string[];
  why: string;
  creation_steps: string[];
  operation_count: number;
};
export type JobPlan = {
  program: string;
  job_name: string;
  description?: string | null;
  job_name_edited?: boolean;
  rename_ignored?: string | null;
  steps: Step[];
  /** Reparto del Job en partes de tamaño razonable (máx. ~25 componentes). */
  job_parts?: JobPart[];
  entry_macro?: { name: string; params: string[]; arguments: Record<string, string> } | null;
  children: { name: string; params: string[]; steps: Step[] }[];
  validation_cases: { id: string; kind: string; description: string }[];
  context_variables: { name: string; suggested: string; sas_value: string | null; talend_type?: string; is_secret?: boolean; needs_value?: boolean; sas_line?: number | null; group_values?: Partial<Record<"DEV" | "QA" | "PROD", string | null>> | null }[];
  libraries_needed: { sas_name: string; engine: string | null; path: string | null; suggested_connection: string }[];
  orchestration: { grid_tasks: string[]; grid_recommendations: GridRecommendation[]; schedules: string[]; upstream: string[]; downstream: string[] };
  unresolved: string[];
  /** Bloques repetidos que conviene convertir en joblet. */
  joblets?: JobletPlan[];
  /** Fontanería de SAS que no genera pasos. */
  not_migrated?: NotMigrated[];
};
export type TranslateResult = {
  sas: string;
  talend: string | null;
  columns: string[];
  warnings: string[];
  engine: string;
  supported: boolean;
  talend_engine_enabled: boolean;
};
export type BulkRenameRule = {
  mode: "prefix" | "suffix" | "replace" | "regex";
  text?: string;
  find?: string;
  replace_with?: string;
  programs?: string[];
};
export type RenamePreviewRow = { program: string; current: string; proposed: string; error: string | null };
export type NamingTemplate = {
  template: string;
  default_template: string;
  tokens: string[];
  example_name: string;
};
export type TalendLicenseProfile = { code: string; label: string };
export type CatalogItem = {
  name: string;
  description: string;
  families: string[];
  documentation_status: string;
  lifecycle_status: string;
  frameworks: string[];
  license_profile: TalendLicenseProfile;
  search_terms?: string[];
};
export type TalendApplyVerification = {
  status: "unavailable" | "inspected";
  reason: string | null;
  components_requested: number;
  components_created: number | null;
  missing_components: string[];
  configured_steps?: number;
  pending_steps?: number;
  checked_at?: string;
  steps?: { step_id: string; talend_unique_name: string | null; studio_unique_name?: string | null; program: string; job_name: string; checked_at?: string; status: "verified" | "pending" | "unavailable"; reason: string | null; checks: Record<string, { status: "verified" | "pending" | "unavailable" | "not_required"; reason?: string | null; expected?: unknown; actual?: unknown }> }[];
  jobs?: { job_name: string; folder_path?: string; status: "unavailable" | "inspected"; reason: string | null; steps: TalendApplyVerification["steps"] }[];
  connections?: { status: "verified" | "pending"; expected: number; actual: number; missing: unknown[] };
  studio_problems: { clean: boolean; items: { severity?: string; message?: string }[] } | null;
};
export type TalendApplyResult = {
  status: "applied" | "partially_applied";
  identity: { project_id: string; program: string; source_sha256: string | null; rules_version: string; job_name: string; folder_path: string };
  blocked_steps: { step_id: string; reason: string }[];
  warnings: string[];
  verification?: TalendApplyVerification;
  review_required?: boolean;
  review_warnings?: string[];
  result: { jobName?: string; itemPath?: string; propertiesPath?: string; generatedComponents?: number; reusedComponents?: number; generatedConnections?: number; reusedConnections?: number; totalComponents?: number; generatedContexts?: number; updatedContexts?: number; reusedContexts?: number; removedContexts?: number; reusedExisting?: boolean; bridgeRefreshed?: boolean; bridgeOpened?: boolean; problems?: unknown };
};
export type TalendApplyPreview = {
  ready: boolean;
  preview_id: string;
  identity: {
    project_id: string;
    program: string;
    source_sha256: string | null;
    rules_version: string;
    job_name: string;
    folder_path: string;
  };
  components?: { name: string; component: string }[];
  child_jobs?: { jobName: string | null; folderPath: string | null; components: number; connections: number }[];
  connections?: unknown[];
  contexts?: { name: string; type: string; value: string | null; purpose: string }[];
  blocked_steps?: { step_id: string; reason: string }[];
};
export type TalendApplyState = {
  status: "not_started" | "running" | "applied" | "partially_applied" | "failed" | "conflict" | "interrupted";
  revision_hash?: string;
  identity: TalendApplyResult["identity"] | null;
  result: TalendApplyResult | null;
  error: string | null;
  started_at: string | null;
  updated_at: string | null;
};
export type TalendApplyBatchJob = {
  program: string;
  status: "pending" | "running" | "applied" | "partially_applied" | "failed" | "conflict" | "interrupted";
  phase: "applying" | "inspecting" | null;
  result: TalendApplyResult | null;
  error: string | null;
};
export type TalendApplyBatchSummary = {
  project_id: string;
  revision_hash: string;
  destination_root: string;
  total_jobs: number;
  creatable_jobs: number;
  cycles: string[][];
  total_components: number;
  total_connections: number;
  total_contexts: number;
  programs: {
    program: string;
    job_name: string;
    folder_path: string;
    ready_for_creation: boolean;
    creation_kind: "components" | "context_only";
    components: number;
    connections: number;
    contexts: number;
    child_jobs: number;
    blocked_steps: { step_id: string; reason: string }[];
    pending: string[];
    draft_components: { unique_name: string; reason: string }[];
  }[];
};
export type TalendApplyBatchState = {
  project_id: string;
  revision_hash: string | null;
  status: "not_started" | "queued" | "running" | "applied" | "partially_applied" | "failed" | "conflict" | "interrupted";
  programs: string[];
  jobs: TalendApplyBatchJob[];
  current_program: string | null;
  completed_jobs: number;
  total_jobs: number;
  error: string | null;
  warnings: string[];
  attempt_count: number;
  started_at: string | null;
  updated_at: string | null;
};
export type TalendApplyPreflightJob = {
  program: string;
  job_name: string;
  folder_path: string;
  action: "create" | "update" | "conflict";
  existing_path: string | null;
  reason: string | null;
};
export type TalendApplyBatchPreflight = {
  project_id: string;
  revision_hash: string;
  checked_at: string;
  available: boolean;
  inventory_count: number;
  total_jobs: number;
  jobs: TalendApplyPreflightJob[];
  create_count: number;
  update_count: number;
  conflict_count: number;
  studio_memory?: { checked: boolean; used_percent?: number; restart_recommended?: boolean };
};
export type CatalogList = {
  count: number;
  result_count: number;
  has_more: boolean;
  families: Record<string, number>;
  components: CatalogItem[];
  official_component_names: string[];
  official_documentation_inventory: {
    target: string;
    snapshot_version: string;
    source: string;
    license_profile: TalendLicenseProfile;
    count: number;
    documented: number;
    exception: number;
  };
};
export type CatalogParam = {
  name: string;
  label?: string;
  field?: string;
  required?: boolean;
  advanced?: boolean;
  default?: string;
  show_if?: string;
  items?: { name: string; label?: string; value?: string; default?: boolean }[];
  columns?: { name: string; field?: string }[];
};
export type CatalogComponent = CatalogItem & {
  status?: string;
  version?: string;
  doc_url?: string;
  connectors: { type: string; name?: string; max_input?: string; max_output?: string }[];
  parameters: CatalogParam[];
  imports?: { module?: string; mvn?: string; required_if?: string }[];
  variants: string[];
  doc_markdown: string | null;
  official_availability?: {
    source: string;
    snapshot_version: string;
    license_profile: TalendLicenseProfile;
    records: {
      family: string;
      framework_code: string;
      documentation_route: string;
      license_branding_codes: string[];
      license_branding_labels: string[];
    }[];
    frameworks: { code: string; label: string }[];
  } | null;
  official_documentation?: {
    target: string;
    framework_codes: string[];
    lifecycle_status: string;
    status: string;
    issues?: string[];
    routes?: {
      route: string;
      status: string;
      pages: { url: string; title?: string; status: string }[];
    }[];
    configuration_pages: { url: string; title?: string; status: string }[];
    configuration_sections: { url: string; heading: string }[];
  } | null;
};
