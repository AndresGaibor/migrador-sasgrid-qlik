import { Icon } from "../../components/Icon";
import { api } from "../../api";
import { Badge } from "../common";
import { ComponentIcon } from "../../components/ComponentIcon";
import { buildGridGuides } from "../../grid-guide";
import type { GridRecommendation } from "../../types";

function ComponentLink({ name, known }: { name: string; known?: boolean | null }) {
  const base = name.split(" ")[0];
  return known ? <a href={`#/catalogo/${base}`}><code>{name}</code></a> : <code>{name}</code>;
}

export function GridRecommendations({ id, items, isDesktop, staged = false }: { id: string; items: GridRecommendation[]; isDesktop: boolean; staged?: boolean }) {
  const guides = buildGridGuides(items);
  return (
    <section className="orchestration-guides" aria-label="Orquestación y planificación">
      <h2>{staged ? "3. Conecta los Jobs y programa su ejecución" : "Dependencias y programación"}</h2>
      <p className="migration-stage-description">{staged ? "Hazlo después de completar y probar los Jobs del paso 2. " : "Primero completa y prueba los Jobs hijos. "}Revisa los Jobs principales que llaman a otros; después configura el calendario en Qlik Talend Cloud.</p>
      <p className="orchestration-reuse-note"><Icon name="info" size={17} /><span>Si MCP ya creó un Job principal y sus conexiones, verifica esa estructura en Studio; no la crees otra vez. Las instrucciones siguientes también sirven para construirla manualmente.</span></p>
      {guides.map((g, gi) => (
        <details className="panel plan-orchestration-card" key={g.key} open={!isDesktop && gi === 0}>
          <summary><span className="orchestration-summary"><b>{g.title}</b><small>{g.actions.length} pasos</small></span> <Badge tone={g.kind === "manual" ? "warn" : "ok"}>{g.kind === "build" ? "Talend Studio" : g.kind === "cloud" ? "Qlik Talend Cloud" : "Validar con Operaciones"}</Badge></summary>
          <div className="orchestration-intro"><p>{g.intro}</p><div>{g.component && <span className="orchestration-component"><ComponentIcon name={g.component} /> <ComponentLink name={g.component} known /></span>} {g.doc_url && <a href={g.doc_url} target="_blank" rel="noreferrer">Documentación oficial <Icon name="external" size={13} /></a>}</div></div>
          <ol className="orchestration-steps">
            {g.actions.map((a, n) => (
              <li key={n}>
                <div className="orchestration-step-heading"><span className="orchestration-step-number" aria-hidden="true">{n + 1}</span><h3>{a.text.replace(/^Paso \d+: /, "")}</h3></div>
                <div className="orchestration-step-body">
                {a.where && <div className="orchestration-location"><strong>Dónde</strong><p>{a.where}</p></div>}
                {a.fields && <dl className="orchestration-fields">{a.fields.map(([k, v], index) => <div key={`${k}:${index}`}><dt>{k}</dt><dd><code>{v}</code></dd></div>)}</dl>}
                {a.note && <p className="orchestration-note"><Icon name="info" size={16} /><span>{a.note}</span></p>}
                {a.doc_url && <p className="guide-official-link"><a href={a.doc_url} target="_blank" rel="noreferrer">Consultar documentación de este paso <Icon name="external" size={13} /></a></p>}
                </div>
              </li>
            ))}
          </ol>
          <details className="orchestration-sources"><summary>Referencias en el SAS ({g.sources.length})</summary><ul>{g.sources.map((r) => <li key={r.id}><a href={api.sourceEvidence(id, r.evidence.file, r.evidence.line)} target="_blank" rel="noreferrer">{r.evidence.file.split("/").pop()} · línea {r.evidence.line}</a></li>)}</ul></details>
        </details>
      ))}
    </section>
  );
}
