import { useState, type FormEvent } from "react";
import { createPortal } from "react-dom";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon, type IconName } from "../components/Icon";
import { Dialog } from "../components/Dialog";
import { DepsTab } from "./DepsTab";
import { ExportTab } from "./ExportTab";
import { ImportTab, InventoryTab } from "./InventoryTab";
import { PlansTab } from "./PlansTab";
import { ProgramsTab } from "./ProgramsTab";
import { SummaryTab } from "./SummaryTab";
import { link, Load } from "./common";
import { ProjectProcessingStatus } from "../components/ProjectProcessingStatus";

const TABS: [string, string, IconName][] = [
  ["resumen", "Resumen", "chart"], ["importar", "Cargar archivos", "upload"],
  ["inventario", "Mis archivos", "folder"], ["programas", "Programas", "file"],
  ["dependencias", "Dependencias", "flow"], ["planes", "Plan de migración", "list"],
  ["exportar", "Exportar", "download"],
];

export function ProjectNavigation({ id, active, hasArchive }: { id: string; active: string; hasArchive: boolean }) {
  const primary = TABS.filter(([key]) => ["resumen", "programas", "dependencias", "planes"].includes(key));
  const secondary = TABS.filter(([key]) => ["inventario", "exportar", ...(!hasArchive ? ["importar"] : [])].includes(key));
  const secondaryActive = secondary.find(([key]) => key === active);
  return <nav className="project-navigation" aria-label="Secciones del proyecto">
    <div className="tabs">{primary.map(([key, label, icon]) => <a key={key} href={link(id, key)} aria-current={active === key ? "page" : undefined}><Icon name={icon} size={17} />{label}</a>)}</div>
    <details className="project-more" key={active} onBlur={(event) => { if (!event.currentTarget.contains(event.relatedTarget)) event.currentTarget.open = false; }} onKeyDown={(event) => { if (event.key === "Escape") { event.preventDefault(); event.currentTarget.open = false; event.currentTarget.querySelector("summary")?.focus(); } }}>
      <summary className={secondaryActive ? "is-active" : undefined}>{secondaryActive?.[1] ?? "Más"}<Icon name="chevron" size={15} /></summary>
      <div className="project-more-links">{secondary.map(([key, label, icon]) => <a key={key} href={link(id, key)} aria-current={active === key ? "page" : undefined} onClick={(event) => { const menu = event.currentTarget.closest("details"); if (menu) menu.open = false; }}><Icon name={icon} size={17} /><span>{label}</span></a>)}</div>
    </details>
  </nav>;
}

