# Tools de talend-mcp (revisión F0)

Fuente: README de https://github.com/AndresGaibor/talend-mcp (clon superficial revisado 2026-10-17). Servidor para **Qlik Talend Studio**; HTTP en `127.0.0.1:3927/mcp` o stdio. Requiere `TALEND_WORKSPACE`. Los nombres de tools se tomaron del README; los esquemas de entrada/salida reales se verifican en F5 contra el servidor en ejecución (`tools/list`).

## Permitidas (solo lectura) — `talend_adapter/policy.py`

Inspección: `talend_detect_open_job`, `talend_list_jobs`, `talend_read_job`, `talend_read_contexts`, `talend_list_project_contexts`, `talend_list_repository_contexts`, `talend_read_repository_context`, `talend_list_components`, `talend_show_flow`, `talend_analyze_tdboutput`, `talend_read_latest_run_log`, `talend_read_job_errors`, `talend_summarize_open_job`, `talend_inspect_component`, `talend_inspect_job`, `talend_job_info`.
Previsualización (no escribe): `talend_preview_component_parameter`, `talend_preview_schema_column`.
Repo: `talend_repo_status`, `talend_repo_sources`.

## Bloqueadas en el MVP

- Jobs/carpetas: `talend_create_job`, `talend_create_folder`, `talend_rename_job`, `talend_delete_job`, `talend_duplicate_job`, `talend_move_job_to_folder`.
- Edición: `talend_update_component_parameter`, `talend_update_schema_column`, `talend_duplicate_component`, `talend_add_connection`, `talend_update_context`, `talend_upsert_context`, `talend_delete_context`, `talend_update_job_metadata`, `talend_create_repository_context`, `talend_upsert_repository_context_parameter`, `talend_delete_repository_context`.
- Repo: `talend_repo_setup`, `talend_repo_pull`, `talend_repo_switch`.
- Ejecución: `talend_run_job`.

## Notas

- Las tools de edición solo operan en modo workspace local, no repo.
- `talend_inspect_component` es la vía prevista para verificar nombres de propiedades y esquemas; no hay tool de catálogo global de componentes (solo componentes de un job existente), así que un componente que no aparezca en ningún Job de referencia queda `verified: false`.
- El servidor además puede levantar un tunnel hacia OpenAI (`bun run start`); usar `bun run start:server` para el adaptador.
