import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const source = await readFile(new URL("./ProjectView.tsx", import.meta.url), "utf8");

test("project deletion is explicit, typed, scoped to the portal, and blocked for active work", () => {
  assert.match(source, /Eliminar proyecto/);
  assert.match(source, /api\.deleteProject\(id/);
  assert.match(source, /placeholder=\{project\.name\}/);
  assert.match(source, /Talend.*no se eliminar/i);
  assert.match(source, /análisis.*lote.*activos/i);
});
