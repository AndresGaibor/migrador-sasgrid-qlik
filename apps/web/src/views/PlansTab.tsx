import { useEffect, useRef, useState } from "react";
import { Icon } from "../components/Icon";
import { api } from "../api";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { GridRecommendation, JobPlan, PlanRow, Step } from "../types";
import { Badge, Load, link } from "./common";
import { orderSteps } from "../guided";
import { buildGridGuides } from "../grid-guide";
import { PlanPreparation } from "./plans/PlanPreparation";
import { decodeProgress, encodeProgress, isUncertainStep, storageStatus, type GuideProgress } from "../guide-progress";
import { Button } from "@/components/ui/button";
import { StepDecisionDialogs, StepInstructions, StepProgressEditor } from "./plans/PlanStepParts";
import { PlanListContent } from "./plans/PlanListContent";

export function PlansTab({ id, file }: { id: string; file?: string }) {
  return file ? <PlanDetail id={id} file={decodeURI(file)} /> : <PlanList id={id} />;
}

// Los ZIP de Mac traen basura «__MACOSX»; se oculta aunque venga de proyectos ya importados.
const real = (rows: PlanRow[]) => rows.filter((r) => !r.program.includes("__MACOSX/"));
const PARENT_PATTERN = /include_dispatch|sysin|submit/;
function parentFiles(grid?: GridRecommendation[]) {
  return new Set((grid ?? []).filter((g) => PARENT_PATTERN.test(g.pattern_id)).map((g) => g.evidence.file));
}
// Orden de construcción: lo que otros usan primero, lo que lanza a los demás al final.
function visible(rows: PlanRow[], grid?: GridRecommendation[]) {
  return buildOrder(real(rows), parentFiles(grid)).flatMap((g) => g.rows);
}
function buildOrder(rows: PlanRow[], parents: Set<string>) {
  const todo = rows.filter((r) => r.steps > 0);
  const groups = [
    { title: "Primero: piezas base", hint: "Macros y formatos que usan los demás programas. Constrúyelos antes.", rows: todo.filter((r) => /\/(Macro|Formats)\//.test(r.program) && !parents.has(r.program)) },
    { title: "Después: los procesos", hint: "Un Job por cada programa de negocio.", rows: todo.filter((r) => !/\/(Macro|Formats)\//.test(r.program) && !parents.has(r.program)) },
    { title: "Al final: los Jobs que lanzan a los demás", hint: "Unen los procesos anteriores en el orden correcto.", rows: todo.filter((r) => parents.has(r.program)) },
  ];
  return groups.filter((g) => g.rows.length > 0);
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
      <h1>Tu plan de trabajo en Talend Studio</h1>
      <p className="subtitle">Construye los Jobs de arriba abajo. Al abrir uno, la guía te dice qué arrastrar y qué escribir.</p>
      <div className="panel"><Button onClick={gen} disabled={busy}><Icon name="play" size={16} />{busy ? "Preparando guías…" : q.data?.length ? "Volver a preparar las guías" : "Preparar guías de migración"}</Button><p className="muted" style={{ fontSize: 12, marginBottom: 0 }}>Lo que ya marcaste como hecho se conserva.</p></div>
      {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
      {q.error?.includes("generados") ? (
        <div className="notice"><Icon name="info" /><span>Todavía no hay guías preparadas para este proyecto. Usa «Preparar guías de migración» para empezar.</span></div>
      ) : (
        <Load q={q}>
          {(all) => { const rows = real(all); return <PlanListContent id={id} rows={rows} groups={buildOrder(rows, parentFiles(grid.data))} />; }}
        </Load>
      )}
    </>
  );
}

function PlanDetail({ id, file }: { id: string; file: string }) {
  const q = useAsync(() => api.plan(id, file), [id, file]);
  const jobs = useAsync(() => api.plans(id), [id]);
  const gridQ = useAsync(() => api.gridRecommendations(id), [id]);
  const ordered = visible(jobs.data ?? [], gridQ.data);
  const ownGrid = (gridQ.data ?? []).filter((g) => g.evidence.file === file);
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
  const jobIndex = ordered.findIndex((item) => item.program === file);
  const previousJob = jobIndex > 0 ? ordered[jobIndex - 1] : undefined;
  const nextJob = jobIndex >= 0 ? ordered[jobIndex + 1] : undefined;
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
      <div className="guide-job-navigation"><a className="button secondary" aria-disabled={saving} href={saving ? undefined : link(id, "planes")} onClick={(event) => navigateAfterSave(event, link(id, "planes"))}>{saving ? "Guardando progreso…" : "Todas las guías"}</a><div><a className={previousJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!previousJob || saving} href={previousJob && !saving ? link(id, "planes", previousJob.program) : undefined} onClick={(event) => previousJob && navigateAfterSave(event, link(id, "planes", previousJob.program))}>Job anterior</a><a className={nextJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!nextJob || saving} href={nextJob && !saving ? link(id, "planes", nextJob.program) : undefined} onClick={(event) => nextJob && navigateAfterSave(event, link(id, "planes", nextJob.program))}>Siguiente job</a></div></div>
      <Load q={{ ...q, data: plan }}>
        {(p) => (
          <>
            <h1>{p.job_name}</h1>
            <p className="subtitle">Sigue las tarjetas en orden para configurar cada componente; el estado muestra el avance general del componente.</p>
            <p><strong>Programa SAS de origen:</strong> <a href={link(id, "programas", p.program)}><code>{p.program}</code></a></p>
            <PlanPreparation plan={p} />
            {ownGrid.length > 0 && <GridRecommendations id={id} items={ownGrid} />}
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
              <details><summary>Sin resolver ({p.unresolved.length})</summary><ul>{p.unresolved.map((u, i) => <li key={i}>{u}</li>)}</ul></details>
            )}
          </>
        )}
      </Load>
    </>
  );
}

function GridRecommendations({ id, items }: { id: string; items: GridRecommendation[] }) {
  const guides = buildGridGuides(items);
  return (
    <section aria-label="Orquestación y planificación">
      <h2>{guides.some((g) => g.kind === "build") ? "Primero: encadena los programas" : "Aparte: se hace fuera de Talend"}</h2>
      {guides.map((g, gi) => (
        <details className="panel" key={g.key} open={gi === 0}>
          <summary><b>{g.title}</b> <Badge tone={g.kind === "build" ? "ok" : "warn"}>{g.kind === "build" ? "Se hace en Talend Studio" : "Se hace fuera de Talend"}</Badge></summary>
          <p className="muted">{g.intro} {g.component && <><ComponentIcon name={g.component} /> <ComponentLink name={g.component} known /></>} {g.doc_url && <a href={g.doc_url} target="_blank" rel="noreferrer">Docs oficiales Talend</a>}</p>
          <ol>
            {g.actions.map((a, n) => (
              <li key={n}>
                <b>{a.text}</b>
                {a.where && <div className="muted">Dónde: {a.where}</div>}
                {a.fields && <ul>{a.fields.map(([k, v]) => <li key={k}>{k}: <code>{v}</code></li>)}</ul>}
              </li>
            ))}
          </ol>
          <p className="muted">Origen en el SAS: {g.sources.map((r, n) => <span key={r.id}>{n > 0 && ", "}<a href={api.sourceEvidence(id, r.evidence.file, r.evidence.line)} target="_blank" rel="noreferrer">{r.evidence.file.split("/").pop()}:{r.evidence.line}</a></span>)}</p>
        </details>
      ))}
    </section>
  );
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
  const save = (next: GuideProgress) => onDecide(s, next, note, blockReason).then(() => { setProgress(next); setDialog(null); setConfirmed(false); setErr(undefined); }).catch((e: Error) => setErr(e.message));
  const chooseProgress = (value: GuideProgress) => {
    if (value === "blocked") { setDialog("blocked"); return; }
    if (value === "completed" && isUncertainStep(s)) { setConfirmed(false); setDialog("confirm"); return; }
    void save(value);
  };
  const officialUrl = s.doc_url;
  return <article className="guide-step" id={`step-${s.id}`}>
    <div className="guide-step-heading"><div className="step-head"><h3>{s.purpose}</h3><span className="step-component">Componente: <code>{s.component_candidate}</code></span></div></div>
    <StepInstructions id={id} step={s} allSteps={allSteps} officialUrl={officialUrl} />
    <StepProgressEditor progress={progress} note={note} blockReason={blockReason} previous={previous} error={err} onProgress={chooseProgress} onNoteChange={setNote} onNoteBlur={() => note !== saved.note && void save(progress)} onEditBlock={() => setDialog("blocked")} onJumpPrevious={(step) => jumpToStep(step.id)} />
    <StepDecisionDialogs step={s} dialog={dialog} setDialog={setDialog} confirmed={confirmed} setConfirmed={setConfirmed} blockReason={blockReason} setBlockReason={setBlockReason} onSave={(state) => void save(state)} />
  </article>;
}
