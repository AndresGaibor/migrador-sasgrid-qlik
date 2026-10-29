import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { TranslatorView } from "./TranslatorView";

test("offers the SAS input and one-click examples before translating", () => {
  const html = renderToStaticMarkup(<TranslatorView />);
  expect(html).toContain('aria-label="Expresión SAS"');
  expect(html).toContain("Traducir");
  expect(html).toContain("Comparar texto");
  expect(html).toContain("Limpiar texto");
  expect(html).toContain("Extraer año");
});
