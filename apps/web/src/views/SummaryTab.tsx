import { useEffect, useState } from "react";
import { ApiError, api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { formatErrorMessage, notifyError, notifySuccess } from "../errors";
import type { ProjectProgress, Summary } from "../types";
import { Badge, Load, link, prioTone } from "./common";
import { groupPendingDecisions, pendingTotals, type PendingDecision } from "../project-workspace";
import { useProjectEvents } from "../project-events";

const PRIORITY_LABEL: Record<string, string> = {
  P0: "Cobertura básica",
  P1: "Revisión adicional",
  P2: "Requiere decisión manual",
};

const STAGE_STATE: Record<ProjectProgress["stages"][number]["status"], string> = {
  done: "Completado",
  current: "En curso",
  blocked: "Bloqueado",
  todo: "Pendiente",
};

const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;

export function SummaryTab({ id, rest, refreshKey = 0 }: { id: string; rest?: string; refreshKey?: number }) {
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
  const decisions = groupPendingDecisions(pending.data ?? []);
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

  const notices = <>
    {processing.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{formatErrorMessage(processing.error, undefined, processing.errorStatus)}</span></div>}
    {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
    {persisted.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>No se pudo recuperar el análisis guardado: {formatErrorMessage(persisted.error, undefined, persisted.errorStatus)}</span></div>}
    {progress.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>No se pudo recuperar el progreso: {formatErrorMessage(progress.error, undefined, progress.errorStatus)}</span><button className="secondary" onClick={progress.reload}>Reintentar</button></div>}
  </>;

  if (rest === "analisis") return <>
    <nav className="summary-back"><a href={link(id, "resumen")}>Volver al resumen</a></nav>
    <h1>Resultado del análisis</h1>
    {notices}
    {summary
      ? <AnalysisDetail summary={summary} />
      : <p className="muted">Aún no hay un análisis guardado. Analiza el proyecto desde el resumen.</p>}
  </>;

  return <>
    {notices}
    <Load q={inventory}>{(m) => {
      const files = m.files.length;
      const headline = !files ? "Empieza cargando tus programas SAS"
        : isProcessing ? "Analizando tus programas"
        : summary ? `${summary.programs} programas analizados`
        : "Falta analizar el proyecto";
      const detail = !files ? "Con los programas cargados, el portal extrae instrucciones, dependencias y pendientes."
        : isProcessing ? "Puedes salir de esta pantalla. El resultado queda guardado al terminar."
        : summary ? `${plural(summary.statements, "instrucción encontrada", "instrucciones encontradas")}, ${summary.unrecognized} sin reconocer.`
        : "Analiza los programas para ver instrucciones, dependencias y pendientes.";
      return <>
        <section className="summary-status" aria-labelledby="summary-headline">
          <div>
            <h1 id="summary-headline">{headline}</h1>
            <p>{detail}</p>
          </div>
          <div className="summary-actions">
            {!files
              ? <a className="button" href={link(id, "importar")}><Icon name="upload" size={18} />Cargar archivos</a>
              : <>
                {summary && <a className="button" href={link(id, "planes")}>Preparar plan de migración</a>}
                <button type="button" className={summary ? "secondary" : undefined} onClick={run} disabled={busy || isProcessing}>
                  <Icon name="play" size={16} />{busy ? "Analizando…" : isProcessing ? "Análisis en curso…" : summary ? "Volver a analizar" : "Analizar proyecto"}
                </button>
              </>}
          </div>
        </section>
        {busy && <p role="status" className="loading-state"><span className="spinner" /> Estamos revisando tus programas. Puedes esperar en esta pantalla.</p>}
      </>;
    }}</Load>

    {progress.data && <section className="summary-route" aria-label="Ruta de migración">
      <div className="summary-route-heading">
        <h2>Ruta de migración</h2>
        {progress.data.next && <a className="summary-route-next" href={link(id, progress.data.next.tab)}>Siguiente: {progress.data.next.label}</a>}
      </div>
      <ol className="route">{progress.data.stages.map((stage) => <li key={stage.key} className={`route-step ${stage.status}`} aria-current={stage.status === "current" ? "step" : undefined}>
        <em className="route-state">{STAGE_STATE[stage.status]}</em>
        <strong>{stage.label}</strong>
        <small>{stage.detail}</small>
      </li>)}</ol>
    </section>}

    {decisions.length > 0 && <details className="disclosure" open>
      <summary><span className="disclosure-title">Decisiones pendientes</span><span className="disclosure-meta">{plural(pendingCount.steps, "paso", "pasos")} en {plural(pendingCount.jobs, "Job", "Jobs")}</span></summary>
      <DecisionList decisions={decisions.slice(0, 5)} />
      <a className="disclosure-link" href={link(id, "planes")}>Abrir las guías de los Jobs</a>
    </details>}

    {summary && <details className="disclosure">
      <summary><span className="disclosure-title">Resultado del análisis</span><span className="disclosure-meta">{summary.programs} programas · {summary.statements} instrucciones</span></summary>
      <Figures summary={summary} />
      <a className="disclosure-link" href={link(id, "resumen", "analisis")}>Ver instrucciones por tipo</a>
    </details>}
  </>;
}

function Figures({ summary }: { summary: Summary }) {
  return <dl className="figures">
    <div><dt>Programas analizados</dt><dd>{summary.programs}</dd></div>
    <div><dt>Instrucciones encontradas</dt><dd>{summary.statements}</dd></div>
    <div><dt>Sin reconocer</dt><dd>{summary.unrecognized}</dd></div>
    <div><dt>Fragmentos de macros</dt><dd>{summary.macro_fragments}</dd></div>
  </dl>;
}

// Los Jobs y sus pasos se revisan en la guía de cada Job: aquí solo se ve qué decisión falta y a cuántos Jobs afecta.
function DecisionList({ decisions }: { decisions: PendingDecision[] }) {
  return <ul className="decision-list">{decisions.map((decision) => {
    const row = <>
      <span className="disclosure-title">{decision.title}</span>
      <span className="decision-steps">{plural(decision.steps, "paso", "pasos")}</span>
      <span className="decision-jobs">{plural(decision.jobs.length, "Job", "Jobs")}</span>
    </>;
    if (!decision.parts) return <li key={decision.title} className="decision-row">{row}</li>;
    return <li key={decision.title}>
      <details className="disclosure decision">
        <summary>{row}</summary>
        {decision.hint && <p className="decision-hint">{decision.hint}</p>}
        <ul className="decision-parts">{decision.parts.map((part) => <li key={part.title}>
          <span><strong>{part.title}</strong><small>{part.detail}</small></span>
          <span className="decision-steps">{plural(part.steps, "paso", "pasos")}</span>
        </li>)}</ul>
      </details>
    </li>;
  })}</ul>;
}

function AnalysisDetail({ summary }: { summary: Summary }) {
  const known = Object.keys(PRIORITY_LABEL);
  const others = [...new Set(summary.coverage.map((c) => c.priority))].filter((p) => !known.includes(p));
  return <>
    <Figures summary={summary} />
    {[...known, ...others].map((priority) => {
      const rows = summary.coverage.filter((c) => c.priority === priority);
      if (rows.length === 0) return null;
      return <details key={priority} className="disclosure" open={priority === "P2"}>
        <summary>
          <span className="disclosure-title"><Badge tone={prioTone(priority)}>{priority}</Badge>{PRIORITY_LABEL[priority] ?? "Sin clasificar"}</span>
          <span className="disclosure-meta">{plural(rows.length, "tipo", "tipos")} · {summary.findings_by_priority[priority] ?? 0} hallazgos</span>
        </summary>
        <table>
          <thead><tr><th>Tipo de instrucción</th><th className="num">Cantidad</th></tr></thead>
          <tbody>{rows.map((c) => <tr key={c.tag}><td>{c.tag}</td><td className="num">{c.count}</td></tr>)}</tbody>
        </table>
      </details>;
    })}
  </>;
}
