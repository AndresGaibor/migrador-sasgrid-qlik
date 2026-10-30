// Lógica pura del panel «Lo que NO hace falta migrar»: agrupa la fontanería de SAS por su descripción.
import type { NotMigrated } from "../types";

export type NotMigratedGroup = {
  /** Descripción de la fontanería (`what`); es la clave de agrupación. */
  what: string;
  category: string;
  reason: string;
  talend_equivalent: string;
  /** Líneas SAS únicas y ordenadas donde aparece. */
  lines: number[];
  /** Número de entradas del plan que caen en este grupo. */
  count: number;
};

/** Número total de entradas (cada una es una aparición de fontanería). */
export function countNotMigrated(items: NotMigrated[]): number {
  return items.length;
}

/**
 * Agrupa por `what`: la misma fontanería repetida en varias líneas aparece una vez con todas sus líneas.
 * Ordena los grupos por su primera línea.
 */
export function groupNotMigrated(items: NotMigrated[]): NotMigratedGroup[] {
  const groups = new Map<string, NotMigratedGroup>();
  for (const item of items) {
    const current = groups.get(item.what);
    if (current) {
      current.count += 1;
      current.lines = uniqueSorted([...current.lines, ...item.lines]);
    } else {
      groups.set(item.what, {
        what: item.what,
        category: item.category,
        reason: item.reason,
        talend_equivalent: item.talend_equivalent,
        lines: uniqueSorted(item.lines),
        count: 1,
      });
    }
  }
  return [...groups.values()].sort((a, b) => firstLine(a) - firstLine(b));
}

function uniqueSorted(values: number[]): number[] {
  return [...new Set(values)].sort((a, b) => a - b);
}

function firstLine(group: NotMigratedGroup): number {
  return group.lines[0] ?? Number.MAX_SAFE_INTEGER;
}
