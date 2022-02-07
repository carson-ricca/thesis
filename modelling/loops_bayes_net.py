from pomegranate import *

from constants import success, failure


def get_loops_nodes(loops):
    repetition = _get_repetition_probability(loops)
    variable_scope = _get_variable_scope_probability(loops)
    decision_diagrams = _get_decision_diagrams_probability(loops, repetition)
    while_loops = _get_while_loops_probability(loops, repetition, decision_diagrams)
    for_loops = _get_for_loops_probability(loops, repetition, decision_diagrams)
    simple_programs = _get_simple_programs_probability(loops, while_loops, for_loops, variable_scope)
    nested_loops = _get_nested_loops_probability(loops, while_loops, for_loops, variable_scope)
    programs = _get_programs_with_repetition_probability(loops, simple_programs, nested_loops)

    repetition_node = State(repetition, name='Repetition')
    variable_scope_node = State(variable_scope, name='Variable Scope')
    decision_diagrams_node = State(decision_diagrams, name='Decision Diagrams')
    while_loops_node = State(while_loops, name='While Loops')
    for_loops_node = State(for_loops, name='For Loops')
    simple_programs_node = State(simple_programs, name='Simple Programs')
    nested_loops_node = State(nested_loops, name='Nested Loops')
    programs_node = State(programs, name='Programs')
    return [repetition_node, variable_scope_node, decision_diagrams_node, while_loops_node, for_loops_node,
            simple_programs_node, nested_loops_node, programs_node]


def generate_loops_bayesian_network():
    loops = _get_loops_probability()
    loops_node = State(loops, name='Loops')
    nodes = get_loops_nodes(loops)
    repetition_node = nodes[0]
    variable_scope_node = nodes[1]
    decision_diagrams_node = nodes[2]
    while_loops_node = nodes[3]
    for_loops_node = nodes[4]
    simple_programs_node = nodes[5]
    nested_loops_node = nodes[6]
    programs_node = nodes[7]

    model = BayesianNetwork('Loops')
    model.add_states(loops_node, repetition_node, variable_scope_node, decision_diagrams_node, while_loops_node,
                     for_loops_node, simple_programs_node, nested_loops_node, programs_node)
    model.add_edge(loops_node, repetition_node)
    model.add_edge(loops_node, decision_diagrams_node)
    model.add_edge(loops_node, variable_scope_node)
    model.add_edge(loops_node, for_loops_node)
    model.add_edge(loops_node, while_loops_node)
    model.add_edge(loops_node, nested_loops_node)
    model.add_edge(loops_node, simple_programs_node)
    model.add_edge(loops_node, programs_node)
    model.add_edge(repetition_node, while_loops_node)
    model.add_edge(repetition_node, decision_diagrams_node)
    model.add_edge(repetition_node, for_loops_node)
    model.add_edge(decision_diagrams_node, while_loops_node)
    model.add_edge(decision_diagrams_node, for_loops_node)
    model.add_edge(while_loops_node, simple_programs_node)
    model.add_edge(while_loops_node, nested_loops_node)
    model.add_edge(for_loops_node, simple_programs_node)
    model.add_edge(for_loops_node, nested_loops_node)
    model.add_edge(variable_scope_node, simple_programs_node)
    model.add_edge(variable_scope_node, nested_loops_node)
    model.add_edge(simple_programs_node, programs_node)
    model.add_edge(nested_loops_node, programs_node)
    model.bake()
    return model


def _get_loops_probability():
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_repetition_probability(loops):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [loops])


def _get_variable_scope_probability(loops):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [loops])


def _get_decision_diagrams_probability(loops, repetition):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.3],
        [failure, failure, failure, 0.7],
    ], [loops, repetition])


def _get_while_loops_probability(loops, repetition, decision_diagrams):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.7],
        [success, failure, success, failure, 0.3],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, success, success, success, 0.7],
        [failure, success, success, failure, 0.3],
        [failure, success, failure, success, 0.4],
        [failure, success, failure, failure, 0.6],
        [failure, failure, success, success, 0.3],
        [failure, failure, success, failure, 0.7],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [loops, repetition, decision_diagrams])


