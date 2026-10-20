import scopeSource from "../../../rules/talend/migration-candidate-scope.json" with { type: "json" };

export type GuideScope = "principal" | "alternativa";
export type GuideCatalogItem = { name: string; scope: GuideScope };
type MigrationCandidateScope = { core: string[]; alternatives: string[] };

export function getGuideCatalogItems(scope: MigrationCandidateScope = scopeSource as MigrationCandidateScope): GuideCatalogItem[] {
  return [
    ...scope.core.map((name) => ({ name, scope: "principal" as const })),
    ...scope.alternatives.map((name) => ({ name, scope: "alternativa" as const })),
  ].sort((a, b) => a.name.localeCompare(b.name));
}

export function filterCatalogItems<T extends {
  name: string;
  description: string;
  families: string[];
  search_terms?: string[];
}>(items: T[], filters: { query?: string; family?: string }): T[] {
  const query = normalize(filters.query ?? "");
  const selectedFamily = normalize(filters.family ?? "");
  return items.filter((item) => {
    if (selectedFamily && !item.families.some((family) => normalize(family) === selectedFamily)) return false;
    if (!query) return true;
    return [item.name, item.description, ...item.families, ...(item.search_terms ?? [])]
      .some((value) => normalize(value).includes(query));
  });
}

function normalize(value: string): string {
  return value.toLocaleLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();
}
