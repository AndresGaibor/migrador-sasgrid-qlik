import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { Load } from "./common";

test("keeps the last loaded content visible when refresh fails", () => {
  const html = renderToStaticMarkup(
    <Load q={{ data: "saved projects", error: "service unavailable", loading: false, reload: () => {} }}>
      {(data) => <p>{data}</p>}
    </Load>,
  );
  expect(html).toContain("No se pudo actualizar la información");
  expect(html).toContain("Se muestran los datos anteriores.");
  expect(html).toContain("saved projects");
  expect(html).toContain("Volver a intentar");
});

test("shows a retry message when the first load fails", () => {
  const html = renderToStaticMarkup(
    <Load q={{ error: "service unavailable", loading: false, reload: () => {} }}>
      {(data: string) => <p>{data}</p>}
    </Load>,
  );
  expect(html).toContain("No pudimos cargar esta información");
  expect(html).not.toContain("Se muestran los datos anteriores.");
  expect(html).toContain("Volver a intentar");
});
