import { useState } from "react";
import { api } from "../../api";
import { notifyError, notifySuccess } from "../../errors";
import type { JobPlan, Step } from "../../types";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "../common";

const EXPRESSION_MAX_LENGTH = 2000;

// Misma validación que el servidor (422): una sola línea, no vacía y de hasta 2000 caracteres.
export function expressionDraftError(text: string): string | undefined {
  if (!text.trim()) return "Escribe la expresión en Java.";
  if (/[\r\n]/.test(text)) return "La expresión debe ir en una sola línea.";
  if (text.length > EXPRESSION_MAX_LENGTH) return `La expresión no puede tener más de ${EXPRESSION_MAX_LENGTH} caracteres.`;
  return undefined;
}

export function ExpressionEditor({ id, file, stepId, index, expression, locked = false, onSaved }: { id: string; file: string; stepId: string; index: number; expression: Step["expressions"][number]; locked?: boolean; onSaved: (plan: JobPlan) => void }) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(expression.talend ?? "");
  const [saving, setSaving] = useState(false);
  const [formError, setFormError] = useState<string>();

  const open = () => {
    setDraft(expression.talend ?? "");
    setFormError(undefined);
    setEditing(true);
  };

  // `talend` a null restaura la traducción automática.
  const save = async (talend: string | null) => {
    if (talend !== null) {
      const invalid = expressionDraftError(talend);
      if (invalid) {
        setFormError(invalid);
        return;
      }
    }
    setSaving(true);
    setFormError(undefined);
    try {
      const plan = await api.editExpression(id, file, stepId, index, talend);
      onSaved(plan);
      setEditing(false);
      notifySuccess(talend === null ? "Traducción automática restaurada" : "Expresión guardada");
    } catch (error) {
      setFormError(notifyError(error, "No se pudo guardar la expresión"));
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="expression-editor">
      <div className="expression-editor-sas"><span className="expression-editor-label">SAS (línea {expression.line})</span><code>{expression.sas}</code></div>
      <div className="expression-editor-java">
        <span className="expression-editor-label">Java en Talend {expression.talend_edited && <Badge>editada</Badge>}</span>
        {expression.talend ? <pre className="do-value">{expression.talend}</pre> : <p className="muted">Sin traducción automática. Escríbela a mano.</p>}
      </div>
      {expression.warnings.length > 0 && <ul className="expression-editor-warnings">{expression.warnings.map((warning) => <li key={warning}>{warning}</li>)}</ul>}
      {editing ? (
        <div className="expression-editor-form">
          <label>Expresión en Java (una línea)<Textarea rows={1} maxLength={EXPRESSION_MAX_LENGTH} value={draft} onChange={(event) => setDraft(event.target.value)} /></label>
          {formError && <p role="alert" className="error">{formError}</p>}
          <div className="expression-editor-actions">
            <button type="button" disabled={saving || locked} onClick={() => void save(draft.trim())}>{saving ? "Guardando…" : "Guardar"}</button>
            <button type="button" className="secondary" disabled={saving} onClick={() => setEditing(false)}>Cancelar</button>
          </div>
        </div>
      ) : (
        <div className="expression-editor-actions">
          <button type="button" className="secondary" disabled={locked} onClick={open}>Editar</button>
          {expression.talend_edited && <button type="button" className="secondary" disabled={locked || saving} onClick={() => void save(null)}>Volver a la traducción automática</button>}
          {locked && <small className="muted">Hay una creación en curso.</small>}
        </div>
      )}
      {!editing && formError && <p role="alert" className="error">{formError}</p>}
    </div>
  );
}
