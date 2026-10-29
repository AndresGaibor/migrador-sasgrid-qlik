import { useEffect, useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Dialog } from "../components/Dialog";
import { Icon } from "../components/Icon";
import { notifyError, notifySuccess } from "../errors";
import {
  filterProjectsByFacets,
  filterProjectsByQuery,
  processingLabel,
  type ProjectSourceFilter,
  type ProjectStatusFilter,
} from "../project-workspace";
import type { Project } from "../types";
import { Load } from "./common";

export function ProjectsView({ go, startUpload = false }: { go: (h: string) => void; startUpload?: boolean }) {
  const q = useAsync(api.projects, []);
  const [projectName, setProjectName] = useState("");
  const [search, setSearch] = useState("");
  const [sort, setSort] = useState("recent");
  const [statusFilter, setStatusFilter] = useState<ProjectStatusFilter>("all");
  const [sourceFilter, setSourceFilter] = useState<ProjectSourceFilter>("all");
  const [uploadOpen, setUploadOpen] = useState(startUpload);
  const [uploading, setUploading] = useState(false);
  const [uploadIndex, setUploadIndex] = useState(0);
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);
  const [err, setErr] = useState<string>();
  const hasActiveProjects = q.data?.some((project) => project.processing?.status === "queued" || project.processing?.status === "running") ?? false;
  useEffect(() => {
    if (!hasActiveProjects) return;
    const timer = window.setInterval(q.reload, 2000);
    return () => window.clearInterval(timer);
  }, [hasActiveProjects, q.reload]);
  const openUpload = () => { setProjectName(""); setSelectedFiles([]); setErr(undefined); setUploadOpen(true); };
  const upload = async (event: React.FormEvent) => {
    event.preventDefault();
    if (uploading || selectedFiles.length === 0) return;
    const invalid = selectedFiles.filter((file) => !/\.(zip|sas|txt)$/i.test(file.name));
    if (invalid.length) {
      setErr(`Formato no admitido: ${invalid.map((file) => file.name).join(", ")}. Usa .zip, .sas o .txt.`);
      return;
    }
    setUploading(true);
    setErr(undefined);
    const created: string[] = [];
    const failures: string[] = [];
    try {
      for (const [index, file] of selectedFiles.entries()) {
        setUploadIndex(index + 1);
        const stem = file.name.replace(/\.(zip|sas|txt)$/i, "");
        const name = projectName.trim()
          ? selectedFiles.length === 1 ? projectName : `${projectName.trim()} ${stem}`
          : undefined;
        try {
          const result = await api.createProjectFromZip(file, name);
          created.push(result.project.id);
        } catch (error) {
          failures.push(`${file.name}: ${notifyError(error, "No se pudo crear el proyecto", "Revisa el archivo y vuelve a intentarlo.")}`);
        }
      }
      q.reload();
      if (created.length) {
        notifySuccess("Proyectos creados", `Se crearon ${created.length} de ${selectedFiles.length}; el análisis comenzó en segundo plano.`);
        if (created.length === 1 && failures.length === 0) {
          go(`/p/${created[0]}/resumen`);
          return;
        }
        setSelectedFiles([]);
      }
      if (failures.length) setErr(`No se pudieron subir algunos archivos:\n${failures.join("\n")}`);
      else setUploadOpen(false);
    } finally {
      setUploading(false);
    }
  };

  return <div className="projects-home">
    <div className="page-heading"><div><h1>Mis proyectos <span className="count">{q.data?.length ?? "—"}</span></h1><p className="subtitle">Abre un proyecto para continuar o sube archivos SAS para analizarlos.</p></div><button onClick={openUpload}><Icon name="upload" size={18} /> Nuevo proyecto</button></div>
    <section aria-labelledby="projects-title">
      <h2 id="projects-title" className="sr-only">Proyectos disponibles</h2>
      <div className="project-toolbar">
        <label className="search-field"><Icon name="search" size={18} /><input aria-label="Buscar proyectos" placeholder="Buscar por proyecto o archivo…" value={search} onChange={(event) => setSearch(event.target.value)} />{search && <button className="icon-button" aria-label="Limpiar búsqueda" onClick={() => setSearch("")}><Icon name="close" size={16} /></button>}</label>
        <label className="sort-field">Estado <select aria-label="Filtrar por estado" value={statusFilter} onChange={(event) => setStatusFilter(event.target.value as ProjectStatusFilter)}><option value="all">Todos</option><option value="processing">En proceso</option><option value="completed">Listos</option><option value="attention">Requieren atención</option><option value="waiting">Sin analizar</option></select></label>
        <label className="sort-field">Origen <select aria-label="Filtrar por origen" value={sourceFilter} onChange={(event) => setSourceFilter(event.target.value as ProjectSourceFilter)}><option value="all">Todos</option><option value="archive">ZIP</option><option value="individual">Archivo individual</option><option value="manual">Importación manual</option></select></label>
        <label className="sort-field">Ordenar por <select aria-label="Ordenar proyectos" value={sort} onChange={(event) => setSort(event.target.value)}><option value="recent">Actividad reciente</option><option value="name">Nombre: A–Z</option><option value="programs">Más programas</option></select></label>
      </div>
      <Load q={q}>{(projects) => {
        const filtered = filterProjectsByFacets(filterProjectsByQuery(projects, search), statusFilter, sourceFilter).sort((a, b) => {
          if (sort === "name") return a.name.localeCompare(b.name, "es");
          if (sort === "programs") return (b.manifest_summary?.programs ?? 0) - (a.manifest_summary?.programs ?? 0);
          const aActivity = a.processing?.updated_at ?? a.uploaded_at ?? a.created_at;
          const bActivity = b.processing?.updated_at ?? b.uploaded_at ?? b.created_at;
          return Date.parse(bActivity) - Date.parse(aActivity);
        });
        return projects.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={32} /></span><h3>Tu primer proyecto empieza aquí</h3><p>Sube un ZIP o un archivo SAS individual (.sas o .txt).</p><button onClick={openUpload}><Icon name="upload" size={18} /> Subir archivo y empezar</button><span className="empty-note">El análisis comienza automáticamente después de recibir el archivo.</span></div>
          : filtered.length === 0 ? <div className="empty-state"><Icon name="search" size={30} /><h3>No hay proyectos con estos filtros</h3><p>Cambia la búsqueda, el estado o el origen seleccionado.</p><button className="secondary" onClick={() => { setSearch(""); setStatusFilter("all"); setSourceFilter("all"); }}>Quitar filtros</button></div>
          : <><div className="project-grid">{filtered.map((project) => <ProjectCard key={project.id} project={project} />)}<button className="new-project-card" onClick={openUpload}><span><Icon name="plus" size={24} /></span><strong>Subir otro archivo</strong><small>Crear un proyecto independiente</small></button></div><p className="home-project-results" role="status">{filtered.length === projects.length ? `${projects.length} proyecto${projects.length === 1 ? "" : "s"}` : `${filtered.length} de ${projects.length} proyectos`}</p></>;
      }}</Load>
    </section>
    {q.data?.some((project) => !project.archive_name) && <div className="home-note"><Icon name="info" size={18} /><p>Los proyectos sin archivo de origen registrado conservan su importación manual. Cada archivo nuevo crea un proyecto independiente.</p></div>}
    {uploadOpen && <Dialog title="Crear proyecto desde archivos" onClose={() => { if (!uploading) { setUploadOpen(false); setSelectedFiles([]); setErr(undefined); } }}>
      <p className="muted">Selecciona uno o varios ZIP o programas SAS (.sas o .txt). Cada archivo creará un proyecto independiente.</p>
      <form onSubmit={upload}>
        <label>Archivos<input autoFocus type="file" multiple accept=".zip,.sas,.txt,application/zip,text/plain" disabled={uploading} onChange={(event) => { setSelectedFiles(Array.from(event.target.files ?? [])); setErr(undefined); }} /></label>
        {selectedFiles.length > 0 && <ul className="selected-zip-list" aria-label="Archivos seleccionados">{selectedFiles.map((file) => <li className="selected-zip" key={`${file.name}:${file.size}:${file.lastModified}`}><Icon name="file" size={18} /><span title={file.name}>{file.name}</span><small>{formatBytes(file.size)}</small></li>)}</ul>}
        <label>Nombre base <span className="muted">(opcional; se combina con cada archivo)</span><input value={projectName} onChange={(event) => setProjectName(event.target.value)} placeholder={selectedFiles[0]?.name.replace(/\.(zip|sas|txt)$/i, "") || "Se usará el nombre del archivo"} maxLength={120} disabled={uploading} /></label>
        {err && <p className="error" role="alert">{err}</p>}
        {uploading && <p className="loading-state" role="status"><span className="spinner" /> Subiendo archivo {uploadIndex} de {selectedFiles.length}…</p>}
        <div className="dialog-actions"><button type="button" className="secondary" disabled={uploading} onClick={() => { setUploadOpen(false); setSelectedFiles([]); setErr(undefined); }}>Cancelar</button><button disabled={uploading || selectedFiles.length === 0}><Icon name="upload" size={17} />{uploading ? "Subiendo…" : `Subir ${selectedFiles.length || ""} y analizar`}</button></div>
      </form>
    </Dialog>}
  </div>;
}

function ProjectCard({ project }: { project: Project }) {
  const summary = project.manifest_summary;
  const processing = project.processing;
  const isLegacy = !project.archive_name;
  const status = isLegacy ? "Proyecto existente · ZIP no registrado" : processing ? processingLabel(processing) : "Análisis pendiente";
  const tone = processing?.status === "completed" ? "ok" : processing?.status === "failed" ? "bad" : processing?.status === "interrupted" ? "warn" : processing && (processing.status === "running" || processing.status === "queued") ? "active" : "neutral";
  const activity = processing?.updated_at ?? project.uploaded_at ?? project.created_at;
  return <a className="project-card" href={`#/p/${project.id}/resumen`}>
    <div className="project-card-visual"><div className="mini-flow"><span><Icon name="file" size={19} /></span><i /><span className="flow-center"><Icon name="flow" size={23} /></span><i /><span><Icon name="check" size={19} /></span></div></div>
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
