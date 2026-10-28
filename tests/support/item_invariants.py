"""Invariantes de un `.item` ya escrito: lo que Studio comprueba al cargar el Job.

Un `.item` puede ser XML válido y aun así dejar a Studio con un diálogo al abrirlo. Esto no es un aviso de la vista
Problemas, así que `job_problems` no lo ve: hay que comprobarlo en el archivo.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

XSI_TYPE = "{http://www.w3.org/2001/XMLSchema-instance}type"
TRIGGERS = {"SUBJOB_OK", "SUBJOB_ERROR", "COMPONENT_OK", "COMPONENT_ERROR", "RUN_IF"}


def _parameter(element: ET.Element, name: str) -> str | None:
    for parameter in element.findall("elementParameter"):
        if parameter.get("name") == name:
            return parameter.get("value")
    return None


def item_problems(path: Path) -> list[str]:
    """Problemas de coherencia del `.item`; lista vacía si Studio lo cargaría sin avisos."""
    root = ET.parse(path).getroot()
    nodes = {_parameter(node, "UNIQUE_NAME"): node for node in root.findall("node")}
    problems: list[str] = []

    flows: list[tuple[ET.Element, str]] = []
    for connection in root.findall("connection"):
        source, target = connection.get("source"), connection.get("target")
        for end in (source, target):
            if end not in nodes:
                problems.append(f"la conexión '{connection.get('label')}' apunta al nodo '{end}', que no existe")
        if (connection.get("connectorName") or "FLOW") in TRIGGERS:
            continue
        if (connection.get("connectorName") or "FLOW") == "FLOW":
            flows.append((connection, _parameter(connection, "UNIQUE_NAME") or connection.get("label") or ""))

    for unique_name, node in nodes.items():
        if node.get("componentName") != "tMap":
            continue
        # Studio enlaza cada conexión con una tabla del mapper por nombre; si no coinciden avisa de errores
        # "in the following connections" al abrir el Job.
        data = node.find("nodeData")
        outputs = [table.get("name") for table in data.findall("outputTables")] if data is not None else []
        inputs = [table.get("name") for table in data.findall("inputTables")] if data is not None else []
        metadata = [table.get("name") for table in node.findall("metadata")]
        leaving = [(connection, name) for connection, name in flows if connection.get("source") == unique_name]
        entering = [name for connection, name in flows if connection.get("target") == unique_name]
        for connection, name in leaving:
            if name not in outputs:
                problems.append(f"{unique_name}: la conexión de salida '{name}' no tiene tabla de salida en el mapper ({outputs})")
            if name not in metadata:
                problems.append(f"{unique_name}: la conexión de salida '{name}' no tiene esquema (metadata {metadata})")
            if connection.get("metaname") != name:
                problems.append(f"{unique_name}: la conexión '{name}' tiene metaname '{connection.get('metaname')}', no '{name}'")
        for name in entering:
            if name not in inputs:
                problems.append(f"{unique_name}: la conexión de entrada '{name}' no tiene tabla de entrada en el mapper ({inputs})")
    return problems
