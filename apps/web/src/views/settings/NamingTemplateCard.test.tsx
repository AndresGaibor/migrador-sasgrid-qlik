import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { NamingTemplateCard } from "./NamingTemplateCard";

const initial = {
  template: "job_{programa}",
  default_template: "job_{programa}",
  tokens: ["proyecto", "carpeta", "programa"],
  example_name: "job_cod_2",
};

test("shows every token, the current template and the fixed explanation", () => {
  const html = renderToStaticMarkup(<NamingTemplateCard initial={initial} />);
  expect(html).toContain("{proyecto}");
  expect(html).toContain("{carpeta}");
  expect(html).toContain("{programa}");
  expect(html).toContain("job_{programa}");
  expect(html).toContain(
    "Se aplica al preparar o actualizar las guías. Los nombres que editaste a mano no cambian.",
  );
  expect(html).toContain("Restaurar job_{programa}");
});

test("keeps save disabled until the template changes", () => {
  const html = renderToStaticMarkup(<NamingTemplateCard initial={initial} />);
  expect(/<button[^>]*disabled[^>]*>Guardar plantilla<\/button>/.test(html)).toBe(true);
});
