import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ProjectNavigation } from "./ProjectView";

test("project navigation prioritizes four work sections and groups secondary destinations", () => {
  const html = renderToStaticMarkup(<ProjectNavigation id="project" active="planes" hasArchive />);
  const primary = html.slice(0, html.indexOf("<details"));
  expect(primary.match(/<a /g)).toHaveLength(4);
  expect(primary).toContain("Dependencias");
  expect(primary).toContain('href="#/p/project/planes" aria-current="page"');
  expect(primary).not.toContain("inventario");
  expect(html).toContain('href="#/p/project/inventario"');
  expect(html).toContain('href="#/p/project/exportar"');
  expect(html).not.toContain('href="#/p/project/importar"');
});

test("manual projects retain import access and secondary pages keep their active state", () => {
  const html = renderToStaticMarkup(<ProjectNavigation id="project" active="inventario" hasArchive={false} />);
  expect(html).toContain('href="#/p/project/importar"');
  expect(html).toContain('href="#/p/project/inventario" aria-current="page"');
  expect(html).toContain('class="is-active">Mis archivos');
});
