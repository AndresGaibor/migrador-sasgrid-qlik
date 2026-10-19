import assert from "node:assert/strict";
import test from "node:test";
import { decodeProgress, encodeProgress, isUncertainStep, storageStatus } from "./guide-progress.ts";

test("stores each guided state in the existing persisted decision note and recovers it", () => {
  for (const state of ["pending", "in_progress", "completed", "blocked"]) {
    const note = encodeProgress(state, "Revisar columna de fecha", "Confirmar formato con negocio");
    assert.deepEqual(decodeProgress(storageStatus(state), note), {
      state,
      note: "Revisar columna de fecha",
      blockReason: state === "blocked" ? "Confirmar formato con negocio" : "",
    });
  }
});

test("keeps existing decisions readable and requires a reason for a blocked step", () => {
  assert.deepEqual(decodeProgress("verificado", "Hecho"), { state: "completed", note: "Hecho", blockReason: "" });
  assert.equal(encodeProgress("blocked", "", "  "), null);
});

test("requires an explicit confirmation whenever a step is uncertain", () => {
  assert.equal(isUncertainStep({ pending: [], confidence: "high", verified: true }), false);
  assert.equal(isUncertainStep({ pending: ["confirmar formato"], confidence: "high", verified: true }), true);
  assert.equal(isUncertainStep({ pending: [], confidence: "low", verified: true }), true);
  assert.equal(isUncertainStep({ pending: [], confidence: "high", verified: false }), true);
});
