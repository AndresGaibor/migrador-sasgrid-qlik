import type { ReactNode } from "react";
import type { Async } from "../hooks";

export function Load<T>({ q, children }: { q: Async<T>; children: (d: T) => ReactNode }) {
  if (q.loading && !q.data) return <p className="muted">Cargando…</p>;
  if (q.error) return <p className="error" role="alert">{q.error}</p>;
  return q.data ? <>{children(q.data)}</> : null;
}

export function Badge({ children, tone = "neutral" }: { children: ReactNode; tone?: string }) {
  return <span className={`badge ${tone}`}>{children}</span>;
}

export const prioTone = (p: string | null) => (p === "P0" ? "ok" : p === "P1" ? "warn" : p === "P2" ? "bad" : "neutral");
export const link = (id: string, tab: string, rest?: string) => `#/p/${id}/${tab}${rest ? "/" + encodeURI(rest) : ""}`;
