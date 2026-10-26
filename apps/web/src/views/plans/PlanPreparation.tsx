import type { JobPlan } from "../../types";
import { toContext } from "../../step-guide";

export function PlanPreparation({ plan }: { plan: JobPlan }) {
  const { libraries_needed: libraries, context_variables: contexts } = plan;
  if (!libraries.length && !contexts.length) return null;

  const csvDirectories = libraries.filter((library) => !library.engine && library.path);
  const values = [
    ...csvDirectories.map((library) => `context.${library.sas_name.toUpperCase()}_DIR = ${library.path}   (carpeta donde guardarás los CSV de esta librería)`),
    ...contexts.map((context) => `${toContext("&" + context.name)}${context.sas_value ? ` = ${context.sas_value}` : "   (el valor te lo da el equipo)"}`),
  ];

  return <div className="panel">
    <h2>Antes de empezar (una sola vez)</h2>
    <ol className="do-list">
      <li><b>Crea el Job.</b><div className="muted">Dónde: Repository → Job Designs → clic derecho → Create Job → Name:</div><pre className="do-value">{plan.job_name}</pre></li>
      {libraries.map((library) => <li key={library.sas_name}>
        <b>{library.engine ? `Crea la conexión «${library.sas_name}».` : `«${library.sas_name}» son archivos: guárdalos como CSV (no hace falta conexión).`}</b>
        {library.engine ? <div className="muted">Dónde: Repository → Metadata → clic derecho en el tipo de conexión → Create. Tipo sugerido: {library.suggested_connection}. Motor SAS: {library.engine}. {library.path ? `Ruta o servicio en SAS: ${library.path}. ` : ""}Pide las credenciales al equipo; no se copian del SAS.</div> : <div className="muted">Se usa la variable de contexto que creas más abajo.</div>}
      </li>)}
      {values.length > 0 && <li><b>Crea estas variables de contexto.</b><div className="muted">Dónde: pestaña Contexts del Job → «+» por cada una. Tipo: String.</div><pre className="do-value">{values.join("\n")}</pre></li>}
    </ol>
  </div>;
}
