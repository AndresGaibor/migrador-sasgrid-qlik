# ZIP Project Workspaces Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Make every uploaded ZIP a distinct, traceable SAS project that the portal extracts and analyzes automatically, while preserving explicit per-Job MCP implementation and preventing cross-project Talend collisions.

**Architecture:** Add a single-upload endpoint that creates a project from a ZIP, stages and extracts it before publishing the project, then starts a bounded background pipeline. Persist ZIP metadata and each pipeline/apply operation in SQLite so the projects list and project detail can recover status after refresh. Keep current project-scoped source paths and analysis/planning services. Assign a stable Talend folder derived from the configured root, a safe archive slug, a stable project ID, and the archive's relative program folders. Existing projects remain addressable and are marked as legacy when no ZIP metadata exists.

**Tech Stack:** FastAPI, Pydantic, SQLite, existing SAS ingestion/analysis/dependency/planning modules, React, TypeScript, Vite, Bun.

**Spec:** [2026-10-23-zip-project-workspaces-design.md](../specs/2026-10-23-zip-project-workspaces-design.md)

## Global Constraints

- Preserve all existing working-tree changes; edit only the scoped files listed below and inspect diffs before each edit.
- Keep each ZIP's source, derived files, pipeline status, and Talend application state scoped by `project_id`.
- Reject an invalid ZIP before publishing a project; do not leave an empty project or partially extracted source folder.
- Keep analysis and planning failures visible and retryable without deleting the extracted source.
- Keep one upload's SAS files, dependencies, and Jobs separate from every other ZIP.
- Do not invent SAS connection, schema, context, or business values. Keep unresolved values pending in the Job context/instructions passed through the existing MCP adapter.
- Talend implementation remains an explicit per-Job action and must not execute Jobs. The first delivery does not add Job execution, Job updates, a distributed queue, or a remote database.
- Assign a per-project Talend folder under configurable `TALEND_APPLY_FOLDER`, preserving ZIP subfolders and using a stable project ID to avoid collisions. Reapplying an identical plan revision is safe; changed or unrelated existing Jobs must surface a conflict instead of being silently overwritten.
- Keep current ZIP traversal, size, and extraction protections. Bound background processing concurrency and state clearly that the SQLite/background-task deployment is single-instance; horizontal scaling requires a shared queue/store in a later phase.
- The user explicitly authorized tests, typecheck, and build at completion. Use test-first changes and keep verification scoped to the plan plus the final full suites.

## Review Focus

- An upload creates one and only one new project, and failed extraction leaves no published project or partial source.
- Upload response and subsequent status reads identify the original ZIP and preserve directory structure.
- The automatic pipeline uses only that project's source and persists stage, timestamps, and useful error/retry state.
- Project list and detail recover state after navigation/refresh and distinguish legacy projects with no recorded ZIP.
- Talend destinations remain unique per ZIP, while the Job guide still sends its current portal plan to the existing MCP apply flow.
- Pending technical details remain explicit and contextual; no Job runs as a side effect.
- APIs remain backward compatible for existing project creation, manual imports, analysis, plans, and Talend health.

---

### Task 1: Persist ZIP identity, project processing, and application operations

**Files:** `src/sas_grid_migrator/persistence/store.py`, `src/sas_grid_migrator/domain/models.py`

1. Extend the SQLite schema with backward-compatible columns or tables for the original ZIP filename, upload timestamp, archive SHA-256 and byte size, manifest summary, pipeline stage/status, current stage timestamps/message/error, retry count, and per-program Talend apply operation identity/status/timestamps/result/error.
2. Add narrow Store methods to atomically register a successfully imported ZIP project, fetch/list enriched project records, transition pipeline state, recover interrupted work on startup, and record/get Talend apply state. Keep data keyed by `project_id`; do not alter existing `step_state` semantics.
3. Migrate existing SQLite databases in place using idempotent schema setup. Projects with no upload metadata must serialize as legacy projects without fabricating an archive name.
4. Keep source/analysis/dependency/plan paths project-scoped. Ensure new registration never routes a ZIP through `import_batch()` in a way that replaces another project's snapshot.

