# Project Talend Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let one project-level portal action create every Talend Job from one ZIP and report durable progress and results per guide.

**Architecture:** FastAPI will persist one batch operation per project and run existing per-Job MCP applications sequentially in the dependency order. It will reconcile nested `childJobs` returned by MCP into the matching project guides so confirmed children are recorded and skipped as independent calls. The React plans view will start/poll the batch and show the result for every Job; individual guides become read-only for Talend implementation.

**Tech Stack:** FastAPI, Pydantic, SQLite, existing Talend MCP adapter, React, TypeScript, Bun, pytest.

**Spec:** [2026-10-23-project-talend-batch-design.md](../specs/2026-10-23-project-talend-batch-design.md)

## Global Constraints

- One ZIP remains one isolated project; the batch is keyed by `project_id`.
- Reuse the existing `talend_job_apply_custom_spec` contract and never write Talend `.item` or `.properties` files directly.
- Invoke MCP sequentially; do not run Talend Jobs.
- Preserve the existing ZIP-relative destination and store incomplete technical details in the generated Job context without inventing source values.
- A changed plan revision or destination conflict must not silently overwrite a Job.
- Persist batch and per-Job status in SQLite so refresh/reopen and server restart are observable; a restart changes running work to `interrupted`.
- A confirmed nested `childJobs` result counts for its guide and must not cause a second independent MCP apply call.
- Continue attempting unconfirmed remaining guides after an individual apply failure and report every outcome.
- Preserve all preexisting working-tree changes. Do not commit the shared checkout because it already contains unrelated/preexisting changes.
- Use the existing local FastAPI/SQLite architecture; do not add a distributed queue or dependencies.

## Review Focus

- A child created recursively by MCP is reconciled by Job name and folder and is not submitted again; cover nested, repeated-name-in-different-folder, and unconfirmed-child-after-error cases in batch tests.
- Dependency layers produce stable order, including missing graph entries and cycles; cover deterministic order and no lost plans.
- Concurrent/repeated start requests do not create two active batches; cover atomic start/reuse and duplicate POST behavior.
- A failure or conflict for one Job does not hide later results; cover mixed success/failure and all-failure final states.
- Restart and retry preserve completed Jobs while allowing failed, partial, or interrupted work to resume; cover state recovery and same/different revision behavior.
- No plans, read-only MCP, unavailable Bridge, and an empty project cannot report successful implementation; cover API validation and UI disabled/error states.
- One project’s progress never appears in another project; cover Store and API isolation by `project_id`.

---

### Task 1: Add durable batch state and deterministic planning helpers

**Files:**
- Modify: `src/sas_grid_migrator/persistence/store.py`
- Create: `src/sas_grid_migrator/talend_adapter/batch.py`
- Test: `tests/unit/test_store_talend_apply_batch.py`
- Test: `tests/unit/test_talend_apply_batch.py`

**Interfaces:**
- `Store.get_talend_apply_batch_state(project_id: str) -> dict | None` returns revision, state, ordered programs, current program, completed count, per-program results, error, attempt count, and timestamps.
- `Store.begin_talend_apply_batch(project_id: str, revision_hash: str, programs: list[str]) -> tuple[dict, bool]` atomically reuses an active/completed same-revision operation, starts an eligible retry, or reports a revision conflict.
- `Store.update_talend_apply_batch_state(project_id: str, *, status: str, jobs: list[dict], current_program: str | None, completed_count: int, error: str | None = None) -> dict` persists each transition.
- `order_plans_for_batch(plans: list[JobPlan], processing_order: list[list[str]]) -> list[JobPlan]` emits each plan once in dependency-layer order, then appends unlisted plans by normalized relative path.
- `collect_child_results(result: dict[str, Any]) -> list[dict[str, Any]]` flattens the MCP `childJobs` result tree while retaining each child’s name, folder, result summary, and nested identity.

- [ ] **Step 1: Write Store tests first** for project isolation, atomic duplicate-start reuse, same-revision retry after partial/interrupted states, changed-revision conflict, and restart recovery of a running batch.
- [ ] **Step 2: Run the Store test file and verify the expected missing-method failures.**

