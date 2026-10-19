"""Construye rules/talend/components.json desde las definiciones XML de componentes de Talaxie
(fork abierto de Talend Open Studio, Apache-2.0).

Uso: python tools/build_talend_catalog.py <ruta/components> [--out rules/talend/components.json]
`<ruta/components>` es .../org.talend.designer.components.localprovider/components del repo
https://github.com/Talaxie/tdi-studio-se (solo hacen falta `*_java.xml` y `*_messages.properties`).

El catálogo guarda hechos estructurados (nombres, campos, conectores, valores por defecto, drivers); no copia
la documentación en prosa. Los nombres de parámetro son los internos (`TABLE`, `QUERY`, `LOGICAL_OP`…), los
mismos que talend-mcp devuelve en `parameters` de un componente de un Job.
"""

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

DOC_URL = "https://help.qlik.com/talend/en-US/components/8.0/{}"
AUDIT_FILE = Path(__file__).resolve().parents[1] / "rules" / "talend" / "catalog-audit.json"
OFFICIAL_INVENTORY_FILE = Path(__file__).resolve().parents[1] / "rules" / "talend" / "components.json"
# sufijos de rol, del más largo al más corto, para agrupar variantes por tecnología
ROLES = [
    "OutputBulkExec", "OutputBulk", "BulkExec", "TableList", "ColumnList", "LastInsertId", "SCDELT",
    "SCD", "Connection", "Rollback", "Commit", "Close", "Input", "Output", "Row", "SP",
]  # fmt: skip
VARIANT_FAMILIES = ("Databases", "Cloud", "Big Data", "File/", "Business_Intelligence/DB_SCD")
MAX_ITEM_VALUE = 60
MAX_COND = 240


