import { describe, expect, test } from "bun:test";
import { ConditionError, evaluateNotShowIf, evaluateShowIf, isParamVisible, parseCondition } from "./show-if";

describe("evaluateShowIf: comparaciones", () => {
  test("sin condición se muestra", () => {
    expect(evaluateShowIf(null, {})).toBe(true);
    expect(evaluateShowIf(undefined, {})).toBe(true);
    expect(evaluateShowIf("", {})).toBe(true);
    expect(evaluateShowIf("   ", {})).toBe(true);
  });

  test("igualdad con texto entre comillas", () => {
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: "false" })).toBe(false);
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: "True" })).toBe(false);
  });

  test("igualdad con texto vacío", () => {
    expect(evaluateShowIf("FIELD == ''", { FIELD: "" })).toBe(true);
    expect(evaluateShowIf("FIELD == ''", { FIELD: "x" })).toBe(false);
  });

  test("desigualdad", () => {
    expect(evaluateShowIf("FIELD != 'x'", { FIELD: "y" })).toBe(true);
    expect(evaluateShowIf("FIELD != 'x'", { FIELD: "x" })).toBe(false);
  });

  test("valores sin comillas", () => {
    expect(evaluateShowIf("FIELD == true", { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD == true", { FIELD: "false" })).toBe(false);
    expect(evaluateShowIf("FIELD == UTF-8", { FIELD: "UTF-8" })).toBe(true);
    expect(evaluateShowIf("FIELD == 1", { FIELD: "1" })).toBe(true);
  });

  test("comparar con texto que contiene espacios exige comillas", () => {
    expect(evaluateShowIf("FIELD == 'a b'", { FIELD: "a b" })).toBe(true);
    expect(evaluateShowIf("FIELD == 'a b'", { FIELD: "a" })).toBe(false);
  });

  test("escapes dentro de comillas", () => {
    expect(evaluateShowIf("FIELD == 'it\\'s'", { FIELD: "it's" })).toBe(true);
    expect(evaluateShowIf("FIELD == 'a\\\\b'", { FIELD: "a\\b" })).toBe(true);
  });

  test("campo booleano suelto equivale a == 'true'", () => {
    expect(evaluateShowIf("FIELD", { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD", { FIELD: "false" })).toBe(false);
    expect(evaluateShowIf("FIELD", {})).toBe(false);
  });

  test("espacios alrededor de los operadores y paréntesis", () => {
    expect(evaluateShowIf("(  FIELD   ==   'true'  )", { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD=='true'", { FIELD: "true" })).toBe(true);
  });
});

describe("evaluateShowIf: operadores lógicos", () => {
  const cases: [string, Record<string, string>, boolean][] = [
    ["(A == 'true') AND (B == 'false')", { A: "true", B: "false" }, true],
    ["(A == 'true') AND (B == 'false')", { A: "true", B: "true" }, false],
    ["(A == 'true') AND (B == 'false')", { A: "false", B: "false" }, false],
    ["(A == 'true') OR (B == 'false')", { A: "false", B: "false" }, true],
    ["(A == 'true') OR (B == 'false')", { A: "false", B: "true" }, false],
    ["NOT (A == 'true')", { A: "true" }, false],
    ["NOT (A == 'true')", { A: "false" }, true],
    ["NOT A == 'true'", { A: "false" }, true],
    ["NOT NOT (A == 'true')", { A: "true" }, true],
    ["(A == 'x') OR (B == 'y') AND (C == 'z')", { A: "x", B: "no", C: "no" }, true],
    ["(A == 'x') OR (B == 'y') AND (C == 'z')", { A: "no", B: "y", C: "no" }, false],
    ["(A == 'x') OR (B == 'y') AND (C == 'z')", { A: "no", B: "y", C: "z" }, true],
    ["((A == 'x') OR (B == 'y')) AND (C == 'z')", { A: "no", B: "y", C: "no" }, false],
    ["((A == 'x') OR (B == 'y')) AND (C == 'z')", { A: "no", B: "y", C: "z" }, true],
    ["(A == 'true') AND NOT (B == 'true') OR (C == 'true')", { A: "true", B: "true", C: "true" }, true],
    ["(A == 'true') AND NOT (B == 'true') OR (C == 'true')", { A: "true", B: "true", C: "false" }, false],
    ["(A == 'true') AND FLAG", { A: "true", FLAG: "true" }, true],
    ["(A == 'true') AND FLAG", { A: "true", FLAG: "false" }, false],
    ["(A != 'x') AND (B != 'y')", { A: "z", B: "z" }, true],
    ["(A != 'x') AND (B != 'y')", { A: "x", B: "z" }, false],
  ];
  for (const [expr, values, expected] of cases) {
    test(`${expr} con ${JSON.stringify(values)} → ${expected}`, () => {
      expect(evaluateShowIf(expr, values)).toBe(expected);
    });
  }

  test("AND es asociativo a la izquierda y OR tiene menor precedencia que AND", () => {
    // A OR B AND C equivale a A OR (B AND C): con A=true, B=false, C=false da true.
    expect(evaluateShowIf("(A == 'true') OR (B == 'true') AND (C == 'true')", { A: "true", B: "false", C: "false" })).toBe(true);
    // Con (A OR B) AND C daría false, así que el resultado distingue la precedencia.
    expect(parseCondition("(A == 'true') OR (B == 'true') AND (C == 'true')")).toMatchObject({ kind: "or" });
  });

  test("palabras clave en minúscula no son operadores: la condición no se entiende y se muestra", () => {
    expect(evaluateShowIf("(A == 'true') and (B == 'false')", { A: "true", B: "false" })).toBe(true);
    expect(evaluateNotShowIf("(A == 'true') and (B == 'false')", { A: "true", B: "false" })).toBe(false);
  });
});

describe("valores por defecto y valores actuales", () => {
  test("usa defaults cuando no hay valor actual", () => {
    expect(evaluateShowIf("FIELD == 'true'", {}, { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD == 'true'", {}, { FIELD: "false" })).toBe(false);
  });

  test("el valor actual prevalece sobre el default", () => {
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: "false" }, { FIELD: "true" })).toBe(false);
  });

  test("null o undefined en el mapa de valores caen al default", () => {
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: null }, { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: undefined }, { FIELD: "true" })).toBe(true);
  });

  test("un valor vacío explícito no cae al default", () => {
    expect(evaluateShowIf("FIELD == ''", { FIELD: "" }, { FIELD: "true" })).toBe(true);
    expect(evaluateShowIf("FIELD == 'true'", { FIELD: "" }, { FIELD: "true" })).toBe(false);
  });

  test("campo sin valor ni default vale cadena vacía", () => {
    expect(evaluateShowIf("FIELD == ''", {})).toBe(true);
    expect(evaluateShowIf("FIELD != 'x'", {})).toBe(true);
  });
});

describe("evaluateNotShowIf", () => {
  test("sin condición no se oculta", () => {
    expect(evaluateNotShowIf(null, {})).toBe(false);
    expect(evaluateNotShowIf("", {})).toBe(false);
  });

  test("se oculta cuando la condición se cumple", () => {
    expect(evaluateNotShowIf("FIELD == 'true'", { FIELD: "true" })).toBe(true);
    expect(evaluateNotShowIf("FIELD == 'true'", { FIELD: "false" })).toBe(false);
  });

  test("usa defaults", () => {
    expect(evaluateNotShowIf("(A == 'true') OR (B == 'true')", {}, { A: "false", B: "true" })).toBe(true);
  });
});

describe("condiciones no soportadas", () => {
  const unsupported = [
    "FIELD.compareTo('x') == 0",
    "FIELD.compareTo('x')",
    "FIELD == ",
    "(FIELD == 'x'",
    "FIELD == 'x')",
    "FIELD == 'sin cerrar",
    "== 'x'",
    "FIELD 'x'",
    "AND",
    "FIELD ==== 'x'",
    "FIELD == 'x' FIELD2 == 'y'",
    "NOT",
    "() ",
    "(FIELD == 'x') AND",
    "FIELD == AND",
    "FIELD ? 'x'",
    "'x' == FIELD",
    "A.B == 'x'",
  ];
  for (const expr of unsupported) {
    test(`«${expr}»: showIf muestra y notShowIf no oculta`, () => {
      expect(evaluateShowIf(expr, { FIELD: "x" })).toBe(true);
      expect(evaluateNotShowIf(expr, { FIELD: "x" })).toBe(false);
    });
  }

  test("parseCondition lanza ConditionError con un mensaje en español", () => {
    expect(() => parseCondition("FIELD.compareTo('x')")).toThrow(ConditionError);
    expect(() => parseCondition("(FIELD == 'x'")).toThrow("paréntesis");
  });
});

describe("parseCondition", () => {
  test("devuelve null para condición vacía", () => {
    expect(parseCondition(null)).toBeNull();
    expect(parseCondition("  ")).toBeNull();
  });

  test("devuelve el árbol de una comparación", () => {
    expect(parseCondition("FIELD == 'true'")).toEqual({ kind: "cmp", name: "FIELD", op: "==", value: "true" });
    expect(parseCondition("FIELD")).toEqual({ kind: "bool", name: "FIELD" });
  });
});

describe("isParamVisible", () => {
  const base = { show: true, showIf: null, notShowIf: null };

  test("un parámetro con show=false nunca se ve", () => {
    expect(isParamVisible({ ...base, show: false }, {})).toBe(false);
  });

  test("respeta SHOW_IF", () => {
    const p = { ...base, showIf: "USE == 'true'" };
    expect(isParamVisible(p, { USE: "true" })).toBe(true);
    expect(isParamVisible(p, { USE: "false" })).toBe(false);
  });

  test("respeta NOT_SHOW_IF", () => {
    const p = { ...base, notShowIf: "USE == 'true'" };
    expect(isParamVisible(p, { USE: "true" })).toBe(false);
    expect(isParamVisible(p, { USE: "false" })).toBe(true);
  });

  test("combina SHOW_IF y NOT_SHOW_IF", () => {
    const p = { ...base, showIf: "A == 'true'", notShowIf: "B == 'true'" };
    expect(isParamVisible(p, { A: "true", B: "false" })).toBe(true);
    expect(isParamVisible(p, { A: "true", B: "true" })).toBe(false);
    expect(isParamVisible(p, { A: "false", B: "false" })).toBe(false);
  });

  test("usa defaults para evaluar", () => {
    const p = { ...base, showIf: "A == 'true'" };
    expect(isParamVisible(p, {}, { A: "true" })).toBe(true);
  });
});
