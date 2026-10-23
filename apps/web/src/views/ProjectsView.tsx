import { useEffect, useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Dialog } from "../components/Dialog";
import { Icon } from "../components/Icon";
import { filterProjectsByQuery, processingLabel } from "../project-workspace";
import type { Project } from "../types";
import { Load } from "./common";

export function ProjectsView({ go }: { go: (h: string) => void }) {
  const q = useAsync(api.projects, []);
  const [projectName, setProjectName] = useState("");
  const [search, setSearch] = useState("");
  const [sort, setSort] = useState("recent");
  const [uploadOpen, setUploadOpen] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File>();
  const [err, setErr] = useState<string>();
  const hasActiveProjects = q.data?.some((project) => project.processing?.status === "queued" || project.processing?.status === "running") ?? false;
  useEffect(() => {
    if (!hasActiveProjects) return;
    const timer = window.setInterval(q.reload, 2000);
    return () => window.clearInterval(timer);
  }, [hasActiveProjects, q.reload]);
  const openUpload = () => { setProjectName(""); setSelectedFile(undefined); setErr(undefined); setUploadOpen(true); };
  const upload = async (event: React.FormEvent) => {
    event.preventDefault();
    if (uploading || !selectedFile) return;
    if (!selectedFile.name.toLocaleLowerCase("es").endsWith(".zip")) {
      setErr("Selecciona un archivo .zip para crear un proyecto independiente.");
      return;
    }
    setUploading(true);
    setErr(undefined);
    try {
      const created = await api.createProjectFromZip(selectedFile, projectName);
      q.reload();
      go(`/p/${created.project.id}/resumen`);
    } catch (error) {
      setErr((error as Error).message);
    } finally {
      setUploading(false);
    }
  };

  return <>
    <div className="breadcrumb"><Icon name="grid" size={15} /> Espacio de trabajo <Icon name="chevron" size={13} /><span>Mis proyectos</span></div>
    <div className="page-heading"><div><div className="eyebrow">TODO EMPIEZA CON UN PROYECTO</div><h1>Tu próximo paso, más claro.</h1><p className="subtitle">Cada ZIP crea un proyecto aislado. El portal conserva sus carpetas, analiza sus programas y prepara las guías.</p></div><button onClick={openUpload}><Icon name="upload" size={18} /> Subir ZIP y crear proyecto</button></div>
    <section className="journey" aria-labelledby="journey-title">
      <div className="journey-heading"><span className="eyebrow">DE SAS A TALEND</span><h2 id="journey-title">Una ruta sencilla para tu migración</h2><p>El portal interpreta el proyecto y el MCP recibe instrucciones desde la guía de cada Job.</p></div>
      <ol className="journey-steps">
        <li><span className="journey-icon"><Icon name="upload" size={24} /></span><div><span className="step-label">PASO 01</span><h3>Carga un ZIP</h3><p>Un paquete crea un proyecto independiente.</p></div></li>
        <li><span className="journey-icon"><Icon name="chart" size={24} /></span><div><span className="step-label">PASO 02</span><h3>Entiende el flujo</h3><p>Revisa archivos, análisis y dependencias.</p></div></li>
        <li><span className="journey-icon"><Icon name="flow" size={24} /></span><div><span className="step-label">PASO 03</span><h3>Prepara Talend</h3><p>Implementa cada Job desde su guía.</p></div></li>
      </ol>
    </section>
    <section aria-labelledby="projects-title">
      <div className="section-heading"><h2 id="projects-title">Mis proyectos <span className="count">{q.data?.length ?? "—"}</span></h2><span className="muted">ZIP, carpetas, estado y análisis permanecen aislados</span></div>
      <div className="project-toolbar">
        <label className="search-field"><Icon name="search" size={18} /><input aria-label="Buscar proyectos" placeholder="Buscar por proyecto o nombre del ZIP…" value={search} onChange={(event) => setSearch(event.target.value)} />{search && <button className="icon-button" aria-label="Limpiar búsqueda" onClick={() => setSearch("")}><Icon name="close" size={16} /></button>}</label>
        <label className="sort-field">Ordenar por <select value={sort} onChange={(event) => setSort(event.target.value)}><option value="recent">Más recientes</option><option value="name">Nombre: A–Z</option></select></label>
      </div>
      <Load q={q}>{(projects) => {
        const filtered = filterProjectsByQuery(projects, search).sort((a, b) => sort === "name" ? a.name.localeCompare(b.name, "es") : Date.parse(b.created_at) - Date.parse(a.created_at));
        return projects.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={32} /></span><h3>Tu primer proyecto empieza aquí</h3><p>Sube un ZIP y el portal creará una carpeta independiente para analizar todos sus programas SAS.</p><button onClick={openUpload}><Icon name="upload" size={18} /> Subir ZIP y empezar</button><span className="empty-note">El análisis comienza automáticamente después de recibir el archivo.</span></div>
          : filtered.length === 0 ? <div className="empty-state"><Icon name="search" size={30} /><h3>No encontramos ese proyecto</h3><p>Prueba con otro nombre de proyecto o del ZIP.</p><button className="secondary" onClick={() => setSearch("")}>Ver todos los proyectos</button></div>
          : <div className="project-grid">{filtered.map((project) => <ProjectCard key={project.id} project={project} />)}<button className="new-project-card" onClick={openUpload}><span><Icon name="plus" size={26} /></span><strong>Subir otro ZIP</strong><small>Crear un proyecto aislado</small></button></div>;
      }}</Load>
    </section>
    <div className="home-note"><Icon name="info" size={18} /><p>Los proyectos existentes sin ZIP registrado mantienen su flujo manual. Un ZIP nuevo siempre crea otro proyecto para evitar mezclar archivos.</p></div>
    {uploadOpen && <Dialog title="Crear proyecto desde un ZIP" onClose={() => { if (!uploading) { setUploadOpen(false); setSelectedFile(undefined); setErr(undefined); } }}>
      <p className="muted">El portal extraerá y analizará el contenido en segundo plano. El proyecto aparecerá cuando el servidor confirme que recibió y registró el ZIP.</p>
      <form onSubmit={upload}>
        <label>Archivo ZIP<input autoFocus type="file" accept=".zip,application/zip" disabled={uploading} onChange={(event) => { setSelectedFile(event.target.files?.[0]); setErr(undefined); }} /></label>
        {selectedFile && <div className="selected-zip"><Icon name="file" size={18} /><span title={selectedFile.name}>{selectedFile.name}</span><small>{formatBytes(selectedFile.size)}</small></div>}
        <label>Nombre del proyecto <span className="muted">(opcional)</span><input value={projectName} onChange={(event) => setProjectName(event.target.value)} placeholder={selectedFile?.name.replace(/\.zip$/i, "") || "Se usará el nombre del ZIP"} maxLength={120} disabled={uploading} /></label>
        {err && <p className="error" role="alert">{err}</p>}
        {uploading && <p className="loading-state" role="status"><span className="spinner" /> Subiendo el ZIP y preparando el proyecto…</p>}
        <div className="dialog-actions"><button type="button" className="secondary" disabled={uploading} onClick={() => { setUploadOpen(false); setSelectedFile(undefined); setErr(undefined); }}>Cancelar</button><button disabled={uploading || !selectedFile}><Icon name="upload" size={17} />{uploading ? "Registrando ZIP…" : "Subir ZIP y analizar"}</button></div>
      </form>
    </Dialog>}
  </>;
}

