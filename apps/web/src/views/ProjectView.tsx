import { DepsTab } from "./DepsTab";
import { ExportTab } from "./ExportTab";
import { ImportTab, InventoryTab } from "./InventoryTab";
import { PlansTab } from "./PlansTab";
import { ProgramsTab } from "./ProgramsTab";
import { SummaryTab } from "./SummaryTab";
import { link } from "./common";

const TABS: [string, string][] = [
  ["resumen", "Resumen"],
  ["importar", "Importar"],
  ["inventario", "Inventario"],
  ["programas", "Programas"],
  ["dependencias", "Dependencias"],
  ["planes", "Planes"],
  ["exportar", "Exportar"],
];

export function ProjectView({ id, tab, rest, go }: { id: string; tab: string; rest?: string; go: (h: string) => void }) {
  return (
    <>
      <nav className="tabs" aria-label="Secciones del proyecto">
        {TABS.map(([k, label]) => (
          <a key={k} href={link(id, k)} aria-current={tab === k ? "page" : undefined}>
            {label}
          </a>
        ))}
      </nav>
      {tab === "resumen" && <SummaryTab id={id} />}
      {tab === "importar" && <ImportTab id={id} go={go} />}
      {tab === "inventario" && <InventoryTab id={id} />}
      {tab === "programas" && <ProgramsTab id={id} file={rest} />}
      {tab === "dependencias" && <DepsTab id={id} />}
      {tab === "planes" && <PlansTab id={id} file={rest} />}
      {tab === "exportar" && <ExportTab id={id} />}
    </>
  );
}
