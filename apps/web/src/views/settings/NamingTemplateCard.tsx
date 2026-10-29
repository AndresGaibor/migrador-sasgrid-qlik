import { useEffect, useRef, useState } from "react";
import { api } from "../../api";
import { formatErrorMessage, notifyError, notifySuccess } from "../../errors";
import type { NamingTemplate } from "../../types";

export function NamingTemplateCard({ initial }: { initial: NamingTemplate }) {
  const [template, setTemplate] = useState(initial.template);
  const [saved, setSaved] = useState(initial.template);
  const [example, setExample] = useState(initial.example_name);
  const [error, setError] = useState<string>();
  const [previewError, setPreviewError] = useState<string>();
  const [saving, setSaving] = useState(false);
  const field = useRef<HTMLInputElement>(null);
  const changed = template.trim() !== saved && template.trim().length > 0;

  useEffect(() => {
    if (!template.trim()) return;
    let active = true;
    const timer = window.setTimeout(async () => {
      try {
        const result = await api.namingExample(template);
        if (!active) return;
        setExample(result.name);
        setPreviewError(undefined);
      } catch (reason) {
        if (active) setPreviewError(formatErrorMessage(reason));
      }
    }, 300);
    return () => {
      active = false;
      window.clearTimeout(timer);
    };
  }, [template]);

  const insert = (token: string) => {
    const start = field.current?.selectionStart ?? template.length;
    const end = field.current?.selectionEnd ?? template.length;
    setTemplate(`${template.slice(0, start)}{${token}}${template.slice(end)}`.slice(0, 200));
    field.current?.focus();
  };

  const save = async (value = template.trim()) => {
    setSaving(true);
    setError(undefined);
    try {
      const result = await api.setNamingTemplate(value);
      setTemplate(result.template);
      setSaved(result.template);
      setExample(result.example_name);
      setPreviewError(undefined);
      notifySuccess("Plantilla guardada", "Se aplicará la próxima vez que prepares o actualices las guías.");
    } catch (reason) {
      setError(notifyError(reason, "No se pudo guardar la plantilla"));
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="naming-template">
      <div className="naming-template-field">
        <label htmlFor="naming-template">Plantilla</label>
        <input
          id="naming-template"
          ref={field}
          value={template}
          maxLength={200}
          onChange={(event) => setTemplate(event.target.value)}
          aria-describedby={previewError ? "naming-template-error" : undefined}
        />
        <div className="naming-tokens" aria-label="Insertar un token">
          {initial.tokens.map((token) => (
            <button key={token} type="button" className="secondary" onClick={() => insert(token)}>
              {`{${token}}`}
            </button>
          ))}
        </div>
      </div>
      <p className="naming-example" role="status" aria-live="polite">
        Ejemplo con un programa de la carpeta lz: <code>{example}</code>
      </p>
      {previewError && <p className="error" id="naming-template-error" role="alert">{previewError}</p>}
      {error && <p className="error" role="alert">{error}</p>}
      <p className="muted">Se aplica al preparar o actualizar las guías. Los nombres que editaste a mano no cambian.</p>
      <div className="naming-template-actions">
        <button type="button" onClick={() => void save()} disabled={!changed || saving || Boolean(previewError)}>
          {saving ? "Guardando…" : "Guardar plantilla"}
        </button>
        <button type="button" className="secondary" onClick={() => void save(initial.default_template)} disabled={saving || saved === initial.default_template}>
          Restaurar {initial.default_template}
        </button>
      </div>
    </div>
  );
}
