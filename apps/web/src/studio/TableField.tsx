import type { Param } from "./panel-types";

type Props = {
  param: Param;
  id: string;
  /** Filas sugeridas: clave = nombre de columna del snapshot. */
  rows: Record<string, string>[];
};

// Rejilla de solo lectura con las columnas de Studio. Las celdas sin sugerencia muestran el default de la columna.
export function TableField({ param, id, rows }: Props) {
  const columns = param.table?.columns ?? [];
  if (columns.length === 0) return <p className="studio-static">Tabla sin columnas en el snapshot.</p>;
  return (
    <div className="studio-table-wrap" id={id}>
      <table className="studio-table">
        <caption className="studio-sr-only">{param.label || param.name}</caption>
        <thead>
          <tr>{columns.map((c) => <th key={c.name} scope="col">{c.label || c.name}</th>)}</tr>
        </thead>
        <tbody>
          {rows.length === 0 ? (
            <tr><td colSpan={columns.length} className="studio-muted">Sin filas sugeridas: deja la tabla como la deja Studio.</td></tr>
          ) : rows.map((row, index) => (
            <tr key={index}>
              {columns.map((c) => <td key={c.name}>{row[c.name] ?? c.defaultValue ?? ""}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
