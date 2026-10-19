import assert from "node:assert/strict";
import test from "node:test";
import { orderSteps, sourceEvidence } from "./guided.ts";

test("orders guide steps numerically and keeps stable order for ties", () => {
  const steps = [{ order: 10, id: "ten" }, { order: 2, id: "two-a" }, { order: 2, id: "two-b" }];
  assert.deepEqual(orderSteps(steps).map((step) => step.id), ["two-a", "two-b", "ten"]);
});

test("finds source excerpts recursively and returns the requested evidence line", () => {
  const nodes = [
    { type: "DataStep", statements: [{ line: 10, text: "data salida;" }, { line: 11, text: "set entrada;" }] },
    { type: "MacroDef", body: [{ type: "GlobalStmt", line: 20, text: "%put listo;" }] },
    { type: "ProcStep", queries: [{ text: "select * from ventas", loc: { line: 30, end_line: 30 } }] },
  ];
  assert.deepEqual(sourceEvidence(nodes, 11), { line: 11, text: "set entrada;" });
  assert.deepEqual(sourceEvidence(nodes, 20), { line: 20, text: "%put listo;" });
  assert.deepEqual(sourceEvidence(nodes, 30), { line: 30, text: "select * from ventas" });
  assert.equal(sourceEvidence(nodes, 99), null);
});
