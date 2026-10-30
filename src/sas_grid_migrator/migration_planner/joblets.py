"""Joblets propuestos: convierte las repeticiones de la IR en `JobletPlan` y marca sus pasos.

La detección (huella, clustering, umbrales) vive en `intermediate_representation.repetition`. Aquí se
decide el nombre (`jl_<Rol>`), qué valores son parámetros, qué componentes lo forman y los textos
en español de creación y uso en Talend Studio.

Parámetros: los datasets que cambian entre apariciones son un parámetro cada uno. Los literales que
cambian se agrupan cuando todos se explican con un mismo reemplazo de palabras (p. ej. el alias
`CUMPLE_NORMA_CTE` por `CUMPLE_NORMA_AHORROS` en cuarenta expresiones): ese reemplazo es UN parámetro.
Si no hay un reemplazo consistente, cada literal que cambia es su propio parámetro.
"""

from __future__ import annotations

import re
from dataclasses import replace

from sas_grid_migrator.intermediate_representation.models import IROperation, ProgramIR
from sas_grid_migrator.intermediate_representation.repetition import (
    Repetition,
    Slot,
    find_repetitions,
)
from sas_grid_migrator.migration_planner.models import (
    JobletOccurrence,
    JobletParameter,
    JobletPlan,
    JobPlan,
    PlanStep,
)

MAX_EXAMPLES = 5
_WORD = re.compile(r"[A-Za-z0-9_]+")
_CONVERSION = re.compile(r"\b(input|put)\(", re.IGNORECASE)

#: Rol de negocio por tipo de operación (para el nombre `jl_<Rol>`).
ROLE_BY_TYPE = {
    "join": "Cruce",
    "union": "Union",
    "aggregate": "Agregado",
    "dedupe": "Deduplicado",
    "sort": "Orden",
    "compute": "Calculo",
    "filter": "Filtro",
    "project": "Proyeccion",
    "select_columns": "Columnas",
    "rename": "Renombrado",
    "stateful": "Estado",
    "append": "Adicion",
    "maintenance": "Mantenimiento",
    "report": "Reporte",
    "unsupported": "Manual",
    "dynamic_code": "Dinamico",
    "os_command": "Comando",
    "format_definition": "Formato",
    "set_variable": "Variable",
    "macro_call": "Macro",
    "inline_data": "Datos",
    "read_file": "Archivo",
    "write_file": "ArchivoSalida",
    "read": "Lectura",
    "write": "Escritura",
}
#: Orden de preferencia para el rol: lo más específico gana (un join con filtro es "Cruce").
ROLE_PRIORITY = [
    "join", "union", "aggregate", "dedupe", "sort", "compute", "stateful", "filter", "project",
    "select_columns", "rename", "append", "format_definition", "report", "maintenance",
    "dynamic_code", "unsupported", "read", "write",
]  # fmt: skip
#: Texto de título para los roles con nombre propio.
ROLE_TEXT = {
    "ConversionTipo": "Conversión de tipo con input()/put()",
}
#: Nombres legibles para la última clave de un literal (la pista de `Slot.hint`).
PARAMETER_NAMES = {
    "target": "columna_destino",
    "expression": "expresion",
    "where": "condicion",
    "on": "condicion_union",
    "keys": "claves",
    "group_by": "agrupar",
    "select": "seleccion",
    "file": "archivo",
    "text": "texto",
    "path": "ruta",
    "statement": "sentencia",
    "options": "opciones",
}


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _camel(text: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in re.split(r"[_\W]+", text) if part)


def _literal_name(hint: str) -> str:
    last = hint.split(".")[-1]
    return PARAMETER_NAMES.get(last, _slug(hint.replace(".", "_")) or "valor")


def _unique(name: str, used: set[str]) -> str:
    final, number = name, 2
    while final in used:
        final, number = f"{name}_{number}", number + 1
    used.add(final)
    return final


