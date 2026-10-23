import type { Project } from "./types";

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
