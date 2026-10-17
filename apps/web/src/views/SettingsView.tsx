import { api } from "../api";
import { useAsync } from "../hooks";
import { Badge, Load } from "./common";

export function SettingsView() {
  const q = useAsync(api.talendHealth, []);
  return (
    <>
      <h1>Ajustes</h1>
      <h2>Integración talend-mcp</h2>
      <p className="muted">
        Opcional y de solo lectura. Sin ella el análisis y los planes funcionan igual; los componentes quedan sin
        verificar.
      </p>
      <Load q={q}>
        {(h) => (
          <p>
            Estado: <Badge tone={h.available ? "ok" : "bad"}>{h.available ? "disponible" : "no disponible"}</Badge>{" "}
            {h.available ? `${h.jobs} Jobs` : h.error}
          </p>
        )}
      </Load>
      <button onClick={q.reload}>Reintentar</button>
    </>
  );
}
