import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import type { Step } from "../../types";

type Expression = Step["expressions"][number];

export function ExpressionEditor({ id, expression, onSave, disabled = false }: { id: string; expression: Expression; onSave: (talend: string | null) => Promise<void>; disabled?: boolean }) {
  const [value, setValue] = useState(expression.talend ?? "");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string>();

  useEffect(() => setValue(expression.talend ?? ""), [expression.talend]);

  const save = async (talend: string | null) => {
    setSaving(true);
    setError(undefined);
    try {
      await onSave(talend);
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "No se pudo guardar la expresión.");
    } finally {
      setSaving(false);
    }
  };

  return <section className="guide-expression" aria-label="Expresión SAS y traducción Talend">
    <div><h4>Expresión SAS · línea {expression.line}</h4><pre>{expression.sas}</pre></div>
    <form onSubmit={(event) => { event.preventDefault(); void save(value.trim()); }}>
      <label htmlFor={`talend-expression-${id}`}>Expresión Talend</label>
      <Textarea
        id={`talend-expression-${id}`}
        aria-label="Expresión Talend"
        value={value}
        onChange={(event) => setValue(event.target.value)}
        required
        maxLength={2000}
        rows={2}
        disabled={saving || disabled}
      />
      <div className="guide-expression-actions">
        <Button type="submit" disabled={saving || disabled || !value.trim()}>{saving ? "Guardando…" : "Guardar expresión"}</Button>
        <Button type="button" variant="link" size="xs" disabled={saving || disabled} onClick={() => void save(null)}>Restaurar traducción sugerida</Button>
        {expression.talend_edited && <span role="status">Corregida manualmente</span>}
      </div>
      {error && <p className="error" role="alert">{error}</p>}
    </form>
  </section>;
}
