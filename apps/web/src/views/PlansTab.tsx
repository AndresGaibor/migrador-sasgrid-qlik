import { useEffect, useRef, useState } from "react";
import type { MouseEvent } from "react";
import { Icon } from "../components/Icon";
import { api, ApiError } from "../api";
import { formatErrorMessage, notifyError, notifySuccess } from "../errors";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { GridRecommendation, JobPlan, PlanRow, Step, TalendApplyBatchJob, TalendApplyBatchPreflight, TalendApplyBatchState, TalendApplyBatchSummary, TalendApplyState } from "../types";
import { Badge, Load, link } from "./common";
import { orderSteps } from "../guided";
import { buildGridGuides } from "../grid-guide";
import { PlanPreparation } from "./plans/PlanPreparation";
import { decodeProgress, encodeProgress, isUncertainStep, storageStatus, type GuideProgress } from "../guide-progress";
import { StepDecisionDialogs, StepInstructions, StepProgressEditor } from "./plans/PlanStepParts";
import { PlanListContent } from "./plans/PlanListContent";
import { ArchivePathTree } from "../components/ArchivePathTree";
import { Dialog } from "../components/Dialog";
import { TalendPreflight } from "./plans/TalendPreflight";

export function PlansTab({ id, file }: { id: string; file?: string }) {
  return file ? <PlanDetail key={`${id}:${decodeURI(file)}`} id={id} file={decodeURI(file)} /> : <PlanList id={id} />;
}

// Los ZIP de Mac traen basura «__MACOSX»; se oculta aunque venga de proyectos ya importados.
const real = (rows: PlanRow[]) => rows.filter((r) => !r.program.includes("__MACOSX/"));
const PARENT_PATTERN = /include_dispatch|sysin|submit/;
function useDesktopLayout() {
  const [isDesktop, setIsDesktop] = useState(() => window.matchMedia("(min-width: 601px)").matches);
  useEffect(() => {
    const desktop = window.matchMedia("(min-width: 601px)");
    const update = () => setIsDesktop(desktop.matches);
    desktop.addEventListener("change", update);
    return () => desktop.removeEventListener("change", update);
  }, []);
  return isDesktop;
}

function visible(rows: PlanRow[], programOrder?: string[]) {
  const todo = real(rows).filter((row) => row.steps > 0);
  if (!programOrder) return todo;
  const rank = new Map(programOrder.map((program, index) => [program, index]));
  return todo.sort((a, b) => (rank.get(a.program) ?? programOrder.length) - (rank.get(b.program) ?? programOrder.length));
}

