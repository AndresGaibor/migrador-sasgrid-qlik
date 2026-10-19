import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon, type IconName } from "../components/Icon";
import { DepsTab } from "./DepsTab";
import { ExportTab } from "./ExportTab";
import { ImportTab, InventoryTab } from "./InventoryTab";
import { PlansTab } from "./PlansTab";
import { ProgramsTab } from "./ProgramsTab";
import { SummaryTab } from "./SummaryTab";
import { link } from "./common";

const TABS: [string, string, IconName][] = [
  ["resumen", "Resumen", "chart"], ["importar", "Cargar archivos", "upload"],
  ["inventario", "Mis archivos", "folder"], ["programas", "Programas", "file"],
  ["dependencias", "Flujo de datos", "flow"], ["planes", "Plan de migración", "list"],
  ["exportar", "Exportar", "download"],
];

export function ProjectView({ id, tab, rest, go }: { id: string; tab: string; rest?: string; go: (h: string) => void }) {
  const projects = useAsync(api.projects, [id]);
  const project = projects.data?.find((p) => p.id === id);
  const active = TABS.some(([k]) => k === tab) ? tab : "resumen";
  return <>
    <div className="breadcrumb"><a href="#/">Mis proyectos</a><Icon name="chevron" size={13} /><span>{project?.name ?? "Proyecto"}</span></div>
    <div className="project-heading"><span className="project-heading-icon"><Icon name="flow" size={26} /></span><div><h1>{project?.name ?? "Mi proyecto"}</h1><p>De tus programas SAS a un plan de trabajo en Talend.</p></div><span className="badge neutral">SAS Grid → Talend</span></div>
    <nav className="tabs" aria-label="Secciones del proyecto">{TABS.map(([k, label, icon]) => <a key={k} href={link(id, k)} aria-current={active === k ? "page" : undefined}><Icon name={icon} size={17} />{label}</a>)}</nav>
    <div className="tab-content" key={active + (rest ?? "")}>
      {active === "resumen" && <SummaryTab id={id} />}
      {active === "importar" && <ImportTab id={id} go={go} />}
      {active === "inventario" && <InventoryTab id={id} />}
      {active === "programas" && <ProgramsTab id={id} file={rest} />}
      {active === "dependencias" && <DepsTab id={id} />}
      {active === "planes" && <PlansTab id={id} file={rest} />}
      {active === "exportar" && <ExportTab id={id} />}
    </div>
  </>;
}
