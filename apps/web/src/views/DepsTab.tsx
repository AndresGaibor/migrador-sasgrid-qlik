import { api } from "../api";
import { H, W, layout } from "../graph";
import { useAsync } from "../hooks";
import type { Deps } from "../types";
import { Badge, Load } from "./common";

export function DepsTab({ id }: { id: string }) {
  const q = useAsync(() => api.deps(id), [id]);
  return (
    <>
      <h1>Dependencias</h1>
      <Load q={q}>{(d) => <DepsBody d={d} />}</Load>
    </>
  );
}

function DepsBody({ d }: { d: Deps }) {
  const programs = d.processing_order.flat().length;
  const g = layout(d.processing_order, d.edges);
  return (
    <>
      <h2>Procesamiento (datos)</h2>
      <p className="muted">
        Qué programa produce o consume cada dataset. Una columna por capa; los de una misma capa son independientes.
        {" "}{programs} unidades · {d.edges.length} aristas · {d.datasets.length} datasets.
      </p>
      {d.cycles.length > 0 && (
        <p className="error">
          Ciclos (requieren decisión): {d.cycles.map((c) => c.join(" ↔ ")).join("; ")}
        </p>
      )}
      {g.nodes.length > 0 && g.nodes.length <= 150 ? (
        <div className="graph" tabIndex={0} role="img" aria-label="Grafo de procesamiento por capas">
          <svg width={g.width + 4} height={g.height + 4}>
            {g.links.map((l, i) => (
              <path
                key={i}
                d={`M${l.from.x + W},${l.from.y + H / 2} C${l.from.x + W + 40},${l.from.y + H / 2} ${l.to.x - 40},${l.to.y + H / 2} ${l.to.x},${l.to.y + H / 2}`}
                className="edge"
              >
                <title>{l.label}</title>
              </path>
            ))}
            {g.nodes.map((n) => (
              <g key={n.id} transform={`translate(${n.x},${n.y})`}>
                <rect width={W} height={H} rx={4} className="node" />
                <text x={8} y={18}>{n.id.length > 26 ? "…" + n.id.slice(-25) : n.id}</text>
                <title>{n.id}</title>
              </g>
            ))}
          </svg>
        </div>
      ) : (
        <ol>
          {d.processing_order.map((layer, i) => (
            <li key={i}>{layer.join(", ")}</li>
          ))}
        </ol>
      )}

      <h2>Orquestación (Grid)</h2>
      <p className="muted">Tareas de lote y planificación. Es un modelo distinto del de procesamiento.</p>
      {d.orchestration.tasks.length === 0 ? (
        <p>No se detectaron tareas Grid.</p>
      ) : (
        <table>
          <thead><tr><th>Tarea</th><th>Tipo</th><th>Programa</th><th>Cola</th><th>Espera</th><th>Después de</th></tr></thead>
          <tbody>
            {d.orchestration.tasks.map((t) => (
              <tr key={t.id}>
                <td title={`${t.source_file}:${t.line}`}>{t.id}</td>
                <td><Badge>{t.kind}</Badge></td>
                <td>
                  {t.resolved_program ?? "—"} {t.match_status && t.match_status !== "resolved" && <Badge tone="warn">{t.match_status}</Badge>}
                </td>
                <td>{t.queue ?? "—"}</td>
                <td>{t.waits ? "sí" : "no"}</td>
                <td>{t.after.join(", ") || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {d.orchestration.schedules.length > 0 && (
        <ul>{d.orchestration.schedules.map((s, i) => <li key={i}>{s.file}: {s.text}</li>)}</ul>
      )}

      <h2>Sin resolver ({d.unresolved.length})</h2>
      <details>
        <summary>Ver lista</summary>
        <ul>
          {d.unresolved.slice(0, 200).map((u, i) => (
            <li key={i}>{u.kind} <b>{u.name}</b> — {u.file}:{u.line} {u.detail}</li>
          ))}
        </ul>
        {d.unresolved.length > 200 && <p className="muted">… y {d.unresolved.length - 200} más</p>}
      </details>
    </>
  );
}
