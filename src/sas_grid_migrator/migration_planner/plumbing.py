"""Fontanería de SAS que no se migra a Talend.

Son operaciones que sirven al propio SAS para orquestar, esperar, medir o limpiar (shell auxiliar,
polling, mensajes, tiempos, variables de control, borrado de temporales, troceado por lotes).
Talend resuelve esas necesidades con otros mecanismos (triggers, tStatCatcher, tDie, Batch size...).
Cada caso detectado se registra en `JobPlan.not_migrated` con su equivalente, en vez de generar pasos.

La clasificación es por FORMA: lo que hace la operación (ejecuta un comando, espera, escribe en el
log, mide tiempos, asigna macro variables, borra temporales, trocea por rangos de observaciones), no
el nombre de la macro que la contiene. Una macro entera es fontanería si la mayoría de su cuerpo lo
es, si solo llama a macros de fontanería, o si su cuerpo no produce datos.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass

from sas_grid_migrator.intermediate_representation.models import IROperation


@dataclass(frozen=True)
class Plumbing:
    category: str
    what: str
    reason: str
    talend: str


#: Operaciones que, por su tipo, producen o transforman datos. Una macro sin ninguna de ellas no produce datos.
DATA_TYPES = frozenset({
    "read", "write", "append", "filter", "compute", "aggregate", "join", "union", "dedupe", "sort",
    "select_columns", "rename", "project", "stateful", "format_definition", "report", "dynamic_code",
    "unsupported", "sql_passthrough", "read_file", "write_file", "inline_data", "maintenance",
})
#: Patrón de espera o sondeo (shell con sleep/until/ps, o bucles de espera).
_SHELL_POLL = re.compile(r"\b(sleep|until|wait|ps\s+-|while|do)\b", re.IGNORECASE)
_SLEEP_CALL = re.compile(r"\bsleep\s*\(", re.IGNORECASE)
#: Lectura por rangos de observaciones (troceo): `firstobs=` o `nlobs` de un dataset.
_CHUNKING = re.compile(r"\bnlobs\b|\bfirstobs\s*=\s*[&%]|\bobs\s*=\s*[&%]", re.IGNORECASE)
_PUT = re.compile(r"^\s*%?put\b", re.IGNORECASE)
_DROP_TABLE = re.compile(r"\bdrop\s+table\b", re.IGNORECASE)
_INTO = re.compile(r"\binto\s*:", re.IGNORECASE)
_ONLY_MACRO_NAME = re.compile(r"^&\w+\.?$")
_LOOP_INDEX = re.compile(r"&(i|j|k|n|sessio\w*)\b\.?", re.IGNORECASE)
_METADATA_PREFIX = "dictionary."
_SYMPUT = re.compile(r"symputx?\(", re.IGNORECASE)
_DATETIME = re.compile(r"datetime\(\)", re.IGNORECASE)
#: Valores de control generados en un paso de datos (identificadores de ejecución, azar).
_CONTROL_VALUE = re.compile(r"symget|ranuni", re.IGNORECASE)
#: Prefijo de las macros auxiliares que SAS Studio añade a sus consultas (visor de resultados).
_STUDIO_HELPER_PREFIX = "web_"

#: Parte mínima de operaciones de fontanería para que una macro entera se considere fontanería.
MACRO_SHARE = 0.7


def _count_only(details: dict) -> bool:
    """Agregado que solo cuenta filas (select count(*) sin agrupar): su resultado es un número, no un dataset."""
    selects = details.get("select")
    if details.get("group_by") not in (None, [], "[]") or not isinstance(selects, list) or not selects:
        return False
    # Solo el conteo impreso en el log (sin alias): un `as n` alimenta una tabla y sí es dato.
    return all(
        isinstance(item, dict)
        and not item.get("alias")
        and re.sub(r"\s+", "", str(item.get("expression", ""))).lower() == "count(*)"
        for item in selects
    )


def _is_counter(assignment: dict) -> bool:
    """Contador de registros: `n + 1` sobre la misma variable (suma de un literal 1)."""
    target = str(assignment.get("target", ""))
    expression = re.sub(r"\s+", "", str(assignment.get("expression", "")))
    return bool(assignment.get("accumulates")) and expression.casefold() == f"{target}+1".casefold()


def is_studio_helper(name: str, defined: set[str]) -> bool:
    """Auxiliar de visor de SAS Studio: llamada con prefijo `web_` a una macro que el proyecto no define."""
    lowered = name.casefold()
    return lowered.startswith(_STUDIO_HELPER_PREFIX) and lowered not in defined


_SYMPUT_NAMES = re.compile(r"symputx?\(\s*['\"](\w+)['\"]", re.IGNORECASE)
_LIBRARY = re.compile(r"\blibrary\s*=\s*(\w+)", re.IGNORECASE)


def symput_names(op: IROperation) -> set[str]:
    """Macro variables que asigna una operación con `call symputx('nombre', ...)`."""
    return {name.casefold() for name in _SYMPUT_NAMES.findall(str(op.details))}


def macro_refs(ops: list[IROperation]) -> set[str]:
    """Macro variables que usan operaciones de DATOS (`&nombre`). Un comando de shell o una llamada a
    macro que usa una macro variable no la convierte en dato."""
    refs: set[str] = set()
    for op in ops:
        if op.type not in DATA_TYPES:
            continue
        refs.update(name.casefold() for name in re.findall(r"&(\w+)", str(op.details)))
        refs.update(name.casefold() for name in re.findall(r"&(\w+)", " ".join(op.inputs + op.outputs)))
    return refs


def plumbing_of(op: IROperation, used: frozenset[str] = frozenset()) -> Plumbing | None:
    """Clasifica una operación de fontanería por lo que hace; None si la operación sí se migra.

    `used`: macro variables que alguna operación de datos usa; un `call symputx` que las asigna no es
    fontanería (su valor llega a los datos)."""
    d = op.details
    if op.type == "macro_call":
        return None  # la llamada se decide por la macro llamada (plumbing_macros)
    if op.type == "compute" and not op.outputs and any(_is_counter(a) for a in d.get("assignments") or []):
        return Plumbing(
            "conteo", "contador de registros del paso (acumulador n + 1)",
            "Cuenta filas para un mensaje o una comprobación; no transforma datos.",
            "tStatCatcher registra los conteos de filas del Job.",
        )
    if symput_names(op) & used:
        return None
    text = str(d.get("text") or d.get("statement") or "")
    if op.type == "os_command":
        if _SHELL_POLL.search(text):
            return Plumbing(
                "espera", "sondeo de procesos con sleep/until del shell",
                "Espera a que terminen procesos del sistema; no transforma datos.",
                "Talend continúa con OnSubjobOk cuando el paso anterior termina.",
            )
        return Plumbing(
            "shell_auxiliar", "comando del sistema operativo auxiliar",
            "El comando del shell no transforma filas; solo orquesta el SAS.",
            "tSystem solo si el comando es imprescindible; si no, el orden lo marca el Job.",
        )
    if op.type == "unsupported" and str(d.get("statement") or "") in ("connect", "disconnect"):
        return Plumbing(
            "conexion", "apertura o cierre de la sesión con la base de datos",
            "Gestiona la sesión del motor; no transforma datos.",
            "La conexión compartida del Job (tipo Connection) y su cierre los pone la estructura.",
        )
    if op.type == "sql_passthrough" and _DROP_TABLE.search(text):
        return Plumbing(
            "limpieza_tablas", "borrado de una tabla de la base antes de cargar (DROP TABLE)",
            "Elimina la tabla de trabajo para reiniciar la carga; no transforma filas.",
            "La acción de tabla del componente de salida (DROP_CREATE/CLEAR) reemplaza la tabla.",
        )
    if op.type == "unsupported" and not d.get("statement") and (
        text.startswith("%") or any(name.startswith("%") for name in op.outputs)
    ):
        return Plumbing(
            "control_macro", "bucle o condicional del lenguaje macro (%do, %if, %to)",
            "Controla qué código se genera; no transforma filas.",
            "No hace falta: el orden y las repeticiones los marca el Job.",
        )
    if op.type == "write" and not op.inputs and any(_ONLY_MACRO_NAME.match(name) for name in op.outputs):
        # Tabla de control cuyo nombre sale solo de una macro variable (tabla de comandos del programa).
        return Plumbing(
            "carga_comando", "tabla de comandos de carga generada en el programa",
            "Prepara órdenes para el shell o el motor; no transforma filas.",
            "No hace falta: el componente de salida reparte la carga internamente.",
        )
    if op.type == "write" and any("&" in name for name in op.outputs) and _LOOP_INDEX.search(" ".join(op.outputs)):
        # Tabla cuyo nombre sale de una macro variable: las de un bucle son trozos; las de un
        # comando, tablas de control del propio programa.
        if any("&" in name for name in op.inputs) or not op.inputs:
            return Plumbing(
                "troceado_lotes" if op.inputs else "carga_comando",
                "escritura de trozos o de tablas de control con nombre dinámico (macro variable)",
                "Reparte o prepara la carga por trozos o por comandos; no es lógica de negocio.",
                "Talend carga el conjunto completo: el componente de salida usa Batch size o escritura por bloques.",
            )
    if op.type == "unsupported" and _PUT.match(text):
        return Plumbing("mensajes", "%put de traza", "Escribe en el log; no transforma datos.",
                        "tLogRow o los logs de ejecución del Job.")
    if op.type == "set_variable" and _SYMPUT.search(str(d.get("statement") or "")):
        return Plumbing(
            "variables_control", "variable de macro calculada en un paso de datos (call symputx)",
            "Pasa un valor a una macro variable de SAS; no transforma filas.",
            "Variable de contexto del Job, o tJava si el valor se calcula en tiempo de ejecución.",
        )
    if not op.outputs and _SLEEP_CALL.search(json.dumps(d, ensure_ascii=False)):
        return Plumbing(
            "espera", "espera con sleep() dentro de un paso de datos",
            "Pausa la ejecución del SAS; no transforma datos.",
            "Talend continúa con OnSubjobOk cuando el paso anterior termina.",
        )
    if op.type == "compute" and not op.outputs:
        expressions = " ".join(str(a.get("expression", "")) for a in d.get("assignments") or [])
        if _DATETIME.search(expressions):
            return Plumbing(
                "medicion", "cálculo de la duración del programa (datetime)",
                "Calcula duraciones con datetime(); no transforma datos.",
                "tStatCatcher registra la duración de la ejecución del Job.",
            )
        if _CONTROL_VALUE.search(expressions):
            return Plumbing(
                "variables_control", "cálculo de valores de control del programa (identificadores, azar)",
                "Prepara valores de macro variables o identificadores de ejecución; no transforma filas.",
                "Variables de contexto del Job; el identificador de ejecución lo genera Talend.",
            )
    if op.type in ("read", "compute", "unsupported", "read_file") and _CHUNKING.search(
        json.dumps(d, ensure_ascii=False)
    ):
        return Plumbing(
            "troceado_lotes", "troceado de un dataset por rangos de observaciones",
            "Reparte la carga en trozos para que el SAS no se quede sin memoria; no es lógica de negocio.",
            "Talend carga el conjunto completo: el componente de salida usa Batch size o escritura por bloques.",
        )
    if op.type == "aggregate" and not op.outputs and _count_only(d):
        return Plumbing(
            "conteo", "conteo de registros impreso en el log (select count)",
            "Solo muestra el número de filas en el log; no transforma datos.",
            "tStatCatcher registra los conteos de filas del Job.",
        )
    if op.type == "append":
        options = str(d.get("options") or "").lower()
        base = re.search(r"base\s*=\s*([\w.]+)", options)
        data = re.search(r"data\s*=\s*([\w.]+)", options)
        if base and data and base.group(1) == data.group(1):
            return Plumbing(
                "datos_de_prueba", "duplicado de filas de una tabla sobre sí misma (proc append en bucle)",
                "Genera datos de prueba para una prueba de carga; no es lógica de negocio.",
                "tRowGenerator o tFixedFlowInput si la prueba de carga lo necesita; si no, se omite.",
            )
    if op.type == "maintenance":
        statements = [str(s).strip().lower() for s in d.get("statements") or []]
        deletes = str(d.get("proc") or "").lower() == "delete" or any(s.startswith("delete") for s in statements)
        library = _LIBRARY.search(str(d.get("options") or "") + " " + " ".join(d.get("statements") or []))
        temporary = (library is None or library.group(1).lower() == "work") and (
            not op.inputs
            or all(dataset.lower().startswith("work.") or "&" in dataset or "." not in dataset for dataset in op.inputs)
        )
        if deletes and temporary:
            return Plumbing(
                "limpieza_datasets", "borrado de datasets temporales (WORK)",
                "Libera espacio de trabajo del SAS; un dataset temporal no sobrevive al Job.",
                "Sin equivalente: el flujo pasa directo entre componentes y no crea el temporal.",
            )
    return None


def _writes_permanent(op: IROperation) -> bool:
    """Escritura a una tabla que sale del programa (no WORK): una macro que lo hace no es fontanería."""
    return (
        op.type in ("write", "append")
        and any(name and not name.casefold().startswith("work.") for name in op.outputs)
    )


def _is_plumbing_call(op: IROperation, found: dict[str, Plumbing]) -> bool:
    return op.type == "macro_call" and str(op.details.get("name", "")).casefold() in found


def plumbing_macros(macros) -> dict[str, Plumbing]:
    """Macros que son fontanería (transitivo). Clave: nombre en minúsculas.

    Una macro es fontanería si (1) al menos el 70% de su cuerpo es `infrastructure` o llama solo a
    macros de fontanería, o (2) su cuerpo no produce datos: ninguna operación de datos ni llamada a
    una macro que sí los produce. Las llamadas a macros SIN definición en el proyecto son neutras: no
    cuentan ni como fontanería ni como datos (se registran aparte, una vez por nombre). Una macro cuyo
    cuerpo solo llama a macros externas no se da por fontanería: su uso queda como decisión manual.
    """
    found: dict[str, Plumbing] = {}
    by_name = {m.name.casefold(): m for m in macros}

    def neutral(op) -> bool:
        if op.type == "macro_call":
            return str(op.details.get("name", "")).casefold() not in by_name
        # SQL pass-through que arma otra macro (`execute (&cmdqry.) by motor`): su texto lo pone el llamador.
        return op.type in ("unsupported", "sql_passthrough") and _DYNAMIC_PASS_THROUGH.match(
            str(op.details.get("text", ""))
        ) is not None

    changed = True
    while changed:
        changed = False
        for key, macro in by_name.items():
            if key in found:
                continue
            if macro.transfer_table:
                # Su llamada es la escritura al motor (ver builder); el cuerpo solo prepara la carga.
                found[key] = Plumbing(
                    "carga_comando", f"entrega de la tabla WORK.{macro.transfer_table} al motor (comando de carga)",
                    "La carga la hace el motor con la escritura del paso de transferencia; el cuerpo solo orquesta.",
                    "Tabla de salida del componente del motor (tImpalaOutput o equivalente).",
                )
                changed = True
                continue
            if any(_writes_permanent(op) for op in macro.operations):
                continue  # escribe fuera de WORK: es trabajo de datos, aunque el resto sea control
            ops = [op for op in macro.operations if not neutral(op)]
            external = len(macro.operations) - len(ops)
            if not ops and external:
                continue  # solo llamadas externas: decisión manual, no fontanería
            infra_ids = {
                id(op) for op in ops
                if op.type == "infrastructure" or _is_plumbing_call(op, found)
            }
            if ops and len(infra_ids) / len(ops) >= MACRO_SHARE:
                found[key] = _summary([op for op in ops if id(op) in infra_ids], found)
                changed = True
                continue
            rest = [op for op in ops if id(op) not in infra_ids]
            produces = any(op.type in DATA_TYPES or op.type == "macro_call" for op in rest)
            if not produces:
                found[key] = Plumbing(
                    "variables_control", "macro sin datos (solo control, mensajes o variables)",
                    "Su cuerpo no lee, escribe ni transforma datos; solo controla el programa.",
                    "No hace falta: el orden y las variables de contexto del Job cubren lo que hacía.",
                )
                changed = True
    return found


def macro_parts(macro, found: dict[str, Plumbing], macros_by_name: dict) -> list[Plumbing]:
    """Partes de fontanería de una macro, una por (categoría, qué hace), siguiendo las llamadas a macros
    de fontanería. Así el informe dice qué se quita (troceo, espera, mensajes...), no solo la macro."""
    parts: dict[tuple[str, str], Plumbing] = {}

    def visit(current, seen: set[str]) -> None:
        for op in current.operations:
            if op.type == "infrastructure":
                info = Plumbing(**op.details["plumbing"])
                parts.setdefault((info.category, info.what), info)
            elif _is_plumbing_call(op, found):
                nested = str(op.details.get("name", "")).casefold()
                if nested in macros_by_name and nested not in seen:
                    visit(macros_by_name[nested], seen | {nested})
                elif nested in found:
                    info = found[nested]
                    parts.setdefault((info.category, info.what), info)

    visit(macro, {macro.name.casefold()})
    return list(parts.values()) or [found[macro.name.casefold()]]


def _summary(infra, found: dict[str, Plumbing]) -> Plumbing:
    parts: dict[str, Plumbing] = {}
    for op in infra:
        if op.type == "infrastructure":
            info = Plumbing(**op.details["plumbing"])
        else:
            info = found[str(op.details.get("name", "")).casefold()]
        parts.setdefault(info.category, info)
    categories = ", ".join(sorted(parts))
    first = next(iter(parts.values()))
    return Plumbing(
        category=first.category,
        what=f"macro de fontanería ({categories})",
        reason=f"La mayoría de sus operaciones es fontanería ({categories}); {first.reason}",
        talend=first.talend,
    )


def tag_macro_calls(ir, found: dict[str, Plumbing]) -> None:
    """Las llamadas a una macro de fontanería pasan a `infrastructure` (en el programa y en todos los cuerpos)."""
    from dataclasses import asdict

    for ops in [ir.operations, *(m.operations for m in ir.macros)]:
        for op in ops:
            name = str(op.details.get("name", "")).casefold()
            if op.type == "macro_call" and name in found:
                op.type = "infrastructure"
                op.details = {**op.details, "plumbing": asdict(found[name])}


#: Tipos que sacan algo al exterior aunque no tengan dataset de salida (informes, escrituras, salidas de SQL).
_OUTPUT_TYPES = frozenset({"report", "unsupported", "write", "append", "write_file", "dynamic_code", "maintenance"})
_NO_OUTPUT_STEP = Plumbing(
    "variables_control", "paso sin salida de datos (data _null_): calcula o lee variables",
    "Ningún dataset sale de este paso; solo asigna valores o lee un archivo de control.",
    "Variables de contexto del Job o tJava; el archivo de control lo gestiona el Job.",
)
#: Tipos de un paso DATA o PROC que, sin dataset de salida, no sacan filas (solo calculan, leen o filtran).
_SILENT_STEP_TYPES = frozenset({
    "compute", "read_file", "set_variable", "read", "select_columns", "filter", "project", "aggregate",
    "sort", "dedupe", "rename", "stateful",
})
_CHUNK_BY_ROW = Plumbing(
    "troceado_lotes", "reparto de filas en trozos por número de fila (_N_)",
    "Reparte el dataset en trozos para la carga; no es lógica de negocio.",
    "Talend carga el conjunto completo: el componente de salida usa Batch size o escritura por bloques.",
)
_TEMPORARY_CONTROL = Plumbing(
    "variables_control", "tabla temporal solo para comprobar o contar (sin salida de datos)",
    "Un dataset de trabajo que solo consume la fontanería de control; no llega a ningún dato del negocio.",
    "Sin equivalente: el control lo hace tStatCatcher o tDie del Job.",
)
_VARIABLES_FROM_DATA = Plumbing(
    "variables_control", "macro variables calculadas desde datos (select into)",
    "El paso solo asigna valores a macro variables para armar nombres o mensajes; no produce filas.",
    "Variables de contexto del Job, o tJava si el valor se calcula en tiempo de ejecución.",
)
_METADATA = Plumbing(
    "metadatos", "lectura de metadatos del sistema (proc contents o diccionario)",
    "Lista tablas o columnas para armar nombres o macro variables; no transforma datos.",
    "Sin equivalente: el esquema viaja con el flujo de Talend.",
)


_ROW_CHUNK = re.compile(r"_n_\s*-\s*1\s*\)\s*/", re.IGNORECASE)
_DYNAMIC_PASS_THROUGH = re.compile(r"^\s*execute\s*\(\s*&[\w.]+\.?\s*\)", re.IGNORECASE)


def tag_structural(ops: list[IROperation], used: frozenset[str] = frozenset()) -> dict[int, Plumbing]:
    """Fontanería que depende del paso o del flujo, no de una sola operación. Devuelve {id(op): Plumbing}.

    - Un paso que selecciona hacia macro variables (`into:`) no produce datos: sus operaciones sin salida
      de datos son fontanería.
    - Un paso que reparte filas en trozos por número de fila (`_N_`) es troceo: todo el paso lo es.
    - Los metadatos del sistema (`proc contents`, `dictionary.*`) y los datasets que de ellos se derivan
      (solo sirven para armar nombres o macro variables) no son datos del negocio.
    - Un dataset temporal (WORK) cuyos únicos consumidores son fontanería es fontanería (control de errores
      que cuenta filas de un log, por ejemplo).
    """
    found: dict[int, Plumbing] = {}
    steps: dict[str, list[IROperation]] = {}
    for op in ops:
        steps.setdefault(op.step, []).append(op)
    for group in steps.values():
        if any(symput_names(op) & used for op in group):
            continue  # el paso asigna macro variables que usan los datos
        # Un paso sin ningún dataset de salida (DATA _null_, o solo lee un archivo de control) no genera filas.
        if (
            group
            and all(op.type in _SILENT_STEP_TYPES for op in group)
            and any(op.type in ("compute", "read_file", "set_variable") for op in group)
            and not any(op.outputs for op in group)
        ):
            for op in group:
                found[id(op)] = _NO_OUTPUT_STEP
        if any(_INTO.search(str(op.details)) for op in group):
            for op in group:
                if not op.outputs and op.type != "infrastructure":
                    found[id(op)] = _VARIABLES_FROM_DATA
        if any(_ROW_CHUNK.search(str(op.details)) for op in group):
            for op in group:
                if op.type != "infrastructure":
                    found[id(op)] = _CHUNK_BY_ROW
    metadata: set[str] = set()
    for op in ops:
        inputs = {dataset.casefold() for dataset in op.inputs}
        # proc contents solo es metadato si mira WORK: sobre una tabla real sigue siendo una decisión.
        is_metadata = (
            (op.type == "maintenance" and str(op.details.get("proc", "")).lower() == "contents"
             and all(d.lower().startswith("work.") or "." not in d for d in op.inputs))
            or any(name.startswith(_METADATA_PREFIX) for name in inputs)
            or bool(inputs & metadata)
        )
        if is_metadata:
            metadata.update(dataset.casefold() for dataset in op.outputs)
            if op.type == "maintenance" and str(op.details.get("proc", "")).lower() == "contents":
                metadata.add("work._all_")
            found[id(op)] = _METADATA
    # Temporales cuyos únicos consumidores ya son fontanería: el productor también lo es (punto fijo).
    changed = True
    while changed:
        changed = False
        for op in ops:
            if id(op) in found or op.type == "infrastructure" or not op.outputs:
                continue
            outs = {name.casefold() for name in op.outputs}
            if not all(name.startswith("work.") for name in outs):
                continue
            consumers = [o for o in ops if o is not op and outs & {d.casefold() for d in o.inputs}]
            if consumers and all(id(o) in found or o.type == "infrastructure" for o in consumers):
                found[id(op)] = _TEMPORARY_CONTROL
                changed = True
    return found
