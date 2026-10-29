import type { JobPlan, Step } from "./types";
import { orderSteps } from "./guided.ts";

function officialUrl(step: Step): string | null {
  return step.doc_url ?? null;
}

function evidenceHref(projectId: string, step: Step): string {
  return `#/p/${encodeURIComponent(projectId)}/programas/${encodeURI(step.evidence.file)}?line=${step.evidence.line}`;
}

function exportStep(step: Step, projectId: string) {
  const technicalStep = { ...step, status: undefined, note: undefined };
  return {
    ...technicalStep,
    references: {
      sas: { file: step.evidence.file, line: step.evidence.line, href: evidenceHref(projectId, step) },
      official: { url: officialUrl(step) },
    },
  };
}

export function guideJson(plan: JobPlan, projectId: string): string {
  const technicalPlan = { ...plan, job_status: undefined };
  const enriched = {
    ...technicalPlan,
    guide_format: "byron-guided-talend-v2",
    steps: orderSteps(plan.steps).map((step) => exportStep(step, projectId)),
    children: plan.children.map((child) => ({ ...child, steps: orderSteps(child.steps).map((step) => exportStep(step, projectId)) })),
  };
  return JSON.stringify(enriched, null, 2);
}

function renderStepMarkdown(step: Step, projectId: string): string[] {
  const doc = officialUrl(step);
  const lines = [
    `### ${step.order}. ${step.purpose}`,
    "",
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
  if (step.pending.length) lines.push("", "**Información técnica pendiente:**", "", ...step.pending.map((pending) => `- ${pending}`));
  lines.push("");
  return lines;
}

export function guideMarkdown(plan: JobPlan, projectId: string): string {
  const lines = [
    `# Guía de migración: ${plan.job_name}`,
    "",
    ...(plan.description ? [plan.description, ""] : []),
    `- **Programa SAS:** \`${plan.program}\``,
    "- **Ejecución:** MCP crea el Job en Talend Studio; esta guía no ejecuta el Job.",
    "",
    "## Instrucciones SAS",
    "",
  ];
  if (plan.entry_macro) {
    lines.push(
      `La macro principal **%${plan.entry_macro.name}(${plan.entry_macro.params.join(", ")})** está integrada en este Job.`,
      "",
    );
  }
  for (const step of orderSteps(plan.steps)) lines.push(...renderStepMarkdown(step, projectId));
  for (const child of plan.children) {
    lines.push(`## Definición de macro auxiliar %${child.name}(${child.params.join(", ")})`, "");
    for (const step of orderSteps(child.steps)) lines.push(...renderStepMarkdown(step, projectId));
  }
  if (plan.validation_cases.length) lines.push("## Casos de validación", "", ...plan.validation_cases.map((item) => `- **${item.kind}:** ${item.description}`), "");
  if (plan.unresolved.length) lines.push("## Información técnica por resolver", "", ...plan.unresolved.map((item) => `- ${item}`), "");
  return `${lines.join("\n")}\n`;
}

function csvCell(value: unknown): string {
  const raw = value == null ? "" : String(value);
  const text = /^[\s]*[=+@]/.test(raw) || /^[\s]*-[^0-9]/.test(raw) ? `'${raw}` : raw;
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

export function guideCsv(plans: JobPlan[], projectId: string): string {
  const rows: unknown[][] = [["job", "programa", "paso_id", "orden", "subjob", "componente", "verificado_talend_mcp", "confianza", "proposito", "evidencia_sas", "evidencia_sas_url", "fuente_oficial_url", "campos_valores", "informacion_tecnica_pendiente"]];
  for (const plan of plans) {
    const steps = [...orderSteps(plan.steps), ...plan.children.flatMap((child) => orderSteps(child.steps))];
    for (const step of steps) {
      rows.push([plan.job_name, plan.program, step.id, step.order, step.subjob, step.component_candidate, step.verified, step.confidence, step.purpose, `${step.evidence.file}:${step.evidence.line}`, evidenceHref(projectId, step), officialUrl(step) ?? "", step.properties.map((p) => `${p.label || p.name}=${p.value ?? "por configurar"}`).join(" | "), step.pending.join(" | ")]);
    }
  }
  return `\uFEFF${rows.map((row) => row.map(csvCell).join(",")).join("\r\n")}`;
}

export function guideIndexMarkdown(plans: JobPlan[]): string {
  const rows = plans.map((plan) => {
    const steps = [...plan.steps, ...plan.children.flatMap((child) => child.steps)];
    return `| \`${plan.job_name}\` | \`${plan.program}\` | ${steps.length} paso(s) |`;
  });
  return [`# Guías de migración`, "", "Resumen de programas y sus instrucciones SAS para Talend Studio.", "", "| Job | Programa SAS | Instrucciones |", "| --- | --- | ---: |", ...rows, ""].join("\n");
}
