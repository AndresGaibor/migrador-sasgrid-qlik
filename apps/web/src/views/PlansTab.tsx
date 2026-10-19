import { useEffect, useRef, useState } from "react";
import { Icon } from "../components/Icon";
import { Dialog } from "../components/Dialog";
import { api } from "../api";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { GridRecommendation, JobPlan, Step } from "../types";
import { Badge, Load, link } from "./common";
import { orderSteps } from "../guided";
import { catalogAudit } from "../catalog-explorer";
import { decodeProgress, encodeProgress, GUIDE_PROGRESS, isUncertainStep, storageStatus, type GuideProgress } from "../guide-progress";

export function PlansTab({ id, file }: { id: string; file?: string }) {
  return file ? <PlanDetail id={id} file={decodeURI(file)} /> : <PlanList id={id} />;
}

function PlanList({ id }: { id: string }) {
  const q = useAsync(() => api.plans(id), [id]);
  const grid = useAsync(() => api.gridRecommendations(id), [id]);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const gen = async () => {
    setBusy(true);
    setErr(undefined);
    try {
      await api.generatePlans(id);
      q.reload();
      grid.reload();
    } catch (x) {
      setErr((x as Error).message);
    } finally {
      setBusy(false);
    }
  };
  return (
    <>
      <h1>Jobs y guías de migración</h1>
      <p className="subtitle">Cada programa SAS tiene una guía ordenada para ayudarte a construir su proceso en Talend Studio.</p>
      <div className="panel"><div className="panel-heading"><Icon name="list" size={26} /><div><h2>Guía para cada programa</h2><p>Abre un job para ver qué hacer, qué componente usar y qué debes confirmar.</p></div></div><button onClick={gen} disabled={busy}><Icon name="play" size={16} />{busy ? "Preparando guías…" : q.data?.length ? "Actualizar guías" : "Preparar guías de migración"}</button><p className="muted" style={{ fontSize: 12, marginBottom: 0 }}>Al actualizar, se conservan las decisiones que ya guardaste por paso.</p></div>
      {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
      {grid.data && <GridRecommendations id={id} items={grid.data} />}
      {q.error?.includes("generados") ? (
        <div className="notice"><Icon name="info" /><span>Todavía no hay planes en este proyecto. Pulsa «Generar planes de migración» para empezar.</span></div>
      ) : (
        <Load q={q}>
          {(rows) => (
            rows.length === 0 ? <div className="empty-state"><span className="empty-icon">🧭</span><h3>Primero analiza tus programas</h3><p>Cuando termine el análisis, aquí aparecerá una guía para cada job.</p><a className="button" href={link(id, "resumen")}>Ir al resumen <Icon name="arrow" size={17} /></a></div> : <div className="guide-job-list">{rows.map((r) => (
              <article className="guide-job" key={r.program}><div className="guide-job-icon" aria-hidden="true">🔄</div><div className="guide-job-main"><h2>{r.job_name}</h2><p>Programa SAS: <code>{r.program}</code></p><div className="guide-job-meta"><Badge tone={r.job_status === "proposed" ? "ok" : "warn"}>{r.job_status === "proposed" ? "Propuesto" : r.job_status === "blocked" ? "Bloqueado" : r.job_status === "needs_review" ? "Requiere revisión" : r.job_status}</Badge><span>{r.steps} pasos</span><span>{r.pending} por revisar</span><span>{r.done} completados</span></div></div><a className="button" href={link(id, "planes", r.program)}>Abrir guía <Icon name="arrow" size={17} /></a></article>
            ))}</div>
          )}
        </Load>
      )}
    </>
  );
}

function PlanDetail({ id, file }: { id: string; file: string }) {
  const q = useAsync(() => api.plan(id, file), [id, file]);
  const jobs = useAsync(() => api.plans(id), [id]);
  const [override, setOverride] = useState<JobPlan>();
  const [saving, setSaving] = useState(false);
  const [navigationWarning, setNavigationWarning] = useState(false);
  const saveFailed = useRef(false);
  const pendingSaves = useRef(0);
  const saveQueue = useRef<Promise<void>>(Promise.resolve());
  const plan = override ?? q.data;
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
  const jobIndex = jobs.data?.findIndex((item) => item.program === file) ?? -1;
  const previousJob = jobIndex > 0 ? jobs.data?.[jobIndex - 1] : undefined;
  const nextJob = jobIndex >= 0 ? jobs.data?.[jobIndex + 1] : undefined;
  const navigateAfterSave = (event: React.MouseEvent<HTMLAnchorElement>, destination: string) => {
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
      <div className="guide-job-navigation"><a aria-disabled={saving} href={saving ? undefined : link(id, "planes")} onClick={(event) => navigateAfterSave(event, link(id, "planes"))}>{saving ? "Guardando progreso…" : "← Todas las guías"}</a><div><a className={previousJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!previousJob || saving} href={previousJob && !saving ? link(id, "planes", previousJob.program) : undefined} onClick={(event) => previousJob && navigateAfterSave(event, link(id, "planes", previousJob.program))}>← Job anterior</a><a className={nextJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!nextJob || saving} href={nextJob && !saving ? link(id, "planes", nextJob.program) : undefined} onClick={(event) => nextJob && navigateAfterSave(event, link(id, "planes", nextJob.program))}>Siguiente job →</a></div></div>
      <Load q={{ ...q, data: plan }}>
        {(p) => (
          <>
            <h1>{p.job_name}</h1>
            <p className="subtitle">Sigue los pasos en orden en Talend Studio. Las sugerencias son candidatas y deben confirmarse en tu entorno.</p>
            <div className="guide-intro"><span aria-hidden="true">🧭</span><div><strong>Tu ruta de trabajo</strong><p>Empieza por el paso 1. En cada tarjeta encontrarás la acción, los valores sugeridos y el fragmento SAS que explica la recomendación.</p></div><Badge tone="warn">Studio: pendiente de validación</Badge></div>
            <p><strong>Programa de origen:</strong> <a href={link(id, "programas", p.program)}><code>{p.program}</code></a></p>
            {p.context_variables.length > 0 && (
              <>
                <h2>Variables de contexto</h2>
                <ul>{p.context_variables.map((c) => <li key={c.name}><code>{c.suggested}</code> ← {c.name} {c.sas_value && <>= <code>{c.sas_value}</code></>}</li>)}</ul>
              </>
            )}
            {p.libraries_needed.length > 0 && (
              <>
                <h2>Conexiones a crear</h2>
                <ul>{p.libraries_needed.map((l) => <li key={l.sas_name}><code>{l.sas_name}</code> ({l.engine ?? "BASE"}{l.path && `, ${l.path}`}) → {l.suggested_connection}</li>)}</ul>
              </>
            )}
            {p.orchestration.grid_recommendations.length > 0 && <GridRecommendations id={id} items={p.orchestration.grid_recommendations} />}
            <h2>Pasos de la guía <Badge>{p.steps.length}</Badge></h2>
            <div className="guide-steps">{orderSteps(p.steps).map((s, index, ordered) => <StepCard key={s.id} id={id} s={s} allSteps={ordered} previous={ordered[index - 1]} onDecide={decide} />)}</div>
            {p.children.map((c) => (
              <section key={c.name}>
                <h2>Job hijo para %{c.name}({c.params.join(", ")})</h2>
                {orderSteps(c.steps).map((s, index, ordered) => <StepCard key={s.id} id={id} s={s} allSteps={ordered} previous={ordered[index - 1]} onDecide={decide} />)}
              </section>
            ))}
            {p.validation_cases.length > 0 && (
              <>
                <h2>Casos de validación</h2>
                <ul>{p.validation_cases.map((v) => <li key={v.id}><code>{v.id}</code> ({v.kind}): {v.description}</li>)}</ul>
              </>
            )}
            {p.unresolved.length > 0 && (
              <details><summary>Sin resolver ({p.unresolved.length})</summary><ul>{p.unresolved.map((u, i) => <li key={i}>{u}</li>)}</ul></details>
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
          {item.required.length > 0 && <><b>Confirmar</b><ul>{item.required.map((requirement) => <li key={requirement}>{requirement}</li>)}</ul></>}
          {item.dependencies.length > 0 && <p className="muted">Depende de: {item.dependencies.join(", ")}</p>}
          <details><summary>Datos interpretados</summary><pre className="doc">{JSON.stringify(item.details, null, 2)}</pre></details>
        </article>
      ))}
    </section>
  );
}

function ComponentLink({ name, known }: { name: string; known?: boolean | null }) {
  const base = name.split(" ")[0];
  return known ? <a href={`#/catalogo/${base}`}><code>{name}</code></a> : <code>{name}</code>;
}

function jumpToStep(stepId: string) {
  document.getElementById(`step-${stepId}`)?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function StepCard({ id, s, allSteps, previous, onDecide }: { id: string; s: Step; allSteps: Step[]; previous?: Step; onDecide: (s: Step, progress: GuideProgress, note: string, blockReason: string) => Promise<void> }) {
  const saved = decodeProgress(s.status, s.note);
  const [progress, setProgress] = useState<GuideProgress>(saved.state);
  const [note, setNote] = useState(saved.note);
  const [blockReason, setBlockReason] = useState(saved.blockReason);
  const [dialog, setDialog] = useState<"blocked" | "confirm" | null>(null);
  const [confirmed, setConfirmed] = useState(false);
  const [err, setErr] = useState<string>();
  useEffect(() => { const current = decodeProgress(s.status, s.note); setProgress(current.state); setNote(current.note); setBlockReason(current.blockReason); }, [s.status, s.note]);
  const uncertain = isUncertainStep(s);
  const save = (next: GuideProgress) => onDecide(s, next, note, blockReason).then(() => { setProgress(next); setDialog(null); setConfirmed(false); setErr(undefined); }).catch((e: Error) => setErr(e.message));
  const chooseProgress = (value: GuideProgress) => {
    if (value === "blocked") { setDialog("blocked"); return; }
    if (value === "completed" && uncertain) { setConfirmed(false); setDialog("confirm"); return; }
    void save(value);
  };
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
      {s.pending.length > 0 && <div className="guide-pending"><strong>⏳ Decisión pendiente</strong><ul>{s.pending.map((x, i) => <li key={i}>{x}</li>)}</ul></div>}
      {s.assumptions.length > 0 && <p className="muted">Supuestos: {s.assumptions.join("; ")}</p>}
      <div className="row">
        <label>
          Progreso del paso
          <select value={progress} onChange={(e) => chooseProgress(e.target.value as GuideProgress)}>
            {GUIDE_PROGRESS.map((x) => <option key={x} value={x}>{{ pending: "Pendiente", in_progress: "En progreso", completed: "Completado", blocked: "Bloqueado" }[x]}</option>)}
          </select>
        </label>
        <label className="grow">
          Nota de trabajo
          <input value={note} onChange={(e) => setNote(e.target.value)} onBlur={() => note !== saved.note && void save(progress)} />
        </label>
      </div>
      {progress === "blocked" && <div className="guide-block-reason"><p><strong>Motivo del bloqueo:</strong> {blockReason || "Falta indicar el motivo."}</p><button type="button" className="text-button" onClick={() => setDialog("blocked")}>Editar motivo</button></div>}
      {previous && <button type="button" className="text-button guide-previous-step" onClick={() => jumpToStep(previous.id)}>← Volver al paso anterior · {previous.order}. {previous.component_candidate}</button>}
      {err && <p className="error" role="alert">{err}</p>}
      {dialog === "blocked" && <Dialog title="¿Qué impide continuar?" onClose={() => setDialog(null)}><p>Indica el motivo para que tú o tu equipo sepan qué falta resolver.</p><label>Motivo del bloqueo<textarea value={blockReason} onChange={(e) => setBlockReason(e.target.value)} rows={3} autoFocus /></label><div className="dialog-actions"><button className="secondary" onClick={() => setDialog(null)}>Cancelar</button><button disabled={!blockReason.trim()} onClick={() => void save("blocked")}>Guardar bloqueo</button></div></Dialog>}
      {dialog === "confirm" && <Dialog title="Confirma este paso incierto" onClose={() => setDialog(null)}><p>Este paso tiene información pendiente o una recomendación que aún no se ha verificado. Revísalo en Talend Studio antes de completarlo.</p><ul>{s.pending.map((item, index) => <li key={index}>{item}</li>)}</ul><label className="guide-confirm"><input type="checkbox" checked={confirmed} onChange={(e) => setConfirmed(e.target.checked)} />Confirmo que revisé este paso en Talend Studio.</label><div className="dialog-actions"><button className="secondary" onClick={() => setDialog(null)}>Volver a revisar</button><button disabled={!confirmed} onClick={() => void save("completed")}>Confirmar y completar</button></div></Dialog>}
    </article>
  );
}
