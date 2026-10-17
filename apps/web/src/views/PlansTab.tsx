import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { STATUSES, type JobPlan, type Step } from "../types";
import { Badge, Load, link } from "./common";

export function PlansTab({ id, file }: { id: string; file?: string }) {
  return file ? <PlanDetail id={id} file={decodeURI(file)} /> : <PlanList id={id} />;
}

function PlanList({ id }: { id: string }) {
  const q = useAsync(() => api.plans(id), [id]);
  const [busy, setBusy] = useState(false);
  const gen = async () => {
    setBusy(true);
    try {
      await api.generatePlans(id);
      q.reload();
    } finally {
      setBusy(false);
    }
  };
  return (
    <>
      <h1>Planes de migración</h1>
      <button onClick={gen} disabled={busy}>{busy ? "Generando…" : "Generar / regenerar planes"}</button>
      <p className="muted">Regenerar conserva las decisiones por paso.</p>
      {q.error?.includes("generados") ? (
        <p>Aún no hay planes. Genéralos con el botón.</p>
      ) : (
        <Load q={q}>
          {(rows) => (
            <table>
              <thead><tr><th>Job</th><th>Programa</th><th>Estado</th><th>Pasos</th><th>Con pendientes</th><th>Cerrados</th></tr></thead>
              <tbody>
                {rows.map((r) => (
                  <tr key={r.program}>
                    <td><a href={link(id, "planes", r.program)}>{r.job_name}</a></td>
                    <td>{r.program}</td>
                    <td><Badge tone={r.job_status === "proposed" ? "ok" : "warn"}>{r.job_status}</Badge></td>
                    <td className="num">{r.steps}</td>
                    <td className="num">{r.pending}</td>
                    <td className="num">{r.done}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </Load>
      )}
    </>
  );
}

function PlanDetail({ id, file }: { id: string; file: string }) {
  const q = useAsync(() => api.plan(id, file), [id, file]);
  const [override, setOverride] = useState<JobPlan>();
  const plan = override ?? q.data;
  const decide = async (s: Step, status: string, note: string | null) => setOverride(await api.decide(id, file, s.id, status, note));
  return (
    <>
      <p><a href={link(id, "planes")}>← Planes</a></p>
      <Load q={{ ...q, data: plan }}>
        {(p) => (
          <>
            <h1>{p.job_name}</h1>
            <p className="muted">
              {p.program} · Los componentes y propiedades son candidatos hasta verificarlos en Talend.
            </p>
            {p.context_variables.length > 0 && (
              <>
                <h2>Variables de contexto</h2>
                <ul>{p.context_variables.map((c) => <li key={c.name}><code>{c.suggested}</code> ← {c.name} {c.sas_value && <>= <code>{c.sas_value}</code></>}</li>)}</ul>
              </>
            )}
            {p.libraries_needed.length > 0 && (
              <>
                <h2>Conexiones a crear</h2>
                <ul>{p.libraries_needed.map((l) => <li key={l.sas_name}><code>{l.sas_name}</code> ({l.engine ?? "BASE"}{l.path && `, ${l.path}`}) → {l.suggested_connection}</li>)}</ul>
              </>
            )}
            <h2>Pasos</h2>
            {p.steps.map((s) => <StepCard key={s.id} s={s} onDecide={decide} />)}
            {p.children.map((c) => (
              <section key={c.name}>
                <h2>Job hijo para %{c.name}({c.params.join(", ")})</h2>
                {c.steps.map((s) => <StepCard key={s.id} s={s} onDecide={decide} />)}
              </section>
            ))}
            {p.validation_cases.length > 0 && (
              <>
                <h2>Casos de validación</h2>
                <ul>{p.validation_cases.map((v) => <li key={v.id}><code>{v.id}</code> ({v.kind}): {v.description}</li>)}</ul>
              </>
            )}
            {p.unresolved.length > 0 && (
              <details><summary>Sin resolver ({p.unresolved.length})</summary><ul>{p.unresolved.map((u, i) => <li key={i}>{u}</li>)}</ul></details>
            )}
          </>
        )}
      </Load>
    </>
  );
}

function StepCard({ s, onDecide }: { s: Step; onDecide: (s: Step, status: string, note: string | null) => Promise<void> }) {
  const [note, setNote] = useState(s.note ?? "");
  const [err, setErr] = useState<string>();
  const save = (status: string) => onDecide(s, status, note || null).catch((e: Error) => setErr(e.message));
  return (
    <article className="step">
      <h3>{s.order}. {s.purpose}</h3>
      <p>
        <code>{s.component_candidate}</code> <Badge tone={s.verified ? "ok" : "warn"}>{s.verified ? "verificado" : "sin verificar"}</Badge>{" "}
        <span className="muted">{s.evidence.file}:{s.evidence.line} · subjob {s.subjob} · confianza {s.confidence}</span>
      </p>
      {s.alternatives.length > 0 && <p className="muted">Alternativas: {s.alternatives.join(", ")}</p>}
      {s.connections.length > 0 && <p>Conexiones: {s.connections.map((c) => `${c.type}${c.from_step ? " ← " + c.from_step : ""}`).join(", ")}</p>}
      {s.properties.length > 0 && (
        <ul>{s.properties.map((p) => <li key={p.name}><code>{p.name}</code> = {p.value ? <code>{p.value}</code> : <i>por configurar</i>} <span className="muted">({p.origin})</span></li>)}</ul>
      )}
      {s.expressions.map((e, i) => (
        <p key={i}>
          SAS <code>{e.sas}</code> → {e.talend ? <code>{e.talend}</code> : <i>sin traducción automática</i>}
          {e.warnings.map((w, j) => <span key={j} className="warn-text"> ⚠ {w}</span>)}
        </p>
      ))}
      {s.pending.length > 0 && <><b>Pendientes</b><ul>{s.pending.map((x, i) => <li key={i}>{x}</li>)}</ul></>}
      {s.assumptions.length > 0 && <p className="muted">Supuestos: {s.assumptions.join("; ")}</p>}
      <div className="row">
        <label>
          Estado
          <select value={s.status} onChange={(e) => save(e.target.value)}>
            {STATUSES.map((x) => <option key={x}>{x}</option>)}
          </select>
        </label>
        <label className="grow">
          Nota
          <input value={note} onChange={(e) => setNote(e.target.value)} onBlur={() => note !== (s.note ?? "") && save(s.status)} />
        </label>
      </div>
      {err && <p className="error" role="alert">{err}</p>}
    </article>
  );
}
