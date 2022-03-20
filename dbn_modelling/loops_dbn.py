from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

loops_node_0 = ('Loops', 0)
identifying_repetition_node_0 = ('Identifying Repetition', 0)
decision_diagrams_node_0 = ('Decision Diagrams', 0)
while_loops_node_0 = ('While Loops', 0)
for_loops_node_0 = ('For Loops', 0)
variable_scope_node_0 = ('Variable Scope', 0)
simple_programs_node_0 = ('Simple Programs', 0)
nested_loops_node_0 = ('Nested Loops', 0)
programs_node_0 = ('Programs with Repetition', 0)
loops_node_1 = ('Loops', 1)
identifying_repetition_node_1 = ('Identifying Repetition', 1)
decision_diagrams_node_1 = ('Decision Diagrams', 1)
while_loops_node_1 = ('While Loops', 1)
for_loops_node_1 = ('For Loops', 1)
variable_scope_node_1 = ('Variable Scope', 1)
simple_programs_node_1 = ('Simple Programs', 1)
nested_loops_node_1 = ('Nested Loops', 1)
programs_node_1 = ('Programs with Repetition', 1)


def loops():
    model = DynamicBayesianNetwork([
        (loops_node_0, identifying_repetition_node_0),
        (loops_node_0, decision_diagrams_node_0),
        (loops_node_0, while_loops_node_0),
        (loops_node_0, for_loops_node_0),
        (loops_node_0, variable_scope_node_0),
        (loops_node_0, simple_programs_node_0),
        (loops_node_0, nested_loops_node_0),
        (loops_node_0, programs_node_0),
        (identifying_repetition_node_0, decision_diagrams_node_0),
        (identifying_repetition_node_0, while_loops_node_0),
        (identifying_repetition_node_0, for_loops_node_0),
        (decision_diagrams_node_0, while_loops_node_0),
        (decision_diagrams_node_0, for_loops_node_0),
        (while_loops_node_0, simple_programs_node_0),
        (while_loops_node_0, nested_loops_node_0),
        (for_loops_node_0, simple_programs_node_0),
        (for_loops_node_0, nested_loops_node_0),
        (variable_scope_node_0, simple_programs_node_0),
        (variable_scope_node_0, nested_loops_node_0),
        (simple_programs_node_0, programs_node_0),
        (nested_loops_node_0, programs_node_0),
        (loops_node_0, loops_node_1),
        (identifying_repetition_node_0, identifying_repetition_node_1),
        (decision_diagrams_node_0, decision_diagrams_node_1),
        (while_loops_node_0, while_loops_node_1),
        (for_loops_node_0, for_loops_node_1),
        (variable_scope_node_0, variable_scope_node_1),
        (simple_programs_node_0, simple_programs_node_1),
        (nested_loops_node_0, nested_loops_node_1),
        (programs_node_0, programs_node_1),
        (loops_node_1, identifying_repetition_node_1),
        (loops_node_1, decision_diagrams_node_1),
        (loops_node_1, while_loops_node_1),
        (loops_node_1, for_loops_node_1),
        (loops_node_1, variable_scope_node_1),
        (loops_node_1, simple_programs_node_1),
        (loops_node_1, nested_loops_node_1),
        (loops_node_1, programs_node_1),
        (identifying_repetition_node_1, decision_diagrams_node_1),
        (identifying_repetition_node_1, while_loops_node_1),
        (identifying_repetition_node_1, for_loops_node_1),
        (decision_diagrams_node_1, while_loops_node_1),
        (decision_diagrams_node_1, for_loops_node_1),
        (while_loops_node_1, simple_programs_node_1),
        (while_loops_node_1, nested_loops_node_1),
        (for_loops_node_1, simple_programs_node_1),
        (for_loops_node_1, nested_loops_node_1),
        (variable_scope_node_1, simple_programs_node_1),
        (variable_scope_node_1, nested_loops_node_1),
        (simple_programs_node_1, programs_node_1),
        (nested_loops_node_1, programs_node_1)
    ])

    loops_cpd = TabularCPD(loops_node_0, 2, [
        [0.5], [0.5]
    ])

    identifying_repetition_cpd = TabularCPD(identifying_repetition_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [loops_node_0], [2])

    decision_diagrams_cpd = TabularCPD(decision_diagrams_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3],
        [0.1, 0.3, 0.3, 0.7]
    ], [loops_node_0, identifying_repetition_node_0], [2, 2])

    while_loops_cpd = TabularCPD(while_loops_node_0, 2, [
        [0.95, 0.8, 0.7, 0.4, 0.7, 0.4, 0.3, 0.1],
        [0.05, 0.2, 0.3, 0.6, 0.3, 0.6, 0.7, 0.9]
    ], [loops_node_0, identifying_repetition_node_0, decision_diagrams_node_0], [2, 2, 2])

    for_loops_cpd = TabularCPD(for_loops_node_0, 2, [
        [0.95, 0.8, 0.7, 0.4, 0.7, 0.4, 0.3, 0.1],
        [0.05, 0.2, 0.3, 0.6, 0.3, 0.6, 0.7, 0.9]
    ], [loops_node_0, identifying_repetition_node_0, decision_diagrams_node_0], [2, 2, 2])

    variable_scope_cpd = TabularCPD(variable_scope_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [loops_node_0], [2])

    simple_programs_cpd = TabularCPD(simple_programs_node_0, 2, [
        [0.95, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.3, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.05, 0.2, 0.2, 0.4, 0.2, 0.4, 0.4, 0.7, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [loops_node_0, while_loops_node_0, for_loops_node_0, variable_scope_node_0], [2, 2, 2, 2])

    nested_loops_cpd = TabularCPD(nested_loops_node_0, 2, [
        [0.95, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.3, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.05, 0.2, 0.2, 0.4, 0.2, 0.4, 0.4, 0.7, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [loops_node_0, while_loops_node_0, for_loops_node_0, variable_scope_node_0], [2, 2, 2, 2])

    programs_cpd = TabularCPD(programs_node_0, 2, [
        [0.95, 0.7, 0.7, 0.3, 0.7, 0.3, 0.3, 0.1],
        [0.05, 0.3, 0.3, 0.7, 0.3, 0.7, 0.7, 0.9]
    ], [loops_node_0, simple_programs_node_0, nested_loops_node_0], [2, 2, 2])

    loops_transitional_cpd = TabularCPD(loops_node_1, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [loops_node_0], [2])

    identifying_repetition_transitional_cpd = TabularCPD(identifying_repetition_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [identifying_repetition_node_0, loops_node_1], [2, 2])

    decision_diagrams_transitional_cpd = TabularCPD(decision_diagrams_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [decision_diagrams_node_0, loops_node_1, identifying_repetition_node_1], [2, 2, 2])

    while_loops_transitional_cpd = TabularCPD(while_loops_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [while_loops_node_0, loops_node_1, identifying_repetition_node_1, decision_diagrams_node_1], [2, 2, 2, 2])

    for_loops_transitional_cpd = TabularCPD(for_loops_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [for_loops_node_0, loops_node_1, identifying_repetition_node_1, decision_diagrams_node_1], [2, 2, 2, 2])

    variable_scope_transitional_cpd = TabularCPD(variable_scope_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [variable_scope_node_0, loops_node_1], [2, 2])

    simple_programs_transitional_cpd = TabularCPD(simple_programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], [simple_programs_node_0, loops_node_1, while_loops_node_1, for_loops_node_1, variable_scope_node_1],
                                                  [2, 2, 2, 2, 2])

    nested_loops_transitional_cpd = TabularCPD(nested_loops_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], [nested_loops_node_0, loops_node_1, while_loops_node_1, for_loops_node_1, variable_scope_node_1],
                                               [2, 2, 2, 2, 2])

    programs_transitional_cpd = TabularCPD(programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [programs_node_0, loops_node_1, simple_programs_node_1, nested_loops_node_1], [2, 2, 2, 2])

    model.add_cpds(loops_cpd, identifying_repetition_cpd, decision_diagrams_cpd, while_loops_cpd, for_loops_cpd,
                   variable_scope_cpd, simple_programs_cpd, nested_loops_cpd, programs_cpd, loops_transitional_cpd,
                   identifying_repetition_transitional_cpd, decision_diagrams_transitional_cpd,
                   while_loops_transitional_cpd, for_loops_transitional_cpd, variable_scope_transitional_cpd,
                   simple_programs_transitional_cpd, nested_loops_transitional_cpd, programs_transitional_cpd)

    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    loops_model = loops()
