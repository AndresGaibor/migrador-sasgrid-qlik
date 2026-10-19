import { useEffect, useRef, useState } from "react";
import { Icon } from "../components/Icon";
import { api } from "../api";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { GridRecommendation, JobPlan, PlanRow, Step } from "../types";
import { Badge, Load, link } from "./common";
import { orderSteps } from "../guided";
import { buildGridGuides } from "../grid-guide";
import { stepDoes, toContext } from "../step-guide";
import { catalogAudit } from "../catalog-explorer";
import { decodeProgress, encodeProgress, GUIDE_PROGRESS, isUncertainStep, storageStatus, type GuideProgress } from "../guide-progress";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Dialog, DialogContent, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";

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
        <div className="notice"><Icon name="info" /><span>Todavía no hay planes en este proyecto. Pulsa «Generar planes de migración» para empezar.</span></div>
      ) : (
        <Load q={q}>
          {(all) => {
            const rows = real(all);
            const groups = buildOrder(rows, parentFiles(grid.data));
            const empty = rows.filter((r) => r.steps === 0);
            const ordered = groups.flatMap((g) => g.rows);
            const next = ordered.find((r) => r.done < r.steps);
            let n = 0;
            if (rows.length === 0) return <div className="empty-state"><span className="empty-icon">🧭</span><h3>Primero analiza tus programas</h3><p>Cuando termine el análisis, aquí aparecerá una guía para cada job.</p><a className="button" href={link(id, "resumen")}>Ir al resumen <Icon name="arrow" size={17} /></a></div>;
            return (
              <>
                {next && <div className="guide-intro"><div><strong>{next.done === 0 && next === ordered[0] ? "Empieza aquí" : "Continúa aquí"}</strong><p>{next.job_name}</p></div><a className="button" href={link(id, "planes", next.program)}>{next.done === 0 && next === ordered[0] ? "Empezar" : "Continuar"} <Icon name="arrow" size={17} /></a></div>}
                {groups.map((g) => (
                  <section key={g.title}>
                    <h2>{g.title}</h2><p className="muted">{g.hint}</p>
                    <div className="guide-job-list">{g.rows.map((r) => (
                      <article className="guide-job" key={r.program}><div className="guide-job-main"><h3>{++n}. {r.job_name}</h3><div className="guide-job-meta">{r.done >= r.steps ? <Badge tone="ok">Terminado</Badge> : <span>{r.done} de {r.steps} pasos hechos</span>}<progress max={r.steps} value={r.done} /></div></div><a className="button" href={link(id, "planes", r.program)}>Abrir <Icon name="arrow" size={17} /></a></article>
                    ))}</div>
                  </section>
                ))}
                {empty.length > 0 && <details><summary>{empty.length} programa{empty.length === 1 ? "" : "s"} sin nada que construir</summary><ul>{empty.map((r) => <li key={r.program}><code>{r.program}</code></li>)}</ul></details>}
              </>
            );
          }}
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
      <div className="guide-job-navigation"><a aria-disabled={saving} href={saving ? undefined : link(id, "planes")} onClick={(event) => navigateAfterSave(event, link(id, "planes"))}>{saving ? "Guardando progreso…" : "← Todas las guías"}</a><div><a className={previousJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!previousJob || saving} href={previousJob && !saving ? link(id, "planes", previousJob.program) : undefined} onClick={(event) => previousJob && navigateAfterSave(event, link(id, "planes", previousJob.program))}>← Job anterior</a><a className={nextJob && !saving ? "button secondary" : "button secondary disabled-link"} aria-disabled={!nextJob || saving} href={nextJob && !saving ? link(id, "planes", nextJob.program) : undefined} onClick={(event) => nextJob && navigateAfterSave(event, link(id, "planes", nextJob.program))}>Siguiente job →</a></div></div>
      <Load q={{ ...q, data: plan }}>
        {(p) => (
          <>
            <h1>{p.job_name}</h1>
            <p className="subtitle">Hazlo en este orden, de arriba abajo. No hace falta interpretar nada: cada paso dice qué arrastrar, qué escribir y dónde.</p>
            <p><strong>Programa SAS de origen:</strong> <a href={link(id, "programas", p.program)}><code>{p.program}</code></a></p>
            {(p.libraries_needed.length > 0 || p.context_variables.length > 0) && (
              <div className="panel">
                <h2>Antes de empezar (una sola vez)</h2>
                <ol className="do-list">
                  <li><b>Crea el Job.</b><div className="muted">Dónde: Repository → Job Designs → clic derecho → Create Job → Name:</div><pre className="do-value">{p.job_name}</pre></li>
                  {p.libraries_needed.map((l) => <li key={l.sas_name}><b>{l.engine ? `Crea la conexión «${l.sas_name}».` : `«${l.sas_name}» son archivos: guárdalos como CSV (no hace falta conexión).`}</b>{l.engine ? <div className="muted">Dónde: Repository → Metadata → clic derecho en el tipo de conexión → Create. Tipo sugerido: {l.suggested_connection}. Motor SAS: {l.engine}. {l.path ? `Ruta o servicio en SAS: ${l.path}. ` : ""}Pide las credenciales al equipo; no se copian del SAS.</div> : <div className="muted">Se usa la variable de contexto que creas más abajo.</div>}</li>)}
                  {(p.context_variables.length > 0 || p.libraries_needed.some((l) => !l.engine && l.path)) && <li><b>Crea estas variables de contexto.</b><div className="muted">Dónde: pestaña Contexts del Job → «+» por cada una. Tipo: String.</div><pre className="do-value">{[...p.libraries_needed.filter((l) => !l.engine && l.path).map((l) => `context.${l.sas_name.toUpperCase()}_DIR = ${l.path}   (carpeta donde guardarás los CSV de esta librería)`), ...p.context_variables.map((c) => `${toContext("&" + c.name)}${c.sas_value ? ` = ${c.sas_value}` : "   (el valor te lo da el equipo)"}`)].join("\n")}</pre></li>}
                </ol>
              </div>
            )}
            {ownGrid.length > 0 && <GridRecommendations id={id} items={ownGrid} />}
            <h2>{ownGrid.some((g) => PARENT_PATTERN.test(g.pattern_id)) ? "Después: el resto del programa" : "Construye el Job paso a paso"} <Badge>{p.steps.length}</Badge></h2>
            <StepGroups id={id} steps={p.steps} onDecide={decide} />
            {p.children.map((c) => (
              <section key={c.name}>
                <h2>Crea también un Job aparte para la macro %{c.name}</h2><p className="muted">Nombre sugerido: <code>job_{c.name.toLowerCase()}</code>{c.params.length > 0 && <> · parámetros que recibe: {c.params.map((x) => <code key={x}> {x}</code>)}</>}. Sus pasos son estos:</p>
                <StepGroups id={id} steps={c.steps} onDecide={decide} />
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
        return (
          <details className="panel step-group" key={g[0].id} open={gi === firstOpen}>
            <summary><b>Bloque {gi + 1} de {groups.length}</b> · {title} <span className="muted">({done} de {g.length} hechos)</span></summary>
            {g.length > 1 && <p className="muted">Estos {g.length} pasos van en el mismo lienzo, uno detrás de otro. Conéctalos como indica cada paso.</p>}
            {g.map((st) => <StepCard key={st.id} id={id} s={st} allSteps={ordered} previous={ordered[ordered.indexOf(st) - 1]} onDecide={onDecide} />)}
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
  return (
    <article className="step guide-step" id={`step-${s.id}`}>
      <div className="guide-step-heading"><span className="guide-step-number">{s.order}</span><div><span className="eyebrow">PASO {s.order} · HAZ ESTO EN TALEND STUDIO</span><h3>{s.purpose}</h3></div></div>
      <ol className="do-list">
        {stepDoes(s, allSteps).map((d, i) => (
          <li key={i} className={d.check ? "do-check" : undefined}>
            <b>{d.text}</b>
            {d.value && <pre className="do-value">{d.value}</pre>}
            {d.where && <div className="muted">Dónde: {d.where}</div>}
          </li>
        ))}
      </ol>
      <div className="guide-links">{s.evidence?.file && <a href={`${link(id, "programas", s.evidence.file)}?line=${s.evidence.line}`}>🔎 Ver el SAS original · {s.evidence.file.split("/").pop()}:{s.evidence.line}</a>}{officialUrl ? <a href={officialUrl} target="_blank" rel="noreferrer">📘 Documentación oficial ↗</a> : null}</div>
      <details><summary>Detalles técnicos</summary><p className="muted">Subjob: {s.subjob} · confianza: {s.confidence} · {s.verified ? "cotejado con Talend MCP" : "sin cotejar con Talend MCP"}{s.alternatives.length > 0 && ` · alternativas: ${s.alternatives.join(", ")}`}</p></details>
      {s.assumptions.length > 0 && <p className="muted">Supuestos: {s.assumptions.join("; ")}</p>}
      <div className="row">
        <label>
          ¿Ya lo hiciste?
          <Select value={progress} onValueChange={(v) => chooseProgress(v as GuideProgress)}>
            <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
            <SelectContent>
              {GUIDE_PROGRESS.map((x) => <SelectItem key={x} value={x}>{{ pending: "Pendiente", in_progress: "En progreso", completed: "Completado", blocked: "Bloqueado" }[x]}</SelectItem>)}
            </SelectContent>
          </Select>
        </label>
        <label className="grow">
          Nota de trabajo
          <Input value={note} onChange={(e) => setNote(e.target.value)} onBlur={() => note !== saved.note && void save(progress)} />
        </label>
      </div>
      {progress === "blocked" && <div className="guide-block-reason"><p><strong>Motivo del bloqueo:</strong> {blockReason || "Falta indicar el motivo."}</p><Button type="button" variant="link" size="xs" onClick={() => setDialog("blocked")}>Editar motivo</Button></div>}
      {previous && <Button type="button" variant="link" size="xs" className="guide-previous-step" onClick={() => jumpToStep(previous.id)}>← Volver al paso anterior · {previous.order}. {previous.component_candidate}</Button>}
      {err && <p className="error" role="alert">{err}</p>}
      {dialog === "blocked" && <Dialog open onOpenChange={(open) => { if (!open) setDialog(null); }}>
        <DialogContent>
          <DialogHeader><DialogTitle>¿Qué impide continuar?</DialogTitle></DialogHeader>
          <p>Indica el motivo para que tú o tu equipo sepan qué falta resolver.</p>
          <Label>Motivo del bloqueo<Textarea value={blockReason} onChange={(e) => setBlockReason(e.target.value)} rows={3} autoFocus /></Label>
          <DialogFooter>
            <Button variant="outline" onClick={() => setDialog(null)}>Cancelar</Button>
            <Button disabled={!blockReason.trim()} onClick={() => void save("blocked")}>Guardar bloqueo</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>}
      {dialog === "confirm" && <Dialog open onOpenChange={(open) => { if (!open) setDialog(null); }}>
        <DialogContent>
          <DialogHeader><DialogTitle>Confirma este paso incierto</DialogTitle></DialogHeader>
          <p>Este paso tiene información pendiente o una recomendación que aún no se ha verificado. Revísalo en Talend Studio antes de completarlo.</p>
          <ul>{s.pending.map((item, index) => <li key={index}>{item}</li>)}</ul>
          <div className="flex items-start gap-2">
            <Checkbox id={`confirm-${s.id}`} checked={confirmed} onCheckedChange={(v) => setConfirmed(v === true)} />
            <Label htmlFor={`confirm-${s.id}`} className="font-normal">Confirmo que revisé este paso en Talend Studio.</Label>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setDialog(null)}>Volver a revisar</Button>
            <Button disabled={!confirmed} onClick={() => void save("completed")}>Confirmar y completar</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>}
    </article>
  );
}
