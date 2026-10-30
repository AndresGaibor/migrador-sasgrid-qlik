import { describe, expect, test } from "bun:test";
import { contextEnvs, contextRows, contextSummary, studioType } from "./context-model";

const plan = (vars: unknown[], libs: unknown[] = []) => ({ context_variables: vars, libraries_needed: libs }) as Parameters<typeof contextRows>[0];

describe("contextRows", () => {
  test("un secreto sale como Password sin valor y marcado pendiente", () => {
    const [row] = contextRows(plan([{ name: "clave", suggested: "", sas_value: "abc123", talend_type: "id_Password", is_secret: true }]));
    expect(row).toMatchObject({ name: "clave", type: "Password", value: "", secret: true, needsValue: true });
  });
  test("una variable normal conserva su valor y no queda pendiente", () => {
    const [row] = contextRows(plan([{ name: "wsplit", suggested: "3500000", sas_value: "3500000", talend_type: "id_Integer", sas_line: 12 }]));
    expect(row).toMatchObject({ name: "wsplit", type: "Integer", value: "3500000", needsValue: false });
    expect(row?.comment).toContain("12");
  });
  test("un placeholder sin resolver queda pendiente", () => {
    const [row] = contextRows(plan([{ name: "dataset5", suggested: "", sas_value: "$dataset5", needs_value: true }]));
    expect(row?.needsValue).toBe(true);
  });
  test("las librerías de archivos añaden su variable _DIR", () => {
    const rows = contextRows(plan([], [{ sas_name: "dwh", engine: null, path: "/data/dwh", suggested_connection: "" }, { sas_name: "db", engine: "oracle", path: null, suggested_connection: "" }]));
    expect(rows.map((r) => r.name)).toEqual(["DWH_DIR"]);
  });
});

describe("ambientes y resumen", () => {
  test("solo pide los ambientes que alguna variable distingue", () => {
    const rows = contextRows(plan([{ name: "ambiente", suggested: "D", sas_value: "D", group_values: { DEV: "d", PROD: "p" } }]));
    expect(contextEnvs(rows)).toEqual(["DEV", "PROD"]);
  });
  test("cuenta secretos y valores pendientes por separado", () => {
    const rows = contextRows(plan([
      { name: "a", suggested: "1", sas_value: "1" },
      { name: "b", suggested: "", sas_value: null },
      { name: "c", suggested: "", sas_value: null, is_secret: true, talend_type: "id_Password" },
    ]));
    expect(contextSummary(rows)).toEqual({ total: 3, secrets: 1, pending: 1 });
  });
  test("studioType quita el prefijo y usa String por defecto", () => {
    expect(studioType("id_Date")).toBe("Date");
    expect(studioType(undefined)).toBe("String");
  });
});
