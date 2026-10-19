import type { ReactNode } from "react";
import type { Async } from "../hooks";
import { Icon } from "../components/Icon";

export function Load<T>({ q, children }: { q: Async<T>; children: (d: T) => ReactNode }) {
  if (q.loading && !q.data) return <div className="loading-state" role="status"><span className="spinner" /> Cargando información…</div>;
  if (q.error) return <div className="notice error-notice" role="alert"><Icon name="warning" /><div><strong>No pudimos cargar esta información</strong><p>{q.error === "Failed to fetch" ? "No se pudo conectar con el servicio. Comprueba que esté en funcionamiento e inténtalo de nuevo." : q.error}</p><button className="secondary" onClick={q.reload}>Volver a intentar</button></div></div>;
  return q.data ? <>{children(q.data)}</> : null;
}

export function Badge({ children, tone = "neutral" }: { children: ReactNode; tone?: string }) {
  return <span className={`badge ${tone}`}>{children}</span>;
}

export const prioTone = (p: string | null) => (p === "P0" ? "ok" : p === "P1" ? "warn" : p === "P2" ? "bad" : "neutral");
export const link = (id: string, tab: string, rest?: string) => `#/p/${id}/${tab}${rest ? "/" + encodeURI(rest) : ""}`;
