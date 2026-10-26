import { useEffect, useState } from "react";
import { Icon } from "../components/Icon";
import { api } from "../api";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { GridRecommendation, Step, TalendApplyBatchJob, TalendApplyBatchPreflight, TalendApplyBatchState, TalendApplyState } from "../types";
import { Badge, Load, link } from "./common";
import { orderSteps } from "../guided";
import { catalogAudit } from "../catalog-explorer";
import { ArchivePathTree } from "../components/ArchivePathTree";

export function PlansTab({ id, file, projectName, archiveName }: { id: string; file?: string; projectName?: string; archiveName?: string | null }) {
  return file ? <PlanDetail key={`${id}:${decodeURI(file)}`} id={id} file={decodeURI(file)} /> : <PlanList id={id} projectName={projectName} archiveName={archiveName} />;
}

function PlanList({ id, projectName, archiveName }: { id: string; projectName?: string; archiveName?: string | null }) {
  const q = useAsync(() => api.plans(id), [id]);
  const grid = useAsync(() => api.gridRecommendations(id), [id]);
  const health = useAsync(() => api.talendHealth(), [id]);
  const batch = useAsync(() => api.talendApplyBatchStatus(id), [id], { preserveDataOnError: true });
  const preflight = useAsync(() => api.talendApplyBatchPreflight(id), [id, q.data?.length ?? 0], { preserveDataOnError: true });
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const [batchBusy, setBatchBusy] = useState(false);
  const [batchError, setBatchError] = useState<string>();
  const batchState = batch.data;
  const batchActive = batchState?.status === "queued" || batchState?.status === "running";
  const preflightReady = Boolean(!preflight.loading && !preflight.error && preflight.data?.available && preflight.data.conflict_count === 0);
  const staleConflictResolved = Boolean(batchState?.status === "conflict" && preflightReady);
  const missingJobCount = preflight.data?.create_count ?? 0;
  const batchFinished = batchState?.status === "applied" && missingJobCount === 0 || batchState?.status === "conflict" && !preflightReady;
  const canStartBatch = Boolean(q.data?.length && health.data?.available && health.data.write_enabled && preflightReady && !batchBusy && !batchActive && !batchFinished);
  useEffect(() => {
    if (!batchActive && !batch.error) return;
    const timer = window.setInterval(batch.reload, 1200);
    return () => window.clearInterval(timer);
  }, [batchActive, batch.error, batch.reload]);
  useEffect(() => {
    if (batchState && ["applied", "partially_applied", "failed", "conflict"].includes(batchState.status)) preflight.reload();
  }, [batchState?.status, preflight.reload]);
  const gen = async () => {
    setBusy(true);
    setErr(undefined);
    try {
      await api.generatePlans(id);
      q.reload();
      grid.reload();
      preflight.reload();
    } catch (x) {
      setErr((x as Error).message);
    } finally {
      setBusy(false);
    }
  };
  const implementProject = async () => {
    setBatchBusy(true);
    setBatchError(undefined);
    try {
      await api.talendApplyBatch(id);
      batch.reload();
    } catch (x) {
      setBatchError((x as Error).message);
      preflight.reload();
    } finally {
      setBatchBusy(false);
    }
  };
  return (
    <>
      <h1>Jobs y guías de migración</h1>
      <p className="subtitle">Cada programa SAS tiene una instrucción técnica que el MCP puede aplicar directamente en Talend Studio.</p>
      <div className="panel"><div className="panel-heading"><Icon name="list" size={26} /><div><h2>Guía para cada programa</h2><p>El portal instruye al MCP con el plan SAS y MCP agrega los componentes compatibles en Talend.</p></div></div><button onClick={gen} disabled={busy}><Icon name="play" size={16} />{busy ? "Preparando guías…" : q.data?.length ? "Actualizar guías" : "Preparar guías de migración"}</button><p className="muted" style={{ fontSize: 12, marginBottom: 0 }}>Las guías se reconstruyen a partir del análisis y del código SAS vigente.</p></div>
      {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
      {q.data?.length ? <section className="talend-batch-panel" aria-labelledby="talend-batch-title">
        <div className="talend-batch-heading"><div><span className="eyebrow">IMPLEMENTACIÓN DEL PROYECTO</span><h2 id="talend-batch-title">Crear todos los Jobs en Talend</h2><p>Un solo envío comparte con el MCP las instrucciones de todos los programas de este ZIP, en orden de dependencias. Los detalles incompletos permanecen como pendientes en cada Job.</p></div>
          <span className={`talend-mcp-status ${health.data?.available ? health.data.write_enabled ? "online" : "readonly" : "offline"}`} role="status" aria-live="polite">{health.loading ? "Consultando MCP…" : health.data?.available ? health.data.write_enabled ? "MCP y Bridge listos" : "MCP en solo lectura" : health.data?.mcp_available ? "Bridge sin conexión" : "MCP sin conexión"}</span>
        </div>
        <div className="talend-batch-project"><Icon name="folder" size={18} /><span><strong>{archiveName ?? projectName ?? `Proyecto ${id}`}</strong><small>{q.data.length} Jobs · destino raíz <code>{health.data?.apply_folder ?? "Process/PruebasWebSAS"}</code></small></span></div>
        <TalendPreflightPanel preflight={preflight} />
        <button type="button" className="talend-implement-button talend-batch-button" onClick={() => void implementProject()} disabled={!canStartBatch}>
          <Icon name="flow" size={20} />{batchBusy || batchActive ? "Implementando lote en Talend…" : preflight.loading ? "Verificando destino en Talend…" : preflight.error ? "Destino sin verificar" : preflight.data?.conflict_count ? "Resolver conflictos de destino" : batchState?.status === "applied" && missingJobCount > 0 ? "Recrear Jobs faltantes en Talend" : staleConflictResolved ? "Aplicar según inventario actual" : batchState?.status === "applied" ? "Todos los Jobs implementados" : batchState && ["failed", "partially_applied", "interrupted"].includes(batchState.status) ? "Reintentar Jobs pendientes" : "Implementar todos los flujos del ZIP en Talend"}
        </button>
        {health.data?.error && <p className="error" role="alert">{health.data.error}</p>}
        {health.error && <p className="error" role="alert">{health.error}</p>}
        {batchError && <p className="error" role="alert">No se pudo iniciar el lote: {batchError}</p>}
        {batch.error && <p className="error" role="alert">No se pudo actualizar el progreso del lote: {batch.error}. Se volverá a intentar automáticamente.</p>}
        {health.data?.available && !health.data.write_enabled && <p className="muted">Activa <code>TALEND_MCP_READONLY=false</code> en la API y reiníciala para permitir la creación.</p>}
        {!health.loading && !health.data?.available && <p className="muted">Abre Talend Studio con el Bridge activo y verifica la conexión MCP antes de iniciar.</p>}
        {batchState && batchState.status !== "not_started" && <div className={`talend-batch-state ${staleConflictResolved ? "preflight-ready" : batchState.status}`} role="status" aria-live="polite">
          <div className="talend-batch-state-heading"><strong>{staleConflictResolved ? "El conflicto anterior ya no está en Talend" : talendApplyBatchLabel(batchState.status)}</strong><span>{staleConflictResolved && preflight.data ? `${preflight.data.create_count} por crear · ${preflight.data.update_count} por actualizar · 0 conflictos actuales` : `${batchState.completed_jobs} / ${batchState.total_jobs} Jobs resueltos`}</span></div>
          {staleConflictResolved && preflight.data && <p>El portal actualizó la comprobación con el inventario de Studio ({preflight.data.inventory_count} Jobs). Al aplicar, creará los Jobs que faltan y actualizará los que ya estén en su carpeta destino.</p>}
          {batchActive && batchState.total_jobs > 0 && <div className="talend-batch-progress" role="progressbar" aria-label="Progreso de implementación del proyecto" aria-valuemin={0} aria-valuemax={batchState.total_jobs} aria-valuenow={batchState.completed_jobs}><span style={{ width: `${Math.round((batchState.completed_jobs / batchState.total_jobs) * 100)}%` }} /></div>}
          {batchActive && <p>{batchState.current_program ? <>MCP trabajando en <code>{batchState.current_program}</code></> : "El MCP está preparando el primer Job…"} Talend no ejecutará los Jobs.</p>}
          {!staleConflictResolved && batchState.error && <p className="error">{batchState.error}</p>}
          {batchState.warnings.map((warning, index) => <p className="notice warning" key={`batch-warning-${index}`}>{warning}</p>)}
          {!staleConflictResolved && batchState.jobs.length > 0 && <ArchivePathTree entries={batchState.jobs.map((job) => ({ path: job.program, value: job }))} renderEntry={({ path, value: job }) => <BatchJobRow key={path} projectId={id} path={path} job={job} />} />}
          {!staleConflictResolved && !batchActive && batchState.jobs.length > 0 && <p className="muted">El lote terminó. Revisa los resultados por programa; esta acción crea los Jobs pero no los ejecuta.</p>}
        </div>}
      </section> : null}
      {grid.data && <GridRecommendations id={id} items={grid.data} />}
      {q.error?.includes("generados") ? (
        <div className="notice"><Icon name="info" /><span>Todavía no hay planes en este proyecto. Pulsa «Generar planes de migración» para empezar.</span></div>
      ) : (
        <Load q={q}>
          {(rows) => (
          rows.length === 0 ? <div className="empty-state"><span className="empty-icon">🧭</span><h3>Primero analiza tus programas</h3><p>Cuando termine el análisis, aquí aparecerá una guía para cada job.</p><a className="button" href={link(id, "resumen")}>Ir al resumen <Icon name="arrow" size={17} /></a></div> : <ArchivePathTree entries={rows.map((row) => ({ path: row.program, value: row }))} renderEntry={({ path, value: row }) => (
              <article className="guide-job" key={path}><div className="guide-job-icon" aria-hidden="true">🔄</div><div className="guide-job-main"><h2>{row.job_name}</h2><p>Programa SAS: <code>{path}</code></p><div className="guide-job-meta"><span>{row.steps} pasos técnicos</span></div></div><a className="button" href={link(id, "planes", row.program)}>Abrir guía <Icon name="arrow" size={17} /></a></article>
            )} />
          )}
        </Load>
      )}
    </>
  );
}

function TalendPreflightPanel({ preflight }: { preflight: { data?: TalendApplyBatchPreflight; error?: string; loading: boolean; reload: () => void } }) {
  const report = preflight.data;
  return <section className={`talend-preflight ${preflight.error ? "error" : report?.conflict_count ? "conflict" : "ready"}`} aria-label="Comprobación del destino Talend" aria-live="polite">
    <div className="talend-preflight-heading">
      <div><strong>{preflight.loading ? "Comprobando el destino en Talend…" : preflight.error ? "No se pudo verificar el destino" : report ? "Destino comprobado en Talend" : "Esperando comprobación del destino"}</strong>
        {report && !preflight.error && <small>{report.create_count} se crearán · {report.update_count} se actualizarán · {report.conflict_count} conflictos · {report.inventory_count} Jobs revisados{report.checked_at ? ` · ${new Date(report.checked_at).toLocaleTimeString("es", { hour: "2-digit", minute: "2-digit" })}` : ""}</small>}
      </div>
      <button type="button" className="secondary" onClick={preflight.reload} disabled={preflight.loading}>Volver a comprobar</button>
    </div>
    {preflight.error && <p className="error" role="alert">No se iniciará ninguna escritura hasta verificar MCP y el inventario completo: {preflight.error}</p>}
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

function BatchJobRow({ projectId, path, job }: { projectId: string; path: string; job: TalendApplyBatchJob }) {
  const result = job.result;
  return <article className={`talend-batch-job ${job.status}`}>
    <div className="talend-batch-job-heading"><Icon name={job.status === "applied" ? "check" : job.status === "running" ? "flow" : job.status === "pending" ? "info" : "warning"} size={17} /><strong>{result?.identity.job_name ?? path}</strong><span>{talendApplyJobLabel(job.status)}</span></div>
    <p className="muted"><code>{path}</code>{result?.result.itemPath && <> · destino <code>{result.result.itemPath}</code></>}</p>
    {result && <p className="talend-batch-job-metrics">{result.result.generatedComponents ?? 0} componentes · {result.result.generatedConnections ?? 0} conexiones · {result.result.generatedContexts ?? 0} variables de contexto</p>}
    {job.error && <p className="error" role="alert">{job.error}</p>}
    {result && (result.warnings.length > 0 || result.blocked_steps.length > 0) && <details><summary>Información técnica pendiente</summary><ul>{result.warnings.map((warning, index) => <li key={`warning-${index}`}>{warning}</li>)}{result.blocked_steps.map((block) => <li key={block.step_id}><strong>{block.step_id === "job" ? "Job" : `Paso ${block.step_id}`}:</strong> {block.reason}</li>)}</ul></details>}
    <a className="talend-batch-job-link" href={link(projectId, "planes", path)}>Abrir guía</a>
  </article>;
}

function PlanDetail({ id, file }: { id: string; file: string }) {
  const q = useAsync(() => api.plan(id, file), [id, file]);
  const jobs = useAsync(() => api.plans(id), [id]);
  const health = useAsync(() => api.talendHealth(), [id]);
  const preview = useAsync(() => api.talendApplyPreview(id, file), [id, file]);
  const applyStatus = useAsync(() => api.talendApplyStatus(id, file), [id, file]);
  const batch = useAsync(() => api.talendApplyBatchStatus(id), [id], { preserveDataOnError: true });
  const jobIndex = jobs.data?.findIndex((item) => item.program === file) ?? -1;
  const previousJob = jobIndex > 0 ? jobs.data?.[jobIndex - 1] : undefined;
  const nextJob = jobIndex >= 0 ? jobs.data?.[jobIndex + 1] : undefined;
  const isApplyRunning = applyStatus.data?.status === "running";
  const isBatchRunning = batch.data?.status === "queued" || batch.data?.status === "running";
  const batchJob = batch.data?.jobs.find((item) => item.program === file);
  const latestResult = applyStatus.data?.result ?? batchJob?.result ?? undefined;
  useEffect(() => {
    if (!isApplyRunning && !isBatchRunning && !batch.error) return;
    const timer = window.setInterval(() => {
      if (isApplyRunning) applyStatus.reload();
      if (isBatchRunning || batch.error) batch.reload();
    }, 1200);
    return () => window.clearInterval(timer);
  }, [isApplyRunning, isBatchRunning, batch.error, applyStatus.reload, batch.reload]);
  return (
    <>
      <div className="guide-job-navigation"><a href={link(id, "planes")}>← Todas las guías</a><div><a className={previousJob ? "button secondary" : "button secondary disabled-link"} aria-disabled={!previousJob} href={previousJob ? link(id, "planes", previousJob.program) : undefined}>← Job anterior</a><a className={nextJob ? "button secondary" : "button secondary disabled-link"} aria-disabled={!nextJob} href={nextJob ? link(id, "planes", nextJob.program) : undefined}>Siguiente job →</a></div></div>
      <Load q={q}>
        {(p) => (
          <>
            <h1>{p.job_name}</h1>
            <p className="subtitle">El portal interpreta el programa SAS y el MCP construye el Job con la API de Talend Studio. El Job no se ejecutará.</p>
            <div className="guide-intro"><span aria-hidden="true">🧭</span><div><strong>Instrucciones de migración</strong><p>El plan incluye los pasos, propiedades sugeridas, expresiones, dependencias y evidencia del programa SAS.</p></div></div>
            <section className="talend-apply-panel" aria-labelledby="talend-apply-title">
              <div className="talend-apply-heading">
                <div><h2 id="talend-apply-title">Estado de este Job en Talend</h2><p>La implementación se inicia desde el botón único del proyecto. El portal envía al MCP las instrucciones de todos los flujos del ZIP en una sola operación por proyecto.</p></div>
                <span className={`talend-mcp-status ${health.data?.available ? health.data.write_enabled ? "online" : "readonly" : "offline"}`} role="status" aria-live="polite">
                  {health.loading ? "Consultando MCP…" : health.data?.available ? health.data.write_enabled ? "MCP y Bridge listos · escritura habilitada" : "MCP conectado · solo lectura" : health.data?.mcp_available ? "MCP conectado · Bridge sin conexión" : "MCP sin conexión"}
                </span>
              </div>
              {health.data?.error && <p className="error" role="alert">{health.data.error}</p>}
              {health.error && <p className="error" role="alert">{health.error}</p>}
              {batch.error && <p className="error" role="alert">No se pudo actualizar el progreso del lote: {batch.error}. Se volverá a intentar automáticamente.</p>}
              {preview.error && <p className="error" role="alert">No se pudo preparar el destino de Talend: {preview.error}</p>}
              <div className="talend-apply-destination"><span>Carpeta raíz configurada</span><code>{health.data?.apply_folder ?? "Process/PruebasWebSAS"}</code><span>Carpeta exacta para este Job</span><code>{preview.data?.identity.folder_path ?? applyStatus.data?.identity?.folder_path ?? "Calculando destino del proyecto…"}</code><small>La ruta incluye las subcarpetas del ZIP y el identificador único del proyecto.</small></div>
              {preview.data && <p className="talend-preview-counts">La guía enviará {preview.data.components?.length ?? 0} componentes · {preview.data.connections?.length ?? 0} conexiones · {preview.data.contexts?.length ?? 0} variables de contexto{preview.data.child_jobs?.length ? ` · ${preview.data.child_jobs.length} Jobs hijos` : ""}.</p>}
              {preview.data?.blocked_steps && preview.data.blocked_steps.length > 0 && <div className="talend-apply-blocked"><h3>Detalles que quedarán pendientes en el Job</h3><ul>{preview.data.blocked_steps.map((item) => <li key={item.step_id}><strong>{item.step_id}:</strong> {item.reason}</li>)}</ul></div>}
              {batchJob && <BatchJobRow projectId={id} path={file} job={batchJob} />}
              {!batchJob && applyStatus.data && <div className={`talend-persisted-status ${applyStatus.data.status}`} role="status" aria-live="polite">
                {isApplyRunning ? <span className="spinner" /> : <Icon name={applyStatus.data.status === "applied" ? "check" : applyStatus.data.status === "not_started" ? "info" : "warning"} size={17} />}
                <div><strong>{applyStatusLabel(applyStatus.data.status)}</strong>{applyStatus.data.updated_at && <small>Actualizado {new Date(applyStatus.data.updated_at).toLocaleString("es", { dateStyle: "medium", timeStyle: "short" })}</small>}{applyStatus.data.error && <span className="error">{applyStatus.data.error}</span>}</div>
              </div>}
              {isBatchRunning && <div className="talend-apply-progress" role="progressbar" aria-label="Implementación del proyecto en Talend" aria-valuetext={`${batch.data?.completed_jobs ?? 0} de ${batch.data?.total_jobs ?? 0} Jobs resueltos`}><span className="talend-apply-progress-bar" /><p>El MCP está implementando el proyecto. Talend no ejecutará los Jobs.</p></div>}
              {health.data?.available && !health.data.write_enabled && <p className="muted">La API está configurada en solo lectura; el botón de implementación del proyecto permanecerá deshabilitado.</p>}
              {latestResult && <div className={`talend-apply-outcome ${latestResult.status === "partially_applied" ? "partial" : "success"}`} aria-live="polite">
                <strong>{latestResult.status === "partially_applied" ? "Job creado parcialmente" : "Job creado en Talend"}</strong>
                <span><code>{latestResult.result.itemPath ?? latestResult.identity.job_name}</code></span>
                <span>{latestResult.result.generatedComponents ?? 0} componente(s) añadidos · {latestResult.result.reusedComponents ?? 0} ya existentes · {latestResult.result.generatedConnections ?? 0} conexiones añadidas · {latestResult.result.reusedConnections ?? 0} ya existentes · contextos: {latestResult.result.generatedContexts ?? 0} nuevos, {latestResult.result.updatedContexts ?? 0} actualizados, {latestResult.result.reusedContexts ?? 0} conservados, {latestResult.result.removedContexts ?? 0} marcadores vacíos obsoletos retirados</span>
                <span>Talend no ejecutará los Jobs.</span>
                {(latestResult.warnings.length > 0 || latestResult.blocked_steps.length > 0) && <div className="talend-apply-blocked"><h3>Información técnica pendiente</h3><ul>{latestResult.warnings.map((warning, index) => <li key={`warning-${index}`}>{warning}</li>)}{latestResult.blocked_steps.map((block) => <li key={block.step_id}><strong>{block.step_id === "job" ? "Job" : `Paso ${block.step_id}`}:</strong> {block.reason}</li>)}</ul></div>}
              </div>}
            </section>
            <p><strong>Programa de origen:</strong> <a href={link(id, "programas", p.program)}><code>{p.program}</code></a></p>
            {p.context_variables.length > 0 && (
              <>
                <h2>Variables de contexto</h2>
                <ul>{p.context_variables.map((c) => <li key={c.name}><code>{c.suggested}</code> ← {c.name} {c.sas_value && <>= <code>{c.sas_value}</code></>}</li>)}</ul>
              </>
            )}
            {p.libraries_needed.length > 0 && (
              <>
                <h2>Conexiones de datos requeridas</h2>
                <ul>{p.libraries_needed.map((l) => <li key={l.sas_name}><code>{l.sas_name}</code> ({l.engine ?? "BASE"}{l.path && `, ${l.path}`}) → {l.suggested_connection}</li>)}</ul>
              </>
            )}
            {p.orchestration.grid_recommendations.length > 0 && <GridRecommendations id={id} items={p.orchestration.grid_recommendations} />}
            {p.entry_macro && (
              <div className="guide-dependencies">
                <strong>Macro principal integrada en este Job</strong>
                <p><code>%{p.entry_macro.name}({p.entry_macro.params.join(", ")})</code> aporta los pasos que aparecen debajo. Sus parámetros se guardan como variables de contexto del Job.</p>
              </div>
            )}
            <h2>Instrucciones SAS <Badge>{p.steps.length + p.children.reduce((count, child) => count + child.steps.length, 0)}</Badge></h2>
            <div className="guide-steps">{orderSteps(p.steps).map((s) => <StepCard key={s.id} id={id} s={s} allSteps={p.steps} />)}</div>
            {p.children.map((c) => (
              <section key={c.name}>
                <h2>Definición de macro auxiliar %{c.name}({c.params.join(", ")})</h2>
                {orderSteps(c.steps).map((s) => <StepCard key={s.id} id={id} s={s} allSteps={c.steps} />)}
              </section>
            ))}
            {p.validation_cases.length > 0 && (
              <>
                <h2>Casos de validación</h2>
                <ul>{p.validation_cases.map((v) => <li key={v.id}><code>{v.id}</code> ({v.kind}): {v.description}</li>)}</ul>
              </>
            )}
            {p.unresolved.length > 0 && (
              <details><summary>Información técnica por resolver ({p.unresolved.length})</summary><ul>{p.unresolved.map((u, i) => <li key={i}>{u}</li>)}</ul></details>
            )}
          </>
        )}
      </Load>
    </>
  );
}
function GridRecommendations({ id, items }: { id: string; items: GridRecommendation[] }) {
  return (
    <section aria-label="Recomendaciones de SAS Grid">
      <h2>Grid y planificación ({items.length})</h2>
      {items.map((item) => (
        <article className="step" key={item.id}>
          <h3><code>{item.pattern_id}</code> <Badge tone={item.status === "unsupported" ? "bad" : "warn"}>{item.status}</Badge></h3>
          <p>{item.instruction}</p><p className="muted">{item.reason}</p>
          <p>
            {item.component_candidate && <><ComponentIcon name={item.component_candidate} /> <ComponentLink name={item.component_candidate} known /></>} {item.doc_url && <a href={item.doc_url} target="_blank" rel="noreferrer">Docs oficiales Talend</a>} {" "}
            <a href={api.sourceEvidence(id, item.evidence.file, item.evidence.line)} target="_blank" rel="noreferrer" aria-label={`Ver evidencia ${item.evidence.file}, línea ${item.evidence.line}`}>
              {item.evidence.file}:{item.evidence.line}
            </a>
          </p>
          {item.required.length > 0 && <><b>Datos requeridos</b><ul>{item.required.map((requirement) => <li key={requirement}>{requirement}</li>)}</ul></>}
          {item.dependencies.length > 0 && <p className="muted">Depende de: {item.dependencies.join(", ")}</p>}
          <details><summary>Datos interpretados</summary><pre className="doc">{JSON.stringify(item.details, null, 2)}</pre></details>
        </article>
      ))}
    </section>
  );
}

function applyStatusLabel(status: TalendApplyState["status"]): string {
  const labels: Record<TalendApplyState["status"], string> = {
    not_started: "Listo para implementar",
    running: "El MCP está creando el Job",
    applied: "Implementación completada",
    partially_applied: "Job creado con información pendiente",
    failed: "La implementación falló",
    conflict: "Destino con conflicto",
    interrupted: "Implementación interrumpida",
  };
  return labels[status];
}

function talendApplyBatchLabel(status: TalendApplyBatchState["status"]): string {
  const labels: Record<TalendApplyBatchState["status"], string> = {
    not_started: "Listo para implementar",
    queued: "Lote en cola",
    running: "El MCP está implementando los Jobs",
    applied: "Todos los Jobs se implementaron",
    partially_applied: "Lote terminado con resultados pendientes",
    failed: "La implementación del lote falló",
    conflict: "Conflicto de revisión o destino",
    interrupted: "Lote interrumpido; puedes reintentarlo",
  };
  return labels[status];
}

function talendApplyJobLabel(status: TalendApplyBatchJob["status"]): string {
  const labels: Record<TalendApplyBatchJob["status"], string> = {
    pending: "Pendiente",
    running: "Creando en Talend…",
    applied: "Creado",
    partially_applied: "Creado con información pendiente",
    failed: "Falló",
    conflict: "Conflicto",
    interrupted: "Interrumpido; puede reintentarse",
  };
  return labels[status];
}

function ComponentLink({ name, known }: { name: string; known?: boolean | null }) {
  const base = name.split(" ")[0];
  return known ? <a href={`#/catalogo/${base}`}><code>{name}</code></a> : <code>{name}</code>;
}

function jumpToStep(stepId: string) {
  document.getElementById(`step-${stepId}`)?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function StepCard({ id, s, allSteps }: { id: string; s: Step; allSteps: Step[] }) {
  const catalogName = s.component_candidate.split(" ")[0];
  const officialUrl = s.doc_url ?? catalogAudit.recommended_components[catalogName]?.official_url;
  const dependencies = s.connections.flatMap((connection) => {
    const source = connection.from_step ? allSteps.find((item) => item.id === connection.from_step) : undefined;
    return [{ connection, source }];
  });
  return (
    <article className="step guide-step" id={`step-${s.id}`}>
      <div className="guide-step-heading"><span className="guide-step-number">{s.order}</span><div><span className="eyebrow">HAZ ESTO EN TALEND</span><h3>{s.purpose}</h3></div></div>
      <p className="guide-component"><span>Componente sugerido</span><ComponentIcon name={catalogName} /><ComponentLink name={s.component_candidate} known={s.in_catalog} /> <Badge tone={s.in_catalog ? "ok" : "warn"}>{s.in_catalog ? "Candidato del catálogo" : "Candidato por revisar"}</Badge><Badge tone={s.verified ? "ok" : "warn"}>{s.verified ? "Cotejado con Talend MCP" : "No cotejado con Talend MCP"}</Badge></p>
      <div className="guide-links">{s.evidence?.file && <a href={`${link(id, "programas", s.evidence.file)}?line=${s.evidence.line}`}>🔎 Ver evidencia SAS · {s.evidence.file}:{s.evidence.line}</a>}{officialUrl ? <a href={officialUrl} target="_blank" rel="noreferrer">📘 Abrir documentación oficial ↗</a> : <span className="muted">📘 Fuente oficial pendiente de confirmar</span>}</div>
      <p className="muted">Subjob: {s.subjob} · confianza de la recomendación: {s.confidence}</p>
      {s.alternatives.length > 0 && <p className="muted">Alternativas: {s.alternatives.join(", ")}</p>}
      {s.variants && s.variants.length > 0 && <p className="muted">Variantes: {s.variants.slice(0, 8).join(", ")}</p>}
      {dependencies.length > 0 && <div className="guide-dependencies"><strong>Dependencias de este paso</strong><ul>{dependencies.map(({ connection, source }, index) => <li key={`${connection.type}-${source?.id ?? index}`}>{connection.type}{source ? <>: <button type="button" className="text-button guide-inline-link" onClick={() => jumpToStep(source.id)}>paso {source.order} · {source.component_candidate}</button></> : " (origen externo o no identificado en esta guía)"}</li>)}</ul></div>}
      {s.properties.length > 0 && (
        <div className="guide-properties"><strong>Campos y valores sugeridos</strong><div className="guide-property-list">{s.properties.map((p) => <div className="guide-property" key={p.name}><span>{p.label || p.name}{p.in_catalog === false && <small>Nombre pendiente de verificar</small>}</span><code>{p.value ?? "Por configurar"}</code></div>)}</div></div>
      )}
      {s.expressions.map((e, i) => (
        <p key={i}>
          SAS <code>{e.sas}</code> → {e.talend ? <code>{e.talend}</code> : <i>sin traducción automática</i>}
          {e.warnings.map((w, j) => <span key={j} className="warn-text"> ⚠ {w}</span>)}
        </p>
      ))}
      {s.pending.length > 0 && <div className="guide-pending"><strong>⏳ Información técnica pendiente</strong><ul>{s.pending.map((x, i) => <li key={i}>{x}</li>)}</ul></div>}
      {s.assumptions.length > 0 && <p className="muted">Supuestos: {s.assumptions.join("; ")}</p>}
    </article>
  );
}
