"""Completa configuraciones de archivos que se pueden inferir sin abrir Talend."""

import csv
import re
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any

from sas_grid_migrator.intermediate_representation.models import IROperation, ProgramIR

_MACRO = re.compile(r"&([A-Za-z_]\w*)\.?", re.IGNORECASE)
_QUOTED = re.compile(r"(['\"])(.*?)\1", re.DOTALL)
_INPUT = re.compile(r"\binput\b(.*?);", re.IGNORECASE | re.DOTALL)
_DATA_FORMATS = ("date", "ddmmyy", "mmddyy", "yymmdd", "anydtdte", "datetime", "time")


def configure_offline_file_operations(ir: ProgramIR, source_root: Path) -> None:
    """Anota archivos locales, esquemas y tablas de dataset en la IR del programa."""
    source = _source_file(source_root, ir.file)
    if source is None:
        return
    text = _read_text(source)
    blocks = _proc_blocks(text)
    parameters = {name.casefold(): value for name, value in ir.parameters.items()}
    datasets: dict[str, list[dict[str, Any]]] = {}
    subjob_schemas: dict[str, list[dict[str, Any]]] = {}

    for operation in ir.operations:
        if operation.type in {"read_file", "write_file"}:
            block = _block_for_line(blocks, operation.evidence.line)
            details = operation.details
            sas_path = _file_path(operation, block)
            if sas_path:
                resolved = _resolve_local_path(sas_path, parameters, source_root)
                path_expression = _talend_path(sas_path, ir, parameters)
                if path_expression:
                    delimiter = _delimiter(_operation_text(operation, block), resolved)
                    input_fields = _input_fields(_operation_text(operation, block))
                    is_import = operation.type == "read_file"
                    header = _header_value(operation, block, input_fields, resolved, delimiter)
                    columns = (
                        _read_schema(resolved, delimiter, header, input_fields)
                        if is_import and resolved and delimiter
                        else []
                    )
                    if not columns and is_import and input_fields and resolved and delimiter:
                        columns = _input_schema(input_fields)
                    file_config = {
                        "filename": path_expression,
                        "delimiter": delimiter,
                        "header": header,
                        "encoding": "UTF-8",
                        "create_header": _output_header(operation, block),
                        "schema": columns,
                        "ready": bool(is_import and resolved and delimiter and columns),
                        "resolved_path": str(resolved) if resolved else None,
                    }
                    details["offline_file_config"] = file_config
                    if columns:
                        subjob_schemas[operation.step] = columns
                        for dataset in operation.outputs:
                            datasets[dataset.casefold()] = columns
            continue

    for operation in ir.operations:
        inherited = next(
            (
                datasets.get(dataset.casefold())
                for dataset in operation.inputs
                if datasets.get(dataset.casefold())
            ),
            None,
        )
        schema = inherited or subjob_schemas.get(operation.step)
        if operation.type == "write_file":
            config = operation.details.get("offline_file_config")
            if config and schema:
                config["schema"] = schema
                resolved = Path(config["resolved_path"]) if config.get("resolved_path") else None
                config["ready"] = bool(
                    resolved
                    and resolved.parent.is_dir()
                    and config.get("delimiter")
                    and all(column.get("name") and column.get("talend_type") for column in schema)
                )
        if schema:
            operation.details["offline_schema"] = schema
            subjob_schemas[operation.step] = schema
            for dataset in operation.outputs:
                datasets[dataset.casefold()] = schema


