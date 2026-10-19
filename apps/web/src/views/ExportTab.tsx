import { useState } from "react";
import { api } from "../api";

export function ExportTab({ id }: { id: string }) {
  const [r, setR] = useState<{ directory: string; files: string[] }>();
  const [err, setErr] = useState<string>();
  const run = async () => {
    setErr(undefined);
    try {
      setR(await api.exportAll(id));
    } catch (x) {
      setErr((x as Error).message);
    }
  };
  return (
    <>
      <h1>Exportar</h1>
      <p className="muted">Un Markdown y un JSON por Job, más <code>index.md</code> y <code>steps.csv</code>, en el servidor local.</p>
      <button onClick={run}>Exportar planes</button>
      {err && <p className="error" role="alert">{err}</p>}
      {r && (
        <>
          <p>Carpeta: <code>{r.directory}</code> · {r.files.length} archivos</p>
          <ul>{r.files.map((f) => <li key={f}><a href={api.exportFile(id, f)} download>{f}</a></li>)}</ul>
        </>
      )}
    </>
  );
}
