import type { CatalogComponent, CatalogList, Deps, GridRecommendation, JobPlan, Manifest, PlanRow, Program, ProgramRow, Project, ProjectUploadResponse, Summary, TalendApplyBatchPreflight, TalendApplyBatchState, TalendApplyPreview, TalendApplyResult, TalendApplyState, ProjectProcessing } from "./types";

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`/api${path}`, {
    ...init,
    headers: { "Content-Type": "application/json", ...init?.headers },
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new ApiError(res.status, body.detail ?? res.statusText);
  }
  return res.json() as Promise<T>;
}

const post = <T>(path: string, body?: unknown) =>
  req<T>(path, { method: "POST", body: body === undefined ? undefined : JSON.stringify(body) });
const enc = encodeURI;

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
    const res = await fetch("/api/projects/uploads", { method: "POST", body });
    if (!res.ok) {
      const b = await res.json().catch(() => ({}));
      throw new ApiError(res.status, b.detail ?? res.statusText);
    }
    return (await res.json()) as ProjectUploadResponse;
  },
  importPath: (id: string, path: string) => post<Manifest>(`/projects/${id}/imports`, { path }),
  upload: async (id: string, file: File) => {
    const body = new FormData();
    body.append("file", file);
    const res = await fetch(`/api/projects/${id}/uploads`, { method: "POST", body });
    if (!res.ok) {
      const b = await res.json().catch(() => ({}));
      throw new ApiError(res.status, b.detail ?? res.statusText);
    }
    return (await res.json()) as Manifest;
  },
  inventory: (id: string) => req<Manifest>(`/projects/${id}/inventory`),
  processing: (id: string) => req<ProjectProcessing>(`/projects/${id}/processing`),
  retryProcessing: (id: string) => post<ProjectProcessing>(`/projects/${id}/processing/retry`),
  analysis: (id: string) => req<Summary>(`/projects/${id}/analyses`),
  analyze: (id: string) => post<Summary>(`/projects/${id}/analyses`),
  programs: (id: string) => req<ProgramRow[]>(`/projects/${id}/programs`),
  program: (id: string, file: string) => req<Program>(`/projects/${id}/programs/${enc(file)}`),
  sourceEvidence: (id: string, file: string, line: number) =>
    `/api/projects/${id}/source/${file.split("/").map(encodeURIComponent).join("/")}?line=${line}`,
  deps: (id: string) => req<Deps>(`/projects/${id}/dependencies`),
  generatePlans: (id: string) => post<{ plans: number }>(`/projects/${id}/plans`),
  plans: (id: string) => req<PlanRow[]>(`/projects/${id}/plans`),
  gridRecommendations: (id: string) => req<GridRecommendation[]>(`/projects/${id}/plans/grid-recommendations`),
  plan: (id: string, file: string) => req<JobPlan>(`/projects/${id}/plans/${enc(file)}`),
  applyTalend: (id: string, file: string) =>
    post<TalendApplyResult>(`/projects/${id}/plans/${enc(file)}/talend-apply`),
  talendApplyPreview: (id: string, file: string) =>
    post<TalendApplyPreview>(`/projects/${id}/plans/${enc(file)}/talend-apply/preview`),
  talendApplyStatus: (id: string, file: string) =>
    req<TalendApplyState>(`/projects/${id}/plans/${enc(file)}/talend-apply`),
  talendApplyBatch: (id: string) => post<TalendApplyBatchState>(`/projects/${id}/talend-apply-batch`),
  talendApplyBatchStatus: (id: string) => req<TalendApplyBatchState>(`/projects/${id}/talend-apply-batch`),
  talendApplyBatchPreflight: (id: string) => req<TalendApplyBatchPreflight>(`/projects/${id}/talend-apply-batch/preflight`),
  exportAll: (id: string) => post<{ directory: string; files: string[] }>(`/projects/${id}/exports`),
  exportFile: (id: string, name: string) => `/api/projects/${id}/exports/${encodeURIComponent(name)}`,
  catalog: (q: string, family: string) =>
    req<CatalogList>(`/talend/catalog?q=${encodeURIComponent(q)}${family ? `&family=${encodeURIComponent(family)}` : ""}`),
  component: (name: string) => req<CatalogComponent>(`/talend/catalog/${encodeURIComponent(name)}`),
  talendHealth: () => req<{ available: boolean; mcp_available?: boolean; bridge_available?: boolean; write_enabled: boolean; apply_folder: string; jobs?: number; error?: string }>("/integrations/talend/health"),
};
