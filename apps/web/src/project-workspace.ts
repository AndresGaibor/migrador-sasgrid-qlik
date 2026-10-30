import type { PendingSummary, Project } from "./types";

export type PendingJob = { program: string; jobName: string; steps: number };
export type PendingPart = { title: string; detail: string; steps: number; jobs: PendingJob[] };
export type PendingDecision = { title: string; hint?: string; steps: number; jobs: PendingJob[]; parts?: PendingPart[] };

// Un mismo paso puede tener varios motivos pendientes: se cuenta una sola vez por su id.
function summarizePending(groups: readonly PendingSummary[]): { steps: number; jobs: PendingJob[] } {
  const byJob = new Map<string, { program: string; jobName: string; ids: Set<string> }>();
  for (const group of groups) {
    for (const job of group.programs) {
      const key = `${job.program}\u0000${job.job_name}`;
      const entry = byJob.get(key) ?? { program: job.program, jobName: job.job_name, ids: new Set<string>() };
      job.step_ids.forEach((id) => entry.ids.add(id));
      byJob.set(key, entry);
    }
  }
  const jobs = [...byJob.values()]
    .map((entry) => ({ program: entry.program, jobName: entry.jobName, steps: entry.ids.size }))
    .sort((a, b) => b.steps - a.steps || a.jobName.localeCompare(b.jobName, "es"));
  return { steps: jobs.reduce((total, job) => total + job.steps, 0), jobs };
}

export function pendingTotals(groups: readonly PendingSummary[]): { steps: number; jobs: number } {
  return {
    steps: summarizePending(groups).steps,
    jobs: new Set(groups.flatMap((group) => group.programs.map((job) => job.program))).size,
  };
}

const LIBRARY_REASON = /^Librería (.+?) es de tipo BASE(?: en (.+?))?: /;

/**
 * Agrupa los motivos por decisión. Los motivos de librerías SAS repiten la misma
 * decisión con otro nombre, así que se juntan en una sola y se listan aparte.
 */
export function groupPendingDecisions(groups: readonly PendingSummary[]): PendingDecision[] {
  const libraries = groups.filter((group) => LIBRARY_REASON.test(group.reason));
  const decisions: PendingDecision[] = groups
    .filter((group) => !LIBRARY_REASON.test(group.reason))
    .map((group) => ({ title: group.reason, ...summarizePending([group]) }));
  if (libraries.length > 0) {
    decisions.push({
      title: "Librerías SAS que Talend no lee directamente",
      hint: "Talend no lee archivos .sas7bdat. Confirma si cada librería tiene una copia en base de datos o en archivo.",
      ...summarizePending(libraries),
      parts: libraries.map((group) => {
        const [, name, path] = LIBRARY_REASON.exec(group.reason) ?? [];
        return { title: name ?? group.reason, detail: path ?? "sin ruta fija", ...summarizePending([group]) };
      }),
    });
  }
  return decisions.sort((a, b) => b.steps - a.steps || a.title.localeCompare(b.title, "es"));
}

export function filterProjectsByQuery<T extends Pick<Project, "name" | "archive_name">>(
  projects: readonly T[],
  query: string,
): T[] {
  const normalized = query.trim().toLocaleLowerCase("es");
  if (!normalized) return [...projects];
  return projects.filter((project) =>
    `${project.name} ${project.archive_name ?? ""}`
      .toLocaleLowerCase("es")
      .includes(normalized),
  );
}

export type ProjectStatusFilter = "all" | "processing" | "completed" | "attention" | "waiting";
export type ProjectSourceFilter = "all" | "archive" | "individual" | "manual";

export function filterProjectsByFacets<
  T extends { archive_name?: string | null; processing?: { status: string } | null },
>(
  projects: readonly T[],
  status: ProjectStatusFilter,
  source: ProjectSourceFilter,
): T[] {
  return projects.filter((project) => {
    const processingStatus = project.processing?.status;
    const isArchive = project.archive_name?.toLocaleLowerCase("es").endsWith(".zip") ?? false;
    const matchesStatus = status === "all"
      || (status === "processing" && (processingStatus === "queued" || processingStatus === "running"))
      || (status === "completed" && processingStatus === "completed")
      || (status === "attention" && (processingStatus === "failed" || processingStatus === "interrupted"))
      || (status === "waiting" && !processingStatus);
    const matchesSource = source === "all"
      || (source === "archive" && isArchive)
      || (source === "individual" && Boolean(project.archive_name) && !isArchive)
      || (source === "manual" && !project.archive_name);
    return matchesStatus && matchesSource;
  });
}

export function processingLabel(processing: { status: string; stage: string }): string {
  if (processing.status === "queued") return "En cola";
  if (processing.status === "completed") return "Análisis listo";
  if (processing.status === "interrupted") return "Interrumpido";
  if (processing.status === "failed") {
    const stageLabels: Record<string, string> = {
      extraction: "la extracción",
      analysis: "el análisis",
      dependencies: "las dependencias",
      plans: "las guías",
    };
    return `Error en ${stageLabels[processing.stage] ?? "el proceso"}`;
  }
  const stageLabels: Record<string, string> = {
    extraction: "Extrayendo ZIP",
    analysis: "Analizando programas SAS",
    dependencies: "Construyendo dependencias",
    plans: "Generando guías",
  };
  return stageLabels[processing.stage] ?? "Procesando proyecto";
}

export function filterArchiveEntries<T extends { path: string }>(
  entries: readonly T[],
  query: string,
): T[] {
  const normalized = query.trim().replaceAll("\\", "/").toLocaleLowerCase("es");
  if (!normalized) return [...entries];
  return entries.filter((entry) =>
    entry.path.replaceAll("\\", "/").toLocaleLowerCase("es").includes(normalized),
  );
}

export type InventoryKindFilter = "all" | "sas" | "shell" | "log" | "doc" | "other";

export function filterFilesByKind<T extends { kind: string }>(
  files: readonly T[],
  kind: InventoryKindFilter,
): T[] {
  return kind === "all" ? [...files] : files.filter((file) => file.kind === kind);
}