export function ProjectView({ id, tab, rest, go }: { id: string; tab: string; rest?: string; go: (h: string) => void }) {
  const projects = useAsync(api.projects, [id]);
  const [processingRefresh, setProcessingRefresh] = useState(0);
  const [deleteOpen, setDeleteOpen] = useState(false);
  const [deleteConfirmation, setDeleteConfirmation] = useState("");
  const [deleteError, setDeleteError] = useState("");
  const [deleting, setDeleting] = useState(false);
  if (!projects.data) return <Load q={projects}>{() => null}</Load>;
  const project = projects.data.find((p) => p.id === id);
  if (!project) return <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={32} /></span><h3>No encontramos este proyecto</h3><p>Puede que se haya eliminado o que el enlace ya no sea válido. Vuelve a tus proyectos para elegir otro.</p><a className="button secondary" href="#/projects">Volver a mis proyectos</a></div>;
  const active = TABS.some(([k]) => k === tab) ? tab : "resumen";
  const header = document.getElementById("project-header-context");
  const deletionBlocked = project?.processing?.status === "queued" || project?.processing?.status === "running";

  const submitDeletion = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!project || deletionBlocked || deleteConfirmation !== project.name || deleting) return;
    setDeleting(true);
    setDeleteError("");
    try {
      await api.deleteProject(id, deleteConfirmation);
      go("/");
    } catch (error) {
      setDeleteError(error instanceof Error ? error.message : "No se pudo eliminar el proyecto.");
    } finally {
      setDeleting(false);
    }
  };

  return <>
    {header && createPortal(<><nav className="header-project-path" aria-label="Proyecto actual"><a href="#/projects">Mis proyectos</a><Icon name="chevron" size={14} /><a className="header-project-name" href={link(id, "resumen")}>{project.name}</a><span className="header-project-section">{TABS.find(([key]) => key === active)?.[1]}</span></nav><a className="header-project-files" href={link(id, "inventario")}><Icon name="folder" size={16} />Archivos del proyecto</a></>, header)}
    <div className="breadcrumb"><a href="#/projects">Mis proyectos</a><Icon className="project-breadcrumb-separator" name="chevron" size={13} /><span className="project-breadcrumb-current">{project.name}</span></div>
    <div className="project-heading"><span className="project-heading-icon"><Icon name="flow" size={26} /></span><div><h1>{project.name}</h1><p>De tus programas SAS a un plan de trabajo en Talend.</p></div><div className="project-heading-actions"><span className="badge neutral">SAS Grid → Talend</span><button type="button" className="button-danger-outline" onClick={() => { setDeleteConfirmation(""); setDeleteError(""); setDeleteOpen(true); }}>Eliminar proyecto</button></div></div>
    <div className="project-context">
      <ProjectProcessingStatus projectId={id} archiveName={project.archive_name} onRetry={() => setProcessingRefresh((value) => value + 1)} />
      <section className="project-archive-card" aria-label="Identidad del ZIP de origen">
        <div className="project-archive-icon"><Icon name={project.archive_name ? "file" : "folder"} size={21} /></div>
        <div className="project-archive-main"><span className="archive-origin-label">Archivo de origen</span><strong title={project.archive_name ?? undefined}>{project.archive_name ?? "Importación manual"}</strong><small>{project.uploaded_at ? `Subido ${new Date(project.uploaded_at).toLocaleString("es", { dateStyle: "medium", timeStyle: "short" })}` : "ZIP no registrado"}</small></div>
        {project.manifest_summary && <div className="project-archive-counts"><span><strong>{project.manifest_summary.programs}</strong> programas SAS</span><span><strong>{project.manifest_summary.folders}</strong> carpetas</span><span><strong>{project.manifest_summary.files}</strong> archivos</span></div>}
      </section>
    </div>
    <ProjectNavigation id={id} active={active} hasArchive={Boolean(project.archive_name)} />
    <div className="tab-content" key={active + (rest ?? "")}>
      {active === "resumen" && <SummaryTab id={id} refreshKey={processingRefresh} />}
      {active === "importar" && (project.archive_name ? <div className="empty-state"><Icon name="folder" size={30} /><h2>Este proyecto ya tiene un ZIP de origen</h2><p>Para analizar otros archivos, crea un proyecto independiente. Los archivos y el progreso de este proyecto se conservan.</p><a className="button" href="#/projects/nuevo"><Icon name="upload" size={17} />Crear proyecto desde otro ZIP</a></div> : <ImportTab id={id} go={go} />)}
      {active === "inventario" && <InventoryTab id={id} />}
      {active === "programas" && <ProgramsTab id={id} file={rest} />}
      {active === "dependencias" && <DepsTab id={id} />}
      {active === "planes" && <PlansTab id={id} file={rest} />}
      {active === "exportar" && <ExportTab id={id} />}
    </div>
    {deleteOpen && project && <Dialog title={`Eliminar ${project.name}`} onClose={() => setDeleteOpen(false)}>
      <form onSubmit={submitDeletion}>
        <p>Se eliminarán del portal el proyecto, los archivos extraídos, el análisis, los planes, las exportaciones y su historial.</p>
        <p><strong>Los Jobs y contextos de Talend no se eliminarán.</strong></p>
        <p className="delete-project-note">El borrado se bloqueará si el análisis o un lote de Talend están activos.</p>
        <label>Escribe el nombre exacto del proyecto para confirmar
          <input value={deleteConfirmation} onChange={(event) => setDeleteConfirmation(event.target.value)} placeholder={project.name} autoComplete="off" />
        </label>
        {deleteError && <p className="error" role="alert">{deleteError}</p>}
        <div className="dialog-actions">
          <button type="button" className="secondary" disabled={deleting} onClick={() => setDeleteOpen(false)}>Cancelar</button>
          <button type="submit" className="button-danger" disabled={deleting || deletionBlocked || deleteConfirmation !== project.name}>
            {deleting ? "Eliminando…" : "Eliminar proyecto"}
          </button>
        </div>
      </form>
    </Dialog>}
  </>;
}