**Interfaces:** Enriched `Project` serialization includes optional `archive_name`, `archive_sha256`, `archive_size_bytes`, `uploaded_at`, and a compact `processing` object. Store exposes status snapshots safe for the API and UI, with ISO timestamps and explicit states (`queued`, stage names, `completed`, `failed`, `interrupted`).

**Test first:** Add `tests/unit/test_store_project_state.py` for legacy project reads, ZIP metadata/state persistence, migration idempotency, and apply operation isolation by project/program. Run the focused pytest file and confirm it fails on the missing behavior before implementing Store/models; rerun it green after the change.

### Task 2: Create projects atomically from a ZIP and run automatic analysis

**Files:** `apps/api/main.py`, `src/sas_grid_migrator/persistence/store.py`, `src/sas_grid_migrator/ingestion/importer.py`, `src/sas_grid_migrator/config.py`

1. Add a multipart `POST /api/projects/uploads` endpoint accepting a ZIP and optional display name. Keep `POST /api/projects` and existing project-scoped import/upload routes for backward compatibility.
2. Stage the bounded upload and extraction in temporary storage. Reuse the current safe-path, symlink, extension, count, and size protections while writing to a staging directory; promote the complete source snapshot atomically before registering the project and roll back the promoted directory if registration fails. Validate that it is a supported, non-empty project ZIP before publishing. On failure, clean temporary files and return a useful 4xx response.
3. After atomic registration, return the new project plus its queued processing snapshot and schedule the existing analysis, dependency graph, and plan generation stages through FastAPI background processing. Persist each transition and error before moving to the next stage. Do not call Talend MCP during upload.
4. Add a status read/retry API scoped to a project. Retry derived processing from the already-extracted project; retain its source and expose interrupted/error states rather than resetting it silently. Keep legacy project-scoped import endpoints for projects without a source snapshot; reject a second ZIP/import on an already-populated project with a clear message instead of replacing its source.
5. Bound concurrent background project pipelines in configuration, expose relevant limits in the API health/config response, and use a FastAPI startup/lifespan hook (once per API process, not per Store instance) to recover persisted `running` and orphaned `queued` state as `interrupted` so the UI can offer retry. Document single-instance limits and avoid implying a distributed worker queue.
6. Add configurable archive/Talend folder slug policy only if needed by the existing `Settings`; do not put machine-specific paths in code.

**Interfaces:** `POST /api/projects/uploads` returns `{project, processing}`; `GET /api/projects/{project_id}/processing` returns the persisted status; `POST /api/projects/{project_id}/processing/retry` queues a retry and returns the updated status. The response must include stage and human-readable status text, not a fabricated percentage.

**Test first:** Add `tests/integration/test_api_zip_projects.py` for isolated uploads, nested paths and ZIP metadata, automatic pipeline completion, invalid ZIP rollback, reimport rejection, status recovery, retry, and concurrency limits. Run the focused pytest file and observe the missing endpoint/state failures before implementing; rerun it green after the change.

### Task 3: Make Talend destinations project-specific and retain apply status

**Files:** `apps/api/main.py`, `src/sas_grid_migrator/talend_adapter/apply_spec.py`, `src/sas_grid_migrator/talend_adapter/adapter.py`, `src/sas_grid_migrator/persistence/store.py`

1. Change Talend folder derivation from only the SAS program path to a deterministic folder rooted at configured `TALEND_APPLY_FOLDER`, followed by a sanitized archive slug, stable `project_id`, and the ZIP-relative subfolder of the program.
2. Use this same path for preview and apply so the destination shown in the guide exactly matches the MCP request.
3. Persist apply state before and after the MCP call and expose a read endpoint per project/program, so reopening the portal shows `running`, `applied`, `partially_applied`, `failed`, or `conflict` with the last result/error.
4. Use existing `project_id`, program, source digest, rules version, Job name, and folder identity from the apply spec to recognize a repeated identical revision. Reuse the existing MCP flow for safe retries; if the target identity/revision differs or MCP reports an unrelated Job collision, return a visible conflict and never silently replace it.
5. Preserve the current MCP payload and pending-information behavior. Do not create connections from fabricated values and do not execute Talend Jobs.

