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

test("job metadata update encodes the program path and sends the body", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let method = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    method = String(init?.method);
    body = JSON.parse(String(init?.body));
    return new Response(JSON.stringify({ plan: {}, warnings: [] }), { status: 200 });
  }) as typeof fetch;
  try {
    await api.updateJobMeta("p", "dir/a ?#.sas", { job_name: "x", description: null });
    expect(method).toBe("PATCH");
    expect(requested).toBe("/api/projects/p/plans/dir/a%20%3F%23.sas/meta");
    expect(body).toEqual({ job_name: "x", description: null });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("translate posts the SAS source to the translator", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let method = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    method = String(init?.method);
    body = JSON.parse(String(init?.body));
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.translate("a");
    expect(method).toBe("POST");
    expect(requested).toBe("/api/translator/translate");
    expect(body).toEqual({ sas: "a" });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("bulk rename sends the list of renames", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response(JSON.stringify({ renamed: 1, warnings: ["Aviso de Studio"] }), { status: 200 });
  }) as typeof fetch;
  try {
    const result = await api.renameJobs("p", [{ program: "dir/a.sas", job_name: "job_a" }]);
    expect(result.warnings).toEqual(["Aviso de Studio"]);
    expect(requested).toBe("/api/projects/p/plans/rename");
    expect(body).toEqual({ renames: [{ program: "dir/a.sas", job_name: "job_a" }] });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("rename preview posts the rule to the preview route", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response("[]", { status: 200 });
  }) as typeof fetch;
  try {
    const rule = { mode: "prefix" as const, text: "ETL_" };
    await api.renamePreview("p", rule);
    expect(requested).toBe("/api/projects/p/plans/rename-preview");
    expect(body).toEqual(rule);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("expression edit patches the encoded step and expression index", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.editExpression("p", "dir/a.sas", "step 1/x", 2, "Trim(x)");
    expect(requested).toBe("/api/projects/p/plans/dir/a.sas/steps/step%201%2Fx/expressions/2");
    expect(body).toEqual({ talend: "Trim(x)" });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("naming example url-encodes the template in the query string", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  globalThis.fetch = (async (input: RequestInfo | URL) => {
    requested = String(input);
    return new Response(JSON.stringify({ example: "x", error: null }), { status: 200 });
  }) as typeof fetch;
  try {
    await api.namingExample("{a}&{b} c");
    expect(requested).toBe("/api/settings/naming/example?template=%7Ba%7D%26%7Bb%7D%20c");
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("progress and pending summary read their project routes", async () => {
  const originalFetch = globalThis.fetch;
  const requested: string[] = [];
  globalThis.fetch = (async (input: RequestInfo | URL) => {
    requested.push(String(input));
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.progress("p");
    await api.pendingSummary("p");
    expect(requested).toEqual(["/api/projects/p/progress", "/api/projects/p/pending-summary"]);
  } finally {
    globalThis.fetch = originalFetch;
  }
});
