import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { TalendPreflight } from "./TalendPreflight";
import { BatchJobRow } from "../PlansTab";
import type { TalendApplyBatchSummary } from "../../types";

test("preflight explains the exact destination, generated scope and pending human work", () => {
  const summary: TalendApplyBatchSummary = {
    project_id: "p", revision_hash: "a".repeat(64), destination_root: "Process/project-p",
    total_jobs: 1, creatable_jobs: 1, total_components: 1, total_connections: 0, total_contexts: 2,
    cycles: [["a.sas", "b.sas"]],
    programs: [{ program: "a.sas", job_name: "job_a", folder_path: "Process/project-p/Banking",
      ready_for_creation: true, creation_kind: "components", components: 1, connections: 0, contexts: 2,
      child_jobs: 0, pending: ["Confirmar esquema"], blocked_steps: [],
      draft_components: [{ unique_name: "tMap_1", reason: "Validar expresión SAS" }] }],
  };
  const html = renderToStaticMarkup(<TalendPreflight id="p" summary={summary} />);
  expect(html).toContain("Process/project-p");
  expect(html).toContain("1 Job con configuración pendiente");
  expect(html).toContain("Confirmar esquema");
  expect(html).toContain("Validar expresión SAS");
  expect(html).toContain("ciclo de dependencias");
  expect(html).toContain('href="#/p/p/planes/a.sas"');
});

test("a reused structure with unfinished configuration is not presented as ready to run", () => {
  const html = renderToStaticMarkup(<BatchJobRow projectId="p" path="a.sas" job={{
    program: "a.sas", status: "applied", phase: null, error: null,
    result: { status: "applied", identity: { project_id: "p", program: "a.sas", source_sha256: null, rules_version: "1", job_name: "job_a", folder_path: "Process/p" },
      warnings: [], blocked_steps: [], review_required: true, review_warnings: ["Completar esquema en Studio"],
      result: { totalComponents: 3, generatedComponents: 0, reusedComponents: 3, generatedConnections: 0, reusedConnections: 2 } },
  }} />);
  expect(html).toContain("Estructura creada; revisión pendiente");
  expect(html).toContain("3 componentes");
  expect(html).toContain("2 conexiones");
  expect(html).toContain("Completar esquema en Studio");
});
