import { expect, test } from "bun:test";
import { api } from "./api";

test("encodes file path segments without losing directory separators", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  globalThis.fetch = (async (input: RequestInfo | URL) => {
    requested = String(input);
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.program("project", "folder/a ?#.sas");
    expect(requested).toBe("/api/projects/project/programs/folder/a%20%3F%23.sas");
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("translates network failures into a clear Spanish message", async () => {
  const originalFetch = globalThis.fetch;
  globalThis.fetch = (async () => { throw new TypeError("Load failed"); }) as unknown as typeof fetch;
  try {
    await expect(api.projects()).rejects.toThrow("No se pudo completar la solicitud. Comprueba tu conexión e inténtalo de nuevo.");
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("batch creation sends the revision that the user reviewed", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response("{}", { status: 202 });
  }) as typeof fetch;
  try {
    await api.talendApplyBatch("project", "a".repeat(64));
    expect(requested).toBe("/api/projects/project/talend-apply-batch");
    expect(body).toEqual({ expected_revision: "a".repeat(64) });
  } finally {
    globalThis.fetch = originalFetch;
  }
});
