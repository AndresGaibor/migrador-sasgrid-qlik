import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ComponentPanel, type ComponentPanelProps } from "./ComponentPanel";
import { dbGuide, fileInputGuide, panelsFixture } from "./__fixtures__/panels.fixture";

const render = (overrides: Partial<ComponentPanelProps> = {}) =>
  renderToStaticMarkup(
    <ComponentPanel
      component="tFileInputDelimited"
      stepLabel="Paso 3 · Leer clientes"
      panels={panelsFixture}
      values={fileInputGuide}
      doneFields={{}}
      onFieldDone={() => {}}
      {...overrides}
    />,
  );

// Segmento de HTML de la fila que contiene el campo indicado.
function rowOf(html: string, field: string): string {
  const at = html.indexOf(`data-field="${field}"`);
  const start = html.lastIndexOf('class="studio-row"', at);
  const end = html.indexOf('class="studio-row"', start + 1);
  return html.slice(start, end === -1 ? undefined : end);
}

describe("ComponentPanel: cabecera y pestañas", () => {
  test("muestra el componente, su label y el label del paso", () => {
    const html = render();
    expect(html).toContain("tFileInputDelimited");
    expect(html).toContain("Delimited file input");
    expect(html).toContain("Paso 3 · Leer clientes");
  });

  test("expone las cinco pestañas con roles de tablist y tab", () => {
    const html = render();
    expect(html).toContain('role="tablist"');
    expect(html.match(/role="tab"/g)).toHaveLength(5);
    for (const label of ["Basic settings", "Advanced settings", "Dynamic settings", "View", "Documentation"]) expect(html).toContain(label);
  });

  test("la pestaña activa está seleccionada y las demás no", () => {
    const html = render();
    expect(html.match(/aria-selected="true"/g)).toHaveLength(1);
    expect(html).toMatch(/id="[^"]+-tab-basic"[^>]*aria-selected="true"/);
  });

  test("el panel de contenido está asociado a la pestaña activa", () => {
    const html = render();
    expect(html).toMatch(/role="tabpanel" id="([^"]+)-panel" aria-labelledby="\1-tab-basic"/);
  });

  test("las pestañas inactivas quedan fuera del orden de tabulación", () => {
    const html = render();
    expect(html.match(/tabindex="-1"/g)).toHaveLength(4);
  });

  test("componente que no está en el snapshot muestra un aviso", () => {
    const html = render({ component: "tNoExiste" });
    expect(html).toContain('role="alert"');
    expect(html).toContain("tNoExiste");
  });

  test("dynamic, view y documentation muestran un mensaje en español y no campos", () => {
    for (const tab of ["dynamic", "view", "documentation"] as const) {
      const html = render({ initialTab: tab });
      expect(html).not.toContain("data-field=");
      expect(html).toContain('class="studio-message"');
    }
    expect(render({ initialTab: "dynamic" })).toContain("Los ajustes dinámicos");
    expect(render({ initialTab: "view" })).toContain("Label format");
  });
});

