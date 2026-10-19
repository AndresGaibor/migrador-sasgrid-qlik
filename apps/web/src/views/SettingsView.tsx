import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { Badge, Load } from "./common";

export function SettingsView() {
  const q = useAsync(api.talendHealth, []);
  return <>
    <div className="eyebrow">TU ESPACIO DE TRABAJO</div><h1>Configuración</h1>
    <p className="subtitle">Consulta el estado de la conexión con Talend Studio.</p>
    <section className="panel">
      <div className="panel-heading"><Icon name="settings" size={28} /><div><h2>Conexión con Talend</h2><p>Integración opcional para consultar y verificar componentes.</p></div><Badge>Solo lectura</Badge></div>
      <div className="notice"><Icon name="info" /><span>Puedes analizar tus programas y preparar planes aunque esta conexión no esté disponible. La verificación de los componentes se hará posteriormente.</span></div>
      <Load q={q}>{(h) => <><p>Estado: <Badge tone={h.available ? "ok" : "warn"}>{h.available ? "Conectado" : "Sin conexión"}</Badge>{h.available && h.jobs != null && <span className="muted"> {h.jobs} procesos disponibles</span>}</p>{!h.available && h.error && <details><summary>Detalles para el equipo técnico</summary><p className="mono">{h.error}</p></details>}</>}</Load>
      <button className="secondary" onClick={q.reload} disabled={q.loading}><Icon name="check" size={18} />{q.loading ? "Comprobando…" : "Comprobar conexión"}</button>
    </section>
  </>;
}
