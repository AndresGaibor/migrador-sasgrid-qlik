from datetime import UTC, datetime
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, Field

SCHEMA_VERSION = "1"


class FileKind(StrEnum):
    SAS = "sas"
    SHELL = "shell"
    LOG = "log"
    DOC = "doc"
    OTHER = "other"


class Severity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class SourceFile(BaseModel):
    path: str  # relativa, separador "/"
    sha256: str
    size: int
    kind: FileKind
    encoding: str | None = None  # None si no es texto


class Skipped(BaseModel):
    path: str
    reason: str


class Manifest(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    files: list[SourceFile] = Field(default_factory=list)
    skipped: list[Skipped] = Field(default_factory=list)


class Project(BaseModel):
    id: str
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Evidence(BaseModel):
    file: str
    line: int


class Finding(BaseModel):
    """Hallazgo con ubicación de origen; lo producen el parser y los analizadores (F2+)."""

    code: str
    severity: Severity
    message: str
    evidence: Evidence
    priority: Literal["P0", "P1", "P2"] | None = None