describe("ComponentPanel: campos de la pestaña básica", () => {
  test("muestra las etiquetas de Talend tal cual y marca los obligatorios", () => {
    const html = render();
    expect(html).toContain("File name/Stream");
    expect(html).toContain("Row separator");
    expect(html).toContain("required");
  });

  test("el valor sugerido aparece como «Set to:» con botón copiar y casilla de hecho", () => {
    const html = render();
    expect(html).toContain("Set to:");
    expect(html).toContain("clientes.csv");
    expect(html).toContain('aria-label="Copiar valor de FILENAME"');
    expect(html).toContain('aria-label="Marcar FILENAME como hecho"');
  });

  test("el porqué de la sugerencia va en un desplegable", () => {
    const html = render();
    expect(html).toContain("¿Por qué?");
    expect(html).toContain("El SAS lee la librería CLIENTES.");
  });

  test("los campos sin sugerencia no muestran chip", () => {
    const html = render({ values: { FILENAME: { value: "x" } } });
    expect(html.match(/class="studio-suggestion/g)).toHaveLength(1);
  });

  test("los campos ocultos por SHOW_IF no se renderizan", () => {
    const html = render({ component: "tDBInput", values: { USE_EXISTING_CONNECTION: { value: "true" } } });
    expect(html).not.toContain('data-field="HOST"');
    expect(html).toContain('data-field="DB_TYPE"');
  });

  test("dos campos con el mismo numRow van en la misma fila horizontal", () => {
    const html = render();
    expect(rowOf(html, "ROWSEPARATOR")).toContain('data-field="FIELDSEPARATOR"');
    expect(rowOf(html, "HEADER")).not.toContain('data-field="FIELDSEPARATOR"');
  });

  test("el campo activo (primer pendiente) queda resaltado", () => {
    const html = render();
    expect(html).toContain('studio-field is-active" data-field="SCHEMA_TYPE"');
  });

  test("muestra el progreso de la pestaña", () => {
    const html = render();
    expect(html).toContain("0 de 4 campos");
    expect(html).toContain('role="progressbar"');
  });

  test("el progreso refleja los campos marcados como hechos", () => {
    const html = render({ doneFields: { FILENAME: true, HEADER: true } });
    expect(html).toContain("2 de 4 campos");
    expect(rowOf(html, "FILENAME")).toContain('checked=""');
    expect(rowOf(html, "ROWSEPARATOR")).not.toContain('checked=""');
  });

  test("un widget FILE muestra el botón de examinar deshabilitado", () => {
    const html = render();
    expect(html).toMatch(/<button[^>]*disabled=""[^>]*aria-label="Examinar: File name\/Stream \(en Studio\)"/);
  });

  test("un widget SCHEMA_TYPE muestra el botón de editar esquema", () => {
    const html = render({ values: {} });
    expect(html).toContain('aria-label="Editar esquema: Edit schema"');
  });

  test("un campo CHECK refleja el valor booleano", () => {
    const html = render({ values: { REMOVE_EMPTY_ROW: { value: "true" } } });
    expect(rowOf(html, "REMOVE_EMPTY_ROW")).toMatch(/studio-check" aria-readonly="true" checked=""/);
  });
});

describe("ComponentPanel: otros widgets y pestaña avanzada", () => {
  test("PASSWORD usa input de contraseña y avisa de la variable de contexto", () => {
    const html = render({ component: "tDBInput", values: dbGuide });
    expect(html).toContain('type="password"');
    expect(html).toContain("context.DB_PASSWORD");
    expect(html).toContain("no la contraseña en claro");
  });

  test("CLOSED_LIST muestra un select con las opciones", () => {
    const html = render({ component: "tDBInput", values: dbGuide });
    expect(html).toContain("<select");
    expect(html).toContain(">PostgreSQL</option>");
    expect(html).toContain(">MS SQL Server</option>");
  });

  test("MEMO_JAVA se muestra como textarea de solo lectura con la consulta", () => {
    const html = render({ component: "tDBInput", values: dbGuide });
    expect(html).toContain("<textarea");
    expect(html).toContain("SELECT id, nombre FROM clientes WHERE activo = 1");
  });

  test("LABEL se muestra como texto estático cuando su condición se cumple", () => {
    // EXISTING_CONN_NOTE solo aparece con conexión existente (NOT_SHOW_IF USE == false).
    const html = render({ component: "tDBInput", values: { USE_EXISTING_CONNECTION: { value: "true" } } });
    expect(html).toContain("Conexión existente");
  });

  test("PROPERTY_TYPE muestra Built-In como selector", () => {
    const html = render();
    expect(html).toContain(">Built-In</option>");
    expect(html).toContain(">Repository</option>");
  });

  test("la pestaña avanzada muestra el ENCODING_TYPE con la opción sugerida", () => {
    const html = render({ initialTab: "advanced", values: fileInputGuide });
    expect(html).toContain("Advanced settings");
    expect(rowOf(html, "ENCODING")).toContain('<option value="&quot;UTF-8&quot;" selected="">UTF-8</option>');
  });

  test("la pestaña avanzada muestra la tabla de TABLE con columnas y filas sugeridas", () => {
    const html = render({ initialTab: "advanced", values: fileInputGuide });
    expect(html).toContain('<table class="studio-table"');
    expect(html).toContain('<th scope="col">Trim</th>');
    expect(html).toContain("<td>NOMBRE</td>");
    expect(html).toContain("1 fila");
  });

  test("la tabla sin filas sugeridas indica que queda como la deja Studio", () => {
    const html = render({ initialTab: "advanced", values: {} });
    expect(html).toContain("Sin filas sugeridas");
  });

  test("CHECK de la pestaña avanzada sin sugerencia no aparece marcado", () => {
    const html = render({ initialTab: "advanced", values: {} });
    expect(rowOf(html, "CSV_OPTION")).not.toContain('checked=""');
  });

  test("sin sugerencias el progreso dice que no hay campos con sugerencia", () => {
    const html = render({ values: {} });
    expect(html).toContain("Sin campos con sugerencia en esta pestaña");
  });
});
