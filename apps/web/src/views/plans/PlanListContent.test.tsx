import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { PlanListContent } from "./PlanListContent";
import { GridRecommendations } from "./PlanGrid";
import type { GridRecommendation, PlanRow } from "../../types";

test("opens the next unfinished group and labels Job search and progress", () => {
  const rows = [
    { program: "base.sas", job_name: "job_base", steps: 1, done: 1 },
    { program: "process.sas", job_name: "job_process", steps: 2, done: 0 },
  ] as PlanRow[];
  const html = renderToStaticMarkup(<PlanListContent id="project" rows={rows} isDesktop groups={rows.map((row) => ({ title: row.job_name, hint: "", rows: [row] }))} />);
  expect(html).toContain('aria-label="Buscar Job o programa SAS"');
  expect(html.match(/<details[^>]*open=""/g)).toHaveLength(1);
  expect(html).toContain('aria-label="Avance manual de job_process"');
  expect(html).toContain("1 de 2 Jobs completados");
});

test("shows Studio readback separately from manually completed guide steps", () => {
  const row = { program: "daily.sas", job_name: "job_daily", steps: 3, done: 1, studio_verified: 2, studio_pending: 1, studio_status: "pending" } as PlanRow;
  const html = renderToStaticMarkup(<PlanListContent id="project" rows={[row]} isDesktop groups={[{ title: "Jobs", hint: "", rows: [row] }]} />);
  expect(html).toContain("1 de 3 pasos hechos");
  expect(html).toContain("Comprobación automática en Studio: 2 de 3 pasos verificados");
  expect(html).toContain('aria-label="Avance manual de job_daily"');
});

test("shows the human-authored Job description in its guide row", () => {
  const row = { program: "daily.sas", job_name: "job_daily", description: "Carga diaria de clientes", steps: 1, done: 0 } as PlanRow;
  const html = renderToStaticMarkup(<PlanListContent id="project" rows={[row]} isDesktop groups={[{ title: "Jobs", hint: "", rows: [row] }]} />);
  expect(html).toContain("Carga diaria de clientes");
});

test("orchestration separates locations, configuration fields and source references", () => {
  const items: GridRecommendation[] = [{ id: "dispatch", pattern_id: "sas_batch.sysin", catalog_version: "1", status: "supported", instruction: "", reason: "", component_candidate: "tRunJob", doc_url: null, required: [], dependencies: [], target_program: "load.sas", evidence: { file: "Batch/run.sas", line: 12, end_line: 12 }, details: { resolved_program: "load.sas", program: "/sas/load.sas" } }];
  const html = renderToStaticMarkup(<GridRecommendations id="project" items={items} isDesktop />);
  expect(html).toContain('class="orchestration-steps"');
  expect(html).toContain('class="orchestration-location"');
  expect(html).toContain('<dl class="orchestration-fields">');
  expect(html).toContain("Referencias en el SAS (1)");
  expect(html).not.toContain('open=""');
});
