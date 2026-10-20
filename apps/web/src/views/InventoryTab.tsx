import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { Load, link } from "./common";
import { ReplaceImportDialog, SasFileUpload, ServerPathImport, type ImportSource } from "./import/ImportComponents";
import { InventoryResult, SkippedFiles } from "./import/InventoryComponents";

export function ImportTab({ id, go }: { id: string; go: (h: string) => void }) {
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const [pending, setPending] = useState<{ source: ImportSource; count: number }>();
  const runImport = async (source: ImportSource) => {
    setBusy(true); setErr(undefined);
    try {
      if (typeof source === "string") await api.importPath(id, source);
      else await api.upload(id, source);
      go(`/p/${id}/inventario`);
    } catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  const requestImport = async (source: ImportSource) => {
    if (busy) return;
    setBusy(true); setErr(undefined);
    try {
      const current = await api.inventory(id);
      if (current.files.length) setPending({ source, count: current.files.length });
      else await runImport(source);
    } catch (x) { setErr((x as Error).message); }
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
  return <>
    <h1>Mis archivos</h1><p className="subtitle">Estos son los archivos que se incluyeron en tu proyecto. El siguiente paso es analizarlos.</p>
    <Load q={q}>{(m) => m.files.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={30} /></span><h3>{m.skipped.length ? "No encontramos archivos compatibles" : "Aún no hay archivos"}</h3><p>{m.skipped.length ? `Se omitieron ${m.skipped.length} archivos. Revisa los motivos y carga un ZIP con programas SAS compatibles.` : "Carga un ZIP con tus programas para empezar."}</p><a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar archivos</a></div> : <>
      <InventoryResult id={id} manifest={m} />
    </>}</Load>
    {q.data && <SkippedFiles files={q.data.skipped} />}
  </>;
}
