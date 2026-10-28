"""Grafo de procesamiento: programas, macros y datasets (NetworkX) + orquestación Grid."""

import json
from collections import defaultdict
from collections.abc import Callable

import networkx as nx
from pydantic import BaseModel

from sas_grid_migrator.domain.models import SCHEMA_VERSION, FileKind
from sas_grid_migrator.domain.redaction import redact
from sas_grid_migrator.grid_analysis.analyzer import Orchestration, analyze_grid
from sas_grid_migrator.macro_resolver.resolver import (
    PathIndex,
    constant_vars,
    first_quoted,
    macro_index,
    resolve_path,
    substitute,
    walk,
)
from sas_grid_migrator.persistence.artifacts import write_text_atomic
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import Analysis, analyze_project, load_analysis
from sas_grid_migrator.sas_parser.ast import (
    DatasetRef,
    DataStep,
    GlobalStmt,
    MacroDef,
    Node,
    ProcStep,
)


class Library(BaseModel):
    name: str
    engine: str | None = None
    path: str | None = None
    defined_in: list[str] = []


class IncludeRef(BaseModel):
    raw: str
    line: int
    status: str  # resolved | candidate | ambiguous | external | dynamic
    file: str | None = None  # destino resuelto
    candidate: str | None = None


class ProgramDeps(BaseModel):
    file: str
    includes: list[IncludeRef] = []
    macros_defined: list[str] = []
    macros_called: list[str] = []
    reads: list[str] = []  # efectivo: propio + macros + includes
    writes: list[str] = []


class DatasetInfo(BaseModel):
    id: str  # lib.nombre en minúsculas; sin lib → work
    role: str  # source | intermediate | final | temporary
    library: str | None = None
    producers: list[str] = []
    consumers: list[str] = []


class DataEdge(BaseModel):
    source: str
    target: str
    datasets: list[str]
    kind: str = "data"  # data | include


class Unresolved(BaseModel):
    kind: str  # macro | include | dataset_dynamic
    name: str
    file: str
    line: int
    detail: str = ""


