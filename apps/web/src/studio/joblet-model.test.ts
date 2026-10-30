import { describe, expect, test } from "bun:test";
import { copyableNames, diagramSteps, kindLabel, occurrenceLabel, parameterRows, showDiagram } from "./joblet-model";
import type { JobletPlan, Step } from "../types";

const joblet: JobletPlan = {
  id: "joblet-01",
  name: "jl_ConversionTipo",
  title: "Conversión de tipo",
  kind: "sequence",
  occurrences: [
    { job: "job_a", label: "pasos s2–s8", step_ids: ["s2", "s3"], values: { expresion_var7: "VAR7" }, usage_steps: [] },
    { job: "job_b", label: "pasos s40–s46", step_ids: ["s40", "s41"], values: { expresion_var7: "VAR8" }, usage_steps: [] },
  ],
  parameters: [
    { name: "expresion_var7", context_variable: "context.expresion_var7", example_values: ["VAR7", "VAR8"] },
    { name: "tabla_entrada_1", context_variable: "context.tabla_entrada_1", example_values: [] },
  ],
  components: [],
  inputs: [],
  outputs: [],
  trigger_inputs: ["inicio"],
  why: "Se repite.",
  creation_steps: [],
  operation_count: 2,
};

const step = (id: string, order: number) => ({ id, order }) as Step;

describe("parameterRows", () => {
  test("una celda por aparición, vacía si la aparición no trae el valor", () => {
    const rows = parameterRows(joblet);
    expect(rows[0]).toEqual({ name: "expresion_var7", context_variable: "context.expresion_var7", values: ["VAR7", "VAR8"] });
    expect(rows[1].values).toEqual(["", ""]);
  });
});

describe("diagramSteps y showDiagram", () => {
  test("toma los pasos de la primera aparición, en orden del plan", () => {
    const steps = [step("s41", 41), step("s2", 2), step("s3", 3), step("s40", 40)];
    expect(diagramSteps(joblet, steps).map((s) => s.id)).toEqual(["s2", "s3"]);
    expect(showDiagram(joblet, steps)).toBe(true);
  });

  test("con menos de dos pasos no se dibuja", () => {
    expect(showDiagram(joblet, [step("s2", 2)])).toBe(false);
    expect(showDiagram(joblet, [])).toBe(false);
  });
});

describe("copyableNames", () => {
  test("nombre del joblet y parámetros, sin repetir", () => {
    expect(copyableNames(joblet)).toEqual(["jl_ConversionTipo", "expresion_var7", "tabla_entrada_1"]);
  });
});

describe("etiquetas", () => {
  test("singular y plural de apariciones, y tipo de joblet", () => {
    expect(occurrenceLabel(1)).toBe("1 aparición");
    expect(occurrenceLabel(5)).toBe("5 apariciones");
    expect(kindLabel("macro")).toBe("Desde una macro");
    expect(kindLabel("sequence")).toBe("Desde pasos consecutivos");
  });
});
