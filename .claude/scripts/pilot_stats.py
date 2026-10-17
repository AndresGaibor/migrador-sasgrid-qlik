"""Cifras del piloto: corre el pipeline sobre una carpeta y resume cobertura y madurez de los planes."""
import sys
import tempfile
from collections import Counter
from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import build_dependencies
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import analyze_project, summarize

st = Store(Settings(data_dir=Path(tempfile.mkdtemp()) / "data"))
p = st.create_project("pilot")
st.import_batch(p.id, Path(sys.argv[1]))
s = summarize(analyze_project(st, p.id))
d = build_dependencies(st, p.id)
ps = generate_plans(st, p.id)
steps = [x for pl in ps.plans for x in pl.steps + [y for c in pl.children for y in c.steps]]
print("programas", s.programs, "sentencias", s.statements, "sin_reconocer", s.unrecognized, "fragmentos", s.macro_fragments)
print("hallazgos", s.findings_by_priority)
print("top constructos", [(c.tag, c.priority, c.count) for c in s.coverage[:8]])
print("datasets", len(d.datasets), "aristas", len(d.edges), "ciclos", len(d.cycles), "sin_resolver", len(d.unresolved), "tareas_grid", len(d.orchestration.tasks))
print("planes", len(ps.plans), "pasos", len(steps))
print("componente", Counter(x.component_candidate for x in steps).most_common(10))
print("sin_componente", sum(1 for x in steps if x.component_candidate == "por_determinar"), "con_pendientes", sum(1 for x in steps if x.pending))
print("tipos_op", Counter(x.operation_type for x in steps).most_common(8))
print("job_status", Counter(pl.job_status for pl in ps.plans))
