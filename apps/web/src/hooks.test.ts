import { expect, test } from "bun:test";
import { decodeHash } from "./hooks";

test("decodes valid routes and defaults an empty hash to home", () => {
  expect(decodeHash("#/p/abc/Mi%20proyecto")).toBe("/p/abc/Mi proyecto");
  expect(decodeHash("")).toBe("/");
});

test("preserves malformed routes so the app can show its not-found state", () => {
  expect(decodeHash("#/p/%E0%A4%A")).toBe("/p/%E0%A4%A");
});
