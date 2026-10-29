import type { PendingGroup } from "../../types";
import { pendingTotals } from "../../project-progress";
import { Icon } from "../../components/Icon";
import { link } from "../common";

const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;

export const pendingText = (totals: { steps: number; jobs: number }) =>
  `${plural(totals.steps, "paso", "pasos")} en ${plural(totals.jobs, "Job", "Jobs")}`;

export function PendingPanel({ id, groups }: { id: string; groups: PendingGroup[] }) {
  if (groups.length === 0) return <section className="pending-panel">
    <h2>Qué falta</h2>
    <div className="notice"><Icon name="check" /><span>No quedan pendientes.</span></div>
  </section>;
  return <section className="pending-panel">
    <h2>Qué falta</h2>
    <p className="muted">{pendingText(pendingTotals(groups))}</p>
    {groups.map((group) => <details key={group.reason}>
      <summary>{group.reason} <span className="muted">({plural(group.steps, "paso", "pasos")})</span></summary>
      <ul className="pending-jobs">
        {group.programs.map((program) => <li key={program.program}><a href={link(id, "planes", program.program)}>{program.job_name}</a> <span className="muted">{program.program}</span></li>)}
      </ul>
    </details>)}
  </section>;
}
