"""Contrasta un plan contra componentes observados en Jobs de referencia de Talend.

Un componente solo se marca `verified` si aparece en algún Job de referencia y todas las
propiedades del paso existen como parámetros de ese componente. Si no, queda sin verificar y
se anota el motivo: no hay catálogo global en talend-mcp (solo componentes de Jobs existentes).
"""

from pydantic import BaseModel

from sas_grid_migrator.migration_planner.models import PlanSet
from sas_grid_migrator.talend_adapter.adapter import JobInspection


class Catalog(BaseModel):
    jobs: list[str] = []
    components: dict[str, list[str]] = {}  # tipo -> parámetros observados

    def add(self, insp: JobInspection) -> None:
        self.jobs.append(insp.job_path)
        for c in insp.components:
            seen = set(self.components.get(c.component, [])) | set(c.parameters)
            self.components[c.component] = sorted(seen)


def verify_plans(ps: PlanSet, catalog: Catalog) -> dict[str, int]:
    stats = {"verified": 0, "component_known": 0, "unknown": 0}
    for plan in ps.plans:
        for step in plan.steps + [s for c in plan.children for s in c.steps]:
            params = catalog.components.get(step.component_candidate)
            if params is None:
                if step.component_candidate != "por_determinar":
                    stats["unknown"] += 1
                continue
            known = set(params)
            for p in step.properties:
                p.verified = p.name in known
            missing = [p.name for p in step.properties if not p.verified]
            step.verified = not missing
            if step.verified:
                stats["verified"] += 1
            else:
                stats["component_known"] += 1
                note = f"Propiedades no vistas en Jobs de referencia: {', '.join(missing)}"
                if note not in step.pending:
                    step.pending.append(note)
    return stats
