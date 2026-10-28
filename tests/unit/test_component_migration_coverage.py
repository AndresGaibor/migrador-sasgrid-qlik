"""Regresión offline: cada componente de migración debe tener un caso SAS ejecutable por el planner."""

import json
from functools import cache
from pathlib import Path

import pytest

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program
from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec

ROOT = Path(__file__).parent.parent.parent
MATRIX = ROOT / "tests" / "fixtures" / "sas" / "synthetic" / "migration_matrix"
SCOPE = json.loads(
    (ROOT / "rules" / "talend" / "migration-candidate-scope.json").read_text(encoding="utf-8")
)
CASES = json.loads((MATRIX / "component-test-cases.json").read_text(encoding="utf-8"))
MAPPINGS = json.loads(
    (ROOT / "rules" / "mappings" / "talend-components.json").read_text(encoding="utf-8")
)


@cache
def _plan(relative_path: str):
    source = MATRIX / relative_path
    program = parse_program(source.read_text(encoding="utf-8"), relative_path)
    ir = build_ir(program)
    return plan_program(ir, "component-regression", load_mapping_rules(), {})


def _plan_source(source: str, name: str = "edge-case.sas"):
    program = parse_program(source, name)
    return plan_program(build_ir(program), "component-regression", load_mapping_rules(), {})


@pytest.mark.parametrize(
    ("component", "relative_path"),
    [
        (component, path)
        for group in ("core", "alternatives")
        for component, paths in CASES[group].items()
        for path in paths
    ],
)
def test_each_scoped_component_has_a_migration_fixture(component: str, relative_path: str):
    """Una regresión de parser/reglas que quite un candidato debe fallar en su caso concreto."""
    steps = _plan(relative_path).steps
    group = "core" if component in CASES["core"] else "alternatives"

    if group == "core":
        assert any(step.component_candidate == component for step in steps), (component, relative_path)
    else:
        assert any(component in step.alternatives for step in steps), (component, relative_path)


def test_case_matrix_matches_the_versioned_component_scope():
    assert set(CASES["core"]) == set(SCOPE["core"])
    assert set(CASES["alternatives"]) == set(SCOPE["alternatives"])
    for path_list in (*CASES["core"].values(), *CASES["alternatives"].values()):
        assert path_list
        assert all((MATRIX / path).is_file() for path in path_list)


@cache
def _corpus_plans():
    return tuple(
        _plan(path.relative_to(MATRIX).as_posix())
        for path in sorted(MATRIX.rglob("*.sas"))
        if path.name != "component-test-cases.json"
    )


@pytest.mark.parametrize(
    "operation_type", sorted(set(MAPPINGS["operations"]) - {"include"})
)
def test_every_mapped_operation_has_a_fixture_and_emits_its_declared_validation_cases(
    operation_type: str,
):
    matching_steps = [
        (plan, step)
        for plan in _corpus_plans()
        for step in plan.steps
        if step.operation_type == operation_type
    ]
    assert matching_steps, f"No hay fixture SAS para la operación {operation_type}"

    declared_kinds = [case["kind"] for case in MAPPINGS["operations"][operation_type]["tests"]]
    for plan, step in matching_steps:
        cases = {case.id: case for case in plan.validation_cases}
        emitted = [cases[test_id] for test_id in step.tests]
        assert [case.kind for case in emitted] == declared_kinds, (operation_type, step.id)


@pytest.mark.parametrize(
    "operation_type", sorted(set(MAPPINGS["operations"]) - {"include"})
)
def test_every_operation_preserves_mapping_required_decisions(operation_type: str):
    mapping = MAPPINGS["operations"][operation_type]
    required = mapping["required"]
    matching_steps = [
        step
        for plan in _corpus_plans()
        for step in plan.steps
        if step.operation_type == operation_type
    ]

    assert matching_steps
    for step in matching_steps:
        assert all(item in step.pending for item in required), (operation_type, step.id)


