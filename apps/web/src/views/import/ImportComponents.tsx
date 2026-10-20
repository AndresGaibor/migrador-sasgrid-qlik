import { useState } from "react";
import { Dialog } from "../../components/Dialog";
import { Icon } from "../../components/Icon";
import { Badge } from "../common";

export type ImportSource = File | string;

export function SasFileUpload({ busy, error, onSelect }: { busy: boolean; error?: string; onSelect: (file: File) => void }) {
  return <section className="panel">
    <div className="panel-heading"><Icon name="upload" size={24} /><div><h2>Selecciona un ZIP o un programa SAS</h2><p>Un ZIP permite cargar varios programas de una vez.</p></div><Badge tone="ok">Recomendado</Badge></div>
    <div className="upload-zone" aria-busy={busy}>
      <Icon name="upload" size={38} /><h3>{busy ? "Procesando la carga…" : "Tus programas, en un solo archivo"}</h3>
      <p>Elige un ZIP con varios programas o un archivo .sas individual.</p>
      <label><span className="sr-only">Archivo ZIP o programa SAS</span><input type="file" accept=".zip,.sas,application/zip" disabled={busy} onChange={(e) => { const file = e.target.files?.[0]; if (file) onSelect(file); e.target.value = ""; }} /></label>
      <small>Se incluirán los archivos compatibles con el análisis.</small>
      {busy && <div role="status" className="loading-state"><span className="spinner" /> Comprobando el proyecto y preparando tus archivos…</div>}
    </div>
    {error && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{error}</span></div>}
  </section>;
}

export function ServerPathImport({ busy, onImport }: { busy: boolean; onImport: (path: string) => void }) {
  const [path, setPath] = useState("");
  return <details><summary>Opciones avanzadas: importar desde una carpeta del servidor</summary><p className="muted">Usa esta opción si los archivos ya están en el equipo donde funciona el servicio. La carpeta debe estar dentro de las rutas permitidas.</p><form onSubmit={(e) => { e.preventDefault(); if (path.trim()) onImport(path.trim()); }} className="row"><label className="grow">Ruta de la carpeta o del ZIP<input value={path} onChange={(e) => setPath(e.target.value)} placeholder="Ruta completa de la carpeta o archivo ZIP" required disabled={busy} /></label><button disabled={busy || !path.trim()}><Icon name="folder" size={18} />{busy ? "Importando…" : "Importar desde ruta"}</button></form></details>;
}

export function ReplaceImportDialog({ source, count, busy, onCancel, onConfirm }: { source: ImportSource; count: number; busy: boolean; onCancel: () => void; onConfirm: () => void }) {
  return <Dialog title="¿Sustituir los archivos del proyecto?" onClose={onCancel}>
    <div className="notice warning"><Icon name="warning" /><span>El proyecto ya contiene {count} {count === 1 ? "archivo" : "archivos"}. Al continuar, se reemplazarán y se eliminarán los análisis y planes actuales. Las decisiones guardadas por paso se conservarán.</span></div>
    <p className="muted">{typeof source === "string" ? `Ruta: ${source}` : `Archivo: ${source.name}`}</p>
    <div className="dialog-actions"><button type="button" className="secondary" onClick={onCancel}>Conservar archivos actuales</button><button type="button" className="danger-button" disabled={busy} onClick={onConfirm}>Reemplazar y continuar</button></div>
  </Dialog>;
}
