import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    max_file_bytes: int = 5 * 1024 * 1024
    max_files: int = 5000
    max_total_bytes: int = 256 * 1024 * 1024
    max_pipeline_concurrency: int = 2
    max_queued_pipelines: int = 20
    import_roots: tuple[Path, ...] = ()  # vacío = cualquier ruta local (uso de un solo usuario)

    @classmethod
    def from_env(cls) -> "Settings":
        e = os.environ
        return cls(
            data_dir=Path(e.get("SGM_DATA_DIR", "./data")),
            max_file_bytes=int(e.get("SGM_MAX_FILE_BYTES", cls.max_file_bytes)),
            max_files=int(e.get("SGM_MAX_FILES", cls.max_files)),
            max_total_bytes=int(e.get("SGM_MAX_TOTAL_BYTES", cls.max_total_bytes)),
            max_pipeline_concurrency=max(1, int(e.get("SGM_MAX_PIPELINE_CONCURRENCY", cls.max_pipeline_concurrency))),
            max_queued_pipelines=max(0, int(e.get("SGM_MAX_QUEUED_PIPELINES", cls.max_queued_pipelines))),
            import_roots=tuple(
                Path(r).resolve() for r in e.get("SGM_IMPORT_ROOTS", "").split(os.pathsep) if r
            ),
        )