def _role(rep: Repetition) -> str:
    """Rol de negocio del bloque: nombre de la macro, o el tipo de operación más específico."""
    first = rep.occurrences[0]
    if rep.kind == "macro" and first.macro:
        return _camel(first.macro)
    for op in first.ops:
        if op.type == "compute" and any(
            _CONVERSION.search(str(a.get("expression", ""))) for a in op.details.get("assignments", [])
        ):
            return "ConversionTipo"
    present = {op.type for op in first.ops}
    for kind in ROLE_PRIORITY:
        if kind in present:
            return ROLE_BY_TYPE[kind]
    return "Bloque"


def _substitute(text: str, mapping: dict[str, str]) -> str:
    return _WORD.sub(lambda match: mapping.get(match.group(0), match.group(0)), text)


def _word_renames(
    template: list[Slot], occurrences: list[Repetition], varying: list[int]
) -> list[dict[str, str]] | None:
    """Un reemplazo de palabras por aparición que explica todos los literales que cambian, o None."""
    renames: list[dict[str, str]] = []
    for occurrence in occurrences:
        mapping: dict[str, str] = {}
        for index in varying:
            ref_words = _WORD.findall(template[index].value)
            words = _WORD.findall(occurrence.slots[index].value)
            if len(ref_words) != len(words):
                return None
            for ref_word, word in zip(ref_words, words, strict=True):
                if ref_word != word and mapping.setdefault(ref_word, word) != word:
                    return None
        for index in varying:
            if _substitute(template[index].value, mapping) != occurrence.slots[index].value:
                return None
        renames.append(mapping)
    return renames


def _parameters(rep: Repetition, template: list[Slot]) -> tuple[list[JobletParameter], list[list[str]]]:
    """Parámetros y, para cada uno, su valor en cada aparición (misma longitud que `occurrences`)."""
    used: set[str] = set()
    occurrences = rep.occurrences
    varying = [
        i for i in range(len(template))
        if len({occ.slots[i].value for occ in occurrences}) > 1
    ]
    literal = [i for i in varying if template[i].kind == "valor"]
    # En una transferencia, las tablas WORK son intermedias del joblet: no son parámetros.
    dataset = [
        i for i in varying
        if template[i].kind != "valor"
        and not (rep.kind == "feed" and _is_work(occurrences[0].slots[i].value))
    ]
    rows: list[tuple[str, list[str]]] = []
    renames = _word_renames(template, occurrences, literal) if literal else []
    if renames is not None and literal:
        seen: list[str] = []
        for index in literal:
            for word in _WORD.findall(template[index].value):
                if word not in seen and any(word in mapping for mapping in renames):
                    seen.append(word)
        for word in seen:
            hint = next(index for index in literal if word in _WORD.findall(template[index].value))
            name = _unique(f"{_literal_name(template[hint].hint)}_{word.lower()}", used)
            values = [mapping.get(word, word) for mapping in renames]
            rows.append((name, values))
    else:
        for index in literal:
            name = _unique(f"{_literal_name(template[index].hint)}_{index + 1}", used)
            rows.append((name, [occ.slots[index].value for occ in occurrences]))
    dataset_names = _dataset_names(template)
    for index in dataset:
        name = _unique(dataset_names[index], used)
        rows.append((name, [occ.slots[index].value for occ in occurrences]))
    parameters = [
        JobletParameter(
            name=name,
            context_variable=f"context.{name}",
            example_values=list(dict.fromkeys(values))[:MAX_EXAMPLES],
        )
        for name, values in rows
    ]
    return parameters, [values for _, values in rows]


def _dataset_names(template: list[Slot]) -> list[str]:
    counts: dict[str, int] = {}
    names = []
    for slot in template:
        if slot.kind == "valor":
            names.append("")
            continue
        counts[slot.hint] = counts.get(slot.hint, 0) + 1
        names.append(f"{slot.hint}_{counts[slot.hint]}")
    return names


def _is_work(dataset: str) -> bool:
    return dataset.casefold().startswith("work.")


def _bypass_work_writes(plan: JobPlan, steps: list[PlanStep]) -> None:
    """Quita los pasos que escriben una tabla WORK intermedia del joblet y conecta sus productores con sus
    consumidores: el joblet recibe el flujo directo, sin escribir WORK."""
    removed = {step.id: step for step in steps}
    if not removed:
        return
    for step in plan.steps:
        rewired = []
        for connection in step.connections:
            if connection.from_step in removed:
                for upstream in removed[connection.from_step].connections:
                    if upstream.from_step not in removed:
                        rewired.append(upstream.model_copy(update={"type": connection.type}))
            else:
                rewired.append(connection)
        step.connections = rewired
    plan.steps = [s for s in plan.steps if s.id not in removed]


