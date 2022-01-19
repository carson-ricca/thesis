from pomegranate import *
from constants import success, failure


def generate_conditionals_bayesian_network():
    conditionals = _get_conditionals_probability()
    boolean = _get_boolean_probability(conditionals)
    decision = _get_decision_probability(conditionals, boolean)
    operators = _get_operators_probability(conditionals, boolean)
    conditional_statements = _get_conditional_statements_probability(conditionals, decision, operators, boolean)
    nested_conditional_statements = _get_nested_conditional_probability(conditionals, conditional_statements)
    simple_programs = _get_simple_programs_probability(conditionals, conditional_statements)
    programs = _get_programs_probability(conditionals, nested_conditional_statements, simple_programs)

    c = Node(conditionals, name='Conditionals')
    b = Node(boolean, name='Boolean')
    d = Node(decision, name='Decision')
    o = Node(operators, name='Operators')
    cs = Node(conditional_statements, name='Conditional Statements')
    ncs = Node(nested_conditional_statements, name='Nested Conditional Statements')
    sp = Node(simple_programs, name='Simple Programs')
    p = Node(programs, name='Programs')

    model = BayesianNetwork('Conditionals')
    model.add_states(c, b, d, o, cs, ncs, sp, p)
    model.add_edge(c, b)
    model.add_edge(c, d)
    model.add_edge(c, o)
    model.add_edge(c, cs)
    model.add_edge(c, ncs)
    model.add_edge(c, sp)
    model.add_edge(c, p)
    model.add_edge(b, d)
    model.add_edge(b, o)
    model.add_edge(b, cs)
    model.add_edge(d, cs)
    model.add_edge(o, cs)
    model.add_edge(cs, ncs)
    model.add_edge(cs, sp)
    model.add_edge(ncs, p)
    model.add_edge(sp, p)
    model.bake()
    return model


def _get_conditionals_probability():
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_boolean_probability(conditionals):
    return ConditionalProbabilityTable([
        [success, success, 0.8],
        [success, failure, 0.2],
        [failure, success, 0.3],
        [failure, failure, 0.7]
    ], [conditionals])


def _get_decision_probability(conditionals, boolean):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], [conditionals, boolean])


def _get_operators_probability(conditionals, boolean):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], [conditionals, boolean])


def _get_conditional_statements_probability(conditionals, decision, operators, boolean):
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.95],
        [success, success, success, success, failure, 0.05],
        [success, success, success, failure, success, 0.8],
        [success, success, success, failure, failure, 0.2],
        [success, success, failure, failure, success, 0.6],
        [success, success, failure, failure, failure, 0.4],
        [success, failure, failure, failure, success, 0.2],
        [success, failure, failure, failure, failure, 0.8],
        [success, failure, failure, success, success, 0.5],
        [success, failure, failure, success, failure, 0.5],
        [success, failure, success, success, success, 0.7],
        [success, failure, success, success, failure, 0.3],
        [success, success, failure, success, success, 0.6],
        [success, success, failure, success, failure, 0.4],
        [success, failure, success, failure, success, 0.6],
        [success, failure, success, failure, failure, 0.4],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.6],
        [failure, success, success, failure, failure, 0.4],
        [failure, success, failure, failure, success, 0.2],
        [failure, success, failure, failure, failure, 0.8],
        [failure, failure, failure, failure, success, 0.05],
        [failure, failure, failure, failure, failure, 0.95],
        [failure, failure, failure, success, success, 0.2],
        [failure, failure, failure, success, failure, 0.8],
        [failure, failure, success, success, success, 0.4],
        [failure, failure, success, success, failure, 0.6],
        [failure, failure, success, failure, success, 0.2],
        [failure, failure, success, failure, failure, 0.8],
        [failure, success, failure, success, success, 0.4],
        [failure, success, failure, success, failure, 0.6],
    ], [conditionals, decision, operators, boolean])


def _get_nested_conditional_probability(conditionals, conditional_statements):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.4],
        [success, failure, failure, 0.6],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], [conditionals, conditional_statements])


def _get_simple_programs_probability(conditionals, conditional_statements):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.5],
        [success, failure, failure, 0.5],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9]
    ], [conditionals, conditional_statements])


def _get_programs_probability(conditionals, nested_conditionals, simple_programs):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.9],
        [success, success, success, failure, 0.1],
        [success, success, failure, success, 0.7],
        [success, success, failure, failure, 0.3],
        [success, failure, failure, success, 0.3],
        [success, failure, failure, failure, 0.7],
        [success, failure, success, success, 0.5],
        [success, failure, success, failure, 0.5],
        [failure, success, success, success, 0.7],
        [failure, success, success, failure, 0.3],
        [failure, success, failure, success, 0.4],
        [failure, success, failure, failure, 0.6],
        [failure, failure, success, success, 0.2],
        [failure, failure, success, failure, 0.8],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [conditionals, nested_conditionals, simple_programs])
