// Filas de la pestaña Contexts de Talend Studio a partir de las variables que propone el planificador.
import type { JobPlan } from "../types";
import { toContext } from "../step-guide";

export const CONTEXT_ENVS = ["DEV", "QA", "PROD"] as const;
type Env = (typeof CONTEXT_ENVS)[number];

export type ContextRow = {
  name: string;
  /** Tipo tal como lo muestra Studio: String, Integer, Password… */
  type: string;
  comment: string;
  /** Valor por defecto. Vacío si es un secreto o si el valor lo da el equipo. */
  value: string;
  secret: boolean;
  needsValue: boolean;
  /** Valor por ambiente, solo cuando el SAS distingue ambientes. */
  envs: Partial<Record<Env, string | null>> | null;
};

type ContextVariable = JobPlan["context_variables"][number] & {
  talend_type?: string;
  is_secret?: boolean;
  needs_value?: boolean;
  sas_line?: number | null;
  group_values?: Partial<Record<Env, string | null>> | null;
};

/** «id_Password» → «Password»: Studio muestra el tipo sin el prefijo. */
export const studioType = (talendType: string | undefined): string => (talendType ?? "id_String").replace(/^id_/, "");

export function contextRows(plan: Pick<JobPlan, "context_variables" | "libraries_needed">): ContextRow[] {
  const dirs = plan.libraries_needed
    .filter((l) => !l.engine && l.path)
    .map((l): ContextRow => ({ name: `${l.sas_name.toUpperCase()}_DIR`, type: "String", comment: `Carpeta de los CSV de la librería ${l.sas_name}`, value: l.path ?? "", secret: false, needsValue: false, envs: null }));
  const vars = (plan.context_variables as ContextVariable[]).map((c): ContextRow => {
    const secret = Boolean(c.is_secret);
    return {
      name: toContext("&" + c.name).replace(/^context\./, ""),
      type: studioType(c.talend_type),
      comment: c.sas_line ? `Viene de la línea ${c.sas_line} del SAS` : "Viene de una macrovariable del SAS",
      value: secret ? "" : (c.sas_value ?? c.suggested ?? ""),
      secret,
      needsValue: secret || Boolean(c.needs_value) || !(c.sas_value ?? c.suggested),
      envs: c.group_values ?? null,
    };
  });
  return [...dirs, ...vars];
}

/** Ambientes que hay que crear en Studio (Configure Contexts): los que alguna variable distingue. */
export function contextEnvs(rows: ContextRow[]): Env[] {
  return CONTEXT_ENVS.filter((env) => rows.some((r) => r.envs && env in r.envs));
}

export const contextSummary = (rows: ContextRow[]) => ({
  total: rows.length,
  secrets: rows.filter((r) => r.secret).length,
  pending: rows.filter((r) => r.needsValue && !r.secret).length,
});
