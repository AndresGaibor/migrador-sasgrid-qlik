import { describe, expect, test } from "bun:test";
import { type CanvasEdge, type CanvasNode, layoutJob, NODE_HEIGHT, NODE_WIDTH } from "./canvas-layout";

const node = (id: string, subjob?: string): CanvasNode => ({ id, label: id.toUpperCase(), component: "tMap", subjob, status: "pending" });
const edge = (from: string, to: string, kind: CanvasEdge["kind"] = "row_main"): CanvasEdge => ({ from, to, kind });

type Rect = { x: number; y: number; w: number; h: number };
const overlaps = (a: Rect, b: Rect) => a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h;

describe("layoutJob: capas de izquierda a derecha", () => {
  test("a→b→c ocupa tres capas consecutivas y avanza hacia la derecha", () => {
    const layout = layoutJob([node("a"), node("b"), node("c")], [edge("a", "b"), edge("b", "c")]);
    const byId = Object.fromEntries(layout.nodes.map((n) => [n.id, n]));
    expect([byId.a.layer, byId.b.layer, byId.c.layer]).toEqual([0, 1, 2]);
    expect(byId.a.x).toBeLessThan(byId.b.x);
    expect(byId.b.x).toBeLessThan(byId.c.x);
  });

  test("una rama reconvergente pone los nodos del mismo nivel en la misma capa", () => {
    const layout = layoutJob(
      [node("s"), node("a"), node("b"), node("c")],
      [edge("s", "a"), edge("s", "b"), edge("a", "c"), edge("b", "c")],
    );
    const layers = Object.fromEntries(layout.nodes.map((n) => [n.id, n.layer]));
    expect(layers).toEqual({ s: 0, a: 1, b: 1, c: 2 });
  });

  test("toda arista de flujo acaba a la derecha de su origen", () => {
    const layout = layoutJob(
      [node("a"), node("b"), node("c"), node("d")],
      [edge("a", "c"), edge("b", "c"), edge("c", "d")],
    );
    const pos = Object.fromEntries(layout.nodes.map((n) => [n.id, n]));
    for (const e of layout.edges) expect(pos[e.to].x).toBeGreaterThan(pos[e.from].x);
  });

  test("la distribución vertical depende solo del orden de entrada: es determinista", () => {
    const nodes = [node("a"), node("b"), node("c"), node("d")];
    const edges = [edge("a", "b"), edge("a", "c"), edge("b", "d"), edge("c", "d")];
    expect(layoutJob(nodes, edges)).toEqual(layoutJob(nodes, edges));
  });
});

describe("layoutJob: solapes", () => {
  test("ningún par de nodos se solapa, ni siquiera con varias ramas", () => {
    const nodes = ["a", "b", "c", "d", "e", "f"].map((id) => node(id));
    const edges = [edge("a", "b"), edge("a", "c"), edge("a", "d"), edge("b", "e"), edge("c", "e"), edge("d", "f"), edge("e", "f")];
    const { nodes: placed } = layoutJob(nodes, edges);
    for (let i = 0; i < placed.length; i++) {
      for (let j = i + 1; j < placed.length; j++) {
        const a = { x: placed[i].x, y: placed[i].y, w: NODE_WIDTH, h: NODE_HEIGHT };
        const b = { x: placed[j].x, y: placed[j].y, w: NODE_WIDTH, h: NODE_HEIGHT };
        expect(overlaps(a, b)).toBe(false);
      }
    }
  });

  test("nodos de subjobs distintos no se solapan aunque compartan capa", () => {
    const nodes = [node("a1", "A"), node("a2", "A"), node("b1", "B"), node("b2", "B")];
    const layout = layoutJob(nodes, [edge("a1", "a2"), edge("b1", "b2")]);
    const rects = layout.nodes.map((n) => ({ x: n.x, y: n.y, w: NODE_WIDTH, h: NODE_HEIGHT }));
    for (let i = 0; i < rects.length; i++) for (let j = i + 1; j < rects.length; j++) expect(overlaps(rects[i], rects[j])).toBe(false);
  });
});

