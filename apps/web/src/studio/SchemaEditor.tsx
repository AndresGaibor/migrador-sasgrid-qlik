import { useState, type ReactNode } from "react";
import { copyText } from "./clipboard";
import type { SchemaColumn } from "./panel-types";
import { differsFromSas, sasOriginText, schemaShape, schemaToTsv, talendFamily } from "./schema-model";

type Props = {
  columns: SchemaColumn[];
  /** Por defecto true: tabla solo de lectura para copiarla a Studio. */
  readOnly?: boolean;
  /** Solo con readOnly=false: recibe la tabla completa tras cada cambio. */
  onChange?: (columns: SchemaColumn[]) => void;
};

const TEXT_FIELDS = ["name", "type", "length", "precision", "default", "comment", "pattern"] as const;
type TextField = (typeof TEXT_FIELDS)[number];

function patchFor(field: TextField, value: string): Partial<SchemaColumn> {
  if (field === "name") return { name: value };
  if (field === "length" || field === "precision") {
    const n = Number(value);
    return { [field]: value.trim() === "" || !Number.isFinite(n) ? null : n };
  }
  return { [field]: value === "" ? null : value } as Partial<SchemaColumn>;
}

// Réplica de la tabla «Edit schema» de Studio. Solo lectura por defecto, con botón para copiar TSV.
export function SchemaEditor({ columns, readOnly = true, onChange }: Props) {
  const shape = schemaShape(columns);
  const [copyState, setCopyState] = useState<"idle" | "ok" | "error">("idle");
  const editable = !readOnly && onChange !== undefined;

  const update = (index: number, patch: Partial<SchemaColumn>) => {
    if (!onChange) return;
    onChange(columns.map((c, i) => (i === index ? { ...c, ...patch } : c)));
  };

  const onCopy = async () => setCopyState((await copyText(schemaToTsv(columns))) ? "ok" : "error");

  const text = (index: number, field: TextField, value: string | number | null | undefined, label: string): ReactNode => {
    if (!editable) return value ?? "";
    return (
      <input
        className="studio-cell-input"
        aria-label={`${label} de la columna ${columns[index].name}`}
        value={value ?? ""}
        onChange={(e) => update(index, patchFor(field, e.target.value))}
      />
    );
  };

  return (
    <div className="studio-panel studio-schema">
      <div className="studio-schema-toolbar">
        <button type="button" className="studio-button" onClick={() => void onCopy()}>Copiar tabla (TSV)</button>
        {copyState !== "idle" && (
          <span role="status" className="studio-copy-status">
            {copyState === "ok" ? "Tabla copiada. Pégala en Edit schema de Studio." : "No se pudo copiar la tabla."}
          </span>
        )}
      </div>
      <div className="studio-table-wrap">
        <table className="studio-table studio-schema-table">
          <caption className="studio-sr-only">Esquema de columnas</caption>
          <thead>
            <tr>
              <th scope="col">Column</th>
              <th scope="col">Key</th>
              <th scope="col">Type</th>
              <th scope="col">Nullable</th>
              <th scope="col">Length</th>
              <th scope="col">Precision</th>
              <th scope="col">Default</th>
              <th scope="col">Comment</th>
              {shape.hasDatePattern && <th scope="col">Date Pattern</th>}
              {shape.hasSasOrigin && <th scope="col">SAS origen</th>}
            </tr>
          </thead>
          <tbody>
            {columns.length === 0 && (
              <tr><td colSpan={8 + (shape.hasDatePattern ? 1 : 0) + (shape.hasSasOrigin ? 1 : 0)} className="studio-muted">Sin columnas sugeridas.</td></tr>
            )}
            {columns.map((c, i) => (
              <tr key={`${c.name}-${i}`}>
                <td>{text(i, "name", c.name, "Nombre")}</td>
                <td>
                  {editable ? (
                    <input type="checkbox" aria-label={`Clave de la columna ${c.name}`} checked={c.key === true} onChange={(e) => update(i, { key: e.target.checked })} />
                  ) : (c.key ? "Sí" : "No")}
                </td>
                <td>
                  {text(i, "type", c.type, "Tipo")}
                  {differsFromSas(c) && (
                    <span className="studio-mismatch" role="img" aria-label="El tipo Talend no coincide con el tipo SAS de origen" title={`Tipo SAS: ${sasOriginText(c)} · tipo Talend: ${c.type} (${talendFamily(c.type)})`}> ≠</span>
                  )}
                </td>
                <td>
                  {editable ? (
                    <input type="checkbox" aria-label={`Nullable de la columna ${c.name}`} checked={c.nullable === true} onChange={(e) => update(i, { nullable: e.target.checked })} />
                  ) : (c.nullable ? "Sí" : "No")}
                </td>
                <td>{text(i, "length", c.length, "Longitud")}</td>
                <td>{text(i, "precision", c.precision, "Precisión")}</td>
                <td>{text(i, "default", c.default, "Valor por defecto")}</td>
                <td>{text(i, "comment", c.comment, "Comentario")}</td>
                {shape.hasDatePattern && <td>{text(i, "pattern", c.pattern, "Date Pattern")}</td>}
                {shape.hasSasOrigin && <td>{sasOriginText(c)}</td>}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
