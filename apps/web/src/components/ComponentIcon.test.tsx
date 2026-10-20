import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ComponentIcon } from "./ComponentIcon";

test("does not request community icons for official-only components", () => {
  expect(renderToStaticMarkup(<ComponentIcon name="tUnlistedFixture" available={false} />)).toBe("");
});
