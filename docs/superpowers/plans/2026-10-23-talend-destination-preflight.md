# Talend Destination Preflight Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconcile the portal's saved batch state with a complete, fresh Talend Job inventory before applying a ZIP project.

**Architecture:** Paginate the existing read-only MCP list tool, classify each desired Job against its exact Talend folder, expose a read-only preflight endpoint, and repeat that check before scheduling writes. Only a conflict-free preflight may retry a same-revision conflict batch. The React panel presents each action.

**Tech Stack:** FastAPI, Python, SQLite, existing Talend MCP adapter, React, TypeScript, Bun, pytest.

**Spec:** [2026-10-23-talend-destination-preflight-design.md](../specs/2026-10-23-talend-destination-preflight-design.md)

## Global Constraints

- Reuse `talend_jobs_list` and `talend_job_apply_custom_spec`.
- Create or edit Jobs through Talend Studio APIs; never write `.item` or `.properties` files.
- Apply requests remain sequential; no Talend Job is compiled or executed.
- Only exact project-folder matches may be updated; ambiguous same-name Jobs elsewhere block the batch.
- An incomplete MCP inventory never authorizes a write.
- When the fresh inventory says a previously completed Job is missing, retry only that Job.

## Review Focus

- Inventory larger than 50 Jobs: tests assert every page is read.
- Windows separators and case differences: tests assert equivalent paths match.
- Same name outside the target: tests assert zero writes.
- A stale conflict after deletion: tests assert a fresh safe preflight enables retry.
- A deleted Job from an otherwise successful batch: tests assert only the missing program is retried.
- MCP unavailable or incomplete pagination: tests assert fail-closed behavior.

---

### Task 1: Complete inventory and pure preflight classification

**Files:**
- Modify: `src/sas_grid_migrator/talend_adapter/adapter.py`
- Create: `src/sas_grid_migrator/talend_adapter/preflight.py`
- Test: `tests/unit/test_talend_adapter.py`
- Create: `tests/unit/test_talend_preflight.py`

**Interfaces:**
- `TalendAdapter.list_jobs() -> list[dict[str, Any]]` returns every MCP inventory page.
- `classify_jobs(specs, inventory) -> dict` returns per-Job actions and conflict reasons.

- [x] Write tests for multi-page reads, incomplete pages, and the create/update/conflict actions; run them and confirm failure.
- [x] Implement complete pagination and path/name classification; run focused tests.

### Task 2: Fresh API checks and safe retry

**Files:**
- Modify: `apps/api/main.py`
- Modify: `src/sas_grid_migrator/persistence/store.py`
- Test: `tests/integration/test_api_talend_batch.py`
- Test: `tests/unit/test_store_talend_apply_batch.py`

**Interfaces:**
- `GET /api/projects/{project_id}/talend-apply-batch/preflight` returns availability, per-Job actions, and counts.
- Batch POST rechecks preflight; collisions or unavailable MCP cause zero writes.
- `Store.begin_talend_apply_batch(..., retry_conflicts=False, retry_programs=None)` reopens a conflict state only after fresh preflight and selectively retries previously applied programs missing from inventory.
- Batch application may bypass saved per-Job conflicts only after that fresh check and if the revision still matches.

- [x] Add API and Store tests for stale conflicts, remaining collisions, unavailable MCP, missing applied Jobs, and revision guards; verify failure.
- [x] Implement the endpoint and guarded retry; run focused tests.

### Task 3: Visible preflight in the project panel

**Files:**
- Modify: `apps/web/src/api.ts`
- Modify: `apps/web/src/types.ts`
- Modify: `apps/web/src/views/PlansTab.tsx`
- Modify: `apps/web/src/styles.css`
- Test: `apps/web/src/api.test.mjs`
- Test: `apps/web/src/views/PlansTab.test.mjs`

- [x] Add tests for the preflight route, action labels, stale conflict messaging, and disabled states; verify failure.
- [x] Render create/update/conflict counts and destination paths; request fresh preflight on click and run frontend tests, typecheck, and build.

Do not commit: this checkout already contains unrelated user changes.
