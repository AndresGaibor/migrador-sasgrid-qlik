import { useState } from "react";
import { Icon } from "../../components/Icon";
import type { PlanRow } from "../../types";
import { Badge, link } from "../common";

export type PlanGroup = { title: string; hint: string; rows: PlanRow[] };

export function PlanListContent({ id, rows, groups, isDesktop, orderVerified = true }: { id: string; rows: PlanRow[]; groups: PlanGroup[]; isDesktop: boolean; orderVerified?: boolean }) {
  const [query, setQuery] = useState("");
  const search = query.trim().toLocaleLowerCase();
  const empty = rows.filter((row) => row.steps === 0);
  const ordered = groups.flatMap((group) => group.rows);
  const next = ordered.find((row) => row.done < row.steps);
  const nextGroup = groups.find((group) => group.rows.some((row) => row.done < row.steps));
  const guideRows = rows.filter((row) => row.steps > 0);
  const completedJobs = guideRows.filter((row) => row.done >= row.steps).length;
  if (rows.length === 0) return <div className="empty-state"><span className="empty-icon"><Icon name="flow" size={34} /></span><h3>Primero analiza tus programas</h3><p>Cuando termine el análisis, aquí aparecerá una guía para cada job.</p><a className="button" href={link(id, "resumen")}>Ir al resumen <Icon name="arrow" size={17} /></a></div>;

  let position = 0;
  return <>
    {next ? <div className="guide-intro"><div><strong>{orderVerified ? "Siguiente Job para revisar" : "Job pendiente de revisar"}</strong><p>{next.job_name}</p><small className="guide-progress-summary">{completedJobs} de {guideRows.length} Jobs completados · {guideRows.length - completedJobs} pendientes</small></div><a className="button" href={link(id, "planes", next.program)}>Abrir guía <Icon name="arrow" size={17} /></a></div> : guideRows.length > 0 && <div className="guide-intro" role="status"><div><strong>Guías completadas</strong><p>Terminaste todos los Jobs que requieren pasos.</p></div><Badge tone="ok">{completedJobs} completados</Badge></div>}
    {isDesktop && guideRows.length > 0 && <div className="guide-list-toolbar"><h2>Guías de los Jobs <span>{guideRows.length}</span></h2><label className="archive-path-search"><Icon name="search" size={16} /><input type="search" aria-label="Buscar Job o programa SAS" placeholder="Buscar Job o programa SAS" value={query} onChange={(event) => setQuery(event.target.value)} /></label></div>}
    {isDesktop && search && !guideRows.some((row) => `${row.job_name} ${row.program}`.toLocaleLowerCase().includes(search)) && <p role="status" className="notice">No hay Jobs que coincidan con «{query}». Prueba con otro nombre.</p>}
    {groups.map((group) => {
      const completed = group.rows.filter((row) => row.done >= row.steps).length;
      const groupStart = position;
      position += group.rows.length;
      const matching = group.rows.filter((row) => !isDesktop || `${row.job_name} ${row.program}`.toLocaleLowerCase().includes(search));
      if (!matching.length) return null;
      const cards = <div className="guide-job-list">{matching.map((row) => <article className={`guide-job${row === next ? " is-next" : ""}`} key={row.program}>
        <div className="guide-job-main"><h3>{groupStart + group.rows.indexOf(row) + 1}. {row.job_name}{isDesktop && row === next && orderVerified && <span className="guide-next-label">Siguiente</span>}</h3>{isDesktop && <small className="guide-source" title={row.program}>{row.program}</small>}<div className="guide-job-meta">{row.done >= row.steps ? <Badge tone="ok">Terminado</Badge> : <span>{row.done} de {row.steps} pasos hechos</span>}<progress aria-label={`Avance manual de ${row.job_name}`} max={row.steps} value={row.done} /></div>{row.studio_status && <small className={`guide-studio-progress ${row.studio_status}`} role="status">{row.studio_status === "not_checked" ? "Comprobación automática: pendiente de creación en Studio" : row.studio_status === "unavailable" ? "Comprobación automática: Studio no disponible" : `Comprobación automática en Studio: ${row.studio_verified ?? 0} de ${row.steps} pasos verificados`}</small>}</div>
        <a className={`button${isDesktop ? " secondary" : ""}`} aria-label={`Abrir guía de ${row.job_name}`} href={link(id, "planes", row.program)}>Abrir <Icon name="arrow" size={17} /></a>
      </article>)}</div>;
      return isDesktop ? (
        <details className="guide-group" key={`${group.title}:${Boolean(search)}`} open={Boolean(search) || group === nextGroup}>
          <summary><strong>{group.title}</strong><span className="guide-group-count">{group === nextGroup && orderVerified && "Siguiente · "}{completed} de {group.rows.length} Jobs completados</span></summary>
          <p className="muted">{group.hint}</p>
          {cards}
        </details>
      ) : (
        <section key={group.title}>
          <h2>{group.title}</h2><p className="muted">{group.hint}</p>
          {cards}
        </section>
      );
    })}
    {empty.length > 0 && <details><summary>{empty.length} programa{empty.length === 1 ? "" : "s"} sin pasos guiados</summary><p className="muted">Puede incluir variables de contexto o información de origen. Consulta su alcance en la vista previa de creación.</p><ul>{empty.map((row) => <li key={row.program}><code>{row.program}</code></li>)}</ul></details>}
  </>;
}
