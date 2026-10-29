import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ComponentIcon } from "./ComponentIcon";

test("does not request community icons for official-only components", () => {
  expect(renderToStaticMarkup(<ComponentIcon name="tUnlistedFixture" available={false} />)).toBe("");
});

test("requests each component's canvas icon from Talend", () => {
  expect(renderToStaticMarkup(<ComponentIcon name="tJava" />))
    .toContain('/api/talend/catalog/tJava/icon');
  expect(renderToStaticMarkup(<ComponentIcon name="tFileInputDelimited" />))
    .toContain('/api/talend/catalog/tFileInputDelimited/icon');
});
