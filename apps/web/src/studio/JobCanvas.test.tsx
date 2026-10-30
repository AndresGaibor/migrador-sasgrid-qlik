import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import type { CanvasEdge, CanvasNode } from "./canvas-layout";
import { JobCanvas } from "./JobCanvas";

const nodes: CanvasNode[] = [
  { id: "read", label: "Leer clientes", component: "tFileInputDelimited", subjob: "Paso 1", status: "done" },
  { id: "map", label: "Transformar", component: "tMap", subjob: "Paso 1", status: "in_progress" },
  { id: "write", label: "Escribir resultado", component: "tFileOutputDelimited", status: "blocked" },
];
const edges: CanvasEdge[] = [
  { from: "read", to: "map", kind: "row_main" },
  { from: "map", to: "write", kind: "row_main" },
  { from: "read", to: "write", kind: "on_subjob_ok" },
];

describe("JobCanvas", () => {
  test("pinta un nodo por componente con su estado y el nombre del componente como texto de respaldo", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={nodes} edges={edges} />);
    expect(html).toContain('aria-label="Leer clientes, tFileInputDelimited, Hecho"');
    expect(html).toContain('aria-label="Transformar, tMap, En progreso"');
    expect(html).toContain('aria-label="Escribir resultado, tFileOutputDelimited, Bloqueado"');
    expect(html).toContain(">tFileInputDelimited</text>");
    expect(html).toContain("status-blocked");
  });

  test("las conexiones de datos llevan etiqueta de fila y los disparadores van como trigger", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={nodes} edges={edges} />);
    expect(html).toContain("row1 (Main)");
    expect(html).toContain("On Subjob Ok");
    expect(html).toContain("is-trigger");
    expect(html).toContain("studio-edge-ok");
  });

  test("dibuja el recuadro del subjob con su título", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={nodes} edges={edges} />);
    expect(html).toContain('class="studio-subjob-title"');
    expect(html).toContain(">Paso 1</text>");
  });

  test("el nodo seleccionado queda resaltado y con aria-pressed", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={nodes} edges={edges} selectedId="map" />);
    expect(html).toMatch(/is-selected[^"]*"[^>]*transform="translate\([^)]*\)" role="button"[^>]*aria-pressed="true"/);
    expect(html.match(/is-selected/g)).toHaveLength(1);
  });

  test("ofrece zoom y lienzo desplazable con foco de teclado", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={nodes} edges={edges} />);
    expect(html).toContain('aria-label="Acercar"');
    expect(html).toContain('aria-label="Alejar"');
    expect(html).toContain('role="region"');
    expect(html).toContain('tabindex="0"');
  });

  test("sin nodos muestra un mensaje y no dibuja lienzo", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={[]} edges={[]} />);
    expect(html).toContain("El Job no tiene componentes");
    expect(html).not.toContain("<svg");
  });

  test("las aristas a nodos inexistentes no rompen el render", () => {
    const html = renderToStaticMarkup(<JobCanvas nodes={nodes} edges={[{ from: "x", to: "y", kind: "row_main" }]} />);
    expect(html).toContain("<svg");
    expect(html).not.toContain("row1 (Main)");
  });
});