Run: `uv run pytest tests/unit/test_store_talend_apply_batch.py -q`

Expected: FAIL because the batch persistence API/table is absent.

- [ ] **Step 3: Add the SQLite batch ledger and the three Store methods** in `src/sas_grid_migrator/persistence/store.py`. Extend `recover_interrupted_operations()` to mark running batches interrupted. Keep one current row per project and update it inside transactions.
- [ ] **Step 4: Rerun Store tests and verify they pass.**

Run: `uv run pytest tests/unit/test_store_talend_apply_batch.py -q`

Expected: PASS, including isolation and restart recovery.

- [ ] **Step 5: Write helper tests first** for dependency layer order, deterministic tie/cycle ordering, missing graph programs, duplicate paths, and recursive MCP child result flattening.
- [ ] **Step 6: Run the helper test file and verify it fails because helpers are missing.**

Run: `uv run pytest tests/unit/test_talend_apply_batch.py -q`

Expected: FAIL because `batch.py` does not expose the requested helpers.

- [ ] **Step 7: Implement the two pure helpers** in `src/sas_grid_migrator/talend_adapter/batch.py` and export them from the package only if the package’s current convention requires it.
- [ ] **Step 8: Rerun Store and helper tests.**

Run: `uv run pytest tests/unit/test_store_talend_apply_batch.py tests/unit/test_talend_apply_batch.py -q`

Expected: PASS.

### Task 2: Orchestrate the batch through the existing MCP apply operation

**Files:**
- Modify: `apps/api/main.py`
- Modify: `src/sas_grid_migrator/persistence/store.py` only if Task 1 interfaces need a transaction-level refinement
- Test: `tests/integration/test_api_talend_batch.py`
- Reuse: `tests/integration/test_api_talend_workspace.py` fixtures/patterns for fake MCP and project ZIP uploads

**Interfaces:**
- `POST /api/projects/{project_id}/talend-apply-batch` returns HTTP 202 and the durable batch snapshot; repeated starts return the active/successful same-revision snapshot, while eligible terminal partial/failed/interrupted states schedule a retry.
- `GET /api/projects/{project_id}/talend-apply-batch` returns the durable snapshot with per-program states and concise outcomes.
- `async _apply_talend_plan(project_id: str, program: str) -> dict` becomes the shared single-Job application path used by both the legacy per-Job POST and the new batch worker; it preserves existing revision checks, context behavior, errors, and per-Job state.
- `async _run_talend_apply_batch(project_id: str, revision_hash: str, ordered_programs: list[str]) -> None` runs one MCP request at a time, updates progress after every result, reconciles nested child results, and continues after per-Job errors.

- [x] **Step 1: Write integration tests first** for no plans, write-disabled MCP, atomic duplicate-start reuse, dependency order, one call per unconfirmed guide, child result reconciliation and skip, repeated Job names in separate folders, distinct projects, progress polling, mixed/all failures, same-revision retry, changed-revision conflict, and interrupted recovery.
- [x] **Step 2: Run the new integration test file and verify it fails because the batch endpoints are missing.**

Run: `uv run pytest tests/integration/test_api_talend_batch.py -q`

Expected: FAIL because the batch endpoints are missing (the initial POST returned 405; the missing GET returned 404).

- [x] **Step 3: Refactor the per-Job endpoint** so spec construction, revision checks, write validation, MCP invocation, and per-Job persistence live in `_apply_talend_plan`; keep the existing route contract unchanged.
- [x] **Step 4: Add the batch start/read endpoints.** Build each plan’s spec and project folder from the current `PlanSet`; hash the ordered revisions and folders to identify the batch; use `order_plans_for_batch`; atomically claim the operation and schedule FastAPI `BackgroundTasks` only when a new/retry attempt starts.
- [x] **Step 5: Implement the worker.** Before applying, restore completed outcomes from a prior same-revision attempt and existing per-Job state. Run each unconfirmed plan sequentially through `_apply_talend_plan`. After MCP success, flatten `childJobs`, match child plans by normalized `(jobName, folderPath)`, persist their concise outcomes in the batch snapshot, and skip those plans later. If a parent call throws before returning child results, leave children unconfirmed and let their own guide attempt run. Persist current program and completed count after each transition. Derive the terminal batch state from all per-guide results.
- [x] **Step 6: Rerun the integration tests and verify each status/result behavior.**

