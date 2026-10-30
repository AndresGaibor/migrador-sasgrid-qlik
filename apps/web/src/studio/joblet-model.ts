// Lógica pura de la guía de joblets: tabla de parámetros, pasos del diagrama y nombres a copiar.
import type { JobPlan, JobletPlan, Step } from "../types";

export type ParameterRow = {
  name: string;
  context_variable: string;
  /** Valor en cada aparición, en el mismo orden que `joblet.occurrences`. Cadena vacía si falta. */
  values: string[];
};

/** Pasos del Job principal y de los Jobs hijos (macros). */
export function allPlanSteps(plan: JobPlan): Step[] {
  return [...plan.steps, ...plan.children.flatMap((child) => child.steps)];
}

/** Una fila por parámetro; una celda por aparición. */
export function parameterRows(joblet: JobletPlan): ParameterRow[] {
  return joblet.parameters.map((parameter) => ({
    name: parameter.name,
    context_variable: parameter.context_variable,
    values: joblet.occurrences.map((occurrence) => occurrence.values[parameter.name] ?? ""),
  }));
}

/** Pasos de la primera aparición que existen en el plan, en su orden. */
export function diagramSteps(joblet: JobletPlan, steps: Step[]): Step[] {
  const ids = new Set(joblet.occurrences[0]?.step_ids ?? []);
  return steps.filter((step) => ids.has(step.id)).sort((a, b) => a.order - b.order);
}

/** El mini-diagrama solo se dibuja con al menos dos pasos. */
export function showDiagram(joblet: JobletPlan, steps: Step[]): boolean {
  return diagramSteps(joblet, steps).length >= 2;
}

/** Nombres que el usuario copia al crear el joblet: el nombre del joblet y cada parámetro (nombre de la variable de contexto). */
export function copyableNames(joblet: JobletPlan): string[] {
  return [...new Set([joblet.name, ...joblet.parameters.map((p) => p.name)])];
}

export function occurrenceLabel(count: number): string {
  return count === 1 ? "1 aparición" : `${count} apariciones`;
}

export function kindLabel(kind: JobletPlan["kind"]): string {
  return kind === "macro" ? "Desde una macro" : "Desde pasos consecutivos";
}
