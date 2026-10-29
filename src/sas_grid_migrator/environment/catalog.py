"""Catálogo de entorno (WP5): lo que el SAS no trae y hay que decir una vez por proyecto.

Un `environment.json` por proyecto declara cada `libname` (motor y conexión, sin credenciales: solo el nombre del grupo de
contexto), y cada dataset (tabla física o archivo, formato y columnas con sus tipos). El planificador lo usa para
configurar las lecturas y escrituras sin dejar pendientes, pero **no inventa nada**: lo que el catálogo no declara sigue
siendo un pendiente con su motivo.

Ejemplo completo en `examples/environment.example.json`; el esquema versionado está en
`schemas/environment.schema.json`.
"""

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

#: Tipos de Talend admitidos en una columna del catálogo.
TALEND_TYPES = {"id_String", "id_Integer", "id_Long", "id_Double", "id_Float", "id_BigDecimal", "id_Date", "id_Boolean"}

#: Cómo se lee cada tipo de dataset.
DatasetKind = Literal["table", "delimited", "positional", "excel", "sas7bdat"]


class CatalogError(ValueError):
    """El catálogo no sirve: se dice por qué en vez de seguir con datos dudosos."""


class EnvironmentColumn(BaseModel):
    name: str
    talend_type: str
    nullable: bool = True
    length: int | None = None
    precision: int | None = None


class EnvironmentLibrary(BaseModel):
    name: str  # el libname de SAS, tal cual aparece en el programa
    engine: str  # clave de `rules/mappings/talend-components.json` → componentes de lectura/escritura
    connection: str | None = None  # grupo de contexto/conexión de Talend; nunca usuario ni contraseña
    path: str | None = None  # para una librería de carpeta
    note: str | None = None

    @property
    def is_file_library(self) -> bool:
        return self.engine in {"base", "file"}


class EnvironmentDataset(BaseModel):
    library: str
    name: str
    kind: DatasetKind = "table"
    target: str | None = None  # tabla física o ruta; por defecto, el nombre del dataset
    delimiter: str | None = None
    header: bool | None = None
    encoding: str | None = None
    columns: list[EnvironmentColumn] = Field(default_factory=list)

    @property
    def physical(self) -> str:
        return self.target or self.name


class EnvironmentCatalog(BaseModel):
    schema_version: int = 1
    project: str | None = None
    libraries: list[EnvironmentLibrary] = Field(default_factory=list)
    datasets: list[EnvironmentDataset] = Field(default_factory=list)

    def library(self, name: str) -> EnvironmentLibrary | None:
        target = name.casefold()
        return next((lib for lib in self.libraries if lib.name.casefold() == target), None)

    def dataset(self, libname: str, name: str) -> EnvironmentDataset | None:
        """Dataset por librería y nombre; `work` no se busca (es temporal, no está en el catálogo)."""
        if libname.casefold() == "work":
            return None
        library = libname.casefold()
        dataset = name.casefold()
        return next(
            (
                item
                for item in self.datasets
                if item.library.casefold() == library and item.name.casefold() == dataset
            ),
            None,
        )

    def dataset_by_path(self, path: str) -> EnvironmentDataset | None:
        """Dataset por la ruta física (para `PROC IMPORT` y `INFILE` de un archivo del catálogo)."""
        target = path.replace("\\", "/").casefold()
        return next(
            (item for item in self.datasets if item.physical.replace("\\", "/").casefold() == target),
            None,
        )


def validate(catalog: EnvironmentCatalog, engines: set[str]) -> EnvironmentCatalog:
    """Comprueba lo que haría fallar el Job: motores desconocidos, datasets huérfanos, tipos raros."""
    seen: set[str] = set()
    for lib in catalog.libraries:
        key = lib.name.casefold()
        if key in seen:
            raise CatalogError(f"librería duplicada en el catálogo: {lib.name}")
        seen.add(key)
        if not lib.is_file_library and lib.engine.casefold() not in engines:
            raise CatalogError(
                f"librería {lib.name}: motor {lib.engine!r} sin componentes en el catálogo de Talend "
                f"(admitidos: {', '.join(sorted(engines))})"
            )
    keys: set[tuple[str, str]] = set()
    for dataset in catalog.datasets:
        key = (dataset.library.casefold(), dataset.name.casefold())
        if key in keys:
            raise CatalogError(f"dataset duplicado en el catálogo: {dataset.library}.{dataset.name}")
        keys.add(key)
        if catalog.library(dataset.library) is None:
            raise CatalogError(f"dataset {dataset.library}.{dataset.name}: la librería no está declarada")
        if dataset.kind == "delimited" and not dataset.delimiter:
            raise CatalogError(f"dataset {dataset.library}.{dataset.name}: falta el delimitador")
        for column in dataset.columns:
            if column.talend_type not in TALEND_TYPES:
                raise CatalogError(
                    f"dataset {dataset.library}.{dataset.name}: tipo {column.talend_type!r} de {column.name} "
                    f"no es un tipo de Talend (admitidos: {', '.join(sorted(TALEND_TYPES))})"
                )
    return catalog


def load(path: Path, engines: set[str]) -> EnvironmentCatalog:
    """Lee y valida un `environment.json`; falla con el motivo exacto, nunca con un catálogo a medias."""
    if not path.exists():
        raise CatalogError(f"no existe el catálogo de entorno: {path}")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise CatalogError(f"{path.name} no es JSON válido: {error}") from error
    try:
        catalog = EnvironmentCatalog.model_validate(raw)
    except ValidationError as error:
        raise CatalogError(f"{path.name} no cumple el esquema: {error}") from error
    if catalog.schema_version != 1:
        raise CatalogError(
            f"{path.name}: versión de esquema {catalog.schema_version} no soportada (se espera 1)"
        )
    return validate(catalog, engines)


def load_if_present(path: Path, engines: set[str]) -> EnvironmentCatalog | None:
    """El catálogo es opcional: sin él, el plan sigue pidiendo los datos que faltan."""
    return load(path, engines) if path.exists() else None
