// Lógica pura del panel: filas por numRow, parámetros visibles y progreso. Sin React.
import { isParamVisible, type ValueMap } from "./show-if";
import type { DoneFields, GuideValues, Param } from "./panel-types";

/** Studio dibuja estos campos sin etiqueta en el XML; se muestra la que ve el usuario. */
export function paramLabel(param: Param): string {
  if (param.label) return param.label;
  if (param.field === "PROPERTY_TYPE") return "Property Type";
  if (param.field === "SCHEMA_TYPE") return /REJECT/i.test(param.name) ? "Schema (reject)" : "Schema";
  return param.name;
}

/** Valores por defecto de los parámetros (defaultValue), para SHOW_IF. */
export function defaultsOf(params: Param[]): ValueMap {
  const out: ValueMap = {};
  for (const p of params) if (p.defaultValue != null) out[p.name] = p.defaultValue;
  return out;
}

/** Valores sugeridos por la guía, para SHOW_IF. Los campos sin sugerencia no aparecen. */
export function suggestedValueMap(values: GuideValues): ValueMap {
  const out: ValueMap = {};
  for (const [name, v] of Object.entries(values)) if (v.value !== undefined) out[name] = v.value;
  return out;
}

/** Hay sugerencia si la guía dio un valor (aunque sea vacío) o filas de tabla. */
export function hasSuggestion(name: string, values: GuideValues): boolean {
  const v = values[name];
  return v !== undefined && (v.value !== undefined || (v.rows !== undefined && v.rows.length > 0));
}

/** Valor que muestra el control: la sugerencia si existe; si no, el defaultValue del parámetro. */
export function displayValue(param: Param, values: GuideValues): string {
  return values[param.name]?.value ?? param.defaultValue ?? "";
}

/** Parámetros que se ven con los valores actuales (SHOW_IF / NOT_SHOW_IF), en su orden original. */
export function visibleParams(params: Param[], values: GuideValues): Param[] {
  const current = suggestedValueMap(values);
  const defaults = defaultsOf(params);
  return params.filter((p) => isParamVisible(p, current, defaults));
}

/**
 * Agrupa los parámetros en filas como Studio: los que comparten numRow van en la misma fila.
 * Las filas siguen el orden de numRow; los parámetros sin numRow van al final, cada uno en su fila.
 * El orden relativo dentro de una misma fila se conserva.
 */
export function groupByRow(params: Param[]): Param[][] {
  const sorted = params
    .map((p, index) => ({ p, index }))
    .sort((a, b) => (a.p.numRow ?? Number.POSITIVE_INFINITY) - (b.p.numRow ?? Number.POSITIVE_INFINITY) || a.index - b.index)
    .map((x) => x.p);
  const rows: Param[][] = [];
  for (const p of sorted) {
    const last = rows[rows.length - 1];
    if (last && p.numRow !== null && last[0].numRow === p.numRow) last.push(p);
    else rows.push([p]);
  }
  return rows;
}

export type TabProgress = {
  /** Campos con sugerencia marcados como hechos. */
  done: number;
  /** Campos visibles con sugerencia. */
  total: number;
  /** Primer campo con sugerencia pendiente, en orden de pantalla. */
  active: string | null;
};

/** Progreso de una pestaña: solo cuentan los campos visibles que tienen sugerencia. */
export function tabProgress(params: Param[], values: GuideValues, doneFields: DoneFields): TabProgress {
  const suggested = visibleParams(params, values).filter((p) => hasSuggestion(p.name, values));
  const pending = suggested.find((p) => !doneFields[p.name]);
  return {
    done: suggested.filter((p) => doneFields[p.name]).length,
    total: suggested.length,
    active: pending?.name ?? null,
  };
}

/** Filas de una tabla en TSV (con cabecera de nombres de columna), para pegarlas en Studio. */
export function rowsToTsv(columns: { name: string; label: string }[], rows: Record<string, string>[]): string {
  const clean = (v: string) => v.replace(/[\t\r\n]+/g, " ");
  const head = columns.map((c) => clean(c.label || c.name)).join("\t");
  const body = rows.map((r) => columns.map((c) => clean(r[c.name] ?? "")).join("\t"));
  return [head, ...body].join("\n");
}
