import { describe, expect, test } from "bun:test";
import type { Step } from "../types";
import { edgeKind, effectiveComponent, jobCanvas, stepGuideValues } from "./step-adapter";

const step = (over: Partial<Step>): Step => ({
  id: "s1", order: 1, subjob: "b1", action: "add_component", component_candidate: "tFileInputDelimited",
  alternatives: [], purpose: "Leer cars", properties: [], connections: [], expressions: [], assumptions: [],
  pending: [], tests: [], status: "pendiente", note: null, evidence: { file: "a.sas", line: 1 },
  confidence: "high", verified: true, ...over,
});

describe("stepGuideValues", () => {
  test("usa las propiedades con valor y omite las vacías", () => {
    const v = stepGuideValues(step({ properties: [
      { name: "FILENAME", value: "context.ruta", origin: "sas", verified: true },
      { name: "HEADER", value: null, origin: "sas", verified: false },
    ] }));
    expect(v.FILENAME?.value).toBe("context.ruta");
    expect(v.HEADER).toBeUndefined();
  });
  test("las columnas del paso se vuelven filas del esquema", () => {
    const v = stepGuideValues(step({ schema_columns: [{ name: "id", talend_type: "id_Integer" }, { name: "n", talend_type: null }] }));
    expect(v.SCHEMA?.rows).toEqual([{ name: "id", type: "id_Integer" }, { name: "n", type: "id_String" }]);
  });
});

describe("jobCanvas", () => {
  test("convierte conexiones en aristas y descarta las que no apuntan a un paso del Job", () => {
    const { nodes, edges } = jobCanvas([
      step({ id: "a" }),
      step({ id: "b", component_candidate: "tMap", connections: [{ type: "Main", from_step: "a" }, { type: "Main", from_step: "fuera" }] }),
      step({ id: "c", connections: [{ type: "OnSubjobOk", from_step: "b" }] }),
    ]);
    expect(nodes.map((n) => n.id)).toEqual(["a", "b", "c"]);
    expect(edges).toEqual([{ from: "a", to: "b", kind: "row_main" }, { from: "b", to: "c", kind: "on_subjob_ok" }]);
  });
  test("el estado de la guía decide el color del nodo", () => {
    const { nodes } = jobCanvas([step({ id: "a", status: "validado_manualmente", note: "[Estado de guía: completado]" })]);
    expect(nodes[0]?.status).toBe("done");
  });
});

describe("edgeKind", () => {
  test("acepta variantes de escritura", () => {
    expect(edgeKind("On Subjob Ok")).toBe("on_subjob_ok");
    expect(edgeKind("run_if")).toBe("run_if");
    expect(edgeKind("desconocido")).toBe("row_main");
  });
});

describe("effectiveComponent", () => {
  const read = (purpose: string) => step({ component_candidate: "por_determinar", operation_type: "read", purpose });
  test("una lectura de librería sin componente se resuelve a tFileInputDelimited con sus valores", () => {
    const s = read("Leer dwh.clientes");
    expect(effectiveComponent(s)).toBe("tFileInputDelimited");
    expect(stepGuideValues(s).FILENAME?.value).toBe('context.DWH_DIR + "/" + "clientes" + ".csv"');
  });
  test("una escritura en WORK usa tHashOutput", () => {
    expect(effectiveComponent(step({ component_candidate: "por_determinar", operation_type: "write", purpose: "Escribir work.tmp" }))).toBe("tHashOutput");
  });
  test("respeta el componente del planificador y quita lo que sigue al nombre", () => {
    expect(effectiveComponent(step({ component_candidate: "tMap (join)" }))).toBe("tMap");
  });
});

describe("títulos de subjob", () => {
  test("sin título de negocio se numera como Bloque n en orden de aparición", () => {
    const { nodes } = jobCanvas([step({ id: "a", subjob: "s5" }), step({ id: "b", subjob: "s5" }), step({ id: "c", subjob: "s15" })]);
    expect(nodes.map((n) => n.subjob)).toEqual(["Bloque 1", "Bloque 1", "Bloque 2"]);
  });
  test("conserva el título de negocio cuando existe", () => {
    expect(jobCanvas([step({ id: "a", business_subjob: "Carga de clientes" })]).nodes[0]?.subjob).toBe("Carga de clientes");
  });
});
