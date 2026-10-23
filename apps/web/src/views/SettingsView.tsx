import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { Badge, Load } from "./common";

type Health = Awaited<ReturnType<typeof api.talendHealth>>;

function Stage({ tone, title, detail }: { tone: string; title: string; detail: string }) {
  return (
    <div className="health-stage">
      <Badge tone={tone}>{tone === "ok" ? "OK" : tone === "warn" ? "Revisar" : "Pendiente"}</Badge>
      <div><strong>{title}</strong><p className="muted">{detail}</p></div>
    </div>
  );
}

function overall(h: Health) {
  if (h.available) return { tone: "ok", label: "Conectado" };
  if (h.mcp_available) return { tone: "warn", label: "Parcial" };
  return { tone: "bad", label: "Sin conexión" };
}

function bridgeModeLabel(mode: string | undefined) {
  return mode === "readWrite" ? "lectura y escritura" : mode === "readOnly" ? "solo lectura" : mode ?? "desconocido";
}

export function SettingsView() {
  const q = useAsync(api.talendHealth, []);
  return <>
    <div className="eyebrow">TU ESPACIO DE TRABAJO</div><h1>Configuración</h1>
    <p className="subtitle">Consulta el estado de la conexión con Talend Studio.</p>
    <section className="panel">
      <div className="panel-heading"><Icon name="settings" size={28} /><div><h2>Conexión con Talend</h2><p>Integración opcional para consultar y verificar componentes.</p></div><Badge>Solo lectura</Badge></div>
      <div className="notice"><Icon name="info" /><span>Puedes analizar tus programas y preparar planes aunque esta conexión no esté disponible. La verificación de los componentes se hará posteriormente.</span></div>
      <Load q={q}>{(h) => {
        const state = overall(h);
        return <>
          <p>Estado: <Badge tone={state.tone}>{state.label}</Badge>{h.available && h.jobs != null && <span className="muted"> {h.jobs} procesos disponibles</span>}</p>
          <div className="health-stages" role="status" aria-live="polite">
            <Stage
              tone={h.mcp_available ? "ok" : "bad"}
              title="Servidor MCP"
              detail={h.mcp_available
                ? `Responde en ${h.mcp_url ?? "la URL configurada"}${h.jobs != null ? ` · ${h.jobs} procesos en el proyecto` : ""}.`
                : `No responde en ${h.mcp_url ?? "la URL configurada"}. Arrántalo con «bun run start:server» en la carpeta de talend-mcp.`}
            />
            <Stage
              tone={h.bridge_available ? "ok" : "warn"}
              title="Bridge de Talend Studio"
              detail={h.bridge_available
                ? `Conectado en modo ${bridgeModeLabel(h.bridge_mode)}.`
                : "Sin conexión. Abre Talend Studio con el plugin del bridge instalado para inspeccionar y escribir Jobs."}
            />
            <Stage
              tone={h.write_enabled ? "ok" : "warn"}
              title="Escritura de Jobs"
              detail={h.write_enabled
                ? `Activada. Los Jobs nuevos se crean en «${h.apply_folder}».`
                : "Bloqueada por TALEND_MCP_READONLY=true; la API solo puede leer."}
            />
          </div>
          {h.error && <details><summary>Detalles para el equipo técnico</summary><p className="mono">{h.error}</p></details>}
          <dl className="health-config">
            <div><dt>URL del MCP</dt><dd className="mono">{h.mcp_url ?? "—"}</dd></div>
            <div><dt>Timeout</dt><dd className="mono">{h.timeout_seconds != null ? `${h.timeout_seconds} s` : "—"}</dd></div>
            <div><dt>Carpeta de aplicación</dt><dd className="mono">{h.apply_folder}</dd></div>
          </dl>
        </>;
      }}</Load>
      <button className="secondary" onClick={q.reload} disabled={q.loading}><Icon name="check" size={18} />{q.loading ? "Comprobando…" : "Comprobar conexión"}</button>
    </section>
  </>;
}
