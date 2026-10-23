import type { GridRecommendation } from "./types";

export type GuideAction = { text: string; fields?: [string, string][]; where?: string; note?: string; doc_url?: string };
export type GridGuide = { key: string; title: string; kind: "build" | "cloud" | "manual"; intro: string; actions: GuideAction[]; component?: string; doc_url?: string | null; sources: GridRecommendation[] };
type ManualGuide = { title: string; intro: string; kind?: "cloud" | "manual"; actions: (string | GuideAction)[] };

const DISPATCH = new Set(["sas_macro_step.include_dispatch", "sas_batch.sysin", "sasgsub.submit"]);
const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
const stem = (f: string) => slug((f.split("/").pop() ?? f).replace(/\.[^.]+$/, ""));
const str = (v: unknown) => (typeof v === "string" ? v : undefined);

const MANUAL: Record<string, ManualGuide> = {
  "scheduler.control_m": {
    title: "Programar los Jobs en Qlik Talend Cloud (Control-M)",
    kind: "cloud",
    intro: "El SAS solo menciona Control-M; no contiene el calendario real. Confírmalo con Operaciones y, si Qlik Talend Cloud será el nuevo planificador, traslada allí la cadena como un Plan.",
    actions: [
      {
        text: "Recupera la definición efectiva del calendario en Control-M.",
        where: "Pide a Operaciones la ficha o exportación del job antes de programarlo.",
        note: "Confirma zona horaria, días y festivos, hora, dependencias, reintentos y política de solapamientos.",
      },
      {
        text: "Publica en Qlik Talend Cloud los Jobs que deben ejecutarse.",
        where: "Talend Studio → Repository → clic derecho en cada Job → Publish to Cloud. Selecciona el Environment y el Space de destino.",
        note: "Al publicar, Talend Management Console (TMC) crea una Task asociada a cada artefacto.",
        doc_url: "https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/publish-jobs",
      },
      {
        text: "Configura y prueba una Task por Job.",
        where: "Qlik Talend Cloud → Management → Tasks. Elige Environment y Space; abre la Task creada al publicar o crea una con Create new → Task.",
        note: "Completa parámetros/contexto y el Processor (Cloud, Cloud exclusive, Remote Engine o cluster). Guarda y ejecuta cada Task correctamente una vez antes de añadirla a un Plan.",
        doc_url: "https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/creating-job-tasks",
      },
      {
        text: "Crea un Plan para reproducir el orden de dependencias.",
        where: "Management → Plans → Create new → Plan. Elige Space, nombre y descripción; agrega las Tasks en el orden acordado.",
        note: "Usa un paso por Job dependiente: formatos y macros, procesos y, al final, Jobs que lanzan a otros.",
        doc_url: "https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/creating-plans",
      },
      {
        text: "Configura los pasos para que respeten las dependencias.",
        where: "En el Plan, selecciona Edit → Steps. Añade cada Task a su paso y mueve los pasos al orden correcto.",
        note: "Elige If all tasks succeed para que el siguiente paso espere a que termine correctamente el anterior.",
        doc_url: "https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/actions-shortcuts-plan-edit-view",
      },
      {
        text: "Programa el Plan con el calendario recuperado de Control-M.",
        where: "Detalles del Plan → Edit → Schedule → Add trigger. Elige tipo de trigger, zona horaria, fecha inicial, frecuencia y horas; termina con Save and close.",
        note: "Puedes elegir Once, Daily, Weekly, Monthly o Cron. Verifica festivos y excepciones; los triggers deben separarse al menos cinco minutos.",
        doc_url: "https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/scheduling-plans",
      },
      {
        text: "Valida el Plan antes de retirar el calendario de Control-M.",
        where: "Ejecuta una prueba desde el detalle del Plan y revisa el resultado y los logs en Operations.",
        note: "Compara la prueba con el resultado de Control-M. No dejes ambos calendarios activos salvo que Operaciones haya definido esa convivencia.",
        doc_url: "https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/monitoring-operations-new-view",
      },
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
    guides.push({
      key: pid,
      kind: m.kind ?? "manual",
      title: m.title,
      intro: m.intro,
      actions: m.actions.map((action) => typeof action === "string" ? { text: action } : action),
      sources: list,
    });
  }
  return guides;
}
