import type { BulkRenameRule, CatalogComponent, CatalogList, Deps, GridRecommendation, JobPlan, Manifest, NamingTemplate, PendingSummary, PlanRow, Program, ProgramRow, Project, ProjectProgress, ProjectUploadResponse, RenamePreviewRow, Summary, TalendApplyBatchPreflight, TalendApplyBatchState, TalendApplyBatchSummary, TalendApplyPreview, TalendApplyResult, TalendApplyState, ProjectProcessing, TranslateResult } from "./types";

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

const fetchApi = async (path: string, init?: RequestInit) => {
  try {
    return await fetch(path, init);
  } catch (e) {
    if (e instanceof TypeError) throw new ApiError(0, "No se pudo completar la solicitud. Comprueba tu conexión e inténtalo de nuevo.");
    throw e;
  }
};

async function responseError(response: Response): Promise<ApiError> {
  const body: unknown = await response.json().catch(() => undefined);
  const detail = body && typeof body === "object" && "detail" in body && typeof body.detail === "string"
    ? body.detail
    : "";
  return new ApiError(response.status, detail);
}

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetchApi(`/api${path}`, {
    ...init,
    headers: { "Content-Type": "application/json", ...init?.headers },
  });
  if (!res.ok) throw await responseError(res);
  return res.json() as Promise<T>;
}

const post = <T>(path: string, body?: unknown) =>
  req<T>(path, { method: "POST", body: body === undefined ? undefined : JSON.stringify(body) });
const patch = <T>(path: string, body: unknown) =>
  req<T>(path, { method: "PATCH", body: JSON.stringify(body) });
const enc = (path: string) => path.split("/").map(encodeURIComponent).join("/");

