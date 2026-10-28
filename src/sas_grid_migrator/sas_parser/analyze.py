"""Análisis estático de un proyecto importado: parsea los .sas y clasifica construcciones."""

import json
from collections import Counter

from pydantic import BaseModel

from sas_grid_migrator.domain.models import SCHEMA_VERSION, FileKind
from sas_grid_migrator.domain.redaction import redact_sas
from sas_grid_migrator.persistence.artifacts import write_text_atomic
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.ast import ParsedProgram
from sas_grid_migrator.sas_parser.parser import parse_program
from sas_grid_migrator.semantic_analysis.classify import classify, load_rules


class CoverageEntry(BaseModel):
    tag: str
    priority: str
    count: int


class Analysis(BaseModel):
    schema_version: str = SCHEMA_VERSION
    project_id: str
    rules_version: str
    programs: list[ParsedProgram]
    coverage: list[CoverageEntry]


class AnalysisSummary(BaseModel):
    project_id: str
    rules_version: str
    programs: int
    statements: int
    unrecognized: int
    macro_fragments: int
    findings_by_priority: dict[str, int]
    coverage: list[CoverageEntry]


def summarize(a: Analysis) -> AnalysisSummary:
    by_prio = Counter(f.priority for p in a.programs for f in p.findings if f.priority)
    return AnalysisSummary(
        project_id=a.project_id,
        rules_version=a.rules_version,
        programs=len(a.programs),
        statements=sum(p.stats.statements for p in a.programs),
        unrecognized=sum(p.stats.unrecognized for p in a.programs),
        macro_fragments=sum(p.stats.fragments for p in a.programs),
        findings_by_priority=dict(sorted(by_prio.items())),
        coverage=a.coverage,
    )


def analyze_project(store: Store, project_id: str) -> Analysis:
    rules = load_rules()
    manifest = store.get_manifest(project_id)
    programs, total = [], Counter()
    for f in manifest.files:
        if f.kind != FileKind.SAS:
            continue
        raw = (store.source_dir(project_id) / f.path).read_bytes()
        text = raw.decode(f.encoding or "utf-8", errors="replace").lstrip("\u200b\ufeff")
        prog = parse_program(redact_sas(text), f.path, f.sha256)
        total += classify(prog, rules)
        programs.append(prog)
    cov = [
        CoverageEntry(tag=t, priority=p, count=n)
        for (p, t), n in sorted(total.items(), key=lambda kv: (kv[0][0], -kv[1], kv[0][1]))
    ]
    analysis = Analysis(
        project_id=project_id, rules_version=rules.version, programs=programs, coverage=cov
    )
    write_text_atomic(store.analysis_path(project_id), analysis.model_dump_json())
    return analysis


def load_analysis(store: Store, project_id: str) -> Analysis | None:
    p = store.analysis_path(project_id)
    return Analysis.model_validate(json.loads(p.read_text(encoding="utf-8"))) if p.exists() else None
