"""`%web_drop_table` y `%web_open_table` son ayudas de SAS Studio para el visor de resultados: no son lógica de negocio."""

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.sas_parser.parser import parse_program

SOURCE = """%web_drop_table(WORK.ACURA);
proc sql; create table work.acura as select * from work.cars where make = 'Acura'; quit;
%web_open_table(WORK.ACURA);
%mi_macro(x=1);
"""


def macro_calls(source: str) -> list[str]:
    ir = build_ir(parse_program(source, "p.sas"), {})
    return [op.details["name"] for op in ir.operations if op.type == "macro_call"]


def test_sas_studio_viewer_helpers_do_not_become_steps():
    assert macro_calls(SOURCE) == ["mi_macro"]
