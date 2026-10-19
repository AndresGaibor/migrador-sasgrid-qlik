import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { Dialog } from "../components/Dialog";
import { Badge, Load, link } from "./common";

export function ImportTab({ id, go }: { id: string; go: (h: string) => void }) {
  const [path, setPath] = useState("");
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const [pending, setPending] = useState<{ source: File | string; count: number }>();
  const runImport = async (source: File | string) => {
    setBusy(true); setErr(undefined);
    try {
      if (typeof source === "string") await api.importPath(id, source);
      else await api.upload(id, source);
      go(`/p/${id}/inventario`);
    } catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  const requestImport = async (source: File | string) => {
    if (busy) return;
    setBusy(true); setErr(undefined);
    try {
      const current = await api.inventory(id);
      if (current.files.length) setPending({ source, count: current.files.length });
      else await runImport(source);
    } catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  const run = (e: React.FormEvent) => {
    e.preventDefault();
    if (path.trim()) void requestImport(path.trim());
  };
  const upload = (f: File | undefined) => {
    if (!f || busy) return;
    if (!/\.(zip|sas)$/i.test(f.name)) { setErr("Selecciona un archivo ZIP o .sas que contenga programas compatibles."); return; }
    void requestImport(f);
  };
  return <>
    <h1>Carga tus archivos SAS</h1>
    <p className="subtitle">El primer paso es reunir los programas que quieres migrar. Tus archivos originales no se modifican.</p>
    <section className="panel">
      <div className="panel-heading"><Icon name="upload" size={24} /><div><h2>Selecciona un ZIP o un programa SAS</h2><p>Un ZIP permite cargar varios programas de una vez.</p></div><Badge tone="ok">Recomendado</Badge></div>
      <div className="upload-zone" aria-busy={busy}>
        <Icon name="upload" size={38} /><h3>{busy ? "Procesando la carga…" : "Tus programas, en un solo archivo"}</h3>
        <p>Elige un ZIP con varios programas o un archivo .sas individual.</p>
        <label><span className="sr-only">Archivo ZIP o programa SAS</span><input type="file" accept=".zip,.sas,application/zip" disabled={busy} onChange={(e) => { void upload(e.target.files?.[0]); e.target.value = ""; }} /></label>
        <small>Se incluirán los archivos compatibles con el análisis.</small>
        {busy && <div role="status" className="loading-state"><span className="spinner" /> Comprobando el proyecto y preparando tus archivos…</div>}
      </div>
      {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
    </section>
    {pending && <Dialog title="¿Sustituir los archivos del proyecto?" onClose={() => setPending(undefined)}><div className="notice warning"><Icon name="warning" /><span>El proyecto ya contiene {pending.count} {pending.count === 1 ? "archivo" : "archivos"}. Al continuar, se reemplazarán y se eliminarán los análisis y planes actuales. Las decisiones guardadas por paso se conservarán.</span></div><p className="muted">{typeof pending.source === "string" ? `Ruta: ${pending.source}` : `Archivo: ${pending.source.name}`}</p><div className="dialog-actions"><button type="button" className="secondary" onClick={() => setPending(undefined)}>Conservar archivos actuales</button><button type="button" className="danger-button" disabled={busy} onClick={() => { const source = pending.source; setPending(undefined); void runImport(source); }}>Reemplazar y continuar</button></div></Dialog>}
    <details><summary>Opciones avanzadas: importar desde una carpeta del servidor</summary><p className="muted">Usa esta opción si los archivos ya están en el equipo donde funciona el servicio. La carpeta debe estar dentro de las rutas permitidas.</p><form onSubmit={run} className="row"><label className="grow">Ruta de la carpeta o del ZIP<input value={path} onChange={(e) => setPath(e.target.value)} placeholder="Ruta completa de la carpeta o archivo ZIP" required disabled={busy} /></label><button disabled={busy || !path.trim()}><Icon name="folder" size={18} />{busy ? "Importando…" : "Importar desde ruta"}</button></form></details>
  </>;
}

export function InventoryTab({ id }: { id: string }) {
  const q = useAsync(() => api.inventory(id), [id]);
  return <>
    <h1>Mis archivos</h1><p className="subtitle">Estos son los archivos que se incluyeron en tu proyecto. El siguiente paso es analizarlos.</p>
    <Load q={q}>{(m) => m.files.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={30} /></span><h3>{m.skipped.length ? "No encontramos archivos compatibles" : "Aún no hay archivos"}</h3><p>{m.skipped.length ? `Se omitieron ${m.skipped.length} archivos. Revisa los motivos y carga un ZIP con programas SAS compatibles.` : "Carga un ZIP con tus programas para empezar."}</p><a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar archivos</a></div> : <>
      <section className="import-result" aria-label="Resultado de la carga">
        <div className="import-result-title"><span aria-hidden="true"><Icon name="check" size={22} /></span><div><h2>Carga completada</h2><p>Revisamos tu paquete y ya puedes iniciar el análisis.</p></div></div>
        <div className="import-result-metrics"><div><strong>{m.files.length}</strong><span>archivos incluidos</span></div><div><strong>{m.files.filter((f) => f.kind === "sas").length}</strong><span>programas SAS</span></div><div><strong>{m.skipped.length}</strong><span>archivos omitidos</span></div></div>
        <a className="button" href={link(id, "resumen")}><Icon name="chart" size={18} /> Analizar mis programas <Icon name="arrow" size={17} /></a>
      </section>
      <div className="section-heading" style={{ marginTop: 24 }}><h2>Archivos incluidos</h2><Badge tone="ok">{m.files.length} listos</Badge></div>
      <table><thead><tr><th>Archivo</th><th>Tipo</th><th className="num">Tamaño</th><th>Identificador de integridad</th></tr></thead><tbody>{m.files.map((f) => <tr key={f.path}><td><Icon name="file" size={15} /> {f.path}</td><td><Badge>{f.kind}</Badge></td><td className="num">{new Intl.NumberFormat("es", { maximumFractionDigits: 1 }).format(f.size / 1024)} KB</td><td className="mono" title={f.sha256}>{f.sha256.slice(0, 12)}</td></tr>)}</tbody></table>
    </>}</Load>
    {q.data && q.data.skipped.length > 0 && <details><summary>Archivos que no se incluyeron ({q.data.skipped.length})</summary><p className="muted">Estos archivos se omitieron durante la carga por los siguientes motivos:</p><ul>{q.data.skipped.map((s) => <li key={s.path}>{s.path} — {s.reason}</li>)}</ul></details>}
  </>;
}
