import { useState } from "react";
import { api } from "../api";
import { Icon } from "../components/Icon";
import type { JobPlan } from "../types";
import { guideCsv, guideIndexMarkdown, guideJson, guideMarkdown } from "../guide-export";

type ServerExport = { directory: string; files: string[]; steps_csv_rows?: number };

function download(name: string, content: string, mime: string) {
  const blob = new Blob([content], { type: `${mime};charset=utf-8` });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = name;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function safeFilename(program: string) {
  return program.replace(/[^A-Za-z0-9._-]+/g, "__").replace(/\.[^.]+$/, "");
}

export function ExportTab({ id }: { id: string }) {
  const [server, setServer] = useState<ServerExport>();
  const [plans, setPlans] = useState<JobPlan[]>();
  const [err, setErr] = useState<string>();
  const [busy, setBusy] = useState(false);
  const run = async () => {
    setErr(undefined); setBusy(true);
    try {
      const serverResult = await api.exportAll(id);
      const rows = await api.plans(id);
      const details = await Promise.all(rows.map((row) => api.plan(id, row.program)));
      setServer(serverResult);
      setPlans(details);
    } catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  return <>
    <h1>Descarga tu guía de trabajo</h1><p className="subtitle">Lleva las guías, referencias y decisiones contigo para revisarlas con tu equipo.</p>
    <section className="panel"><div className="panel-heading"><Icon name="download" size={27} /><div><h2>Archivos para continuar</h2><p>Preparamos una guía Markdown y un JSON por job, además del índice y el CSV general.</p></div></div><ul className="list"><li><strong>Markdown:</strong> lectura sencilla, con evidencia SAS y enlaces oficiales.</li><li><strong>JSON:</strong> datos del plan, estado guiado, motivo de bloqueo y pendientes.</li><li><strong>CSV:</strong> seguimiento en Excel con estados, evidencia y referencias.</li></ul><div className="notice"><Icon name="info" /><span>También se guarda una copia en el servidor. Los archivos descargables describen una guía de trabajo y no generan un Job Talend <code>.item</code>.</span></div><button onClick={run} disabled={busy}><Icon name="download" size={18} />{busy ? "Preparando descargas…" : "Exportar planes"}</button></section>
    {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
    {server && plans && <>
      <section className="panel"><div className="notice" role="status"><Icon name="check" /><span><strong>Exportación preparada.</strong> Se guardaron {server.files.length} archivos en el servidor y puedes descargarlos aquí.</span></div><p><strong>Copia del servidor:</strong> <code>{server.directory}</code></p><details><summary>Archivos guardados en el servidor ({server.files.length})</summary><ul>{server.files.map((file) => <li key={file}><a href={api.exportFile(id, file)} download>{file}</a></li>)}</ul></details></section>
      <section className="panel"><div className="section-heading"><h2>Resumen y seguimiento</h2></div><p>Descarga un índice general o el listado de pasos para Excel.</p><div className="export-downloads"><button className="secondary" onClick={() => download("guias-migracion.md", guideIndexMarkdown(plans), "text/markdown")}><Icon name="download" size={17} /> Índice Markdown</button><button className="secondary" onClick={() => download("pasos-migracion.csv", guideCsv(plans, id), "text/csv")}><Icon name="download" size={17} /> Tabla CSV para Excel</button></div></section>
      <section className="panel"><div className="section-heading"><h2>Guías por job <span className="count">{plans.length}</span></h2></div>{plans.length ? <div className="export-guide-list">{plans.map((plan) => { const allSteps = [...plan.steps, ...plan.children.flatMap((child) => child.steps)]; return <article className="export-guide" key={plan.program}><div><h3>{plan.job_name}</h3><p>Programa SAS: <code>{plan.program}</code></p><small>{allSteps.length} pasos · {allSteps.filter((step) => step.pending.length > 0).length} con decisiones pendientes</small></div><div className="export-downloads"><button className="secondary" onClick={() => download(`${safeFilename(plan.program)}.md`, guideMarkdown(plan, id), "text/markdown")}><Icon name="download" size={16} /> Markdown</button><button className="secondary" onClick={() => download(`${safeFilename(plan.program)}.json`, guideJson(plan, id), "application/json")}><Icon name="download" size={16} /> JSON</button></div></article>; })}</div> : <p>No hay guías disponibles para descargar.</p>}</section>
    </>}
  </>;
}
