import { describe, expect, test } from "bun:test";
import { filterArchiveEntries, filterProjectsByQuery, processingLabel } from "./project-workspace";

describe("aislamiento y estado del proyecto ZIP", () => {
  test("busca por el nombre del proyecto y el ZIP de origen", () => {
    const projects = [
      { id: "one", name: "Clientes", archive_name: "ts-sasgrid-legacy.zip" },
      { id: "two", name: "Seguros", archive_name: "insurance.zip" },
    ];

    expect(filterProjectsByQuery(projects, "sasgrid").map((item) => item.id)).toEqual(["one"]);
    expect(filterProjectsByQuery(projects, "seguros").map((item) => item.id)).toEqual(["two"]);
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
});
