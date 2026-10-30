// Layout determinista del lienzo del Job: de izquierda a derecha por capas, con subjobs en bandas apiladas.
// Pura: no toca el DOM ni React.

export type NodeStatus = "pending" | "in_progress" | "done" | "blocked";

export type CanvasNode = {
  id: string;
  label: string;
  component: string;
  /** Subjob al que pertenece. Los nodos con el mismo subjob se agrupan en un recuadro. */
  subjob?: string;
  status: NodeStatus;
};

export type EdgeKind =
  | "row_main"
  | "row_lookup"
  | "row_reject"
  | "on_subjob_ok"
  | "on_subjob_error"
  | "on_component_ok"
  | "on_component_error"
  | "run_if"
  | "iterate";

export type CanvasEdge = { from: string; to: string; kind: EdgeKind };

export type PlacedNode = CanvasNode & { x: number; y: number; layer: number };

export type PlacedEdge = CanvasEdge & {
  /** Punto de salida (borde derecho del nodo origen) y de llegada (borde izquierdo del destino). */
  x1: number;
  y1: number;
  x2: number;
  y2: number;
  /** Etiqueta de la conexión, por ejemplo «row1 (Main)» o «On Subjob Ok». */
  label: string;
  /** true para conexiones de datos (línea continua); false para disparadores (punteada). */
  isRow: boolean;
};

export type SubjobBox = { name: string; x: number; y: number; width: number; height: number };

export type CanvasLayout = {
  nodes: PlacedNode[];
  edges: PlacedEdge[];
  boxes: SubjobBox[];
  width: number;
  height: number;
};

export const NODE_WIDTH = 180;
export const NODE_HEIGHT = 56;
const COLUMN_GAP = 90;
const ROW_GAP = 20;
const BOX_PAD = 16;
const BOX_TITLE = 26;
const BAND_GAP = 36;
const MARGIN = 24;

const EDGE_LABELS: Record<EdgeKind, string> = {
  row_main: "Main",
  row_lookup: "Lookup",
  row_reject: "Reject",
  on_subjob_ok: "On Subjob Ok",
  on_subjob_error: "On Subjob Error",
  on_component_ok: "On Component Ok",
  on_component_error: "On Component Error",
  run_if: "Run if",
  iterate: "Iterate",
};

/** Orden topológico (estable por orden de entrada) y capas, ignorando las aristas que cierran ciclos. */
function layerNodes(ids: string[], edges: CanvasEdge[]) {
  const index = new Map(ids.map((id, i) => [id, i]));
  const out = new Map<number, number[]>();
  ids.forEach((_, i) => out.set(i, []));
  edges.forEach((e, k) => out.get(index.get(e.from)!)!.push(k));

  // DFS para marcar las aristas de retorno (ciclos); se ignoran al calcular capas.
  const state = new Array<number>(ids.length).fill(0);
  const back = new Set<number>();
  const visit = (v: number) => {
    state[v] = 1;
    for (const k of out.get(v)!) {
      const w = index.get(edges[k].to)!;
      if (state[w] === 1) back.add(k);
      else if (state[w] === 0) visit(w);
    }
    state[v] = 2;
  };
  for (let v = 0; v < ids.length; v++) if (state[v] === 0) visit(v);

  const kept = edges.map((_, k) => k).filter((k) => !back.has(k));
  const indegree = new Array<number>(ids.length).fill(0);
  for (const k of kept) indegree[index.get(edges[k].to)!]++;

  const order: number[] = [];
  const done = new Array<boolean>(ids.length).fill(false);
  while (order.length < ids.length) {
    // Siguiente nodo sin dependencias pendientes, por orden de entrada.
    const v = ids.findIndex((_, i) => !done[i] && indegree[i] === 0);
    if (v === -1) break; // no debería ocurrir: las aristas de retorno están fuera
    done[v] = true;
    order.push(v);
    for (const k of out.get(v)!) {
      if (!back.has(k)) indegree[index.get(edges[k].to)!]--;
    }
  }

  const topo = new Array<number>(ids.length).fill(0);
  order.forEach((v, pos) => (topo[v] = pos));
  const layer = new Array<number>(ids.length).fill(0);
  for (const v of order) {
    for (const k of out.get(v)!) {
      if (back.has(k)) continue;
      const w = index.get(edges[k].to)!;
      layer[w] = Math.max(layer[w], layer[v] + 1);
    }
  }
  return { layer, topo, index, back };
}

