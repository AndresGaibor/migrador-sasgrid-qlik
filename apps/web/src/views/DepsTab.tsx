import { api } from "../api";
import { useState } from "react";
import { Icon } from "../components/Icon";
import { H, W, layout } from "../graph";
import { useAsync } from "../hooks";
import type { Deps } from "../types";
import { Badge, Load, link } from "./common";

export function DepsTab({ id }: { id: string }) {
  const q = useAsync(() => api.deps(id), [id]);
  return (
    <>
      <h1>Explora tu flujo de datos</h1>
      <p className="subtitle">Descubre cómo se conectan tus programas y en qué orden se pueden ejecutar.</p>
      <Load q={q}>{(d) => <DepsBody d={d} id={id} />}</Load>
    </>
  );
}

function DepsBody({ d, id }: { d: Deps; id: string }) {
  const [zoom, setZoom] = useState(1);
  const programs = d.processing_order.flat().length;
  const g = layout(d.processing_order, d.edges);
  return (
    <>
      <h2>Conexiones entre programas</h2>
      <p className="muted">
        Cada tarjeta es un programa y cada línea representa datos compartidos. Lee el flujo de izquierda a derecha; los programas de una misma columna pueden ejecutarse de forma independiente.
      </p>
      {d.cycles.length > 0 && (
        <p className="error">
          Ciclos (requieren decisión): {d.cycles.map((c) => c.join(" ↔ ")).join("; ")}
        </p>
      )}
      <div className="graph-toolbar"><span className="muted">{programs} programas · {d.edges.length} conexiones · {d.datasets.length} conjuntos de datos</span><div className="zoom-controls"><button className="secondary" aria-label="Alejar flujo" disabled={zoom <= .5} onClick={() => setZoom(Math.max(.5, zoom - .25))}>−</button><button className="secondary" onClick={() => setZoom(1)} title="Restablecer tamaño">{Math.round(zoom * 100)}%</button><button className="secondary" aria-label="Acercar flujo" disabled={zoom >= 2} onClick={() => setZoom(Math.min(2, zoom + .25))}>+</button></div></div>
      {g.nodes.length === 0 ? <div className="empty-state"><Icon name="flow" size={32} /><h3>Aún no hay un flujo para mostrar</h3><p>Carga y analiza tus programas desde el resumen del proyecto.</p><a className="button" href={link(id, "resumen")}>Ir al resumen <Icon name="arrow" size={17} /></a></div> : g.nodes.length <= 150 ? (
        <div className="graph" tabIndex={0} role="region" aria-label="Flujo de datos. Selecciona un programa para ver su análisis.">
          <svg width={(g.width + 12) * zoom} height={(g.height + 12) * zoom} viewBox={`-6 -6 ${g.width + 12} ${g.height + 12}`}>
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
              <a key={n.id} href={link(id, "programas", n.id)} aria-label={`Ver programa ${n.id}`}>
              <g transform={`translate(${n.x},${n.y})`}>
                <rect width={W} height={H} rx={7} className="node" />
                <text x={13} y={26}>{n.id.length > 26 ? "…" + n.id.slice(-25) : n.id}</text>
                <text x={13} y={45} className="node-caption">Programa SAS · Ver análisis</text>
                <circle cx={0} cy={H / 2} r={4} className="node-port" />
                <circle cx={W} cy={H / 2} r={4} className="node-port" />
                <title>{n.id}</title>
              </g>
              </a>
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

      <h2>Orden de ejecución en SAS Grid</h2>
      <p className="muted">Tareas programadas y condiciones de espera que coordinan la ejecución de tus programas.</p>
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

      <h2>Conexiones por revisar ({d.unresolved.length})</h2>
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
