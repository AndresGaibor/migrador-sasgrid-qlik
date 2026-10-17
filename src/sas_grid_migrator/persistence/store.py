import sqlite3
import uuid
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.domain.models import Manifest, Project, Skipped, SourceFile
from sas_grid_migrator.ingestion.importer import import_source

SCHEMA = """
create table if not exists projects(id text primary key, name text not null, created_at text not null);
create table if not exists source_files(
  project_id text not null references projects(id), path text not null, sha256 text not null,
  size integer not null, kind text not null, encoding text, primary key(project_id, path));
create table if not exists step_state(
  project_id text not null references projects(id), program text not null, step_id text not null,
  status text not null, note text, updated_at text not null, primary key(project_id, program, step_id));
create table if not exists skipped(project_id text not null references projects(id), path text not null, reason text not null);
"""


class Store:
    def __init__(self, settings: Settings):
        self.settings = settings
        settings.data_dir.mkdir(parents=True, exist_ok=True)
        self.db = settings.data_dir / "sgm.sqlite"
        with self._conn() as c:
            c.executescript(SCHEMA)

    def _conn(self) -> sqlite3.Connection:
        c = sqlite3.connect(self.db)
        c.execute("pragma foreign_keys = on")
        return c

    def source_dir(self, project_id: str) -> Path:
        return self.settings.data_dir / "projects" / project_id / "src"

    def analysis_path(self, project_id: str) -> Path:
        return self.settings.data_dir / "projects" / project_id / "analysis.json"

    def dependencies_path(self, project_id: str) -> Path:
        return self.settings.data_dir / "projects" / project_id / "dependencies.json"

    def plans_path(self, project_id: str) -> Path:
        return self.settings.data_dir / "projects" / project_id / "plans.json"

    def set_step_state(
        self, project_id: str, program: str, step_id: str, status: str, note: str | None
    ) -> None:
        with closing(self._conn()) as c, c:
            c.execute(
                "insert or replace into step_state values (?,?,?,?,?,?)",
                (project_id, program, step_id, status, note, datetime.now(UTC).isoformat()),
            )

    def get_step_states(
        self, project_id: str, program: str | None = None
    ) -> dict[tuple[str, str], tuple[str, str | None]]:
        q = "select program,step_id,status,note from step_state where project_id=?"
        args: tuple = (project_id,)
        if program:
            q, args = q + " and program=?", (project_id, program)
        with closing(self._conn()) as c:
            return {(p, i): (st, n) for p, i, st, n in c.execute(q, args).fetchall()}

    def create_project(self, name: str) -> Project:
        p = Project(id=uuid.uuid4().hex[:12], name=name)
        with closing(self._conn()) as c, c:
            c.execute(
                "insert into projects values (?,?,?)", (p.id, p.name, p.created_at.isoformat())
            )
        return p

    def get_project(self, project_id: str) -> Project | None:
        with closing(self._conn()) as c:
            r = c.execute(
                "select id,name,created_at from projects where id=?", (project_id,)
            ).fetchone()
        return Project(id=r[0], name=r[1], created_at=datetime.fromisoformat(r[2])) if r else None

    def list_projects(self) -> list[Project]:
        with closing(self._conn()) as c:
            rows = c.execute(
                "select id,name,created_at from projects order by created_at"
            ).fetchall()
        return [Project(id=i, name=n, created_at=datetime.fromisoformat(t)) for i, n, t in rows]

    def import_batch(self, project_id: str, src: Path) -> Manifest:
        """Reemplaza el snapshot del proyecto por el contenido de `src` (carpeta o ZIP)."""
        files, skipped = import_source(src, self.source_dir(project_id), self.settings)
        for derived in (
            self.analysis_path(project_id),
            self.dependencies_path(project_id),
            self.plans_path(project_id),
        ):
            derived.unlink(missing_ok=True)  # el snapshot cambió: resultados derivados obsoletos
        with closing(self._conn()) as c, c:
            c.execute("delete from source_files where project_id=?", (project_id,))
            c.execute("delete from skipped where project_id=?", (project_id,))
            c.executemany(
                "insert into source_files values (?,?,?,?,?,?)",
                [(project_id, f.path, f.sha256, f.size, f.kind.value, f.encoding) for f in files],
            )
            c.executemany(
                "insert into skipped values (?,?,?)",
                [(project_id, s.path, s.reason) for s in skipped],
            )
        return Manifest(project_id=project_id, files=files, skipped=skipped)

    def get_manifest(self, project_id: str) -> Manifest:
        with closing(self._conn()) as c:
            files = c.execute(
                "select path,sha256,size,kind,encoding from source_files where project_id=? order by path",
                (project_id,),
            ).fetchall()
            skipped = c.execute(
                "select path,reason from skipped where project_id=? order by path", (project_id,)
            ).fetchall()
        return Manifest(
            project_id=project_id,
            files=[
                SourceFile(path=p, sha256=h, size=s, kind=k, encoding=e) for p, h, s, k, e in files
            ],
            skipped=[Skipped(path=p, reason=r) for p, r in skipped],
        )