def _source_file(root: Path, program: str) -> Path | None:
    relative = PurePosixPath(program.replace("\\", "/"))
    if relative.is_absolute() or ".." in relative.parts:
        return None
    candidate = (root / Path(*relative.parts)).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def _read_text(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return ""


def _proc_blocks(text: str) -> list[tuple[int, int, str]]:
    blocks = []
    pattern = re.compile(
        r"\bproc\s+(?:import|export)\b.*?\b(?:run|quit)\s*;", re.IGNORECASE | re.DOTALL
    )
    for match in pattern.finditer(text):
        start = text.count("\n", 0, match.start()) + 1
        end = text.count("\n", 0, match.end()) + 1
        blocks.append((start, end, match.group(0)))
    return blocks


def _block_for_line(blocks: list[tuple[int, int, str]], line: int) -> str:
    return next((block for start, end, block in blocks if start <= line <= end), "")


def _operation_text(operation: IROperation, block: str) -> str:
    statements = operation.details.get("statements", [])
    return "\n".join(str(item) for item in statements) + "\n" + block


def _file_path(operation: IROperation, block: str) -> str | None:
    raw = operation.details.get("file")
    if isinstance(raw, str) and raw.strip():
        return _unquote(raw.strip())
    statement = "infile" if operation.type == "read_file" else "file"
    match = re.search(
        rf"\b{statement}\s+([^;]+);", _operation_text(operation, block), re.IGNORECASE | re.DOTALL
    )
    if not match:
        return None
    path = match.group(1).strip()
    quoted = _QUOTED.search(path)
    if quoted:
        return quoted.group(2)
    return path.split()[0] if path else None


def _unquote(value: str) -> str:
    if len(value) > 1 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1].replace(value[0] * 2, value[0])
    return value


def _expanded_path(value: str, parameters: dict[str, str]) -> str | None:
    missing = False

    def replace(match: re.Match[str]) -> str:
        nonlocal missing
        replacement = parameters.get(match.group(1).casefold())
        if replacement is None or re.search(r"[&%]", replacement):
            missing = True
            return ""
        return replacement

    expanded = _MACRO.sub(replace, value).replace("\\", "/")
    return None if missing else expanded


def _resolve_local_path(value: str, parameters: dict[str, str], root: Path) -> Path | None:
    expanded = _expanded_path(value, parameters)
    if not expanded:
        return None
    path = Path(expanded)
    candidate = path.resolve() if path.is_absolute() else (root / path).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def _talend_path(value: str, ir: ProgramIR, parameters: dict[str, str]) -> str | None:
    matches = list(_MACRO.finditer(value))
    segments: list[str] = []
    cursor = 0
    for match in matches:
        name = match.group(1)
        if name.casefold() not in parameters:
            ir.parameters.setdefault(name, "")
        literal = value[cursor : match.start()].replace("\\", "/")
        if literal:
            segments.append(f'"{literal}"')
        segments.append(f"context.{name}")
        cursor = match.end()
    tail = value[cursor:].replace("\\", "/")
    if tail:
        segments.append(f'"{tail}"')
    if not matches:
        normalized = value.replace("\\", "/")
        if Path(normalized).is_absolute() or normalized.startswith("/"):
            return None
        ir.parameters.setdefault("SAS_PROJECT_ROOT", ".")
        segments = ["context.SAS_PROJECT_ROOT", f'"/{normalized.lstrip("/")}"']
    return " + ".join(segments) if segments else None


def _delimiter(text: str, path: Path | None) -> str | None:
    match = re.search(
        r"\b(?:dlm|delimiter|dlmstr)\s*=\s*(['\"])(.*?)\1", text, re.IGNORECASE | re.DOTALL
    )
    if match:
        value = match.group(2).replace("''", "'").replace('""', '"')
        return value if len(value) == 1 else None
    if (
        re.search(r"\bdsd\b", text, re.IGNORECASE)
        and path
        and path.suffix.casefold()
        in {
            ".csv",
            ".tsv",
            ".psv",
        }
    ):
        return {".csv": ",", ".tsv": "\t", ".psv": "|"}[path.suffix.casefold()]
    if path:
        return {".csv": ",", ".tsv": "\t", ".psv": "|"}.get(path.suffix.casefold())
    return None


