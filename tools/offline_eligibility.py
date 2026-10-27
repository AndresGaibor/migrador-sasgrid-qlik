"""Mide cuántas guías de un ZIP o carpeta pueden ir por el motor offline del MCP.

Uso:
    uv run python tools/offline_eligibility.py <zip-o-carpeta> [<zip-o-carpeta> ...]

Solo lee: importa el lote en un proyecto temporal, genera los planes y cuenta los
bloqueos de cada especificación. No llama al MCP ni a Studio.
"""

from __future__ import annotations

import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sas_grid_migrator.config import Settings  # noqa: E402
from sas_grid_migrator.migration_planner.service import generate_plans  # noqa: E402
from sas_grid_migrator.persistence.store import Store  # noqa: E402
from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec  # noqa: E402
from sas_grid_migrator.talend_adapter.eligibility import offline_blockers  # noqa: E402


def measure(source: Path) -> tuple[int, int, Counter[str]]:
    with tempfile.TemporaryDirectory(prefix="offline-eligibility-") as tmp:
        store = Store(Settings(data_dir=Path(tmp)))
        project = store.create_project(source.stem)
        store.import_batch(project.id, source)
        plans = generate_plans(store, project.id, fresh=True).plans
        blockers: Counter[str] = Counter()
        eligible = 0
        for plan in plans:
            found = offline_blockers(build_apply_spec(plan, "Process/PruebasOffline").to_mcp_arguments())
            if found:
                blockers.update(item.split(":")[0] for item in found)
            else:
                eligible += 1
        return len(plans), eligible, blockers


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    for raw in argv:
        source = Path(raw).expanduser()
        if not source.exists():
            print(f"{source}: no existe")
            continue
        total, eligible, blockers = measure(source)
        share = (eligible / total * 100) if total else 0.0
        detail = ", ".join(f"{name}={count}" for name, count in sorted(blockers.items())) or "sin bloqueos"
        print(f"{source.name}: {eligible}/{total} elegibles ({share:.1f} %) · {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
