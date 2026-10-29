import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { JobIdentity } from "./JobIdentity";
import type { JobPlan } from "../../types";

const basePlan = { program: "ventas.sas", job_name: "job_ventas", steps: [], children: [], validation_cases: [], unresolved: [] } as unknown as JobPlan;

function render(plan: Partial<JobPlan>, props: { folderPath?: string; locked?: boolean } = {}) {
  return renderToStaticMarkup(<JobIdentity id="project" plan={{ ...basePlan, ...plan }} folderPath={props.folderPath} locked={props.locked ?? false} onSaved={() => {}} />);
}

test("shows the job name with an edited badge when the name was overridden", () => {
  const html = render({ job_name: "job_custom", job_name_edited: true });
  expect(html).toContain("<h1>job_custom</h1>");
  expect(html).toContain("editado");
});

test("omits the edited badge for generated names", () => {
  expect(render({ job_name_edited: false })).not.toContain("editado");
});

test("shows the description and destination folder", () => {
  const html = render({ description: "Carga diaria de ventas" }, { folderPath: "Jobs/Ventas" });
  expect(html).toContain("Carga diaria de ventas");
  expect(html).toContain("Jobs/Ventas");
});

test("explains when a requested name was ignored", () => {
  const html = render({ rename_ignored: "x" });
  expect(html).toContain("El nombre «x» ya no está disponible; se usa el generado");
});

test("disables the edit button while a Talend creation is running", () => {
  const html = render({}, { locked: true });
  expect(html).toMatch(/<button[^>]*disabled=""[^>]*>[^<]*Hay una creación en curso/);
});

test("offers the edit button when no creation is running", () => {
  const html = render({});
  expect(html).toContain("Editar nombre y descripción");
  expect(html).not.toMatch(/<button[^>]*disabled=""/);
});
