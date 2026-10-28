import json
import os
import shutil
import sqlite3
import uuid
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path

from sas_grid_migrator.config import Settings
from sas_grid_migrator.domain.models import (
    Manifest,
    Project,
    ProjectProcessing,
    Skipped,
    SourceFile,
)
from sas_grid_migrator.ingestion.importer import import_source

SCHEMA = """
create table if not exists talend_permissions(
  id integer primary key check(id=1), write_enabled integer not null check(write_enabled in (0,1))
);
create table if not exists projects(
  id text primary key, name text not null, created_at text not null,
  archive_name text, archive_sha256 text, archive_size_bytes integer, uploaded_at text,
  manifest_summary text
);
create table if not exists source_files(
  project_id text not null references projects(id), path text not null, sha256 text not null,
  size integer not null, kind text not null, encoding text, primary key(project_id, path));
create table if not exists step_state(
  project_id text not null references projects(id), program text not null, step_id text not null,
  status text not null, note text, updated_at text not null, primary key(project_id, program, step_id));
create table if not exists skipped(project_id text not null references projects(id), path text not null, reason text not null);
create table if not exists project_processing(
  project_id text primary key references projects(id), status text not null, stage text not null,
  started_at text, stage_started_at text, updated_at text not null, message text, error text,
  retry_count integer not null default 0
);
create table if not exists talend_apply_operations(
  project_id text not null references projects(id), program text not null,
  revision_hash text not null, status text not null, identity_json text not null,
  result_json text, error text, started_at text not null, updated_at text not null,
  primary key(project_id, program)
);
create table if not exists talend_apply_batches(
  project_id text primary key references projects(id), revision_hash text not null,
  status text not null, programs_json text not null, jobs_json text not null,
  current_program text, completed_jobs integer not null default 0, error text,
  attempt_count integer not null default 1, started_at text not null, updated_at text not null,
  warnings_json text not null default '[]'
);
"""


class ProjectDeletionBlockedError(RuntimeError):
    """Indica que no se puede retirar un proyecto mientras sigue trabajando."""