def _get_for_loops_probability(loops, repetition, decision_diagrams):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.7],
        [success, failure, success, failure, 0.3],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, success, success, success, 0.7],
        [failure, success, success, failure, 0.3],
        [failure, success, failure, success, 0.4],
        [failure, success, failure, failure, 0.6],
        [failure, failure, success, success, 0.3],
        [failure, failure, success, failure, 0.7],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [loops, repetition, decision_diagrams])


def _get_simple_programs_probability(loops, while_loops, for_loops, variable_scope):
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.95],
        [success, success, success, success, failure, 0.05],
        [success, success, success, failure, success, 0.8],
        [success, success, success, failure, failure, 0.2],
        [success, success, failure, success, success, 0.8],
        [success, success, failure, success, failure, 0.2],
        [success, success, failure, failure, success, 0.6],
        [success, success, failure, failure, failure, 0.4],
        [success, failure, success, success, success, 0.8],
        [success, failure, success, success, failure, 0.2],
        [success, failure, success, failure, success, 0.6],
        [success, failure, success, failure, failure, 0.4],
        [success, failure, failure, success, success, 0.6],
        [success, failure, failure, success, failure, 0.4],
        [success, failure, failure, failure, success, 0.3],
        [success, failure, failure, failure, failure, 0.7],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.6],
        [failure, success, success, failure, failure, 0.4],
        [failure, success, failure, success, success, 0.6],
        [failure, success, failure, success, failure, 0.4],
        [failure, success, failure, failure, success, 0.3],
        [failure, success, failure, failure, failure, 0.7],
        [failure, failure, success, success, success, 0.6],
        [failure, failure, success, success, failure, 0.4],
        [failure, failure, success, failure, success, 0.3],
        [failure, failure, success, failure, failure, 0.7],
        [failure, failure, failure, success, success, 0.3],
        [failure, failure, failure, success, failure, 0.7],
        [failure, failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, failure, 0.9],
    ], [loops, while_loops, for_loops, variable_scope])


def _get_nested_loops_probability(loops, while_loops, for_loops, variable_scope):
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.95],
        [success, success, success, success, failure, 0.05],
        [success, success, success, failure, success, 0.8],
        [success, success, success, failure, failure, 0.2],
        [success, success, failure, success, success, 0.8],
        [success, success, failure, success, failure, 0.2],
        [success, success, failure, failure, success, 0.6],
        [success, success, failure, failure, failure, 0.4],
        [success, failure, success, success, success, 0.8],
        [success, failure, success, success, failure, 0.2],
        [success, failure, success, failure, success, 0.6],
        [success, failure, success, failure, failure, 0.4],
        [success, failure, failure, success, success, 0.6],
        [success, failure, failure, success, failure, 0.4],
        [success, failure, failure, failure, success, 0.3],
        [success, failure, failure, failure, failure, 0.7],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.6],
        [failure, success, success, failure, failure, 0.4],
        [failure, success, failure, success, success, 0.6],
        [failure, success, failure, success, failure, 0.4],
        [failure, success, failure, failure, success, 0.3],
        [failure, success, failure, failure, failure, 0.7],
        [failure, failure, success, success, success, 0.6],
        [failure, failure, success, success, failure, 0.4],
        [failure, failure, success, failure, success, 0.3],
        [failure, failure, success, failure, failure, 0.7],
        [failure, failure, failure, success, success, 0.3],
        [failure, failure, failure, success, failure, 0.7],
        [failure, failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, failure, 0.9],
    ], [loops, while_loops, for_loops, variable_scope])


def _get_programs_with_repetition_probability(loops, simple_programs, nested_loops):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.7],
        [success, success, failure, failure, 0.3],
        [success, failure, success, success, 0.7],
        [success, failure, success, failure, 0.3],
        [success, failure, failure, success, 0.3],
        [success, failure, failure, failure, 0.7],
        [failure, success, success, success, 0.7],
        [failure, success, success, failure, 0.3],
        [failure, success, failure, success, 0.3],
        [failure, success, failure, failure, 0.7],
        [failure, failure, success, success, 0.3],
        [failure, failure, success, failure, 0.7],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [loops, simple_programs, nested_loops])
