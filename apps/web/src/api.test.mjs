import assert from "node:assert/strict";
import test from "node:test";
import { api } from "./api.ts";

test("ZIP upload creates a project in one multipart request", async () => {
  const originalFetch = globalThis.fetch;
  let request;
  globalThis.fetch = async (input, init) => {
    request = { input: String(input), init };
    return new Response(JSON.stringify({ project: { id: "project-1" }, processing: { status: "queued" } }), {
      status: 201,
      headers: { "Content-Type": "application/json" },
    });
  };
  try {
    const file = new File(["zip bytes"], "banking.zip", { type: "application/zip" });
    const result = await api.createProjectFromZip(file, "Banking");
    assert.equal(result.project.id, "project-1");
  } finally {
    globalThis.fetch = originalFetch;
  }
  assert.equal(request.input, "/api/projects/uploads");
  assert.equal(request.init.method, "POST");
  assert.equal(request.init.body.get("file").name, "banking.zip");
  assert.equal(request.init.body.get("name"), "Banking");
  assert.equal(request.init.headers, undefined);
});

test("project processing and Talend batch APIs use project-scoped routes", async () => {
  const originalFetch = globalThis.fetch;
  const requests = [];
  globalThis.fetch = async (input, init) => {
    requests.push({ input: String(input), init });
    return new Response(JSON.stringify({ status: "running" }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  };
  try {
    await api.processing("project-1");
    await api.retryProcessing("project-1");
    await api.analysis("project-1");
    await api.talendApplyPreview("project-1", "Banking/daily.sas");
    await api.talendApplyStatus("project-1", "Banking/daily.sas");
    await api.talendApplyBatch("project-1");
    await api.talendApplyBatchStatus("project-1");
  } finally {
    globalThis.fetch = originalFetch;
  }
  assert.deepEqual(requests.map((request) => request.input), [
    "/api/projects/project-1/processing",
    "/api/projects/project-1/processing/retry",
    "/api/projects/project-1/analyses",
    "/api/projects/project-1/plans/Banking/daily.sas/talend-apply/preview",
    "/api/projects/project-1/plans/Banking/daily.sas/talend-apply",
    "/api/projects/project-1/talend-apply-batch",
    "/api/projects/project-1/talend-apply-batch",
  ]);
  assert.equal(requests[0].init.method, undefined);
  assert.equal(requests[1].init.method, "POST");
  assert.equal(requests[2].init.method, undefined);
  assert.equal(requests[3].init.method, "POST");
  assert.equal(requests[4].init.method, undefined);
  assert.equal(requests[5].init.method, "POST");
  assert.equal(requests[6].init.method, undefined);
});
