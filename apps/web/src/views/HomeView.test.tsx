import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { HomeView } from "./HomeView";

test("home separates onboarding from project management and offers direct ZIP creation", () => {
  const html = renderToStaticMarkup(<HomeView />);
  expect(html).toContain('href="#/projects"');
  expect(html).toContain('href="#/projects/nuevo"');
  expect(html).toContain("Cómo funciona");
  expect(html).not.toContain('class="project-grid"');
});
