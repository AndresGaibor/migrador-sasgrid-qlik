"""Helpers for ordering project-level Talend application batches."""

import posixpath
from typing import Any

from sas_grid_migrator.migration_planner.models import JobPlan


def _normalized_program(program: str) -> str:
    return posixpath.normpath(program.replace("\\", "/"))


def order_plans_for_batch(
    plans: list[JobPlan], processing_order: list[list[str]]
) -> list[JobPlan]:
    """Order plans by dependency layers and append plans absent from the graph."""
    by_path: dict[str, JobPlan] = {}
    for plan in plans:
        by_path.setdefault(_normalized_program(plan.program), plan)

    ordered_paths: list[str] = []
    included: set[str] = set()
    for layer in processing_order:
        for path in sorted(
            (_normalized_program(item) for item in layer if _normalized_program(item) in by_path),
            key=lambda item: (item.casefold(), item),
        ):
            if path not in included:
                included.add(path)
                ordered_paths.append(path)

    remaining = sorted(
        by_path.keys() - included,
        key=lambda item: (item.casefold(), item),
    )
    ordered_paths.extend(remaining)
    return [by_path[path] for path in ordered_paths]


def collect_child_results(result: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten confirmed MCP child Job results in their creation order."""
    children: list[dict[str, Any]] = []

    def visit(parent: dict[str, Any]) -> None:
        parent_name = parent.get("jobName")
        raw_children = parent.get("childJobs")
        if not isinstance(raw_children, list):
            return
        for child in raw_children:
            if not isinstance(child, dict):
                continue
            visit(child)
            children.append(
                {
                    **{key: value for key, value in child.items() if key != "childJobs"},
                    "parentJobName": parent_name,
                }
            )

    visit(result)
    return children
