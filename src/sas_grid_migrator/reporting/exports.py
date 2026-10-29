"""Exportación de planes: Markdown por programa, índice del lote, JSON y CSV de pasos."""

import csv
import io
import json
import re
import shutil
from pathlib import Path

from sas_grid_migrator.dependency_graph.builder import DependencyReport
from sas_grid_migrator.migration_planner.models import JobPlan, PlanSet, PlanStep

ROOT = Path(__file__).resolve().parents[3]
CHECKLIST = ROOT / "templates" / "validation-checklist.md"
TALEND_ICONS = ROOT / "apps" / "web" / "public" / "talend-icons"


def _component_icon_file(name: str) -> str | None:
    component = name.split(" ", 1)[0]
    if not re.fullmatch(r"t[A-Za-z0-9]+", component):
        return None
    for extension in ("png", "svg"):
        filename = f"{component}_icon32.{extension}"
        if (TALEND_ICONS / filename).is_file():
            return filename
    return None


def _plan_export_data(plan: JobPlan) -> dict:
    """Serialize technical guidance without persisted manual workflow state."""
    data = plan.model_dump(mode="json", exclude={"job_status"})
    for step in data["steps"]:
        step.pop("status", None)
        step.pop("note", None)
    for child in data["children"]:
        for step in child["steps"]:
            step.pop("status", None)
            step.pop("note", None)
    return data


def safe_name(program: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "__", program)


def _step_md(s: PlanStep, icon_base: str = "/talend-icons") -> list[str]:
    ver = "verificado" if s.verified else "sin verificar"
    icon = _component_icon_file(s.component_candidate)
    icon_md = f" ![Icono Talend]({icon_base.rstrip('/')}/{icon})" if icon else ""
    out = [
        f"### {s.order}. {s.purpose}",
        "",
        f"- **Acción:** {s.action} · **Componente:** `{s.component_candidate}`{icon_md} ({ver})"
        + (
            f" · alternativas: {', '.join(f'`{a}`' for a in s.alternatives)}"
            if s.alternatives
            else ""
        ),
        (
            f"- **Subjob:** `{s.subjob}` · **Confianza:** {s.confidence}"
            f" · **Origen SAS:** `{s.evidence.file}:{s.evidence.line}`"
        ),
    ]
    if s.doc_url or s.variants:
        out.append(
            "- **Referencia:** "
            + (f"[documentación]({s.doc_url})" if s.doc_url else "")
            + (f" · variantes: {', '.join(f'`{v}`' for v in s.variants[:8])}" if s.variants else "")
        )
    if s.connections:
        out.append(
            "- **Conexiones:** "
            + ", ".join(f"{c.type} desde `{c.from_step}`" for c in s.connections)
        )
    if s.properties:
        out.append("- **Propiedades:**")
        out += [
            f"  - `{p.name}`"
            + (f" ({p.label})" if p.label else "")
            + f" = {('`' + p.value + '`') if p.value else '_por configurar_'} — {p.origin}"
            + (
                " · nombre oficial"
                if p.in_catalog
                else " · _no está en el catálogo_"
                if p.in_catalog is False
                else ""
            )
            + (f" · opciones: {', '.join(p.options[:8])}" if p.options else "")
            for p in s.properties
        ]
    if s.schema_columns:
        out.append(
            "- **Esquema:** "
            + ", ".join(
                f"`{c.name}`" + (f":{c.talend_type}" if c.talend_type else "")
                for c in s.schema_columns
            )
            + " _(tipos por determinar)_"
        )
    for e in s.expressions:
        out.append(
            f"- **Expresión** (línea {e.line}): SAS `{e.sas}`"
            + (f" → Java `{e.talend}`" if e.talend else " → _sin traducción automática_")
        )
        out += [f"  - ⚠ {w}" for w in e.warnings]
    if s.assumptions:
        out.append("- **Supuestos:** " + "; ".join(s.assumptions))
    if s.pending:
        out.append("- **Pendientes:**")
        out += [f"  - {p}" for p in s.pending]
    if s.tests:
        out.append("- **Pruebas:** " + ", ".join(f"`{t}`" for t in s.tests))
    out.append("")
    return out


def _grid_recommendation_md(item) -> list[str]:
    out = [
        f"### `{item.pattern_id}` ({item.status})",
        "",
        f"- **Accion:** {item.instruction}",
        f"- **Motivo/limite:** {item.reason}",
        f"- **Evidencia:** `{item.evidence.file}:{item.evidence.line}` | catalogo Grid v{item.catalog_version}",
    ]
    if item.component_candidate:
        out.append(f"- **Componente candidato:** `{item.component_candidate}`")
    if item.doc_url:
        out.append(f"- **Documentacion oficial Talend:** {item.doc_url}")
    if item.dependencies:
        out.append("- **Depende de:** " + ", ".join(f"`{x}`" for x in item.dependencies))
    if item.required:
        out.append("- **Confirmar:** " + "; ".join(item.required))
    if item.details:
        out += ["- **Datos interpretados:**", "", "```json", json.dumps(item.details, ensure_ascii=False, indent=2), "```"]
    out.append("")
    return out


