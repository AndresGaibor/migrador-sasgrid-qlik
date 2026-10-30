import type { Step } from "./types";

export type Do = { text: string; value?: string; columns?: string[]; rows?: string[][]; where?: string; check?: boolean };

const WIRE: Record<string, string> = {
  OnSubjobOk: "Trigger → On Subjob Ok",
  OnComponentOk: "Trigger → On Component Ok",
  Main: "Row → Main",
  Lookup: "Row → Lookup",
  Reject: "Row → Reject",
  Iterate: "Row → Iterate",
};
const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
// SAS &VAR / &VAR. → variable de contexto de Talend
export const toContext = (v: string) => v.replace(/&(\w+)\.?/g, "context.$1");
const looksLikePath = (v: string) => /[\\/]|\.sas\b/i.test(v);

// Pendientes que esta guía ya resuelve con una instrucción concreta: no se muestran como «decisión».
const RESOLVED = /^(Formato físico|Esquema y tipos de columnas|Sistema y tabla|Confirmar la acción sobre la tabla|Librería |Tabla base destino|Job o joblet hijo|Crear\/identificar el Job hijo|Confirmar si el programa incluido)/;
const DATASET = /^(Leer|Escribir|Añadir filas a) +([\w&]+)\.(\S+)/;

/**
 * Componente y valores de un paso de lectura/escritura de dataset cuyo componente el planificador dejó «por_determinar».
 * Es la misma decisión que toman las instrucciones (datasetSteps): se comparte para que el panel de Studio no la contradiga.
 */
