import { expect, test } from "bun:test";
import { nextActionHref, pendingPanelState, pendingTotals, stageTone } from "./project-progress";
import type { PendingGroup } from "./types";

test("stage status maps to a tone", () => {
  expect(stageTone("done")).toBe("ok");
  expect(stageTone("current")).toBe("warn");
  expect(stageTone("blocked")).toBe("bad");
  expect(stageTone("todo")).toBe("neutral");
});

test("next action links to the suggested tab, or nothing when there is no next step", () => {
  expect(nextActionHref("p", { key: "k", label: "l", tab: "planes", reason: "r" })).toBe("#/p/p/planes");
  expect(nextActionHref("p", null)).toBeNull();
});

test("pending totals count distinct jobs and steps across groups", () => {
  const groups: PendingGroup[] = [
    {
      reason: "a",
      steps: 2,
      programs: [{ program: "dir/a.sas", job_name: "job_a", step_ids: ["s1", "s2"] }],
    },
    {
      reason: "b",
      steps: 2,
      programs: [
        { program: "dir/a.sas", job_name: "job_a", step_ids: ["s2", "s3"] },
        { program: "dir/b.sas", job_name: "job_b", step_ids: ["s1"] },
      ],
    },
  ];
  expect(pendingTotals(groups)).toEqual({ steps: 4, jobs: 2 });
  expect(pendingTotals([])).toEqual({ steps: 0, jobs: 0 });
});

test("pending panel is hidden until guides are done", () => {
  expect(pendingPanelState(false, { data: [] })).toBe("hidden");
  expect(pendingPanelState(false, { loading: false })).toBe("hidden");
});

test("pending panel is loading while the request is in flight, never an empty all-clear", () => {
  expect(pendingPanelState(true, { loading: true })).toBe("loading");
  expect(pendingPanelState(true, { loading: true, data: [] })).toBe("loading");
  expect(pendingPanelState(true, {})).toBe("loading");
});

test("pending panel is ready once the list is fetched or the request failed", () => {
  expect(pendingPanelState(true, { loading: false, data: [] })).toBe("ready");
  expect(pendingPanelState(true, { loading: false, error: "boom" })).toBe("ready");
});
