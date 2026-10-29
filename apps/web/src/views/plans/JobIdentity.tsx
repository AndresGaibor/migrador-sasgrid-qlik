import { Badge } from "../common";
import type { JobPlan } from "../../types";

export function JobIdentity({
  plan,
  folderPath,
}: {
  plan: Pick<JobPlan, "job_name" | "description" | "job_name_edited">;
  folderPath?: string;
}) {
  return (
    <div className="job-identity">
      <h1>{plan.job_name}{plan.job_name_edited && <Badge tone="warn">editado</Badge>}</h1>
      {plan.description && <p className="job-description">{plan.description}</p>}
      {folderPath && <p className="muted job-folder">Carpeta en Studio: <code>{folderPath}</code></p>}
    </div>
  );
}