def _header_value(
    operation: IROperation,
    block: str,
    input_fields: list[tuple[str, str | None]],
    path: Path | None,
    delimiter: str | None,
) -> str:
    if re.search(r"\bgetnames\s*=\s*(?:no|false|0)", block, re.IGNORECASE):
        return "0"
    if re.search(r"\bgetnames\s*=\s*(?:yes|true|1)", block, re.IGNORECASE):
        return "1"
    firstobs = re.search(
        r"\bfirstobs\s*=\s*(\d+)", _operation_text(operation, block), re.IGNORECASE
    )
    if firstobs and int(firstobs.group(1)) > 1:
        return "1"
    if input_fields and path and delimiter:
        try:
            with path.open(encoding="utf-8-sig", newline="") as stream:
                first = next(csv.reader(stream, delimiter=delimiter), [])
            names = [name.casefold() for name, _ in input_fields]
            if [value.strip().casefold() for value in first] == names:
                return "1"
        except (OSError, UnicodeError, csv.Error):
            pass
    return "1" if operation.details.get("file") else "0"


def _input_fields(text: str) -> list[tuple[str, str | None]]:
    match = _INPUT.search(text)
    if not match:
        return []
    tokens = re.findall(r"\$[\w.]+|[A-Za-z_]\w*|\d+(?:\.\d+)?\.?|[:@#/-]+", match.group(1))
    fields: list[tuple[str, str | None]] = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token in {":", "@", "@@", "/"} or token.startswith("#"):
            index += 1
            continue
        if not re.fullmatch(r"[A-Za-z_]\w*", token):
            return []
        name = token
        index += 1
        if index < len(tokens) and tokens[index] == ":":
            index += 1
        format_ = None
        if index < len(tokens) and re.fullmatch(
            r"(?:\$[\w.]+|\d+(?:\.\d+)?\.?|[A-Za-z_]\w*\d*\.)", tokens[index], re.IGNORECASE
        ):
            format_ = tokens[index]
            index += 1
        fields.append((name, format_))
    return fields


def _read_schema(
    path: Path | None,
    delimiter: str | None,
    header: str,
    input_fields: list[tuple[str, str | None]],
) -> list[dict[str, Any]]:
    if not path or not delimiter or not path.is_file():
        return []
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(islice(csv.reader(stream, delimiter=delimiter), 101))
    except (OSError, UnicodeError, csv.Error):
        return []
    if not rows:
        return []
    has_header = header == "1"
    names = [item.strip() for item in rows[0]] if has_header else [name for name, _ in input_fields]
    sample = rows[1:101] if has_header else rows[:100]
    if not names or any(not re.fullmatch(r"[A-Za-z_]\w*", name) for name in names):
        return []
    formats = {name.casefold(): fmt for name, fmt in input_fields}
    columns = []
    for column_index, name in enumerate(names):
        values = [row[column_index].strip() for row in sample if column_index < len(row)]
        talend_type = _infer_type(values, formats.get(name.casefold()))
        columns.append(
            {
                "name": name,
                "talend_type": talend_type,
                "nullable": any(not value for value in values),
                "origin": f"CSV local {path.name}",
            }
        )
    return columns


def _input_schema(fields: list[tuple[str, str | None]]) -> list[dict[str, Any]]:
    return [
        {
            "name": name,
            "talend_type": _infer_type([], format_),
            "nullable": True,
            "origin": "SAS INPUT",
        }
        for name, format_ in fields
    ]


def _infer_type(values: list[str], sas_format: str | None) -> str:
    format_text = (sas_format or "").casefold()
    if format_text.startswith("$"):
        return "id_String"
    if any(name in format_text for name in _DATA_FORMATS):
        return "id_Date"
    present = [value for value in values if value]
    if present and all(re.fullmatch(r"[+-]?\d+", value) for value in present):
        numbers = [int(value) for value in present]
        return "id_Integer" if all(-(2**31) <= value < 2**31 for value in numbers) else "id_Long"
    if present and all(re.fullmatch(r"[+-]?\d+(?:\.\d+)?", value) for value in present):
        return "id_Double"
    return "id_String"


def _output_header(operation: IROperation, block: str) -> str | None:
    if operation.type != "write_file":
        return None
    if re.search(r"\bputnames\s*=\s*(?:yes|true|1)", block, re.IGNORECASE):
        return "true"
    if re.search(r"\bputnames\s*=\s*(?:no|false|0)", block, re.IGNORECASE):
        return "false"
    return "false"
