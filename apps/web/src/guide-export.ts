import type { JobPlan, Step } from "./types";
import { orderSteps } from "./guided.ts";
import { decodeProgress, type GuideProgress } from "./guide-progress.ts";

const progressLabels: Record<GuideProgress, string> = {
  pending: "Pendiente",
  in_progress: "En progreso",
  completed: "Completado",
  blocked: "Bloqueado",
};

function officialUrl(step: Step): string | null {
  return step.doc_url ?? null;
}

function evidenceHref(projectId: string, step: Step): string {
  return `#/p/${encodeURIComponent(projectId)}/programas/${encodeURI(step.evidence.file)}?line=${step.evidence.line}`;
}

function exportStep(step: Step, projectId: string) {
  const progress = decodeProgress(step.status, step.note);
  return {
    ...step,
    backend_status: step.status,
    status: progress.state,
    note: progress.note,
    block_reason: progress.blockReason || null,
    references: {
      sas: { file: step.evidence.file, line: step.evidence.line, href: evidenceHref(projectId, step) },
      official: { url: officialUrl(step) },
    },
  };
}

export function guideJson(plan: JobPlan, projectId: string): string {
  const enriched = {
    ...plan,
    guide_format: "byron-guided-talend-v1",
    studio_validation: "pending",
    steps: orderSteps(plan.steps).map((step) => exportStep(step, projectId)),
    children: plan.children.map((child) => ({ ...child, steps: orderSteps(child.steps).map((step) => exportStep(step, projectId)) })),
  };
  return JSON.stringify(enriched, null, 2);
}

function renderStepMarkdown(step: Step, projectId: string): string[] {
  const progress = decodeProgress(step.status, step.note);
  const doc = officialUrl(step);
  const lines = [
    `### ${step.order}. ${step.purpose}`,
    "",
    `- **Estado de la guía:** ${progressLabels[progress.state]}`,
    ...(progress.blockReason ? [`- **Motivo del bloqueo:** ${progress.blockReason}`] : []),
    `- **Componente candidato:** \`${step.component_candidate}\` · ${step.in_catalog ? "presente en el catálogo" : "presencia en catálogo por revisar"} · ${step.verified ? "cotejado con Talend MCP" : "sin cotejo con Talend MCP"}`,
    `- **Confianza:** ${step.confidence} · **Subjob:** \`${step.subjob}\``,
    `- **Evidencia SAS:** [${step.evidence.file}:${step.evidence.line}](${evidenceHref(projectId, step)})`,
    `- **Fuente oficial:** ${doc ? `[documentación Talend](${doc})` : "pendiente de confirmar"}`,
  ];
  if (step.properties.length) {
    lines.push("", "**Campos y valores sugeridos:**", "");
    for (const property of step.properties) lines.push(`- \`${property.label || property.name}\` = ${property.value ? `\`${property.value}\`` : "_por configurar_"}${property.in_catalog === false ? " _(nombre por verificar)_" : ""}`);
  }
  if (step.connections.length) {
    lines.push("", "**Dependencias:**", "");
    for (const connection of step.connections) lines.push(`- ${connection.type}${connection.from_step ? ` desde el paso \`${connection.from_step}\`` : " desde origen externo/no identificado"}`);
  }
  if (step.pending.length) lines.push("", "**Pendientes de decisión:**", "", ...step.pending.map((pending) => `- ${pending}`));
  if (progress.note) lines.push("", `**Nota de trabajo:** ${progress.note}`);
  lines.push("");
  return lines;
}

export function guideMarkdown(plan: JobPlan, projectId: string): string {
  const lines = [
    `# Guía de migración: ${plan.job_name}`,
    "",
    `- **Programa SAS:** \`${plan.program}\``,
    `- **Estado del análisis:** ${plan.job_status}`,
    "- **Validación en Talend Studio:** pendiente; este documento no representa un Job Talend nativo.",
    "",
    "## Haz esto en Talend",
    "",
  ];
  for (const step of orderSteps(plan.steps)) lines.push(...renderStepMarkdown(step, projectId));
  for (const child of plan.children) {
    lines.push(`## Job hijo para %${child.name}(${child.params.join(", ")})`, "");
    for (const step of orderSteps(child.steps)) lines.push(...renderStepMarkdown(step, projectId));
  }
  if (plan.validation_cases.length) lines.push("## Casos de validación", "", ...plan.validation_cases.map((item) => `- **${item.kind}:** ${item.description}`), "");
  if (plan.unresolved.length) lines.push("## Por resolver", "", ...plan.unresolved.map((item) => `- ${item}`), "");
  return `${lines.join("\n")}\n`;
}

function csvCell(value: unknown): string {
  const raw = value == null ? "" : String(value);
  const text = /^[\s]*[=+@]/.test(raw) || /^[\s]*-[^0-9]/.test(raw) ? `'${raw}` : raw;
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

export function guideCsv(plans: JobPlan[], projectId: string): string {
  const rows: unknown[][] = [["job", "programa", "paso_id", "orden", "subjob", "componente", "estado_guia", "verificado_talend_mcp", "confianza", "proposito", "evidencia_sas", "evidencia_sas_url", "fuente_oficial_url", "campos_valores", "pendientes", "motivo_bloqueo", "nota"]];
  for (const plan of plans) {
    const steps = [...orderSteps(plan.steps), ...plan.children.flatMap((child) => orderSteps(child.steps))];
    for (const step of steps) {
      const progress = decodeProgress(step.status, step.note);
      rows.push([plan.job_name, plan.program, step.id, step.order, step.subjob, step.component_candidate, progressLabels[progress.state], step.verified, step.confidence, step.purpose, `${step.evidence.file}:${step.evidence.line}`, evidenceHref(projectId, step), officialUrl(step) ?? "", step.properties.map((p) => `${p.label || p.name}=${p.value ?? "por configurar"}`).join(" | "), step.pending.join(" | "), progress.blockReason, progress.note]);
    }
  }
  return `\uFEFF${rows.map((row) => row.map(csvCell).join(",")).join("\r\n")}`;
}

export function guideIndexMarkdown(plans: JobPlan[]): string {
  const rows = plans.map((plan) => {
    const steps = [...plan.steps, ...plan.children.flatMap((child) => child.steps)];
    const states = steps.map((step) => decodeProgress(step.status, step.note).state);
    const blocked = states.filter((state) => state === "blocked").length;
    const pending = states.filter((state) => state === "pending").length;
    const completed = states.filter((state) => state === "completed").length;
    return `| \`${plan.job_name}\` | \`${plan.program}\` | ${steps.length} | ${completed} completado(s) | ${pending} pendiente(s) | ${blocked} bloqueado(s) |`;
  });
  return [`# Guías de migración`, "", "Los componentes son sugerencias. La validación en Talend Studio debe realizarse por separado.", "", "| Job | Programa SAS | Pasos | Completados | Pendientes | Bloqueados |", "| --- | --- | ---: | ---: | ---: | ---: |", ...rows, ""].join("\n");
}
