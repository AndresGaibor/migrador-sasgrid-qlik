import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { ArchivePathTree } from "../components/ArchivePathTree";
import { Badge, Load, link } from "./common";

export function ImportTab({ id, go }: { id: string; go: (h: string) => void }) {
  const [path, setPath] = useState("");
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const run = async (e: React.FormEvent) => {
    e.preventDefault();
    if (busy) return;
    setBusy(true); setErr(undefined);
    try { await api.importPath(id, path.trim()); go(`/p/${id}/inventario`); }
    catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  const upload = async (f: File | undefined) => {
    if (!f || busy) return;
    if (!/\.(zip|sas)$/i.test(f.name)) { setErr("Selecciona un archivo ZIP o .sas que contenga programas compatibles."); return; }
    setBusy(true); setErr(undefined);
    try { await api.upload(id, f); go(`/p/${id}/inventario`); }
    catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  return <>
    <h1>Carga tus archivos SAS</h1>
    <p className="subtitle">El primer paso es reunir los programas que quieres migrar. Tus archivos originales no se modifican.</p>
    <section className="panel">
      <div className="panel-heading"><Icon name="upload" size={24} /><div><h2>Selecciona un archivo ZIP</h2><p>La forma más sencilla de comenzar.</p></div><Badge tone="ok">Recomendado</Badge></div>
      <div className="upload-zone" aria-busy={busy}>
        <Icon name="upload" size={38} /><h3>{busy ? "Estamos cargando tus archivos…" : "Tus programas, en un solo archivo"}</h3>
        <p>Comprime la carpeta de programas SAS en formato ZIP y selecciónala aquí.</p>
        <label><span className="sr-only">Archivo ZIP o programa SAS</span><input type="file" accept=".zip,.sas,application/zip" disabled={busy} onChange={(e) => { void upload(e.target.files?.[0]); e.target.value = ""; }} /></label>
        <small>Se incluirán los archivos compatibles con el análisis.</small>
        {busy && <div role="status" className="loading-state"><span className="spinner" /> Cargando e identificando archivos…</div>}
      </div>
      {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
    </section>
    <div className="notice warning"><Icon name="info" /><span><strong>Los ZIP se mantienen aislados:</strong> una nueva carga desde «Mis proyectos» crea un proyecto separado; este proyecto no se sobrescribe ni mezcla con otro lote.</span></div>
    <details><summary>Opciones avanzadas: importar desde una carpeta del servidor</summary><p className="muted">Usa esta opción si los archivos ya están en el equipo donde funciona el servicio. La carpeta debe estar dentro de las rutas permitidas.</p><form onSubmit={run} className="row"><label className="grow">Ruta de la carpeta o del ZIP<input value={path} onChange={(e) => setPath(e.target.value)} placeholder="Ruta completa de la carpeta o archivo ZIP" required disabled={busy} /></label><button disabled={busy || !path.trim()}><Icon name="folder" size={18} />{busy ? "Importando…" : "Importar desde ruta"}</button></form></details>
  </>;
}

export function InventoryTab({ id }: { id: string }) {
  const q = useAsync(() => api.inventory(id), [id]);
  return <>
    <h1>Mis archivos</h1><p className="subtitle">Conservamos las carpetas del ZIP dentro de este proyecto para que cada programa siga en su ubicación original.</p>
    <Load q={q}>{(m) => m.files.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={30} /></span><h3>{m.skipped.length ? "No encontramos archivos compatibles" : "Aún no hay archivos"}</h3><p>{m.skipped.length ? `Se omitieron ${m.skipped.length} archivos. Revisa los motivos y carga un ZIP con programas SAS compatibles.` : "Carga un ZIP con tus programas para empezar."}</p><a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar archivos</a></div> : <>
      <section className="import-result" aria-label="Resultado de la carga">
        <div className="import-result-title"><span aria-hidden="true">✅</span><div><h2>Archivos del proyecto disponibles</h2><p>El ZIP y sus carpetas se guardaron en este proyecto. Consulta el resumen para ver el estado del análisis automático.</p></div></div>
        <div className="import-result-metrics"><div><strong>{m.files.length}</strong><span>archivos incluidos</span></div><div><strong>{m.files.filter((f) => f.kind === "sas").length}</strong><span>programas SAS</span></div><div><strong>{m.skipped.length}</strong><span>archivos omitidos</span></div></div>
        <a className="button" href={link(id, "resumen")}><Icon name="chart" size={18} /> Ver análisis y estado <Icon name="arrow" size={17} /></a>
      </section>
      <div className="section-heading" style={{ marginTop: 24 }}><h2>Archivos incluidos</h2><Badge tone="ok">{m.files.length} listos</Badge></div>
      <ArchivePathTree
        entries={m.files.map((file) => ({ path: file.path, value: file }))}
        renderEntry={({ path, name, value: file }) => (
          <article className="archive-file-entry" key={path} title={path}>
            <span className="archive-file-name"><Icon name="file" size={16} /><code>{name}</code></span>
            <Badge>{file.kind}</Badge>
            <span className="muted">{new Intl.NumberFormat("es", { maximumFractionDigits: 1 }).format(file.size / 1024)} KB</span>
            <code className="mono" title={file.sha256}>{file.sha256.slice(0, 12)}</code>
          </article>
        )}
      />
    </>}</Load>
    {q.data && q.data.skipped.length > 0 && <details><summary>Archivos que no se incluyeron ({q.data.skipped.length})</summary><p className="muted">Estos archivos se omitieron durante la carga por los siguientes motivos:</p><ul>{q.data.skipped.map((s) => <li key={s.path}>{s.path} — {s.reason}</li>)}</ul></details>}
  </>;
}
