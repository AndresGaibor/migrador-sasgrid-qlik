import { useState } from "react";
import { useHash } from "./hooks";
import { Dialog } from "./components/Dialog";
import { Icon } from "./components/Icon";
import { CatalogView } from "./views/CatalogView";
import { ProjectView } from "./views/ProjectView";
import { ProjectsView } from "./views/ProjectsView";
import { SettingsView } from "./views/SettingsView";

export function App() {
  const [hash, go] = useHash();
  const [help, setHelp] = useState(false);
  const m = hash.match(/^\/p\/([^/]+)(?:\/([^/]+))?(?:\/(.+))?$/);
  const catalog = hash.startsWith("/catalogo");
  const settings = hash === "/settings";
  return (
    <>
      <a className="skip-link" href="#main-content" onClick={(e) => { e.preventDefault(); document.getElementById("main-content")?.focus(); }}>Saltar al contenido</a>
      <header className="app-header">
        <a href="#/" className="brand" aria-label="Migrador, ir al inicio"><span className="brand-symbol"><Icon name="flow" size={25} /></span><span>Migrador<span className="brand-caption">SAS Grid → Talend</span></span></a>
        <div className="header-context">Espacio de migración</div>
        <div className="header-actions"><span className="workspace-label">Mi espacio de trabajo</span><button className="icon-button" onClick={() => setHelp(true)} aria-label="Abrir guía de ayuda" title="Guía de ayuda"><Icon name="help" /></button><span className="workspace-avatar" aria-hidden="true">M</span></div>
      </header>
      <aside className="sidebar">
        <div className="nav-caption">ESPACIO DE TRABAJO</div>
        <nav aria-label="Navegación principal">
          <a href="#/" aria-label="Mis proyectos" title="Mis proyectos" aria-current={!catalog && !settings ? "page" : undefined}><Icon name="grid" /><span>Mis proyectos</span></a>
          <a href="#/catalogo" aria-label="Catálogo Talend" title="Catálogo Talend" aria-current={catalog ? "page" : undefined}><Icon name="book" /><span>Catálogo Talend</span></a>
          <a href="#/settings" aria-label="Configuración" title="Configuración" aria-current={settings ? "page" : undefined}><Icon name="settings" /><span>Configuración</span></a>
        </nav>
        <div className="sidebar-bottom"><div className="sidebar-tip"><span className="tip-icon"><Icon name="help" /></span><strong>Te acompañamos</strong><p>De tus archivos SAS a un plan de migración, paso a paso.</p><button className="text-button" onClick={() => setHelp(true)}>Ver guía rápida <Icon name="arrow" size={16} /></button></div><span className="sidebar-footer">SAS Grid · Talend Studio</span></div>
      </aside>
      <main id="main-content" tabIndex={-1}>
        {catalog ? (
          <CatalogView key={hash} name={hash.split("/")[2]} />
        ) : settings ? (
          <SettingsView />
        ) : m ? (
          <ProjectView key={m[1]} id={m[1]} tab={m[2] ?? "resumen"} rest={m[3]} go={go} />
        ) : (
          <ProjectsView go={go} />
        )}
        <footer className="page-footer"><Icon name="flow" size={16} /> Tu migración, con una ruta clara.</footer>
      </main>
      {help && <Dialog title="Tu primera migración, paso a paso" onClose={() => setHelp(false)}>
        <p className="muted">Cada proyecto reúne tus archivos y los resultados de su análisis.</p>
        <ol className="help-steps"><li><strong>Crea un proyecto y carga tus archivos</strong><p>Elige un nombre fácil de reconocer. Después, selecciona un archivo ZIP o un programa SAS.</p></li><li><strong>Analiza y explora</strong><p>En «Resumen», pulsa «Analizar proyecto». Podrás revisar los programas y ver cómo se conectan en «Flujo de datos».</p></li><li><strong>Prepara tu migración</strong><p>Genera un plan, revisa los pasos propuestos y exporta los resultados para trabajar con tu equipo.</p></li></ol>
        <div className="notice"><Icon name="info" /><span>La herramienta prepara un plan de trabajo. La construcción y validación final se realizan en Talend Studio.</span></div>
        <div className="dialog-actions"><button onClick={() => setHelp(false)}>Entendido <Icon name="check" size={18} /></button></div>
      </Dialog>}
    </>
  );
}
