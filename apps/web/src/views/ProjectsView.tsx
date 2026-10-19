import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Dialog } from "../components/Dialog";
import { Icon } from "../components/Icon";
import { Load } from "./common";

export function ProjectsView({ go }: { go: (h: string) => void }) {
  const q = useAsync(api.projects, []);
  const [name, setName] = useState("");
  const [search, setSearch] = useState("");
  const [sort, setSort] = useState("recent");
  const [creating, setCreating] = useState(false);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const openCreate = () => { setName(""); setErr(undefined); setCreating(true); };
  const create = async (e: React.FormEvent) => {
    e.preventDefault();
    if (busy || !name.trim()) return;
    setBusy(true);
    setErr(undefined);
    try {
      const p = await api.createProject(name.trim());
      go(`/p/${p.id}/importar`);
    } catch (x) {
      setErr((x as Error).message);
    } finally {
      setBusy(false);
    }
  };
  return <>
    <div className="breadcrumb"><Icon name="grid" size={15} /> Espacio de trabajo <Icon name="chevron" size={13} /><span>Mis proyectos</span></div>
    <div className="page-heading"><div><div className="eyebrow">TODO EMPIEZA CON UN PROYECTO</div><h1>Tu próximo paso, más claro.</h1><p className="subtitle">Organiza tus programas SAS y prepara su migración a Talend en un solo lugar.</p></div><button onClick={openCreate}><Icon name="plus" size={18} /> Nuevo proyecto</button></div>
    <section className="journey" aria-labelledby="journey-title">
      <div className="journey-heading"><span className="eyebrow">DE SAS A TALEND</span><h2 id="journey-title">Una ruta sencilla para tu migración</h2><p>Tú eliges los archivos. Nosotros te ayudamos a entender el camino.</p></div>
      <ol className="journey-steps">
        <li><span className="journey-icon"><Icon name="upload" size={24} /></span><div><span className="step-label">PASO 01</span><h3>Carga tus archivos</h3><p>Reúne tus programas SAS en un ZIP.</p></div></li>
        <li><span className="journey-icon"><Icon name="chart" size={24} /></span><div><span className="step-label">PASO 02</span><h3>Comprende tu proyecto</h3><p>Explora el análisis y las conexiones.</p></div></li>
        <li><span className="journey-icon"><Icon name="flow" size={24} /></span><div><span className="step-label">PASO 03</span><h3>Prepara la migración</h3><p>Revisa y exporta tu plan de trabajo.</p></div></li>
      </ol>
    </section>
    <section aria-labelledby="projects-title">
      <div className="section-heading"><h2 id="projects-title">Mis proyectos <span className="count">{q.data?.length ?? "—"}</span></h2><span className="muted">Tu trabajo, en un solo lugar</span></div>
      <div className="project-toolbar">
        <label className="search-field"><Icon name="search" size={18} /><input aria-label="Buscar proyectos" placeholder="Buscar un proyecto..." value={search} onChange={(e) => setSearch(e.target.value)} />{search && <button className="icon-button" aria-label="Limpiar búsqueda" onClick={() => setSearch("")}><Icon name="close" size={16} /></button>}</label>
        <label className="sort-field">Ordenar por <select value={sort} onChange={(e) => setSort(e.target.value)}><option value="recent">Más recientes</option><option value="name">Nombre: A–Z</option></select></label>
      </div>
      <Load q={q}>{(ps) => {
        const filtered = ps.filter((p) => p.name.toLocaleLowerCase("es").includes(search.trim().toLocaleLowerCase("es"))).sort((a, b) => sort === "name" ? a.name.localeCompare(b.name, "es") : Date.parse(b.created_at) - Date.parse(a.created_at));
        return ps.length === 0 ? <div className="empty-state"><span className="empty-icon"><Icon name="folder" size={32} /></span><h3>Tu primer proyecto empieza aquí</h3><p>Crea un espacio para tus archivos y descubre qué necesitas para migrarlos.</p><button onClick={openCreate}><Icon name="plus" size={18} /> Crear mi primer proyecto</button><span className="empty-note">Solo necesitas un nombre para empezar.</span></div>
          : filtered.length === 0 ? <div className="empty-state"><Icon name="search" size={30} /><h3>No encontramos ese proyecto</h3><p>Prueba con otro nombre o limpia la búsqueda.</p><button className="secondary" onClick={() => setSearch("")}>Ver todos los proyectos</button></div>
          : <div className="project-grid">{filtered.map((p) => <a className="project-card" key={p.id} href={`#/p/${p.id}/resumen`}>
              <div className="project-card-visual"><span className="project-type">SAS → TALEND</span><div className="mini-flow"><span><Icon name="file" size={24} /></span><i /><span className="flow-center"><Icon name="flow" size={28} /></span><i /><span><Icon name="check" size={24} /></span></div></div>
              <div className="project-card-body"><h3>{p.name}</h3><p><Icon name="clock" size={14} /> Creado el {new Date(p.created_at).toLocaleDateString("es", { day: "numeric", month: "short", year: "numeric" })}</p><div className="project-card-action"><span>Abrir proyecto</span><Icon name="arrow" size={18} /></div></div>
            </a>)}<button className="new-project-card" onClick={openCreate}><span><Icon name="plus" size={26} /></span><strong>Nuevo proyecto</strong><small>Empieza otra migración</small></button></div>;
      }}</Load>
    </section>
    <div className="home-note"><Icon name="info" size={18} /><p>¿Primera vez aquí? Crea un proyecto y sigue los pasos. Puedes consultar la <strong>guía rápida</strong> en el menú lateral.</p></div>
    {creating && <Dialog title="Crea tu nuevo proyecto" onClose={() => setCreating(false)}><p className="muted">Dale un nombre fácil de reconocer. En el siguiente paso podrás cargar tus archivos SAS.</p><form onSubmit={create}><label>Nombre del proyecto<input autoFocus value={name} onChange={(e) => setName(e.target.value)} placeholder="Ej. Ventas diarias" required maxLength={120} disabled={busy} /></label>{err && <p className="error" role="alert">{err}</p>}<div className="dialog-actions"><button type="button" className="secondary" disabled={busy} onClick={() => setCreating(false)}>Cancelar</button><button disabled={busy || !name.trim()}>{busy ? "Creando proyecto…" : "Crear y cargar archivos"}<Icon name="arrow" size={18} /></button></div></form></Dialog>}
  </>;
}
