import { readFileSync } from "node:fs";
import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { BulkRename, renameSummary, shouldCloseBulkRename } from "./BulkRename";

test("the dialog refuses to close while a rename request is in flight", () => {
  expect(shouldCloseBulkRename(true)).toBe(false);
  expect(shouldCloseBulkRename(false)).toBe(true);
});
import type { RenamePreviewRow } from "../../types";

test("renameSummary is empty-safe and needs changes without errors", () => {
  expect(renameSummary([])).toEqual({ changes: 0, errors: 0, canApply: false });
  const changed = (program: string, current: string, proposed: string): RenamePreviewRow => ({ program, current, proposed, error: null });
  expect(renameSummary([changed("a.sas", "job_a", "pre_job_a"), changed("b.sas", "job_b", "pre_job_b")])).toEqual({ changes: 2, errors: 0, canApply: true });
  expect(renameSummary([changed("a.sas", "job_a", "pre_job_a"), { program: "b.sas", current: "job_b", proposed: "job_b", error: "Nombre duplicado" }])).toEqual({ changes: 1, errors: 1, canApply: false });
});

test("renameSummary does not count unchanged rows as changes or errors", () => {
  const rows: RenamePreviewRow[] = [
    { program: "a.sas", current: "job_a", proposed: "job_a", error: null },
    { program: "b.sas", current: "job_b", proposed: "job_b", error: null },
  ];
  expect(renameSummary(rows)).toEqual({ changes: 0, errors: 0, canApply: false });
});

test("BulkRename offers the four modes and starts with apply disabled", () => {
  const html = renderToStaticMarkup(<BulkRename id="project" onClose={() => {}} onDone={() => {}} />);
  expect(html).toContain("Prefijo");
  expect(html).toContain("Sufijo");
  expect(html).toContain("Buscar y reemplazar");
  expect(html).toContain("Expresión regular");
  expect(html).toMatch(/<button[^>]*disabled=""[^>]*>Aplicar/);
});

test("the rename preview keeps headers on one line and only breaks long paths and names", () => {
  const css = readFileSync(new URL("../../styles.css", import.meta.url), "utf8").replace(/\r\n/g, "\n");
  const rule = (selector: string) => {
    const start = css.indexOf(`${selector} {`);
    return start === -1 ? "" : css.slice(start, css.indexOf("}", start));
  };
  expect(rule(".bulk-rename-table th")).toContain("white-space: nowrap");
  expect(rule(".bulk-rename-table th")).toContain("overflow-wrap: normal");
  expect(rule(".bulk-rename-table td.mono")).toContain("overflow-wrap: anywhere");
  expect(rule(".bulk-rename-table")).toContain("table-layout: auto");
});
