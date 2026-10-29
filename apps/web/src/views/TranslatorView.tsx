import { useState } from "react";
import type { FormEvent } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { api } from "../api";
import { formatErrorMessage } from "../errors";
import type { TranslateResult } from "../types";

const EXAMPLES = [
  { label: "Comparar texto", sas: "nombre = 'ANA'" },
  { label: "Limpiar texto", sas: "strip(nombre)" },
  { label: "Extraer año", sas: "year(fecha)" },
];

export function TranslatorView() {
  const [sas, setSas] = useState("");
  const [result, setResult] = useState<TranslateResult>();
  const [error, setError] = useState<string>();
  const [pending, setPending] = useState(false);

  const translate = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setPending(true);
    setError(undefined);
    setResult(undefined);
    try {
      const translated = await api.translate(sas.trim());
      setResult(translated);
    } catch (reason) {
      setError(formatErrorMessage(reason));
    } finally {
      setPending(false);
    }
  };

  return <>
    <h1>Laboratorio del traductor SAS → Talend</h1>
    <p className="subtitle">Prueba una expresión aislada y revisa el Java propuesto antes de llevarlo a una guía.</p>
    <section className="translator-workbench" aria-label="Laboratorio de traducción">
      <div className="translator-examples"><strong>Prueba un ejemplo</strong>{EXAMPLES.map((example) => <Button key={example.label} type="button" variant="outline" size="sm" onClick={() => { setSas(example.sas); setResult(undefined); setError(undefined); }}>{example.label}</Button>)}</div>
      <form onSubmit={(event) => void translate(event)}>
        <label htmlFor="translator-sas">Expresión SAS</label>
        <Textarea id="translator-sas" aria-label="Expresión SAS" value={sas} onChange={(event) => setSas(event.target.value)} maxLength={20_000} rows={5} placeholder="Escribe una condición o expresión SAS" required />
        <div className="translator-actions"><small>{sas.length.toLocaleString("es")} / 20 000 caracteres</small><Button type="submit" disabled={pending || !sas.trim()}>{pending ? "Traduciendo…" : "Traducir"}</Button></div>
      </form>
      {error && <p className="error" role="alert">{error}</p>}
      {result && <section className="translator-result" aria-label="Resultado de traducción" aria-live="polite">
        <div className="translator-result-heading"><h2>Resultado</h2><span>{result.engine === "talend" ? "Rutinas de Talend" : "Motor integrado"}</span></div>
        {result.talend === null ? <p className="notice">No hay una traducción automática segura. Revisa los avisos antes de continuar.</p> : <pre>{result.talend}</pre>}
        {result.columns.length > 0 && <p><strong>Columnas detectadas:</strong> {result.columns.map((column) => <code key={column}>{column}</code>)}</p>}
        {result.warnings.length > 0 && <ul className="translator-warnings">{result.warnings.map((warning) => <li key={warning}>{warning}</li>)}</ul>}
        {result.talend === null && !result.talend_engine_enabled && <p className="muted">El traductor ampliado con rutinas de Talend está apagado (<code>SGM_TALEND_EXPRESSIONS</code>).</p>}
        <small className="muted">La salida es una propuesta; valida su semántica y compatibilidad en Talend Studio.</small>
      </section>}
    </section>
  </>;
}
