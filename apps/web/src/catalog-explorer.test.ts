import { expect, test } from "bun:test";
import { filterCatalogItems, getGuideCatalogItems, provenanceLabel, type CatalogAudit } from "./catalog-explorer";

const audit: CatalogAudit = {
  mapping_scope: {
    core_components_required_for_catalog: ["tFilterRow", "tDBInput"],
    conditional_alternative_components: ["tMap"],
  },
  official_documentation_version: "Talend Studio 8.0 R2026-09 documentation baseline",
  installed_environment_status: "not available",
  target_version: { product: "Talend Studio", major_version: "8.0", monthly_release: "R2026-09", status: "documentation_target_environment_unconfirmed" },
  recommended_components: {
    tFilterRow: {
      catalog_entry_present: true,
      catalog_family: ["Processing"],
      official_family: "Processing",
      official_version: "8.0",
      official_purpose: "Filters rows in a flow.",
      official_url: "https://help.qlik.com/filterrow",
      verification_status: "partially_verified",
      catalog_internal_property_names: ["CONDITIONS"],
      official_essential_property_labels: ["Conditions"],
      limitations: [],
    },
    tDBInput: {
      catalog_entry_present: false,
      catalog_family: null,
      official_family: "Databases",
      official_version: "8.0",
      official_purpose: "Extracts data from a database.",
      official_url: "https://help.qlik.com/dbinput",
      verification_status: "needs_review",
      catalog_internal_property_names: [],
      official_essential_property_labels: [],
      limitations: ["No component-specific property page compared."],
    },
    tMap: {
      catalog_entry_present: true,
      catalog_family: ["Processing"],
      official_family: "Processing",
      official_version: "8.0",
      official_purpose: "Maps flows.",
      official_url: null,
      verification_status: "needs_review",
      catalog_internal_property_names: [],
      official_essential_property_labels: [],
      limitations: [],
    },
  },
};

test("builds guide component records and distinguishes core candidates from alternatives", () => {
  const items = getGuideCatalogItems(audit);
  expect(items.map((item) => [item.name, item.scope])).toEqual([
    ["tDBInput", "principal"],
    ["tFilterRow", "principal"],
    ["tMap", "alternativa"],
  ]);
  expect(items.find((item) => item.name === "tDBInput")?.audit.catalog_entry_present).toBe(false);
});

test("filters guide components by text, family and official verification status", () => {
  const items = getGuideCatalogItems(audit);
  expect(filterCatalogItems(items, { query: "dbinput" }).map((item) => item.name)).toEqual(["tDBInput"]);
  expect(filterCatalogItems(items, { family: "Processing" }).map((item) => item.name)).toEqual(["tFilterRow", "tMap"]);
  expect(filterCatalogItems(items, { verification: "needs_review" }).map((item) => item.name)).toEqual(["tDBInput", "tMap"]);
});

test("uses distinct labels for documentary provenance and Studio verification", () => {
  expect(provenanceLabel("partially_verified")).toBe("Referencia oficial cotejada parcialmente");
  expect(provenanceLabel("needs_review")).toBe("Requiere revisión documental");
})
