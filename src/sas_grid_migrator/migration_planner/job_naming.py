"""Naming rules for generated and user-edited Talend Jobs."""

from __future__ import annotations

import re
from collections.abc import Collection, Sequence
from pathlib import PurePosixPath
from typing import Literal

from pydantic import BaseModel

from .models import JobPlan
from .planner import slug

DEFAULT_NAME_TEMPLATE = "job_{programa}"
TEMPLATE_TOKENS = ("proyecto", "carpeta", "programa")
MAX_JOB_NAME = 60


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
    error: str | None = None


def validate_job_name(name: str, *, taken: Collection[str]) -> str | None:
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        return "El nombre debe empezar con una letra o guion bajo y usar solo letras, números y guion bajo."
    if len(name) > MAX_JOB_NAME:
        return "El nombre no puede pasar de 60 caracteres."
    if name.casefold() in {item.casefold() for item in taken}:
        return "Ya existe otro Job con ese nombre."
    return None


def validate_template(template: str) -> str | None:
    tokens = re.findall(r"\{([^{}]+)\}", template)
    for token in tokens:
        if token not in TEMPLATE_TOKENS:
            return f"Token desconocido: {{{token}}}."
    if "{programa}" not in template:
        return "La plantilla debe incluir {programa}."
    return None


def render_job_name(template: str, *, project: str, program: str, depth: int = 0) -> str:
    parts = PurePosixPath(program.replace("\\", "/")).parts
    stem = PurePosixPath(parts[-1]).stem if parts else ""
    prefix = parts[max(0, len(parts) - depth - 1):-1] if depth else []
    program_name = slug("_".join([*prefix, stem]))
    folder = slug(parts[-2]) if len(parts) > 1 else ""
    rendered = template.replace("{proyecto}", slug(project))
    rendered = rendered.replace("{carpeta}", folder).replace("{programa}", program_name)
    rendered = re.sub(r"[^A-Za-z0-9_]+", "_", rendered)
    rendered = re.sub(r"_+", "_", rendered).strip("_")
    if not rendered or rendered[0].isdigit():
        rendered = f"job_{rendered}"
    return rendered


def bulk_preview(plans: Sequence[JobPlan], rule: BulkRule) -> list[RenamePreview]:
    selected = set(rule.programs) if rule.programs is not None else None
    targets = [plan for plan in plans if selected is None or plan.program in selected]
    if selected is not None and selected.difference(plan.program for plan in targets):
        raise ValueError("Uno o más programas solicitados no existen en el plan.")
    if rule.mode == "regex":
        if len(rule.find) > 200 or re.search(r"\([^)]*[+*][^)]*\)[+*{]", rule.find):
            raise ValueError("El patrón es demasiado complejo.")
        try:
            pattern = re.compile(rule.find)
        except re.error as exc:
            raise ValueError("El patrón regex no es válido.") from exc

    rows: list[RenamePreview] = []
    for plan in targets:
        if rule.mode == "prefix":
            proposed = rule.text + plan.job_name
        elif rule.mode == "suffix":
            proposed = plan.job_name + rule.text
        elif rule.mode == "replace":
            proposed = plan.job_name.replace(rule.find, rule.replace_with)
        else:
            proposed = pattern.sub(rule.replace_with, plan.job_name)
        rows.append(RenamePreview(program=plan.program, current=plan.job_name, proposed=proposed))

    target_programs = {plan.program for plan in targets}
    fixed_names = [plan.job_name for plan in plans if plan.program not in target_programs]
    proposals = [row.proposed.casefold() for row in rows if row.proposed != row.current]
    for row in rows:
        if row.proposed == row.current:
            continue
        error = validate_job_name(row.proposed, taken=fixed_names)
        if error is None and proposals.count(row.proposed.casefold()) > 1:
            error = "Ya existe otro Job con ese nombre."
        row.error = error
    return rows
