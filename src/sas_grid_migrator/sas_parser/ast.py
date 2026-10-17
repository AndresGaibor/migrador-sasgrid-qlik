"""Modelo de salida del parser SAS: estructura por pasos con ubicación de origen.

Es un árbol a nivel de paso/sentencia, no una gramática completa de expresiones.
Cada nodo lleva `constructs`: etiquetas que `semantic_analysis` clasifica con `rules/sas/`.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, Field

from sas_grid_migrator.domain.models import Finding


class Loc(BaseModel):
    file: str
    line: int
    end_line: int


class DatasetRef(BaseModel):
    raw: str
    lib: str | None = None
    name: str
    dynamic: bool = False  # contiene referencias de macro (&var, %fn)
    options: str | None = None
    in_var: str | None = None
    alias: str | None = None


class SqlJoin(BaseModel):
    kind: str
    table: DatasetRef | None = None
    on: str | None = None


class SqlQuery(BaseModel):
    kind: str
    target: DatasetRef | None = None
    select_list: str | None = None
    distinct: bool = False
    sources: list[DatasetRef] = []
    joins: list[SqlJoin] = []
    where: str | None = None
    group_by: str | None = None
    having: str | None = None
    order_by: str | None = None
    into: list[str] = []
    text: str
    loc: Loc
    constructs: list[str] = []


class MacroParam(BaseModel):
    name: str
    default: str | None = None


class MacroCall(BaseModel):
    name: str
    line: int


class StepStmt(BaseModel):
    """Sentencia de un paso con su línea y palabra clave (texto recortado a 600 caracteres)."""

    line: int
    kw: str
    text: str


class DataStep(BaseModel):
    type: Literal["data_step"] = "data_step"
    loc: Loc
    outputs: list[DatasetRef] = []
    inputs: list[DatasetRef] = []
    input_kind: str | None = None  # set | merge | update | modify
    by: list[str] = []
    where: list[str] = []
    subsetting_if: list[str] = []
    keep: list[str] = []
    drop: list[str] = []
    rename: list[str] = []
    retain: list[str] = []
    arrays: list[str] = []
    n_assignments: int = 0
    n_conditionals: int = 0
    functions: list[str] = []
    statements: list[StepStmt] = []
    constructs: list[str] = []
    construct_lines: dict[str, int] = {}  # etiqueta → primera línea donde aparece


class ProcStep(BaseModel):
    type: Literal["proc_step"] = "proc_step"
    loc: Loc
    name: str
    options: str = ""
    inputs: list[DatasetRef] = []
    outputs: list[DatasetRef] = []
    by: list[str] = []
    fields: dict[str, str] = {}
    queries: list[SqlQuery] = []
    statements: list[StepStmt] = []
    constructs: list[str] = []


class GlobalStmt(BaseModel):
    type: Literal["global"] = "global"
    loc: Loc
    kind: str  # libname, filename, let, include, options, macro_call, x_command, other, ...
    fields: dict[str, str] = {}
    text: str = ""
    constructs: list[str] = []


class MacroDef(BaseModel):
    type: Literal["macro_def"] = "macro_def"
    loc: Loc
    name: str
    params: list[MacroParam] = []
    calls: list[str] = []  # macros invocadas en el cuerpo (minúsculas)
    body: list["Node"] = []
    constructs: list[str] = []


Node = Annotated[DataStep | ProcStep | GlobalStmt | MacroDef, Field(discriminator="type")]
MacroDef.model_rebuild()


class ParseStats(BaseModel):
    statements: int = 0
    unrecognized: int = 0  # fuera de macros
    fragments: int = 0  # dentro de macros (código generado, sin contexto de paso)


class ParsedProgram(BaseModel):
    file: str
    sha256: str | None = None
    nodes: list[Node] = []
    macro_calls: list[MacroCall] = []
    findings: list[Finding] = []
    stats: ParseStats = ParseStats()
