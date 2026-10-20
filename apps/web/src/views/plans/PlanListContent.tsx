import { Icon } from "../../components/Icon";
import type { PlanRow } from "../../types";
import { Badge, link } from "../common";

export type PlanGroup = { title: string; hint: string; rows: PlanRow[] };

export function PlanListContent({ id, rows, groups }: { id: string; rows: PlanRow[]; groups: PlanGroup[] }) {
  const empty = rows.filter((row) => row.steps === 0);
  const ordered = groups.flatMap((group) => group.rows);
  const next = ordered.find((row) => row.done < row.steps);
  if (rows.length === 0) return <div className="empty-state"><span className="empty-icon"><Icon name="flow" size={34} /></span><h3>Primero analiza tus programas</h3><p>Cuando termine el análisis, aquí aparecerá una guía para cada job.</p><a className="button" href={link(id, "resumen")}>Ir al resumen <Icon name="arrow" size={17} /></a></div>;

  let position = 0;
  return <>
    {next && <div className="guide-intro"><div><strong>{next.done === 0 && next === ordered[0] ? "Empieza aquí" : "Continúa aquí"}</strong><p>{next.job_name}</p></div><a className="button" href={link(id, "planes", next.program)}>{next.done === 0 && next === ordered[0] ? "Empezar" : "Continuar"} <Icon name="arrow" size={17} /></a></div>}
    {groups.map((group) => <section key={group.title}>
      <h2>{group.title}</h2><p className="muted">{group.hint}</p>
      <div className="guide-job-list">{group.rows.map((row) => <article className="guide-job" key={row.program}>
        <div className="guide-job-main"><h3>{++position}. {row.job_name}</h3><div className="guide-job-meta">{row.done >= row.steps ? <Badge tone="ok">Terminado</Badge> : <span>{row.done} de {row.steps} pasos hechos</span>}<progress max={row.steps} value={row.done} /></div></div>
        <a className="button" href={link(id, "planes", row.program)}>Abrir <Icon name="arrow" size={17} /></a>
      </article>)}</div>
    </section>)}
    {empty.length > 0 && <details><summary>{empty.length} programa{empty.length === 1 ? "" : "s"} sin nada que construir</summary><ul>{empty.map((row) => <li key={row.program}><code>{row.program}</code></li>)}</ul></details>}
  </>;
}
