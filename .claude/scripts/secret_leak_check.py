"""Importa un SAS con credenciales y busca los secretos en todo lo derivado (JSON, exports, SQLite)."""

import subprocess
import sys
from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.reporting.exports import write_exports

src, data = Path(sys.argv[1]), Path(sys.argv[2])
st = Store(Settings(data_dir=data))
p = st.create_project("s")
st.import_batch(p.id, src)
write_exports(generate_plans(st, p.id), data / "out")
for secret in sys.argv[3:]:
    hits = subprocess.run(
        ["grep", "-rl", "--exclude-dir=src", secret, str(data)],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.split()
    print(secret, [h.replace(str(data), "") for h in hits])
