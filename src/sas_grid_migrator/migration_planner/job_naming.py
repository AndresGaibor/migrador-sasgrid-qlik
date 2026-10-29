"""Reglas de nombres de los Jobs de Talend: validación, plantilla y renombrado masivo.

Todo es determinista y no toca disco: los nombres se validan contra el resto del proyecto y las demás propuestas,
y el renombrado masivo solo devuelve una vista previa.
"""

import re
from collections.abc import Collection, Sequence
from pathlib import PurePosixPath
from typing import Literal

from pydantic import BaseModel

from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.migration_planner.planner import slug
from sas_grid_migrator.talend_adapter.naming import MAX_JOB_NAME

DEFAULT_NAME_TEMPLATE = "job_{programa}"
TEMPLATE_TOKENS = ("proyecto", "carpeta", "programa")

_IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_TOKEN = re.compile(r"\{([^{}]*)\}")
_NESTED_QUANTIFIERS = re.compile(r"\([^()]*[|+*{][^()]*\)[+*{]|\([^)]*\([^)]*\)[^)]*\)[+*{]")
_MAX_PATTERN = 200


class BulkRule(BaseModel):
    mode: Literal["prefix", "suffix", "replace", "regex"]
    text: str = ""
    find: str = ""
    replace_with: str = ""
    programs: list[str] | None = None


class RenamePreview(BaseModel):
    program: str
    current: str
    proposed: str
    error: str | None


def validate_job_name(name: str, *, taken: Collection[str]) -> str | None:
    """Mensaje de error si `name` no sirve como nombre de Job, o `None`."""
    if not _IDENTIFIER.fullmatch(name):
        return "El nombre debe empezar con una letra o guion bajo y usar solo letras, números y guion bajo."
    if len(name) > MAX_JOB_NAME:
        return f"El nombre no puede pasar de {MAX_JOB_NAME} caracteres."
    folded = name.casefold()
    if any(other.casefold() == folded for other in taken):
        return "Ya existe otro Job con ese nombre."
    return None


def validate_template(template: str) -> str | None:
    """Mensaje de error si la plantilla no es válida, o `None`."""
    for token in _TOKEN.findall(template):
        if token not in TEMPLATE_TOKENS:
            return f"Token desconocido: {{{token}}}."
    if "{programa}" not in template:
        return "La plantilla debe incluir {programa}."
    return None


def render_job_name(template: str, *, project: str, program: str, depth: int = 0) -> str:
    """Nombre de Job a partir de la plantilla; `{programa}` antepone `depth` carpetas como `_job_name_with_folders`."""
    parts = PurePosixPath(program.replace("\\", "/")).parts
    folders = parts[:-1]
    stem = PurePosixPath(parts[-1]).stem if parts else ""
    ancestors = folders[-depth:] if depth > 0 else ()
    values = {
        "proyecto": slug(project),
        "carpeta": slug(folders[-1]) if folders else "",
        "programa": slug("_".join([*ancestors, stem])),
    }
    rendered = _TOKEN.sub(lambda m: values.get(m.group(1), m.group(0)), template)
    name = re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9_]", "_", rendered)).strip("_")
    if not name or name[0].isdigit():
        name = f"job_{name}".strip("_")
    return name


def _proposal(current: str, rule: BulkRule, pattern: re.Pattern[str] | None) -> str:
    if rule.mode == "prefix":
        return rule.text + current
    if rule.mode == "suffix":
        return current + rule.text
    if rule.mode == "replace":
        return current.replace(rule.find, rule.replace_with) if rule.find else current
    assert pattern is not None
    try:
        return pattern.sub(rule.replace_with, current)
    except re.error as error:
        raise ValueError("El patrón de reemplazo no es válido.") from error


def bulk_preview(plans: Sequence[JobPlan], rule: BulkRule) -> list[RenamePreview]:
    """Vista previa del renombrado masivo de los Jobs pedidos (o todos), con errores de validación por fila."""
    pattern: re.Pattern[str] | None = None
    if rule.mode == "regex":
        if len(rule.find) > _MAX_PATTERN or _NESTED_QUANTIFIERS.search(rule.find):
            raise ValueError("El patrón es demasiado complejo.")
        try:
            pattern = re.compile(rule.find)
        except re.error as error:
            raise ValueError("El patrón no es una expresión regular válida.") from error

    selected = [i for i, plan in enumerate(plans) if rule.programs is None or plan.program in rule.programs]
    proposals = {i: _proposal(plans[i].job_name, rule, pattern) for i in selected}
    finals = [proposals.get(i, plan.job_name) for i, plan in enumerate(plans)]

    rows: list[RenamePreview] = []
    for i in selected:
        plan, proposed = plans[i], proposals[i]
        error = None
        if proposed != plan.job_name:
            others = [name for j, name in enumerate(finals) if j != i]
            error = validate_job_name(proposed, taken=others)
        rows.append(RenamePreview(program=plan.program, current=plan.job_name, proposed=proposed, error=error))
    return rows
