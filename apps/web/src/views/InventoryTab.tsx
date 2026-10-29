import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { notifyError, notifySuccess } from "../errors";
import { Badge, Load, link } from "./common";
import { ReplaceImportDialog, SasFileUpload, ServerPathImport, type ImportSource } from "./import/ImportComponents";
import { ArchivePathTree } from "../components/ArchivePathTree";
import { SkippedFiles } from "./import/InventoryComponents";
import { filterFilesByKind, type InventoryKindFilter } from "../project-workspace";

export function ImportTab({ id, go }: { id: string; go: (h: string) => void }) {
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const [pending, setPending] = useState<{ source: ImportSource; count: number }>();
  const runImport = async (source: ImportSource) => {
    setBusy(true); setErr(undefined);
    try {
      const manifest = typeof source === "string"
        ? await api.importPath(id, source)
        : await api.upload(id, source);
      notifySuccess("Archivos cargados", `${manifest.files.length} archivos quedaron disponibles en el inventario.`);
      go(`/p/${id}/inventario`);
    } catch (x) { setErr(notifyError(x, "No se pudieron importar los archivos")); }
    finally { setBusy(false); }
  };
  const requestImport = async (source: ImportSource) => {
    if (busy) return;
    setBusy(true); setErr(undefined);
    try {
      const current = await api.inventory(id);
      if (current.files.length) setPending({ source, count: current.files.length });
      else await runImport(source);
    } catch (x) { setErr(notifyError(x, "No se pudo preparar la importación")); }
    finally { setBusy(false); }
  };
  const upload = (file: File) => {
    if (busy) return;
    if (!/\.(zip|sas)$/i.test(file.name)) { setErr("Selecciona un archivo ZIP o .sas que contenga programas compatibles."); return; }
    void requestImport(file);
  };
  const confirmReplacement = () => {
    if (!pending) return;
    const source = pending.source;
    setPending(undefined);
    void runImport(source);
  };
  return <>
    <h1>Carga tus archivos SAS</h1>
    <p className="subtitle">El primer paso es reunir los programas que quieres migrar. Tus archivos originales no se modifican.</p>
    <SasFileUpload busy={busy} error={err} onSelect={upload} />
    {pending && <ReplaceImportDialog source={pending.source} count={pending.count} busy={busy} onCancel={() => setPending(undefined)} onConfirm={confirmReplacement} />}
    <ServerPathImport busy={busy} onImport={(source) => { void requestImport(source); }} />
  </>;
}

export function InventoryTab({ id }: { id: string }) {
  const q = useAsync(() => api.inventory(id), [id]);
  const [kindFilter, setKindFilter] = useState<InventoryKindFilter>("all");
  const copyPath = async (path: string) => {
    try {
      await navigator.clipboard.writeText(path);
      notifySuccess("Ruta copiada", path);
    } catch (error) {
      notifyError(error, "No se pudo copiar la ruta", "Copia la ruta desde el atributo de título del archivo.");
    }
  };
  const visibleFiles = q.data ? filterFilesByKind(q.data.files, kindFilter) : [];
  return <>
    <h1>Mis archivos</h1><p className="subtitle">Conservamos los nombres y las carpetas de origen para que cada programa siga en su ubicación original.</p>
    <Load q={q}>{(m) => m.files.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={30} /></span><h3>{m.skipped.length ? "No encontramos archivos compatibles" : "Aún no hay archivos"}</h3><p>{m.skipped.length ? `Se omitieron ${m.skipped.length} archivos. Revisa los motivos y carga fuentes compatibles.` : "Carga programas SAS o un ZIP para empezar."}</p><a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar archivos</a></div> : <>
      <section className="import-result" aria-label="Resultado de la carga">
        <div className="import-result-title"><span aria-hidden="true">✅</span><div><h2>Archivos del proyecto disponibles</h2><p>Se conservaron los archivos y sus carpetas. Consulta el resumen para ver el estado del análisis automático.</p></div></div>
        <div className="import-result-metrics"><div><strong>{m.files.length}</strong><span>archivos incluidos</span></div><div><strong>{m.files.filter((f) => f.kind === "sas").length}</strong><span>programas SAS</span></div><div><strong>{m.skipped.length}</strong><span>archivos omitidos</span></div></div>
        <a className="button" href={link(id, "resumen")}><Icon name="chart" size={18} /> Ver análisis y estado <Icon name="arrow" size={17} /></a>
      </section>
      <div className="inventory-file-toolbar">
        <div className="section-heading" style={{ marginTop: 24 }}><h2>Archivos incluidos</h2><Badge tone="ok">{m.files.length} en total</Badge></div>
        <label>Tipo de archivo <select aria-label="Filtrar archivos por tipo" value={kindFilter} onChange={(event) => setKindFilter(event.target.value as InventoryKindFilter)}>
          <option value="all">Todos ({m.files.length})</option>
          {(["sas", "shell", "log", "doc", "other"] as const).map((kind) => <option key={kind} value={kind}>{kind} ({m.files.filter((file) => file.kind === kind).length})</option>)}
        </select></label>
      </div>
      {visibleFiles.length === 0 ? <p className="muted">No hay archivos de tipo «{kindFilter}» en este proyecto.</p> : <ArchivePathTree
        entries={visibleFiles.map((file) => ({ path: file.path, value: file }))}
        renderEntry={({ path, name, value: file }) => (
          <article className="archive-file-entry" key={path} title={path}>
            <span className="archive-file-name"><Icon name="file" size={16} /><code>{name}</code></span>
            <Badge>{file.kind}</Badge>
            <span className="muted">{new Intl.NumberFormat("es", { maximumFractionDigits: 1 }).format(file.size / 1024)} KB</span>
            <code className="mono" title={file.sha256}>{file.sha256.slice(0, 12)}</code>
            <button type="button" className="secondary archive-copy-path" onClick={() => { void copyPath(path); }}>Copiar ruta</button>
          </article>
        )}
      />}
    </>}</Load>
    {q.data && <SkippedFiles files={q.data.skipped} />}
  </>;
}
