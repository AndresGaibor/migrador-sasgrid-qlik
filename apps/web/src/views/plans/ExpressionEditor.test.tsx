import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ExpressionEditor } from "./ExpressionEditor";

test("shows the SAS source beside an editable Talend expression", () => {
  const html = renderToStaticMarkup(
    <ExpressionEditor
      id="step-1-0"
      expression={{ sas: "amount > 0", talend: "row.amount > 0", line: 12, warnings: [] }}
      onSave={async () => undefined}
    />,
  );

  expect(html).toContain("Expresión SAS · línea 12");
  expect(html).toContain("amount &gt; 0");
  expect(html).toContain('aria-label="Expresión Talend"');
  expect(html).toContain("Guardar expresión");
  expect(html).toContain("Restaurar traducción sugerida");
});
