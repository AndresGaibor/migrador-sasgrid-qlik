import { useEffect, useMemo, useState } from "react";
import "./studio-compact.css";
import { api } from "../api";
import { notifyError } from "../errors";
import type { JobPart, Step } from "../types";
import { ComponentPanel } from "./ComponentPanel";
import { JobCanvas } from "./JobCanvas";
import type { DoneFields, PanelsSnapshot } from "./panel-types";
import { effectiveComponent, jobCanvas, stepGuideValues } from "./step-adapter";

// El snapshot pesa cientos de KB y no cambia durante la sesión: se pide una sola vez.
let snapshotPromise: Promise<PanelsSnapshot | null> | undefined;
function loadPanels(): Promise<PanelsSnapshot | null> {
  snapshotPromise ??= api.componentPanels().catch(() => { snapshotPromise = undefined; return null; });
  return snapshotPromise;
}

export function usePanels(): PanelsSnapshot | null {
  const [panels, setPanels] = useState<PanelsSnapshot | null>(null);
  useEffect(() => { let alive = true; void loadPanels().then((p) => alive && setPanels(p)); return () => { alive = false; }; }, []);
  return panels;
}

/** ¿Hay panel de Studio para este paso? Sirve para plegar las instrucciones en texto que lo repiten. */
export function useHasPanel(step: Step): boolean {
  const panels = usePanels();
  return Boolean(panels?.components[effectiveComponent(step)]);
}

/** Panel de configuración con el aspecto de Talend Studio. Si el componente no está en el snapshot, no muestra nada. */
export function StudioStepView({ step, onFieldDone }: { step: Step; onFieldDone?: (stepId: string, field: string, done: boolean) => Promise<void> }) {
  const panels = usePanels();
  const values = useMemo(() => stepGuideValues(step), [step]);
  const [done, setDone] = useState<DoneFields>(step.field_done ?? {});
  useEffect(() => setDone(step.field_done ?? {}), [step.id, step.field_done]);
  const component = effectiveComponent(step);
  if (!panels?.components[component]) return null;
  const change = (field: string, value: boolean) => {
    setDone((d) => ({ ...d, [field]: value }));
    onFieldDone?.(step.id, field, value).catch((error: unknown) => {
      setDone((d) => ({ ...d, [field]: !value }));
      notifyError(error, "No se pudo guardar el campo");
    });
  };
  return <section className="studio-step" aria-label={`Configuración de ${component} como en Talend Studio`}>
    <ComponentPanel component={component} stepLabel={step.purpose} panels={panels} values={values} doneFields={done} onFieldDone={change} />
  </section>;
}

/** Diagrama del Job: los componentes, sus conexiones y cuáles van quedando listos. */
export function StudioJobCanvas({ steps, selectedId, onSelect }: { steps: Step[]; selectedId?: string | null; onSelect?: (id: string) => void }) {
  const { nodes, edges } = useMemo(() => jobCanvas(steps), [steps]);
  if (nodes.length < 2) return null;
  return <JobCanvas nodes={nodes} edges={edges} selectedId={selectedId} onSelect={onSelect} />;
}

/** Un lienzo por parte del Job: así cada diagrama cabe en pantalla y se parece a lo que se arma en Studio. */
export function StudioJobMaps({ steps, parts, onSelect }: { steps: Step[]; parts?: JobPart[]; onSelect?: (id: string) => void }) {
  const groups = parts && parts.length > 1
    ? parts.map((part) => ({ key: part.name, title: `${part.title} · ${part.component_count} componentes`, steps: steps.filter((s) => part.step_ids.includes(s.id)) }))
    : [{ key: "job", title: "", steps }];
  const shown = groups.filter((g) => g.steps.length > 1);
  if (shown.length === 0) return null;
  return <details className="panel studio-canvas-panel" open={shown.length === 1}>
    <summary><b>Mapa del Job</b> <span className="muted">Así debe quedar el lienzo en Talend Studio. Pulsa un componente para ir a su paso.</span></summary>
    {shown.map((g) => <div key={g.key} className="studio-canvas-part">
      {g.title && <h4>{g.title}</h4>}
      <StudioJobCanvas steps={g.steps} onSelect={onSelect} />
    </div>)}
  </details>;
}
