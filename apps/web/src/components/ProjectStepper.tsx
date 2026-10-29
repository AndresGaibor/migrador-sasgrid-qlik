import type { ProjectStage } from "../types";
import { stageTone } from "../project-progress";
import { Badge } from "../views/common";

const statusLabel: Record<ProjectStage["status"], string> = {
  done: "Hecho",
  current: "En curso",
  todo: "Pendiente",
  blocked: "Bloqueado",
};

export function ProjectStepper({ stages }: { stages: ProjectStage[] }) {
  return <ol className="project-stepper">
    {stages.map((stage) => <li key={stage.key} className={`project-stepper-step ${stage.status}`} aria-current={stage.status === "current" ? "step" : undefined}>
      <strong>{stage.label}</strong>
      <span className="project-stepper-detail">{stage.detail}</span>
      <Badge tone={stageTone(stage.status)}>{statusLabel[stage.status]}</Badge>
    </li>)}
  </ol>;
}
