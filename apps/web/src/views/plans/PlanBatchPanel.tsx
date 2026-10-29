import { Icon } from "../../components/Icon";
import { Badge, link } from "../common";
import { formatErrorMessage } from "../../errors";
import type { TalendApplyBatchJob, TalendApplyBatchPreflight } from "../../types";
import { talendApplyJobLabel } from "./plan-status";

export function TalendPreflightPanel({ preflight }: { preflight: { data?: TalendApplyBatchPreflight; error?: string; loading: boolean; reload: () => void } }) {
  const report = preflight.data;
  return <section className={`talend-preflight ${preflight.error ? "error" : report?.conflict_count ? "conflict" : "ready"}`} aria-label="Comprobación del destino Talend" aria-live="polite">
    <div className="talend-preflight-heading">
      <div><strong>{preflight.loading ? "Comprobando el destino en Talend…" : preflight.error ? "No se pudo verificar el destino" : report ? "Destino comprobado en Talend" : "Esperando comprobación del destino"}</strong>
        {report && !preflight.error && <small>{report.create_count} se crearán · {report.update_count} se actualizarán · {report.conflict_count} conflictos · {report.inventory_count} Jobs revisados{report.checked_at ? ` · ${new Date(report.checked_at).toLocaleTimeString("es", { hour: "2-digit", minute: "2-digit" })}` : ""}</small>}
      </div>
      <button type="button" className="secondary" onClick={preflight.reload} disabled={preflight.loading}>Volver a comprobar</button>
    </div>
    {preflight.error && <p className="error" role="alert">No se iniciará ninguna escritura hasta verificar MCP y el inventario completo: {preflight.error}</p>}
    {report?.studio_memory?.restart_recommended && !preflight.error && <p className="notice" role="status">Studio ya usa el {report.studio_memory.used_percent} % de su memoria y un lote grande la llena: reinícialo desde Configuración antes de aplicar.</p>}
    {report && !preflight.error && <details open={report.conflict_count > 0}>
      <summary>Ver acciones para los {report.total_jobs} Jobs</summary>
      <ul>{report.jobs.map((job) => <li key={job.program} className={`talend-preflight-job ${job.action}`}>
        <div><strong>{preflightActionLabel(job.action)}:</strong> <code>{job.job_name}</code> · <code>{job.program}</code></div>
        <small>Destino: <code>{job.folder_path}</code></small>
        {job.existing_path && <small>Job existente: <code>{job.existing_path}</code></small>}
        {job.reason && <small className="error">{job.reason}</small>}
      </li>)}</ul>
    </details>}
  </section>;
}

function preflightActionLabel(action: TalendApplyBatchPreflight["jobs"][number]["action"]): string {
  const labels = { create: "Se creará", update: "Se actualizará en esta carpeta", conflict: "Conflicto" };
  return labels[action];
}

export function BatchJobRow({ projectId, path, job }: { projectId: string; path: string; job: TalendApplyBatchJob }) {
  const result = job.result;
  const reviewRequired = Boolean(result?.review_required || result?.review_warnings?.length || result?.warnings.length || result?.blocked_steps.length);
  const warnings = [...(result?.warnings ?? []), ...(result?.review_warnings ?? [])];
  return <article className={`talend-batch-job ${job.status}`}>
    <div className="talend-batch-job-heading"><Icon name={reviewRequired ? "warning" : job.status === "applied" ? "check" : job.status === "running" ? "flow" : job.status === "pending" ? "info" : "warning"} size={17} /><strong>{result?.identity.job_name ?? path}</strong><span>{job.status === "applied" && reviewRequired ? "Estructura creada; revisión pendiente" : talendApplyJobLabel(job.status)}</span></div>
    {job.phase && <p className="muted">{job.phase === "applying" ? "Fase: creando componentes" : job.phase === "inspecting" ? "Fase: verificando el Job en Studio" : "Fase: preparando el Job"}</p>}
    <p className="muted"><code>{path}</code>{result?.result.itemPath && <> · destino <code>{result.result.itemPath}</code></>}</p>
    {result && <p className="talend-batch-job-metrics">{result.result.totalComponents ?? (result.result.generatedComponents ?? 0) + (result.result.reusedComponents ?? 0)} componentes · {(result.result.generatedConnections ?? 0) + (result.result.reusedConnections ?? 0)} conexiones · {(result.result.generatedContexts ?? 0) + (result.result.updatedContexts ?? 0) + (result.result.reusedContexts ?? 0)} variables de contexto</p>}
    {job.error && <p className="error" role="alert">{formatErrorMessage(job.error)}</p>}
    {result?.verification && <p className="talend-batch-job-verification">{result.verification.status === "inspected"
      ? <>Inspeccionado en Studio: {result.verification.components_created} componentes encontrados; {result.verification.components_requested} solicitados. · {result.verification.configured_steps ?? 0} pasos configurados · {result.verification.pending_steps ?? 0} pendientes.</>
      : <>Verificación no disponible: {result.verification.reason ?? "el MCP no pudo inspeccionar el Job."}</>}
      {result.verification.studio_problems && (result.verification.studio_problems.clean
        ? <Badge tone="ok">Sin avisos de diseño</Badge>
        : <Badge tone="warn">Revisar avisos en Studio</Badge>)}
    </p>}
    {result?.verification && result.verification.missing_components.length > 0 && <details><summary>Componentes que no aparecen en Studio ({result.verification.missing_components.length})</summary><ul>{result.verification.missing_components.map((name) => <li key={name}><code>{name}</code></li>)}</ul></details>}
    {result?.verification?.steps?.some((item) => item.status !== "verified") && <details><summary>Pasos que requieren revisión automática ({result.verification.pending_steps ?? 0})</summary><ul>{result.verification.steps.filter((item) => item.status !== "verified").map((item, index) => <li key={`${item.program}:${item.step_id}:${index}`}><strong>{item.program} · {item.step_id}:</strong> {item.reason ?? "No se confirmó el componente o su configuración."}</li>)}</ul></details>}
    {result?.verification?.studio_problems && !result.verification.studio_problems.clean && <details><summary>Avisos de la vista Problemas de Studio</summary><ul>{result.verification.studio_problems.items.map((item, index) => <li key={index}>{item.severity ? `[${item.severity}] ` : ""}{item.message ?? JSON.stringify(item)}</li>)}</ul></details>}
    {result && (warnings.length > 0 || result.blocked_steps.length > 0) && <details><summary>Información técnica pendiente</summary><ul>{warnings.map((warning, index) => <li key={`warning-${index}`}>{warning}</li>)}{result.blocked_steps.map((block) => <li key={block.step_id}><strong>{block.step_id === "job" ? "Job" : `Paso ${block.step_id}`}:</strong> {block.reason}</li>)}</ul></details>}
    <a className="talend-batch-job-link" href={link(projectId, "planes", path)}>Abrir guía</a>
  </article>;
}
