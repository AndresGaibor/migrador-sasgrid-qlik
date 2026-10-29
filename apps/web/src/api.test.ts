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

test("Job metadata edit encodes the source path and sends name and description", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response(JSON.stringify({ plan: {} }), { status: 200 });
  }) as typeof fetch;
  try {
    await api.updateJobMeta("project", "folder/daily file.sas", "daily_load", "Carga diaria");
    expect(requested).toBe("/api/projects/project/plans/folder/daily%20file.sas/meta");
    expect(body).toEqual({ job_name: "daily_load", description: "Carga diaria" });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("expression edits encode the program and step and send the replacement", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.editExpression("project", "src/daily job.sas", "step / one", 0, "input_row.amount > 0");
    expect(requested).toBe("/api/projects/project/plans/src/daily%20job.sas/steps/step%20%2F%20one/expressions/0");
    expect(body).toEqual({ talend: "input_row.amount > 0" });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("translator sends the SAS text to the translator endpoint", async () => {
  const originalFetch = globalThis.fetch;
  let requested = "";
  let body: unknown;
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requested = String(input);
    body = JSON.parse(String(init?.body));
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.translate("nombre = 'Ana'");
    expect(requested).toBe("/api/translator/translate");
    expect(body).toEqual({ sas: "nombre = 'Ana'" });
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("bulk rename preview and apply use their project endpoints", async () => {
  const originalFetch = globalThis.fetch;
  const requests: Array<{ path: string; body: unknown }> = [];
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requests.push({ path: String(input), body: JSON.parse(String(init?.body)) });
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    const rule = { mode: "prefix" as const, text: "fin_" };
    const renames = [{ program: "daily.sas", job_name: "fin_daily" }];
    await api.renamePreview("project", rule);
    await api.renameJobs("project", renames);
    expect(requests).toEqual([
      { path: "/api/projects/project/plans/rename-preview", body: rule },
      { path: "/api/projects/project/plans/rename", body: { renames } },
    ]);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("naming template reads, previews and saves the template", async () => {
  const originalFetch = globalThis.fetch;
  const requests: Array<{ path: string; method: string; body?: unknown }> = [];
  globalThis.fetch = (async (input: RequestInfo | URL, init?: RequestInit) => {
    requests.push({
      path: String(input),
      method: init?.method ?? "GET",
      body: init?.body ? JSON.parse(String(init.body)) : undefined,
    });
    return new Response("{}", { status: 200 });
  }) as typeof fetch;
  try {
    await api.namingTemplate();
    await api.namingExample("fin_{programa}");
    await api.setNamingTemplate("fin_{programa}");
    expect(requests).toEqual([
      { path: "/api/settings/naming", method: "GET", body: undefined },
      { path: "/api/settings/naming/preview", method: "POST", body: { template: "fin_{programa}" } },
      { path: "/api/settings/naming", method: "PUT", body: { template: "fin_{programa}" } },
    ]);
  } finally {
    globalThis.fetch = originalFetch;
  }
});
