import type { ReactNode } from "react";
import type { Async } from "../hooks";
import { Icon } from "../components/Icon";
import { formatErrorMessage } from "../errors";

export function Load<T>({ q, children }: { q: Async<T>; children: (d: T) => ReactNode }) {
  if (q.loading && !q.data) return <div className="loading-state" role="status"><span className="spinner" /> Cargando información…</div>;
  const error = q.error && <div className="notice error-notice" role="alert"><Icon name="warning" /><div><strong>{q.data ? "No se pudo actualizar la información" : "No pudimos cargar esta información"}</strong>{q.data && <p>Se muestran los datos anteriores.</p>}<p>{formatErrorMessage(q.error, undefined, q.errorStatus)}</p><button className="secondary" onClick={q.reload} disabled={q.loading}>{q.loading ? "Volviendo a intentar…" : "Volver a intentar"}</button></div></div>;
  if (!q.data) return error;
  return <>{error}{children(q.data)}</>;
}

export function Badge({ children, tone = "neutral" }: { children: ReactNode; tone?: string }) {
  return <span className={`badge ${tone}`}>{children}</span>;
}

export const prioTone = (p: string | null) => (p === "P0" ? "ok" : p === "P1" ? "warn" : p === "P2" ? "bad" : "neutral");
export const link = (id: string, tab: string, rest?: string) => `#/p/${id}/${tab}${rest ? "/" + encodeURI(rest) : ""}`;
