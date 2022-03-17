from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

conditionals_node_0 = ('Conditionals', 0)
boolean_expressions_node_0 = ('Boolean Expressions', 0)
decision_diagrams_node_0 = ('Decision Diagrams', 0)
relational_and_logical_operators_node_0 = ('Relational and Logical Operators', 0)
conditional_statements_node_0 = ('Conditional Statements', 0)
nested_conditional_statements_node_0 = ('Nested Conditional Statements', 0)
simple_programs_node_0 = ('Simple Programs', 0)
programs_node_0 = ('Programs', 0)
conditionals_node_1 = ('Conditionals', 1)
boolean_expressions_node_1 = ('Boolean Expressions', 1)
decision_diagrams_node_1 = ('Decision Diagrams', 1)
relational_and_logical_operators_node_1 = ('Relational and Logical Operators', 1)
conditional_statements_node_1 = ('Conditional Statements', 1)
nested_conditional_statements_node_1 = ('Nested Conditional Statements', 1)
simple_programs_node_1 = ('Simple Programs', 1)
programs_node_1 = ('Programs', 1)


def conditionals():
    model = DynamicBayesianNetwork([
        (conditionals_node_0, boolean_expressions_node_0),
        (conditionals_node_0, decision_diagrams_node_0),
        (conditionals_node_0, relational_and_logical_operators_node_0),
        (conditionals_node_0, conditional_statements_node_0),
        (conditionals_node_0, nested_conditional_statements_node_0),
        (conditionals_node_0, simple_programs_node_0),
        (conditionals_node_0, programs_node_0),
        (boolean_expressions_node_0, decision_diagrams_node_0),
        (boolean_expressions_node_0, relational_and_logical_operators_node_0),
        (boolean_expressions_node_0, conditional_statements_node_0),
        (decision_diagrams_node_0, conditional_statements_node_0),
        (relational_and_logical_operators_node_0, conditional_statements_node_0),
        (conditional_statements_node_0, nested_conditional_statements_node_0),
        (conditional_statements_node_0, simple_programs_node_0),
        (nested_conditional_statements_node_0, programs_node_0),
        (simple_programs_node_0, programs_node_0),
        (conditionals_node_0, conditionals_node_1),
        (boolean_expressions_node_0, boolean_expressions_node_1),
        (decision_diagrams_node_0, decision_diagrams_node_1),
        (relational_and_logical_operators_node_0, relational_and_logical_operators_node_1),
        (conditional_statements_node_0, conditional_statements_node_1),
        (nested_conditional_statements_node_0, nested_conditional_statements_node_1),
        (simple_programs_node_0, simple_programs_node_1),
        (programs_node_0, programs_node_1),
        (conditionals_node_1, boolean_expressions_node_1),
        (conditionals_node_1, decision_diagrams_node_1),
        (conditionals_node_1, relational_and_logical_operators_node_1),
        (conditionals_node_1, conditional_statements_node_1),
        (conditionals_node_1, nested_conditional_statements_node_1),
        (conditionals_node_1, simple_programs_node_1),
        (conditionals_node_1, programs_node_1),
        (boolean_expressions_node_1, decision_diagrams_node_1),
        (boolean_expressions_node_1, relational_and_logical_operators_node_1),
        (boolean_expressions_node_1, conditional_statements_node_1),
        (decision_diagrams_node_1, conditional_statements_node_1),
        (relational_and_logical_operators_node_1, conditional_statements_node_1),
        (conditional_statements_node_1, nested_conditional_statements_node_1),
        (conditional_statements_node_1, simple_programs_node_1),
        (nested_conditional_statements_node_1, programs_node_1),
        (simple_programs_node_1, programs_node_1),
    ])

    conditionals_cpd = TabularCPD(conditionals_node_0, 2, [
        [0.5], [0.5]
    ])

    boolean_expressions_cpd = TabularCPD(boolean_expressions_node_0, 2, [
        [0.8, 0.3],
        [0.2, 0.7]
    ], evidence=[conditionals_node_0], evidence_card=[2])

    decision_diagrams_cpd = TabularCPD(decision_diagrams_node_0, 2, [
        [0.9, 0.7, 0.6, 0.2],
        [0.1, 0.3, 0.4, 0.8]
    ], evidence=[conditionals_node_0, boolean_expressions_node_0], evidence_card=[2, 2])

    relational_and_logical_operators_cpd = TabularCPD(relational_and_logical_operators_node_0, 2, [
        [0.9, 0.7, 0.6, 0.2],
        [0.1, 0.3, 0.4, 0.8]
    ], evidence=[conditionals_node_0, boolean_expressions_node_0], evidence_card=[2, 2])

    conditional_statements_cpd = TabularCPD(conditional_statements_node_0, 2, [
        [0.95, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.3, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.05, 0.2, 0.2, 0.4, 0.2, 0.4, 0.4, 0.7, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], evidence=[conditionals_node_0, decision_diagrams_node_0, relational_and_logical_operators_node_0,
                 boolean_expressions_node_0], evidence_card=[2, 2, 2, 2])

    nested_conditional_statements_cpd = TabularCPD(nested_conditional_statements_node_0, 2, [
        [0.9, 0.4, 0.7, 0.2],
        [0.1, 0.6, 0.3, 0.8]
    ], evidence=[conditionals_node_0, conditional_statements_node_0], evidence_card=[2, 2])

    simple_programs_cpd = TabularCPD(simple_programs_node_0, 2, [
        [0.9, 0.5, 0.7, 0.1],
        [0.1, 0.5, 0.3, 0.9]
    ], evidence=[conditionals_node_0, conditional_statements_node_0], evidence_card=[2, 2])

    programs_cpd = TabularCPD(programs_node_0, 2, [
        [0.9, 0.7, 0.3, 0.5, 0.7, 0.4, 0.2, 0.1],
        [0.1, 0.3, 0.7, 0.5, 0.3, 0.6, 0.8, 0.9]
    ], evidence=[conditionals_node_0, nested_conditional_statements_node_0, simple_programs_node_0],
                              evidence_card=[2, 2, 2])

    conditionals_transitional_cpd = TabularCPD(conditionals_node_1, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], evidence=[conditionals_node_0], evidence_card=[2])

    boolean_expressions_transitional_cpd = TabularCPD(boolean_expressions_node_1, 2, [
        [0.9, 0.7, 0.6, 0.1],
        [0.1, 0.3, 0.4, 0.9]
    ], evidence=[boolean_expressions_node_0, conditionals_node_1], evidence_card=[2, 2])

    decision_diagrams_transitional_cpd = TabularCPD(decision_diagrams_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], evidence=[decision_diagrams_node_0, conditionals_node_1, boolean_expressions_node_1], evidence_card=[2, 2, 2])

    relational_and_logical_operators_transitional_cpd = TabularCPD(relational_and_logical_operators_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], evidence=[relational_and_logical_operators_node_0, conditionals_node_1, boolean_expressions_node_1],
                                                                   evidence_card=[2, 2, 2])

    conditional_statements_transitional_cpd = TabularCPD(conditional_statements_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], evidence=[conditional_statements_node_0, conditionals_node_1, decision_diagrams_node_1,
                 relational_and_logical_operators_node_1, boolean_expressions_node_1], evidence_card=[2, 2, 2, 2, 2])

    nested_conditional_statements_transitional_cpd = TabularCPD(nested_conditional_statements_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], evidence=[nested_conditional_statements_node_0, conditionals_node_1, conditional_statements_node_1],
                                                                evidence_card=[2, 2, 2])

    simple_programs_transitional_cpd = TabularCPD(simple_programs_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], evidence=[simple_programs_node_0, conditionals_node_1, conditional_statements_node_1], evidence_card=[2, 2, 2])

    programs_transitional_cpd = TabularCPD(programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], evidence=[programs_node_0, conditionals_node_1, nested_conditional_statements_node_1, simple_programs_node_1],
                                           evidence_card=[2, 2, 2, 2])

    model.add_cpds(conditionals_cpd, boolean_expressions_cpd, decision_diagrams_cpd,
                   relational_and_logical_operators_cpd, conditional_statements_cpd, nested_conditional_statements_cpd,
                   simple_programs_cpd, programs_cpd, conditionals_transitional_cpd,
                   boolean_expressions_transitional_cpd, decision_diagrams_transitional_cpd,
                   relational_and_logical_operators_transitional_cpd, conditional_statements_transitional_cpd,
                   nested_conditional_statements_transitional_cpd, simple_programs_transitional_cpd,
                   programs_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    conditionals_model = conditionals()
