"""Modelo de ejecución (SAS Grid): qué se lanza, en qué orden, con qué parámetros.

Separado del modelo de procesamiento de datos: una espera entre trabajos es una dependencia de
orquestación, nunca una conexión de filas entre componentes. Las dependencias se marcan
`inferred` cuando salen de la secuencia del script y no de una declaración explícita.
"""

import re
import shlex
from collections.abc import Callable
from itertools import pairwise

from pydantic import BaseModel

from sas_grid_migrator.macro_resolver.resolver import (
    PathIndex,
    PathMatch,
    first_quoted,
    resolve_path,
    walk,
)
from sas_grid_migrator.sas_parser.ast import GlobalStmt, MacroDef, ParsedProgram
from sas_grid_migrator.sas_parser.parser import split_args


class GridTask(BaseModel):
    id: str
    kind: str  # sasgsub | sas_batch | sas_macro_step
    source_file: str
    line: int
    program: str | None = None  # ruta tal como aparece
    resolved_program: str | None = None
    match_status: str | None = None
    job_name: str | None = None
    queue: str | None = None
    waits: bool = False
    params: dict[str, str] = {}
    condition: str | None = None
    after: list[str] = []  # ids de tareas de las que depende
    inferred: bool = True
    notes: list[str] = []


class Schedule(BaseModel):
    file: str
    text: str


class Orchestration(BaseModel):
    tasks: list[GridTask] = []
    schedules: list[Schedule] = []
    order: list[str] = []


_SCHEDULE = re.compile(r"(?:Schedule|Schedule[d]?\s+by|Planificaci[oó]n)\s*:\s*(.+)", re.IGNORECASE)
_PROGRAM = re.compile(r"\.sas$", re.IGNORECASE)


def _logical_lines(text: str) -> list[tuple[int, str]]:
    out, buf, start = [], "", 0
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.split("#", 1)[0] if not re.search(r"""['"].*#.*['"]""", raw) else raw
        if not buf:
            start = i
        if line.rstrip().endswith("\\"):
            buf += line.rstrip()[:-1] + " "
            continue
        buf += line
        if buf.strip():
            out.append((start, buf.strip()))
        buf = ""
    return out


def _tokens(s: str) -> list[str]:
    try:
        return shlex.split(s)
    except ValueError:
        return s.split()


def shell_tasks(file: str, text: str, files: "list[str] | PathIndex") -> list[GridTask]:
    tasks: list[GridTask] = []
    env: dict[str, str] = {}
    for line, stmt in _logical_lines(text):
        em = re.match(r"(?:export\s+)?([A-Za-z_]\w*)=(.*)$", stmt)
        if em and not re.search(r"\bsas(gsub)?\b", em.group(2)):
            env[em.group(1)] = em.group(2).strip("'\"")
            continue
        m = re.search(r"\b(sasgsub|sas)\b(?=\s)", stmt)
        if not m or not re.search(r"\.sas\b", stmt, re.IGNORECASE):
            continue
        prefix = stmt[: m.start()].strip()
        if prefix.endswith("$(") and stmt.endswith(")"):
            stmt = stmt[:-1]  # JOB=$(sasgsub ...): quitar el cierre de la sustitución
        cond = None
        if prefix and re.search(r"&&|\|\||\bif\b|\bthen\b|\[", prefix):
            cond = prefix.rstrip("&| ").strip()
            cond = "previous_success" if re.search(r'"\$\?"\s*-eq\s*0', cond) else cond
        toks = _tokens(stmt[m.start() :])
        opts: dict[str, str] = {}
        prog = None
        params = dict(env)
        i = 1
        while i < len(toks):
            t = toks[i]
            low = t.lower()
            if low in ("-gridsubmitpgm", "-sysin") and i + 1 < len(toks):
                prog = toks[i + 1]
                i += 1
            elif low in ("-gridjobname", "-gridqueue", "-sysparm") and i + 1 < len(toks):
                opts[low] = toks[i + 1]
                i += 1
            elif low == "-set" and i + 2 < len(toks):
                params[toks[i + 1]] = toks[i + 2]
                i += 2
            elif low == "-gridsasoptions" and i + 1 < len(toks):
                for k, v in re.findall(r"-set\s+(\S+)\s+(\S+)", toks[i + 1]):
                    params[k] = v
                i += 1
            elif low == "-gridwaitresults":
                opts[low] = "1"
            elif _PROGRAM.search(t) and prog is None:
                prog = t
            i += 1
        if "-sysparm" in opts:
            params["sysparm"] = opts["-sysparm"]
        kind = m.group(1) if m.group(1) == "sasgsub" else "sas_batch"
        match = resolve_path(prog, files) if prog and "$" not in prog else PathMatch("external")
        tasks.append(
            GridTask(
                id=f"{file}#{len(tasks) + 1}",
                kind=kind,
                source_file=file,
                line=line,
                program=prog,
                resolved_program=match.file if match.status == "resolved" else None,
                match_status=match.status if prog and "$" not in prog else "dynamic",
                job_name=opts.get("-gridjobname"),
                queue=opts.get("-gridqueue"),
                waits=kind == "sas_batch" or "-gridwaitresults" in opts,
                params=params,
                condition=cond,
            )
        )
    for prev, cur in pairwise(tasks):
        if prev.waits or cur.condition:
            cur.after = [prev.id]
    return tasks


