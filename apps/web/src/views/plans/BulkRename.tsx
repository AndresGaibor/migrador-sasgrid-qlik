import { useEffect, useState } from "react";
import { api } from "../../api";
import { formatErrorMessage, notifyError } from "../../errors";
import type { BulkRenameRule, RenamePreviewRow } from "../../types";

type Mode = BulkRenameRule["mode"];

const MODES: { value: Mode; label: string }[] = [
  { value: "prefix", label: "Prefijo" },
  { value: "suffix", label: "Sufijo" },
  { value: "replace", label: "Buscar y reemplazar" },
  { value: "regex", label: "Expresión regular" },
];

export function renameSummary(rows: RenamePreviewRow[]): { changes: number; errors: number; canApply: boolean } {
  const changes = rows.filter((row) => row.proposed !== row.current).length;
  const errors = rows.filter((row) => row.error !== null).length;
  return { changes, errors, canApply: changes > 0 && errors === 0 };
}

// El diálogo no se cierra mientras hay una llamada en vuelo: el resultado debe poder mostrarse.
export function shouldCloseBulkRename(busy: boolean): boolean {
  return !busy;
}

export function BulkRename({ id, onClose, onDone, onBusyChange }: { id: string; onClose: () => void; onDone: (warnings: string[]) => void; onBusyChange?: (busy: boolean) => void }) {
  const [mode, setMode] = useState<Mode>("prefix");
  const [text, setText] = useState("");
  const [find, setFind] = useState("");
  const [replaceWith, setReplaceWith] = useState("");
  const [rows, setRows] = useState<RenamePreviewRow[]>();
  const [previewing, setPreviewing] = useState(false);
  const [applying, setApplying] = useState(false);
  const [error, setError] = useState<string>();
  const summary = rows ? renameSummary(rows) : undefined;
  const usesText = mode === "prefix" || mode === "suffix";
  const required = usesText ? text : find;
  const busy = previewing || applying;

  useEffect(() => {
    onBusyChange?.(busy);
  }, [busy]);

  // Cualquier cambio en los campos invalida la vista previa: solo se aplica lo que se ha visto.
  const changeField = (update: () => void) => {
    update();
    setRows(undefined);
    setError(undefined);
  };

  const buildRule = (): BulkRenameRule =>
    usesText ? { mode, text } : { mode, find, replace_with: replaceWith };

  const preview = async () => {
    setPreviewing(true);
    setError(undefined);
    try {
      setRows(await api.renamePreview(id, buildRule()));
    } catch (x) {
      setRows(undefined);
      setError(formatErrorMessage(x, "No se pudo calcular la vista previa"));
    } finally {
      setPreviewing(false);
    }
  };

  const apply = async () => {
    if (!rows || !summary?.canApply) return;
    setApplying(true);
    setError(undefined);
    try {
      const renames = rows.filter((row) => row.proposed !== row.current).map((row) => ({ program: row.program, job_name: row.proposed }));
      const result = await api.renameJobs(id, renames);
      onDone(result.warnings);
    } catch (x) {
      // Error inline (role="alert") y toast, como el resto de acciones de la vista.
      setError(notifyError(x, "No se pudieron renombrar los Jobs"));
    } finally {
      setApplying(false);
    }
  };

  return (
    <div className="bulk-rename">
      <label>
        Modo
        <select value={mode} disabled={busy} onChange={(e) => changeField(() => setMode(e.target.value as Mode))}>
          {MODES.map((option) => <option key={option.value} value={option.value}>{option.label}</option>)}
        </select>
      </label>
      {usesText ? (
        <label>
          {mode === "prefix" ? "Texto a añadir al inicio" : "Texto a añadir al final"}
          <input value={text} disabled={busy} onChange={(e) => changeField(() => setText(e.target.value))} />
        </label>
      ) : (
        <div className="bulk-rename-fields">
          <label>
            {mode === "regex" ? "Patrón (expresión regular)" : "Texto a buscar"}
            <input value={find} disabled={busy} onChange={(e) => changeField(() => setFind(e.target.value))} />
          </label>
          <label>
            {mode === "regex" ? "Reemplazo" : "Reemplazar por"}
            <input value={replaceWith} disabled={busy} onChange={(e) => changeField(() => setReplaceWith(e.target.value))} />
          </label>
        </div>
      )}
      <div className="dialog-actions">
        <button type="button" className="secondary" disabled={busy || !required} onClick={() => void preview()}>{previewing ? "Calculando…" : "Ver cambios"}</button>
      </div>
      {error && <div className="notice error-notice" role="alert"><span>{error}</span></div>}
      {rows && summary && (
        <>
          <p className="muted">{summary.changes} cambios{summary.errors > 0 ? `, ${summary.errors} con error` : ""}.</p>
          <div className="table-wrap">
            <table className="bulk-rename-table" aria-label="Vista previa del renombrado de Jobs">
              <thead><tr><th>Programa</th><th>Antes</th><th>Después</th><th>Error</th></tr></thead>
              <tbody>
                {rows.map((row) => (
                  <tr key={row.program}>
                    <td>{row.program}</td>
                    <td className="mono">{row.current}</td>
                    <td className="mono">{row.proposed}</td>
                    <td>{row.error ?? ""}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
      <div className="dialog-actions">
        <button type="button" className="secondary" disabled={busy} onClick={onClose}>Cancelar</button>
        <button type="button" disabled={busy || !summary?.canApply} onClick={() => void apply()}>{applying ? "Aplicando…" : rows ? `Aplicar ${summary?.changes} cambios` : "Aplicar"}</button>
      </div>
    </div>
  );
}
