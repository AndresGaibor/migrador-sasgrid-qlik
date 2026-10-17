import type { Deps, JobPlan, Manifest, PlanRow, Program, ProgramRow, Project, Summary } from "./types";

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
  analyze: (id: string) => post<Summary>(`/projects/${id}/analyses`),
  programs: (id: string) => req<ProgramRow[]>(`/projects/${id}/programs`),
  program: (id: string, file: string) => req<Program>(`/projects/${id}/programs/${enc(file)}`),
  deps: (id: string) => req<Deps>(`/projects/${id}/dependencies`),
  generatePlans: (id: string) => post<{ plans: number }>(`/projects/${id}/plans`),
  plans: (id: string) => req<PlanRow[]>(`/projects/${id}/plans`),
  plan: (id: string, file: string) => req<JobPlan>(`/projects/${id}/plans/${enc(file)}`),
  decide: (id: string, file: string, step: string, status: string, note: string | null) =>
    req<JobPlan>(`/projects/${id}/plans/${enc(file)}/steps/${step}`, {
      method: "PATCH",
      body: JSON.stringify({ status, note }),
    }),
  exportAll: (id: string) => post<{ directory: string; files: string[] }>(`/projects/${id}/exports`),
  talendHealth: () => req<{ available: boolean; jobs?: number; error?: string }>("/integrations/talend/health"),
};
