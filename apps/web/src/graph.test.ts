import { expect, test } from "bun:test";
import { layout } from "./graph";

test("layout agrupa por capa y descarta aristas fuera del grafo", () => {
  const g = layout(
    [["a.sas"], ["b.sas", "c.sas"]],
    [
      { source: "a.sas", target: "b.sas", datasets: ["x"], kind: "data" },
      { source: "a.sas", target: "zz.sas", datasets: ["y"], kind: "data" },
      { source: "a.sas", target: "c.sas", datasets: [], kind: "include" },
    ],
  );
  expect(g.nodes).toHaveLength(3);
  expect(g.links).toHaveLength(1);
  expect(g.links[0].label).toBe("x");
  expect(g.nodes.find((n) => n.id === "c.sas")!.x).toBe(g.nodes.find((n) => n.id === "b.sas")!.x);
});

test("layout vacío", () => {
  expect(layout([], []).nodes).toEqual([]);
});
