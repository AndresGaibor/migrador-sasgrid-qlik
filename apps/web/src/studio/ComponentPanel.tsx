import { useId, useState } from "react";
import { ComponentIcon } from "../components/ComponentIcon";
import { Dialog } from "../components/Dialog";
import { groupByRow, tabProgress, visibleParams } from "./panel-model";
import { ParamField } from "./ParamField";
import { SchemaEditor } from "./SchemaEditor";
import { schemaColumnsFromRows } from "./schema-model";
import { STUDIO_TABS, StudioTabs } from "./StudioTabs";
import type { ComponentTab, DoneFields, GuideValues, PanelsSnapshot } from "./panel-types";
import "./studio.css";

export type ComponentPanelProps = {
  /** Nombre del componente Talend, por ejemplo tFileInputDelimited. */
  component: string;
  /** Etiqueta del paso de la guía, que se muestra en la cabecera. */
  stepLabel?: string;
  panels: PanelsSnapshot;
  /** Sugerencias de la guía por nombre de parámetro. */
  values: GuideValues;
  /** Campos marcados como hechos. */
  doneFields: DoneFields;
  onFieldDone: (name: string, done: boolean) => void;
  /**
   * Si se pasa, el botón «...» de SCHEMA_TYPE llama a este callback y el integrador muestra el editor.
   * Si no se pasa, el panel abre su propia ventana con SchemaEditor.
   */
  onOpenSchema?: (paramName: string) => void;
  /** Pestaña inicial (por defecto Basic settings). */
  initialTab?: ComponentTab;
};

const MESSAGES: Record<Exclude<ComponentTab, "basic" | "advanced">, string> = {
  dynamic: "Los ajustes dinámicos (Dynamic settings) se configuran en Studio. La guía no sugiere valores para esta pestaña.",
  view: "La pestaña View define el nombre que se ve en el lienzo (Label format). El nombre sugerido aparece en las instrucciones del paso.",
  documentation: "La documentación oficial del componente está enlazada desde el paso de la guía.",
};

// Réplica del panel inferior de Talend Studio: cabecera, filas de parámetros y pestañas abajo.
export function ComponentPanel({ component, stepLabel, panels, values, doneFields, onFieldDone, onOpenSchema, initialTab = "basic" }: ComponentPanelProps) {
  const idPrefix = useId();
  const [tab, setTab] = useState<ComponentTab>(initialTab);
  const [schemaParam, setSchemaParam] = useState<string | null>(null);

  const spec = panels.components[component];
  if (!spec) {
    return (
      <section className="studio-panel" aria-label={`Panel de ${component}`}>
        <p role="alert" className="studio-message">No hay panel para «{component}» en el snapshot de Talend.</p>
      </section>
    );
  }

  const isFieldTab = tab === "basic" || tab === "advanced";
  const params = tab === "basic" ? spec.tabs.basic : tab === "advanced" ? spec.tabs.advanced : [];
  const rows = groupByRow(visibleParams(params, values));
  const progress = tabProgress(params, values, doneFields);
  const pct = progress.total === 0 ? 0 : Math.round((progress.done / progress.total) * 100);

  const openSchema = (name: string) => {
    if (onOpenSchema) onOpenSchema(name);
    else setSchemaParam(name);
  };

  return (
    <section className="studio-panel" aria-label={`Panel de ${component}`}>
      <header className="studio-header">
        <ComponentIcon name={component} className="studio-header-icon" />
        <div className="studio-header-text">
          <strong className="studio-component-name">{component}</strong>
          {spec.label && <span className="studio-component-label">{spec.label}</span>}
        </div>
        {stepLabel && <span className="studio-step-label">{stepLabel}</span>}
      </header>

      <div className="studio-body" role="tabpanel" id={`${idPrefix}-panel`} aria-labelledby={`${idPrefix}-tab-${tab}`}>
        {isFieldTab && (
          <div className="studio-progress">
            <span className="studio-progress-text">
              {progress.total === 0 ? "Sin campos con sugerencia en esta pestaña" : `${progress.done} de ${progress.total} campos`}
            </span>
            {progress.total > 0 && (
              <div className="studio-progress-bar" role="progressbar" aria-label="Progreso de la pestaña" aria-valuemin={0} aria-valuemax={progress.total} aria-valuenow={progress.done}>
                <div className="studio-progress-fill" style={{ width: `${pct}%` }} />
              </div>
            )}
          </div>
        )}

        {isFieldTab ? (
          <div className="studio-rows">
            {rows.length === 0 && <p className="studio-muted">Este componente no tiene campos visibles en esta pestaña.</p>}
            {rows.map((row) => (
              <div className="studio-row" key={row.map((p) => p.name).join("|")}>
                {row.map((param) => (
                  <ParamField
                    key={param.name}
                    param={param}
                    idPrefix={idPrefix}
                    values={values}
                    done={doneFields[param.name] === true}
                    active={progress.active === param.name}
                    onDone={onFieldDone}
                    onOpenSchema={openSchema}
                  />
                ))}
              </div>
            ))}
          </div>
        ) : (
          <p className="studio-message">{MESSAGES[tab]}</p>
        )}
      </div>

      <StudioTabs tabs={STUDIO_TABS} active={tab} onChange={setTab} idPrefix={idPrefix} />

      {schemaParam && !onOpenSchema && (
        <Dialog title={`Esquema de ${schemaParam}`} onClose={() => setSchemaParam(null)}>
          <SchemaEditor columns={schemaColumnsFromRows(values[schemaParam]?.rows ?? [])} />
        </Dialog>
      )}
    </section>
  );
}
