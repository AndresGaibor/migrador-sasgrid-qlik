# Automatic Studio Flow Checks Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Automatically mark migration steps as verified only when MCP readback confirms their Talend component, configuration, schema/mapper and connections in Studio.

**Architecture:** Keep automatic Studio evidence in the existing Talend apply result, separate from manual `step_state`. Add component ownership to MCP mapper inspection, translate a conservative subset of SAS mapping expressions, and compare expected specs with readback for parent and child Jobs. Expose per-step results and retry in the API/UI without compiling or executing Jobs.

**Tech Stack:** Python 3.12+, FastAPI, Pydantic, SQLite, React, TypeScript, Bun, MCP Talend inspection tools.

**Spec:** `docs/superpowers/specs/2026-10-27-talend-auto-flow-checks-design.md`

## Global Constraints

- Confirm a step only after reading the saved Job from Talend Studio.
- Do not compile or execute Jobs as part of this check.
- Keep manual guide decisions and notes separate from Studio evidence.
- Unsupported or incomplete mappings remain pending with a reason.
- Tie evidence to the current apply-spec revision.
- Preserve all pre-existing modified and untracked files in both repositories.
- Never report a failed MCP read as proof that the Talend Job changed.

## Review Focus

- Missing component or a reused alias: verify the actual component identity through MCP aliases.
- Missing or changed connection: leave the affected step pending and name the missing edge.
- Incomplete schema or mapper: do not mark the step verified even when the component exists.
- MCP unavailable after create: persist an unavailable result and allow a read-only retry.
- Nested child Job created by an orchestrator: verify and persist it independently from its parent.

---

### Task 1: Read back exact mapper and component configuration

**Files:**
- Modify: `talend-mcp/src/domain/job/job.entity.ts`
- Modify: `talend-mcp/src/talend/job-parser.ts`
- Modify: `talend-mcp/src/server/enriched/base-schemas.ts`
- Test: `talend-mcp/tests/talend/job-parser.test.ts`
- Modify: `migrador-sasgrid-qlik/src/sas_grid_migrator/talend_adapter/adapter.py`
- Test: `migrador-sasgrid-qlik/tests/unit/test_talend_adapter.py`

**Interfaces:**
- `MapperEntry.componentUniqueName?: string` identifies the Talend node that owns a parsed mapper entry.
- `JobInspection` preserves component parameter values, schema tables/columns, connections and mapper entries while retaining current summary fields.

- [x] **Step 1: Write failing tests** for mapper ownership in parsed MCP inspection and for the portal adapter preserving component values, schemas, connection endpoints/labels and mapper entries.
- [x] **Step 2: Run the tests and confirm the missing readback fields cause failure.**
- [x] **Step 3: Add optional mapper ownership to the MCP inspection contract and parser; preserve detailed inspection fields in the portal adapter.**
- [x] **Step 4: Run the focused MCP and portal adapter tests.**

### Task 2: Generate stable step identities and supported tMap mappings

**Files:**
- Modify: `migrador-sasgrid-qlik/src/sas_grid_migrator/talend_adapter/apply_spec.py`
- Modify: `migrador-sasgrid-qlik/src/sas_grid_migrator/migration_planner/models.py`
- Modify: `migrador-sasgrid-qlik/src/sas_grid_migrator/migration_planner/planner.py`
- Test: `migrador-sasgrid-qlik/tests/unit/test_talend_apply_spec.py`
- Test: `migrador-sasgrid-qlik/tests/unit/test_planner.py`

**Interfaces:**
- Portal instruction steps include `talendUniqueName` when a concrete Talend component represents that SAS step.
- Compute expressions retain their SAS target column. A private mapper builder returns a mapper only for direct column references and arithmetic expressions with known input/output schemas and connection labels; otherwise it returns a pending reason.

- [x] **Step 1: Write failing tests** for a direct mapping, simple arithmetic, and unsupported/ambiguous mapper expressions remaining drafts.
- [x] **Step 2: Run the tests and confirm mapper generation is absent or unsupported expressions are incorrectly promoted.**
- [x] **Step 3: Implement the allow-listed mapper builder and include the Talend unique name in source-step instructions; remove the mapper-draft reason only when a complete mapper is generated.**
- [x] **Step 4: Run the focused apply-spec tests, including existing offline-file configuration cases.**

### Task 3: Verify and persist parent/child Job steps

**Files:**
- Modify: `migrador-sasgrid-qlik/apps/api/main.py`
- Modify: `migrador-sasgrid-qlik/src/sas_grid_migrator/talend_adapter/adapter.py`
- Test: `migrador-sasgrid-qlik/tests/integration/test_api_talend_batch.py`

**Interfaces:**
- `verification.steps[]` contains `step_id`, `talend_unique_name`, `status` (`verified`, `pending`, `unavailable`), per-area checks and a human-readable reason.
- Successful verification is stored with the existing apply result and its revision hash; manual `step_state` is never overwritten.
- `POST /api/projects/{project_id}/plans/{program}/talend-apply/verify` retries read-only verification for an already-applied Job.

- [x] **Step 1: Write failing API tests** for exact component/parameter/schema/mapper/edge matching, stale revision rejection, unavailable readback, and nested child verification; assert manual states and notes remain unchanged.
- [x] **Step 2: Run the tests and confirm the per-step result/retry behavior is missing.**
- [x] **Step 3: Implement readback comparison, recursive child verification/persistence, and the explicit retry endpoint.**
- [x] **Step 4: Run the focused Talend batch and persistence tests.**

### Task 4: Show automatic checks separately in the portal

**Files:**
- Modify: `migrador-sasgrid-qlik/apps/api/main.py`
- Modify: `migrador-sasgrid-qlik/apps/web/src/types.ts`
- Modify: `migrador-sasgrid-qlik/apps/web/src/api.ts`
- Modify: `migrador-sasgrid-qlik/apps/web/src/views/PlansTab.tsx`
- Modify: `migrador-sasgrid-qlik/apps/web/src/views/plans/PlanListContent.tsx`
- Test: `migrador-sasgrid-qlik/apps/web/src/views/plans/PlanListContent.test.tsx`
- Test: `migrador-sasgrid-qlik/apps/web/src/views/PlansTab.test.mjs`

**Interfaces:**
- Plan list rows expose current-revision verified counts separately from existing manual progress counts.
- Plan detail exposes a read-only verification result per step and a retry action when verification is pending/unavailable.

- [x] **Step 1: Write failing UI tests** for distinct “Verificado en Studio” vs manual status, per-step reason display and retry action.
- [x] **Step 2: Run the tests and confirm the separate automatic state is not shown.**
- [x] **Step 3: Implement the types, API call, auto-verification labels/counts and retry control.**
- [x] **Step 4: Run the focused frontend tests and typecheck/build.**

### Task 5: End-to-end regression verification

- [x] Run the portal Python tests; full suite: 256 passed, 1 skipped.
- [x] Run `bun run verify` and focused Talend inspection/parser tests in `talend-mcp`.
- [x] Run the portal web tests and build: 60 passed; build succeeded.
- [x] Review both diffs and confirm no pre-existing user changes were reverted or included unintentionally.
