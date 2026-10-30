import { describe, expect, test } from "bun:test";
import { differsFromSas, sasFamily, sasOriginText, schemaColumnsFromRows, schemaShape, schemaToTsv, talendFamily } from "./schema-model";
import type { SchemaColumn } from "./panel-types";

describe("talendFamily y sasFamily", () => {
  test("familias de tipos Talend", () => {
    expect(talendFamily("String")).toBe("string");
    expect(talendFamily("Character")).toBe("string");
    for (const t of ["Integer", "Long", "Short", "Byte", "Double", "Float", "BigDecimal"]) expect(talendFamily(t)).toBe("number");
    expect(talendFamily("Date")).toBe("date");
    expect(talendFamily("Boolean")).toBe("boolean");
    expect(talendFamily("Object")).toBe("other");
    expect(talendFamily("  integer ")).toBe("number");
  });

  test("familias de tipos SAS", () => {
    expect(sasFamily("char")).toBe("string");
    expect(sasFamily("num")).toBe("number");
    expect(sasFamily("date")).toBe("date");
    expect(sasFamily("datetime")).toBe("date");
    expect(sasFamily("time")).toBe("date");
    expect(sasFamily("otra")).toBeNull();
    expect(sasFamily("")).toBeNull();
    expect(sasFamily(null)).toBeNull();
  });
});

describe("differsFromSas", () => {
  const base: SchemaColumn = { name: "ID", type: "Integer" };
  test("sin origen SAS no hay diferencia", () => {
    expect(differsFromSas(base)).toBe(false);
  });
  test("char en String no difiere; char en Integer sí", () => {
    expect(differsFromSas({ ...base, type: "String", sasType: "char" })).toBe(false);
    expect(differsFromSas({ ...base, type: "Integer", sasType: "char" })).toBe(true);
  });
  test("num en Double no difiere; num en String sí", () => {
    expect(differsFromSas({ ...base, type: "Double", sasType: "num" })).toBe(false);
    expect(differsFromSas({ ...base, type: "String", sasType: "num" })).toBe(true);
  });
  test("date en Date no difiere", () => {
    expect(differsFromSas({ ...base, type: "Date", sasType: "date" })).toBe(false);
    expect(differsFromSas({ ...base, type: "String", sasType: "date" })).toBe(true);
  });
  test("tipo SAS desconocido no marca diferencia", () => {
    expect(differsFromSas({ ...base, type: "Object", sasType: "raro" })).toBe(false);
  });
});

describe("schemaColumnsFromRows", () => {
  test("convierte filas de la guía en columnas tipadas", () => {
    const cols = schemaColumnsFromRows([
      { name: "ID", type: "Integer", key: "true", nullable: "false", length: "10", precision: "", sasType: "num", sasFormat: "BEST12." },
      { name: "NOMBRE", type: "", nullable: "true", length: "x", pattern: "", comment: "Nombre del cliente" },
    ]);
    expect(cols[0]).toEqual({
      name: "ID", type: "Integer", key: true, nullable: false, length: 10, precision: null,
      pattern: null, default: null, sasType: "num", sasFormat: "BEST12.", comment: null,
    });
    expect(cols[1]).toEqual({
      name: "NOMBRE", type: "String", key: false, nullable: true, length: null, precision: null,
      pattern: null, default: null, sasType: null, sasFormat: null, comment: "Nombre del cliente",
    });
  });

  test("descarta filas sin nombre y recorta espacios", () => {
    const cols = schemaColumnsFromRows([{ name: "  ", type: "String" }, { name: " A ", type: " Date " }]);
    expect(cols.map((c) => [c.name, c.type])).toEqual([["A", "Date"]]);
  });

  test("reconoce «sí» y «1» como verdadero", () => {
    const [a, b, c] = schemaColumnsFromRows([
      { name: "a", type: "String", key: "sí" },
      { name: "b", type: "String", key: "1" },
      { name: "c", type: "String", key: "no" },
    ]);
    expect([a.key, b.key, c.key]).toEqual([true, true, false]);
  });
});

describe("schemaShape y textos", () => {
  test("muestra Date Pattern solo si hay columnas Date", () => {
    expect(schemaShape([{ name: "a", type: "String" }]).hasDatePattern).toBe(false);
    expect(schemaShape([{ name: "a", type: "Date" }]).hasDatePattern).toBe(true);
  });

  test("muestra SAS origen solo si hay tipos SAS", () => {
    expect(schemaShape([{ name: "a", type: "String" }]).hasSasOrigin).toBe(false);
    expect(schemaShape([{ name: "a", type: "String", sasType: "char" }]).hasSasOrigin).toBe(true);
  });

  test("texto de origen SAS", () => {
    expect(sasOriginText({ name: "a", type: "Date", sasType: "num", sasFormat: "DATE9." })).toBe("num DATE9.");
    expect(sasOriginText({ name: "a", type: "String", sasType: "char" })).toBe("char");
    expect(sasOriginText({ name: "a", type: "String" })).toBe("");
  });
});

describe("schemaToTsv", () => {
  test("cabecera básica sin columnas opcionales", () => {
    const tsv = schemaToTsv([{ name: "ID", type: "Integer", key: true, nullable: false, length: 10 }]);
    const [head, row] = tsv.split("\n");
    expect(head.split("\t")).toEqual(["Column", "Key", "Type", "Nullable", "Length", "Precision", "Default", "Comment"]);
    expect(row.split("\t")).toEqual(["ID", "true", "Integer", "false", "10", "", "", ""]);
  });

  test("añade Date Pattern y SAS origen cuando aplican", () => {
    const tsv = schemaToTsv([
      { name: "FECHA", type: "Date", pattern: "yyyy-MM-dd", sasType: "num", sasFormat: "DATE9." },
    ]);
    const [head, row] = tsv.split("\n");
    expect(head.split("\t").slice(-2)).toEqual(["Date Pattern", "SAS origen"]);
    expect(row.split("\t").slice(-2)).toEqual(["yyyy-MM-dd", "num DATE9."]);
  });

  test("no rompe la tabla con tabuladores o saltos de línea dentro de un comentario", () => {
    const tsv = schemaToTsv([{ name: "A", type: "String", comment: "uno\tdos\nTres" }]);
    expect(tsv.split("\n")).toHaveLength(2);
    expect(tsv.split("\n")[1].split("\t")[7]).toBe("uno dos Tres");
  });

  test("sin columnas devuelve solo la cabecera", () => {
    expect(schemaToTsv([]).split("\n")).toHaveLength(1);
  });
});
