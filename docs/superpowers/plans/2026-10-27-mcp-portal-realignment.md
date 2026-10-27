# Talend MCP and Portal Realignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task by task. Steps use checkbox syntax for tracking.

**Goal:** Align the updated Talend MCP, its Studio Bridge, and the portal while allowing only safe retries of failed, unapplied Jobs.

**Architecture:** Update the MCP checkout from its fetched upstream branch while retaining the portal-required `talend_job_apply_custom_spec` in the `agent` preset. Keep the portal's batch retry safeguards and extend them to per-Job operation state only when a fresh inventory says the target is absent and no prior result exists.

**Tech Stack:** Bun/TypeScript, Talend Studio Bridge (Java/Eclipse), FastAPI/Python, React.

**Spec:** Current user request in this Codex conversation; repo contracts in both `talend-mcp/AGENTS.md` and portal tests.

## Global Constraints

- Do not execute, compile, or publish migrated Jobs during this alignment task.
- Preserve existing uncommitted changes in both repositories.
- Keep the portal's custom-spec MCP tool available in the `agent` preset.
- Never allow a changed revision to overwrite an applied Job or a Job with a non-null result.
- Do not hot-reload the Studio Bridge while a Studio job or dialog is in progress.
- Do not start duplicate local services or change their ports.

## Review Focus

- The upstream MCP update must still expose `talend_job_apply_custom_spec` to the portal's agent-preset server.
- A stale failed operation with no result must be retryable only when fresh preflight confirms the Job is absent.
- Any applied result, partial batch result, or in-progress operation must continue to block revision reset.
- Actual destination conflicts must remain conflicts even if a retry is requested.
- Studio's active editor must not be modified or closed as part of Bridge installation.

---

### Task 1: Update and verify the MCP checkout

**Files:**
- Merge fetched `origin/main` into the current MCP checkout.
- Preserve the existing local change that includes `talend_job_apply_custom_spec` in `src/server/registered-tools/preset-sets.ts` and its preset test.

**Interfaces:**
- The portal requires the canonical `talend_job_apply_custom_spec` tool in the `agent` preset.
- The Studio Bridge must serve the routes expected by the updated MCP server.

- [x] Review the upstream merge tree and confirm it preserves the custom-spec tool implementation.
- [x] Merge `origin/main`, then restore/verify the portal-required agent-preset entry.
- [x] Run `bun run typecheck`, `bun test`, and `bun run verify`.
- [x] Compile Java bridge tests without reloading Studio.

### Task 2: Allow safe retry after the failed connector revision

**Files:**
- Modify `apps/api/main.py` to permit prior failed per-Job state with `result is None` only for a fresh preflight-confirmed missing target.
- Modify `src/sas_grid_migrator/persistence/store.py` only as needed for resetting a fully unapplied failed/conflict batch revision.
- Add behavior tests in `tests/integration/test_api_talend_batch.py` and `tests/unit/test_store_talend_apply_batch.py`.

**Interfaces:**
- The batch route already passes the set of programs missing from the fresh Talend inventory.
- A permitted retry reuses the same program list and queues those missing Jobs under the new revision.

- [x] Add failing tests for the current per-Job revision rejection and batch conflict state.
- [x] Confirm tests fail for the stale-revision guard.
- [x] Implement the narrow reset path; preserve rejection for any prior result or non-missing destination.
- [x] Run the focused tests, then the full portal suite and Ruff.

### Task 3: Align the live services without running migrated Jobs

**Files:**
- No product code beyond Tasks 1–2.

**Interfaces:**
- Portal health must report the MCP tool, MCP server, Bridge, and write permission as ready.
- MCP server and Bridge versions must correspond to the updated local checkout.

- [x] Verify portal health and fresh project preflight are read-only and report all five targets absent.
- [x] Check the Bridge build; `bridge:install` confirmed the active Studio bundle already matches and did not reload it. The MCP server already exposes the needed tool; the fetched upstream changes were fixtures/docs.
- [x] Verify MCP tool discovery and portal health again; do not call apply/execute tools.
