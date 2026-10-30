import { describe, expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { SchemaEditor } from "./SchemaEditor";
import type { SchemaColumn } from "./panel-types";

const columns: SchemaColumn[] = [
  { name: "ID", type: "Integer", key: true, nullable: false, length: 10, sasType: "num", sasFormat: "BEST12." },
  { name: "NOMBRE", type: "String", nullable: true, length: 60, comment: "Nombre del cliente", sasType: "char", sasFormat: "$60." },
  { name: "FECHA", type: "Date", pattern: "yyyy-MM-dd", sasType: "num", sasFormat: "DATE9." },
];

describe("SchemaEditor", () => {
  test("muestra las columnas de Studio en el orden de la tabla Edit schema", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={columns} />);
    const heads = [...html.matchAll(/<th scope="col">([^<]+)<\/th>/g)].map((m) => m[1]);
    expect(heads).toEqual(["Column", "Key", "Type", "Nullable", "Length", "Precision", "Default", "Comment", "Date Pattern", "SAS origen"]);
  });

  test("muestra Date Pattern solo si hay una columna Date", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={[{ name: "A", type: "String" }]} />);
    expect(html).not.toContain("Date Pattern");
    expect(html).not.toContain("SAS origen");
  });

  test("la columna SAS origen muestra el tipo y el formato de origen", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={columns} />);
    expect(html).toContain("num BEST12.");
    expect(html).toContain("char $60.");
  });

  test("marca el tipo Talend que no coincide con el tipo SAS de origen", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={[{ name: "X", type: "Integer", sasType: "char" }]} />);
    expect(html).toContain("El tipo Talend no coincide con el tipo SAS de origen");
  });

  test("no marca las columnas cuyo tipo coincide", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={[{ name: "X", type: "String", sasType: "char" }]} />);
    expect(html).not.toContain("studio-mismatch");
  });

  test("es de solo lectura por defecto y ofrece copiar la tabla", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={columns} />);
    expect(html).toContain("Copiar tabla (TSV)");
    expect(html).not.toContain("studio-cell-input");
    expect(html).toContain("Sí");
  });

  test("con readOnly=false muestra campos editables", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={columns} readOnly={false} onChange={() => {}} />);
    expect(html).toContain('aria-label="Tipo de la columna ID"');
    expect(html).toContain("studio-cell-input");
    expect(html).toContain('aria-label="Clave de la columna ID"');
  });

  test("sin columnas indica que no hay columnas sugeridas", () => {
    const html = renderToStaticMarkup(<SchemaEditor columns={[]} />);
    expect(html).toContain("Sin columnas sugeridas");
  });
});