def orchestrator_macros(programs: list[ParsedProgram]) -> dict[str, tuple[MacroDef, int, str]]:
    """Macros cuyo cuerpo hace `%include "&param"`: nombre → (macro, índice del parámetro, archivo)."""
    out = {}
    for p in programs:
        for n in walk(p.nodes):
            if not isinstance(n, MacroDef):
                continue
            names = [x.name.lower() for x in n.params]
            for g in walk(n.body):
                if isinstance(g, GlobalStmt) and g.kind == "include":
                    for v in re.findall(r"&(\w+)", g.fields.get("path", "")):
                        if v.lower() in names:
                            out[n.name.lower()] = (n, names.index(v.lower()), p.file)
    return out


def macro_step_tasks(
    programs: list[ParsedProgram], files: "list[str] | PathIndex"
) -> list[GridTask]:
    orch = orchestrator_macros(programs)
    tasks: list[GridTask] = []
    for p in programs:
        group: list[GridTask] = []
        for g in walk(p.nodes):
            if not (isinstance(g, GlobalStmt) and g.kind == "macro_call"):
                continue
            name = g.fields["name"].lower()
            if name not in orch:
                continue
            macro, idx, _ = orch[name]
            args = split_args(g.fields["args"])
            pos = [a for a in args if "=" not in a.split("(")[0]]
            kw = {
                a.split("=", 1)[0].strip().lower(): a.split("=", 1)[1].strip()
                for a in args
                if "=" in a
            }
            pname = macro.params[idx].name.lower()
            prog = kw.get(pname) or (pos[idx] if idx < len(pos) else None)
            if not prog:
                continue
            prog = first_quoted(prog) or prog.strip()
            params = {
                macro.params[i].name: pos[i].strip()
                for i in range(min(len(pos), len(macro.params)))
            }
            params.update({k: v for k, v in kw.items()})
            match = resolve_path(prog, files) if "&" not in prog else PathMatch("external")
            t = GridTask(
                id=f"{p.file}#{len(group) + 1}",
                kind="sas_macro_step",
                source_file=p.file,
                line=g.loc.line,
                program=prog,
                resolved_program=match.file if match.status == "resolved" else None,
                match_status=match.status if "&" not in prog else "dynamic",
                waits=True,
                params=params,
                notes=[f"ejecutado mediante la macro %{macro.name}"],
            )
            if group:
                t.after = [group[-1].id]
            group.append(t)
        tasks += group
    return tasks


def analyze_grid(
    programs: list[ParsedProgram],
    shell_files: list[str],
    all_files: list[str],
    read: Callable[[str], str],
) -> Orchestration:
    tasks: list[GridTask] = []
    index = PathIndex(all_files)
    for f in shell_files:
        tasks += shell_tasks(f, read(f), index)
    tasks += macro_step_tasks(programs, index)
    schedules = []
    for f in [p.file for p in programs] + shell_files:
        m = _SCHEDULE.search(read(f)[:3000])
        if m:
            schedules.append(Schedule(file=f, text=m.group(1).strip()))
    order = _topological(tasks)
    return Orchestration(tasks=tasks, schedules=schedules, order=order)


def _topological(tasks: list[GridTask]) -> list[str]:
    ids = [t.id for t in tasks]
    seen: set[str] = set()
    out: list[str] = []
    by_id = {t.id: t for t in tasks}

    def visit(i: str) -> None:
        if i in seen:
            return
        seen.add(i)
        for a in by_id[i].after:
            visit(a)
        out.append(i)

    for i in ids:
        visit(i)
    return out
