import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { TRANSLATOR_EXAMPLES, TranslatorView, TranslationResult } from "./TranslatorView";
import type { TranslateResult } from "../types";

const base: TranslateResult = { sas: "x", talend: "input_row.x", columns: ["x"], warnings: [], engine: "inline", supported: true, talend_engine_enabled: false };

test("initial state shows the textarea, the translate button and three examples", () => {
  const html = renderToStaticMarkup(<TranslatorView />);
  expect(html).toContain("<textarea");
  expect(html).toContain('maxLength="20000"');
  expect(html).toContain("Traducir");
  expect(TRANSLATOR_EXAMPLES).toHaveLength(3);
  for (const example of TRANSLATOR_EXAMPLES) expect(html).toContain(example.replace(/&/g, "&amp;"));
});

test("shows the Java, columns, warnings and engine of a translation", () => {
  const html = renderToStaticMarkup(<TranslationResult result={{ ...base, columns: ["a", "b"], warnings: ["cuidado"] }} />);
  expect(html).toMatch(/<pre[^>]*>input_row\.x<\/pre>/);
  expect(html).toContain("a");
  expect(html).toContain("cuidado");
  expect(html).toContain("inline");
  expect(html).not.toContain("SGM_TALEND_EXPRESSIONS");
});

test("explains that the extended translator is off when there is no translation", () => {
  const html = renderToStaticMarkup(<TranslationResult result={{ ...base, talend: null, supported: false }} />);
  expect(html).toContain("El traductor ampliado con rutinas de Talend está apagado");
  expect(html).toContain("SGM_TALEND_EXPRESSIONS");
  expect(html).toContain("Sin traducción automática");
});

test("does not show the off note when the extended translator is enabled", () => {
  const html = renderToStaticMarkup(<TranslationResult result={{ ...base, talend: null, talend_engine_enabled: true }} />);
  expect(html).not.toContain("SGM_TALEND_EXPRESSIONS");
});
