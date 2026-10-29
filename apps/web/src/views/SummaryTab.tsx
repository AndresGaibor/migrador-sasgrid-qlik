import { useEffect, useState } from "react";
import { ApiError, api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { formatErrorMessage, notifyError, notifySuccess } from "../errors";
import type { Summary } from "../types";
import { Badge, Load, link, prioTone } from "./common";
import { pendingTotals } from "../project-workspace";
import { useProjectEvents } from "../project-events";

export function SummaryTab({ id, refreshKey = 0 }: { id: string; refreshKey?: number }) {
  const inventory = useAsync(() => api.inventory(id), [id]);
  const persisted = useAsync(async () => {
    try { return await api.analysis(id); }
    catch (error) {
      if (error instanceof ApiError && error.status === 409) return undefined;
      throw error;
    }
  }, [id, refreshKey]);
  const processing = useAsync(async () => {
    try { return await api.processing(id); }
    catch (error) {
      if (error instanceof ApiError && error.status === 409) return undefined;
      throw error;
    }
  }, [id, refreshKey]);
  const progress = useAsync(async () => {
    try { return await api.projectProgress(id); }
    catch (error) { if (error instanceof ApiError && error.status === 409) return undefined; throw error; }
  }, [id, refreshKey]);
  const pending = useAsync(async () => {
    try { return await api.pendingSummary(id); }
    catch (error) { if (error instanceof ApiError && error.status === 409) return undefined; throw error; }
  }, [id, refreshKey]);
  const [s, setS] = useState<Summary>();
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const summary = s ?? persisted.data;
  const pendingCount = pendingTotals(pending.data ?? []);
  const events = useProjectEvents(id, processing.reload);
  const isProcessing = processing.data?.status === "queued" || processing.data?.status === "running";
  useEffect(() => {
    if (!isProcessing) {
      if (processing.data?.status === "completed") persisted.reload();
      return;
    }
    if (events.connected) return;
    const timer = window.setInterval(processing.reload, 1500);
    return () => window.clearInterval(timer);
  }, [isProcessing, processing.data?.status, processing.reload, persisted.reload, events.connected]);
  useEffect(() => {
    if (processing.data?.status === "completed") { progress.reload(); pending.reload(); }
  }, [processing.data?.status, progress.reload, pending.reload]);
  const run = async () => {
    setBusy(true); setErr(undefined);
    try {
      const result = await api.analyze(id);
      setS(result);
      persisted.reload();
      notifySuccess("Análisis completado", `${result.programs} programas revisados.`);
    }
    catch (x) { setErr(notifyError(x, "No se pudo analizar el proyecto")); }
    finally { setBusy(false); }
  };
  return <>
    <h1>Conoce tu punto de partida</h1>
    <p className="subtitle">Analiza tus programas para descubrir cómo funcionan y qué necesita atención antes de migrar.</p>
    {processing.data && <div className={`project-processing-inline ${isProcessing ? "active" : processing.data.status}`} role="status" aria-live="polite"><span>{isProcessing ? <span className="spinner" /> : <Icon name={processing.data.status === "completed" ? "check" : "info"} size={17} />}</span><div><strong>{processing.data.message}</strong><small>Etapa: {processing.data.stage} · Estado: {processing.data.status}</small></div></div>}
    {processing.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{formatErrorMessage(processing.error, undefined, processing.errorStatus)}</span></div>}
    {progress.data && <section className="panel command-center" aria-label="Progreso de migración">
      <div className="command-center-heading"><div><span className="eyebrow">CENTRO DE MANDO</span><h2>Tu ruta de migración</h2><p>Avance basado en el estado guardado de este proyecto.</p></div>
        {progress.data.next && <a className="button" href={link(id, progress.data.next.tab)}>{progress.data.next.label}<Icon name="arrow" size={17} /></a>}
      </div>
      <ol className="migration-progress-list">{progress.data.stages.map((stage) => <li key={stage.key} className={`migration-progress-step ${stage.status}`}>
        <span className="migration-progress-marker" aria-hidden="true">{stage.status === "done" ? "✓" : stage.status === "blocked" ? "!" : stage.status === "current" ? "●" : "○"}</span>
        <span className="migration-progress-copy"><strong>{stage.label}</strong><small>{stage.detail}</small></span>
      </li>)}</ol>
    </section>}
    {pending.data && pending.data.length > 0 && <section className="panel pending-summary" aria-label="Pendientes de migración">
      <div className="section-heading"><div><h2>Pendientes por resolver</h2><p className="muted">Agrupados por decisión necesaria; abre el Job para revisar los pasos.</p></div><Badge tone="warn">{pendingCount.steps} {pendingCount.steps === 1 ? "paso" : "pasos"} en {pendingCount.jobs} {pendingCount.jobs === 1 ? "Job" : "Jobs"}</Badge></div>
      <ul>{pending.data.map((group) => <li key={group.reason}><div><strong>{group.reason}</strong><small>{group.steps} {group.steps === 1 ? "paso" : "pasos"}</small></div><div className="pending-job-links">{group.programs.map((job) => <a key={`${job.program}:${job.job_name}`} href={link(id, "planes", job.program)}>{job.job_name}<Icon name="arrow" size={14} /></a>)}</div></li>)}</ul>
    </section>}
    {progress.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>No se pudo recuperar el progreso: {formatErrorMessage(progress.error, undefined, progress.errorStatus)}</span><button className="secondary" onClick={progress.reload}>Reintentar</button></div>}
    <Load q={inventory}>{(m) => <section className="panel">
      <div className="panel-heading"><Icon name={m.files.length ? "chart" : "upload"} size={28} /><div><h2>{m.files.length ? isProcessing ? "El análisis automático está en curso" : "Tu proyecto está listo" : "Empecemos por tus archivos"}</h2><p>{m.files.length ? `${m.files.length} archivos cargados. El portal analiza programas, instrucciones y aspectos por revisar.` : "Carga tus programas SAS para obtener un resumen de tu proyecto."}</p></div></div>
      {m.files.length ? <button onClick={run} disabled={busy || (Boolean(processing.data) && isProcessing)}><Icon name="play" size={16} />{busy ? "Analizando proyecto…" : isProcessing ? "Análisis en curso…" : summary ? "Volver a analizar" : "Analizar proyecto"}</button> : <a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar mis archivos <Icon name="arrow" size={16} /></a>}
      {busy && <p role="status" className="loading-state"><span className="spinner" /> Estamos revisando tus programas. Puedes esperar en esta pantalla.</p>}
    </section>}</Load>
    {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
    {persisted.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>No se pudo recuperar el análisis guardado: {formatErrorMessage(persisted.error, undefined, persisted.errorStatus)}</span></div>}
    {summary ? <>
      <div className="notice" role="status"><Icon name="check" /><span><strong>Análisis completado.</strong> Ya puedes explorar tus programas y generar el plan de migración.</span></div>
      <div className="metrics"><div className="metric"><strong>{summary.programs}</strong><span>Programas analizados</span></div><div className="metric"><strong>{summary.statements}</strong><span>Instrucciones encontradas</span></div><div className="metric"><strong>{summary.unrecognized}</strong><span>Instrucciones sin reconocer</span></div><div className="metric"><strong>{summary.macro_fragments}</strong><span>Fragmentos de macros</span></div></div>
      <div className="next-actions"><a className="button" href={link(id, "planes")}>Preparar plan de migración <Icon name="arrow" size={17} /></a><a className="button secondary" href={link(id, "dependencias")}><Icon name="flow" size={18} /> Explorar flujo de datos</a></div>
      <h2>Resultado por tipo de instrucción</h2><p className="muted">Prioridades de revisión: P0 = cobertura básica · P1 = revisión adicional · P2 = requiere decisión manual.</p>
      <p>{Object.entries(summary.findings_by_priority).map(([p, n]) => <Badge key={p} tone={prioTone(p)}>{p}: {n} hallazgos</Badge>)}</p>
      <table><thead><tr><th>Tipo de instrucción</th><th>Prioridad</th><th className="num">Cantidad</th></tr></thead><tbody>{summary.coverage.map((c) => <tr key={c.tag}><td>{c.tag}</td><td><Badge tone={prioTone(c.priority)}>{c.priority}</Badge></td><td className="num">{c.count}</td></tr>)}</tbody></table>
    </> : isProcessing ? <div className="notice"><Icon name="info" /><span>El análisis se está ejecutando en segundo plano. Esta pantalla recuperará los resultados al terminar, incluso si la recargas.</span></div> : <div className="notice"><Icon name="info" /><span><strong>¿Qué obtendrás?</strong> Un inventario de programas, un mapa de sus conexiones y una base para preparar tu plan. Si ya analizaste este proyecto, consulta los resultados en las pestañas de arriba.</span></div>}
  </>;
}
