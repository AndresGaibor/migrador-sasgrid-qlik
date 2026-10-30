"""Funciones SAS del traductor en línea: cada una con su equivalente Java y su guarda de nulo.

Las funciones sin equivalente claro no se traducen: el resultado queda sin Java y con el motivo.
"""

import pytest

from sas_grid_migrator.migration_planner.expressions import translate


def test_logical_operators_and_not_missing_translate_to_one_condition():
    t = translate("cantidad > 0 and not missing(precio)")
    assert t.talend == "((input_row.cantidad > 0) && !((input_row.precio == null)))"


def test_numeric_literal_types_a_column_comparison_with_a_warning():
    t = translate("cantidad > 0")
    assert t.talend == "(input_row.cantidad > 0)"
    assert any("se infiere del literal" in w for w in t.warnings)


def test_text_equality_with_a_column_is_null_safe_and_flagged():
    t = translate("canal = 'WEB'")
    assert t.talend == '"WEB".equals(input_row.canal)'
    assert any("tipo no confirmado: se asumió texto" in w for w in t.warnings)


def test_blank_literal_matches_missing_or_blank():
    assert translate("canal = ''").talend == "(input_row.canal == null || input_row.canal.trim().isEmpty())"
    assert translate("canal ne ''").talend == "!((input_row.canal == null || input_row.canal.trim().isEmpty()))"


def test_text_in_list_is_an_or_of_null_safe_equalities():
    assert translate("tipo in ('D', 'C')").talend == '("D".equals(input_row.tipo) || "C".equals(input_row.tipo))'



@pytest.mark.parametrize(
    ("sas", "expected"),
    [
        ("substr(producto, 1, 3)", "(input_row.producto == null ? null : input_row.producto.substring(0, 0 + 3))"),
        ("substr(producto, n, 2)", "(input_row.producto == null ? null : input_row.producto.substring((input_row.n - 1), (input_row.n - 1) + 2))"),
        ("round(precio)", "(input_row.precio == null ? null : Math.round(input_row.precio))"),
        ("round(precio, 0.01)", "(input_row.precio == null ? null : (Math.round(input_row.precio / 0.01) * 0.01))"),
        ("length(texto)", "(input_row.texto == null ? 0 : input_row.texto.length())"),
        ("abs(saldo)", "(input_row.saldo == null ? null : Math.abs(input_row.saldo))"),
        ("int(saldo)", "(input_row.saldo == null ? null : ((long) (input_row.saldo)))"),
        ("cats(a, b)", '((input_row.a == null ? "" : String.valueOf(input_row.a)) + (input_row.b == null ? "" : String.valueOf(input_row.b)))'),
        ("upcase(canal)", "input_row.canal.toUpperCase()"),
        ("ifn(saldo < 0, 0, saldo)", "((input_row.saldo < 0) ? 0 : input_row.saldo)"),
    ],
)
def test_each_function_has_its_java_and_null_guard(sas, expected):
    assert translate(sas).talend == expected


def test_substr_needs_its_three_arguments():
    t = translate("substr(producto, 2)")
    assert t.talend is None
    assert any("tres argumentos" in w for w in t.warnings)


def test_unknown_function_stays_untranslated_with_its_name():
    t = translate("zipcode(codigo)")
    assert t.talend is None
    assert any("intck" in w or "función" in w for w in t.warnings)


@pytest.mark.parametrize(
    ("sas", "expected"),
    [
        ("min(a, b)", "Math.min(input_row.a, input_row.b)"),
        ("max(a, b, 0)", "Math.max(Math.max(input_row.a, input_row.b), 0)"),
        ("coalesce(a, 0)", "(input_row.a != null ? input_row.a : 0)"),
        ("compress(texto)", "(input_row.texto == null ? null : input_row.texto.replaceAll(\"\\\\s\", \"\"))"),
        ("index(texto, 'AB')", "(input_row.texto == null ? null : (input_row.texto.indexOf(\"AB\") + 1))"),
    ],
)
def test_min_max_coalesce_compress_index(sas, expected):
    assert translate(sas).talend == expected


def test_compress_with_character_list_stays_untranslated():
    t = translate("compress(texto, 'abc')")
    assert t.talend is None
    assert any("compress" in w for w in t.warnings)


@pytest.mark.parametrize(
    ("sas", "expected"),
    [
        ("today()", "TalendDate.getCurrentDate()"),
        ("year(fecha)", '(input_row.fecha == null ? null : TalendDate.getPartOfDate("YEAR", input_row.fecha))'),
        ("month(fecha)", '(input_row.fecha == null ? null : TalendDate.getPartOfDate("MONTH", input_row.fecha))'),
        ("day(fecha)", '(input_row.fecha == null ? null : TalendDate.getPartOfDate("DAY_OF_MONTH", input_row.fecha))'),
        ("input(txt, best12.)", "(input_row.txt == null ? null : Double.parseDouble(input_row.txt))"),
        ("put(n, best12.)", "(input_row.n == null ? null : String.valueOf(input_row.n))"),
    ],
)
def test_date_and_numeric_conversion_functions(sas, expected):
    t = translate(sas)
    assert t.talend == expected
    assert t.warnings


def test_date_informat_in_input_stays_untranslated():
    t = translate("input(txt, mmddyy8.)")
    assert t.talend is None
    assert any("input()" in w for w in t.warnings)


def test_dotted_identifiers_are_still_identifiers():
    assert translate("cars.make").talend == "input_row.make"


@pytest.mark.parametrize(
    ("sas", "expected_fragment"),
    [
        ("mdy(m, d, y)", "TalendDate.parseDate(\"yyyy-MM-dd\""),
        ("datepart(fecha)", "TalendDate.formatDate(\"yyyy-MM-dd\", input_row.fecha)"),
        ("intnx('month', fecha, 1)", 'TalendDate.addDate(input_row.fecha, (int) (1), "mm")'),
        ("intnx('day', fecha, 2)", 'TalendDate.addDate(input_row.fecha, (int) (2), "dd")'),
        ("intnx('week', fecha, 1)", '(int) ((1) * 7)'),
        ("intnx('month', fecha, 1, 'begin')", 'formatDate("yyyy-MM-01"'),
        ("intck('day', ini, fin)", 'TalendDate.diffDate(input_row.fin, input_row.ini, "dd")'),
        ("input(txt, yymmdd10.)", 'TalendDate.parseDate("yyyy-MM-dd", input_row.txt)'),
        ("input(txt, ddmmyy10.)", 'TalendDate.parseDate("dd/MM/yyyy", input_row.txt)'),
        ("put(fecha, date9.)", 'TalendDate.formatDate("ddMMMyyyy", input_row.fecha)'),
    ],
)
def test_date_functions_and_formats(sas, expected_fragment):
    t = translate(sas)
    assert t.talend is not None, sas
    assert expected_fragment in t.talend, t.talend
    assert t.warnings, sas


@pytest.mark.parametrize("sas", ["intnx('month', fecha, 1, 'end')", "intnx('quarter', fecha, 1)", "intck('month')"])
def test_unsupported_date_forms_stay_untranslated_with_reason(sas):
    t = translate(sas)
    assert t.talend is None, sas
    assert t.warnings, sas
