import { useState } from "react";
import { api } from "../api";
import { notifyError } from "../errors";
import type { TranslateResult } from "../types";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "./common";

const SAS_MAX_LENGTH = 20000;

// Expresiones que el traductor en línea resuelve sin rutinas de Talend (comparaciones salen sin traducir a propósito: semántica de nulos).
export const TRANSLATOR_EXAMPLES = ["(precio - descuento) * cantidad", "upcase(nombre)", "saldo + &min"];

export function TranslationResult({ result }: { result: TranslateResult }) {
  return (
    <section className="translator-result" aria-label="Resultado de la traducción" aria-live="polite">
      {result.talend !== null ? (
        <>
          <h2>Java para Talend</h2>
          <pre className="do-value">{result.talend}</pre>
        </>
      ) : (
        <>
          <h2>Sin traducción automática</h2>
          {!result.talend_engine_enabled && <p className="notice warning">El traductor ampliado con rutinas de Talend está apagado (<code>SGM_TALEND_EXPRESSIONS</code>).</p>}
        </>
      )}
      <p className="muted">Motor: <Badge>{result.engine}</Badge></p>
      {result.columns.length > 0 && <p>Columnas detectadas: {result.columns.map((column) => <code key={column} className="translator-column">{column}</code>)}</p>}
      {result.warnings.length > 0 && <ul className="translator-warnings">{result.warnings.map((warning) => <li key={warning}>{warning}</li>)}</ul>}
    </section>
  );
}

export function TranslatorView() {
  const [sas, setSas] = useState("");
  const [busy, setBusy] = useState(false);
  const [result, setResult] = useState<TranslateResult>();
  const [error, setError] = useState<string>();

  const translate = async () => {
    setBusy(true);
    setError(undefined);
    try {
      setResult(await api.translate(sas));
    } catch (x) {
      setResult(undefined);
      setError(notifyError(x, "No se pudo traducir la expresión"));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="translator">
      <h1>Traductor de expresiones</h1>
      <p className="muted">Escribe una expresión o condición de SAS y mira el Java que se usaría en Talend.</p>
      <label>Expresión SAS<Textarea rows={4} maxLength={SAS_MAX_LENGTH} value={sas} disabled={busy} onChange={(event) => setSas(event.target.value)} placeholder="saldo + 10" /></label>
      <div className="translator-examples">
        <span className="muted">Ejemplos:</span>
        {TRANSLATOR_EXAMPLES.map((example) => <button key={example} type="button" className="secondary" disabled={busy} onClick={() => setSas(example)}><code>{example}</code></button>)}
      </div>
      <div className="job-identity-actions">
        <button type="button" disabled={busy || !sas.trim()} onClick={() => void translate()}>{busy ? "Traduciendo…" : "Traducir"}</button>
      </div>
      {error && <p role="alert" className="error">{error}</p>}
      {result && <TranslationResult result={result} />}
    </div>
  );
}
