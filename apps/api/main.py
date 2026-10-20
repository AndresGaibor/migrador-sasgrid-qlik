import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from sas_grid_migrator import __version__

from .integrations import router as integrations_router
from .plans import router as plans_router
from .projects import router as projects_router

app = FastAPI(title="SAS Grid Migrator", version=__version__)
app.include_router(projects_router)
app.include_router(plans_router)
app.include_router(integrations_router)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}


# UI compilada (apps/web/dist): se monta al final para que /api/* tenga prioridad.
_dist = Path(os.environ.get("SGM_WEB_DIST", Path(__file__).resolve().parents[1] / "web" / "dist"))
if _dist.is_dir():
    app.mount("/", StaticFiles(directory=_dist, html=True), name="web")