export function datasetConfig(s: Step): { component: string; values: Record<string, string> } | null {
  if (s.component_candidate.split(" ")[0] !== "por_determinar" || !["read", "write", "append"].includes(s.operation_type ?? "")) return null;
  const m = s.purpose.match(DATASET);
  if (!m) return null;
  const [, , lib, table] = m;
  if (lib.includes("&")) return null;
  const isRead = s.operation_type === "read";
  if (lib.toLowerCase() === "work") return { component: isRead ? "tHashInput" : "tHashOutput", values: {} };
  const tableExpr = table.includes("&") ? toContext(table.replace(/\(.*$/, "")) : `"${table.replace(/\(.*$/, "").toLowerCase()}"`;
  const filename = `context.${lib.toUpperCase()}_DIR + "/" + ${tableExpr} + ".csv"`;
  return isRead
    ? { component: "tFileInputDelimited", values: { FILENAME: filename, FIELDSEPARATOR: '","', HEADER: "1" } }
    : { component: "tFileOutputDelimited", values: { FILENAME: filename, FIELDSEPARATOR: '","', APPEND: s.operation_type === "append" ? "true" : "false", INCLUDEHEADER: "true" } };
}

// Dataset SAS → archivo CSV en la carpeta de su librería (variable de contexto <LIB>_DIR); WORK → tHash*.
function datasetSteps(s: Step, all: Step[], comp: string): Do[] | null {
  if (comp !== "por_determinar" || !["read", "write", "append"].includes(s.operation_type ?? "")) return null;
  const m = s.purpose.match(DATASET);
  if (!m) return null;
  const [, , lib, table] = m;
  if (lib.includes("&")) return null;
  const isRead = s.operation_type === "read";
  const name = (table.replace(/\(.*$/, "").toLowerCase());
  const tableExpr = table.includes("&") ? toContext(table.replace(/\(.*$/, "")) : `"${name}"`;
  const out: Do[] = [];
  if (lib.toLowerCase() === "work") {
    const writer = all.filter((x) => x.order < s.order && /^Escribir +work\./i.test(x.purpose) && x.purpose.toLowerCase().includes(name)).pop();
    out.push({ text: `Arrastra el componente ${isRead ? "tHashInput" : "tHashOutput"} al lienzo.`, where: `Palette (panel derecho) → buscar «${isRead ? "tHashInput" : "tHashOutput"}»` });
    out.push({ text: "Ponle este nombre:", value: s.purpose, where: "Clic en el componente → Component → View → Label format" });
    if (isRead) out.push({ text: "En «Component list» elige el componente que guardó estos datos:", value: writer?.purpose ?? "(el paso que escribe este dataset temporal)", where: "Pestaña Component → Basic settings" });
    else out.push({ text: "Deja «Append» desmarcado y pulsa «Sync columns».", where: "Pestaña Component → Basic settings (hereda las columnas del componente anterior)" });
    return out;
  }
  const dirVar = `context.${lib.toUpperCase()}_DIR`;
  const path = `${dirVar} + "/" + ${tableExpr} + ".csv"`;
  const comp2 = isRead ? "tFileInputDelimited" : "tFileOutputDelimited";
  out.push({ text: `Arrastra el componente ${comp2} al lienzo.`, where: `Palette (panel derecho) → buscar «${comp2}»` });
  out.push({ text: "Ponle este nombre:", value: s.purpose, where: "Clic en el componente → Component → View → Label format" });
  out.push({ text: isRead ? "En «File name/Stream» escribe:" : "En «File Name» escribe:", value: path, where: "Pestaña Component → Basic settings" });
  if (isRead) {
    out.push({ text: "En «Field Separator» escribe:", value: '","' }, { text: "En «Header» escribe:", value: "1" });
    const cols = (s.schema_columns ?? []).filter((c) => c.name);
    out.push(cols.length ? { text: "Pulsa «Edit schema» y añade una columna por cada campo del dataset:", columns: ["Columna", "Tipo"], rows: cols.map((c) => [c.name, c.talend_type ?? "String"]), where: "Si otro Job de esta lista genera este archivo, copia el esquema de su componente de salida" } : { text: "Pulsa «Edit schema» y añade una columna por cada campo del dataset.", where: "Si otro Job de esta lista genera este archivo, copia el esquema de su componente de salida" });
  } else {
    out.push({ text: s.operation_type === "append" ? "Marca «Append» (este paso añade filas al final, no reemplaza)." : "Deja «Append» desmarcado (SAS reemplaza el dataset completo)." });
    out.push({ text: "Marca «Include Header» y pulsa «Sync columns».", where: "Pestaña Component → Basic settings (hereda las columnas del componente anterior)" });
  }
  return out;
}

export function stepDoes(s: Step, all: Step[]): Do[] {
  const comp = s.component_candidate.split(" ")[0];
  const ds = datasetSteps(s, all, comp);
  const out: Do[] = ds ?? [];
  const known = comp && comp !== "por_determinar";
  if (ds) return finish(s, all, out);
  out.push(
    known
      ? { text: `Arrastra el componente ${comp} al lienzo.`, where: `Palette (panel derecho) → buscar «${comp}»` }
      : { text: "Elige el componente a mano: la herramienta no pudo decidirlo.", where: `Alternativas: ${s.alternatives.join(", ") || "ver documentación"}` },
  );
  const jobProp = comp === "tRunJob" ? s.properties.find((p) => (p.label || p.name) === "Job" && p.value) : undefined;
  const jobName = jobProp ? "job_" + slug(((jobProp.value ?? "").replace(/["']/g, "").split("/").pop() ?? "").replace(/\.[^.]+$/, "").replace(/^job_/, "")) : undefined;
  out.push({ text: "Ponle este nombre:", value: jobName ?? s.purpose, where: "Clic en el componente → pestaña Component → View → Label format" });
  const cols = (s.schema_columns ?? []).filter((c) => c.name);
  const schemaStep = cols.length ? { text: "Antes de cargar valores, pulsa «Edit schema» y añade estas columnas:", columns: ["Columna", "Tipo"], rows: cols.map((c) => [c.name, c.talend_type ?? "String"]) } : null;
  // Talend necesita el esquema definido antes de cargar las filas inline.
  if (comp === "tFixedFlowInput" && schemaStep) out.push(schemaStep);
  for (const p of s.properties) {
    const label = p.label || p.name;
    const raw = p.value ?? "";
    if (comp === "tRunJob" && label === "Job" && raw) {
      out.push({ text: "En el campo «Job» pulsa «…» y elige este Job hijo:", value: jobName, where: `Pestaña Component → Basic settings. Si no existe, créalo antes${looksLikePath(raw) ? ` (programa SAS: ${raw.replace(/["']/g, "")})` : ""}` });
      continue;
    }
    if (comp === "tRunJob" && label === "Context Param" && raw.includes("=")) {
      for (const pair of raw.split(",")) {
        const [k, v = ""] = pair.split("=");
        out.push({ text: `En la tabla «Context Param» pulsa «+» y añade el parámetro «${k.trim()}» con este valor:`, value: toContext(v.trim()), where: "Pestaña Component → Basic settings → Context Param" });
      }
      continue;
    }
    if (comp === "tFixedFlowInput" && label === "Use Inline Table") continue;
    if (comp === "tFixedFlowInput" && (label === "Inline Table" || label === "Values") && raw.includes(" | ")) {
      const schema = (s.schema_columns ?? []).filter((c) => c.name);
      const heads = schema.map((c) => c.name);
      const stringSchema = heads.length > 0 && schema.every((c) => !c.talend_type || c.talend_type.toLowerCase() === "string");
      const rows = raw.split("\n").map((line) => line.split(" | ").map((cell) => {
        const value = cell.trim();
        return stringSchema ? JSON.stringify(value) : value;
      }));
      out.push({ text: `Marca «Use Inline Table» y copia estas ${rows.length} filas (valores String entre comillas dobles):`, columns: heads.length ? heads : undefined, rows, where: "Pestaña Component → Basic settings → Mode: Use Inline Table" });
      continue;
    }
    out.push(p.value == null ? { text: `Campo «${label}»: no hay valor sugerido; complétalo según el SAS.`, where: "Pestaña Component → Basic settings" } : { text: `En el campo «${label}» escribe:`, value: toContext(raw), where: "Pestaña Component → Basic settings" });
  }
  if (schemaStep && comp !== "tFixedFlowInput") out.push(schemaStep);
  for (const e of s.expressions) {
    out.push(e.talend ? { text: `Donde el SAS hace «${e.sas}», escribe:`, value: e.talend, where: "En el campo de expresión del componente" } : { text: `Sin traducción automática para «${e.sas}»: escribe su equivalente en Java a mano.` });
  }
  return finish(s, all, out);
}

function finish(s: Step, all: Step[], out: Do[]): Do[] {
  for (const c of s.connections) {
    const src = all.find((x) => x.operation_id && x.operation_id === c.from_step) ?? all.find((x) => x.id === c.from_step);
    const how = WIRE[c.type] ?? c.type;
    out.push(src
      ? { text: `Conecta el paso ${src.order} («${src.purpose}») con este componente.`, where: `Clic derecho en el componente del paso ${src.order} → ${how} → clic en este componente` }
      : { text: `Conéctalo con su componente de origen (${how}).`, where: `Clic derecho en el origen → ${how}` });
  }
  for (const x of s.pending.filter((p) => !RESOLVED.test(p))) out.push({ text: `Antes de seguir, resuelve: ${x}`, check: true });
  return out;
}
