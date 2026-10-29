import { useState } from "react";
import { Dialog } from "../../components/Dialog";
import { api } from "../../api";
import { formatErrorMessage } from "../../errors";
import type { BulkRenameRule, RenamePreviewRow } from "../../types";

export function renameSummary(rows: RenamePreviewRow[]) {
  const changes = rows.filter((row) => row.current !== row.proposed).length;
  const errors = rows.filter((row) => Boolean(row.error)).length;
  return { changes, errors, canApply: changes > 0 && errors === 0 };
}

export function BulkRename({ id, onClose, onDone, batchActive }: { id: string; onClose: () => void; onDone: () => void; batchActive: boolean }) {
  const [mode, setMode] = useState<BulkRenameRule["mode"]>("prefix");
  const [text, setText] = useState("");
  const [find, setFind] = useState("");
  const [replaceWith, setReplaceWith] = useState("");
  const [rows, setRows] = useState<RenamePreviewRow[]>();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string>();
  const summary = renameSummary(rows ?? []);

  const rule = (): BulkRenameRule => ({ mode, text, find, replace_with: replaceWith });

  const preview = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setBusy(true);
    setError(undefined);
    try {
      setRows(await api.renamePreview(id, rule()));
    } catch (reason) {
      setError(formatErrorMessage(reason));
    } finally {
      setBusy(false);
    }
  };

  const apply = async () => {
    if (!summary.canApply || batchActive || busy) return;
    setBusy(true);
    setError(undefined);
    try {
      const changes = rows!.filter((row) => row.current !== row.proposed).map((row) => ({ program: row.program, job_name: row.proposed }));
      await api.renameJobs(id, changes);
      onDone();
      onClose();
    } catch (reason) {
      setError(formatErrorMessage(reason));
    } finally {
      setBusy(false);
    }
  };

  return <Dialog title="Renombrar Jobs" onClose={onClose}>
    <p className="muted">Previsualiza todos los nombres antes de guardarlos. Los nombres editados a mano pueden cambiarse aquí.</p>
    <form className="bulk-rename-form" onSubmit={(event) => void preview(event)}>
      <label>Modo<select value={mode} onChange={(event) => { setMode(event.target.value as BulkRenameRule["mode"]); setRows(undefined); }}>
        <option value="prefix">Prefijo</option>
        <option value="suffix">Sufijo</option>
        <option value="replace">Buscar y reemplazar</option>
        <option value="regex">Expresión regular</option>
      </select></label>
      {(mode === "prefix" || mode === "suffix") && <label>{mode === "prefix" ? "Prefijo" : "Sufijo"}<input value={text} onChange={(event) => { setText(event.target.value); setRows(undefined); }} maxLength={60} /></label>}
      {(mode === "replace" || mode === "regex") && <>
        <label>{mode === "regex" ? "Patrón" : "Texto que buscarás"}<input value={find} onChange={(event) => { setFind(event.target.value); setRows(undefined); }} maxLength={200} /></label>
        <label>Reemplazar por<input value={replaceWith} onChange={(event) => { setReplaceWith(event.target.value); setRows(undefined); }} maxLength={60} /></label>
      </>}
      <div className="dialog-actions"><button type="submit" className="secondary" disabled={busy || batchActive}>{busy ? "Calculando…" : "Ver cambios"}</button></div>
    </form>
    {error && <p className="error" role="alert">{error}</p>}
    {rows && <>
      <div className="bulk-rename-table-wrap"><table className="bulk-rename-table"><thead><tr><th>Programa</th><th>Antes</th><th>Después</th><th>Error</th></tr></thead><tbody>{rows.map((row) => <tr key={row.program}><td><code>{row.program}</code></td><td><code>{row.current}</code></td><td><code>{row.proposed}</code></td><td>{row.error ?? ""}</td></tr>)}</tbody></table></div>
      <p role="status">{summary.changes} cambios · {summary.errors} errores</p>
      <div className="dialog-actions"><button type="button" onClick={() => void apply()} disabled={!summary.canApply || busy || batchActive}>{busy ? "Aplicando…" : `Aplicar ${summary.changes} cambios`}</button></div>
    </>}
    {batchActive && <p className="muted" role="status">No se pueden cambiar nombres mientras se crean Jobs en Talend Studio.</p>}
  </Dialog>;
}
