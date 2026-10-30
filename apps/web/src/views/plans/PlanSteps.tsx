import { useEffect, useState } from "react";
import { Badge } from "../common";
import { notifyError } from "../../errors";
import { orderSteps } from "../../guided";
import { decodeProgress, isUncertainStep, type GuideProgress } from "../../guide-progress";
import type { JobPart, Step } from "../../types";
import { ExpressionEditor } from "./ExpressionEditor";
import { StepDecisionDialogs, StepInstructions, StepProgressEditor } from "./PlanStepParts";
import { verificationCheckLabel, verificationStatusLabel } from "./plan-status";
import { StudioJobMaps, StudioStepView, useHasPanel } from "../../studio/StudioStepView";
import { effectiveComponent } from "../../studio/step-adapter";
import { FusedBadge } from "../../studio/FusedBadge";
import "../../studio/studio.css";

type Decide = (s: Step, progress: GuideProgress, note: string, blockReason: string) => Promise<void>;
type EditExpression = (step: Step, index: number, talend: string | null) => Promise<void>;
type FieldDone = (stepId: string, field: string, done: boolean) => Promise<void>;

// Los pasos que comparten «subjob» salen de un mismo bloque del SAS (un DATA o PROC): se construyen juntos.
export function StepGroups({ id, steps, onDecide, onEditExpression, expressionsDisabled, onFieldDone, parts }: { id: string; steps: Step[]; onDecide: Decide; onEditExpression: EditExpression; expressionsDisabled: boolean; onFieldDone?: FieldDone; parts?: JobPart[] }) {
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
      <StudioJobMaps steps={ordered} parts={parts} onSelect={jumpToStep} />
      {groups.map((g, gi) => {
        const reads = g.filter((x) => x.purpose.startsWith("Leer ")).map((x) => x.purpose.slice(5));
        const writes = g.filter((x) => x.purpose.startsWith("Escribir ")).map((x) => x.purpose.slice(9).replace(/ \(reemplaza\)/, ""));
        const title = reads.length || writes.length ? `${reads.join(" + ") || "datos"} → ${writes.join(" + ") || "resultado"}` : g[0].purpose;
        const done = g.filter(isDone).length;
        const cards = <>{g.length > 1 && <p className="muted">Estos {g.length} pasos van en el mismo lienzo, uno detrás de otro. Conéctalos como indica cada paso.</p>}{g.map((st) => <StepCard key={st.id} id={id} s={st} allSteps={ordered} previous={ordered[ordered.indexOf(st) - 1]} onDecide={onDecide} onEditExpression={onEditExpression} expressionsDisabled={expressionsDisabled} onFieldDone={onFieldDone} />)}</>;
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

function StepCard({ id, s, allSteps, previous, onDecide, onEditExpression, expressionsDisabled, onFieldDone }: { id: string; s: Step; allSteps: Step[]; previous?: Step; onDecide: Decide; onEditExpression: EditExpression; expressionsDisabled: boolean; onFieldDone?: FieldDone }) {
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
  const hasPanel = useHasPanel(s);
  const studioCheck = s.studio_verification;
  const studioUniqueName = studioCheck?.studio_unique_name ?? studioCheck?.talend_unique_name;
  return <article className="guide-step" id={`step-${s.id}`}>
    <div className="guide-step-heading"><div className="step-head"><h3>{s.purpose}</h3><span className="step-component">Componente: <code>{effectiveComponent(s)}</code></span></div></div>
    {studioCheck && <div className={`studio-step-verification ${studioCheck.status}`} role="status"><Badge tone={studioCheck.status === "verified" ? "ok" : "warn"}>{studioCheck.status === "verified" ? "Configurado en Studio" : studioCheck.status === "unavailable" ? "Studio no disponible" : "Pendiente de configuración"}</Badge>{studioUniqueName && <code>{studioUniqueName}</code>}{studioCheck.checked_at && <small>Lectura de Studio: {new Date(studioCheck.checked_at).toLocaleString("es")}</small>}{studioCheck.reason && <span>{studioCheck.reason}</span>}{Object.keys(studioCheck.checks).length > 0 && <details><summary>Verificación automática</summary><ul>{Object.entries(studioCheck.checks).map(([name, check]) => <li key={name}><strong>{verificationCheckLabel(name)}:</strong> {verificationStatusLabel(check.status)}{check.reason ? ` · ${check.reason}` : ""}</li>)}</ul></details>}</div>}
    {s.recommended && <p className="notice info-notice" role="note"><b>Buena práctica.</b> {s.why ?? "Este paso no viene del SAS: lo añade el portal por buenas prácticas de Talend."}</p>}
    <FusedBadge fusedFrom={s.fused_from} why={s.recommended ? null : s.why} />
    <StudioStepView step={s} onFieldDone={onFieldDone} />
    {hasPanel
      ? <details className="studio-text-steps"><summary>Ver las instrucciones en texto</summary><StepInstructions id={id} step={s} allSteps={allSteps} officialUrl={officialUrl} /></details>
      : <StepInstructions id={id} step={s} allSteps={allSteps} officialUrl={officialUrl} />}
    {s.expressions.length > 0 && <div className="guide-expressions">{s.expressions.map((expression, index) => <ExpressionEditor key={`${s.id}:${index}`} id={`${s.id}-${index}`} expression={expression} disabled={expressionsDisabled} onSave={(talend) => onEditExpression(s, index, talend)} />)}</div>}
    <StepProgressEditor progress={progress} note={note} blockReason={blockReason} previous={previous} error={err} onProgress={chooseProgress} onNoteChange={setNote} onNoteBlur={() => note !== saved.note && void save(progress)} onEditBlock={() => setDialog("blocked")} onJumpPrevious={(step) => jumpToStep(step.id)} />
    <StepDecisionDialogs step={s} dialog={dialog} setDialog={setDialog} confirmed={confirmed} setConfirmed={setConfirmed} blockReason={blockReason} setBlockReason={setBlockReason} onSave={(state) => void save(state)} />
  </article>;
}

