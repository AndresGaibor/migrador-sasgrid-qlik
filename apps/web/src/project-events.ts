import { useEffect, useRef, useState } from "react";

export type ProjectActivity = {
  revision: number;
  processing: { status: string; stage: string; message: string | null; updated_at: string } | null;
  batch: {
    status: string;
    completed_jobs: number;
    total_jobs: number;
    current_program: string | null;
    updated_at: string | null;
  } | null;
};

/** Acepta solo eventos con forma conocida: un mensaje raro no debe romper la pantalla. */
export function parseActivity(data: string): ProjectActivity | null {
  let value: unknown;
  try {
    value = JSON.parse(data);
  } catch {
    return null;
  }
  if (!value || typeof value !== "object") return null;
  const activity = value as Partial<ProjectActivity>;
  if (typeof activity.revision !== "number" || !Number.isFinite(activity.revision)) return null;
  if (!("processing" in activity) || !("batch" in activity)) return null;
  return activity as ProjectActivity;
}

/**
 * Se suscribe a los cambios del proyecto. El evento es solo un disparador: `onChange` debe releer
 * los datos por la ruta de siempre. Si el navegador no soporta `EventSource` o la conexión falla,
 * `connected` queda en `false` y quien lo use mantiene su sondeo.
 */
export function useProjectEvents(id: string, onChange: (activity: ProjectActivity) => void) {
  const [connected, setConnected] = useState(false);
  const callback = useRef(onChange);
  const revision = useRef(0);

  useEffect(() => {
    callback.current = onChange;
  }, [onChange]);

  useEffect(() => {
    if (typeof EventSource === "undefined") return undefined;
    revision.current = 0;
    const source = new EventSource(`/api/projects/${encodeURIComponent(id)}/events`);
    const open = () => {
      revision.current = 0;
      setConnected(true);
    };
    const close = () => setConnected(false);
    const activity = (event: MessageEvent<string>) => {
      const parsed = parseActivity(event.data);
      if (!parsed || parsed.revision <= revision.current) return;
      revision.current = parsed.revision;
      callback.current(parsed);
    };
    source.addEventListener("open", open);
    source.addEventListener("error", close);
    source.addEventListener("activity", activity as EventListener);
    return () => {
      source.removeEventListener("open", open);
      source.removeEventListener("error", close);
      source.removeEventListener("activity", activity as EventListener);
      source.close();
      setConnected(false);
    };
  }, [id]);

  return { connected };
}