def read_props(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if "=" in line and not line.lstrip().startswith(("#", "!")):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip().replace("\\:", ":").replace("\\=", "=")
    return out


def _items(el: ET.Element, labels: dict[str, str], param: str) -> list[dict]:
    items = el.find("ITEMS")
    if items is None:
        return []
    default = items.get("DEFAULT")
    out = []
    for it in items.findall("ITEM"):
        name = it.get("NAME", "")
        d: dict = {"name": name, "label": labels.get(f"{param}.ITEM.{name}")}
        v = it.get("VALUE")
        if v is not None and len(v) <= MAX_ITEM_VALUE:
            d["value"] = v
        if name == default:
            d["default"] = True
        out.append({k: x for k, x in d.items() if x not in (None, "")})
    return out


def _columns(el: ET.Element) -> list[dict]:
    t = el.find("TABLE")
    cols = []
    if t is not None:
        for c in t.findall("COLUMN"):
            cols.append(
                {k.lower(): v for k, v in c.attrib.items() if k in ("NAME", "TYPE", "LENGTH")}
            )
    return cols


def _param(el: ET.Element, labels: dict[str, str], advanced: bool) -> dict:
    name = el.get("NAME", "")
    p: dict = {
        "name": name,
        "label": labels.get(f"{name}.NAME"),
        "field": el.get("FIELD"),
        "required": el.get("REQUIRED") == "true" or None,
        "advanced": advanced or None,
        "readonly": el.get("READONLY") == "true" or None,
        "show_if": (el.get("SHOW_IF") or "")[:MAX_COND] or None,
    }
    d = el.find("DEFAULT")
    if d is not None and (d.text or "").strip():
        p["default"] = d.text.strip()[:200]
    items = _items(el, labels, name)
    if items:
        p["items"] = items
    if el.get("FIELD") == "TABLE":
        # columnas de una tabla de parámetros (p. ej. CONDITIONS): sus ITEM son campos, no opciones
        cols = []
        wrap = el.find("ITEMS")
        for it in wrap.findall("ITEM") if wrap is not None else []:
            cols.append({"name": it.get("NAME"), "field": it.get("FIELD")})
        p["columns"] = cols
        p.pop("items", None)
    schema_cols = _columns(el)
    if schema_cols and el.get("FIELD") == "SCHEMA_TYPE":
        p["fixed_columns"] = schema_cols
    return {k: v for k, v in p.items() if v not in (None, "")}


def parse_component(xml: Path, props: dict[str, str]) -> dict | None:
    try:
        root = ET.parse(xml).getroot()
    except ET.ParseError:
        return None
    name = xml.parent.name
    h = root.find("HEADER")
    comp: dict = {
        "name": name,
        "description": props.get("LONG_NAME", ""),
        "families": [f.text.strip() for f in root.findall("FAMILIES/FAMILY") if f.text],
        "status": h.get("STATUS") if h is not None else None,
        "version": h.get("VERSION") if h is not None else None,
        "startable": (h.get("STARTABLE") == "true") if h is not None else None,
        "doc_url": DOC_URL.format(name.lower()),
    }
    comp["connectors"] = [
        {
            k: v
            for k, v in {
                "type": c.get("CTYPE"),
                "name": c.get("NAME"),
                "max_input": c.get("MAX_INPUT"),
                "max_output": c.get("MAX_OUTPUT"),
            }.items()
            if v is not None
        }
        for c in root.findall("CONNECTORS/CONNECTOR")
    ]
    params = [_param(p, props, False) for p in root.findall("PARAMETERS/PARAMETER")]
    params += [_param(p, props, True) for p in root.findall("ADVANCED_PARAMETERS/PARAMETER")]
    comp["parameters"] = params
    comp["imports"] = [
        {k: v for k, v in {"module": i.get("MODULE"), "mvn": i.get("MVN"),
                           "required_if": (i.get("REQUIRED_IF") or "")[:MAX_COND] or None}.items() if v}
        for i in root.findall("CODEGENERATION/IMPORTS/IMPORT")
    ]  # fmt: skip
    # las listas siempre presentes (vacías si no hay): el consumidor no necesita comprobar claves
    always = ("parameters", "connectors", "imports", "families")
    return {k: v for k, v in comp.items() if k in always or v not in (None, "", [])}


def split_variant(name: str) -> tuple[str, str] | None:
    """tOracleInput → (Input, Oracle). Solo para nombres con un rol conocido y tecnología no vacía."""
    m = re.fullmatch(r"t(File)(Input|Output)(.+)", name)
    if m:  # tFileInputDelimited → rol FileInput, variante Delimited
        return f"File{m.group(2)}", m.group(3)
    for role in ROLES:
        if name.endswith(role) and len(name) > len(role) + 1:
            return role, name[1 : -len(role)]
    return None


def build(src: Path, audit_file: Path = AUDIT_FILE) -> dict:
    comps = {}
    for d in sorted(p for p in src.iterdir() if p.is_dir() and p.name.startswith("t")):
        xml = d / f"{d.name}_java.xml"
        if xml.exists():
            c = parse_component(xml, read_props(d / f"{d.name}_messages.properties"))
            if c:
                comps[d.name] = c
    families: dict[str, list[str]] = {}
    variants: dict[str, dict[str, list[str]]] = {}
    for n, c in comps.items():
        for f in c.get("families", []):
            families.setdefault(f, []).append(n)
        # solo familias donde el sufijo identifica un rol (bases de datos, nube, ficheros); no Processing/Custom Code
        in_scope = any(f.startswith(VARIANT_FAMILIES) for f in c.get("families", []))
        if (
            in_scope
            and (v := split_variant(n))
            and not n.startswith(("tFileInputMS", "tFileOutputMS"))
        ):
            variants.setdefault(v[0], {}).setdefault(v[1], []).append(n)
    # un rol solo es útil si hay más de una tecnología
    variants = {r: t for r, t in variants.items() if len(t) > 1}
    catalog = {
        "source": "https://github.com/Talaxie/tdi-studio-se (Apache-2.0), components/*/*_java.xml",
        "doc_base": DOC_URL.format("<componente en minúsculas>"),
        "count": len(comps),
        "families": {k: sorted(v) for k, v in sorted(families.items())},
        "variants": variants,
        "components": comps,
    }
    if OFFICIAL_INVENTORY_FILE.exists():
        try:
            existing_catalog = json.loads(OFFICIAL_INVENTORY_FILE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"Invalid catalog at {OFFICIAL_INVENTORY_FILE}") from exc
        if not isinstance(existing_catalog, dict):
            raise ValueError(f"Invalid catalog at {OFFICIAL_INVENTORY_FILE}")
        if existing_catalog.get("official_inventory"):
            catalog["official_inventory"] = existing_catalog["official_inventory"]
    if audit_file.exists():
        audit = json.loads(audit_file.read_text(encoding="utf-8"))
        for name, record in audit.get("recommended_components", {}).items():
            if name not in comps:
                continue
            url = record.get("official_url")
            if url and record.get("official_reference_scope") in (
                "component_page", "standard_properties"
            ):
                comps[name]["doc_url"] = url
            else:
                # No exponer la URL genérica generada por nombre como si estuviera verificada.
                comps[name].pop("doc_url", None)
        catalog["official_audit"] = audit
    return catalog


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("components_dir", type=Path)
    ap.add_argument("--out", type=Path, default=Path("rules/talend/components.json"))
    ap.add_argument("--audit", type=Path, default=AUDIT_FILE)
    a = ap.parse_args()
    cat = build(a.components_dir, a.audit)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(cat, ensure_ascii=False, indent=1, sort_keys=False) + "\n")
    print(
        f"{cat['count']} componentes, {len(cat['families'])} familias, {a.out.stat().st_size // 1024} KB"
    )
