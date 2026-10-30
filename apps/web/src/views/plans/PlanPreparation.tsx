import type { JobPlan } from "../../types";
import { ContextTable } from "../../studio/ContextTable";
import { contextRows } from "../../studio/context-model";

export function PlanPreparation({ plan }: { plan: JobPlan }) {
  const { libraries_needed: libraries, context_variables: contexts } = plan;
  if (!libraries.length && !contexts.length) return null;

  const rows = contextRows(plan);

  return <div className="panel">
    <h2>Antes de empezar (una sola vez)</h2>
    <ol className="do-list">
      <li><b>Crea el Job.</b><div className="muted">Dónde: Repository → Job Designs → clic derecho → Create Job → Name:</div><pre className="do-value">{plan.job_name}</pre></li>
      {libraries.map((library) => <li key={library.sas_name}>
        <b>{library.engine ? `Crea la conexión «${library.sas_name}».` : `«${library.sas_name}» son archivos: guárdalos como CSV (no hace falta conexión).`}</b>
        {library.engine ? <div className="muted">Dónde: Repository → Metadata → clic derecho en el tipo de conexión → Create. Tipo sugerido: {library.suggested_connection}. Motor SAS: {library.engine}. {library.path ? `Ruta o servicio en SAS: ${library.path}. ` : ""}Pide las credenciales al equipo; no se copian del SAS.</div> : <div className="muted">Se usa la variable de contexto que creas más abajo.</div>}
      </li>)}
      {rows.length > 0 && <li><b>Crea las variables de contexto.</b><div className="muted">Dónde: pestaña Contexts del Job. Así debe quedar la tabla en Studio:</div><ContextTable rows={rows} /></li>}
    </ol>
  </div>;
}