class DependencyReport(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    libraries: list[Library] = []
    programs: list[ProgramDeps] = []
    datasets: list[DatasetInfo] = []
    edges: list[DataEdge] = []
    processing_order: list[list[str]] = []  # capas; los de una capa son independientes
    cycles: list[list[str]] = []
    unresolved: list[Unresolved] = []
    orchestration: Orchestration = Orchestration()


# ---------- extracción por unidad (programa o macro) ----------


def _own_nodes(nodes: list[Node]):
    """Nodos de un nivel sin entrar en macros (cada macro es su propia unidad)."""
    for n in nodes:
        if not isinstance(n, MacroDef):
            yield n


def _dataset_id(ref: DatasetRef, variables: dict[str, str]) -> tuple[str | None, str]:
    """(id normalizado | None si dinámico no resoluble, texto crudo)."""
    raw = ref.raw
    if ref.dynamic:
        raw, ok = substitute(raw, variables)
        if not ok:
            return None, ref.raw
    lib, _, name = raw.rpartition(".")
    return f"{(lib or 'work').lower()}.{name.lower()}", ref.raw


def _io(nodes: list[Node]):
    """Genera (modo, DatasetRef|ruta, línea) de lectura/escritura en los nodos dados."""
    for n in nodes:
        if isinstance(n, DataStep):
            for r in n.inputs:
                yield "r", r, n.loc.line
            for r in n.outputs:
                yield "w", r, n.loc.line
        elif isinstance(n, ProcStep):
            for r in n.inputs:
                yield "r", r, n.loc.line
            for r in n.outputs:
                yield "w", r, n.loc.line
            if "datafile" in n.fields:
                yield (
                    ("r" if n.name == "import" else "w"),
                    "file:" + n.fields["datafile"],
                    n.loc.line,
                )
            if "outfile" in n.fields:
                yield "w", "file:" + n.fields["outfile"], n.loc.line


class _Unit:
    def __init__(self, key: str):
        self.key = key
        self.reads: set[str] = set()
        self.writes: set[str] = set()
        self.macros: set[str] = set()
        self.includes: list[str] = []  # archivos incluidos resueltos


def build_report(
    analysis: Analysis,
    all_files: list[str],
    shell_files: list[str],
    read: Callable[[str], str],
) -> DependencyReport:
    programs = analysis.programs
    path_index = PathIndex(all_files)
    variables = constant_vars(programs)
    index = macro_index(programs)
    unresolved: list[Unresolved] = []
    seen_unres: set[tuple] = set()

    def unres(kind: str, name: str, file: str, line: int, detail: str = "") -> None:
        k = (kind, name, file, line)
        if k not in seen_unres:
            seen_unres.add(k)
            unresolved.append(Unresolved(kind=kind, name=name, file=file, line=line, detail=detail))

    # librerías
    libs: dict[str, Library] = {}
    for p in programs:
        for n in walk(p.nodes):
            if isinstance(n, GlobalStmt) and n.kind == "libname" and n.fields.get("action") is None:
                lib = libs.setdefault(n.fields["name"].lower(), Library(name=n.fields["name"]))
                lib.engine = lib.engine or n.fields.get("engine")
                lib.path = lib.path or n.fields.get("path")
                if p.file not in lib.defined_in:
                    lib.defined_in.append(p.file)

    # unidades: cada programa (nivel superior) y cada macro
    units: dict[str, _Unit] = {}
    prog_info: dict[str, ProgramDeps] = {}
    macro_unit: dict[str, list[str]] = defaultdict(list)  # nombre → claves de unidad

    def fill(unit: _Unit, nodes: list[Node], file: str) -> None:
        for mode, ref, line in _io(nodes):
            if isinstance(ref, str):
                (unit.reads if mode == "r" else unit.writes).add(ref)
                continue
            ds, raw = _dataset_id(ref, variables)
            if ds is None:
                unres("dataset_dynamic", raw, file, line, "nombre de dataset con macrovariables")
                continue
            (unit.reads if mode == "r" else unit.writes).add(ds)

    for p in programs:
        u = _Unit(f"prog:{p.file}")
        units[u.key] = u
        deps = ProgramDeps(file=p.file)
        prog_info[p.file] = deps
        own = list(_own_nodes(p.nodes))
        fill(u, own, p.file)
        for g in own:
            if isinstance(g, GlobalStmt) and g.kind == "include":
                raw = first_quoted(g.fields.get("path", ""))
                if raw is None or "&" in raw or "%" in raw:
                    sub, ok = (
                        substitute(raw or g.fields.get("path", ""), variables)
                        if raw
                        else ("", False)
                    )
                    raw = sub if ok and "%" not in sub else None
                if raw is None:
                    deps.includes.append(
                        IncludeRef(raw=g.fields.get("path", ""), line=g.loc.line, status="dynamic")
                    )
                    unres("include", g.fields.get("path", ""), p.file, g.loc.line, "ruta dinámica")
                    continue
                m = resolve_path(raw, path_index)
                ref = IncludeRef(
                    raw=raw,
                    line=g.loc.line,
                    status=m.status,
                    file=m.file if m.status == "resolved" else None,
                    candidate=m.file if m.status == "candidate" else None,
                )
                deps.includes.append(ref)
                if m.status == "resolved":
                    u.includes.append(m.file)
                else:
                    unres(
                        "include",
                        raw,
                        p.file,
                        g.loc.line,
                        m.status + (f" → {m.file}" if m.file else ""),
                    )
        for n in walk(p.nodes):
            if isinstance(n, MacroDef):
                mu = _Unit(f"macro:{n.name.lower()}@{p.file}")
                units[mu.key] = mu
                fill(mu, [x for x in walk(n.body) if not isinstance(x, MacroDef)], p.file)
                mu.macros |= set(n.calls)
                macro_unit[n.name.lower()].append(mu.key)
                deps.macros_defined.append(n.name)
        u.macros = {c.name for c in p.macro_calls}
        deps.macros_called = sorted(u.macros)
        for c in p.macro_calls:
            if c.name not in index:
                unres("macro", c.name, p.file, c.line, "sin definición en el proyecto")

    # cierre transitivo: programa → macros e includes
    memo: dict[str, tuple[set[str], set[str]]] = {}

    def effective(key: str, stack: tuple[str, ...] = ()) -> tuple[set[str], set[str]]:
        if key in memo:
            return memo[key]
        if key in stack:
            return set(), set()
        u = units[key]
        r, w = set(u.reads), set(u.writes)
        children = [k for m in u.macros for k in macro_unit.get(m, [])]
        children += [f"prog:{f}" for f in u.includes]
        for c in children:
            cr, cw = effective(c, (*stack, key))
            r |= cr
            w |= cw
        memo[key] = (r, w)
        return r, w

    for f, deps in prog_info.items():
        r, w = effective(f"prog:{f}")
        deps.reads, deps.writes = sorted(r), sorted(w)

    # datasets y aristas
    producers: dict[str, set[str]] = defaultdict(set)
    consumers: dict[str, set[str]] = defaultdict(set)
    for f, d in prog_info.items():
        for x in d.writes:
            producers[x].add(f)
        for x in d.reads:
            consumers[x].add(f)
    datasets = []
    for ds in sorted(set(producers) | set(consumers)):
        lib = ds.split(".", 1)[0] if not ds.startswith("file:") else None
        if lib == "work":
            role = "temporary"
        elif not producers[ds]:
            role = "source"
        elif consumers[ds] - producers[ds]:
            role = "intermediate"
        else:
            role = "final"
        datasets.append(
            DatasetInfo(
                id=ds,
                role=role,
                library=lib,
                producers=sorted(producers[ds]),
                consumers=sorted(consumers[ds]),
            )
        )

    g = nx.DiGraph()
    g.add_nodes_from(prog_info)
    edges: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for ds in datasets:
        if ds.role == "temporary":
            continue
        for a in ds.producers:
            for b in ds.consumers:
                if a != b:
                    edges[(a, b, "data")].add(ds.id)
    for f, d in prog_info.items():
        for inc in d.includes:
            if inc.file and inc.file != f:
                edges[(inc.file, f, "include")].add(inc.file)
    for a, b, _ in edges:
        g.add_edge(a, b)
    cond = nx.condensation(g)
    cycles = [sorted(c) for c in (cond.nodes[n]["members"] for n in cond) if len(c) > 1]
    layers = [
        sorted(m for n in layer for m in cond.nodes[n]["members"])
        for layer in nx.topological_generations(cond)
    ]
    orchestration = analyze_grid(programs, shell_files, all_files, read)
    return DependencyReport(
        project_id=analysis.project_id,
        libraries=sorted(libs.values(), key=lambda x: x.name.lower()),
        programs=sorted(prog_info.values(), key=lambda x: x.file),
        datasets=datasets,
        edges=[
            DataEdge(source=a, target=b, kind=k, datasets=sorted(s))
            for (a, b, k), s in sorted(edges.items())
        ],
        processing_order=layers,
        cycles=cycles,
        unresolved=unresolved,
        orchestration=orchestration,
    )


def build_dependencies(store: Store, project_id: str) -> DependencyReport:
    analysis = load_analysis(store, project_id) or analyze_project(store, project_id)
    manifest = store.get_manifest(project_id)
    root = store.source_dir(project_id)
    all_files = [f.path for f in manifest.files]
    shell = [f.path for f in manifest.files if f.kind == FileKind.SHELL]
    enc = {f.path: f.encoding or "utf-8" for f in manifest.files}

    def read(path: str) -> str:
        text = (root / path).read_bytes().decode(enc.get(path, "utf-8"), errors="replace")
        return redact(text, path)

    report = build_report(analysis, all_files, shell, read)
    write_text_atomic(store.dependencies_path(project_id), report.model_dump_json())
    return report


def load_dependencies(store: Store, project_id: str) -> DependencyReport | None:
    p = store.dependencies_path(project_id)
    return DependencyReport.model_validate(json.loads(p.read_text(encoding="utf-8"))) if p.exists() else None
