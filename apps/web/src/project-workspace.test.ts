import { describe, expect, test } from "bun:test";
import {
  filterArchiveEntries,
  filterFilesByKind,
  filterProjectsByFacets,
  filterProjectsByQuery,
  groupPendingDecisions,
  pendingTotals,
  processingLabel,
} from "./project-workspace";

describe("aislamiento y estado del proyecto ZIP", () => {
  test("busca por el nombre del proyecto y el ZIP de origen", () => {
    const projects = [
      { id: "one", name: "Clientes", archive_name: "ts-sasgrid-legacy.zip" },
      { id: "two", name: "Seguros", archive_name: "insurance.zip" },
    ];

    expect(filterProjectsByQuery(projects, "sasgrid").map((item) => item.id)).toEqual(["one"]);
    expect(filterProjectsByQuery(projects, "seguros").map((item) => item.id)).toEqual(["two"]);
  });

  test("filtra proyectos por estado del análisis y origen", () => {
    const projects = [
      { id: "zip", name: "ZIP", archive_name: "proyecto.zip", processing: { status: "completed" } },
      { id: "sas", name: "SAS", archive_name: "programa.txt", processing: { status: "running" } },
      { id: "manual", name: "Manual", archive_name: null, processing: { status: "failed" } },
      { id: "legacy", name: "Anterior", archive_name: null, processing: null },
    ];

    expect(filterProjectsByFacets(projects, "processing", "all").map((item) => item.id)).toEqual(["sas"]);
    expect(filterProjectsByFacets(projects, "attention", "all").map((item) => item.id)).toEqual(["manual"]);
    expect(filterProjectsByFacets(projects, "all", "individual").map((item) => item.id)).toEqual(["sas"]);
    expect(filterProjectsByFacets(projects, "waiting", "manual").map((item) => item.id)).toEqual(["legacy"]);
  });

  test("explica la etapa activa, el éxito y un fallo de análisis", () => {
    expect(processingLabel({ status: "queued", stage: "queued" })).toBe("En cola");
    expect(processingLabel({ status: "running", stage: "dependencies" })).toBe(
      "Construyendo dependencias",
    );
    expect(processingLabel({ status: "completed", stage: "completed" })).toBe("Análisis listo");
    expect(processingLabel({ status: "failed", stage: "analysis" })).toBe("Error en el análisis");
    expect(processingLabel({ status: "interrupted", stage: "plans" })).toBe("Interrumpido");
  });

  test("filtra archivos por ruta completa incluso si llega con separadores de Windows", () => {
    const entries = [
      { path: "Banking/Reports/monthly.sas", value: 1 },
      { path: "Insurance/policy.sas", value: 2 },
    ];

    expect(filterArchiveEntries(entries, "banking\\reports").map((item) => item.value)).toEqual([1]);
    expect(filterArchiveEntries(entries, "policy").map((item) => item.value)).toEqual([2]);
  });

  test("filtra el inventario por tipo sin alterar la lista original", () => {
    const files = [
      { path: "daily.sas", kind: "sas" },
      { path: "notes.md", kind: "doc" },
      { path: "run.sh", kind: "shell" },
    ];

    expect(filterFilesByKind(files, "sas").map((file) => file.path)).toEqual(["daily.sas"]);
    expect(filterFilesByKind(files, "all")).toEqual(files);
    expect(files).toHaveLength(3);
  });
});

test("cuenta pasos y Jobs distintos: un paso con dos motivos cuenta una vez", () => {
  const group = (reason: string, programs: { program: string; steps: string[] }[]) => ({
    reason,
    steps: programs.reduce((total, item) => total + item.steps.length, 0),
    programs: programs.map((item) => ({ program: item.program, job_name: `job_${item.program}`, step_ids: item.steps })),
  });

  expect(pendingTotals([])).toEqual({ steps: 0, jobs: 0 });
  expect(pendingTotals([
    group("Esquema sin confirmar", [{ program: "daily.sas", steps: ["s1", "s2"] }, { program: "other.sas", steps: ["s1"] }]),
    group("Expresión sin traducir", [{ program: "daily.sas", steps: ["s2", "s3"] }]),
  ])).toEqual({ steps: 4, jobs: 2 });
});

test("agrupa las librerías SAS en una sola decisión y ordena por pasos", () => {
  const group = (reason: string, steps: string[]) => ({
    reason,
    steps: steps.length,
    programs: [{ program: "daily.sas", job_name: "job_daily", step_ids: steps }],
  });
  const decisions = groupPendingDecisions([
    group("Librería archive es de tipo BASE en /data/sas/archive: Talend no lee .sas7bdat directamente; confirmar copia", ["a1", "a2"]),
    group("Librería dictionary es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar copia", ["d1"]),
    group("Confirmar el esquema", ["e1", "e2", "e3"]),
  ]);

  expect(decisions.map((decision) => decision.title)).toEqual([
    "Confirmar el esquema",
    "Librerías SAS que Talend no lee directamente",
  ]);
  const libraries = decisions[1]!;
  expect(libraries.steps).toBe(3);
  expect(libraries.parts).toEqual([
    { title: "archive", detail: "/data/sas/archive", steps: 2, jobs: [{ program: "daily.sas", jobName: "job_daily", steps: 2 }] },
    { title: "dictionary", detail: "sin ruta fija", steps: 1, jobs: [{ program: "daily.sas", jobName: "job_daily", steps: 1 }] },
  ]);
});
