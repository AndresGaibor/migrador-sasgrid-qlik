import { describe, expect, test } from "bun:test";
import { countNotMigrated, groupNotMigrated } from "./not-migrated-model";
import type { NotMigrated } from "../types";

const entry = (over: Partial<NotMigrated>): NotMigrated => ({
  category: "troceado_lotes",
  lines: [10],
  what: "macro %split2 no se migra: troceado de tablas en lotes",
  reason: "Reparte la carga en trozos.",
  talend_equivalent: "Batch size en el componente de salida.",
  ...over,
});

describe("countNotMigrated", () => {
  test("cuenta entradas, no grupos", () => {
    expect(countNotMigrated([])).toBe(0);
    expect(countNotMigrated([entry({}), entry({ lines: [14] })])).toBe(2);
  });
});

describe("groupNotMigrated", () => {
  test("una misma descripción se agrupa y reúne sus líneas", () => {
    const groups = groupNotMigrated([entry({ lines: [14] }), entry({ lines: [10, 14] })]);
    expect(groups).toHaveLength(1);
    expect(groups[0].count).toBe(2);
    expect(groups[0].lines).toEqual([10, 14]);
    expect(groups[0].reason).toBe("Reparte la carga en trozos.");
    expect(groups[0].talend_equivalent).toBe("Batch size en el componente de salida.");
  });

  test("descripciones distintas dan grupos distintos, ordenados por la primera línea", () => {
    const groups = groupNotMigrated([
      entry({ what: "espera", category: "espera", lines: [30] }),
      entry({ what: "conteo", category: "conteo", lines: [5] }),
    ]);
    expect(groups.map((g) => g.what)).toEqual(["conteo", "espera"]);
  });

  test("elimina líneas duplicadas y tolera listas vacías", () => {
    const groups = groupNotMigrated([entry({ lines: [7, 7] }), entry({ lines: [] })]);
    expect(groups[0].lines).toEqual([7]);
    expect(groups[0].count).toBe(2);
  });

  test("sin entradas no hay grupos", () => {
    expect(groupNotMigrated([])).toEqual([]);
  });
});
