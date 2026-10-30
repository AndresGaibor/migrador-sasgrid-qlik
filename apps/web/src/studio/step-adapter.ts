// Puente entre los pasos del planificador (Step) y los componentes que replican Talend Studio.
import { decodeProgress, type GuideProgress } from "../guide-progress";
import { datasetConfig } from "../step-guide";
import type { Step } from "../types";
import type { CanvasEdge, CanvasNode, EdgeKind, NodeStatus } from "./canvas-layout";
import type { GuideValues } from "./panel-types";

/** Componente que debe usar el paso: el del planificador o, si lo dejó «por_determinar», el que deduce la guía. */
export function effectiveComponent(step: Step): string {
  // Un uso de joblet no es un componente del catálogo: el lienzo muestra el nombre del joblet.
  const joblet = step.joblet_id ? step.purpose.match(/^Usa el joblet (\S+)/)?.[1] : undefined;
  if (joblet) return joblet;
  const comp = step.component_candidate.split(" ")[0] ?? "";
  return comp === "por_determinar" ? (datasetConfig(step)?.component ?? comp) : comp;
}

/** Valores sugeridos para el panel: cada propiedad del paso es un parámetro Talend (FILENAME, QUERY…). */
export function stepGuideValues(step: Step): GuideValues {
  const values: GuideValues = {};
  for (const [name, value] of Object.entries(datasetConfig(step)?.values ?? {})) values[name] = { value };
  for (const p of step.properties) {
    if (p.value === null || p.value === "") continue;
    values[p.name] = { value: p.value, why: p.origin ? `Origen: ${p.origin}` : undefined };
  }
  if (step.schema_columns?.length) {
    values.SCHEMA = {
      rows: step.schema_columns.map((c) => ({ name: c.name, type: c.talend_type ?? "id_String" })),
      why: "Columnas derivadas del SAS. Revisa tipos y longitudes en el editor de esquema.",
    };
  }
  return values;
}

const PROGRESS_TO_NODE: Record<GuideProgress, NodeStatus> = {
  pending: "pending",
  in_progress: "in_progress",
  completed: "done",
  blocked: "blocked",
};

const EDGE_KINDS: Record<string, EdgeKind> = {
  main: "row_main",
  lookup: "row_lookup",
  reject: "row_reject",
  filter: "row_main",
  onsubjobok: "on_subjob_ok",
  onsubjoberror: "on_subjob_error",
  oncomponentok: "on_component_ok",
  oncomponenterror: "on_component_error",
  runif: "run_if",
  iterate: "iterate",
};

/** Normaliza «OnSubjobOk», «On Subjob Ok» o «on_subjob_ok» al mismo tipo de conexión. */
export function edgeKind(type: string): EdgeKind {
  return EDGE_KINDS[type.toLowerCase().replace(/[^a-z]/g, "")] ?? "row_main";
}

/** Nodos y conexiones del lienzo de un Job. Las conexiones apuntan al paso que las recibe. */
export function jobCanvas(steps: Step[]): { nodes: CanvasNode[]; edges: CanvasEdge[] } {
  const ids = new Set(steps.map((s) => s.id));
  // Sin título de negocio, el subjob sale como «Bloque n» (el mismo nombre que usan las tarjetas), no como «s15».
  const blockNumber = new Map<string, number>();
  for (const s of steps) if (!s.business_subjob && !blockNumber.has(s.subjob)) blockNumber.set(s.subjob, blockNumber.size + 1);
  const nodes = steps.map((s): CanvasNode => ({
    id: s.id,
    label: s.purpose,
    component: effectiveComponent(s),
    subjob: s.business_subjob ?? `Bloque ${blockNumber.get(s.subjob)}`,
    status: PROGRESS_TO_NODE[decodeProgress(s.status, s.note).state],
  }));
  const edges = steps.flatMap((s) =>
    s.connections
      .filter((c): c is { type: string; from_step: string } => c.from_step !== null && ids.has(c.from_step))
      .map((c): CanvasEdge => ({ from: c.from_step, to: s.id, kind: edgeKind(c.type) })),
  );
  return { nodes, edges };
}
