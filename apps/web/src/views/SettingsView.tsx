import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { Badge, Load } from "./common";
import { notifyError, notifySuccess } from "../errors";

type Health = Awaited<ReturnType<typeof api.talendHealth>>;

const DIAGNOSIS_LABELS: Record<string, string> = {
  mcp_down: "MCP sin respuesta",
  client_incompatible: "Cliente MCP desactualizado",
  tools_missing: "Faltan tools del portal",
  contract_incomplete: "Contrato MCP incompatible",
  bridge_down: "Bridge sin conexión",
  studio_blocked: "Diálogo abierto en Studio",
};

function Stage({ tone, title, detail }: { tone: string; title: string; detail: string }) {
  return (
    <div className="health-stage">
      <Badge tone={tone}>{tone === "ok" ? "OK" : tone === "bad" ? "Bloqueado" : "Revisar"}</Badge>
      <div><strong>{title}</strong><p className="muted">{detail}</p></div>
    </div>
  );
}

function overall(h: Health) {
  if (h.diagnosis && h.diagnosis !== "ok") return { tone: "warn", label: DIAGNOSIS_LABELS[h.diagnosis] ?? "Revisar" };
  if (h.available && h.spec_supported === false) return { tone: "warn", label: "Contrato MCP incompatible" };
  if (h.available) return { tone: "ok", label: "Conectado" };
  if (h.mcp_available) return { tone: "warn", label: "Parcial" };
  return { tone: "bad", label: "Sin conexión" };
}

function bridgeModeLabel(mode: string | undefined) {
  return mode === "readWrite" ? "lectura y escritura" : mode === "readOnly" ? "solo lectura" : mode ?? "desconocido";
}

export function SettingsView() {
  const q = useAsync(api.talendHealth, []);
  const permissions = useAsync(api.talendPermissions, []);
  const [permission, setPermission] = useState<boolean>();
  const [savingWrite, setSavingWrite] = useState(false);
  const [writeError, setWriteError] = useState<string>();
  const enabled = permission ?? permissions.data?.write_enabled;

  const toggleWrite = async (enabled: boolean) => {
    if (savingWrite) return;
    setSavingWrite(true);
    setWriteError(undefined);
    try {
      const saved = await api.setTalendWriteEnabled(enabled);
      setPermission(saved.write_enabled);
      notifySuccess(saved.write_enabled ? "Escritura habilitada" : "Escritura desactivada", "El permiso se conserva al reiniciar el portal.");
      q.reload();
    } catch (error) {
      setWriteError(notifyError(error, "No se pudo guardar el permiso de escritura"));
    } finally {
      setSavingWrite(false);
    }
  };

  return <>
    <div className="eyebrow">TU ESPACIO DE TRABAJO</div><h1>Configuración</h1>
    <p className="subtitle">Consulta el estado de la conexión con Talend Studio.</p>
    <section className="panel" aria-labelledby="write-permission-title"><h2 id="write-permission-title">Permiso de escritura</h2><label className="permission-toggle"><input type="checkbox" role="switch" checked={Boolean(enabled)} disabled={savingWrite || enabled === undefined} onChange={(event) => void toggleWrite(event.target.checked)} /><span>Permitir crear Jobs desde el portal{savingWrite ? " · Guardando…" : enabled === undefined ? " · Consultando…" : enabled ? " · Habilitado" : " · Solo lectura"}</span></label><p className="muted">Cada creación requiere revisión y confirmación. No permite ejecutar ni publicar Jobs. Desactivar no interrumpe una operación ya enviada a Studio, pero impide enviar las siguientes.</p>{(writeError || permissions.error) && <p className="permission-toggle-error" role="alert">{writeError ?? permissions.error} <button className="secondary" onClick={permissions.reload}>Volver a consultar</button></p>}</section>
    <section className="panel">
      <div className="panel-heading"><Icon name="settings" size={28} /><div><h2>Conexión con Talend</h2><p>Diagnóstico del MCP, el Bridge y el contrato de creación.</p></div></div>
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
              tone={!h.studio_dialogs?.checked ? "warn" : h.studio_dialogs.blocked ? "bad" : "ok"}
              title="Diálogos de Studio"
              detail={!h.studio_dialogs?.checked
                ? "No se pudieron comprobar los diálogos abiertos. El Bridge puede ser anterior al endpoint de diálogos."
                : h.studio_dialogs.blocked
                ? `Un modal bloquea el IDE y detendría compilaciones o ejecuciones: ${h.studio_dialogs.blocking.map((dialog) => `«${dialog.title}»`).join(", ")}. Crear y leer Jobs sigue funcionando.`
                : "Sin diálogos que bloqueen el IDE."}
            />
            <Stage
              tone={h.write_tool === false ? "bad" : h.write_enabled ? "ok" : "warn"}
              title="Escritura de Jobs"
              detail={h.write_tool === false
                ? "El MCP no publica talend_job_apply_custom_spec. Actualiza talend-mcp antes de crear Jobs."
                : h.write_enabled
                ? `Activada. Los Jobs nuevos se crean en «${h.apply_folder}».`
                : "Desactivada desde el permiso de escritura de esta pantalla."}
            />
            <Stage tone={h.spec_supported ? "ok" : "warn"} title="Contrato de creación" detail={h.spec_supported ? "Compatible con Jobs hijos, borradores y tablas de configuración." : h.spec_error ?? "No se pudo comprobar la compatibilidad del MCP."} />
          </div>
          {h.diagnosis && h.diagnosis !== "ok" && h.fix_hint && (
            <div className="notice" role="alert">
              <Icon name="info" />
              <span>{h.fix_hint}{h.missing_tools?.length ? ` Faltan: ${h.missing_tools.join(", ")}.` : ""}</span>
            </div>
          )}
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
