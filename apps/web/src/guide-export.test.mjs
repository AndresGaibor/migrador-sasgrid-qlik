import assert from "node:assert/strict";
import test from "node:test";
import { guideCsv, guideJson, guideMarkdown, guideIndexMarkdown } from "./guide-export.ts";

const plan = {
  program: "ventas.sas", job_name: "job_ventas", job_status: "needs_review", sha256: null, rules_version: "1",
  steps: [{ id: "s1", order: 1, subjob: "main", action: "configure", operation_id: null, operation_type: null, component_candidate: "tMap", alternatives: [], purpose: "Configura el mapeo", properties: [{ name: "EXPRESSION", label: "Expresión", value: "row1.total", origin: "sas", verified: false, in_catalog: true, options: [] }], schema_columns: [], connections: [], expressions: [], assumptions: [], pending: ["Confirmar el tipo de dato"], tests: [], evidence: { file: "ventas.sas", line: 8, end_line: 8 }, confidence: "low", status: "pendiente", note: "[Estado de guía: bloqueado]\n[Motivo de bloqueo: Espera confirmación]\n[Nota de trabajo: Revisar con el equipo]", verified: false, in_catalog: true, doc_url: "https://help.qlik.com/tMap", variants: [], requires_semantic_validation: true }],
  children: [], validation_cases: [], context_variables: [], libraries_needed: [], unresolved: [], orchestration: { schedules: [], upstream: [], downstream: [], grid_tasks: [] },
};

test("Markdown and JSON exports include workflow state, evidence, official docs and pending decisions", () => {
  const md = guideMarkdown(plan, "project-1");
  assert.match(md, /Estado de la guía:\*\* Bloqueado/);
  assert.match(md, /Esper[a]? confirmación/);
  assert.match(md, /Confirmar el tipo de dato/);
  assert.match(md, /https:\/\/help\.qlik\.com\/tMap/);
  assert.match(md, /ventas\.sas:8/);
  const json = JSON.parse(guideJson(plan, "project-1"));
  assert.equal(json.steps[0].status, "blocked");
  assert.equal(json.steps[0].block_reason, "Espera confirmación");
  assert.equal(json.steps[0].note, "Revisar con el equipo");
  assert.equal(json.steps[0].pending[0], "Confirmar el tipo de dato");
  assert.equal(json.steps[0].references.official.url, "https://help.qlik.com/tMap");
  assert.match(json.steps[0].references.sas.href, /line=8/);
});

test("CSV and index exports expose state, pending items and block counts", () => {
  const csv = guideCsv([plan], "project-1");
  assert.match(csv.split("\n")[0], /estado_guia/);
  assert.match(csv, /Bloqueado/);
  assert.match(csv, /Confirmar el tipo de dato/);
  assert.match(guideIndexMarkdown([plan]), /1 bloqueado/);
});

test("CSV quotes uploaded text that could be interpreted as a spreadsheet formula", () => {
  const unsafe = { ...plan, steps: [{ ...plan.steps[0], purpose: "=HYPERLINK(\"https://example.invalid\")" }] };
  assert.match(guideCsv([unsafe], "project-1"), /"'=HYPERLINK/);
})
