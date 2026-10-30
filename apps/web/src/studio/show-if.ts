// Evaluador de las condiciones SHOW_IF / NOT_SHOW_IF de los paneles de Talend.
//
// Sintaxis soportada:
//   FIELD == 'true'            comparación con texto entre comillas simples
//   FIELD != 'x'               desigualdad
//   FIELD == true              valor sin comillas (una palabra)
//   FIELD                      campo booleano suelto: equivale a FIELD == 'true'
//   (A == 'true') AND (B == 'false')   AND, OR, NOT (en mayúsculas), con paréntesis
//
// Lo que no entiende (por ejemplo FIELD.compareTo('x')) no se evalúa:
// showIf devuelve true (se muestra) y notShowIf devuelve false (no se oculta).

/** Valores actuales por nombre de campo. `null`/`undefined` cuenta como «sin valor». */
export type ValueMap = Record<string, string | null | undefined>;

export type Condition =
  | { kind: "cmp"; name: string; op: "==" | "!="; value: string }
  | { kind: "bool"; name: string }
  | { kind: "and" | "or"; left: Condition; right: Condition }
  | { kind: "not"; expr: Condition };

export class ConditionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "ConditionError";
  }
}

type Token =
  | { kind: "lparen" | "rparen" | "op"; text: string }
  | { kind: "string" | "word"; text: string };

const KEYWORDS = new Set(["AND", "OR", "NOT"]);
const IDENTIFIER = /^[A-Za-z_][A-Za-z0-9_]*$/;
// Palabras sin comillas, nombres de campo y los dos operadores; el orden importa.
const TOKEN = /\s*(?:(\()|(\))|(==|!=)|'((?:[^'\\]|\\.)*)'|([A-Za-z0-9_.\-&$]+))/y;

function tokenize(source: string): Token[] {
  const tokens: Token[] = [];
  let pos = 0;
  while (pos < source.length) {
    if (/^\s*$/.test(source.slice(pos))) break;
    TOKEN.lastIndex = pos;
    const m = TOKEN.exec(source);
    if (!m) throw new ConditionError(`Símbolo no reconocido en «${source.slice(pos).trim()}»`);
    pos = TOKEN.lastIndex;
    if (m[1]) tokens.push({ kind: "lparen", text: "(" });
    else if (m[2]) tokens.push({ kind: "rparen", text: ")" });
    else if (m[3]) tokens.push({ kind: "op", text: m[3] });
    else if (m[4] !== undefined) tokens.push({ kind: "string", text: m[4].replace(/\\(.)/g, "$1") });
    else if (m[5]) tokens.push({ kind: "word", text: m[5] });
  }
  return tokens;
}

class Parser {
  private pos = 0;
  constructor(private readonly tokens: Token[]) {}

  parse(): Condition {
    const node = this.parseOr();
    if (this.pos < this.tokens.length) throw new ConditionError(`Sobra texto desde «${this.tokens[this.pos].text}»`);
    return node;
  }

  private peek(): Token | undefined {
    return this.tokens[this.pos];
  }

  private isKeyword(word: string): boolean {
    const t = this.peek();
    return t?.kind === "word" && t.text === word;
  }

  private parseOr(): Condition {
    let left = this.parseAnd();
    while (this.isKeyword("OR")) {
      this.pos++;
      left = { kind: "or", left, right: this.parseAnd() };
    }
    return left;
  }

  private parseAnd(): Condition {
    let left = this.parseUnary();
    while (this.isKeyword("AND")) {
      this.pos++;
      left = { kind: "and", left, right: this.parseUnary() };
    }
    return left;
  }

  private parseUnary(): Condition {
    if (this.isKeyword("NOT")) {
      this.pos++;
      return { kind: "not", expr: this.parseUnary() };
    }
    return this.parsePrimary();
  }

  private parsePrimary(): Condition {
    const t = this.peek();
    if (!t) throw new ConditionError("La condición termina antes de tiempo");
    if (t.kind === "lparen") {
      this.pos++;
      const inner = this.parseOr();
      if (this.peek()?.kind !== "rparen") throw new ConditionError("Falta el paréntesis de cierre");
      this.pos++;
      return inner;
    }
    if (t.kind !== "word") throw new ConditionError(`Se esperaba un campo y llegó «${t.text}»`);
    if (KEYWORDS.has(t.text)) throw new ConditionError(`Palabra reservada «${t.text}» donde se esperaba un campo`);
    if (!IDENTIFIER.test(t.text)) throw new ConditionError(`Nombre de campo no soportado «${t.text}»`);
    this.pos++;
    const next = this.peek();
    if (next?.kind !== "op") return { kind: "bool", name: t.text };
    this.pos++;
    const value = this.peek();
    if (!value || (value.kind !== "string" && value.kind !== "word")) throw new ConditionError("Falta el valor a comparar");
    if (value.kind === "word" && KEYWORDS.has(value.text)) throw new ConditionError(`Valor no válido «${value.text}»: use comillas`);
    this.pos++;
    return { kind: "cmp", name: t.text, op: next.text as "==" | "!=", value: value.text };
  }
}

/** Convierte el texto de una condición en un árbol. Devuelve null si está vacía; lanza ConditionError si no se entiende. */
export function parseCondition(source: string | null | undefined): Condition | null {
  if (source == null || source.trim() === "") return null;
  return new Parser(tokenize(source)).parse();
}

function lookup(name: string, values: ValueMap, defaults: ValueMap): string {
  return values[name] ?? defaults[name] ?? "";
}

function evaluate(node: Condition, values: ValueMap, defaults: ValueMap): boolean {
  switch (node.kind) {
    case "cmp": {
      const same = lookup(node.name, values, defaults) === node.value;
      return node.op === "==" ? same : !same;
    }
    case "bool":
      return lookup(node.name, values, defaults) === "true";
    case "and":
      return evaluate(node.left, values, defaults) && evaluate(node.right, values, defaults);
    case "or":
      return evaluate(node.left, values, defaults) || evaluate(node.right, values, defaults);
    case "not":
      return !evaluate(node.expr, values, defaults);
  }
}

/**
 * ¿Se muestra el campo según SHOW_IF? Sin condición o condición no soportada: true.
 * `values` son los valores actuales; `defaults` (defaultValue del parámetro) se usan cuando no hay valor.
 */
export function evaluateShowIf(expr: string | null | undefined, values: ValueMap, defaults: ValueMap = {}): boolean {
  try {
    const node = parseCondition(expr);
    return node ? evaluate(node, values, defaults) : true;
  } catch (error) {
    if (error instanceof ConditionError) return true;
    throw error;
  }
}

/**
 * ¿Se oculta el campo según NOT_SHOW_IF? Sin condición o condición no soportada: false.
 */
export function evaluateNotShowIf(expr: string | null | undefined, values: ValueMap, defaults: ValueMap = {}): boolean {
  try {
    const node = parseCondition(expr);
    return node ? evaluate(node, values, defaults) : false;
  } catch (error) {
    if (error instanceof ConditionError) return false;
    throw error;
  }
}

/** Un campo se ve si `show` es true, SHOW_IF se cumple y NOT_SHOW_IF no se cumple. */
export function isParamVisible(
  param: { show: boolean; showIf: string | null; notShowIf: string | null },
  values: ValueMap,
  defaults: ValueMap = {},
): boolean {
  return param.show && evaluateShowIf(param.showIf, values, defaults) && !evaluateNotShowIf(param.notShowIf, values, defaults);
}
