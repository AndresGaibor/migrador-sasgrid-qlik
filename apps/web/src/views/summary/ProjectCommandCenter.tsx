import { ApiError, api } from "../../api";
import { useAsync } from "../../hooks";
import { Icon } from "../../components/Icon";
import { ProjectStepper } from "../../components/ProjectStepper";
import { nextActionHref, pendingPanelState } from "../../project-progress";
import { Load } from "../common";
import { PendingPanel } from "./PendingPanel";

export function ProjectCommandCenter({ id, refreshKey = 0 }: { id: string; refreshKey?: number }) {
  const progress = useAsync(() => api.progress(id), [id, refreshKey]);
  const guidesDone = progress.data?.stages.some((stage) => stage.key === "guides" && stage.status === "done") ?? false;
  const pending = useAsync(async () => {
    if (!guidesDone) return undefined;
    try { return await api.pendingSummary(id); }
    catch (error) {
      if (error instanceof ApiError && error.status === 409) return [];
      throw error;
    }
  }, [id, refreshKey, guidesDone]);
  const pendingState = pendingPanelState(guidesDone, pending);
  return <section className="command-center" aria-label="Centro de mando del proyecto">
    <Load q={progress}>{(p) => {
      const href = nextActionHref(id, p.next);
      return <>
        <ProjectStepper stages={p.stages} />
        {p.next && href
          ? <div className="command-next">
              <a className="button" href={href}>{p.next.label} <Icon name="arrow" size={16} /></a>
              <p className="muted">{p.next.reason}</p>
            </div>
          : <div className="notice" role="status"><Icon name="check" /><span>Proyecto listo: no quedan acciones pendientes.</span></div>}
      </>;
    }}</Load>
    {pendingState === "loading" && <div className="loading-state" role="status"><span className="spinner" /> Cargando pendientes…</div>}
    {pendingState === "ready" && <Load q={pending}>{(groups) => groups ? <PendingPanel id={id} groups={groups} /> : null}</Load>}
  </section>;
}
