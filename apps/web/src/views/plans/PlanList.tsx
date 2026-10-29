import { useEffect, useState } from "react";
import { Icon } from "../../components/Icon";
import { api, ApiError } from "../../api";
import { formatErrorMessage, notifyError, notifySuccess } from "../../errors";
import { useAsync } from "../../hooks";
import { ArchivePathTree } from "../../components/ArchivePathTree";
import type { TalendApplyBatchSummary } from "../../types";
import { Load } from "../common";
import { Dialog } from "../../components/Dialog";
import { TalendPreflight } from "./TalendPreflight";
import { BulkRename } from "./BulkRename";
import { PlanListContent } from "./PlanListContent";
import { GridRecommendations } from "./PlanGrid";
import { BatchJobRow, TalendPreflightPanel } from "./PlanBatchPanel";
import { real, useDesktopLayout, visible } from "./plan-rows";
import { talendApplyBatchLabel } from "./plan-status";
import { useProjectEvents } from "../../project-events";

export function PlanList({ id }: { id: string }) {
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
  const [showBulkRename, setShowBulkRename] = useState(false);
  const [renameWarnings, setRenameWarnings] = useState<string[]>([]);
  const batchState = batch.data;
  const batchActive = batchState?.status === "queued" || batchState?.status === "running";
  const events = useProjectEvents(id, batch.reload);
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
    if (events.connected || (!batchActive && !batch.error)) return;
    const timer = window.setInterval(batch.reload, 1200);
    return () => window.clearInterval(timer);
  }, [batchActive, batch.error, batch.reload, events.connected]);
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
      <div className="plan-rebuild-toolbar">{q.data?.length ? <button type="button" className="secondary" onClick={() => setShowBulkRename(true)} disabled={batchActive || batchBusy || busy || Boolean(confirmation)}>Renombrar Jobs</button> : null}<button type="button" className={q.data?.length ? "secondary" : undefined} onClick={gen} disabled={busy || batchActive || batchBusy || Boolean(confirmation)} title="Tu progreso se conserva al volver a preparar las guías"><Icon name="play" size={16} />{busy ? "Preparando guías…" : q.data?.length ? "Actualizar guías" : "Preparar guías de migración"}</button><small>Tu progreso se conserva.</small></div></div>
      {renameWarnings.length > 0 && <div className="notice warning" role="status">{renameWarnings.map((warning) => <p key={warning}>{warning}</p>)}</div>}
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
      {showBulkRename && <BulkRename id={id} batchActive={batchActive || batchBusy} onClose={() => setShowBulkRename(false)} onDone={(warnings) => { setRenameWarnings(warnings); q.reload(); summary.reload(); preflight.reload(); }} />}
    </>
  );
}
