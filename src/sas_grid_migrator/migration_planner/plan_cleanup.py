"""Limpieza del plan: llamadas a macros sin definición y variables de contexto que sobran.

- Una llamada a macro que el proyecto no define deja un único `manual_decision` por nombre (no un paso
  por llamada): no se sabe qué hace sin su código.
- La poda quita del contexto los restos de plantilla de SAS Studio sin uso, por forma (`$nombre`,
  `%str(...)`, vacío) y deja el resto de variables aunque no se usen.
"""

from __future__ import annotations

import re

from sas_grid_migrator.intermediate_representation.models import ProgramIR
from sas_grid_migrator.migration_planner.models import (
    ContextVariable,
    JobPlan,
    NotMigrated,
    PlanStep,
)


def collapse_undefined_macros(plan: JobPlan, ir: ProgramIR) -> None:
    """Llamadas a macros sin definición en el programa: un único `manual_decision` por nombre."""
    defined = {macro.name.casefold() for macro in ir.macros}
    called = {
        op.id: str(op.details.get("name", "")).casefold()
        for op in ir.operations
        if op.type == "macro_call"
    }
    seen: set[str] = set()
    kept: list[PlanStep] = []
    for step in plan.steps:
        name = called.get(step.operation_id or "")
        if name is None or name in defined or step.joblet_id:
            kept.append(step)
            continue
        if name in seen:
            continue
        seen.add(name)
        step.action = "manual_decision"
        step.component_candidate = "por_determinar"
        step.confidence = "low"
        step.purpose = f"Falta el archivo que define %{name}: confirmar qué hace antes de migrarla."
        step.why = (
            f"%{name} se llama en el programa pero su definición no está en el proyecto; "
            "no se puede traducir sin ver su código."
        )
        kept.append(step)
    plan.steps = kept


def prune_unused_context(plan: JobPlan) -> None:
    """Quita del contexto las variables que ningún paso, propiedad, expresión ni joblet usa.

    Un nombre cuenta como usado si aparece como palabra en los textos del plan (`context.x`, `&x` o el
    nombre suelto). Se conservan las credenciales (id_Password) y las variables de grupo de ambiente.
    Las propiedades de pasos `manual_decision` (argumentos de macros sin definición) no cuentan: no se
    traducen. Las no usadas van en UNA sola entrada de `not_migrated`.
    """
    texts: list[str] = []
    steps = [*plan.steps, *(step for child in plan.children for step in child.steps)]
    for step in steps:
        texts += [step.purpose, step.why or "", step.note or "", *step.pending, *step.assumptions]
        if step.action != "manual_decision":
            for prop in step.properties:
                texts += [prop.name, prop.value or ""]
        for expression in step.expressions:
            texts += [expression.sas, expression.talend or "", expression.target or ""]
    for joblet in plan.joblets:
        texts += [joblet.title, joblet.why, *joblet.creation_steps]
        texts += [parameter.context_variable for parameter in joblet.parameters]
        for occurrence in joblet.occurrences:
            texts += [*occurrence.usage_steps, *occurrence.values.values()]
    for child in plan.children:
        texts += child.params
    if plan.entry_macro:
        # Los parámetros de la macro principal son la interfaz del Job: siempre son contexto.
        texts += [*plan.entry_macro.params, *plan.entry_macro.arguments.values()]
    haystack = "\n".join(texts)

    def used(name: str) -> bool:
        return re.search(rf"(?<!\w){re.escape(name)}(?!\w)", haystack, re.IGNORECASE) is not None

    kept: list[ContextVariable] = []
    dropped: list[str] = []
    for variable in plan.context_variables:
        # Sin uso en el plan se descarta (la fontanería ya está fuera); las credenciales y las variables de
        # ambiente se conservan siempre.
        if (
            variable.is_secret
            or variable.group_values is not None
            or used(variable.name)
        ):
            kept.append(variable)
        else:
            dropped.append(variable.name)
    plan.context_variables = kept
    if dropped:
        plan.not_migrated.append(
            NotMigrated(
                category="variables_sin_uso",
                lines=[],
                what="variables sin uso en el plan",
                reason="Sin uso en el plan (no alimentan ningún paso ni propiedad, porque la fontanería no se migra): "
                + ", ".join(dropped) + ".",
                talend_equivalent="No se crean en el contexto del Job; si un paso las necesita, se añaden entonces.",
            )
        )
