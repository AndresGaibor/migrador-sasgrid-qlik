"""Resumen del DependencyReport de un proyecto. Uso: uv run python .claude/scripts/deps_report.py <project_id>"""

import collections
import sys

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import build_dependencies
from sas_grid_migrator.persistence.store import Store

r = build_dependencies(Store(Settings.from_env()), sys.argv[1])
print("cycles:", r.cycles)
print("unresolved by kind:", collections.Counter(u.kind for u in r.unresolved))
print(
    "top unresolved macros:",
    collections.Counter(u.name for u in r.unresolved if u.kind == "macro").most_common(15),
)
print(
    "includes:",
    collections.Counter(u.detail.split(" ")[0] for u in r.unresolved if u.kind == "include"),
)
print("roles:", collections.Counter(d.role for d in r.datasets))
for e in r.edges[:12]:
    print(e.kind, e.source.split("/")[-1], "->", e.target.split("/")[-1], e.datasets[:3])
print("libs:", [(l.name, l.engine, l.path) for l in r.libraries[:8]])
print("schedules:", r.orchestration.schedules)
