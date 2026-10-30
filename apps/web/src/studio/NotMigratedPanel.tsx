// Panel «Lo que NO hace falta migrar»: fontanería de SAS que el planificador no traduce, con su equivalente en Talend.
import { Icon } from "../components/Icon";
import { link } from "../views/common";
import type { JobPlan } from "../types";
import { countNotMigrated, groupNotMigrated } from "./not-migrated-model";
import "./studio-panels.css";

export function NotMigratedPanel({ id, plan }: { id: string; plan: JobPlan }) {
  const items = plan.not_migrated ?? [];
  if (items.length === 0) return null;
  const groups = groupNotMigrated(items);
  const sasLink = (line: number) => `${link(id, "programas", plan.program)}?line=${line}`;
  return (
    <details className="panel nm-panel">
      <summary>
        <Icon name="info" size={16} /> <b>Lo que NO hace falta migrar</b>{" "}
        <span className="badge">{countNotMigrated(items)} {countNotMigrated(items) === 1 ? "caso" : "casos"}</span>
      </summary>
      <p className="muted nm-lead">SAS necesitaba esto; Talend lo resuelve solo o con otro componente.</p>
      {groups.map((group) => (
        <section className="nm-group" key={group.what}>
          <h3>{group.what}</h3>
          <p><b>Por qué no hace falta:</b> {group.reason}</p>
          <p><b>Qué hace Talend:</b> {group.talend_equivalent}</p>
          <p className="muted nm-meta">
            <code>{group.category}</code> · {group.count} {group.count === 1 ? "aparición" : "apariciones"} · Ver el SAS original:{" "}
            {group.lines.length > 0
              ? group.lines.map((line, index) => <span key={line}>{index > 0 && ", "}<a href={sasLink(line)}>línea {line}</a></span>)
              : "sin línea indicada"}
          </p>
        </section>
      ))}
    </details>
  );
}
