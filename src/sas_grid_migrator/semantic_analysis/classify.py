"""Clasifica las construcciones del parser con `rules/sas/constructs.json` (P0/P1/P2)."""

from collections import Counter
from pathlib import Path

from pydantic import BaseModel

from sas_grid_migrator.domain.models import Evidence, Finding, Severity
from sas_grid_migrator.sas_parser.ast import Loc, MacroDef, Node, ParsedProgram, ProcStep


class Rule(BaseModel):
    priority: str
    severity: str = "info"
    message: str = ""


class Rules(BaseModel):
    version: str
    default_proc: Rule
    unknown: Rule
    constructs: dict[str, Rule]

    def for_tag(self, tag: str) -> Rule:
        if tag in self.constructs:
            return self.constructs[tag]
        return self.default_proc if tag.startswith("proc:") else self.unknown


def default_rules_path() -> Path:
    return Path(__file__).resolve().parents[3] / "rules" / "sas" / "constructs.json"


def load_rules(path: Path | None = None) -> Rules:
    return Rules.model_validate_json((path or default_rules_path()).read_text(encoding="utf-8"))


def _tags(nodes: list[Node]):
    """Genera (etiqueta, ubicación) recorriendo cuerpos de macro y consultas SQL."""
    for n in nodes:
        if isinstance(n, ProcStep):
            for t in n.constructs:
                if not t.startswith("sql_"):
                    yield t, n.loc
            for q in n.queries:
                for t in q.constructs:
                    yield t, q.loc
            continue
        lines = getattr(n, "construct_lines", {})
        for t in n.constructs:
            yield t, n.loc.model_copy(update={"line": lines[t]}) if t in lines else n.loc
        if isinstance(n, MacroDef):
            yield from _tags(n.body)


def classify(program: ParsedProgram, rules: Rules) -> Counter[tuple[str, str]]:
    """Añade hallazgos P1/P2 a `program.findings`; devuelve conteo por (prioridad, etiqueta)."""
    coverage: Counter[tuple[str, str]] = Counter()
    seen: set[tuple[str, int]] = set()
    for tag, loc in _tags(program.nodes):
        rule = rules.for_tag(tag)
        coverage[(rule.priority, tag)] += 1
        if rule.priority == "P0" or (tag, loc.line) in seen:
            continue
        seen.add((tag, loc.line))
        program.findings.append(
            Finding(
                code=tag,
                severity=Severity(rule.severity),
                message=rule.message,
                evidence=Evidence(file=loc.file, line=loc.line),
                priority=rule.priority,  # type: ignore[arg-type]
            )
        )
    return coverage


__all__ = ["Loc", "Rule", "Rules", "classify", "default_rules_path", "load_rules"]
