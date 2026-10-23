import { useEffect, useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { processingLabel } from "../project-workspace";
import type { ProjectProcessing } from "../types";
import { Icon } from "./Icon";

export function ProjectProcessingStatus({
  projectId,
  archiveName,
  onRetry,
}: {
  projectId: string;
  archiveName: string | null | undefined;
  onRetry?: () => void;
}) {
  const state = useAsync(() => api.processing(projectId), [projectId]);
  const [retrying, setRetrying] = useState(false);
  const [retryError, setRetryError] = useState<string>();

  useEffect(() => {
    if (!state.data || !isActive(state.data.status)) return;
    const timer = window.setInterval(state.reload, 1500);
    return () => window.clearInterval(timer);
  }, [state.data?.status, state.reload]);

  if (!archiveName) {
    return <div className="project-processing legacy" role="status"><Icon name="info" size={18} /><span><strong>Proyecto existente</strong> · No tiene un ZIP de origen registrado. Puedes continuar con su flujo de importación manual.</span></div>;
  }

  const processing = state.data;
  const status = processing?.status;
  const tone = status === "completed" ? "ok" : status === "failed" ? "bad" : status === "interrupted" ? "warn" : status ? "active" : "neutral";
  const retry = async () => {
    setRetrying(true);
    setRetryError(undefined);
    try {
      await api.retryProcessing(projectId);
      onRetry?.();
      state.reload();
    } catch (error) {
      setRetryError((error as Error).message);
    } finally {
      setRetrying(false);
    }
  };

  return (
    <section className={`project-processing ${tone}`} aria-live="polite" aria-busy={Boolean(status && isActive(status))}>
      <div className="project-processing-icon">{status && isActive(status) ? <span className="spinner" /> : <Icon name={status === "completed" ? "check" : status === "failed" ? "warning" : "clock"} size={19} />}</div>
      <div className="project-processing-copy">
        <div className="project-processing-title"><strong>{state.loading && !processing ? "Consultando estado del proyecto…" : state.error && !processing ? "Estado no disponible" : processing ? processingLabel(processing) : "Análisis en cola"}</strong><span className={`project-status-pill ${tone}`}>{status ? statusLabel(status) : state.error ? "Sin conexión" : "En cola"}</span></div>
        <p>{processing?.message ?? (state.loading ? "Recuperando el último estado guardado." : "El ZIP está registrado y listo para su análisis automático.")}</p>
        {processing?.error && <p className="project-processing-error">{processing.error}</p>}
        {(processing?.started_at || processing?.updated_at) && <small>{processing.started_at && <>Inició: {formatDate(processing.started_at)} · </>}Actualizado: {formatDate(processing.updated_at)}</small>}
        {(state.error || retryError) && <p className="project-processing-error" role="alert">{retryError ?? state.error}</p>}
      </div>
      {(status === "failed" || status === "interrupted") && <button type="button" className="secondary project-retry" onClick={() => void retry()} disabled={retrying}><Icon name="play" size={15} />{retrying ? "Reintentando…" : "Reintentar análisis"}</button>}
    </section>
  );
}

function isActive(status: ProjectProcessing["status"]): boolean {
  return status === "queued" || status === "running";
}

function statusLabel(status: ProjectProcessing["status"]): string {
  const labels: Record<ProjectProcessing["status"], string> = {
    queued: "En cola",
    running: "En proceso",
    completed: "Completado",
    failed: "Falló",
    interrupted: "Interrumpido",
  };
  return labels[status];
}

function formatDate(value: string): string {
  return new Date(value).toLocaleString("es", { dateStyle: "medium", timeStyle: "short" });
}
