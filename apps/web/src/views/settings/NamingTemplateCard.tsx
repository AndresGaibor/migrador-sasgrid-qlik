import { useEffect, useRef, useState } from "react";
import { api } from "../../api";
import { useAsync } from "../../hooks";
import { Load } from "../common";
import { formatErrorMessage, notifyError, notifySuccess } from "../../errors";
import type { NamingTemplate } from "../../types";

const HELP = "Se aplica al preparar o actualizar las guías. Los nombres que editaste a mano no cambian.";

function TemplateForm({ initial }: { initial: NamingTemplate }) {
  const [saved, setSaved] = useState(initial.template);
  const [draft, setDraft] = useState(initial.template);
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string>();
  const [example, setExample] = useState<{ example: string | null; error: string | null }>();
  const inputRef = useRef<HTMLInputElement>(null);
  const caret = useRef<number | undefined>(undefined);

  useEffect(() => {
    let live = true;
    const timer = window.setTimeout(() => {
      api.namingExample(draft)
        .then((result) => live && setExample(result))
        .catch((error: unknown) => live && setExample({ example: null, error: formatErrorMessage(error) }));
    }, 300);
    return () => {
      live = false;
      window.clearTimeout(timer);
    };
  }, [draft]);

  useEffect(() => {
    if (caret.current === undefined || !inputRef.current) return;
    inputRef.current.setSelectionRange(caret.current, caret.current);
    caret.current = undefined;
  }, [draft]);

  const insertToken = (token: string) => {
    const input = inputRef.current;
    const start = input?.selectionStart ?? draft.length;
    const end = input?.selectionEnd ?? draft.length;
    caret.current = start + token.length;
    setDraft(draft.slice(0, start) + token + draft.slice(end));
    input?.focus();
  };

  const save = async () => {
    if (saving || draft === saved) return;
    setSaving(true);
    setSaveError(undefined);
    try {
      const result = await api.setNamingTemplate(draft);
      setSaved(result.template);
      setDraft(result.template);
      notifySuccess("Plantilla guardada", "Se aplicará al preparar o actualizar las guías.");
    } catch (error) {
      setSaveError(notifyError(error, "No se pudo guardar la plantilla"));
    } finally {
      setSaving(false);
    }
  };

  const unchanged = draft === saved;
  return <>
    <label className="naming-label" htmlFor="naming-template">Plantilla del nombre del Job</label>
    <input
      id="naming-template"
      ref={inputRef}
      className="naming-input mono"
      value={draft}
      onChange={(event) => setDraft(event.target.value)}
      aria-invalid={Boolean(example?.error)}
      aria-describedby="naming-template-help"
    />
    <div className="chip-list" aria-label="Tokens disponibles">
      {initial.tokens.map((token) => (
        <button key={token} type="button" className="secondary" onClick={() => insertToken(token)} aria-label={`Insertar ${token}`}>{token}</button>
      ))}
    </div>
    <p className="muted" id="naming-template-help">{HELP}</p>
    <p>Ejemplo: <span className="mono">{example?.example ?? "—"}</span></p>
    {example?.error && <p className="permission-toggle-error" role="alert">{example.error}</p>}
    {saveError && <p className="permission-toggle-error" role="alert">{saveError}</p>}
    <button type="button" onClick={() => void save()} disabled={unchanged || saving}>{saving ? "Guardando…" : "Guardar"}</button>{" "}
    <button type="button" className="secondary" onClick={() => setDraft(initial.default)}>Restaurar {initial.default}</button>
  </>;
}

function LoadedTemplateForm() {
  const q = useAsync(api.namingTemplate, []);
  return <Load q={q}>{(data) => <TemplateForm initial={data} />}</Load>;
}

export function NamingTemplateCard({ initial }: { initial?: NamingTemplate }) {
  return <section className="panel" aria-labelledby="naming-template-title">
    <h2 id="naming-template-title">Plantilla de nombres</h2>
    <p className="muted">Define el nombre de los Jobs que se crean desde las guías.</p>
    {initial ? <TemplateForm initial={initial} /> : <LoadedTemplateForm />}
  </section>;
}
