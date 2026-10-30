import { useId, useMemo, useState, type KeyboardEvent } from "react";
import { ComponentIcon } from "../components/ComponentIcon";
import { type CanvasEdge, type CanvasNode, type NodeStatus, type PlacedEdge, type PlacedNode, layoutJob, NODE_HEIGHT, NODE_WIDTH } from "./canvas-layout";
import "./studio.css";

export type JobCanvasProps = {
  nodes: CanvasNode[];
  edges: CanvasEdge[];
  /** Id del nodo seleccionado (resaltado). */
  selectedId?: string | null;
  onSelect?: (id: string) => void;
};

const STATUS_LABEL: Record<NodeStatus, string> = {
  pending: "Pendiente",
  in_progress: "En progreso",
  done: "Hecho",
  blocked: "Bloqueado",
};

const ZOOM_MIN = 0.4;
const ZOOM_MAX = 2;
const ZOOM_STEP = 0.2;

/** Clase de color de una conexión: datos, disparador correcto, error u otros disparadores. */
function edgeTone(edge: PlacedEdge): "row" | "reject" | "ok" | "error" | "other" {
  if (edge.kind === "row_reject") return "reject";
  if (edge.isRow) return "row";
  if (edge.kind === "on_subjob_ok" || edge.kind === "on_component_ok") return "ok";
  if (edge.kind === "on_subjob_error" || edge.kind === "on_component_error") return "error";
  return "other";
}

const TONES = ["row", "reject", "ok", "error", "other"] as const;

// Recorta el nombre para que quepa en el nodo; el texto completo va en el aria-label.
const shorten = (text: string, max = 22) => (text.length > max ? `${text.slice(0, max - 1)}…` : text);

function curve(e: PlacedEdge): string {
  const dx = Math.max(40, Math.abs(e.x2 - e.x1) / 2);
  return `M ${e.x1} ${e.y1} C ${e.x1 + dx} ${e.y1}, ${e.x2 - dx} ${e.y2}, ${e.x2} ${e.y2}`;
}

// Lienzo SVG del Job: subjobs como recuadros azul claro, nodos con su icono y conexiones con etiqueta.
export function JobCanvas({ nodes, edges, selectedId = null, onSelect }: JobCanvasProps) {
  const uid = useId();
  const [scale, setScale] = useState(1);
  const layout = useMemo(() => layoutJob(nodes, edges), [nodes, edges]);
  const markerId = (tone: string) => `${uid}-arrow-${tone}`;

  const select = (id: string) => onSelect?.(id);
  const onNodeKey = (id: string) => (event: KeyboardEvent<SVGGElement>) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      select(id);
    }
  };

  if (nodes.length === 0) {
    return <p className="studio-muted">El Job no tiene componentes todavía.</p>;
  }

  return (
    <div className="studio-panel studio-canvas">
      <div className="studio-canvas-toolbar" role="toolbar" aria-label="Zoom del lienzo">
        <button type="button" className="studio-button" aria-label="Alejar" onClick={() => setScale((s) => Math.max(ZOOM_MIN, +(s - ZOOM_STEP).toFixed(2)))}>−</button>
        <span className="studio-canvas-zoom" aria-live="polite">{Math.round(scale * 100)}%</span>
        <button type="button" className="studio-button" aria-label="Acercar" onClick={() => setScale((s) => Math.min(ZOOM_MAX, +(s + ZOOM_STEP).toFixed(2)))}>+</button>
        <button type="button" className="studio-button" onClick={() => setScale(1)}>100%</button>
      </div>
      <div className="studio-canvas-scroll" role="region" aria-label="Lienzo del Job" tabIndex={0}>
        <svg
          className="studio-canvas-svg"
          width={layout.width * scale}
          height={layout.height * scale}
          viewBox={`0 0 ${layout.width} ${layout.height}`}
          role="group"
          aria-label={`Job con ${layout.nodes.length} componentes`}
        >
          <defs>
            {TONES.map((tone) => (
              <marker key={tone} id={markerId(tone)} viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" className={`studio-arrow studio-arrow-${tone}`} />
              </marker>
            ))}
          </defs>

          {layout.boxes.map((box) => (
            <g key={`box-${box.name}`} className="studio-subjob">
              <rect className="studio-subjob-box" x={box.x} y={box.y} width={box.width} height={box.height} rx={6} />
              <text className="studio-subjob-title" x={box.x + 10} y={box.y + 17}>{box.name}</text>
            </g>
          ))}

          {layout.edges.map((edge, i) => {
            const tone = edgeTone(edge);
            return (
              <g key={`edge-${i}`} className={`studio-edge studio-edge-${tone}${edge.isRow ? " is-row" : " is-trigger"}`}>
                <path d={curve(edge)} className="studio-edge-line" markerEnd={`url(#${markerId(tone)})`} />
                <text className="studio-edge-label" x={(edge.x1 + edge.x2) / 2} y={(edge.y1 + edge.y2) / 2 - 6} textAnchor="middle">{edge.label}</text>
              </g>
            );
          })}

          {layout.nodes.map((node: PlacedNode) => {
            const selected = node.id === selectedId;
            return (
              <g
                key={node.id}
                className={`studio-node status-${node.status}${selected ? " is-selected" : ""}`}
                transform={`translate(${node.x} ${node.y})`}
                role="button"
                tabIndex={0}
                aria-label={`${node.label}, ${node.component}, ${STATUS_LABEL[node.status]}`}
                aria-pressed={selected}
                onClick={() => select(node.id)}
                onKeyDown={onNodeKey(node.id)}
              >
                <rect className="studio-node-body" width={NODE_WIDTH} height={NODE_HEIGHT} rx={4} />
                <foreignObject x={8} y={(NODE_HEIGHT - 32) / 2} width={32} height={32}>
                  <div className="studio-node-icon"><ComponentIcon name={node.component} /></div>
                </foreignObject>
                <text className="studio-node-label" x={48} y={23}>{shorten(node.label)}</text>
                <text className="studio-node-component" x={48} y={41}>{node.component}</text>
              </g>
            );
          })}
        </svg>
      </div>
    </div>
  );
}