describe("layoutJob: subjobs", () => {
  test("cada subjob tiene su recuadro y los recuadros no se solapan", () => {
    const nodes = [node("a1", "A"), node("a2", "A"), node("b1", "B"), node("b2", "B")];
    const layout = layoutJob(nodes, [edge("a1", "a2"), edge("b1", "b2"), edge("a2", "b1")]);
    expect(layout.boxes.map((b) => b.name).sort()).toEqual(["A", "B"]);
    const [a, b] = ["A", "B"].map((name) => layout.boxes.find((x) => x.name === name)!);
    expect(overlaps({ x: a.x, y: a.y, w: a.width, h: a.height }, { x: b.x, y: b.y, w: b.width, h: b.height })).toBe(false);
  });

  test("cada nodo cae dentro del recuadro de su subjob y fuera del de los demás", () => {
    const nodes = [node("a1", "A"), node("a2", "A"), node("b1", "B")];
    const layout = layoutJob(nodes, [edge("a1", "a2"), edge("a2", "b1")]);
    const inside = (n: { x: number; y: number }, box: { x: number; y: number; width: number; height: number }) =>
      n.x >= box.x && n.x + NODE_WIDTH <= box.x + box.width && n.y >= box.y && n.y + NODE_HEIGHT <= box.y + box.height;
    const boxA = layout.boxes.find((b) => b.name === "A")!;
    const boxB = layout.boxes.find((b) => b.name === "B")!;
    for (const n of layout.nodes) {
      if (n.subjob === "A") {
        expect(inside(n, boxA)).toBe(true);
        expect(inside(n, boxB)).toBe(false);
      }
      if (n.subjob === "B") expect(inside(n, boxB)).toBe(true);
    }
  });

  test("nodos sin subjob no generan recuadro", () => {
    const layout = layoutJob([node("x"), node("y")], [edge("x", "y")]);
    expect(layout.boxes).toEqual([]);
  });

  test("el recuadro del subjob contiene su nodo con margen", () => {
    const layout = layoutJob([node("a", "Sub")], []);
    const box = layout.boxes[0];
    expect(box.name).toBe("Sub");
    expect(box.width).toBeGreaterThan(NODE_WIDTH);
    expect(box.height).toBeGreaterThan(NODE_HEIGHT);
  });
});

describe("layoutJob: conexiones", () => {
  test("las conexiones de datos se etiquetan rowN (Tipo) y son continuas", () => {
    const layout = layoutJob(
      [node("a"), node("b"), node("c")],
      [edge("a", "b", "row_main"), edge("a", "c", "row_lookup")],
    );
    expect(layout.edges.map((e) => e.label)).toEqual(["row1 (Main)", "row2 (Lookup)"]);
    expect(layout.edges.every((e) => e.isRow)).toBe(true);
  });

  test("los disparadores tienen etiqueta propia y no son de datos (punteada)", () => {
    const layout = layoutJob(
      [node("a"), node("b"), node("c")],
      [edge("a", "b", "on_subjob_ok"), edge("b", "c", "on_component_error")],
    );
    expect(layout.edges.map((e) => e.label)).toEqual(["On Subjob Ok", "On Component Error"]);
    expect(layout.edges.some((e) => e.isRow)).toBe(false);
  });

  test("las aristas salen del borde derecho y llegan al izquierdo", () => {
    const layout = layoutJob([node("a"), node("b")], [edge("a", "b")]);
    const [a, b] = layout.nodes;
    const e = layout.edges[0];
    expect(e.x1).toBe(a.x + NODE_WIDTH);
    expect(e.y1).toBe(a.y + NODE_HEIGHT / 2);
    expect(e.x2).toBe(b.x);
    expect(e.y2).toBe(b.y + NODE_HEIGHT / 2);
  });

  test("las aristas a nodos inexistentes o autobucles se ignoran", () => {
    const layout = layoutJob([node("a"), node("b")], [edge("a", "zz"), edge("a", "a"), edge("a", "b")]);
    expect(layout.edges.map((e) => [e.from, e.to])).toEqual([["a", "b"]]);
  });

  test("un ciclo no se queda en bucle: todos los nodos quedan colocados", () => {
    const layout = layoutJob([node("a"), node("b"), node("c")], [edge("a", "b"), edge("b", "a"), edge("b", "c")]);
    expect(layout.nodes).toHaveLength(3);
    for (const n of layout.nodes) {
      expect(Number.isFinite(n.x)).toBe(true);
      expect(Number.isFinite(n.y)).toBe(true);
    }
    const pos = Object.fromEntries(layout.nodes.map((n) => [n.id, n]));
    expect(pos.c.x).toBeGreaterThan(pos.b.x);
  });
});

describe("layoutJob: entradas degeneradas", () => {
  test("sin nodos devuelve un lienzo vacío con tamaño mínimo", () => {
    const layout = layoutJob([], []);
    expect(layout.nodes).toEqual([]);
    expect(layout.width).toBeGreaterThan(0);
    expect(layout.height).toBeGreaterThan(0);
  });

  test("ids repetidos: gana la primera aparición", () => {
    const layout = layoutJob([{ ...node("a"), label: "primero" }, { ...node("a"), label: "segundo" }], []);
    expect(layout.nodes).toHaveLength(1);
    expect(layout.nodes[0].label).toBe("primero");
  });

  test("conserva estado y componente de cada nodo", () => {
    const layout = layoutJob([{ ...node("a"), status: "blocked", component: "tDBOutput" }], []);
    expect(layout.nodes[0]).toMatchObject({ status: "blocked", component: "tDBOutput" });
  });

  test("el lienzo incluye todos los nodos y recuadros", () => {
    const layout = layoutJob([node("a", "S"), node("b", "S")], [edge("a", "b")]);
    for (const n of layout.nodes) {
      expect(n.x + NODE_WIDTH).toBeLessThanOrEqual(layout.width);
      expect(n.y + NODE_HEIGHT).toBeLessThanOrEqual(layout.height);
    }
    for (const b of layout.boxes) expect(b.y + b.height).toBeLessThanOrEqual(layout.height);
  });
});