function PlanList({ id }: { id: string }) {
  const q = useAsync(() => api.plans(id), [id]);
  const grid = useAsync(() => api.gridRecommendations(id), [id]);
  const health = useAsync(() => api.talendHealth(), [id]);
  const batch = useAsync(() => api.talendApplyBatchStatus(id), [id], { preserveDataOnError: true });
  const preflight = useAsync(() => api.talendApplyBatchPreflight(id), [id, q.data?.length ?? 0], { preserveDataOnError: true });
  const summary = useAsync(() => api.talendApplyBatchSummary(id), [id]);
  const isDesktop = useDesktopLayout();
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const [batchBusy, setBatchBusy] = useState(false);
  const [batchError, setBatchError] = useState<string>();
  const [confirmation, setConfirmation] = useState<TalendApplyBatchSummary>();
  const batchState = batch.data;
  const batchActive = batchState?.status === "queued" || batchState?.status === "running";
  const preflightReady = Boolean(!preflight.loading && !preflight.error && preflight.data?.available && preflight.data.conflict_count === 0);
  const staleConflictResolved = Boolean(batchState?.status === "conflict" && preflightReady);
  const missingJobCount = preflight.data?.create_count ?? 0;
  const batchFinished = (batchState?.status === "applied" && missingJobCount === 0) || (batchState?.status === "conflict" && !preflightReady);
  const canStartBatch = Boolean(q.data?.length && summary.data?.creatable_jobs && !summary.loading && !summary.error && preflightReady && batch.data && !batch.error && health.data?.available && health.data.spec_supported === true && health.data.write_enabled && !health.loading && !busy && !batchBusy && !batchActive && !batchFinished);
  const gridGuides = grid.data && <GridRecommendations id={id} items={grid.data} isDesktop={isDesktop} staged />;
  const planContent = q.error?.includes("generados") ? (
    <div className="notice"><Icon name="info" /><span>Todavía no hay guías preparadas para este proyecto. Usa «Preparar guías de migración» para empezar.</span></div>
  ) : (
    <Load q={q}>
      {(all) => { const rows = real(all); return <PlanListContent id={id} rows={rows} groups={[{ title: summary.data ? "Orden de revisión por dependencias" : "Guías del proyecto", hint: summary.data ? "El mismo orden de dependencias que utiliza la creación en Studio. Los ciclos requieren revisión manual; este listado no programa la ejecución." : "Orden de dependencias no disponible. Puedes revisar las guías; confirma las dependencias antes de ejecutar los Jobs.", rows: visible(rows, summary.data?.programs.map((job) => job.program)) }]} isDesktop={isDesktop} orderVerified={Boolean(summary.data)} />; }}
    </Load>
  );
  useEffect(() => {
    if (!batchActive && !batch.error) return;
    const timer = window.setInterval(batch.reload, 1200);
    return () => window.clearInterval(timer);
  }, [batchActive, batch.error, batch.reload]);
  useEffect(() => {
    if (batchState && ["applied", "partially_applied", "failed", "conflict"].includes(batchState.status)) preflight.reload();
  }, [batchState?.status, preflight.reload]);
  useEffect(() => {
    if (batchState && (batchState.completed_jobs > 0 || ["applied", "partially_applied", "failed", "conflict"].includes(batchState.status))) q.reload();
  }, [batchState?.status, batchState?.completed_jobs, q.reload]);
  useEffect(() => {
    if (batchState && ["applied", "partially_applied", "failed", "conflict"].includes(batchState.status)) summary.reload();
  }, [batchState?.status, summary.reload]);
  const gen = async () => {
    setBusy(true);
    setErr(undefined);
    try {
      const result = await api.generatePlans(id);
      notifySuccess("Guías preparadas", `${result.plans} guías listas para revisar.`);
      q.reload();
      grid.reload();
      preflight.reload();
      summary.reload();
    } catch (x) {
      setErr(notifyError(x, "No se pudieron preparar las guías"));
    } finally {
      setBusy(false);
    }
  };
  const implementProject = async () => {
    if (!confirmation || !canStartBatch) return;
    setBatchBusy(true);
    setBatchError(undefined);
    try {
      await api.talendApplyBatch(id, confirmation.revision_hash);
      setConfirmation(undefined);
      notifySuccess("Creación iniciada", "El MCP creará la estructura de los Jobs; no los ejecutará.");
      batch.reload();
    } catch (x) {
      setBatchError(notifyError(x, "No se pudo iniciar la creación en Talend Studio"));
      preflight.reload();
      if (x instanceof ApiError && x.status === 409) {
        setConfirmation(undefined);
        summary.reload();
        batch.reload();
      }
    } finally {
      setBatchBusy(false);
    }
  };
  return (
    <>
      <div className="migration-heading"><div><h1>Plan de migración</h1><p className="subtitle">Primero crea la estructura, después completa los Jobs y al final programa su ejecución.</p></div>
      <div className="plan-rebuild-toolbar"><button type="button" className={q.data?.length ? "secondary" : undefined} onClick={gen} disabled={busy || batchActive || batchBusy || Boolean(confirmation)} title="Tu progreso se conserva al volver a preparar las guías"><Icon name="play" size={16} />{busy ? "Preparando guías…" : q.data?.length ? "Actualizar guías" : "Preparar guías de migración"}</button><small>Tu progreso se conserva.</small></div></div>
      {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
      <div className="migration-workspace">
      {q.data?.length ? <section className="talend-batch-panel" aria-labelledby="talend-batch-title">
        <div className="talend-batch-heading"><div><h2 id="talend-batch-title">1. Crea la estructura de los Jobs</h2><p>El MCP crea componentes y conexiones en Talend Studio; no se ejecutan ni se publican en Qlik Talend Cloud.</p></div>
          <span className={`talend-mcp-status ${health.loading ? "readonly" : health.data?.available ? health.data.write_enabled ? "online" : "readonly" : "offline"}`} role="status" aria-live="polite">{health.loading ? "Consultando MCP…" : health.data?.available ? health.data.write_enabled ? "MCP y Bridge listos" : "MCP en solo lectura" : health.data?.mcp_available ? "Bridge sin conexión" : "MCP sin conexión"}</span>
        </div>
        <TalendPreflightPanel preflight={preflight} />
        {summary.loading ? <p className="muted" role="status">Preparando vista previa del proyecto…</p> : summary.data ? <TalendPreflight id={id} summary={summary.data} /> : <div className="preflight-unavailable" role="alert"><p>No se pudo preparar la vista previa: {formatErrorMessage(summary.error, undefined, summary.errorStatus)}</p><button type="button" className="secondary" onClick={summary.reload}>Reintentar vista previa</button></div>}
        <button type="button" className="talend-implement-button talend-batch-button" onClick={() => { setBatchError(undefined); setConfirmation(summary.data); }} disabled={!canStartBatch}>
          <Icon name="flow" size={20} />{batchBusy || batchActive ? "Creando Jobs en Talend Studio…" : preflight.loading ? "Comprobando destino…" : preflight.error ? "Destino sin verificar" : preflight.data?.conflict_count ? "Resolver conflictos de destino" : batchState?.status === "applied" && missingJobCount > 0 ? "Recrear Jobs faltantes" : staleConflictResolved ? "Aplicar según inventario actual" : batchState?.status === "applied" ? "Estructura creada; continúa con las guías" : batchState && ["failed", "partially_applied", "interrupted"].includes(batchState.status) ? "Revisar reintento de Jobs" : "Revisar creación en Studio"}
        </button>
        <p className="muted talend-batch-followup">Después de crear la estructura, continúa con el paso 2. Para construirla manualmente, empieza directamente por sus guías.</p>
        {health.data?.error && <p className="error" role="alert">{formatErrorMessage(health.data.error)}</p>}
        {health.error && <p className="error" role="alert">{formatErrorMessage(health.error, undefined, health.errorStatus)}</p>}
        {batchError && <p className="error" role="alert">{batchError}</p>}
        {batch.error && <p className="error" role="alert">No se pudo actualizar el progreso del lote: {formatErrorMessage(batch.error, undefined, batch.errorStatus)} Se volverá a intentar automáticamente.</p>}
        {health.data?.available && !health.data.write_enabled && <p className="muted">Activa la escritura en <a href="#/settings">Configuración</a> para permitir la creación.</p>}
        {health.data?.available && health.data.spec_supported !== true && <p className="error" role="alert">{health.data.spec_error ?? "No se pudo comprobar la compatibilidad del contrato MCP."} <a href="#/settings">Revisar Configuración</a></p>}
        {!health.loading && !health.data?.available && <div className="preflight-unavailable"><p>Abre Talend Studio con el Bridge activo. Puedes continuar con las guías sin conexión.</p><button type="button" className="secondary" onClick={health.reload}>Comprobar conexión</button><a href="#/settings">Diagnóstico MCP</a></div>}
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
      <section className="migration-guides" aria-labelledby="migration-guides-title"><h2 id="migration-guides-title">2. Completa y prueba los Jobs</h2><p className="migration-stage-description">Revisa cada Job y marca los pasos terminados. Si usaste MCP, completa los pendientes sin volver a crear lo que ya existe.</p>{planContent}</section>
      <div className="migration-reference">{gridGuides}</div>
      </div>
      {confirmation && <Dialog title="Confirmar creación en Talend Studio" onClose={() => { if (!batchBusy) setConfirmation(undefined); }}>
        <p>Se creará o reutilizará la estructura de los Jobs en la carpeta de este proyecto. No se ejecutarán ni se publicarán Jobs.</p>
        <TalendPreflight id={id} summary={confirmation} />
        {batchError && <p className="error" role="alert">{batchError}</p>}
        <div className="dialog-actions"><button type="button" className="secondary" disabled={batchBusy} onClick={() => setConfirmation(undefined)}>Cancelar</button><button type="button" disabled={!canStartBatch} onClick={() => void implementProject()}>{batchBusy ? "Iniciando…" : "Crear Jobs en Talend Studio"}</button></div>
      </Dialog>}
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

function PlanDetail({ id, file }: { id: string; file: string }) {
  const isDesktop = useDesktopLayout();
  const q = useAsync(() => api.plan(id, file), [id, file]);
  const jobs = useAsync(() => api.plans(id), [id]);
  const gridQ = useAsync(() => api.gridRecommendations(id), [id]);
  const summary = useAsync(() => api.talendApplyBatchSummary(id), [id]);
  const ordered = visible(jobs.data ?? [], summary.data?.programs.map((job) => job.program));
  const ownGrid = (gridQ.data ?? []).filter((g) => g.evidence.file === file);
  const [override, setOverride] = useState<JobPlan>();
  const [saving, setSaving] = useState(false);
  const [navigationWarning, setNavigationWarning] = useState(false);
  const [verifyBusy, setVerifyBusy] = useState(false);
  const [verifyError, setVerifyError] = useState<string>();
  const saveFailed = useRef(false);
  const pendingSaves = useRef(0);
  const saveQueue = useRef<Promise<void>>(Promise.resolve());
  const plan = override ?? q.data;
  const health = useAsync(() => api.talendHealth(), [id]);
  const preview = useAsync(() => api.talendApplyPreview(id, file), [id, file]);
  const applyStatus = useAsync(() => api.talendApplyStatus(id, file), [id, file]);
  const batch = useAsync(() => api.talendApplyBatchStatus(id), [id], { preserveDataOnError: true });
  const isApplyRunning = applyStatus.data?.status === "running";
  const isBatchRunning = batch.data?.status === "queued" || batch.data?.status === "running";
  const batchJob = batch.data?.jobs.find((item) => item.program === file);
  const latestResult = applyStatus.data?.result ?? batchJob?.result ?? undefined;
  const verifyStudio = async () => {
    setVerifyBusy(true);
    setVerifyError(undefined);
    try {
      await api.talendApplyVerify(id, file);
      applyStatus.reload();
      q.reload();
      jobs.reload();
      batch.reload();
      notifySuccess("Comprobación actualizada", "Los pasos se contrastaron de nuevo con lo que Studio puede leer.");
    } catch (error) {
      setVerifyError(notifyError(error, "No se pudo comprobar el Job en Studio"));
    } finally {
      setVerifyBusy(false);
    }
  };
  useEffect(() => {
    if (!isApplyRunning && !isBatchRunning && !batch.error) return;
    const timer = window.setInterval(() => {
      if (isApplyRunning) applyStatus.reload();
      if (isBatchRunning || batch.error) batch.reload();
    }, 1200);
    return () => window.clearInterval(timer);
  }, [isApplyRunning, isBatchRunning, batch.error, applyStatus.reload, batch.reload]);
  useEffect(() => {
    if (batch.data?.completed_jobs) q.reload();
  }, [batch.data?.completed_jobs, q.reload]);
  useEffect(() => {
    if (applyStatus.data?.result?.verification) q.reload();
  }, [applyStatus.data?.result?.verification?.configured_steps, applyStatus.data?.result?.verification?.pending_steps, q.reload]);
  const decide = async (s: Step, progress: GuideProgress, note: string, blockReason: string) => {
    const savedNote = encodeProgress(progress, note, blockReason);
    if (savedNote === null) throw new Error("Escribe el motivo para poder marcar el paso como bloqueado.");
    pendingSaves.current += 1;
    setSaving(true);
    const operation = saveQueue.current.then(async () => { setOverride(await api.decide(id, file, s.id, storageStatus(progress), savedNote)); });
    void operation.then(() => { saveFailed.current = false; }, () => { saveFailed.current = true; setNavigationWarning(true); });
    saveQueue.current = operation.catch(() => undefined);
    try { await operation; }
    finally { pendingSaves.current -= 1; setSaving(pendingSaves.current > 0); }
  };
  const jobIndex = ordered.findIndex((item) => item.program === file);
  const previousJob = jobIndex > 0 ? ordered[jobIndex - 1] : undefined;
  const nextJob = jobIndex >= 0 ? ordered[jobIndex + 1] : undefined;
  const navigateAfterSave = (event: MouseEvent<HTMLAnchorElement>, destination: string) => {
    event.preventDefault();
    void saveQueue.current.then(() => {
      if (saveFailed.current) return;
      setNavigationWarning(false);
      window.location.hash = encodeURI(destination.slice(1));
    });
  };
  return (
    <>
      {navigationWarning && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>No pudimos guardar el último cambio. Permaneces en esta guía; vuelve a guardar el estado o la nota antes de cambiar de job.</span></div>}
      <div className="guide-job-navigation"><a className="button secondary" aria-disabled={saving} href={saving ? undefined : link(id, "planes")} onClick={(event) => navigateAfterSave(event, link(id, "planes"))}>{saving ? "Guardando progreso…" : "Todas las guías"}</a><div><a className={previousJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!previousJob || saving} href={previousJob && !saving ? link(id, "planes", previousJob.program) : undefined} onClick={(event) => previousJob && navigateAfterSave(event, link(id, "planes", previousJob.program))}>Job anterior</a><a className={nextJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!nextJob || saving} href={nextJob && !saving ? link(id, "planes", nextJob.program) : undefined} onClick={(event) => nextJob && navigateAfterSave(event, link(id, "planes", nextJob.program))}>Siguiente job</a></div></div>
      <Load q={{ ...q, data: plan }}>
        {(p) => (
          <>
            <h1>{p.job_name}</h1>
            <p className="subtitle">Sigue las tarjetas en orden para configurar cada componente; el estado muestra el avance general del componente.</p>
            <section className="talend-apply-panel" aria-label="Estado de implementación en Talend">
              <div className="talend-apply-heading"><div><h2>Creación en Talend Studio</h2><p>El MCP crea la estructura del Job; no lo ejecuta ni lo publica en Qlik Talend Cloud.</p></div><span className={`talend-mcp-status ${health.data?.available ? health.data.write_enabled ? "online" : "readonly" : "offline"}`} role="status">{health.loading ? "Consultando MCP…" : health.data?.available ? health.data.write_enabled ? "MCP listo" : "Solo lectura" : "MCP sin conexión"}</span></div>
              {health.error && <p className="error" role="alert">{formatErrorMessage(health.error, undefined, health.errorStatus)}</p>}
              {preview.error && <p className="error" role="alert">No se pudo preparar el destino: {formatErrorMessage(preview.error, undefined, preview.errorStatus)}</p>}
              {preview.data && <p className="muted">Destino: <code>{preview.data.identity.folder_path}</code> · {preview.data.components?.length ?? 0} componentes · {preview.data.connections?.length ?? 0} conexiones.</p>}
              {batchJob ? <BatchJobRow projectId={id} path={file} job={batchJob} /> : applyStatus.data && <p className="talend-persisted-status" role="status"><Icon name={isApplyRunning ? "flow" : applyStatus.data.status === "applied" ? "check" : "info"} size={17} /> {applyStatusLabel(applyStatus.data.status)}{applyStatus.data.error && `: ${formatErrorMessage(applyStatus.data.error)}`}</p>}
              {latestResult && <p className="muted">{latestResult.result.generatedComponents ?? 0} componentes · {latestResult.result.generatedConnections ?? 0} conexiones. {latestResult.warnings[0] ?? latestResult.blocked_steps[0]?.reason ?? ""}</p>}
              {latestResult && <div className="studio-verification-actions"><button type="button" className="secondary" onClick={() => void verifyStudio()} disabled={verifyBusy || isApplyRunning || isBatchRunning}>{verifyBusy ? "Comprobando en Studio…" : "Volver a comprobar pasos en Studio"}</button>{latestResult.verification && <span role="status">{latestResult.verification.configured_steps ?? 0} verificados · {latestResult.verification.pending_steps ?? 0} pendientes</span>}</div>}
              {verifyError && <p className="error" role="alert">{verifyError}</p>}
            </section>
            <p><strong>Programa SAS de origen:</strong> <a href={link(id, "programas", p.program)}><code>{p.program}</code></a></p>
            <PlanPreparation plan={p} />
            {ownGrid.length > 0 && <GridRecommendations id={id} items={ownGrid} isDesktop={isDesktop} />}
            <h2>{ownGrid.some((g) => PARENT_PATTERN.test(g.pattern_id)) ? "Después: el resto del programa" : "Construye el Job"}</h2>
            <StepGroups id={id} steps={p.steps} onDecide={decide} />
            {p.children.map((c) => (
              <section key={c.name}>
                <h2>Crea también un Job aparte para la macro %{c.name}</h2><p className="muted">Nombre sugerido: <code>job_{c.name.toLowerCase()}</code>{c.params.length > 0 && <> · parámetros que recibe: {c.params.map((x) => <code key={x}> {x}</code>)}</>}. Sus pasos son estos:</p>
                <StepGroups id={id} steps={c.steps} onDecide={decide} />
              </section>
            ))}
            {p.validation_cases.length > 0 && (
              <details><summary>Casos de validación ({p.validation_cases.length})</summary><ul>{p.validation_cases.map((v) => <li key={v.id}>{v.description} <span className="muted">· {v.id}</span></li>)}</ul></details>
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
export function GridRecommendations({ id, items, isDesktop, staged = false }: { id: string; items: GridRecommendation[]; isDesktop: boolean; staged?: boolean }) {
  const guides = buildGridGuides(items);
  return (
    <section className="orchestration-guides" aria-label="Orquestación y planificación">
      <h2>{staged ? "3. Conecta los Jobs y programa su ejecución" : "Dependencias y programación"}</h2>
      <p className="migration-stage-description">{staged ? "Hazlo después de completar y probar los Jobs del paso 2. " : "Primero completa y prueba los Jobs hijos. "}Revisa los Jobs principales que llaman a otros; después configura el calendario en Qlik Talend Cloud.</p>
      <p className="orchestration-reuse-note"><Icon name="info" size={17} /><span>Si MCP ya creó un Job principal y sus conexiones, verifica esa estructura en Studio; no la crees otra vez. Las instrucciones siguientes también sirven para construirla manualmente.</span></p>
      {guides.map((g, gi) => (
        <details className="panel plan-orchestration-card" key={g.key} open={!isDesktop && gi === 0}>
          <summary><span className="orchestration-summary"><b>{g.title}</b><small>{g.actions.length} pasos</small></span> <Badge tone={g.kind === "manual" ? "warn" : "ok"}>{g.kind === "build" ? "Talend Studio" : g.kind === "cloud" ? "Qlik Talend Cloud" : "Validar con Operaciones"}</Badge></summary>
          <div className="orchestration-intro"><p>{g.intro}</p><div>{g.component && <span className="orchestration-component"><ComponentIcon name={g.component} /> <ComponentLink name={g.component} known /></span>} {g.doc_url && <a href={g.doc_url} target="_blank" rel="noreferrer">Documentación oficial <Icon name="external" size={13} /></a>}</div></div>
          <ol className="orchestration-steps">
            {g.actions.map((a, n) => (
              <li key={n}>
                <div className="orchestration-step-heading"><span className="orchestration-step-number" aria-hidden="true">{n + 1}</span><h3>{a.text.replace(/^Paso \d+: /, "")}</h3></div>
                <div className="orchestration-step-body">
                {a.where && <div className="orchestration-location"><strong>Dónde</strong><p>{a.where}</p></div>}
                {a.fields && <dl className="orchestration-fields">{a.fields.map(([k, v], index) => <div key={`${k}:${index}`}><dt>{k}</dt><dd><code>{v}</code></dd></div>)}</dl>}
                {a.note && <p className="orchestration-note"><Icon name="info" size={16} /><span>{a.note}</span></p>}
                {a.doc_url && <p className="guide-official-link"><a href={a.doc_url} target="_blank" rel="noreferrer">Consultar documentación de este paso <Icon name="external" size={13} /></a></p>}
                </div>
              </li>
            ))}
          </ol>
          <details className="orchestration-sources"><summary>Referencias en el SAS ({g.sources.length})</summary><ul>{g.sources.map((r) => <li key={r.id}><a href={api.sourceEvidence(id, r.evidence.file, r.evidence.line)} target="_blank" rel="noreferrer">{r.evidence.file.split("/").pop()} · línea {r.evidence.line}</a></li>)}</ul></details>
        </details>
      ))}
    </section>
  );
}

function applyStatusLabel(status: TalendApplyState["status"]): string {
  const labels: Record<TalendApplyState["status"], string> = {
    not_started: "Listo para crear el Job",
    running: "El MCP está creando el Job en Talend Studio",
    applied: "Job creado en Talend Studio",
    partially_applied: "Job creado con información pendiente",
    failed: "No se pudo crear el Job",
    conflict: "Destino con conflicto",
    interrupted: "Creación interrumpida",
  };
  return labels[status];
}

function talendApplyBatchLabel(status: TalendApplyBatchState["status"]): string {
  const labels: Record<TalendApplyBatchState["status"], string> = {
    not_started: "Listo para crear Jobs en Talend Studio",
    queued: "Creación en cola",
    running: "El MCP está creando Jobs en Talend Studio",
    applied: "Jobs creados en Talend Studio",
    partially_applied: "Jobs creados con información pendiente",
    failed: "No se pudieron crear los Jobs",
    conflict: "Conflicto de revisión o destino",
    interrupted: "Creación interrumpida; puedes reintentar",
  };
  return labels[status];
}

function talendApplyJobLabel(status: TalendApplyBatchJob["status"]): string {
  const labels: Record<TalendApplyBatchJob["status"], string> = {
    pending: "Pendiente",
    running: "Creando en Talend Studio…",
    applied: "Job creado",
    partially_applied: "Job creado con pendientes",
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

type Decide = (s: Step, progress: GuideProgress, note: string, blockReason: string) => Promise<void>;

// Los pasos que comparten «subjob» salen de un mismo bloque del SAS (un DATA o PROC): se construyen juntos.
function StepGroups({ id, steps, onDecide }: { id: string; steps: Step[]; onDecide: Decide }) {
  const ordered = orderSteps(steps);
  const groups: Step[][] = [];
  for (const st of ordered) {
    const last = groups[groups.length - 1];
    if (last && last[0].subjob === st.subjob) last.push(st); else groups.push([st]);
  }
  const isDone = (st: Step) => decodeProgress(st.status, st.note).state === "completed";
  const firstOpen = groups.findIndex((g) => !g.every(isDone));
  return (
    <div className="guide-steps">
      {groups.map((g, gi) => {
        const reads = g.filter((x) => x.purpose.startsWith("Leer ")).map((x) => x.purpose.slice(5));
        const writes = g.filter((x) => x.purpose.startsWith("Escribir ")).map((x) => x.purpose.slice(9).replace(/ \(reemplaza\)/, ""));
        const title = reads.length || writes.length ? `${reads.join(" + ") || "datos"} → ${writes.join(" + ") || "resultado"}` : g[0].purpose;
        const done = g.filter(isDone).length;
        const cards = <>{g.length > 1 && <p className="muted">Estos {g.length} pasos van en el mismo lienzo, uno detrás de otro. Conéctalos como indica cada paso.</p>}{g.map((st) => <StepCard key={st.id} id={id} s={st} allSteps={ordered} previous={ordered[ordered.indexOf(st) - 1]} onDecide={onDecide} />)}</>;
        // Con un solo bloque el desplegable sólo repite el título del paso: se muestran los pasos directamente.
        if (groups.length === 1) return <div key={g[0].id}>{cards}</div>;
        return (
          <details className="panel step-group" key={g[0].id} open={gi === firstOpen}>
            <summary><b>Bloque {gi + 1} · {title}</b> <Badge tone={done === g.length ? "ok" : undefined}>{done === g.length ? "Terminado" : `${done} de ${g.length}`}</Badge></summary>
            {cards}
          </details>
        );
      })}
    </div>
  );
}

function jumpToStep(stepId: string) {
  const el = document.getElementById(`step-${stepId}`);
  el?.closest("details")?.setAttribute("open", "");
  el?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function StepCard({ id, s, allSteps, previous, onDecide }: { id: string; s: Step; allSteps: Step[]; previous?: Step; onDecide: Decide }) {
  const saved = decodeProgress(s.status, s.note);
  const [progress, setProgress] = useState<GuideProgress>(saved.state);
  const [note, setNote] = useState(saved.note);
  const [blockReason, setBlockReason] = useState(saved.blockReason);
  const [dialog, setDialog] = useState<"blocked" | "confirm" | null>(null);
  const [confirmed, setConfirmed] = useState(false);
  const [err, setErr] = useState<string>();
  useEffect(() => { const current = decodeProgress(s.status, s.note); setProgress(current.state); setNote(current.note); setBlockReason(current.blockReason); }, [s.status, s.note]);
  const save = (next: GuideProgress) => onDecide(s, next, note, blockReason).then(() => { setProgress(next); setDialog(null); setConfirmed(false); setErr(undefined); }).catch((error: unknown) => setErr(notifyError(error, "No se pudo guardar el avance")));
  const chooseProgress = (value: GuideProgress) => {
    if (value === "blocked") { setDialog("blocked"); return; }
    if (value === "completed" && isUncertainStep(s)) { setConfirmed(false); setDialog("confirm"); return; }
    void save(value);
  };
  const officialUrl = s.doc_url;
  const studioCheck = s.studio_verification;
  const studioUniqueName = studioCheck?.studio_unique_name ?? studioCheck?.talend_unique_name;
  return <article className="guide-step" id={`step-${s.id}`}>
    <div className="guide-step-heading"><div className="step-head"><h3>{s.purpose}</h3><span className="step-component">Componente: <code>{s.component_candidate}</code></span></div></div>
    {studioCheck && <div className={`studio-step-verification ${studioCheck.status}`} role="status"><Badge tone={studioCheck.status === "verified" ? "ok" : "warn"}>{studioCheck.status === "verified" ? "Configurado en Studio" : studioCheck.status === "unavailable" ? "Studio no disponible" : "Pendiente de configuración"}</Badge>{studioUniqueName && <code>{studioUniqueName}</code>}{studioCheck.checked_at && <small>Lectura de Studio: {new Date(studioCheck.checked_at).toLocaleString("es")}</small>}{studioCheck.reason && <span>{studioCheck.reason}</span>}{Object.keys(studioCheck.checks).length > 0 && <details><summary>Verificación automática</summary><ul>{Object.entries(studioCheck.checks).map(([name, check]) => <li key={name}><strong>{verificationCheckLabel(name)}:</strong> {verificationStatusLabel(check.status)}{check.reason ? ` · ${check.reason}` : ""}</li>)}</ul></details>}</div>}
    <StepInstructions id={id} step={s} allSteps={allSteps} officialUrl={officialUrl} />
    <StepProgressEditor progress={progress} note={note} blockReason={blockReason} previous={previous} error={err} onProgress={chooseProgress} onNoteChange={setNote} onNoteBlur={() => note !== saved.note && void save(progress)} onEditBlock={() => setDialog("blocked")} onJumpPrevious={(step) => jumpToStep(step.id)} />
    <StepDecisionDialogs step={s} dialog={dialog} setDialog={setDialog} confirmed={confirmed} setConfirmed={setConfirmed} blockReason={blockReason} setBlockReason={setBlockReason} onSave={(state) => void save(state)} />
  </article>;
}

function verificationCheckLabel(name: string): string {
  const labels: Record<string, string> = { component: "Componente", parameters: "Parámetros", schema: "Esquema", mapper: "Mapper", connections: "Conexiones" };
  return labels[name] ?? name;
}

function verificationStatusLabel(status: string): string {
  return status === "verified" ? "confirmado" : status === "not_required" ? "no aplica" : status === "unavailable" ? "no disponible" : "pendiente";
}
