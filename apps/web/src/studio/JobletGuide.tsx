// Guía de joblets propuestos: qué bloque crear una vez en Studio, con qué parámetros y dónde usarlo en cada Job.
import { useState } from "react";
import type { JobPlan, JobletPlan, Step } from "../types";
import { JobCanvas } from "./JobCanvas";
import { jobCanvas } from "./step-adapter";
import { copyText } from "./clipboard";
import {
  allPlanSteps,
  copyableNames,
  diagramSteps,
  kindLabel,
  occurrenceLabel,
  parameterRows,
  showDiagram,
} from "./joblet-model";
import "./studio-panels.css";

export function JobletGuide({ plan }: { plan: JobPlan }) {
  const joblets = plan.joblets ?? [];
  if (joblets.length === 0) return null;
  const steps = allPlanSteps(plan);
  return (
    <section className="panel jl-guide" aria-label="Joblets propuestos">
      <h2>Bloques repetidos para crear como joblet</h2>
      <p className="muted">
        Estos bloques se repiten en el programa. Créalos una vez en Studio como joblet y úsalos en cada Job donde aparecen.
        El portal no crea ni modifica joblets: esta guía solo indica cómo hacerlo.
      </p>
      {joblets.map((joblet) => <JobletCard key={joblet.id} joblet={joblet} steps={steps} />)}
    </section>
  );
}

function JobletCard({ joblet, steps }: { joblet: JobletPlan; steps: Step[] }) {
  const rows = parameterRows(joblet);
  const canvas = showDiagram(joblet, steps) ? jobCanvas(diagramSteps(joblet, steps)) : null;
  return (
    <article className="jl-card" id={`joblet-${joblet.id}`}>
      <header className="jl-card-head">
        <h3><code>{joblet.name}</code> · {joblet.title}</h3>
        <div className="jl-badges">
          <span className="badge">{kindLabel(joblet.kind)}</span>
          <span className="badge">{occurrenceLabel(joblet.occurrences.length)}</span>
          <span className="badge">{joblet.operation_count} operaciones por aparición</span>
        </div>
      </header>
      <p><b>Por qué:</b> {joblet.why}</p>

      {rows.length > 0 && (
        <>
          <h4>Parámetros</h4>
          <div className="jl-table-wrap">
            <table className="jl-table">
              <thead>
                <tr>
                  <th scope="col">Parámetro</th>
                  <th scope="col">Variable de contexto</th>
                  {joblet.occurrences.map((occurrence) => (
                    <th scope="col" key={occurrence.job + occurrence.label}>{occurrence.job} <small className="muted">· {occurrence.label}</small></th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rows.map((row) => (
                  <tr key={row.name}>
                    <td><code>{row.name}</code></td>
                    <td><code>{row.context_variable}</code></td>
                    {row.values.map((value, index) => <td key={index}>{value || <span className="muted">—</span>}</td>)}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}

      {joblet.creation_steps.length > 0 && (
        <>
          <h4>Cómo crearlo en Studio</h4>
          <ol className="jl-steps">
            {joblet.creation_steps.map((text, index) => <li key={index}>{text}</li>)}
          </ol>
        </>
      )}
      <CopyNames names={copyableNames(joblet)} />

      <h4>Dónde usarlo</h4>
      {joblet.occurrences.map((occurrence) => (
        <div className="jl-usage" key={occurrence.job + occurrence.label}>
          <p><b>{occurrence.job}</b> <span className="muted">· {occurrence.label}</span></p>
          {occurrence.usage_steps.length > 0 && (
            <ol className="jl-steps">
              {occurrence.usage_steps.map((text, index) => <li key={index}>{text}</li>)}
            </ol>
          )}
        </div>
      ))}

      {canvas && (
        <div className="jl-diagram">
          <p className="muted">Componentes del joblet, tomados de la primera aparición ({canvas.nodes.length} pasos).</p>
          <JobCanvas nodes={canvas.nodes} edges={canvas.edges} />
        </div>
      )}
    </article>
  );
}

function CopyNames({ names }: { names: string[] }) {
  return (
    <div className="jl-copy-row" aria-label="Nombres para copiar">
      <span className="muted">Copia los nombres:</span>
      {names.map((name) => <CopyButton key={name} value={name} />)}
    </div>
  );
}

function CopyButton({ value }: { value: string }) {
  const [state, setState] = useState<"idle" | "copied" | "failed">("idle");
  const onClick = async () => {
    const ok = await copyText(value);
    setState(ok ? "copied" : "failed");
    window.setTimeout(() => setState("idle"), 1500);
  };
  return (
    <button type="button" className="secondary jl-copy" onClick={() => void onClick()} aria-label={`Copiar ${value}`}>
      <code>{value}</code> {state === "copied" ? "· Copiado" : state === "failed" ? "· No se pudo copiar" : ""}
    </button>
  );
}
