import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const source = await readFile(new URL("./SettingsView.tsx", import.meta.url), "utf8");

test("the settings panel reports the connection in stages: MCP server, Studio bridge, and write access", () => {
  assert.match(source, /Servidor MCP/);
  assert.match(source, /Bridge de Talend Studio/);
  assert.match(source, /Escritura de Jobs/);
  assert.match(source, /h\.mcp_available/);
  assert.match(source, /h\.bridge_available/);
  assert.match(source, /h\.write_enabled/);
});

test("the overall state distinguishes connected, partial, and disconnected", () => {
  assert.match(source, /Conectado/);
  assert.match(source, /Parcial/);
  assert.match(source, /Sin conexión/);
  assert.match(source, /if \(h\.available\) return \{ tone: "ok"/);
  assert.match(source, /if \(h\.mcp_available\) return \{ tone: "warn"/);
});

test("the active connection configuration is visible for debugging", () => {
  assert.match(source, /h\.mcp_url/);
  assert.match(source, /h\.timeout_seconds/);
  assert.match(source, /h\.apply_folder/);
  assert.match(source, /Detalles para el equipo técnico/);
});
