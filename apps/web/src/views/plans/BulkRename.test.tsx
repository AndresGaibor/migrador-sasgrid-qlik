import { expect, test } from "bun:test";
import { renameSummary } from "./BulkRename";
import type { RenamePreviewRow } from "../../types";

test("only enables apply for valid proposed changes", () => {
  expect(renameSummary([])).toEqual({ changes: 0, errors: 0, canApply: false });
  expect(renameSummary([
    { program: "a.sas", current: "job_a", proposed: "fin_a", error: null },
    { program: "b.sas", current: "job_b", proposed: "fin_b", error: null },
  ])).toEqual({ changes: 2, errors: 0, canApply: true });
  expect(renameSummary([
    { program: "a.sas", current: "job_a", proposed: "job_a", error: null },
    { program: "b.sas", current: "job_b", proposed: "bad-name", error: "Nombre no válido" },
  ] as RenamePreviewRow[])).toEqual({ changes: 1, errors: 1, canApply: false });
});
