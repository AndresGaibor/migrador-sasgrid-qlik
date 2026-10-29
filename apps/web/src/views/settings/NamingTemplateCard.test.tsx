import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { NamingTemplateCard } from "./NamingTemplateCard";
import type { NamingTemplate } from "../../types";

const initial: NamingTemplate = { template: "job_{programa}", default: "job_{programa}", tokens: ["{proyecto}", "{carpeta}", "{programa}"] };

test("renders the tokens, the default template and the fixed help text from the initial value", () => {
  const html = renderToStaticMarkup(<NamingTemplateCard initial={initial} />);
  expect(html).toContain("{proyecto}");
  expect(html).toContain("{carpeta}");
  expect(html).toContain("{programa}");
  expect(html).toContain("job_{programa}");
  expect(html).toContain("Se aplica al preparar o actualizar las guías. Los nombres que editaste a mano no cambian.");
});

test("disables Guardar while the template is unchanged", () => {
  const html = renderToStaticMarkup(<NamingTemplateCard initial={initial} />);
  expect(html).toMatch(/<button[^>]*disabled=""[^>]*>Guardar<\/button>/);
});
