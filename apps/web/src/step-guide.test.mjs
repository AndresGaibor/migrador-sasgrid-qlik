import assert from "node:assert/strict";
import test from "node:test";
import { stepDoes } from "./step-guide.ts";

test("tFixedFlowInput sets inline-table mode, quotes strings, and keeps format semantics for review", () => {
  const instructions = stepDoes({
    component_candidate: "tFixedFlowInput",
    purpose: "Definir formatos",
    properties: [
      { name: "USE_INTABLE", label: "Use Inline Table", value: "true" },
      { name: "INTABLE", label: "Inline Table", value: "CHK | Checking\nSAV | Savings" },
    ],
    schema_columns: [
      { name: "FORMAT", talend_type: "String" },
      { name: "CODE", talend_type: "String" },
      { name: "LABEL", talend_type: "String" },
    ],
    expressions: [],
    connections: [],
    pending: ["Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas"],
  }, []);

  assert.deepEqual(instructions.slice(0, 4).map((step) => step.text), [
    "Arrastra el componente tFixedFlowInput al lienzo.",
    "Ponle este nombre:",
    "Antes de cargar valores, pulsa «Edit schema» y añade estas columnas:",
    "Marca «Use Inline Table» y copia estas 2 filas (valores String entre comillas dobles):",
  ]);
  assert.deepEqual(instructions[3].rows, [["\"CHK\"", "\"Checking\""], ["\"SAV\"", "\"Savings\""]]);
  assert.equal(instructions.length, 5);
  assert.equal(instructions[4].check, true);
  assert.match(instructions[4].text, /rangos y OTHER/);
});
