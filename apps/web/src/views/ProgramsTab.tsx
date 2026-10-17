import { api } from "../api";
import { useAsync } from "../hooks";
import { Badge, Load, link, prioTone } from "./common";

export function ProgramsTab({ id, file }: { id: string; file?: string }) {
  return file ? <ProgramDetail id={id} file={decodeURI(file)} /> : <ProgramList id={id} />;
}

function ProgramList({ id }: { id: string }) {
  const q = useAsync(() => api.programs(id), [id]);
  return (
    <>
      <h1>Programas</h1>
      <Load q={q}>
        {(rows) => (
          <table>
            <thead><tr><th>Archivo</th><th>Sentencias</th><th>Hallazgos</th></tr></thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.file}>
                  <td><a href={link(id, "programas", r.file)}>{r.file}</a></td>
                  <td className="num">{r.statements}</td>
                  <td className="num">{r.findings}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </Load>
      {q.error?.includes("analizado") && <p>Ejecuta el análisis desde Resumen.</p>}
    </>
  );
}

function ProgramDetail({ id, file }: { id: string; file: string }) {
  const q = useAsync(() => api.program(id, file), [id, file]);
  return (
    <>
      <p><a href={link(id, "programas")}>← Programas</a></p>
      <h1>{file}</h1>
      <Load q={q}>
        {(p) =>
          p.findings.length === 0 ? (
            <p className="muted">Sin hallazgos P1/P2.</p>
          ) : (
            <table>
              <thead><tr><th>Línea</th><th>Prioridad</th><th>Código</th><th>Mensaje</th></tr></thead>
              <tbody>
                {p.findings.map((f, i) => (
                  <tr key={i}>
                    <td className="num">{f.evidence.line}</td>
                    <td><Badge tone={prioTone(f.priority)}>{f.priority ?? f.severity}</Badge></td>
                    <td className="mono">{f.code}</td>
                    <td>{f.message}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )
        }
      </Load>
    </>
  );
}
