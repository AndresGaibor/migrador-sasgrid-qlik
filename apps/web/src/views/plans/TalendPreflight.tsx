import { Icon } from "../../components/Icon";
import type { TalendApplyBatchSummary } from "../../types";
import { link } from "../common";

export function TalendPreflight({ id, summary }: { id: string; summary: TalendApplyBatchSummary }) {
  const reviewJobs = summary.programs.filter((job) => job.draft_components.length || job.pending.length || job.blocked_steps.length || job.creation_kind === "context_only");
  return <div className="talend-preflight">
    <p className="preflight-destination"><Icon name="folder" size={16} /><span>Destino en Studio <code>{summary.destination_root}</code></span></p>
    <dl className="preflight-counts"><div><dt>Jobs</dt><dd>{summary.creatable_jobs}</dd></div><div><dt>Componentes</dt><dd>{summary.total_components}</dd></div><div><dt>Conexiones</dt><dd>{summary.total_connections}</dd></div><div><dt>Variables de contexto</dt><dd>{summary.total_contexts}</dd></div></dl>
    {reviewJobs.length > 0 && <p className="preflight-review"><Icon name="warning" size={16} /><span>{reviewJobs.length} {reviewJobs.length === 1 ? "Job con configuración pendiente" : "Jobs con configuración pendiente"}. La creación no sustituye la revisión ni las pruebas.</span></p>}
    {summary.cycles.length > 0 && <div className="notice warning"><Icon name="warning" size={17} /><span>Hay {summary.cycles.length === 1 ? "un ciclo de dependencias" : `${summary.cycles.length} ciclos de dependencias`}. El orden dentro de un ciclo es estable, no una garantía de ejecución correcta. <a href={link(id, "dependencias")}>Revisar dependencias</a></span></div>}
    <details className="preflight-programs"><summary>Ver alcance y pendientes por Job ({summary.total_jobs})</summary>
      {summary.programs.map((job) => {
        const reasons = [...new Set([...job.pending, ...job.draft_components.map((item) => `${item.unique_name}: ${item.reason}`), ...job.blocked_steps.map((item) => `${item.step_id}: ${item.reason}`)])];
        return <details className="preflight-job" key={job.program}><summary>{job.job_name}<span>{job.components} componentes · {job.draft_components.length} en borrador</span></summary>
          <p className="muted">Programa: <code>{job.program}</code></p><p className="muted">Destino: <code>{job.folder_path}</code></p>
          {job.creation_kind === "context_only" && <p className="preflight-review">Solo contexto: no se generarán componentes para este programa.</p>}
          {reasons.length > 0 ? <ul>{reasons.map((reason) => <li key={reason}>{reason}</li>)}</ul> : <p className="muted">Sin pendientes detectados en esta vista previa. Valida el Job en Studio.</p>}
          <a href={link(id, "planes", job.program)}>Abrir guía de {job.job_name}</a>
        </details>;
      })}
    </details>
  </div>;
}