def _steps_of(ops: list[IROperation], index: dict[str, list[PlanStep]]) -> list[PlanStep]:
    seen: dict[str, PlanStep] = {}
    for op in ops:
        for step in index.get(op.id, []):
            seen.setdefault(step.id, step)
    return sorted(seen.values(), key=lambda step: step.order)


def _creation_steps(
    name: str,
    components: list[str],
    inputs: list[str],
    outputs: list[str],
    params: list[JobletParameter],
    pending: int,
) -> list[str]:
    present = [c for c in components if c and c != "por_determinar"]
    steps = [
        "Repository › Joblet Designs › clic derecho › Create Joblet.",
        f"Dale el nombre {name} y guárdalo en la carpeta por defecto del proyecto.",
        "Añade los componentes del bloque y conéctalos con Main: "
        + (", ".join(present) if present else "define primero el componente de cada paso")
        + ".",
    ]
    if pending:
        steps.append(f"Resuelve antes {pending} paso(s) sin componente decidido dentro del bloque.")
    if inputs:
        steps.append("Añade un componente Input por cada tabla de entrada: " + ", ".join(inputs) + ".")
    else:
        steps.append("Añade un componente Input si el bloque lee datos de fuera del joblet.")
    if outputs:
        steps.append("Añade un componente Output por cada tabla de salida: " + ", ".join(outputs) + ".")
    steps.append("Añade un componente Trigger Input para la señal de inicio del joblet.")
    if params:
        steps.append(
            "Define en Contexts del joblet las variables: "
            + ", ".join(p.context_variable for p in params)
            + ". Los valores concretos se asignan en cada Job al usar el joblet."
        )
    steps.append(
        f"Usa el joblet en el Job arrastrándolo desde Repository › Joblet Designs › {name} "
        "al lienzo, y conéctalo con el paso anterior y el siguiente."
    )
    steps.append("Guarda el joblet y comprueba que no quedan componentes sin conectar.")
    return steps


def _usage_steps(name: str, job: str, step_ids: list[str], values: dict[str, str]) -> list[str]:
    if step_ids:
        steps = [f"En {job}, sustituye los componentes {', '.join(step_ids)} por el joblet {name}."]
    else:
        steps = [f"En {job}, coloca el joblet {name} en el punto donde va el bloque."]
    steps.append(
        f"Arrástralo desde Repository › Joblet Designs al lienzo de {job} y conéctalo: "
        "Trigger Input con OnSubjobOk desde el paso anterior."
    )
    if values:
        steps.append(
            "Asigna en el contexto del Job: " + ", ".join(f"{k} = {v}" for k, v in values.items()) + "."
        )
    return steps


def _why(rep: Repetition, parameter_count: int, jobs: list[str]) -> str:
    count = len(rep.occurrences)
    where = ", ".join(dict.fromkeys(jobs))
    if parameter_count == 0:
        subject = f"macro %{rep.occurrences[0].macro}" if rep.kind == "macro" else "bloque"
        return (
            f"El {subject} aparece {count} veces con la misma estructura y los mismos valores "
            f"({rep.operation_count} operaciones; {where}). Un solo joblet evita mantener las copias."
        )
    if rep.kind == "macro":
        return (
            f"La macro %{rep.occurrences[0].macro} aparece {count} veces con la misma estructura de "
            f"{rep.operation_count} operaciones ({where}). Solo cambian {parameter_count} valor(es) "
            "entre apariciones; se propone un joblet con esos valores como parámetros."
        )
    return (
        f"El mismo bloque de {rep.operation_count} operaciones aparece {count} veces ({where}). "
        f"Solo cambian {parameter_count} valor(es) entre apariciones (tablas o literales); se "
        "propone un joblet con esos valores como parámetros."
    )


