import auditSource from "../../../rules/talend/catalog-audit.json" with { type: "json" };

export type VerificationStatus = "partially_verified" | "needs_review" | "unverified";
export type GuideScope = "principal" | "alternativa";

export type AuditRecord = {
  catalog_entry_present: boolean;
  catalog_family: string[] | null;
  official_family: string | null;
  official_version: string | null;
  official_purpose: string | null;
  official_url: string | null;
  official_reference_scope?: string | null;
  checked_at?: string | null;
  verification_status: VerificationStatus;
  catalog_internal_property_names: string[];
  official_essential_property_labels: string[];
  property_comparison_status?: string;
  limitations: string[];
};

export type CatalogAudit = {
  official_documentation_version: string;
  installed_environment_status: string;
  target_version: {
    product: string;
    major_version: string;
    monthly_release: string;
    status: string;
  };
  mapping_scope: {
    core_components_required_for_catalog: string[];
    conditional_alternative_components: string[];
  };
  recommended_components: Record<string, AuditRecord>;
};

export type GuideCatalogItem = {
  name: string;
  description: string;
  families: string[];
  parameters: number;
  scope: GuideScope;
  audit: AuditRecord;
};

export const catalogAudit = auditSource as CatalogAudit;

export function getGuideCatalogItems(audit: CatalogAudit = catalogAudit): GuideCatalogItem[] {
  const core = new Set(audit.mapping_scope.core_components_required_for_catalog);
  const alternatives = new Set(audit.mapping_scope.conditional_alternative_components);
  return [...core, ...alternatives]
    .sort((a, b) => a.localeCompare(b))
    .flatMap((name) => {
      const record = audit.recommended_components[name];
      if (!record) return [];
      return [{
        name,
        description: record.official_purpose ?? "Función oficial pendiente de confirmar.",
        families: record.official_family ? [record.official_family] : record.catalog_family ?? [],
        parameters: record.catalog_internal_property_names.length,
        scope: core.has(name) ? "principal" as const : "alternativa" as const,
        audit: record,
      }];
    });
}

export function filterCatalogItems<T extends { name: string; description: string; families: string[]; audit?: AuditRecord }>(
  items: T[],
  filters: { query?: string; family?: string; verification?: string },
): T[] {
  const query = normalize(filters.query ?? "");
  return items.filter((item) => {
    if (filters.family && !item.families.some((family) => normalize(family) === normalize(filters.family!))) return false;
    if (filters.verification && item.audit?.verification_status !== filters.verification) return false;
    if (!query) return true;
    return [item.name, item.description, ...item.families].some((value) => normalize(value).includes(query));
  });
}

export function provenanceLabel(status?: string): string {
  if (status === "partially_verified") return "Referencia oficial cotejada parcialmente";
  if (status === "needs_review") return "Requiere revisión documental";
  if (status === "unverified") return "Sin verificar con fuente oficial";
  return "Fuera del alcance auditado";
}

function normalize(value: string): string {
  return value.toLocaleLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();
}
