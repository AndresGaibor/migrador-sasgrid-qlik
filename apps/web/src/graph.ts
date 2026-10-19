import type { DataEdge } from "./types";

export type Node = { id: string; x: number; y: number };
export type Link = { from: Node; to: Node; label: string };

export const W = 190;
export const H = 62;
const GAP_X = 70;
const GAP_Y = 26;

/** Una columna por capa de procesamiento; solo aristas de datos entre nodos visibles. */
export function layout(layers: string[][], edges: DataEdge[]) {
  const nodes = new Map<string, Node>();
  layers.forEach((layer, c) =>
    layer.forEach((id, r) => nodes.set(id, { id, x: c * (W + GAP_X), y: r * (H + GAP_Y) })),
  );
  const links: Link[] = [];
  for (const e of edges) {
    const from = nodes.get(e.source);
    const to = nodes.get(e.target);
    if (from && to && e.kind === "data") links.push({ from, to, label: e.datasets.join(", ") });
  }
  const width = layers.length * (W + GAP_X) - GAP_X;
  const height = Math.max(0, ...layers.map((l) => l.length)) * (H + GAP_Y);
  return { nodes: [...nodes.values()], links, width: Math.max(width, 0), height };