def _joblet(
    number: int,
    rep: Repetition,
    plan: JobPlan,
    index: dict[str, list[PlanStep]],
    used_names: set[str],
) -> JobletPlan | None:
    occurrence_steps = [_steps_of(occ.ops, index) for occ in rep.occurrences]
    if rep.kind == "feed":
        intermediate = [
            step
            for occ in rep.occurrences
            for op in occ.ops
            if op.type == "write" and op.outputs and all(_is_work(name) for name in op.outputs)
            for step in index.get(op.id, [])
        ]
        _bypass_work_writes(plan, intermediate)
        occurrence_steps = [[s for s in steps if s not in intermediate] for steps in occurrence_steps]
    # Copias sin ningún paso (plegadas en un joblet de región) no forman parte del bloque.
    keep = [k for k, steps in enumerate(occurrence_steps) if steps]
    if len(keep) < len(rep.occurrences):
        if len(keep) < 2:
            return None
        rep = replace(rep, occurrences=[rep.occurrences[k] for k in keep])
        occurrence_steps = [occurrence_steps[k] for k in keep]
    if not any(occurrence_steps):
        return None
    template = rep.occurrences[0].slots
    parameters, rows = _parameters(rep, template)
    dataset_names = _dataset_names(template)
    feed = rep.kind == "feed"
    inputs = [
        dataset_names[i] for i, slot in enumerate(template)
        if slot.kind == "in" and not (feed and _is_work(slot.value))
    ]
    outputs = [
        dataset_names[i] for i, slot in enumerate(template)
        if slot.kind == "out" and not (feed and _is_work(slot.value))
    ]
    joblet_id = f"joblet-{number:02d}"
    name = _unique(f"jl_{_role(rep)}", used_names)
    components = [step.component_candidate for step in occurrence_steps[0]]
    pending = sum(1 for step in occurrence_steps[0] if step.action == "manual_decision")
    occurrences: list[JobletOccurrence] = []
    jobs: list[str] = []
    for k, (occ, steps) in enumerate(zip(rep.occurrences, occurrence_steps, strict=True)):
        default_job = occ.macro or plan.job_name
        job = (steps[0].job_part or default_job) if steps else default_job
        jobs.append(job)
        step_ids = [step.id for step in steps]
        values = {param.name: row[k] for param, row in zip(parameters, rows, strict=True)}
        occurrences.append(
            JobletOccurrence(
                job=job,
                label=occ.label,
                step_ids=step_ids,
                values=values,
                usage_steps=_usage_steps(name, job, step_ids, values),
            )
        )
        for step in steps:
            step.joblet_id = joblet_id
    role = _role(rep)
    readable = (
        f"Macro %{rep.occurrences[0].macro}" if rep.kind == "macro" else ROLE_TEXT.get(role, role)
    )
    return JobletPlan(
        id=joblet_id,
        name=name,
        title=f"{readable} ({len(rep.occurrences)} apariciones)",
        kind=rep.kind,
        occurrences=occurrences,
        parameters=parameters,
        components=components,
        inputs=inputs,
        outputs=outputs,
        trigger_inputs=["inicio"],
        why=_why(rep, len(parameters), jobs),
        creation_steps=_creation_steps(name, components, inputs, outputs, parameters, pending),
        operation_count=rep.operation_count,
    )


def attach_joblets(plan: JobPlan, ir: ProgramIR) -> None:
    """Calcula los joblets del programa y marca `joblet_id` en los pasos que los forman."""
    index: dict[str, list[PlanStep]] = {}
    for step in plan.steps + [s for child in plan.children for s in child.steps]:
        if step.joblet_id:  # ya es parte de un joblet propuesto (p. ej. la carga a Impala)
            continue
        for operation_id in step.fused_from or ([step.operation_id] if step.operation_id else []):
            index.setdefault(operation_id, []).append(step)
    used_names: set[str] = {joblet.name for joblet in plan.joblets}
    # Los joblets ya propuestos (p. ej. la carga a Impala) conservan su número y nombre.
    joblets: list[JobletPlan] = list(plan.joblets)
    for rep in find_repetitions(ir.macros, ir.operations):
        joblet = _joblet(len(joblets) + 1, rep, plan, index, used_names)
        if joblet is not None:
            joblets.append(joblet)
    plan.joblets = joblets


