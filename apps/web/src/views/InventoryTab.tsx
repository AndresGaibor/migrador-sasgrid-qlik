import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Badge, Load } from "./common";

export function ImportTab({ id, go }: { id: string; go: (h: string) => void }) {
  const [path, setPath] = useState("");
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const run = async (e: React.FormEvent) => {
    e.preventDefault();
    setBusy(true);
    setErr(undefined);
    try {
      await api.importPath(id, path.trim());
      go(`/p/${id}/inventario`);
    } catch (x) {
      setErr((x as Error).message);
    } finally {
      setBusy(false);
    }
  };
  const upload = async (f: File | undefined) => {
    if (!f) return;
    setBusy(true);
    setErr(undefined);
    try {
      await api.upload(id, f);
      go(`/p/${id}/inventario`);
    } catch (x) {
      setErr((x as Error).message);
    } finally {
      setBusy(false);
    }
  };
  return (
    <>
      <h1>Importar</h1>
      <div className="row">
        <label>
          Subir ZIP del proyecto o un archivo .sas
          <input type="file" accept=".zip,.sas" disabled={busy} onChange={(e) => upload(e.target.files?.[0])} />
        </label>
      </div>
      <p className="muted">
        También puedes indicar una carpeta o ZIP que ya esté en el servidor (solo bajo las rutas permitidas). Se copia una instantánea; el original no se modifica. Reimportar borra
        análisis y planes derivados (las decisiones por paso se conservan).
      </p>
      <form onSubmit={run} className="row">
        <label>
          Ruta
          <input value={path} onChange={(e) => setPath(e.target.value)} placeholder="/ruta/a/programas" required />
        </label>
        <button disabled={busy || !path.trim()}>{busy ? "Importando…" : "Importar"}</button>
      </form>
      {err && <p className="error" role="alert">{err}</p>}
    </>
  );
}

export function InventoryTab({ id }: { id: string }) {
  const q = useAsync(() => api.inventory(id), [id]);
  return (
    <>
      <h1>Inventario</h1>
      <Load q={q}>
        {(m) => (
          <>
            <p>
              {m.files.length} archivos · {m.skipped.length} omitidos
            </p>
            <table>
              <thead>
                <tr><th>Ruta</th><th>Tipo</th><th>Bytes</th><th>sha256</th></tr>
              </thead>
              <tbody>
                {m.files.map((f) => (
                  <tr key={f.path}>
                    <td>{f.path}</td>
                    <td><Badge>{f.kind}</Badge></td>
                    <td className="num">{f.size}</td>
                    <td className="mono">{f.sha256.slice(0, 12)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            {m.skipped.length > 0 && (
              <details>
                <summary>Omitidos ({m.skipped.length})</summary>
                <ul>{m.skipped.map((s) => <li key={s.path}>{s.path} — {s.reason}</li>)}</ul>
              </details>
            )}
          </>
        )}
      </Load>
    </>
  );
}
