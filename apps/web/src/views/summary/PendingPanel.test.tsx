import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { PendingPanel, pendingText } from "./PendingPanel";
import type { PendingGroup } from "../../types";

test("shows totals, reasons and links to each pending Job", () => {
  const groups: PendingGroup[] = [
    {
      reason: "Falta configurar la conexión",
      steps: 2,
      programs: [
        { program: "a.sas", job_name: "job_a", step_ids: ["s1", "s2"] },
        { program: "b.sas", job_name: "job_b", step_ids: ["s1"] },
      ],
    },
    {
      reason: "Falta el contexto",
      steps: 1,
      programs: [{ program: "a.sas", job_name: "job_a", step_ids: ["s1"] }],
    },
  ];
  const html = renderToStaticMarkup(<PendingPanel id="p1" groups={groups} />);
  expect(html).toContain("Qué falta");
  expect(html).toContain("3 pasos en 2 Jobs");
  expect(html).toContain("Falta configurar la conexión");
  expect(html).toContain("Falta el contexto");
  expect(html).toContain('href="#/p/p1/planes/a.sas"');
  expect(html.match(/<details/g)).toHaveLength(2);
});

test("says there is nothing pending when there are no groups", () => {
  const html = renderToStaticMarkup(<PendingPanel id="p1" groups={[]} />);
  expect(html).toContain("No quedan pendientes.");
});

test("pendingText handles singular and plural", () => {
  expect(pendingText({ steps: 1, jobs: 1 })).toBe("1 paso en 1 Job");
  expect(pendingText({ steps: 2, jobs: 1 })).toBe("2 pasos en 1 Job");
  expect(pendingText({ steps: 3, jobs: 2 })).toBe("3 pasos en 2 Jobs");
});
