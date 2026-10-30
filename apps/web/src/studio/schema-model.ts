// Lógica pura del esquema: conversión desde filas de la guía, tipos Talend frente a SAS y TSV para Studio.
import type { SchemaColumn } from "./panel-types";

export type TypeFamily = "string" | "number" | "date" | "boolean" | "other";

const NUMBER_TYPES = new Set(["integer", "int", "long", "short", "byte", "double", "float", "bigdecimal"]);

/** Familia de un tipo Talend: String, Integer, Date… */
export function talendFamily(type: string): TypeFamily {
  const t = type.trim().toLowerCase();
  if (t === "string" || t === "character" || t === "char") return "string";
  if (NUMBER_TYPES.has(t)) return "number";
  if (t === "date") return "date";
  if (t === "boolean") return "boolean";
  return "other";
}

/** Familia que corresponde a un tipo SAS (char, num, date…). Null si no se conoce. */
export function sasFamily(sasType: string | null | undefined): TypeFamily | null {
  const t = (sasType ?? "").trim().toLowerCase();
  if (t === "") return null;
  if (t === "char" || t === "character" || t === "$") return "string";
  if (t === "num" || t === "numeric") return "number";
  if (t === "date" || t === "datetime" || t === "time" || t === "timestamp") return "date";
  return null;
}

/** true cuando el tipo Talend no corresponde a la familia del tipo SAS de origen. */
export function differsFromSas(column: SchemaColumn): boolean {
  const expected = sasFamily(column.sasType);
  return expected !== null && talendFamily(column.type) !== expected;
}

const truthy = (v: string | undefined) => v !== undefined && ["true", "yes", "sí", "si", "1"].includes(v.trim().toLowerCase());

function optionalNumber(v: string | undefined): number | null {
  if (v === undefined || v.trim() === "") return null;
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
}

const text = (v: string | undefined): string | null => (v === undefined || v === "" ? null : v);

/**
 * Convierte filas de la guía (claves name, type, key, nullable, length, precision, pattern, default,
 * sasType, sasFormat, comment) en columnas. Las filas sin nombre se descartan.
 */
export function schemaColumnsFromRows(rows: Record<string, string>[]): SchemaColumn[] {
  return rows
    .filter((r) => (r.name ?? "").trim() !== "")
    .map((r) => ({
      name: r.name.trim(),
      key: truthy(r.key),
      type: r.type?.trim() || "String",
      nullable: truthy(r.nullable),
      length: optionalNumber(r.length),
      precision: optionalNumber(r.precision),
      pattern: text(r.pattern),
      default: text(r.default),
      sasType: text(r.sasType),
      sasFormat: text(r.sasFormat),
      comment: text(r.comment),
    }));
}

export type SchemaShape = {
  /** Hay alguna columna de tipo Date: se muestra «Date Pattern». */
  hasDatePattern: boolean;
  /** Hay origen SAS: se muestra la columna «SAS origen». */
  hasSasOrigin: boolean;
};

export function schemaShape(columns: SchemaColumn[]): SchemaShape {
  return {
    hasDatePattern: columns.some((c) => c.type.trim().toLowerCase() === "date"),
    hasSasOrigin: columns.some((c) => c.sasType),
  };
}

/** Texto de origen SAS: «char», «num DATE9.»… */
export function sasOriginText(c: SchemaColumn): string {
  return [c.sasType, c.sasFormat].filter((x) => x).join(" ");
}

const cell = (v: string | number | boolean | null | undefined): string => {
  if (v === null || v === undefined) return "";
  return String(v).replace(/[\t\r\n]+/g, " ");
};

/** Tabla en TSV (con cabecera) para pegarla en la tabla Edit schema de Studio. */
export function schemaToTsv(columns: SchemaColumn[]): string {
  const shape = schemaShape(columns);
  const head = ["Column", "Key", "Type", "Nullable", "Length", "Precision", "Default", "Comment"];
  if (shape.hasDatePattern) head.push("Date Pattern");
  if (shape.hasSasOrigin) head.push("SAS origen");
  const lines = columns.map((c) => {
    const row = [c.name, c.key, c.type, c.nullable, c.length, c.precision, c.default, c.comment];
    if (shape.hasDatePattern) row.push(c.pattern);
    if (shape.hasSasOrigin) row.push(sasOriginText(c));
    return row.map(cell).join("\t");
  });
  return [head.join("\t"), ...lines].join("\n");
}