def test_include_evidence_is_preserved_but_not_treated_as_a_ready_child_job():
    relative_path = "orchestration/01_static_include.sas"
    parsed = parse_program((MATRIX / relative_path).read_text(encoding="utf-8"), relative_path)
    ir = build_ir(parsed)
    plan = _plan(relative_path)

    assert any(operation.type == "include" for operation in ir.operations)
    macro_call = next(step for step in plan.steps if step.operation_type == "macro_call")
    assert macro_call.component_candidate == "tRunJob"
    assert macro_call.pending
    assert "Job o joblet hijo que implementa la macro" in macro_call.pending


def test_unsupported_sas_operations_are_never_promoted_to_automatic_components():
    for relative_path in (
        "p1/10_transpose.sas",
        "p1/11_update.sas",
        "component_scenarios/19_compare_outputs.sas",
    ):
        unsupported = [
            step for step in _plan(relative_path).steps if step.operation_type == "unsupported"
        ]
        assert unsupported, relative_path
        assert all(step.component_candidate == "por_determinar" for step in unsupported)
        assert all(step.pending and not step.verified for step in unsupported)


def test_tmap_preserves_simple_calculated_column_and_expression():
    plan = _plan("component_scenarios/01_integrated_file_etl.sas")
    compute = next(step for step in plan.steps if step.operation_type == "compute")

    assert compute.component_candidate == "tMap"
    assert [(expr.target, expr.talend) for expr in compute.expressions] == [
        ("net_amount", "(input_row.amount * 0.9)")
    ]
    assert {column.name for column in compute.schema_columns} == {"amount", "net_amount"}


def test_tmap_join_has_main_and_lookup_connections_and_schema():
    plan = _plan("component_scenarios/15_sql_full_join.sas")
    join = next(step for step in plan.steps if step.operation_type == "join")

    assert join.component_candidate == "tMap"
    assert "tJoin" in join.alternatives
    assert [connection.type for connection in join.connections] == ["Main", "Lookup"]
    assert [column.name for column in join.schema_columns] == ["id"]


def test_tmap_filter_case_keeps_filter_candidate_and_tmap_alternative():
    plan = _plan("component_scenarios/01_integrated_file_etl.sas")
    filter_step = next(step for step in plan.steps if step.operation_type == "filter")

    assert filter_step.component_candidate == "tFilterRow"
    assert "tMap" in filter_step.alternatives
    assert filter_step.expressions[0].talend == "(input_row.amount > 0)"
    assert filter_step.properties[0].name == "LOGICAL_OP"
    assert filter_step.properties[0].value == "AND"


def test_tmap_keeps_unsupported_string_functions_explicitly_untranslated():
    plan = _plan("component_scenarios/03_clean_strings.sas")
    compute = next(step for step in plan.steps if step.operation_type == "compute")
    unsupported = next(expr for expr in compute.expressions if expr.target == "normalized_name")
    supported = next(expr for expr in compute.expressions if expr.target == "email_clean")

    assert compute.component_candidate == "tMap"
    assert unsupported.talend is None
    assert any("compbl" in warning for warning in unsupported.warnings)
    assert supported.talend == "input_row.email.trim().toLowerCase()"
    assert compute.requires_semantic_validation


def test_tmap_date_functions_require_semantic_validation():
    plan = _plan("component_scenarios/06_date_datetime_conversion.sas")
    compute = next(step for step in plan.steps if step.operation_type == "compute")

    assert compute.component_candidate == "tMap"
    assert compute.requires_semantic_validation
    assert all(expr.talend is None and expr.warnings for expr in compute.expressions)


def test_tmap_routes_unsupported_conditional_logic_to_review_not_false_translation():
    plan = _plan("component_scenarios/02_reject_invalid_rows.sas")
    compute = next(step for step in plan.steps if step.operation_type == "compute")

    assert compute.component_candidate == "tMap"
    assert compute.requires_semantic_validation
    assert all(expr.talend is None for expr in compute.expressions)
    assert all(any("IF/ELSE" in warning for warning in expr.warnings) for expr in compute.expressions)
    assert not compute.verified