Run: `uv run pytest tests/integration/test_api_talend_batch.py tests/integration/test_api_talend_workspace.py -q`

Expected: PASS; legacy single-Job apply contract remains green and the batch never calls a Job execution tool.

### Task 3: Replace individual implementation actions with one project-level action

**Files:**
- Modify: `apps/web/src/api.ts`
- Modify: `apps/web/src/types.ts`
- Modify: `apps/web/src/views/PlansTab.tsx`
- Modify: `apps/web/src/styles.css`
- Test: `apps/web/src/api.test.mjs`
- Test: `apps/web/src/views/PlansTab.test.mjs`

**Interfaces:**
- `api.talendApplyBatch(id: string) -> Promise<TalendApplyBatchState>` starts the project operation.
- `api.talendApplyBatchStatus(id: string) -> Promise<TalendApplyBatchState>` reads its progress.
- `TalendApplyBatchState` exposes `status`, `revision_hash`, `total_jobs`, `completed_jobs`, `current_program`, ordered `jobs` with state/result/error, and timestamps.

- [x] **Step 1: Add frontend tests first** for the API routes, one project-level button, disabled/no-plan/read-only states, polling while active, visible per-Job status and errors, child-job reconciliation display, and absence of the individual guide implementation button.
- [x] **Step 2: Run the focused Bun tests and verify the missing project action/API failures.**

Run: `bun test apps/web/src/api.test.mjs apps/web/src/views/PlansTab.test.mjs`

Expected: FAIL because batch API and project-level UI do not exist.

- [x] **Step 3: Add batch types and API methods** matching the API snapshot exactly.
- [x] **Step 4: Add the single implementation panel to `PlanList`.** Show ZIP/project identity and Job count, use MCP health to disable unsafe starts, post once, poll the durable endpoint while queued/running, and show `completed / total`, current program, per-Job outcome, retry action, and errors. Keep folders grouped through `ArchivePathTree`.
- [x] **Step 5: Remove the per-Job apply button from `PlanDetail`.** Retain last result/status as read-only, using the project batch snapshot for Jobs applied as nested children and the existing per-Job status endpoint for legacy operations. Keep pending contexts and the warning that Talend Jobs are not executed.
- [x] **Step 6: Add responsive styles for the batch progress panel and result rows.** Do not invent a percentage; show the backend’s completed count.
- [x] **Step 7: Rerun focused Bun tests, then typecheck and build.**

Run: `bun test apps/web/src/api.test.mjs apps/web/src/views/PlansTab.test.mjs`

Expected: PASS.

Run: `bun run typecheck`

Expected: no TypeScript errors.

Run: `bun run build`

Expected: Vite build succeeds.

### Task 4: Document operation limits and verify the complete portal

**Files:**
- Modify: `README.md`
- Modify: `docs/talend-mcp-tools.md`
- Modify: `docs/zip-project-workspaces.md`
- Modify: `tests` only if a verified uncovered acceptance case requires a regression test

- [x] **Step 1: Document** the single project-level button, sequential MCP requests, status meanings, nested child reconciliation, retry behavior, Bridge prerequisites, and the fact that Jobs are not executed.
- [x] **Step 2: Run backend focused tests and frontend tests/typecheck/build.**

Run: `uv run pytest tests/unit/test_store_talend_apply_batch.py tests/unit/test_talend_apply_batch.py tests/integration/test_api_talend_batch.py tests/integration/test_api_talend_workspace.py -q`

Expected: PASS.

Run: `bun test`

Expected: PASS.

Run: `bun run typecheck`

Expected: no errors.

Run: `bun run build`

Expected: build succeeds.

- [x] **Step 3: Run the complete backend suite** and record any already-known golden-fixture mismatches separately from regressions.

Run: `uv run pytest -q`

Expected: all tests pass except the two previously recorded baseline golden mismatches, if those are still present.

- [x] **Step 4: Inspect the final diff and confirm no unrelated dirty files were reverted or committed.**
