from fastapi import HTTPException

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import PlanSet
from sas_grid_migrator.migration_planner.service import load_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import load_analysis


def store() -> Store:
    return Store(Settings.from_env())


def require_project(s: Store, project_id: str) -> None:
    if s.get_project(project_id) is None:
        raise HTTPException(404, "proyecto no encontrado")


def analysis(project_id: str):
    s = store()
    require_project(s, project_id)
    result = load_analysis(s, project_id)
    if result is None:
        raise HTTPException(409, "el proyecto aún no fue analizado")
    return result


def plans(project_id: str) -> PlanSet:
    s = store()
    require_project(s, project_id)
    result = load_plans(s, project_id)
    if result is None:
        raise HTTPException(409, "los planes aún no fueron generados")
    return result


def talend():
    from sas_grid_migrator.talend_adapter.adapter import TalendAdapter

    return TalendAdapter.from_env()