def test_stateful_tmap_like_pattern_stays_manual_when_semantics_are_unknown():
    plan = _plan("component_scenarios/12_denormalize_grouped_values.sas")
    stateful = next(step for step in plan.steps if step.operation_type == "stateful")

    assert stateful.component_candidate == "por_determinar"
    assert stateful.requires_semantic_validation
    assert stateful.pending
    assert not stateful.verified


def test_multi_key_sort_preserves_direction_without_treating_it_as_a_column():
    plan = _plan("component_scenarios/08_multi_key_sort.sas")
    sort = next(step for step in plan.steps if step.operation_type == "sort")
    properties = {property_.name: property_.value for property_ in sort.properties}

    assert properties["CRITERIA"] == "region ASC, transaction_date DESC, customer_id ASC"
    assert [column.name for column in sort.schema_columns] == [
        "region",
        "transaction_date",
        "customer_id",
    ]


def test_nodupkey_does_not_include_sort_direction_in_the_unique_key():
    plan = _plan("component_scenarios/09_group_dedupe.sas")
    dedupe = next(step for step in plan.steps if step.operation_type == "dedupe")
    properties = {property_.name: property_.value for property_ in dedupe.properties}

    assert properties["UNIQUE_KEY"] == "account_id, event_timestamp"
    assert [column.name for column in dedupe.schema_columns] == ["account_id", "event_timestamp"]


def test_case_expression_project_cannot_be_marked_semantically_safe_when_untranslated():
    plan = _plan("component_scenarios/17_sql_case_multi_branch.sas")
    project = next(step for step in plan.steps if step.operation_type == "project")

    assert project.component_candidate == "tMap"
    assert project.expressions
    assert all(expression.talend is None for expression in project.expressions)
    assert project.requires_semantic_validation


def test_sql_union_distinct_and_union_all_do_not_claim_the_same_duplicate_semantics():
    distinct_plan = _plan("transformations/04_sql_distinct_union.sas")
    all_plan = _plan("p0/11_sql_union.sas")
    distinct_union = next(step for step in distinct_plan.steps if step.operation_type == "union")
    union_all = next(step for step in all_plan.steps if step.operation_type == "union")

    assert any("duplic" in item.lower() for item in distinct_union.pending)
    assert not any("duplic" in item.lower() for item in union_all.pending)
    assert distinct_union.requires_semantic_validation and union_all.requires_semantic_validation


def test_proc_append_force_warns_that_incompatible_schemas_need_manual_review():
    plan = _plan("component_scenarios/18_append_force.sas")
    append = next(step for step in plan.steps if step.operation_type == "append")

    assert append.component_candidate == "por_determinar"
    assert append.pending
    assert any("FORCE" in item and "esquema" in item.lower() for item in append.pending)


def test_proc_means_and_freq_do_not_claim_inferred_aggregation_schema():
    for relative_path in (
        "component_scenarios/13_aggregate_missing.sas",
        "component_scenarios/14_frequency_missing.sas",
    ):
        aggregate = next(
            step for step in _plan(relative_path).steps if step.operation_type == "aggregate"
        )
        assert aggregate.component_candidate == "tAggregateRow"
        assert aggregate.requires_semantic_validation
        assert aggregate.pending
        assert not aggregate.schema_columns


@pytest.mark.parametrize(
    ("relative_path", "operation_type", "component"),
    [
        ("component_scenarios/17_sql_case_multi_branch.sas", "project", "tMap"),
        ("transformations/04_sql_distinct_union.sas", "union", "tUnite"),
        ("component_scenarios/02_reject_invalid_rows.sas", "compute", "tMap"),
    ],
)
def test_apply_spec_never_promotes_unverified_semantics_to_executable_components(
    relative_path: str, operation_type: str, component: str
):
    plan = _plan(relative_path)
    step = next(item for item in plan.steps if item.operation_type == operation_type)
    result = build_apply_spec(plan, "Process/Regression")
    emitted = next(item for item in result.components if item.component_name == component)

    assert step.requires_semantic_validation
    assert emitted.draft_only


