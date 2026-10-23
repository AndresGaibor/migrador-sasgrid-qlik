import { api } from "../api";
import { Icon } from "../components/Icon";
import { useAsync } from "../hooks";
import { Badge, Load, link, prioTone } from "./common";
import { sourceLines } from "../guided";
import { ArchivePathTree } from "../components/ArchivePathTree";

export function ProgramsTab({ id, file }: { id: string; file?: string }) {
  return file ? <ProgramDetail id={id} file={decodeURI(file)} /> : <ProgramList id={id} />;
}

function ProgramList({ id }: { id: string }) {
  const q = useAsync(() => api.programs(id), [id]);
  return (
    <>
      <h1>Tus programas SAS</h1>
      <p className="subtitle">Selecciona un programa para revisar los aspectos que requieren atención. «Hallazgos» indica cuántos puntos identificó el análisis.</p>
      <Load q={q}>
        {(rows) => rows.length ? <ArchivePathTree
          entries={rows.map((row) => ({ path: row.file, value: row }))}
          renderEntry={({ path, name, value: row }) => (
            <article className="archive-list-entry" key={path}>
              <a href={link(id, "programas", path)}><span className="archive-file-name"><span aria-hidden="true">📄</span><code>{name}</code></span></a>
              <span>{row.statements} sentencias</span>
              <span>{row.findings} hallazgos</span>
            </article>
          )}
        /> : (
          <div className="empty-state"><span className="empty-icon"><Icon name="file" size={30} /></span><h3>No se analizaron programas SAS</h3><p>El análisis no encontró archivos .sas. Revisa qué archivos se importaron o carga otro paquete.</p><div className="next-actions"><a className="button secondary" href={link(id, "inventario")}>Revisar mis archivos</a><a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar otros archivos</a></div></div>
        )}
      </Load>
      {q.error?.includes("analizado") && <p><a className="button" href={link(id, "resumen")}>Ir al resumen y analizar</a></p>}
    </>
  );
}

function ProgramDetail({ id, file }: { id: string; file: string }) {
  const [sourceFile, lineQuery] = file.split("?line=");
  const selectedLine = lineQuery ? Number(lineQuery) : undefined;
  const q = useAsync(() => api.program(id, sourceFile), [id, sourceFile]);
  return (
    <>
      <p><a href={link(id, "programas")}>← Programas</a></p>
      <h1>{sourceFile}</h1>
      <Load q={q}>
        {(p) => <>
          {selectedLine !== undefined && <section className="source-evidence" aria-live="polite"><div className="section-heading"><h2>Evidencia del programa · línea {selectedLine}</h2><Badge tone="ok">Fragmento SAS</Badge></div>{(() => { const lines = sourceLines(p.nodes ?? []); const excerpt = lines.filter((item) => item.line >= selectedLine - 2 && item.line <= selectedLine + 2); return excerpt.length ? <pre className="source-code">{excerpt.map((item) => <span className={item.line === selectedLine ? "source-line selected" : "source-line"} key={`${item.line}-${item.text}`}><b>{item.line}</b><code>{item.text}</code></span>)}</pre> : <p>No hay texto de sentencia disponible para esa línea; la referencia se conserva para ubicarla en el archivo original.</p>; })()}</section>}
          <h2>Hallazgos del análisis</h2>
          {p.findings.length === 0 ? (
            <p className="notice">No se encontraron hallazgos P1/P2 en este programa. La validación final se realiza en Talend Studio.</p>
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
          )}
        </>}
      </Load>
    </>
  );
}
