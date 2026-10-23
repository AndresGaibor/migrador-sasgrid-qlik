"""Allowlist de lectura y aplicación de guías para tools de talend-mcp.

La aplicación solo invoca writers tipados tras una confirmación del usuario.
"""

READ_TOOLS = frozenset(
    {
        "talend_detect_open_jobs",
        "talend_jobs_list",
        "talend_jobs_read",
        "talend_read_contexts",
        "talend_list_project_contexts",
        "talend_list_repository_contexts",
        "talend_read_repository_context",
        "talend_list_components",
        "talend_show_flow",
        "talend_analyze_tdboutput",
        "talend_read_run_log",
        "talend_summarize_open_job",
        "talend_inspect_component",
        "talend_inspect_job",
        "talend_preview_component_parameter",
        "talend_preview_schema_column",
        "talend_repo_status",
        "talend_repo_sources",
        "talend_job_info",
        "talend_job_problems",
        "talend_job_list_nodes",
        "talend_bridge_ping",
    }
)

WRITE_TOOLS = frozenset(
    {
        "talend_job_apply_custom_spec",
    }
)


class ToolNotAllowed(PermissionError):
    pass


def assert_allowed(tool: str) -> None:
    if tool not in READ_TOOLS and tool not in WRITE_TOOLS:
        raise ToolNotAllowed(f"{tool} no está en la allowlist de lectura y creación")
