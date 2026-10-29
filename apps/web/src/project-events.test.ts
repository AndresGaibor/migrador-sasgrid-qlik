import { expect, test } from "bun:test";
import { parseActivity } from "./project-events";

test("acepta un evento con revisión y estados", () => {
  const activity = parseActivity(
    JSON.stringify({
      revision: 3,
      processing: { status: "running", stage: "analysis", message: "Analizando", updated_at: "2026-10-28T10:00:00+00:00" },
      batch: null,
    }),
  );
  expect(activity?.revision).toBe(3);
  expect(activity?.processing?.stage).toBe("analysis");
  expect(activity?.batch).toBeNull();
});

test("descarta mensajes que no son JSON válido", () => {
  expect(parseActivity(": ping")).toBeNull();
  expect(parseActivity("")).toBeNull();
});

test("descarta JSON sin forma de evento", () => {
  expect(parseActivity(JSON.stringify({ revision: 1 }))).toBeNull();
  expect(parseActivity(JSON.stringify({ processing: null, batch: null }))).toBeNull();
  expect(parseActivity(JSON.stringify({ revision: "2", processing: null, batch: null }))).toBeNull();
  expect(parseActivity(JSON.stringify([1, 2]))).toBeNull();
});