**Interfaces:** Apply preview and apply responses expose the exact per-project `folder_path`; `GET /api/projects/{project_id}/plans/{program:path}/talend-apply` returns the persisted application state; the POST route remains the explicit side-effecting action and records all outcomes.

**Test first:** Extend/add `tests/integration/test_api_talend_workspace.py` to assert different ZIP projects derive different stable folders, preview and POST agree, a successful result is persisted, an identical retry does not duplicate a completed apply, partial apply can retry with the same revision, and a changed revision is reported as a conflict. Mock the MCP boundary only; assert the exact structured payload and that no Job execution tool is called.

### Task 4: Upload and monitor one ZIP per project in the portal

**Files:** `apps/web/src/api.ts`, `apps/web/src/types.ts`, `apps/web/src/views/ProjectsView.tsx`, `apps/web/src/views/ProjectView.tsx`, `apps/web/src/views/InventoryTab.tsx`, `apps/web/src/views/SummaryTab.tsx`, `apps/web/src/views/PlansTab.tsx`, `apps/web/src/components/ArchivePathTree.tsx`, `apps/web/src/styles.css`

1. Replace the create-then-upload path for new ZIP projects with one clearly labeled upload flow. Show the selected ZIP name, upload state, useful errors, and create/open the project only after the API confirms extraction and registration.
2. Enrich each project card with ZIP filename, nested-folder/program counts, pipeline state, last update, and a direct action to open that project. Add filters/search against both project name and ZIP filename.
3. Add a project-level status banner showing current stage/message, started/updated time, terminal success/failure/interrupted state, and an explicit retry action when appropriate. Poll while a pipeline is active and reload persisted state on route entry/refresh.
4. Identify the ZIP/archive at the top of project detail and show its folder tree collapsed by default with search/filter for large projects. Ensure paths and program/dependency/guide views remain scoped to the selected project.
5. Show the exact per-project Talend folder and durable last implementation state in each Job guide. Keep the explicit “Implementar flujo directo en Talend” action; show pending technical information as context and make clear that implementation does not run the Job.
6. Mark existing projects with no archive metadata as “Proyecto existente” or “ZIP no registrado” and preserve their existing navigation and manual-import flow.
7. Add empty/loading/error states and responsive styling for one ZIP per project, long filenames, deeply nested folders, and large project lists. Do not use misleading progress bars without a backend-reported percentage.

**Interfaces:** Frontend API/types mirror the persisted backend contracts; the project list and detail can be refreshed independently without losing stage or apply state.

**Test first:** Extend `apps/web/src/api.test.mjs` for multipart ZIP creation and processing/apply status routes, and add `apps/web/src/project-workspace.test.ts` for project filtering, status labels, and large/nested archive path presentation helpers. Add or adjust `apps/web/src/views/PlansTab.test.mjs` to cover durable apply status and the exact project-scoped destination. Run focused Bun tests and observe failures before changing frontend code; rerun them green after the change.

### Task 5: Update operational and architecture documentation

**Files:** `README.md`, `docs/architecture.md`, `docs/talend-mcp-tools.md`, `.env.example`

1. Document the one-ZIP-per-project upload flow, extraction/analysis stages, retries, legacy projects, status meanings, and supported ZIP limits.
2. Document the single-instance SQLite/background processing boundary and what would be required for horizontal scaling (shared durable queue and database).
3. Document the exact Talend destination formula, configurable root, stable project identity, collision/idempotency behavior, and the fact that apply does not execute the Job.
4. Add only the new environment settings actually implemented, with safe local defaults and no machine-specific paths.

### Deferred

- Execute Talend Jobs, resolve real connection credentials/schemas, update existing Jobs, add a distributed queue/database, or make MCP apply automatic on upload.
