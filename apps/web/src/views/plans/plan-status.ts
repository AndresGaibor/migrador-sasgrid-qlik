import type { TalendApplyBatchJob, TalendApplyBatchState, TalendApplyState } from "../../types";

export function applyStatusLabel(status: TalendApplyState["status"]): string {
  const labels: Record<TalendApplyState["status"], string> = {
    not_started: "Listo para crear el Job",
    running: "El MCP está creando el Job en Talend Studio",
    applied: "Job creado en Talend Studio",
    partially_applied: "Job creado con información pendiente",
    failed: "No se pudo crear el Job",
    conflict: "Destino con conflicto",
    interrupted: "Creación interrumpida",
  };
  return labels[status];
}

export function talendApplyBatchLabel(status: TalendApplyBatchState["status"]): string {
  const labels: Record<TalendApplyBatchState["status"], string> = {
    not_started: "Listo para crear Jobs en Talend Studio",
    queued: "Creación en cola",
    running: "El MCP está creando Jobs en Talend Studio",
    applied: "Jobs creados en Talend Studio",
    partially_applied: "Jobs creados con información pendiente",
    failed: "No se pudieron crear los Jobs",
    conflict: "Conflicto de revisión o destino",
    interrupted: "Creación interrumpida; puedes reintentar",
  };
  return labels[status];
}

export function talendApplyJobLabel(status: TalendApplyBatchJob["status"]): string {
  const labels: Record<TalendApplyBatchJob["status"], string> = {
    pending: "Pendiente",
    running: "Creando en Talend Studio…",
    applied: "Job creado",
    partially_applied: "Job creado con pendientes",
    failed: "Falló",
    conflict: "Conflicto",
    interrupted: "Interrumpido; puede reintentarse",
  };
  return labels[status];
}

export function verificationCheckLabel(name: string): string {
  const labels: Record<string, string> = { component: "Componente", parameters: "Parámetros", schema: "Esquema", mapper: "Mapper", connections: "Conexiones" };
  return labels[name] ?? name;
}

export function verificationStatusLabel(status: string): string {
  return status === "verified" ? "confirmado" : status === "not_required" ? "no aplica" : status === "unavailable" ? "no disponible" : "pendiente";
}
