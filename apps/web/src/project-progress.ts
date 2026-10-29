import { link } from "./views/common";
import type { PendingGroup, ProjectProgress, ProjectStage } from "./types";

export const nextActionHref = (id: string, next: ProjectProgress["next"]): string | null =>
  next ? link(id, next.tab) : null;

export const stageTone = (status: ProjectStage["status"]): "ok" | "warn" | "bad" | "neutral" => {
  if (status === "done") return "ok";
  if (status === "current") return "warn";
  if (status === "blocked") return "bad";
  return "neutral";
};

export type PendingPanelState = "hidden" | "loading" | "ready";

// "ready" only when the pending list was really fetched (or failed, and Load shows the error).
// A request still in flight, or one never made because guides are not done, must not read as "nothing pending".
export const pendingPanelState = (
  guidesDone: boolean,
  pending: { loading?: boolean; data?: PendingGroup[]; error?: string },
): PendingPanelState => {
  if (!guidesDone) return "hidden";
  if (pending.loading || (pending.data === undefined && pending.error === undefined)) return "loading";
  return "ready";
};

export const pendingTotals =(groups: PendingGroup[]): { steps: number; jobs: number } => {
  const jobs = new Set<string>();
  const steps = new Set<string>();
  for (const group of groups) {
    for (const program of group.programs) {
      jobs.add(program.program);
      for (const stepId of program.step_ids) steps.add(`${program.program}\u0000${stepId}`);
    }
  }
  return { steps: steps.size, jobs: jobs.size };
};
