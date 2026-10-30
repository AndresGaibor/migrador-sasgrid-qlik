import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { FusedBadge } from "./FusedBadge";
import { JobletGuide } from "./JobletGuide";
import { NotMigratedPanel } from "./NotMigratedPanel";
import type { JobPlan, JobletPlan } from "../types";

const joblet: JobletPlan = {
  id: "joblet-01",
  name: "jl_Split3",
  title: "Troceado en lotes",
  kind: "macro",
  occurrences: [
    { job: "job_split3", label: "macro %split3 (línea 12)", step_ids: ["s1", "s2"], values: { tabla_entrada_1: "dwh.clientes" }, usage_steps: ["Sustituye el bloque por el joblet."] },
  ],
  parameters: [{ name: "tabla_entrada_1", context_variable: "context.tabla_entrada_1", example_values: ["dwh.clientes"] }],
  components: ["tMap", "tUniqRow"],
  inputs: ["tabla_entrada_1"],
  outputs: [],
  trigger_inputs: ["inicio"],
  why: "El mismo bloque aparece dos veces.",
  creation_steps: ["Repository › Joblet Designs › clic derecho › Create Joblet."],
  operation_count: 2,
};

const plan = (over: Partial<JobPlan>): JobPlan => ({
  program: "cod1.sas",
  job_name: "job_cod1",
  steps: [],
  children: [],
  validation_cases: [],
  context_variables: [],
  libraries_needed: [],
  orchestration: { grid_tasks: [], grid_recommendations: [], schedules: [], upstream: [], downstream: [] },
  unresolved: [],
  ...over,
} as JobPlan);

describe("NotMigratedPanel", () => {
  test("sin entradas no muestra nada", () => {
    expect(renderToStaticMarkup(<NotMigratedPanel id="p1" plan={plan({ not_migrated: [] })} />)).toBe("");
    expect(renderToStaticMarkup(<NotMigratedPanel id="p1" plan={plan({})} />)).toBe("");
  });

  test("muestra el conteo, la frase guía y el enlace a la línea SAS", () => {
    const html = renderToStaticMarkup(
      <NotMigratedPanel
        id="p1"
        plan={plan({
          not_migrated: [{ category: "espera", lines: [7], what: "espera de 10 s", reason: "No aporta datos.", talend_equivalent: "Nada." }],
        })}
      />,
    );
    expect(html).toContain("Lo que NO hace falta migrar");
    expect(html).toContain("SAS necesitaba esto; Talend lo resuelve solo o con otro componente.");
    expect(html).toContain("espera de 10 s");
    expect(html).toContain("?line=7");
  });
});

describe("JobletGuide", () => {
  test("sin joblets no muestra nada", () => {
    expect(renderToStaticMarkup(<JobletGuide plan={plan({ joblets: [] })} />)).toBe("");
  });

  test("muestra nombre, por qué, creación y botón copiar", () => {
    const html = renderToStaticMarkup(<JobletGuide plan={plan({ joblets: [joblet] })} />);
    expect(html).toContain("jl_Split3");
    expect(html).toContain("El mismo bloque aparece dos veces.");
    expect(html).toContain("Create Joblet.");
    expect(html).toContain("Copiar jl_Split3");
    expect(html).toContain("dwh.clientes");
  });
});

describe("FusedBadge", () => {
  test("solo aparece con dos o más operaciones fusionadas", () => {
    expect(renderToStaticMarkup(<FusedBadge fusedFrom={["op1"]} why="x" />)).toBe("");
    const html = renderToStaticMarkup(<FusedBadge fusedFrom={["op1", "op2", "op3"]} why="Filtro y cálculo en un tMap." />);
    expect(html).toContain("Reúne 3 operaciones del SAS");
    expect(html).toContain("Filtro y cálculo en un tMap.");
  });
});
