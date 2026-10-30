"""Representación intermedia: operaciones de datos independientes de Talend.

El parser produce estructura SAS; esta capa produce *qué hace* el programa (leer, filtrar,
unir, agregar, escribir…). El planner traduce operaciones a pasos de Talend sin acoplarse al parser.
"""

from typing import Any, Literal

from pydantic import BaseModel

from sas_grid_migrator.sas_parser.ast import Loc

OpType = Literal[
    "read",  # dataset o tabla
    "read_file",  # archivo externo (infile, proc import)
    "inline_data",  # datalines
    "filter",
    "join",
    "union",
    "aggregate",
    "sort",
    "dedupe",
    "project",  # SELECT de columnas/expresiones
    "select_columns",  # keep/drop
    "rename",
    "compute",  # asignaciones y condicionales de DATA step
    "stateful",  # retain / first. / last. / arrays / hash
    "write",
    "write_file",
    "append",
    "format_definition",
    "set_variable",  # call symput / select into
    "macro_call",
    "include",
    "dynamic_code",  # call execute
    "os_command",
    "report",  # PROC PRINT/REPORT/…
    "maintenance",
    "unsupported",
    "sql_passthrough",  # SQL que se ejecuta en el motor externo (`execute (...) by motor`): tiene componente Row
    "infrastructure",  # fontanería de SAS (shell, espera, mensajes, tiempos, troceo): no se migra
]


class IROperation(BaseModel):
    id: str
    type: OpType
    step: str  # subjob: identificador del paso SAS que lo origina
    evidence: Loc
    inputs: list[str] = []
    outputs: list[str] = []
    details: dict[str, Any] = {}
    constructs: list[str] = []
    confidence: Literal["high", "medium", "low"] = "high"
    notes: list[str] = []


class MacroIR(BaseModel):
    name: str  # nombre único dentro del programa; las variantes llevan sufijo _v2, _v3…
    params: list[str]
    loc: Loc
    operations: list[IROperation]
    source_name: str | None = None  # nombre SAS original cuando `name` es una variante (_vN)
    copies: int = 1  # definiciones idénticas colapsadas en esta (misma macro repetida)
    duplicate_lines: list[int] = []  # líneas de las copies idénticas descartadas
    notes: list[str] = []
    #: Tabla WORK que la macro entrega a un motor externo (comando de carga): None si no transfiere.
    transfer_table: str | None = None


class LibraryRef(BaseModel):
    name: str
    engine: str | None = None
    path: str | None = None
    #: Esquema del motor (`schema=` del libname), si lo declara: para traducir `lib.tabla` a `esquema.tabla`.
    db_schema: str | None = None


class ProgramIR(BaseModel):
    file: str
    sha256: str | None = None
    operations: list[IROperation] = []
    macros: list[MacroIR] = []
    parameters: dict[str, str] = {}  # %let de primer nivel
    parameter_lines: dict[str, int] = {}  # línea del %let de primer nivel (contexto y evidencia)
    libraries: list[LibraryRef] = []
    includes: list[str] = []
