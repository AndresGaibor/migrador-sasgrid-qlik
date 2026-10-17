import { useHash } from "./hooks";
import { CatalogView } from "./views/CatalogView";
import { ProjectView } from "./views/ProjectView";
import { ProjectsView } from "./views/ProjectsView";
import { SettingsView } from "./views/SettingsView";

export function App() {
  const [hash, go] = useHash();
  const m = hash.match(/^\/p\/([^/]+)(?:\/([^/]+))?(?:\/(.+))?$/);
  return (
    <>
      <header className="bar">
        <a href="#/" className="brand">
          SAS Grid → Talend
        </a>
        <nav>
          <a href="#/">Proyectos</a>
          <a href="#/catalogo">Catálogo Talend</a>
          <a href="#/settings">Ajustes</a>
        </nav>
      </header>
      <main>
        {hash.startsWith("/catalogo") ? (
          <CatalogView name={hash.split("/")[2]} />
        ) : hash === "/settings" ? (
          <SettingsView />
        ) : m ? (
          <ProjectView id={m[1]} tab={m[2] ?? "resumen"} rest={m[3]} go={go} />
        ) : (
          <ProjectsView go={go} />
        )}
      </main>
    </>
  );
}
