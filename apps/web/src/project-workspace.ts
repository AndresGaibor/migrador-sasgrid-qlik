import type { PendingSummary, Project } from "./types";

export function pendingTotals(groups: readonly PendingSummary[]): { steps: number; jobs: number } {
  return {
    steps: groups.reduce((total, group) => total + group.steps, 0),
    jobs: new Set(groups.flatMap((group) => group.programs.map((job) => job.program))).size,
  };
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
