import { useState } from "react";
import { useHash } from "./hooks";
import { Dialog } from "./components/Dialog";
import { ErrorBoundary } from "./components/ErrorBoundary";
import { Icon } from "./components/Icon";
import { CatalogView } from "./views/CatalogView";
import { ProjectView } from "./views/ProjectView";
import { ProjectsView } from "./views/ProjectsView";
import { HomeView } from "./views/HomeView";
import { SettingsView } from "./views/SettingsView";
import { TranslatorView } from "./views/TranslatorView";
import { Toaster } from "sonner";

export function App() {
  const [hash, go] = useHash();
  const [help, setHelp] = useState(false);
  const m = hash.match(/^\/p\/([^/]+)(?:\/([^/]+))?(?:\/(.+))?$/);
  const catalog = hash === "/catalogo" || hash.startsWith("/catalogo/");
  const settings = hash === "/settings";
  const translator = hash === "/traductor";
  const projects = hash === "/projects" || hash === "/projects/nuevo";
  return (
    <>
      <a className="skip-link" href="#main-content" onClick={(e) => { e.preventDefault(); document.getElementById("main-content")?.focus(); }}>Saltar al contenido</a>
      <header className="app-header">
        <a href="#/" className="brand" aria-label="Migrador, ir al inicio"><span className="brand-symbol"><Icon name="flow" size={25} /></span><span>Migrador<span className="brand-caption">SAS Grid → Talend</span></span></a>
        <div id="project-header-context" className="project-header-context">{!m && <nav className="header-project-path" aria-label="Ubicación actual"><span>Espacio de trabajo</span><span className="header-project-section">{projects ? "Mis proyectos" : catalog ? "Catálogo Talend" : settings ? "Configuración" : translator ? "Laboratorio del traductor" : "Inicio"}</span></nav>}</div>
        <div className="header-actions"><button className="icon-button" onClick={() => setHelp(true)} aria-label="Abrir guía de ayuda" title="Guía de ayuda"><Icon name="help" /></button></div>
      </header>
      <aside className="sidebar">
        <div className="nav-caption">ESPACIO DE TRABAJO</div>
        <nav aria-label="Navegación principal">
          <a href="#/" aria-label="Inicio" title="Inicio" aria-current={hash === "/" ? "page" : undefined}><Icon name="home" /><span>Inicio</span></a>
          <a href="#/projects" aria-label="Mis proyectos" title="Mis proyectos" aria-current={projects || m ? "page" : undefined}><Icon name="grid" /><span>Mis proyectos</span></a>
          <a href="#/catalogo" aria-label="Catálogo Talend" title="Catálogo Talend" aria-current={catalog ? "page" : undefined}><Icon name="book" /><span>Catálogo Talend</span></a>
          <a href="#/traductor" aria-label="Traductor" title="Traductor" aria-current={translator ? "page" : undefined}><Icon name="file" /><span>Traductor</span></a>
          <a href="#/settings" aria-label="Configuración" title="Configuración" aria-current={settings ? "page" : undefined}><Icon name="settings" /><span>Configuración</span></a>
        </nav>
        <div className="sidebar-bottom"><span className="sidebar-footer">SAS Grid · Talend Studio</span></div>
      </aside>
      <main id="main-content" tabIndex={-1}>
        <ErrorBoundary key={hash}>
          {catalog ? (
            <CatalogView key={hash} name={hash.split("/")[2]} />
          ) : translator ? (
            <TranslatorView key={hash} />
          ) : settings ? (
            <SettingsView />
          ) : m ? (
            <ProjectView key={m[1]} id={m[1]} tab={m[2] ?? "resumen"} rest={m[3]} go={go} />
          ) : hash === "/" ? (
            <HomeView />
          ) : projects ? (
            <ProjectsView key={hash} go={go} startUpload={hash === "/projects/nuevo"} />
          ) : (
            <div className="empty-state"><span className="empty-icon"><Icon name="warning" size={30} /></span><h3>No encontramos esta página</h3><p>El enlace puede estar incompleto o haber cambiado. Vuelve a tus proyectos para continuar.</p><a className="button" href="#/projects">Volver a mis proyectos</a></div>
          )}
        </ErrorBoundary>
        <footer className="page-footer"><span className="muted">Análisis y plan de migración · SAS Grid → Talend</span></footer>
      </main>
      <Toaster position="top-right" richColors closeButton toastOptions={{ duration: 6000 }} />
      {help && <Dialog title="Tu primera migración, paso a paso" onClose={() => setHelp(false)}>
        <p className="muted">Cada proyecto reúne tus archivos y los resultados de su análisis.</p>
        <ol className="help-steps"><li><strong>Crea un proyecto y carga tus archivos</strong><p>Elige un nombre fácil de reconocer. Después, selecciona un archivo ZIP o un programa SAS.</p></li><li><strong>Analiza y explora</strong><p>En «Resumen», pulsa «Analizar proyecto». Podrás revisar los programas y ver cómo se conectan en «Flujo de datos».</p></li><li><strong>Prepara tu migración</strong><p>Genera un plan, revisa los pasos propuestos y exporta los resultados para trabajar con tu equipo.</p></li></ol>
        <div className="notice"><Icon name="info" /><span>La herramienta prepara un plan de trabajo. La construcción y validación final se realizan en Talend Studio.</span></div>
        <div className="dialog-actions"><button onClick={() => setHelp(false)}>Entendido <Icon name="check" size={18} /></button></div>
      </Dialog>}
    </>
  );
}