function ProjectCard({ project }: { project: Project }) {
  const summary = project.manifest_summary;
  const processing = project.processing;
  const isLegacy = !project.archive_name;
  const status = isLegacy ? "Proyecto existente · ZIP no registrado" : processing ? processingLabel(processing) : "Análisis pendiente";
  const tone = processing?.status === "completed" ? "ok" : processing?.status === "failed" ? "bad" : processing?.status === "interrupted" ? "warn" : processing && (processing.status === "running" || processing.status === "queued") ? "active" : "neutral";
  const activity = processing?.updated_at ?? project.uploaded_at ?? project.created_at;
  return <a className="project-card" href={`#/p/${project.id}/resumen`}>
    <div className="project-card-visual"><span className="project-type">{isLegacy ? "PROYECTO" : "PROYECTO SAS → TALEND"}</span><div className="mini-flow"><span><Icon name="file" size={24} /></span><i /><span className="flow-center"><Icon name="flow" size={28} /></span><i /><span><Icon name="check" size={24} /></span></div></div>
    <div className="project-card-body"><h3>{project.name}</h3>
      <p className="project-archive-name" title={project.archive_name ?? undefined}><Icon name="folder" size={14} />{project.archive_name ?? "Importación manual"}</p>
      <span className={`project-card-status ${tone}`}><i />{status}</span>
      <div className="project-card-counts">{summary ? <><span>{summary.programs} programas</span><span>{summary.folders} carpetas</span><span>{summary.files} archivos</span></> : <span>{isLegacy ? "Sin resumen ZIP" : "Conteo al finalizar extracción"}</span>}</div>
      <p className="project-card-date"><Icon name="clock" size={14} /> Actualizado {new Date(activity).toLocaleString("es", { dateStyle: "medium", timeStyle: "short" })}</p>
      <div className="project-card-action"><span>Abrir proyecto</span><Icon name="arrow" size={18} /></div>
    </div>
  </a>;
}

function formatBytes(size: number): string {
  if (size < 1024) return `${size} B`;
  if (size < 1024 * 1024) return `${(size / 1024).toFixed(1)} KB`;
  return `${(size / (1024 * 1024)).toFixed(1)} MB`;
}
