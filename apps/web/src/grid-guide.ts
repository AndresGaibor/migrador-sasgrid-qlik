import type { GridRecommendation } from "./types";

export type GuideAction = { text: string; fields?: [string, string][]; where?: string };
export type GridGuide = { key: string; title: string; kind: "build" | "manual"; intro: string; actions: GuideAction[]; component?: string; doc_url?: string | null; sources: GridRecommendation[] };

const DISPATCH = new Set(["sas_macro_step.include_dispatch", "sas_batch.sysin", "sasgsub.submit"]);
const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
const stem = (f: string) => slug((f.split("/").pop() ?? f).replace(/\.[^.]+$/, ""));
const str = (v: unknown) => (typeof v === "string" ? v : undefined);

const MANUAL: Record<string, { title: string; intro: string; actions: string[] }> = {
  "scheduler.control_m": {
    title: "Horario de ejecución (Control-M)",
    intro: "Esto no se configura en Talend Studio. Solo encontramos un comentario en el SAS, no el horario real.",
    actions: [
      "Pide a quien administra Control-M la definición del job: horario, calendario y dependencias.",
      "Programa el Job principal con esos mismos datos en tu planificador (por ejemplo Talend Management Console o Control-M).",
    ],
  },
  "scheduler.lsf": {
    title: "Comando LSF",
    intro: "No sabemos interpretar este comando. Hay que decidirlo con una persona.",
    actions: ["Copia el comando LSF y pide a operaciones qué hace (cola, recursos, dependencias).", "No lo migres hasta tener ese diseño por escrito."],
  },
  "sasgsub.job_options": {
    title: "Cola y nombre del trabajo en Grid",
    intro: "Talend no tiene un campo equivalente de forma directa.",
    actions: ["Pregunta a operaciones si la cola y el nombre deben conservarse en el planificador de destino.", "Si sí, configúralos allí, no en el Job."],
  },
  "sasgsub.set_parameters": {
    title: "Parámetros pasados al programa",
    intro: "Se convierten en variables de contexto del Job hijo.",
    actions: ["En el Job hijo: Contexts → crea una variable por parámetro (mismo nombre).", "En el tRunJob que lo llama, tabla «Context Param»: añade cada variable con su valor."],
  },
  "sasgsub.unverified_options": {
    title: "Opciones no reconocidas",
    intro: "La herramienta no entiende estas opciones y no las traslada.",
    actions: ["Consulta con quien conozca SAS Grid qué hace cada opción.", "Decide a mano si se necesita en Talend."],
  },
  "sasgsub.missing_option_value": {
    title: "Falta un valor en el comando",
    intro: "No se puede inferir. Detén este paso.",
    actions: ["Recupera el valor que falta de la definición original del job y vuelve a analizar."],
  },
  "shell.inferred_sequence": {
    title: "Orden de ejecución deducido del script",
    intro: "El orden se dedujo del shell; puede haber ramas que no se ven.",
    actions: ["Lee el script original y confirma el orden y qué pasa si un paso falla.", "Solo entonces conecta los Jobs."],
  },
};

function buildGuide(file: string, items: GridRecommendation[]): GridGuide {
  const sorted = [...items].sort((a, b) => a.evidence.line - b.evidence.line);
  const parent = `job_${stem(file)}`;
  const children = sorted.map((i) => {
    const d = i.details as Record<string, unknown>;
    const params = (d.params ?? {}) as Record<string, string>;
    const target = str(d.resolved_program);
    return { rec: i, label: params.step_name ?? (target ? stem(target) : "Paso"), job: target ? `job_${stem(target)}` : undefined, raw: str(d.program) };
  });
  const actions: GuideAction[] = [
    { text: `Crea el Job principal «${parent}».`, where: "Repository → Job Designs → clic derecho → Create Job → Name" },
    { text: "Antes de seguir, crea y guarda estos Jobs hijos (uno por programa):", fields: children.map((c): [string, string] => [c.job ?? "(sin resolver)", c.raw ?? ""]) },
  ];
  children.forEach((c, n) => {
    const prev = children[n - 1];
    actions.push({
      text: `Paso ${n + 1}: arrastra un tRunJob al lienzo del Job principal.`,
      where: "Palette → busca «tRunJob»",
      fields: [
        ["Label (pestaña Component → View)", c.label],
        ["Job", c.job ?? "elige el Job hijo a mano"],
        ["Die on child error", "marcado"],
      ],
    });
    if (prev) actions.push({ text: `Une «${prev.label}» con «${c.label}».`, where: `Clic derecho en «${prev.label}» → Trigger → On Subjob Ok → clic en «${c.label}»` });
  });
  const first = sorted[0];
  return { key: file, kind: "build", title: `${parent}: lanza ${children.length} programa${children.length === 1 ? "" : "s"} en orden`, intro: `Se construye a partir de ${file.split("/").slice(-2).join("/")}.`, actions, component: "tRunJob", doc_url: first.doc_url, sources: sorted };
}

export function buildGridGuides(items: GridRecommendation[]): GridGuide[] {
  const byFile = new Map<string, GridRecommendation[]>();
  const manual = new Map<string, GridRecommendation[]>();
  for (const i of items) {
    const bucket = DISPATCH.has(i.pattern_id) ? byFile : manual;
    const key = DISPATCH.has(i.pattern_id) ? i.evidence.file : i.pattern_id;
    bucket.set(key, [...(bucket.get(key) ?? []), i]);
  }
  const guides = [...byFile].map(([f, l]) => buildGuide(f, l));
  for (const [pid, list] of manual) {
    const m = MANUAL[pid] ?? { title: pid, intro: list[0].instruction, actions: list[0].required };
    guides.push({ key: pid, kind: "manual", title: m.title, intro: m.intro, actions: m.actions.map((text) => ({ text })), sources: list });
  }
  return guides;
}
