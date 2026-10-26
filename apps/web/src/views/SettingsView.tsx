import { useState } from "react";
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
  const [savingWrite, setSavingWrite] = useState(false);
  const [writeError, setWriteError] = useState<string>();

  const toggleWrite = async (enabled: boolean) => {
    setSavingWrite(true);
    setWriteError(undefined);
    try {
      await api.setTalendWriteEnabled(enabled);
      q.reload();
    } catch (error) {
      setWriteError(error instanceof Error ? error.message : "No se pudo guardar el permiso de escritura.");
    } finally {
      setSavingWrite(false);
    }
  };

  return <>
    <div className="eyebrow">TU ESPACIO DE TRABAJO</div><h1>Configuración</h1>
    <p className="subtitle">Consulta el estado de la conexión con Talend Studio.</p>
    <section className="panel">
      <div className="panel-heading"><Icon name="settings" size={28} /><div><h2>Conexión con Talend</h2><p>Integración opcional para consultar y verificar componentes.</p></div>{q.data && <Badge tone={q.data.write_enabled ? "ok" : "warn"}>{q.data.write_enabled ? "Creación habilitada" : "Solo lectura"}</Badge>}</div>
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
                ? `Responde en ${h.mcp_url ?? "la URL configurada"}${h.tools != null ? ` · ${h.tools} tools publicadas` : ""}${h.jobs != null ? ` · ${h.jobs} procesos en el proyecto` : ""}.`
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
              tone={h.write_tool === false ? "bad" : h.write_enabled ? "ok" : "warn"}
              title="Escritura de Jobs"
              detail={h.write_tool === false
                ? "El MCP no publica talend_job_apply_custom_spec. Actualiza talend-mcp antes de crear Jobs."
                : h.write_enabled
                ? `Activada. Los Jobs nuevos se crean en «${h.apply_folder}».`
                : "Desactivada en Configuración o por TALEND_MCP_READONLY=true; la API solo puede leer."}
            />
          </div>
          <label className="permission-toggle">
            <input
              type="checkbox"
              checked={h.write_enabled}
              disabled={savingWrite}
              onChange={(event) => toggleWrite(event.target.checked)}
            />
            <span>Permitir crear Jobs desde el portal{savingWrite ? " · Guardando…" : ""}</span>
          </label>
          {writeError && <p className="permission-toggle-error" role="alert">{writeError}</p>}
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
