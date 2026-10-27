# Talend Destination Preflight — Design

## Intent

Before applying a ZIP project, the portal queries the current Talend inventory and distinguishes Jobs to create, Jobs to update in that project's exact destination folder, and ambiguous name collisions. This prevents a saved conflict from being mistaken for current Studio state and permits a safe same-revision retry after a Job was removed.

## Evidence and current behavior

- Project `331f40838579` has a persisted `conflict` batch with eight conflict results.
- A fresh `talend_jobs_list` query returns 68 Jobs and none of the eight requested names; the saved errors are stale.
- `talend_jobs_list` defaults to 50 results, while the health endpoint uses that default.
- Batch start returns the saved conflict without a fresh Talend check, and per-Job persistence rejects the old conflict too.

## Goals and constraints

- Query every page from the existing read-only `talend_jobs_list` MCP tool.
- Show a per-Job preflight: `create` when absent; `update` when present in the exact project destination; `conflict` when the name exists only elsewhere.
- Fail closed when MCP cannot provide a complete inventory, and check again immediately before writes.
- Only a fresh, conflict-free inventory may authorize a same-revision conflict retry. Continue applying through the existing Studio API tool.
- If a previously completed Job has since been removed, a same-revision retry recreates only that missing Job and preserves completed Jobs that still exist.
- Keep writes sequential. Never edit Talend `.item` files, delete Jobs, compile, or execute Jobs during preflight.

## Approaches

1. **Read-only MCP inventory preflight (chosen):** paginate the existing tool, compare exact target folders, show each action, and repeat the check at batch start. This reuses the current MCP contract and supports automatic create/update behavior.
2. **Retry from stored error text:** simpler, but cannot tell whether the Job was deleted or the conflict persists.
3. **Add a new Studio bridge tool:** can inspect more IDE state, but adds a capability when the existing inventory provides name and path and the actual apply remains protected by MCP.

## UI behavior

The project panel displays the latest per-Job actions and counts. Apply remains disabled while preflight is unavailable or has ambiguous collisions. The server repeats preflight on click, so stale client state cannot authorize a write. Exact-path matches are labeled for update; missing Jobs are labeled for creation.

## Acceptance

1. Pagination includes Jobs beyond the first 50.
2. Name and path matching is case-insensitive and compares the full target folder.
3. Exact-path matches are updates, missing names are creates, and same-name Jobs elsewhere are conflicts.
4. A saved conflict can retry only after a fresh complete inventory has no ambiguous collision.
5. If a completed Job is missing from the current inventory, the portal can recreate it without reapplying other completed Jobs.
6. The UI explains each action and fails closed when MCP is unavailable.
