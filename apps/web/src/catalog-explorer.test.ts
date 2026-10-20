import { expect, test } from "bun:test";
import currentGuides from "../../../rules/talend/component-documentation-index.json" with { type: "json" };
import { filterCatalogItems, getGuideCatalogItems } from "./catalog-explorer";

const scope = { core: ["tFilterRow", "tDBInput"], alternatives: ["tMap"] };

test("builds a minimal current migration candidate scope", () => {
  expect(getGuideCatalogItems(scope)).toEqual([
    { name: "tDBInput", scope: "principal" },
    { name: "tFilterRow", scope: "principal" },
    { name: "tMap", scope: "alternativa" },
  ]);
});

test("active mapping candidates all exist in the current Studio 8 guide index", () => {
  const names = new Set(currentGuides.components.map((item) => item.name));
  expect(getGuideCatalogItems().length).toBe(47);
  expect(getGuideCatalogItems().every((item) => names.has(item.name))).toBe(true);
});

test("filters current component items by text and family", () => {
  const items = [
    { name: "tFilterRow", description: "Filters data rows", families: ["Processing"] },
    { name: "tDBInput", description: "Reads database rows", families: ["Databases"] },
  ];
  expect(filterCatalogItems(items, { query: "database" }).map((item) => item.name)).toEqual(["tDBInput"]);
  expect(filterCatalogItems(items, { family: "Processing" }).map((item) => item.name)).toEqual(["tFilterRow"]);
});

test("searches current framework metadata", () => {
  const items = [{ name: "cAMQP", description: "", families: [], search_terms: ["Camel"] }];
  expect(filterCatalogItems(items, { query: "camel" })).toEqual(items);
});
