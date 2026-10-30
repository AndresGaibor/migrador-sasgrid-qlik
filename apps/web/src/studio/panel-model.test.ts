import { describe, expect, test } from "bun:test";
import { displayValue, groupByRow, hasSuggestion, rowsToTsv, tabProgress, visibleParams } from "./panel-model";
import type { GuideValues, Param } from "./panel-types";
import { dbGuide, fileInputGuide, panelsFixture } from "./__fixtures__/panels.fixture";

const param = (name: string, numRow: number | null, extra: Partial<Param> = {}): Param => ({
  name, label: name, field: "TEXT", required: false, show: true, showIf: null, notShowIf: null,
  defaultValue: null, numRow, group: null, repositoryValue: null, options: null, table: null, ...extra,
});

describe("groupByRow", () => {
  test("agrupa por numRow en orden ascendente y conserva el orden dentro de cada fila", () => {
    const rows = groupByRow([param("c", 2), param("a", 1), param("b", 1), param("d", 2)]);
    expect(rows.map((r) => r.map((p) => p.name))).toEqual([["a", "b"], ["c", "d"]]);
  });

  test("los parámetros sin numRow van al final, cada uno en su fila", () => {
    const rows = groupByRow([param("x", null), param("a", 1), param("y", null), param("b", 1)]);
    expect(rows.map((r) => r.map((p) => p.name))).toEqual([["a", "b"], ["x"], ["y"]]);
  });

  test("lista vacía no produce filas", () => {
    expect(groupByRow([])).toEqual([]);
  });

  test("no mutan la entrada", () => {
    const input = [param("b", 2), param("a", 1)];
    groupByRow(input);
    expect(input.map((p) => p.name)).toEqual(["b", "a"]);
  });

  test("las filas del fixture de tFileInputDelimited salen en el orden de Studio", () => {
    const basic = panelsFixture.components.tFileInputDelimited.tabs.basic;
    const names = groupByRow(basic).map((r) => r.map((p) => p.name));
    expect(names[0]).toEqual(["PROPERTY_TYPE"]);
    expect(names[3]).toEqual(["ROWSEPARATOR", "FIELDSEPARATOR"]);
    expect(names[names.length - 1]).toEqual(["DIE_ON_ERROR"]);
  });
});

describe("visibleParams", () => {
  test("oculta los campos con show=false", () => {
    const params = [param("A", 1), param("B", 2, { show: false })];
    expect(visibleParams(params, {}).map((p) => p.name)).toEqual(["A"]);
  });

  test("usa las sugerencias de la guía para SHOW_IF", () => {
    const db = panelsFixture.components.tDBInput.tabs.basic;
    const names = (values: GuideValues) => visibleParams(db, values).map((p) => p.name);
    // Sin sugerencia, USE_EXISTING_CONNECTION toma su default (false): se ven HOST y PORT.
    expect(names({})).toContain("HOST");
    expect(names({ USE_EXISTING_CONNECTION: { value: "true" } })).not.toContain("HOST");
    expect(names({ USE_EXISTING_CONNECTION: { value: "true" } })).toContain("EXISTING_CONN_NOTE");
  });

  test("el fixture de tDBInput con la guía de conexión", () => {
    const names = visibleParams(panelsFixture.components.tDBInput.tabs.basic, dbGuide).map((p) => p.name);
    expect(names).toEqual(expect.arrayContaining(["DB_TYPE", "HOST", "PORT", "DBNAME", "PASS", "QUERY"]));
    expect(names).not.toContain("EXISTING_CONN_NOTE");
  });

  test("el default alimenta SHOW_IF cuando no hay sugerencia", () => {
    const params = [param("FLAG", 1, { defaultValue: "true" }), param("X", 2, { showIf: "FLAG == 'true'" })];
    expect(visibleParams(params, {}).map((p) => p.name)).toEqual(["FLAG", "X"]);
    expect(visibleParams(params, { FLAG: { value: "false" } }).map((p) => p.name)).toEqual(["FLAG"]);
  });
});

describe("hasSuggestion y displayValue", () => {
  test("hay sugerencia con value (aunque sea vacío) o con filas", () => {
    expect(hasSuggestion("A", { A: { value: "" } })).toBe(true);
    expect(hasSuggestion("A", { A: { rows: [{ x: "1" }] } })).toBe(true);
    expect(hasSuggestion("A", { A: { rows: [] } })).toBe(false);
    expect(hasSuggestion("A", { A: { why: "solo explicación" } })).toBe(false);
    expect(hasSuggestion("A", {})).toBe(false);
  });

  test("el valor mostrado es la sugerencia o el default", () => {
    const p = param("A", 1, { defaultValue: "dflt" });
    expect(displayValue(p, { A: { value: "sug" } })).toBe("sug");
    expect(displayValue(p, {})).toBe("dflt");
    expect(displayValue(param("B", 1), {})).toBe("");
  });
});

describe("tabProgress", () => {
  const params = [param("A", 1), param("B", 2), param("C", 3), param("D", 4, { show: false })];

  test("cuenta solo los visibles con sugerencia", () => {
    const values: GuideValues = { A: { value: "1" }, B: { value: "2" }, C: { why: "sin valor" }, D: { value: "x" } };
    expect(tabProgress(params, values, {})).toEqual({ done: 0, total: 2, active: "A" });
  });

  test("cuenta hechos y señala el primer pendiente en orden de pantalla", () => {
    const values: GuideValues = { A: { value: "1" }, B: { value: "2" }, C: { value: "3" } };
    expect(tabProgress(params, values, { B: true })).toEqual({ done: 1, total: 3, active: "A" });
    expect(tabProgress(params, values, { A: true, B: true, C: true })).toEqual({ done: 3, total: 3, active: null });
  });

  test("sin sugerencias el progreso es 0 de 0", () => {
    expect(tabProgress(params, {}, {})).toEqual({ done: 0, total: 0, active: null });
  });

  test("progreso de un fixture real", () => {
    const basic = panelsFixture.components.tFileInputDelimited.tabs.basic;
    const p = tabProgress(basic, fileInputGuide, { FILENAME: true });
    // SCHEMA_TYPE, FILENAME, FIELDSEPARATOR y HEADER tienen sugerencia visible en la pestaña básica.
    expect(p.total).toBe(4);
    expect(p.done).toBe(1);
    // SCHEMA_TYPE va en la fila 2, antes que FILENAME (fila 3), así que es el siguiente pendiente.
    expect(p.active).toBe("SCHEMA_TYPE");
  });
});

describe("rowsToTsv", () => {
  test("cabecera con las etiquetas de columna y una fila por registro", () => {
    const tsv = rowsToTsv(
      [{ name: "SCHEMA_COLUMN", label: "Column" }, { name: "TRIM", label: "Trim" }],
      [{ SCHEMA_COLUMN: "NOMBRE", TRIM: "true" }, { SCHEMA_COLUMN: "ID" }],
    );
    expect(tsv).toBe("Column\tTrim\nNOMBRE\ttrue\nID\t");
  });

  test("limpia tabuladores y saltos de línea dentro de una celda", () => {
    expect(rowsToTsv([{ name: "A", label: "A" }], [{ A: "x\ty\nz" }])).toBe("A\nx y z");
  });
});
