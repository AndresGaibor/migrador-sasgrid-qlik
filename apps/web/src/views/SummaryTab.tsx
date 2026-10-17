import { useState } from "react";
import { api } from "../api";
import type { Summary } from "../types";
import { Badge, prioTone } from "./common";

export function SummaryTab({ id }: { id: string }) {
  const [s, setS] = useState<Summary>();
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const run = async () => {
    setBusy(true);
    setErr(undefined);
    try {
      setS(await api.analyze(id));
    } catch (x) {
      setErr((x as Error).message);
    } finally {
      setBusy(false);
    }
  };
  return (
    <>
      <h1>Resumen</h1>
      <button onClick={run} disabled={busy}>{busy ? "Analizando…" : "Analizar proyecto"}</button>
      {err && <p className="error" role="alert">{err}</p>}
      {s && (
        <>
          <p>
            {s.programs} programas · {s.statements} sentencias · {s.unrecognized} sin reconocer ·{" "}
            {s.macro_fragments} fragmentos de macro
          </p>
          <p>
            {Object.entries(s.findings_by_priority).map(([p, n]) => (
              <Badge key={p} tone={prioTone(p)}>{p}: {n}</Badge>
            ))}
          </p>
          <table>
            <thead><tr><th>Construcción</th><th>Prioridad</th><th>Ocurrencias</th></tr></thead>
            <tbody>
              {s.coverage.map((c) => (
                <tr key={c.tag}>
                  <td>{c.tag}</td>
                  <td><Badge tone={prioTone(c.priority)}>{c.priority}</Badge></td>
                  <td className="num">{c.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </>
  );
}
