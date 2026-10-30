import { copyText } from "./clipboard";
import { CONTEXT_ENVS, contextEnvs, contextSummary, type ContextRow } from "./context-model";
import "./studio-contexts.css";

const cell = (value: string | null | undefined) => (value ? <code>{value}</code> : <span className="muted">—</span>);

/** Réplica de la pestaña Contexts del Job: Name / Type / Comment / Default y una columna por ambiente. */
export function ContextTable({ rows }: { rows: ContextRow[] }) {
  if (rows.length === 0) return null;
  const envs = contextEnvs(rows);
  const { total, secrets, pending } = contextSummary(rows);
  const tsv = rows.map((r) => [r.name, r.type, r.comment, r.value].join("\t")).join("\n");
  return <div className="studio-contexts">
    <ol className="studio-contexts-how">
      <li>Abre el Job y entra en la pestaña <b>Contexts</b> (abajo, junto a Run).</li>
      {envs.length > 0
        ? <li>Pulsa <b>Create contexts group</b> o el botón de la esquina superior derecha y añade los ambientes <b>{envs.join(", ")}</b> con <b>Configure Contexts…</b> → <b>New</b>.</li>
        : <li>Deja el ambiente <b>Default</b>: este SAS no distingue ambientes.</li>}
      <li>Pulsa <b>«+»</b> una vez por variable, escribe su <b>Name</b> sin el prefijo <code>context.</code> y elige el <b>Type</b> de la tabla.</li>
      <li>Las que dicen <b>Password</b> son secretos: el valor lo da el equipo y no se copia del SAS.</li>
    </ol>
    <p className="studio-contexts-summary" role="status">{total} variables · {secrets} secretos · {pending} sin valor todavía</p>
    <div className="studio-contexts-wrap">
      <table className="studio-contexts-table">
        <thead><tr><th>Name</th><th>Type</th><th>Comment</th><th>Default</th>{CONTEXT_ENVS.filter((e) => envs.includes(e)).map((e) => <th key={e}>{e}</th>)}</tr></thead>
        <tbody>
          {rows.map((r) => <tr key={r.name} className={r.needsValue ? "needs-value" : undefined}>
            <td><code>{r.name}</code></td>
            <td><span className={`studio-type${r.secret ? " secret" : ""}`}>{r.type}</span></td>
            <td className="muted">{r.comment}</td>
            <td>{r.secret ? <span className="studio-pending">Lo da el equipo</span> : r.needsValue ? <span className="studio-pending">Falta el valor</span> : cell(r.value)}</td>
            {CONTEXT_ENVS.filter((e) => envs.includes(e)).map((e) => <td key={e}>{r.secret ? <span className="muted">—</span> : cell(r.envs?.[e])}</td>)}
          </tr>)}
        </tbody>
      </table>
    </div>
    <button type="button" className="secondary" onClick={() => void copyText(tsv)}>Copiar la tabla</button>
  </div>;
}
