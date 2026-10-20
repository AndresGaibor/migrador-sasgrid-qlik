import { Icon } from "../../components/Icon";
import { Dialog } from "../../components/Dialog";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import type { Step } from "../../types";
import { stepDoes } from "../../step-guide";
import { GUIDE_PROGRESS, type GuideProgress } from "../../guide-progress";
import { link } from "../common";

export function StepInstructions({ id, step, allSteps, officialUrl }: { id: string; step: Step; allSteps: Step[]; officialUrl?: string | null }) {
  return <>
    <h4 className="guide-actions-heading">Pasos para configurar este componente</h4>
    <ol className="do-list" aria-label="Pasos para configurar este componente">
      {stepDoes(step, allSteps).map((d, i) => (
        <li key={i} className={`guide-action-step${d.check ? " do-check" : ""}`}>
          <span className="guide-action-number" aria-hidden="true">{i + 1}</span>
          <div className="guide-action-content">
            <b>{d.text}</b>
            {d.where && <div className="do-location"><span className="do-location-label">En Talend Studio</span><span>{d.where}</span></div>}
            {d.rows ? <div className="do-table-wrap"><table className="do-table">{d.columns && <thead><tr>{d.columns.map((c) => <th key={c}>{c}</th>)}</tr></thead>}<tbody>{d.rows.map((r, ri) => <tr key={ri}>{r.map((cell, ci) => <td key={ci}>{cell}</td>)}</tr>)}</tbody></table></div> : d.value && <pre className="do-value">{d.value}</pre>}
          </div>
        </li>
      ))}
    </ol>
    <div className="guide-links">{step.evidence?.file && <a href={`${link(id, "programas", step.evidence.file)}?line=${step.evidence.line}`}><Icon name="search" size={15} /> Ver el SAS original · {step.evidence.file.split("/").pop()}:{step.evidence.line}</a>}{officialUrl && <a href={officialUrl} target="_blank" rel="noreferrer"><Icon name="book" size={15} /> Documentación oficial</a>}</div>
    <details><summary>Trazabilidad</summary><p className="muted">Subjob: {step.subjob} · confianza: {step.confidence} · {step.verified ? "cotejado con Talend MCP" : "sin cotejar con Talend MCP"}{step.alternatives.length > 0 && ` · alternativas: ${step.alternatives.join(", ")}`}</p></details>
    {step.assumptions.length > 0 && <p className="muted">Supuestos: {step.assumptions.join("; ")}</p>}
  </>;
}

export function StepProgressEditor({ progress, note, blockReason, previous, error, onProgress, onNoteChange, onNoteBlur, onEditBlock, onJumpPrevious }: { progress: GuideProgress; note: string; blockReason: string; previous?: Step; error?: string; onProgress: (value: GuideProgress) => void; onNoteChange: (value: string) => void; onNoteBlur: () => void; onEditBlock: () => void; onJumpPrevious: (step: Step) => void }) {
  return <>
    <section className="guide-step-tracking" aria-label="Seguimiento del componente">
      <div className="guide-step-tracking-heading"><h4>Progreso del componente</h4><p>Este estado se aplica al componente completo; las tarjetas ordenan sus acciones. Se guarda al cambiarlo; la nota, al salir del campo.</p></div>
      <div className="row">
        <label>Estado del componente<Select value={progress} onValueChange={(value) => onProgress(value as GuideProgress)}><SelectTrigger className="w-full"><SelectValue /></SelectTrigger><SelectContent>{GUIDE_PROGRESS.map((value) => <SelectItem key={value} value={value}>{{ pending: "Pendiente", in_progress: "En progreso", completed: "Completado", blocked: "Bloqueado" }[value]}</SelectItem>)}</SelectContent></Select></label>
        <label className="grow">Nota para el equipo<Input value={note} onChange={(e) => onNoteChange(e.target.value)} onBlur={onNoteBlur} placeholder="Añade una decisión o contexto" /></label>
      </div>
      {progress === "blocked" && <div className="guide-block-reason"><p><strong>Motivo del bloqueo:</strong> {blockReason || "Falta indicar el motivo."}</p><Button type="button" variant="link" size="xs" onClick={onEditBlock}>Editar motivo</Button></div>}
      {error && <p className="error" role="alert">{error}</p>}
    </section>
    {previous && <Button type="button" variant="link" size="xs" className="guide-previous-step" onClick={() => onJumpPrevious(previous)}>← Volver al paso anterior · {previous.order}. {previous.component_candidate}</Button>}
  </>;
}

export function StepDecisionDialogs({ step, dialog, setDialog, confirmed, setConfirmed, blockReason, setBlockReason, onSave }: { step: Step; dialog: "blocked" | "confirm" | null; setDialog: (dialog: "blocked" | "confirm" | null) => void; confirmed: boolean; setConfirmed: (confirmed: boolean) => void; blockReason: string; setBlockReason: (reason: string) => void; onSave: (state: GuideProgress) => void }) {
  return <>
    {dialog === "blocked" && <Dialog title="¿Qué impide continuar?" onClose={() => setDialog(null)}>
      <p>Indica el motivo para que tú o tu equipo sepan qué falta resolver.</p>
      <label>Motivo del bloqueo<Textarea value={blockReason} onChange={(e) => setBlockReason(e.target.value)} rows={3} autoFocus /></label>
      <div className="dialog-actions"><Button variant="outline" onClick={() => setDialog(null)}>Cancelar</Button><Button disabled={!blockReason.trim()} onClick={() => onSave("blocked")}>Guardar bloqueo</Button></div>
    </Dialog>}
    {dialog === "confirm" && <Dialog title="Confirma este paso incierto" onClose={() => setDialog(null)}>
      <p>Este paso tiene información pendiente o una recomendación que aún no se ha verificado. Revísalo en Talend Studio antes de completarlo.</p>
      <ul>{step.pending.map((item, index) => <li key={index}>{item}</li>)}</ul>
      <div className="guide-confirm flex"><Checkbox id={`confirm-${step.id}`} checked={confirmed} onCheckedChange={(value) => setConfirmed(value === true)} /><label htmlFor={`confirm-${step.id}`}>Confirmo que revisé este paso en Talend Studio.</label></div>
      <div className="dialog-actions"><Button variant="outline" onClick={() => setDialog(null)}>Volver a revisar</Button><Button disabled={!confirmed} onClick={() => onSave("completed")}>Confirmar y completar</Button></div>
    </Dialog>}
  </>;
}