class Store:
    def __init__(self, settings: Settings):
        self.settings = settings
        settings.data_dir.mkdir(parents=True, exist_ok=True)
        self.db = settings.data_dir / "sgm.sqlite"
        with self._conn() as c:
            c.executescript(SCHEMA)
            columns = {row[1] for row in c.execute("pragma table_info(projects)")}
            for name, sql_type in (
                ("archive_name", "text"),
                ("archive_sha256", "text"),
                ("archive_size_bytes", "integer"),
                ("uploaded_at", "text"),
                ("manifest_summary", "text"),
            ):
                if name not in columns:
                    c.execute(f"alter table projects add column {name} {sql_type}")
            batch_columns = {row[1] for row in c.execute("pragma table_info(talend_apply_batches)")}
            if "warnings_json" not in batch_columns:
                c.execute("alter table talend_apply_batches add column warnings_json text not null default '[]'")

    def _conn(self) -> sqlite3.Connection:
        c = sqlite3.connect(self.db)
        c.execute("pragma foreign_keys = on")
        return c

    def talend_write_enabled(self, default: bool = True) -> bool:
        """Permiso de escritura guardado; `default` solo se usa antes de la primera elección."""
        with closing(self._conn()) as c:
            row = c.execute("select write_enabled from talend_permissions where id=1").fetchone()
        return bool(row[0]) if row else default

    def set_talend_write_enabled(self, enabled: bool) -> None:
        with closing(self._conn()) as c, c:
            c.execute(
                "insert into talend_permissions(id,write_enabled) values(1,?) "
                "on conflict(id) do update set write_enabled=excluded.write_enabled",
                (int(enabled),),
            )

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
                "insert into projects (id,name,created_at) values (?,?,?)",
                (p.id, p.name, p.created_at.isoformat()),
            )
        return p

    def create_zip_project(
        self,
        *,
        name: str,
        archive_name: str,
        archive_sha256: str,
        archive_size_bytes: int,
        staged_source_dir: Path,
        files: list[SourceFile],
        skipped: list[Skipped],
    ) -> tuple[Project, Manifest]:
        """Atomically publish a staged source snapshot and its ZIP project metadata."""
        project_id = uuid.uuid4().hex[:12]
        now = datetime.now(UTC)
        folders: set[str] = set()
        for item in files:
            parts = item.path.replace("\\", "/").split("/")[:-1]
            for index in range(1, len(parts) + 1):
                folders.add("/".join(parts[:index]))
        summary = {
            "files": len(files),
            "programs": sum(item.kind.value == "sas" for item in files),
            "folders": len(folders),
            "skipped": len(skipped),
        }
        project = Project(
            id=project_id,
            name=name,
            created_at=now,
            archive_name=archive_name,
            archive_sha256=archive_sha256,
            archive_size_bytes=archive_size_bytes,
            uploaded_at=now,
            manifest_summary=summary,
            processing=ProjectProcessing(
                status="queued",
                stage="queued",
                updated_at=now,
                message="ZIP recibido y listo para analizar.",
            ),
        )
        root = self.source_dir(project_id).parent
        staged_source_dir = Path(staged_source_dir)
        if not staged_source_dir.is_dir():
            raise ValueError("No existe el directorio temporal del proyecto.")
        root.parent.mkdir(parents=True, exist_ok=True)
        root.mkdir()
        try:
            os.replace(staged_source_dir, self.source_dir(project_id))
            with closing(self._conn()) as c, c:
                c.execute(
                    """insert into projects
                    (id,name,created_at,archive_name,archive_sha256,archive_size_bytes,uploaded_at,manifest_summary)
                    values (?,?,?,?,?,?,?,?)""",
                    (
                        project.id,
                        project.name,
                        project.created_at.isoformat(),
                        project.archive_name,
                        project.archive_sha256,
                        project.archive_size_bytes,
                        project.uploaded_at.isoformat() if project.uploaded_at else None,
                        json.dumps(summary, sort_keys=True),
                    ),
                )
                c.execute(
                    """insert into project_processing
                    (project_id,status,stage,started_at,stage_started_at,updated_at,message,error,retry_count)
                    values (?,?,?,?,?,?,?,?,?)""",
                    (
                        project.id,
                        "queued",
                        "queued",
                        None,
                        None,
                        now.isoformat(),
                        "ZIP recibido y listo para analizar.",
                        None,
                        0,
                    ),
                )
                c.executemany(
                    "insert into source_files values (?,?,?,?,?,?)",
                    [
                        (
                            project.id,
                            f.path,
                            f.sha256,
                            f.size,
                            f.kind.value,
                            f.encoding,
                        )
                        for f in files
                    ],
                )
                c.executemany(
                    "insert into skipped values (?,?,?)",
                    [(project.id, item.path, item.reason) for item in skipped],
                )
        except BaseException:
            shutil.rmtree(root, ignore_errors=True)
            raise
        return project, Manifest(project_id=project.id, files=files, skipped=skipped)

    def _project_from_row(self, row: tuple) -> Project:
        processing = self.get_processing(row[0])
        return Project(
            id=row[0],
            name=row[1],
            created_at=datetime.fromisoformat(row[2]),
            archive_name=row[3],
            archive_sha256=row[4],
            archive_size_bytes=row[5],
            uploaded_at=datetime.fromisoformat(row[6]) if row[6] else None,
            manifest_summary=json.loads(row[7]) if row[7] else None,
            processing=processing,
        )

    def get_project(self, project_id: str) -> Project | None:
        with closing(self._conn()) as c:
            r = c.execute(
                """select id,name,created_at,archive_name,archive_sha256,archive_size_bytes,uploaded_at,manifest_summary
                from projects where id=?""",
                (project_id,),
            ).fetchone()
        return self._project_from_row(r) if r else None

    def list_projects(self) -> list[Project]:
        with closing(self._conn()) as c:
            rows = c.execute(
                """select id,name,created_at,archive_name,archive_sha256,archive_size_bytes,uploaded_at,manifest_summary
                from projects order by created_at"""
            ).fetchall()
        return [self._project_from_row(row) for row in rows]

    def delete_project(self, project_id: str) -> bool:
        """Elimina el estado del portal y sus archivos, sin tocar Talend Studio."""
        projects_dir = self.settings.data_dir / "projects"
        project_dir = projects_dir / project_id
        quarantine: Path | None = None

        with closing(self._conn()) as connection:
            connection.execute("begin immediate")
            try:
                project = connection.execute(
                    "select id from projects where id=?", (project_id,)
                ).fetchone()
                if project is None:
                    connection.rollback()
                    return False

                processing = connection.execute(
                    "select status from project_processing where project_id=?", (project_id,)
                ).fetchone()
                if processing and processing[0] in {"queued", "running"}:
                    raise ProjectDeletionBlockedError(
                        "No se puede eliminar el proyecto mientras su análisis esté activo."
                    )

                batch = connection.execute(
                    "select status from talend_apply_batches where project_id=?", (project_id,)
                ).fetchone()
                operation = connection.execute(
                    "select 1 from talend_apply_operations where project_id=? and status='running' limit 1",
                    (project_id,),
                ).fetchone()
                if (batch and batch[0] in {"queued", "running"}) or operation:
                    raise ProjectDeletionBlockedError(
                        "No se puede eliminar el proyecto mientras haya una implementación Talend activa."
                    )

                projects_dir_resolved = projects_dir.resolve()
                if project_dir.parent.resolve() != projects_dir_resolved:
                    raise ValueError("La carpeta del proyecto está fuera del directorio administrado.")
                if project_dir.is_symlink():
                    raise ValueError("La carpeta del proyecto es un enlace y no se eliminará.")
                if project_dir.exists():
                    quarantine = projects_dir / f".deleting-{project_id}-{uuid.uuid4().hex}"
                    project_dir.replace(quarantine)

                for table in (
                    "source_files",
                    "step_state",
                    "skipped",
                    "project_processing",
                    "talend_apply_operations",
                    "talend_apply_batches",
                ):
                    connection.execute(f"delete from {table} where project_id=?", (project_id,))
                connection.execute("delete from projects where id=?", (project_id,))
                connection.commit()
            except BaseException:
                connection.rollback()
                if quarantine is not None and quarantine.exists() and not project_dir.exists():
                    quarantine.replace(project_dir)
                raise

        if quarantine is not None:
            if quarantine.is_dir() and not quarantine.is_symlink():
                shutil.rmtree(quarantine, ignore_errors=True)
            else:
                quarantine.unlink(missing_ok=True)
        return True

    def get_processing(self, project_id: str) -> ProjectProcessing | None:
        with closing(self._conn()) as c:
            row = c.execute(
                """select status,stage,started_at,stage_started_at,updated_at,message,error,retry_count
                from project_processing where project_id=?""",
                (project_id,),
            ).fetchone()
        if row is None:
            return None
        return ProjectProcessing(
            status=row[0],
            stage=row[1],
            started_at=datetime.fromisoformat(row[2]) if row[2] else None,
            stage_started_at=datetime.fromisoformat(row[3]) if row[3] else None,
            updated_at=datetime.fromisoformat(row[4]),
            message=row[5],
            error=row[6],
            retry_count=row[7],
        )

    def update_processing(
        self,
        project_id: str,
        *,
        status: str,
        stage: str,
        message: str | None = None,
        error: str | None = None,
    ) -> ProjectProcessing:
        current = self.get_processing(project_id)
        if current is None:
            raise ValueError("El proyecto no tiene un proceso registrado.")
        now = datetime.now(UTC)
        started_at = current.started_at
        if status == "running" and current.status != "running":
            started_at = now
        stage_started_at = current.stage_started_at
        if stage != current.stage or stage_started_at is None:
            stage_started_at = now
        retry_count = current.retry_count
        with closing(self._conn()) as c, c:
            c.execute(
                """update project_processing set status=?,stage=?,started_at=?,stage_started_at=?,
                updated_at=?,message=?,error=?,retry_count=? where project_id=?""",
                (
                    status,
                    stage,
                    started_at.isoformat() if started_at else None,
                    stage_started_at.isoformat() if stage_started_at else None,
                    now.isoformat(),
                    message,
                    error,
                    retry_count,
                    project_id,
                ),
            )
        return ProjectProcessing(
            status=status,
            stage=stage,
            started_at=started_at,
            stage_started_at=stage_started_at,
            updated_at=now,
            message=message,
            error=error,
            retry_count=retry_count,
        )

    def queue_processing_retry(self, project_id: str) -> ProjectProcessing | None:
        """Transiciona a queued solo si el proceso sigue fallido o interrumpido."""
        now = datetime.now(UTC)
        with closing(self._conn()) as c, c:
            updated = c.execute(
                """update project_processing set status='queued',stage='queued',stage_started_at=?,
                updated_at=?,message=?,error=null,retry_count=retry_count+1
                where project_id=? and status in ('failed','interrupted')""",
                (
                    now.isoformat(),
                    now.isoformat(),
                    "En cola para analizar el proyecto.",
                    project_id,
                ),
            ).rowcount
        return self.get_processing(project_id) if updated else None

    def recover_interrupted_operations(self) -> None:
        now = datetime.now(UTC).isoformat()
        with closing(self._conn()) as c, c:
            c.execute(
                """update project_processing set status='interrupted',updated_at=?,
                message='El proceso se interrumpió al reiniciar el servidor.'
                where status in ('queued','running')""",
                (now,),
            )
            c.execute(
                """update talend_apply_operations set status='interrupted',updated_at=?,
                error='La solicitud MCP se interrumpió al reiniciar el servidor.'
                where status='running'""",
                (now,),
            )
            running_batches = c.execute(
                "select project_id,jobs_json from talend_apply_batches where status in ('queued','running')"
            ).fetchall()
            for project_id, jobs_json in running_batches:
                jobs = json.loads(jobs_json)
                for job in jobs:
                    if job.get("status") == "running":
                        job["status"] = "interrupted"
                        job["error"] = "El Job se interrumpió al reiniciar el servidor."
                c.execute(
                    """update talend_apply_batches set jobs_json=?,current_program=null
                    where project_id=?""",
                    (json.dumps(jobs, ensure_ascii=False, sort_keys=True), project_id),
                )
            c.execute(
                """update talend_apply_batches set status='interrupted',updated_at=?,
                error='El lote MCP se interrumpió al reiniciar el servidor.'
                where status in ('queued','running')""",
                (now,),
            )

    @staticmethod
    def _talend_apply_batch_from_row(row: tuple) -> dict:
        programs = json.loads(row[3])
        return {
            "project_id": row[0],
            "revision_hash": row[1],
            "status": row[2],
            "programs": programs,
            "jobs": json.loads(row[4]),
            "current_program": row[5],
            "completed_jobs": row[6],
            "total_jobs": len(programs),
            "error": row[7],
            "attempt_count": row[8],
            "started_at": row[9],
            "updated_at": row[10],
            "warnings": json.loads(row[11]),
        }

    def get_talend_apply_batch_state(self, project_id: str) -> dict | None:
        with closing(self._conn()) as c:
            row = c.execute(
                """select project_id,revision_hash,status,programs_json,jobs_json,current_program,
                completed_jobs,error,attempt_count,started_at,updated_at,warnings_json
                from talend_apply_batches where project_id=?""",
                (project_id,),
            ).fetchone()
        return self._talend_apply_batch_from_row(row) if row else None

    def begin_talend_apply_batch(
        self,
        project_id: str,
        revision_hash: str,
        programs: list[str],
        *,
        retry_conflicts: bool = False,
        retry_programs: set[str] | None = None,
        allow_revision_reset: bool = False,
    ) -> tuple[dict, bool]:
        now = datetime.now(UTC).isoformat()
        encoded_programs = json.dumps(programs, ensure_ascii=False)
        initial_jobs = [
            {"program": program, "status": "pending", "result": None, "error": None}
            for program in programs
        ]
        encoded_jobs = json.dumps(initial_jobs, ensure_ascii=False, sort_keys=True)
        retry_programs = retry_programs or set()
        if not retry_programs.issubset(programs):
            raise ValueError("El lote recibió programas de reintento que no pertenecen al proyecto.")
        with closing(self._conn()) as c, c:
            c.execute("begin immediate")
            row = c.execute(
                """select project_id,revision_hash,status,programs_json,jobs_json,current_program,
                completed_jobs,error,attempt_count,started_at,updated_at,warnings_json
                from talend_apply_batches where project_id=?""",
                (project_id,),
            ).fetchone()
            if row is None:
                c.execute(
                    """insert into talend_apply_batches
                    (project_id,revision_hash,status,programs_json,jobs_json,current_program,
                     completed_jobs,error,attempt_count,started_at,updated_at)
                    values (?,?, 'queued', ?, ?, null, 0, null, 1, ?, ?)""",
                    (project_id, revision_hash, encoded_programs, encoded_jobs, now, now),
                )
                row = c.execute(
                    """select project_id,revision_hash,status,programs_json,jobs_json,current_program,
                    completed_jobs,error,attempt_count,started_at,updated_at,warnings_json
                    from talend_apply_batches where project_id=?""",
                    (project_id,),
                ).fetchone()
                return self._talend_apply_batch_from_row(row), True

            if row[1] != revision_hash:
                previous_programs = json.loads(row[3])
                previous_jobs = json.loads(row[4])
                safe_to_reset = (
                    allow_revision_reset
                    and row[2] in {"failed", "conflict"}
                    and previous_programs == programs
                    and len(previous_jobs) == len(programs)
                    and all(
                        item.get("status") in {"failed", "conflict"}
                        and item.get("result") is None
                        for item in previous_jobs
                    )
                )
                if not safe_to_reset:
                    raise ValueError(
                        "El proyecto ya tiene un lote Talend con otra revisión; crea un nuevo ZIP para evitar sobrescribir Jobs."
                    )

            if row[2] in {"queued", "running"} or (
                row[2] == "applied" and not retry_programs
            ) or (
                row[2] == "conflict" and not retry_conflicts
            ):
                return self._talend_apply_batch_from_row(row), False

            previous_jobs = json.loads(row[4])
            previous_by_program = {item["program"]: item for item in previous_jobs}
            retry_jobs = []
            for program in programs:
                previous_job = previous_by_program.get(program, {})
                if previous_job.get("status") == "applied" and program not in retry_programs:
                    retry_jobs.append(previous_job)
                else:
                    retry_jobs.append(
                        {"program": program, "status": "pending", "result": None, "error": None}
                    )
            encoded_retry_jobs = json.dumps(retry_jobs, ensure_ascii=False, sort_keys=True)
            completed_jobs = sum(item["status"] == "applied" for item in retry_jobs)

            c.execute(
                """update talend_apply_batches set revision_hash=?,programs_json=?,status='queued',jobs_json=?,current_program=null,
                completed_jobs=?,error=null,attempt_count=attempt_count+1,started_at=?,updated_at=?
                where project_id=?""",
                (revision_hash, encoded_programs, encoded_retry_jobs, completed_jobs, now, now, project_id),
            )
            row = c.execute(
                """select project_id,revision_hash,status,programs_json,jobs_json,current_program,
                completed_jobs,error,attempt_count,started_at,updated_at,warnings_json
                from talend_apply_batches where project_id=?""",
                (project_id,),
            ).fetchone()
            return self._talend_apply_batch_from_row(row), True

    def update_talend_apply_batch_state(
        self,
        project_id: str,
        *,
        status: str,
        jobs: list[dict],
        current_program: str | None,
        completed_count: int,
        error: str | None = None,
        warnings: list[str] | None = None,
    ) -> dict:
        now = datetime.now(UTC).isoformat()
        encoded_jobs = json.dumps(jobs, ensure_ascii=False, sort_keys=True)
        encoded_warnings = json.dumps(warnings, ensure_ascii=False) if warnings is not None else None
        with closing(self._conn()) as c, c:
            updated = c.execute(
                """update talend_apply_batches set status=?,jobs_json=?,current_program=?,
                completed_jobs=?,error=?,updated_at=?,warnings_json=coalesce(?,warnings_json) where project_id=?""",
                (status, encoded_jobs, current_program, completed_count, error, now, encoded_warnings, project_id),
            ).rowcount
            if not updated:
                raise ValueError("El lote Talend del proyecto no existe.")
            row = c.execute(
                """select project_id,revision_hash,status,programs_json,jobs_json,current_program,
                completed_jobs,error,attempt_count,started_at,updated_at,warnings_json
                from talend_apply_batches where project_id=?""",
                (project_id,),
            ).fetchone()
        return self._talend_apply_batch_from_row(row)

    def has_snapshot(self, project_id: str) -> bool:
        with closing(self._conn()) as c:
            return c.execute(
                """select exists(select 1 from source_files where project_id=?)
                or exists(select 1 from skipped where project_id=?)""",
                (project_id, project_id),
            ).fetchone()[0] == 1

    def get_talend_apply_state(self, project_id: str, program: str) -> dict | None:
        with closing(self._conn()) as c:
            row = c.execute(
                """select revision_hash,status,identity_json,result_json,error,started_at,updated_at
                from talend_apply_operations where project_id=? and program=?""",
                (project_id, program),
            ).fetchone()
        if row is None:
            return None
        return {
            "revision_hash": row[0],
            "status": row[1],
            "identity": json.loads(row[2]),
            "result": json.loads(row[3]) if row[3] else None,
            "error": row[4],
            "started_at": row[5],
            "updated_at": row[6],
        }

    def save_talend_apply_state(
        self,
        project_id: str,
        program: str,
        *,
        revision_hash: str,
        status: str,
        identity: dict,
        result: dict | None = None,
        error: str | None = None,
    ) -> None:
        now = datetime.now(UTC).isoformat()
        encoded_identity = json.dumps(identity, ensure_ascii=False, sort_keys=True)
        encoded_result = json.dumps(result, ensure_ascii=False, sort_keys=True) if result is not None else None
        with closing(self._conn()) as c, c:
            c.execute(
                """insert into talend_apply_operations
                (project_id,program,revision_hash,status,identity_json,result_json,error,started_at,updated_at)
                values (?,?,?,?,?,?,?,?,?)
                on conflict(project_id,program) do update set
                revision_hash=excluded.revision_hash,status=excluded.status,
                identity_json=excluded.identity_json,result_json=excluded.result_json,
                error=excluded.error,updated_at=excluded.updated_at""",
                (
                    project_id,
                    program,
                    revision_hash,
                    status,
                    encoded_identity,
                    encoded_result,
                    error,
                    now,
                    now,
                ),
            )

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
