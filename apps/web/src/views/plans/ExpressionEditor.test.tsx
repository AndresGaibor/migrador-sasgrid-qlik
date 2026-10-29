import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ExpressionEditor, expressionDraftError } from "./ExpressionEditor";
import type { Step } from "../../types";

type Expression = Step["expressions"][number];
const base: Expression = { sas: "saldo + 10", talend: "(input_row.saldo + 10)", line: 3, warnings: [] };

function render(expression: Partial<Expression>, locked = false) {
  return renderToStaticMarkup(<ExpressionEditor id="p" file="a.sas" stepId="s1" index={0} expression={{ ...base, ...expression }} locked={locked} onSaved={() => {}} />);
}

test("shows the SAS and the current Java with an Editar button", () => {
  const html = render({});
  expect(html).toContain("saldo + 10");
  expect(html).toContain("(input_row.saldo + 10)");
  expect(html).toContain("Editar");
  expect(html).not.toContain("editada");
  expect(html).not.toContain("Volver a la traducción automática");
});

test("an edited expression shows the badge and the restore button", () => {
  const html = render({ talend_edited: true, talend: "input_row.saldo" });
  expect(html).toContain("editada");
  expect(html).toContain("Volver a la traducción automática");
});

test("without a translation it says so", () => {
  const html = render({ talend: null });
  expect(html).toContain("Sin traducción automática");
  expect(html).not.toContain("Volver a la traducción automática");
});

test("editing is disabled while Talend works", () => {
  expect(render({}, true)).toMatch(/<button[^>]*disabled=""[^>]*>Editar/);
});

test("validates the draft like the server does", () => {
  expect(expressionDraftError("")).toBeDefined();
  expect(expressionDraftError("   ")).toBeDefined();
  expect(expressionDraftError("a\nb")).toBeDefined();
  expect(expressionDraftError("x".repeat(2001))).toBeDefined();
  expect(expressionDraftError("input_row.a")).toBeUndefined();
});
