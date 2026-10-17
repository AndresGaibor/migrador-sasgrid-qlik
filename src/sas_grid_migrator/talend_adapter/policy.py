"""Allowlist de tools de talend-mcp. Fuente: README de AndresGaibor/talend-mcp (revisado 2026-10-17).

Solo lectura por defecto: cualquier tool fuera de READ_TOOLS se rechaza.
"""

READ_TOOLS = frozenset(
    {
        "talend_detect_open_job",
        "talend_list_jobs",
        "talend_read_job",
        "talend_read_contexts",
        "talend_list_project_contexts",
        "talend_list_repository_contexts",
        "talend_read_repository_context",
        "talend_list_components",
        "talend_show_flow",
        "talend_analyze_tdboutput",
        "talend_read_latest_run_log",
        "talend_read_job_errors",
        "talend_summarize_open_job",
        "talend_inspect_component",
        "talend_inspect_job",
        "talend_preview_component_parameter",
        "talend_preview_schema_column",
        "talend_repo_status",
        "talend_repo_sources",
        "talend_job_info",
    }
)


class ToolNotAllowed(PermissionError):
    pass


def assert_allowed(tool: str) -> None:
    if tool not in READ_TOOLS:
        raise ToolNotAllowed(f"{tool} no está en la allowlist de solo lectura")
