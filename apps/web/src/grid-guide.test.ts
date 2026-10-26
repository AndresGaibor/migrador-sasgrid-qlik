import { expect, test } from "bun:test";
import { buildGridGuides } from "./grid-guide";

test("Control-M recommendation becomes a Qlik Talend Cloud scheduling guide", () => {
  const [guide] = buildGridGuides([{
    id: "control-m-schedule",
    pattern_id: "scheduler.control_m",
    catalog_version: "test",
    status: "partial",
    instruction: "Control-M schedule comment",
    reason: "The actual calendar is not available in SAS source",
    component_candidate: null,
    doc_url: null,
    required: [],
    dependencies: [],
    target_program: null,
    evidence: { file: "BatchJobs/run_daily_banking.sas", line: 120, end_line: 120 },
    details: {},
  }]);

  expect(guide.kind).toBe("cloud");
  expect(guide.actions.map(({ text }) => text)).toContain("Programa el Plan con el calendario recuperado de Control-M.");
  expect(guide.actions.find(({ text }) => text.startsWith("Configura los pasos"))?.note).toContain("If all tasks succeed");
  expect(guide.actions.find(({ text }) => text.startsWith("Publica en Qlik"))?.doc_url).toContain("publish-jobs");
});
