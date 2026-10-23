export const GUIDE_PROGRESS = ["pending", "in_progress", "completed", "blocked"] as const;
export type GuideProgress = (typeof GUIDE_PROGRESS)[number];
export type DecodedProgress = { state: GuideProgress; note: string; blockReason: string };
export type UncertainStep = { pending?: string[]; confidence?: string; verified?: boolean; requires_semantic_validation?: boolean };

export function isUncertainStep(step: UncertainStep): boolean {
  return Boolean(step.pending?.length || step.confidence !== "high" || !step.verified || step.requires_semantic_validation);
}

const stateLabels: Record<GuideProgress, string> = {
  pending: "pendiente",
  in_progress: "en_progreso",
  completed: "completado",
  blocked: "bloqueado",
};

export function storageStatus(state: GuideProgress): string {
  if (state === "in_progress") return "propuesto";
  if (state === "completed") return "validado_manualmente";
  if (state === "blocked") return "pendiente";
  return "pendiente";
}

// Persist the web-only progress label in the note field supported by the API.
export function encodeProgress(state: GuideProgress, note: string, blockReason: string): string | null {
  if (state === "blocked" && !blockReason.trim()) return null;
  const metadata = [`[Estado de guía: ${stateLabels[state]}]`];
  if (state === "blocked") metadata.push(`[Motivo de bloqueo: ${blockReason.trim().replace(/\s+/g, " ")}]`);
  if (note.trim()) metadata.push(`[Nota de trabajo: ${note.trim()}]`);
  return metadata.join("\n");
}

export function decodeProgress(status: string, note: string | null): DecodedProgress {
  const savedState = note?.match(/^\[Estado de guía: (pendiente|en_progreso|completado|bloqueado)\]/m)?.[1];
  const state: GuideProgress = savedState === "en_progreso" ? "in_progress"
    : savedState === "completado" ? "completed"
    : savedState === "bloqueado" ? "blocked"
    : savedState === "pendiente" ? "pending"
    : status === "verificado" || status === "validado_manualmente" ? "completed"
    : status === "descartado" ? "blocked"
    : "pending";
  const blockReason = note?.match(/^\[Motivo de bloqueo: (.*)\]$/m)?.[1]
    ?? (status === "descartado" ? "Este paso fue descartado anteriormente; confirma si debe continuar bloqueado." : "");
  const workNote = note?.match(/^\[Nota de trabajo: ([\s\S]*)\]$/m)?.[1] ?? (savedState ? "" : note ?? "");
  return { state, note: workNote, blockReason };
}