def macro_call_joblets(plan: JobPlan, ir: ProgramIR, arguments_of) -> None:
    """Una macro de datos llamada dos o más veces desde el programa es UN joblet con una ocurrencia por
    llamada (no un Job hijo por macro). Sus argumentos que cambian entre llamadas son los parámetros.

    `arguments_of(op)` devuelve {parámetro: valor} de una llamada. Una macro llamada una sola vez se
    expande en línea (no entra aquí).
    """
    calls_by_name: dict[str, list] = {}
    for op in ir.operations:
        if op.type == "macro_call":
            calls_by_name.setdefault(str(op.details.get("name", "")).casefold(), []).append(op)
    definitions: dict[str, list] = {}
    for macro in ir.macros:
        definitions.setdefault(re.sub(r"_v\d+$", "", macro.name.casefold()), []).append(macro)
    for child in list(plan.children):
        calls = calls_by_name.get(child.name.casefold(), [])
        if len(calls) < 2:
            continue
        family = definitions.get(re.sub(r"_v\d+$", "", child.name.casefold()), [])
        if len(family) > 1 or any(m.copies > 1 for m in family):
            continue  # copias o variantes de una definición: lo agrupa la repetición de macros (attach_joblets)
        call_steps = [s for call in calls for s in plan.steps if s.operation_id == call.id]
        if len(call_steps) != len(calls) or not child.steps:
            continue
        joblet_id = f"joblet-{len(plan.joblets) + 1:02d}"
        used = {joblet.name for joblet in plan.joblets}
        name = _unique(f"jl_{_camel(child.name)}", used)
        values_rows = [{k: v for k, v in arguments_of(call).items()} for call in calls]
        varying = [
            p for p in child.params
            if len({row.get(p, "") for row in values_rows}) > 1
        ]
        parameters = [
            JobletParameter(
                name=p,
                context_variable=f"context.{p}",
                example_values=list(dict.fromkeys(row.get(p, "") for row in values_rows))[:MAX_EXAMPLES],
            )
            for p in varying
        ]
        for step in child.steps:
            step.joblet_id = joblet_id
        body = list(child.steps)
        first = min(plan.steps.index(s) for s in call_steps)
        plan.steps = [s for s in plan.steps if s not in call_steps]
        plan.steps[first:first] = body
        plan.children = [c for c in plan.children if c is not child]
        occurrences: list[JobletOccurrence] = []
        for call, step, values in zip(calls, call_steps, values_rows, strict=True):
            step.component_candidate = "por_determinar"
            step.alternatives = ["Joblet"]
            step.joblet_id = joblet_id
            step.purpose = f"Usa el joblet {name} con los valores de la llamada %{child.name}."
            step.why = (
                f"Llamada %{child.name} (línea {call.evidence.line}): la macro se repite con otros valores; "
                "el joblet evita copiar el bloque por llamada."
            )
            occurrences.append(
                JobletOccurrence(
                    job=step.job_part or plan.job_name,
                    label=f"macro %{child.name} (línea {call.evidence.line})",
                    step_ids=[step.id],
                    values={p: values.get(p, "") for p in varying},
                    usage_steps=_usage_steps(name, plan.job_name, [step.id], {p: values.get(p, "") for p in varying}),
                )
            )
        components = [s.component_candidate for s in body]
        pending = sum(1 for s in body if s.action == "manual_decision")
        plan.joblets.append(
            JobletPlan(
                id=joblet_id,
                name=name,
                title=f"Macro %{child.name} ({len(calls)} llamadas)",
                kind="macro",
                occurrences=occurrences,
                parameters=parameters,
                components=components,
                inputs=[],
                outputs=[],
                trigger_inputs=["inicio"],
                why=(
                    f"La macro %{child.name} se llama {len(calls)} veces; "
                    + (
                        f"solo cambian {len(parameters)} valor(es) entre llamadas."
                        if parameters
                        else "con los mismos valores."
                    )
                    + " Un solo joblet evita mantener una copia por llamada."
                ),
                creation_steps=_creation_steps(name, components, [], [], parameters, pending),
                operation_count=len(body),
            )
        )
