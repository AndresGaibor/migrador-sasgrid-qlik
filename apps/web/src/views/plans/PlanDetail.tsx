import { useEffect, useRef, useState } from "react";
import type { FormEvent, MouseEvent } from "react";
import { Icon } from "../../components/Icon";
import { api } from "../../api";
import { formatErrorMessage, notifyError, notifySuccess } from "../../errors";
import { useAsync } from "../../hooks";
import { encodeProgress, storageStatus, type GuideProgress } from "../../guide-progress";
import type { JobPlan, Step } from "../../types";
import { Load, link } from "../common";
import { PlanPreparation } from "./PlanPreparation";
import { JobIdentity } from "./JobIdentity";
import { GridRecommendations } from "./PlanGrid";
import { BatchJobRow } from "./PlanBatchPanel";
import { StepGroups } from "./PlanSteps";
import { applyStatusLabel } from "./plan-status";
import { PARENT_PATTERN, useDesktopLayout, visible } from "./plan-rows";
import { useProjectEvents } from "../../project-events";

export function PlanDetail({ id, file }: { id: string; file: string }) {
  const isDesktop = useDesktopLayout();
  const q = useAsync(() => api.plan(id, file), [id, file]);
  const jobs = useAsync(() => api.plans(id), [id]);
  const gridQ = useAsync(() => api.gridRecommendations(id), [id]);
  const summary = useAsync(() => api.talendApplyBatchSummary(id), [id]);
  const ordered = visible(jobs.data ?? [], summary.data?.programs.map((job) => job.program));
  const ownGrid = (gridQ.data ?? []).filter((g) => g.evidence.file === file);
  const [override, setOverride] = useState<JobPlan>();
  const [saving, setSaving] = useState(false);
  const [metaSaving, setMetaSaving] = useState(false);
  const [metaMessage, setMetaMessage] = useState<string>();
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
  const events = useProjectEvents(id, () => {
    applyStatus.reload();
    batch.reload();
  });
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
    if (events.connected) return;
    if (!isApplyRunning && !isBatchRunning && !batch.error) return;
    const timer = window.setInterval(() => {
      if (isApplyRunning) applyStatus.reload();
      if (isBatchRunning || batch.error) batch.reload();
    }, 1200);
    return () => window.clearInterval(timer);
  }, [isApplyRunning, isBatchRunning, batch.error, applyStatus.reload, batch.reload, events.connected]);
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
  const saveJobMeta = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    setMetaSaving(true);
    setMetaMessage(undefined);
    try {
      const result = await api.updateJobMeta(
        id,
        file,
        String(form.get("job_name") ?? "").trim(),
        String(form.get("description") ?? "").trim() || null,
      );
      setOverride(result.plan);
      jobs.reload();
      setMetaMessage("Nombre y descripción guardados.");
      notifySuccess("Job actualizado", "El cambio también aparece en la lista de guías.");
    } catch (error) {
      setMetaMessage(notifyError(error, "No se pudo guardar el nombre del Job"));
    } finally {
      setMetaSaving(false);
    }
  };
  const editExpression = async (step: Step, index: number, talend: string | null) => {
    const updated = await api.editExpression(id, file, step.id, index, talend);
    setOverride(updated);
    notifySuccess(talend === null ? "Traducción restaurada" : "Expresión guardada", "La guía ya usa esta expresión Talend.");
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
            <JobIdentity plan={p} folderPath={preview.data?.identity.folder_path} />
            {p.rename_ignored && <p className="notice" role="status">No se aplicó “{p.rename_ignored}” porque ese nombre ya está ocupado. El nombre actual se conserva.</p>}
            <details className="job-meta-editor" key={`${p.job_name}:${p.description ?? ""}`}>
              <summary>Editar nombre y descripción</summary>
              <form onSubmit={(event) => void saveJobMeta(event)}>
                <label>Nombre del Job<input name="job_name" required maxLength={60} pattern="[A-Za-z_][A-Za-z0-9_]*" defaultValue={p.job_name} aria-describedby="job-name-help" /></label>
                <small id="job-name-help">Empieza con una letra o guion bajo; usa letras, números y guiones bajos.</small>
                <label>Descripción<textarea name="description" maxLength={500} rows={2} defaultValue={p.description ?? ""} /></label>
                <button type="submit" disabled={metaSaving || isApplyRunning || isBatchRunning}>{metaSaving ? "Guardando…" : "Guardar cambios"}</button>
              </form>
              {metaMessage && <p role="status">{metaMessage}</p>}
            </details>
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
            <StepGroups id={id} steps={p.steps} onDecide={decide} onEditExpression={editExpression} expressionsDisabled={Boolean(isApplyRunning || isBatchRunning)} />
            {p.children.map((c) => (
              <section key={c.name}>
                <h2>Crea también un Job aparte para la macro %{c.name}</h2><p className="muted">Nombre sugerido: <code>job_{c.name.toLowerCase()}</code>{c.params.length > 0 && <> · parámetros que recibe: {c.params.map((x) => <code key={x}> {x}</code>)}</>}. Sus pasos son estos:</p>
              <StepGroups id={id} steps={c.steps} onDecide={decide} onEditExpression={editExpression} expressionsDisabled={Boolean(isApplyRunning || isBatchRunning)} />
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
