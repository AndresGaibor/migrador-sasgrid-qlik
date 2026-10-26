import type { Manifest } from "../../types";
import { Icon } from "../../components/Icon";
import { Badge, link } from "../common";

export function InventoryResult({ id, manifest }: { id: string; manifest: Manifest }) {
  const sasFiles = manifest.files.filter((file) => file.kind === "sas").length;
  return <>
    <section className="import-result" aria-label="Resultado de la carga">
      <div className="import-result-title"><span aria-hidden="true"><Icon name="check" size={22} /></span><div><h2>Carga completada</h2><p>Revisamos tu paquete y ya puedes iniciar el análisis.</p></div></div>
      <div className="import-result-metrics"><div><strong>{manifest.files.length}</strong><span>archivos incluidos</span></div><div><strong>{sasFiles}</strong><span>programas SAS</span></div><div><strong>{manifest.skipped.length}</strong><span>archivos omitidos</span></div></div>
      <a className="button" href={link(id, "resumen")}><Icon name="chart" size={18} /> Analizar mis programas <Icon name="arrow" size={17} /></a>
    </section>
    <div className="section-heading" style={{ marginTop: 24 }}><h2>Archivos incluidos</h2><Badge tone="ok">{manifest.files.length} listos</Badge></div>
    <table><thead><tr><th>Archivo</th><th>Tipo</th><th className="num">Tamaño</th><th>Identificador de integridad</th></tr></thead><tbody>{manifest.files.map((file) => <tr key={file.path}><td><Icon name="file" size={15} /> {file.path}</td><td><Badge>{file.kind}</Badge></td><td className="num">{new Intl.NumberFormat("es", { maximumFractionDigits: 1 }).format(file.size / 1024)} KB</td><td className="mono" title={file.sha256}>{file.sha256.slice(0, 12)}</td></tr>)}</tbody></table>
  </>;
}

export function SkippedFiles({ files }: { files: Manifest["skipped"] }) {
  return files.length > 0 && <details><summary>Archivos que no se incluyeron ({files.length})</summary><p className="muted">Estos archivos se omitieron durante la carga por los siguientes motivos:</p><ul>{files.map((file) => <li key={file.path}>{file.path} — {file.reason}</li>)}</ul></details>;
}