@pytest.mark.parametrize(
    ("condition", "expected_operator"),
    [
        ("amount > 0 or status = 'A'", "OR"),
        ("amount > 0 and status = 'A'", "AND"),
    ],
)
def test_filter_preserves_boolean_operator_and_source_columns(condition: str, expected_operator: str):
    plan = _plan_source(f"data filtered; set source; if {condition}; run;")
    filter_step = next(step for step in plan.steps if step.operation_type == "filter")
    properties = {property_.name: property_.value for property_ in filter_step.properties}

    assert filter_step.component_candidate == "tFilterRow"
    assert properties["LOGICAL_OP"] == expected_operator
    assert [column.name for column in filter_step.schema_columns] == ["amount", "status"]
    assert filter_step.expressions[0].talend
    assert filter_step.requires_semantic_validation


def test_missing_filter_uses_advanced_mode_and_keeps_null_semantics_warning():
    plan = _plan_source("data filtered; set source; if missing(amount); run;")
    filter_step = next(step for step in plan.steps if step.operation_type == "filter")
    properties = {property_.name: property_.value for property_ in filter_step.properties}

    assert properties["USE_ADVANCED"] == "true"
    assert properties["ADVANCED_COND"] == "(input_row.amount == null)"
    assert any("missing()" in warning for warning in filter_step.expressions[0].warnings)
    assert filter_step.requires_semantic_validation


@pytest.mark.parametrize(
    ("by_clause", "expected_criteria"),
    [
        ("by descending event_date customer_id;", "event_date DESC, customer_id ASC"),
        ("by descending event_date ascending customer_id;", "event_date DESC, customer_id ASC"),
        ("by id descending event_date;", "id ASC, event_date DESC"),
    ],
)
def test_proc_sort_directions_apply_only_to_the_following_key(
    by_clause: str, expected_criteria: str
):
    plan = _plan_source(f"proc sort data=source; {by_clause} run;")
    sort_step = next(step for step in plan.steps if step.operation_type == "sort")
    properties = {property_.name: property_.value for property_ in sort_step.properties}

    assert properties["CRITERIA"] == expected_criteria
    assert [column.name for column in sort_step.schema_columns] == [
        part.split()[0] for part in expected_criteria.split(", ")
    ]


@pytest.mark.parametrize(
    ("join_code", "expected_model"),
    [
        (
            "data joined; merge left(in=left_row) right(in=right_row); by id; if left_row; run;",
            "Left Outer Join",
        ),
        (
            "data joined; merge left(in=left_row) right(in=right_row); by id; if left_row and right_row; run;",
            None,
        ),
    ],
)
def test_merge_join_keeps_unconfirmed_match_model_pending(join_code: str, expected_model: str | None):
    plan = _plan_source(join_code)
    join = next(step for step in plan.steps if step.operation_type == "join")
    properties = {property_.name: property_.value for property_ in join.properties}

    assert join.component_candidate == "tMap"
    assert properties["Join model"] == expected_model
    assert join.pending
    assert join.requires_semantic_validation


def test_nodup_remains_distinct_from_nodupkey_and_has_no_invented_key():
    plan = _plan_source("proc sort data=source out=deduped nodup; by id; run;")
    dedupe = next(step for step in plan.steps if step.operation_type == "dedupe")

    assert dedupe.component_candidate == "por_determinar"
    assert not any(property_.name == "UNIQUE_KEY" for property_ in dedupe.properties)
    assert dedupe.pending and not dedupe.verified


@pytest.mark.parametrize(
    ("source", "expected_action", "expected_data_action"),
    [
        ("data target; set source; run;", "DROP_CREATE", "INSERT"),
        ("proc append base=target data=source; run;", "NONE", "INSERT"),
    ],
)
def test_replace_and_append_have_distinct_write_actions(
    source: str, expected_action: str, expected_data_action: str
):
    plan = _plan_source(source)
    write_step = next(step for step in plan.steps if step.operation_type in {"write", "append"})
    properties = {property_.name: property_.value for property_ in write_step.properties}

    assert properties["TABLE_ACTION"] == expected_action
    assert properties["DATA_ACTION"] == expected_data_action