/** Calcula posiciones, recuadros de subjob y trazado de las conexiones. */
export function layoutJob(inputNodes: CanvasNode[], inputEdges: CanvasEdge[]): CanvasLayout {
  // Un id repetido se ignora: gana la primera aparición.
  const seen = new Set<string>();
  const nodes: CanvasNode[] = [];
  for (const n of inputNodes) {
    if (seen.has(n.id)) continue;
    seen.add(n.id);
    nodes.push(n);
  }
  const ids = nodes.map((n) => n.id);
  const edges = inputEdges.filter((e) => e.from !== e.to && seen.has(e.from) && seen.has(e.to));
  if (nodes.length === 0) return { nodes: [], edges: [], boxes: [], width: MARGIN * 2, height: MARGIN * 2 };

  const { layer, topo, index } = layerNodes(ids, edges);

  // Bandas: un grupo por subjob (o uno compartido para los nodos sin subjob), ordenadas por su primer nodo.
  const groups = new Map<string, number[]>();
  nodes.forEach((n, i) => {
    const key = n.subjob ? `s:${n.subjob}` : "";
    groups.set(key, [...(groups.get(key) ?? []), i]);
  });
  const bands = [...groups.entries()]
    .map(([key, members]) => ({ key, members, first: Math.min(...members.map((i) => topo[i])) }))
    .sort((a, b) => a.first - b.first);

  const placed = new Array<PlacedNode>(nodes.length);
  const boxes: SubjobBox[] = [];
  let bandTop = MARGIN;

  for (const band of bands) {
    const boxed = band.key !== "";
    const inner = boxed ? BOX_PAD + BOX_TITLE : 0;
    const columns = new Map<number, number[]>();
    for (const i of band.members) columns.set(layer[i], [...(columns.get(layer[i]) ?? []), i]);
    for (const members of columns.values()) members.sort((a, b) => topo[a] - topo[b]);

    const tallest = Math.max(...[...columns.values()].map((c) => c.length));
    // Contenido de la banda más el marco del subjob (cabecera arriba, padding abajo).
    const content = tallest * (NODE_HEIGHT + ROW_GAP) - ROW_GAP;
    const bandHeight = content + (boxed ? inner + BOX_PAD : 0);

    for (const [col, members] of columns) {
      members.forEach((i, k) => {
        const x = MARGIN + col * (NODE_WIDTH + COLUMN_GAP) + (boxed ? BOX_PAD : 0);
        const y = bandTop + (boxed ? BOX_PAD + BOX_TITLE : 0) + k * (NODE_HEIGHT + ROW_GAP);
        placed[i] = { ...nodes[i], x, y, layer: col };
      });
    }

    if (boxed) {
      const members = band.members.map((i) => placed[i]);
      const left = Math.min(...members.map((n) => n.x)) - BOX_PAD;
      const right = Math.max(...members.map((n) => n.x + NODE_WIDTH)) + BOX_PAD;
      boxes.push({ name: band.key.slice(2), x: left, y: bandTop, width: right - left, height: bandHeight });
    }
    bandTop += bandHeight + BAND_GAP;
  }

  // Trazado: la numeración de filas «rowN» sigue el orden de las conexiones de datos desde cada origen.
  const rowCounter = new Map<string, number>();
  const placedEdges: PlacedEdge[] = edges.map((e) => {
    const from = placed[index.get(e.from)!];
    const to = placed[index.get(e.to)!];
    const isRow = e.kind.startsWith("row_");
    let label = EDGE_LABELS[e.kind];
    if (isRow) {
      const n = (rowCounter.get(e.from) ?? 0) + 1;
      rowCounter.set(e.from, n);
      label = `row${n} (${label})`;
    }
    return {
      ...e,
      x1: from.x + NODE_WIDTH,
      y1: from.y + NODE_HEIGHT / 2,
      x2: to.x,
      y2: to.y + NODE_HEIGHT / 2,
      label,
      isRow,
    };
  });

  const width = Math.max(...placed.map((n) => n.x + NODE_WIDTH), ...boxes.map((b) => b.x + b.width)) + MARGIN;
  const height = Math.max(...placed.map((n) => n.y + NODE_HEIGHT), ...boxes.map((b) => b.y + b.height)) + MARGIN;
  return { nodes: placed, edges: placedEdges, boxes, width, height };
}
