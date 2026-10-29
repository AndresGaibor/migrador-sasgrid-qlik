import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { JobIdentity } from "./JobIdentity";

test("marks a Job whose name was edited and shows its description and destination", () => {
  const html = renderToStaticMarkup(
    <JobIdentity
      plan={{ job_name: "fin_daily", description: "Carga diaria", job_name_edited: true }}
      folderPath="Process/Finanzas"
    />,
  );
  expect(html).toContain("fin_daily");
  expect(html).toContain("editado");
  expect(html).toContain("Carga diaria");
  expect(html).toContain("Process/Finanzas");
});

test("keeps the generated name clean when nothing was edited", () => {
  const html = renderToStaticMarkup(<JobIdentity plan={{ job_name: "job_daily", description: null }} />);
  expect(html).toContain("job_daily");
  expect(html).not.toContain("editado");
});
