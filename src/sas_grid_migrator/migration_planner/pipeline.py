"""Etapa de fusión «a corriente»: convierte las operaciones SAS de un programa en pasos Talend encadenados.

Reglas (ver docs/pipeline-fusion.md):

1. Dataset intermedio: lo escribe un único grupo SAS (un DATA step o PROC) del programa y lo leen grupos
   posteriores, sin que otro programa o macro lo use. No genera escritura ni lectura: el flujo pasa
   directo al consumidor. Con 2+ consumidores se coloca un `tReplicate`.
2. Cadenas fila a fila (filter, compute, rename, select_columns, project) consecutivas se funden en un
   único `tMap` (`fusion.merge_tmap`). Una operación sola conserva su componente.
3. La fontanería de SAS (`plumbing.py`) no genera pasos: se registra en `not_migrated`.
4. Conexiones: Main desde la fuente de la cadena (Lookup para la segunda entrada de un join); dentro de
   una cadena, Main en serie; OnSubjobOk solo entre grupos sin datos en común.

`planner.plan_program` aporta el paso de cada operación (`_Planner.step`); aquí se decide qué pasos
existen y cómo se conectan.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from sas_grid_migrator.intermediate_representation.models import IROperation
from sas_grid_migrator.migration_planner.fusion import (
    FUSABLE,
    ChainState,
    fusable_expressions,
    merge_tmap,
)
from sas_grid_migrator.migration_planner.models import Connection, NotMigrated, PlanStep
from sas_grid_migrator.migration_planner.plumbing import Plumbing
from sas_grid_migrator.migration_planner.versions import (
    HASH_FAN_OUT,
    intermediate_datasets,
    merge_in_place_chains,
    split_groups,
    version_info,
)
from sas_grid_migrator.sas_parser.ast import Loc

#: Operaciones que leen un dataset o un archivo: son la fuente de su grupo.
SOURCES = frozenset({"read", "read_file", "inline_data"})
#: Operaciones que escriben un dataset o archivo: son el sumidero de su grupo.
WRITES = frozenset({"write", "write_file", "append"})

Item = tuple[IROperation, str]
Ref = tuple[str, str]  # ("step", id_de_paso) | ("ds", dataset_intermedio)


class StepMaker(Protocol):
    """Lo que la etapa pide al planificador: un paso por operación y el catálogo del tMap."""

    def step(self, op: IROperation, order: int, prefix: str) -> PlanStep: ...

    def tmap_meta(self) -> tuple[bool | None, str | None, list[str]]: ...


@dataclass
class Flow:
    steps: list[PlanStep] = field(default_factory=list)
    not_migrated: list[NotMigrated] = field(default_factory=list)
    #: Id del paso SAS que ya no existe como tal -> id del paso que lo absorbe (None: se descartó).
    retarget: dict[str, str | None] = field(default_factory=dict)


def _bare_keys(keys: list[str]) -> list[str]:
    return [key.split()[0].lower() if key.split() else key.lower() for key in keys]


def _drop_redundant_sorts(chain: list[Item], notes: dict[str, str]) -> list[Item]:
    """Un PROC SORT NODUPKEY seguido de su deduplicado con las mismas claves: tUniqRow basta."""
    out: list[Item] = []
    for index, (op, prefix) in enumerate(chain):
        nxt = chain[index + 1][0] if index + 1 < len(chain) else None
        if (
            op.type == "sort"
            and nxt is not None
            and nxt.type == "dedupe"
            and str(nxt.details.get("mode", "")).lower() == "nodupkey"
            and _bare_keys(list(op.details.get("keys", []))) == _bare_keys(list(nxt.details.get("keys", [])))
        ):
            notes[nxt.id] = (
                "PROC SORT NODUPKEY: tUniqRow conserva la primera fila de cada clave en el orden de entrada; "
                "SAS la conservaba en el orden ordenado. Validar si el resto de columnas difiere entre duplicados."
            )
            continue
        out.append((op, prefix))
    return out


def _segments(chain: list[Item], exprs_of) -> list[list[Item]]:
    """Parte la cadena: los fusionables consecutivos y compatibles van juntos; el resto, cada uno solo."""
    segments: list[list[Item]] = []
    current: list[Item] = []
    state = ChainState()
    for op, prefix in chain:
        if op.type in FUSABLE:
            if current and state.accepts(op, exprs_of(op, prefix)):
                current.append((op, prefix))
                state.add(op)
                continue
            if current:
                segments.append(current)
            current, state = [], ChainState()
            if state.accepts(op, exprs_of(op, prefix)):
                current = [(op, prefix)]
                state.add(op)
                continue
        elif current:
            segments.append(current)
            current, state = [], ChainState()
        segments.append([(op, prefix)])
    if current:
        segments.append(current)
    return segments


def _resolve(ref: Ref, tail_ref: dict[str, str]) -> str | None:
    kind, value = ref
    return value if kind == "step" else tail_ref.get(value)


def _record(flow: Flow, op: IROperation, plumbing: Plumbing) -> None:
    end = op.evidence.end_line or op.evidence.line
    lines = list(range(op.evidence.line, end + 1)) if end - op.evidence.line < 50 else [op.evidence.line, end]
    for entry in flow.not_migrated:
        if entry.category == plumbing.category and entry.what == plumbing.what:
            entry.lines = sorted({*entry.lines, *lines})
            return
    flow.not_migrated.append(
        NotMigrated(
            category=plumbing.category,
            lines=lines,
            what=plumbing.what,
            reason=plumbing.reason,
            talend_equivalent=plumbing.talend,
        )
    )


def _replicate(dataset: str, prefix: str, source: str, consumers: int, evidence: Loc) -> PlanStep:
    """Reparto de un intermedio a varios consumidores. Se usa un tMap con varias salidas FLOW, no tReplicate:
    el catálogo del MCP no declara salidas para el FLOW de tReplicate y el Studio rechaza esas conexiones
    (INVALID_CONNECTIONS). El tMap sí admite FLOW de salida múltiple."""
    slug = dataset.replace(".", "_").lower()
    return PlanStep(
        id=f"{prefix}tMap_reparto_{slug}",
        order=0,
        subjob=f"{prefix}replicate",
        action="add_component",
        operation_type="replicate",
        component_candidate="tMap",
        purpose=f"Reparte {dataset} a {consumers} consumidores (tMap con varias salidas)",
        evidence=evidence,
        connections=[Connection(type="Main", from_step=source)],
        why=f"Varios pasos leen {dataset}: un tMap con {consumers} salidas evita escribirlo y releerlo.",
    )


def _connect_first(step: PlanStep, op: IROperation, refs: list[str]) -> None:
    """Primer paso de un grupo: Main desde la fuente (join: Lookup para las demás entradas)."""
    if not refs:
        return
    if op.type == "join":
        step.connections = [Connection(type="Main", from_step=refs[0])] + [
            Connection(type="Lookup", from_step=s) for s in refs[1:]
        ]
    elif op.type == "union":
        step.connections = [Connection(type="Main", from_step=s) for s in refs]
    else:
        step.connections = [Connection(type="Main", from_step=refs[0])]


def _hash_out(dataset: str, prefix: str, source: str, readers: int, evidence: Loc) -> PlanStep:
    """Materialización única de una versión con muchos consumidores (tHashOutput, sumidero)."""
    slug = dataset.replace(".", "_").lower()
    return PlanStep(
        id=f"{prefix}tHashOutput_{slug}",
        order=0,
        subjob=f"{prefix}hash",
        action="add_component",
        operation_type="hash",
        component_candidate="tHashOutput",
        purpose=f"Materializa {dataset} en memoria (tHashOutput) para {readers} consumidores",
        evidence=evidence,
        connections=[Connection(type="Main", from_step=source)],
        why=f"{dataset} se reutiliza {readers} veces: se carga una vez en memoria.",
    )


def _hash_in(dataset: str, prefix: str, hash_id: str, readers: int, evidence: Loc, position: int) -> PlanStep:
    """Lectura de una versión materializada (tHashInput, origen). Se ejecuta tras el tHashOutput."""
    slug = dataset.replace(".", "_").lower()
    return PlanStep(
        id=f"{prefix}tHashInput_{slug}_{position}",
        order=0,
        subjob=f"{prefix}hash",
        action="add_component",
        operation_type="hash",
        component_candidate="tHashInput",
        purpose=f"Lee {dataset} desde memoria (tHashInput)",
        evidence=evidence,
        connections=[Connection(type="OnSubjobOk", from_step=hash_id)],
        why=f"se reutiliza {readers} veces: se carga una vez en memoria.",
    )


#: Componentes que admiten cualquier número de salidas o entradas por FLOW (no necesitan reparto).
_MULTI_FLOW = frozenset({"tmap", "tunite", "treplicate"})


def _fan_out_steps(out: list[PlanStep]) -> list[PlanStep]:
    """Reparte la salida de todo paso leído por varios consumidores, aunque estén en grupos distintos.

    El FLOW de un paso de lectura o de un componente de una sola salida (tFixedFlowInput, tSortRow...) admite
    una conexión; Studio rechaza las demás (INVALID_CONNECTIONS). Cuando una versión de dataset se decide sin
    versionar (p. ej. un dataset que un PROC SORT reescribe en el mismo grupo que lo lee), sus lectores
    llegan directamente a la fuente: aquí se intercala un tMap con varias salidas, igual que en `_replicate`.
    """
    readers: dict[str, int] = {}
    for step in out:
        for edge in step.connections:
            if edge.type in {"Main", "Lookup"} and edge.from_step:
                readers[edge.from_step] = readers.get(edge.from_step, 0) + 1
    by_id = {step.id: step for step in out}
    reparto: dict[str, PlanStep] = {}
    for source_id, count in readers.items():
        source = by_id.get(source_id)
        if count < 2 or source is None or source.component_candidate.casefold() in _MULTI_FLOW:
            continue
        reparto[source_id] = PlanStep(
            id=f"{source_id}_reparto",
            order=0,
            subjob=source.subjob,
            action="add_component",
            operation_type="replicate",
            component_candidate="tMap",
            purpose=f"Reparte la salida de {source.component_candidate} a {count} consumidores (tMap con varias salidas)",
            evidence=source.evidence,
            connections=[Connection(type="Main", from_step=source_id)],
            why=f"{source.component_candidate} admite una sola conexión de salida por FLOW; varios pasos leen esa salida.",
        )
    if not reparto:
        return out
    for step in out:
        for edge in step.connections:
            if edge.type in {"Main", "Lookup"} and edge.from_step in reparto:
                edge.from_step = reparto[edge.from_step].id
    result: list[PlanStep] = []
    for step in out:
        result.append(step)
        if step.id in reparto:
            result.append(reparto[step.id])
    return result


def build_flow(pl: StepMaker, items: list[Item], shared: set[str] | frozenset[str] = frozenset()) -> Flow:
    """Pasos, conexiones y fontanería de un programa (o de un cuerpo de macro) ya expandido."""
    flow = Flow()
    kept: list[Item] = []
    for op, prefix in items:
        if op.type == "infrastructure":
            _record(flow, op, Plumbing(**op.details["plumbing"]))
        else:
            kept.append((op, prefix))

    # Reescrituras en sitio encadenadas al grupo que produce la versión que reescriben (versions.py).
    kept = merge_in_place_chains(kept)
    groups = split_groups(kept)
    ops_by_group = [[op for op, _ in group] for group in groups]
    intermediates = intermediate_datasets(ops_by_group, shared)
    versions = version_info(ops_by_group, intermediates)
    cache: dict[str, PlanStep] = {}

    def probe(op: IROperation, prefix: str) -> PlanStep:
        key = f"{prefix}|{op.id}"
        if key not in cache:
            cache[key] = pl.step(op, 0, prefix)
        return cache[key]

    fusable: dict[str, list | None] = {}

    def exprs_of(op: IROperation, prefix: str):
        key = f"{prefix}|{op.id}"
        if key not in fusable:
            fusable[key] = fusable_expressions(op, probe(op, prefix))
        return fusable[key]

    out = flow.steps
    tail_ref: dict[str, str] = {}
    hash_ref: dict[str, str] = {}  # versión con alto fan-out: id de su tHashOutput
    hash_readers: dict[str, int] = {}
    previous_last: str | None = None
    for group_index, group in enumerate(groups):
        group_ops = [op for op, _ in group]
        prefix = group[0][1]
        start = len(out)
        produced = {d for op in group_ops for d in op.outputs}

        # Fuentes del grupo: lecturas reales (paso propio) o versiones intermedias (flujo de otro grupo).
        refs: list[Ref] = []
        for op, op_prefix in group:
            if op.type not in SOURCES:
                continue
            dataset = op.inputs[0] if op.inputs else ""
            if op.type == "read" and dataset in intermediates:
                refs.append(("ds", dataset))
            else:
                step = probe(op, op_prefix)
                out.append(step)
                refs.append(("step", step.id))
        for op in group_ops:
            for dataset in op.inputs:
                if dataset in intermediates and dataset not in produced and ("ds", dataset) not in refs:
                    refs.append(("ds", dataset))
        # Alto fan-out: cada grupo que lee una versión materializada tiene su propio tHashInput.
        for position, (kind, value) in enumerate(refs):
            if kind == "ds" and value in hash_ref:
                evidence = next(s.evidence for s in out if s.id == hash_ref[value])
                step = _hash_in(value, prefix, hash_ref[value], hash_readers[value], evidence, len(out))
                out.append(step)
                refs[position] = ("step", step.id)

        # Cadena: operaciones de transformación. Las escrituras de versiones no tienen paso propio.
        chain = [
            (op, op_prefix)
            for op, op_prefix in group
            if op.type not in SOURCES and op.type not in WRITES
        ]
        notes: dict[str, str] = {}
        chain = _drop_redundant_sorts(chain, notes)
        resolved = [r for r in (_resolve(ref, tail_ref) for ref in refs) if r]
        # Una misma fuente en dos entradas del grupo (p. ej. union all de un dataset con dos filtros):
        # el FLOW de un paso de lectura admite una sola salida, así que la fuente se reparte con un tMap.
        for source in list(dict.fromkeys(r for r in resolved if resolved.count(r) > 1)):
            evidence = next((st.evidence for st in out if st.id == source), None)
            if evidence is None:
                continue
            rep = _replicate(source, prefix, source, resolved.count(source), evidence)
            out.append(rep)
            resolved = [rep.id if r == source else r for r in resolved]

        tail: str | None = None  # último paso emitido de la cadena (fuente de las siguientes)
        for segment in _segments(chain, exprs_of):
            first_op, first_prefix = segment[0]
            if len(segment) == 1:
                step = probe(first_op, first_prefix)
                if first_op.id in notes:
                    step.assumptions.append(notes[first_op.id])
            else:
                entries = [(op, probe(op, op_prefix), exprs_of(op, op_prefix)) for op, op_prefix in segment]
                step = merge_tmap(
                    entries,
                    step_id=f"{first_prefix}tmap_{first_op.id}",
                    meta=pl.tmap_meta(),
                )
                for _, sub, _ in entries:
                    flow.retarget[sub.id] = step.id
            if tail is None:
                _connect_first(step, first_op, resolved)
            else:
                step.connections = [Connection(type="Main", from_step=tail)]
            out.append(step)
            tail = step.id

        # Sumideros: escrituras de datasets que sí salen del programa. Una versión intermedia no tiene
        # escritura si la leen grupos posteriores (la consumen por el flujo) o si otra escritura la
        # reemplaza sin que nadie la lea (versión muerta).
        for op, op_prefix in group:
            if op.type not in WRITES:
                continue
            if op.type == "write" and any(
                dataset in intermediates and (versions.get((group_index, dataset), (0, False))[0] > 0 or versions.get((group_index, dataset), (0, False))[1])
                for dataset in op.outputs
            ):
                continue
            step = probe(op, op_prefix)
            source = tail or (resolved[0] if resolved else None)
            if source:
                step.connections = [Connection(type="Main", from_step=source), *step.connections]
            out.append(step)
            tail = step.id

        # Salida del grupo hacia otros grupos: el último paso de la cadena (o la fuente, si no hay cadena).
        chain_tail = tail if chain else (resolved[0] if resolved else None)
        for dataset in sorted(produced & intermediates):
            if chain_tail is None:
                continue
            readers, _ = versions.get((group_index, dataset), (0, False))
            evidence = next((s.evidence for s in out if s.id == chain_tail), None)
            if readers > HASH_FAN_OUT:
                if evidence is not None:
                    hop = _hash_out(dataset, prefix, chain_tail, readers, evidence)
                    out.append(hop)
                    hash_ref[dataset] = hop.id
                    hash_readers[dataset] = readers
                    tail_ref.pop(dataset, None)
            elif readers >= 2:
                if evidence is not None:
                    rep = _replicate(dataset, prefix, chain_tail, readers, evidence)
                    out.append(rep)
                    tail_ref[dataset] = rep.id
                    hash_ref.pop(dataset, None)
            else:
                tail_ref[dataset] = chain_tail
                hash_ref.pop(dataset, None)

        # Orden entre grupos sin datos en común: OnSubjobOk desde el último paso del grupo anterior.
        first = out[start] if len(out) > start else None
        if previous_last and first is not None and not refs:
            first.connections = [*first.connections, Connection(type="OnSubjobOk", from_step=previous_last)]
        elif previous_last and refs and refs[0][0] == "step":
            read = next((s for s in out if s.id == refs[0][1]), None)
            if read is not None and not read.connections:
                read.connections = [Connection(type="OnSubjobOk", from_step=previous_last)]
        if out:
            previous_last = out[-1].id

    out[:] = _fan_out_steps(out)
    for index, step in enumerate(out, 1):
        step.order = index
    return flow
