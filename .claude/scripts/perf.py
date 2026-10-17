"""Mide import/análisis/deps/IR+planes sobre N copias del corpus. Uso: perf.py <copias>"""
import shutil
import sys
import tempfile
import time
from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import build_dependencies
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import analyze_project

n = int(sys.argv[1])
corpus = Path("tests/fixtures/sas")
tmp = Path(tempfile.mkdtemp())
src = tmp / "in"
for i in range(n):
    shutil.copytree(corpus, src / f"c{i}", ignore=shutil.ignore_patterns("*.md"))
st = Store(Settings(data_dir=tmp / "data", max_files=100000, max_total_bytes=2**31))
p = st.create_project("perf")


def t(label, fn):
    a = time.perf_counter()
    r = fn()
    print(f"{label:10s} {time.perf_counter() - a:6.2f}s")
    return r


m = t("import", lambda: st.import_batch(p.id, src))
print("archivos", len(m.files), "bytes", sum(f.size for f in m.files))
an = t("analyze", lambda: analyze_project(st, p.id))
d = t("deps", lambda: build_dependencies(st, p.id))
ps = t("plans", lambda: generate_plans(st, p.id))
print("programas", len(an.programs), "planes", len(ps.plans), "capas", len(d.processing_order))
shutil.rmtree(tmp)
