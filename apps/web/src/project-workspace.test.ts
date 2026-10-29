import { describe, expect, test } from "bun:test";
import {
  filterArchiveEntries,
  filterFilesByKind,
  filterProjectsByFacets,
  filterProjectsByQuery,
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

test("cuenta pasos y Jobs distintos aunque un Job aparezca en dos motivos", () => {
  const group = (reason: string, steps: number, programs: string[]) => ({
    reason,
    steps,
    programs: programs.map((program) => ({ program, job_name: `job_${program}`, step_ids: [] })),
  });

  expect(pendingTotals([])).toEqual({ steps: 0, jobs: 0 });
  expect(pendingTotals([
    group("Esquema sin confirmar", 2, ["daily.sas", "other.sas"]),
    group("Expresión sin traducir", 1, ["daily.sas"]),
  ])).toEqual({ steps: 3, jobs: 2 });
});
