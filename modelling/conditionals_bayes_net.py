from pomegranate import *


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
    return DiscreteDistribution({'Success': 0.5, 'Failure': 0.5})


def _get_boolean_probability(conditionals):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 0.8],
        ['Success', 'Failure', 0.2],
        ['Failure', 'Success', 0.3],
        ['Failure', 'Failure', 0.7]
    ], [conditionals])


def _get_decision_probability(conditionals, boolean):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 'Success', 0.9],
        ['Success', 'Success', 'Failure', 0.1],
        ['Success', 'Failure', 'Success', 0.7],
        ['Success', 'Failure', 'Failure', 0.3],
        ['Failure', 'Success', 'Success', 0.6],
        ['Failure', 'Success', 'Failure', 0.4],
        ['Failure', 'Failure', 'Success', 0.2],
        ['Failure', 'Failure', 'Failure', 0.8]
    ], [conditionals, boolean])


def _get_operators_probability(conditionals, boolean):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 'Success', 0.9],
        ['Success', 'Success', 'Failure', 0.1],
        ['Success', 'Failure', 'Success', 0.7],
        ['Success', 'Failure', 'Failure', 0.3],
        ['Failure', 'Success', 'Success', 0.6],
        ['Failure', 'Success', 'Failure', 0.4],
        ['Failure', 'Failure', 'Success', 0.2],
        ['Failure', 'Failure', 'Failure', 0.8]
    ], [conditionals, boolean])


def _get_conditional_statements_probability(conditionals, decision, operators, boolean):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 'Success', 'Success', 'Success', 0.95],
        ['Success', 'Success', 'Success', 'Success', 'Failure', 0.05],
        ['Success', 'Success', 'Success', 'Failure', 'Success', 0.8],
        ['Success', 'Success', 'Success', 'Failure', 'Failure', 0.2],
        ['Success', 'Success', 'Failure', 'Failure', 'Success', 0.6],
        ['Success', 'Success', 'Failure', 'Failure', 'Failure', 0.4],
        ['Success', 'Failure', 'Failure', 'Failure', 'Success', 0.2],
        ['Success', 'Failure', 'Failure', 'Failure', 'Failure', 0.8],
        ['Success', 'Failure', 'Failure', 'Success', 'Success', 0.5],
        ['Success', 'Failure', 'Failure', 'Success', 'Failure', 0.5],
        ['Success', 'Failure', 'Success', 'Success', 'Success', 0.7],
        ['Success', 'Failure', 'Success', 'Success', 'Failure', 0.3],
        ['Success', 'Success', 'Failure', 'Success', 'Success', 0.6],
        ['Success', 'Success', 'Failure', 'Success', 'Failure', 0.4],
        ['Success', 'Failure', 'Success', 'Failure', 'Success', 0.6],
        ['Success', 'Failure', 'Success', 'Failure', 'Failure', 0.4],
        ['Failure', 'Success', 'Success', 'Success', 'Success', 0.8],
        ['Failure', 'Success', 'Success', 'Success', 'Failure', 0.2],
        ['Failure', 'Success', 'Success', 'Failure', 'Success', 0.6],
        ['Failure', 'Success', 'Success', 'Failure', 'Failure', 0.4],
        ['Failure', 'Success', 'Failure', 'Failure', 'Success', 0.2],
        ['Failure', 'Success', 'Failure', 'Failure', 'Failure', 0.8],
        ['Failure', 'Failure', 'Failure', 'Failure', 'Success', 0.05],
        ['Failure', 'Failure', 'Failure', 'Failure', 'Failure', 0.95],
        ['Failure', 'Failure', 'Failure', 'Success', 'Success', 0.2],
        ['Failure', 'Failure', 'Failure', 'Success', 'Failure', 0.8],
        ['Failure', 'Failure', 'Success', 'Success', 'Success', 0.4],
        ['Failure', 'Failure', 'Success', 'Success', 'Failure', 0.6],
        ['Failure', 'Failure', 'Success', 'Failure', 'Success', 0.2],
        ['Failure', 'Failure', 'Success', 'Failure', 'Failure', 0.8],
        ['Failure', 'Success', 'Failure', 'Success', 'Success', 0.4],
        ['Failure', 'Success', 'Failure', 'Success', 'Failure', 0.6],
    ], [conditionals, decision, operators, boolean])


def _get_nested_conditional_probability(conditionals, conditional_statements):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 'Success', 0.9],
        ['Success', 'Success', 'Failure', 0.1],
        ['Success', 'Failure', 'Success', 0.4],
        ['Success', 'Failure', 'Failure', 0.6],
        ['Failure', 'Success', 'Success', 0.7],
        ['Failure', 'Success', 'Failure', 0.3],
        ['Failure', 'Failure', 'Success', 0.2],
        ['Failure', 'Failure', 'Failure', 0.8]
    ], [conditionals, conditional_statements])


def _get_simple_programs_probability(conditionals, conditional_statements):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 'Success', 0.9],
        ['Success', 'Success', 'Failure', 0.1],
        ['Success', 'Failure', 'Success', 0.5],
        ['Success', 'Failure', 'Failure', 0.5],
        ['Failure', 'Success', 'Success', 0.7],
        ['Failure', 'Success', 'Failure', 0.3],
        ['Failure', 'Failure', 'Success', 0.1],
        ['Failure', 'Failure', 'Failure', 0.9]
    ], [conditionals, conditional_statements])


def _get_programs_probability(conditionals, nested_conditionals, simple_programs):
    return ConditionalProbabilityTable([
        ['Success', 'Success', 'Success', 'Success', 0.9],
        ['Success', 'Success', 'Success', 'Failure', 0.1],
        ['Success', 'Success', 'Failure', 'Success', 0.7],
        ['Success', 'Success', 'Failure', 'Failure', 0.3],
        ['Success', 'Failure', 'Failure', 'Success', 0.3],
        ['Success', 'Failure', 'Failure', 'Failure', 0.7],
        ['Success', 'Failure', 'Success', 'Success', 0.5],
        ['Success', 'Failure', 'Success', 'Failure', 0.5],
        ['Failure', 'Success', 'Success', 'Success', 0.7],
        ['Failure', 'Success', 'Success', 'Failure', 0.3],
        ['Failure', 'Success', 'Failure', 'Success', 0.4],
        ['Failure', 'Success', 'Failure', 'Failure', 0.6],
        ['Failure', 'Failure', 'Success', 'Success', 0.2],
        ['Failure', 'Failure', 'Success', 'Failure', 0.8],
        ['Failure', 'Failure', 'Failure', 'Success', 0.1],
        ['Failure', 'Failure', 'Failure', 'Failure', 0.9],
    ], [conditionals, nested_conditionals, simple_programs])
