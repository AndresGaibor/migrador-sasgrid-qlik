import { useState } from "react";
import type { FormEvent } from "react";
import { api } from "../../api";
import { notifyError, notifySuccess } from "../../errors";
import type { JobPlan } from "../../types";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "../common";

const NAME_MAX_LENGTH = 60;

export function JobIdentity({ id, plan, folderPath, locked, onSaved }: { id: string; plan: JobPlan; folderPath?: string; locked: boolean; onSaved: (plan: JobPlan) => void }) {
  const [editing, setEditing] = useState(false);
  const [name, setName] = useState(plan.job_name);
  const [description, setDescription] = useState(plan.description ?? "");
  const [saving, setSaving] = useState(false);
  const [formError, setFormError] = useState<string>();
  const [warnings, setWarnings] = useState<string[]>([]);

  const open = () => {
    setName(plan.job_name);
    setDescription(plan.description ?? "");
    setFormError(undefined);
    setEditing(true);
  };

  const submit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const trimmedName = name.trim();
    if (trimmedName.length > NAME_MAX_LENGTH) {
      setFormError(`El nombre no puede tener más de ${NAME_MAX_LENGTH} caracteres.`);
      return;
    }
    setSaving(true);
    setFormError(undefined);
    try {
      const result = await api.updateJobMeta(id, plan.program, { job_name: trimmedName || null, description: description.trim() || null });
      setWarnings(result.warnings);
      onSaved(result.plan);
      setEditing(false);
      notifySuccess("Nombre y descripción guardados");
    } catch (error) {
      setFormError(notifyError(error, "No se pudo guardar el Job"));
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="job-identity">
      <div className="job-identity-title">
        <h1>{plan.job_name}</h1>
        {plan.job_name_edited && <Badge>editado</Badge>}
      </div>
      {plan.description && <p className="job-identity-description">{plan.description}</p>}
      {folderPath && <p className="muted job-identity-folder">Carpeta destino: <code>{folderPath}</code></p>}
      {plan.rename_ignored && <p role="status" className="notice warning">{`El nombre «${plan.rename_ignored}» ya no está disponible; se usa el generado.`}</p>}
      {warnings.length > 0 && <div role="status" className="notice warning">{warnings.map((warning) => <p key={warning}>{warning}</p>)}</div>}
      {editing ? (
        <form className="job-identity-form" aria-label="Editar nombre y descripción" onSubmit={submit}>
          <label>Nombre del Job<Input value={name} onChange={(event) => setName(event.target.value)} aria-describedby="job-name-hint" /></label>
          <small id="job-name-hint" className="muted">Máximo {NAME_MAX_LENGTH} caracteres. Déjalo vacío para volver al nombre generado.</small>
          <label>Descripción<Textarea rows={3} value={description} onChange={(event) => setDescription(event.target.value)} /></label>
          {formError && <p role="alert" className="error">{formError}</p>}
          <div className="job-identity-actions">
            <button type="submit" disabled={saving || locked}>{saving ? "Guardando…" : "Guardar"}</button>
            <button type="button" className="secondary" disabled={saving} onClick={() => setEditing(false)}>Cancelar</button>
          </div>
        </form>
      ) : (
        <div className="job-identity-actions">
          <button type="button" className="secondary" disabled={locked} onClick={open}>{locked ? "Hay una creación en curso" : "Editar nombre y descripción"}</button>
        </div>
      )}
    </div>
  );
}