def render_plan_md(plan: JobPlan, icon_base: str = "/talend-icons") -> str:
    n_steps = len(plan.steps) + sum(len(c.steps) for c in plan.children)
    out = [
        f"# Job `{plan.job_name}`",
        "",
        *([plan.description, ""] if plan.description else []),
        f"- **Programa SAS:** `{plan.program}`"
        + (f" (sha256 `{plan.sha256[:12]}`)" if plan.sha256 else ""),
        f"- **Instrucciones:** {n_steps} · **Reglas:** v{plan.rules_version}",
        "- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.",
        "",
    ]
    if plan.entry_macro:
        out += [
            f"La macro principal `%{plan.entry_macro.name}({', '.join(plan.entry_macro.params)})` está integrada en el Job.",
            "",
        ]
    if plan.orchestration.schedules or plan.orchestration.upstream or plan.orchestration.grid_tasks:
        o = plan.orchestration
        out += ["## Orquestación", ""]
        if o.schedules:
            out.append("- Planificación: " + "; ".join(o.schedules))
        if o.upstream:
            out.append("- Depende de (datos): " + ", ".join(f"`{u}`" for u in o.upstream))
        if o.downstream:
            out.append("- Lo consumen: " + ", ".join(f"`{u}`" for u in o.downstream))
        if o.grid_tasks:
            out.append("- Tareas Grid: " + ", ".join(f"`{t}`" for t in o.grid_tasks))
        out.append("")
        if o.grid_recommendations:
            out += ["### Recomendaciones Grid", ""]
            for item in o.grid_recommendations:
                out += _grid_recommendation_md(item)
    if plan.context_variables:
        out += ["## Variables de contexto", ""]
        out += [
            f"- `{c.suggested}` ← SAS `{c.name}`"
            + (f" = `{c.sas_value}`" if c.sas_value else "")
            + f" ({c.origin})"
            for c in plan.context_variables
        ]
        out.append("")
    if plan.libraries_needed:
        out += ["## Conexiones a crear", ""]
        out += [
            f"- `{x.sas_name}` ({x.engine or 'BASE'}{', ' + x.path if x.path else ''}) → {x.suggested_connection}. {x.note}"
            for x in plan.libraries_needed
        ]
        out.append("")
    out += ["## Pasos", ""]
    for s in plan.steps:
        out += _step_md(s, icon_base)
    for c in plan.children:
        out += [f"## Definición de macro auxiliar `%{c.name}`({', '.join(c.params)})", ""]
        for s in c.steps:
            out += _step_md(s, icon_base)
    if plan.unresolved:
        out += ["## Sin resolver", ""] + [f"- {u}" for u in plan.unresolved[:50]]
        if len(plan.unresolved) > 50:
            out.append(f"- … y {len(plan.unresolved) - 50} más")
        out.append("")
    if plan.validation_cases:
        out += ["## Casos de validación", ""]
        out += [f"- `{v.id}` ({v.kind}): {v.description}" for v in plan.validation_cases]
        out.append("")
    if CHECKLIST.exists():
        out += [CHECKLIST.read_text(encoding="utf-8").strip(), ""]
    return "\n".join(out)


def render_index_md(ps: PlanSet, deps: DependencyReport | None = None) -> str:
    out = [
        f"# Plan de migración — proyecto `{ps.project_id}`",
        "",
        f"Reglas v{ps.rules_version} · {len(ps.plans)} programas",
        "",
    ]
    if deps:
        out += ["## Orden de procesamiento sugerido", ""]
        for i, layer in enumerate(deps.processing_order, 1):
            out.append(f"{i}. " + ", ".join(f"`{p}`" for p in layer))
        if deps.cycles:
            out += [
                "",
                "Ciclos detectados (requieren decisión): "
                + "; ".join(" ↔ ".join(c) for c in deps.cycles),
            ]
        out.append("")
    out += [
        "## Jobs",
        "",
        "| Job | Programa | Instrucciones |",
        "| --- | --- | ---: |",
    ]
    for p in ps.plans:
        steps = p.steps + [s for c in p.children for s in c.steps]
        out.append(f"| `{p.job_name}` | `{p.program}` | {len(steps)} paso(s) |")
    if ps.grid_recommendations:
        out += ["", "## Recomendaciones Grid del proyecto", ""]
        for item in ps.grid_recommendations:
            out += _grid_recommendation_md(item)
    return "\n".join(out) + "\n"


def steps_csv(ps: PlanSet) -> str:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(
        [
            "job",
            "programa",
            "paso_id",
            "orden",
            "subjob",
            "componente",
            "verificado",
            "confianza",
            "linea_sas",
            "proposito",
            "pendientes",
        ]
    )
    for p in ps.plans:
        for s in p.steps + [x for c in p.children for x in c.steps]:
            w.writerow(
                [
                    p.job_name,
                    p.program,
                    s.id,
                    s.order,
                    s.subjob,
                    s.component_candidate,
                    s.verified,
                    s.confidence,
                    s.evidence.line,
                    s.purpose,
                    " | ".join(s.pending),
                ]
            )
    return buf.getvalue()


def write_exports(ps: PlanSet, out_dir: Path, deps: DependencyReport | None = None) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    icon_files = {
        icon
        for p in ps.plans
        for s in p.steps + [s for child in p.children for s in child.steps]
        if (icon := _component_icon_file(s.component_candidate))
    }
    if icon_files:
        icon_dir = out_dir / "assets" / "talend-icons"
        icon_dir.mkdir(parents=True, exist_ok=True)
        for icon in sorted(icon_files | {"LICENSE", "NOTICE.md"}):
            shutil.copyfile(TALEND_ICONS / icon, icon_dir / icon)
    written = []
    for p in ps.plans:
        base = out_dir / safe_name(p.program)
        (base.with_suffix(".md")).write_text(render_plan_md(p, "assets/talend-icons"), encoding="utf-8")
        (base.with_suffix(".json")).write_text(json.dumps(_plan_export_data(p), ensure_ascii=False, indent=2), encoding="utf-8")
        written += [base.with_suffix(".md"), base.with_suffix(".json")]
    for name, content in (("index.md", render_index_md(ps, deps)), ("steps.csv", steps_csv(ps))):
        (out_dir / name).write_text(content, encoding="utf-8")
        written.append(out_dir / name)
    return written