export const api = {
  projects: () => req<Project[]>("/projects"),
  createProject: (name: string) => post<Project>("/projects", { name }),
  deleteProject: (id: string, confirmation: string) =>
    req<{ deleted: boolean; project_id: string; name: string; talend_jobs_untouched: boolean }>(
      `/projects/${id}`,
      { method: "DELETE", body: JSON.stringify({ confirmation }) },
    ),
  createProjectFromZip: async (file: File, name?: string) => {
    const body = new FormData();
    body.append("file", file);
    if (name?.trim()) body.append("name", name.trim());
    const res = await fetchApi("/api/projects/uploads", { method: "POST", body });
    if (!res.ok) throw await responseError(res);
    return (await res.json()) as ProjectUploadResponse;
  },
  importPath: (id: string, path: string) => post<Manifest>(`/projects/${id}/imports`, { path }),
  upload: async (id: string, file: File) => {
    const body = new FormData();
    body.append("file", file);
    const res = await fetchApi(`/api/projects/${id}/uploads`, { method: "POST", body });
    if (!res.ok) throw await responseError(res);
    return (await res.json()) as Manifest;
  },
  inventory: (id: string) => req<Manifest>(`/projects/${id}/inventory`),
  processing: (id: string) => req<ProjectProcessing>(`/projects/${id}/processing`),
  projectProgress: (id: string) => req<ProjectProgress>(`/projects/${id}/progress`),
  pendingSummary: (id: string) => req<PendingSummary[]>(`/projects/${id}/pending-summary`),
  retryProcessing: (id: string) => post<ProjectProcessing>(`/projects/${id}/processing/retry`),
  analyze: (id: string) => post<Summary>(`/projects/${id}/analyses`),
  analysis: (id: string) => req<Summary | null>(`/projects/${id}/analyses`),
  programs: (id: string) => req<ProgramRow[]>(`/projects/${id}/programs`),
  program: (id: string, file: string) => req<Program>(`/projects/${id}/programs/${enc(file)}`),
  sourceEvidence: (id: string, file: string, line: number) =>
    `/api/projects/${id}/source/${file.split("/").map(encodeURIComponent).join("/")}?line=${line}`,
  deps: (id: string) => req<Deps>(`/projects/${id}/dependencies`),
  generatePlans: (id: string) => post<{ plans: number }>(`/projects/${id}/plans`),
  plans: (id: string) => req<PlanRow[]>(`/projects/${id}/plans`),
  gridRecommendations: (id: string) => req<GridRecommendation[]>(`/projects/${id}/plans/grid-recommendations`),
  plan: (id: string, file: string) => req<JobPlan>(`/projects/${id}/plans/${enc(file)}`),
  updateJobMeta: (id: string, file: string, job_name: string | null, description: string | null) =>
    patch<{ plan: JobPlan; warnings: string[] }>(`/projects/${id}/plans/${enc(file)}/meta`, { job_name, description }),
  editExpression: (id: string, file: string, step: string, index: number, talend: string | null) =>
    patch<JobPlan>(`/projects/${id}/plans/${enc(file)}/steps/${encodeURIComponent(step)}/expressions/${index}`, { talend }),
  translate: (sas: string) => post<TranslateResult>("/translator/translate", { sas }),
  renamePreview: (id: string, rule: BulkRenameRule) => post<RenamePreviewRow[]>(`/projects/${id}/plans/rename-preview`, rule),
  renameJobs: (id: string, renames: { program: string; job_name: string }[]) =>
    post<{ renamed: number; warnings: string[] }>(`/projects/${id}/plans/rename`, { renames }),
  namingTemplate: () => req<NamingTemplate>("/settings/naming"),
  namingExample: (template: string) => post<{ name: string }>("/settings/naming/preview", { template }),
  setNamingTemplate: (template: string) =>
    req<NamingTemplate>("/settings/naming", { method: "PUT", body: JSON.stringify({ template }) }),
  decide: (id: string, file: string, step: string, status: string, note: string) =>
    req<JobPlan>(`/projects/${id}/plans/${enc(file)}/steps/${encodeURIComponent(step)}`, {
      method: "PATCH",
      body: JSON.stringify({ status, note }),
    }),
  applyTalend: (id: string, file: string) =>
    post<TalendApplyResult>(`/projects/${id}/plans/${enc(file)}/talend-apply`),
  talendApplyPreview: (id: string, file: string) =>
    post<TalendApplyPreview>(`/projects/${id}/plans/${enc(file)}/talend-apply/preview`),
  talendApplyStatus: (id: string, file: string) =>
    req<TalendApplyState>(`/projects/${id}/plans/${enc(file)}/talend-apply`),
  talendApplyVerify: (id: string, file: string) =>
    post<TalendApplyResult>(`/projects/${id}/plans/${enc(file)}/talend-apply/verify`),
  talendApplyBatch: (id: string, expectedRevision?: string) => post<TalendApplyBatchState>(`/projects/${id}/talend-apply-batch`, expectedRevision ? { expected_revision: expectedRevision } : undefined),
  talendApplyBatchStatus: (id: string) => req<TalendApplyBatchState>(`/projects/${id}/talend-apply-batch`),
  talendApplyBatchPreflight: (id: string) => req<TalendApplyBatchPreflight>(`/projects/${id}/talend-apply-batch/preflight`),
  talendApplyBatchSummary: (id: string) => req<TalendApplyBatchSummary>(`/projects/${id}/talend-apply-batch/summary`),
  exportAll: (id: string) => post<{ directory: string; files: string[] }>(`/projects/${id}/exports`),
  exportFile: (id: string, name: string) => `/api/projects/${id}/exports/${encodeURIComponent(name)}`,
  catalog: (q: string, family: string) =>
    req<CatalogList>(`/talend/catalog?q=${encodeURIComponent(q)}${family ? `&family=${encodeURIComponent(family)}` : ""}`),
  component: (name: string) => req<CatalogComponent>(`/talend/catalog/${encodeURIComponent(name)}`),
  studioConfiguration: () => req<{ target: string; source: string; markdown: string }>("/talend/studio-configuration"),
  talendHealth: () => req<{
    available: boolean;
    mcp_available?: boolean;
    bridge_available?: boolean;
    bridge_mode?: string;
    unsafe_actions?: boolean;
    write_enabled: boolean;
    spec_supported?: boolean;
    spec_error?: string | null;
    tools?: number | null;
    write_tool?: boolean | null;
    missing_tools?: string[];
    diagnosis?: "ok" | "mcp_down" | "client_incompatible" | "tools_missing" | "contract_incomplete" | "bridge_down" | "studio_blocked";
    fix_hint?: string | null;
    studio_dialogs?: {
      checked: boolean;
      blocked: boolean;
      blocking: Array<{ title: string; hint: string }>;
      error?: string;
    };
    studio_memory?: {
      checked: boolean;
      used_percent?: number;
      used_mb?: number;
      max_mb?: number;
      restart_recommended?: boolean;
      error?: string;
    };
    apply_folder: string;
    mcp_url?: string;
    timeout_seconds?: number;
    jobs?: number;
    error?: string;
  }>("/integrations/talend/health"),
  restartTalendStudio: () =>
    post<{ restarted: boolean; forced?: boolean; closedDialogs?: number; seconds?: number }>("/integrations/talend/studio/restart"),
  talendPermissions: () => req<{ write_enabled: boolean }>("/integrations/talend/permissions"),
  setTalendWriteEnabled: (enabled: boolean) =>
    patch<{ write_enabled: boolean }>("/integrations/talend/permissions", { write_enabled: enabled }),
};
