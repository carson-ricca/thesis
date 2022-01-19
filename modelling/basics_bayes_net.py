from pomegranate import *
from constants import success, failure


def generate_basics_bayesian_network():
    basics = _get_basics_probability()
    variables = _get_variables_probability(basics)
    data_types = _get_data_types_probability(basics, variables)
    statements = _get_statements_probability(basics, variables)
    constants = _get_constants_probability(basics, variables)
    arithmetic_operators = _get_arithmetic_operators_probability(variables, data_types, statements)
    casting = _get_casting_probability(basics, data_types)
    simple_calculation_problems = _get_simple_calculation_problems_probability(basics, data_types, arithmetic_operators,
                                                                               constants)

    b = Node(basics, name='Basics')
    v = Node(variables, name='Variables')
    dt = Node(data_types, name='Data Types')
    s = Node(statements, name='Statements')
    co = Node(constants, name='Constants')
    ao = Node(arithmetic_operators, name='Arithmetic Operators')
    ca = Node(casting, name='Casting')
    scp = Node(simple_calculation_problems, name='Simple Calculation Problems')

    model = BayesianNetwork('Basics')
    model.add_states(b, v, dt, s, co, ao, ca, scp)
    model.add_edge(b, v)
    model.add_edge(b, dt)
    model.add_edge(b, s)
    model.add_edge(b, co)
    model.add_edge(b, ao)
    model.add_edge(b, ca)
    model.add_edge(b, scp)
    model.add_edge(v, dt)
    model.add_edge(v, s)
    model.add_edge(v, co)
    model.add_edge(dt, ao)
    model.add_edge(dt, ca)
    model.add_edge(dt, scp)
    model.add_edge(s, ao)
    model.add_edge(ao, scp)
    model.add_edge(co, scp)
    model.bake()
    return model


def _get_basics_probability():
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_variables_probability(basics):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9]
    ], [basics])


def _get_data_types_probability(basics, variables):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], [basics, variables])


def _get_statements_probability(basics, variables):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], [basics, variables])


def _get_constants_probability(basics, variables):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], [basics, variables])


def _get_arithmetic_operators_probability(basics, data_types, statements):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.4],
        [success, failure, success, failure, 0.6],
        [success, failure, failure, success, 0.6],
        [success, failure, failure, failure, 0.4],
        [failure, success, success, success, 0.7],
        [failure, success, success, failure, 0.4],
        [failure, success, failure, success, 0.3],
        [failure, success, failure, failure, 0.7],
        [failure, failure, success, success, 0.2],
        [failure, failure, success, failure, 0.8],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9]
    ], basics, data_types, statements)


def _get_casting_probability(basics, data_types):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8]
    ], basics, data_types)


def _get_simple_calculation_problems_probability(basics, data_types, arithmetic_operators, constants):
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.9],
        [success, success, success, success, failure, 0.1],
        [success, success, success, failure, success, 0.8],
        [success, success, success, failure, failure, 0.2],
        [success, success, failure, success, success, 0.8],
        [success, success, failure, success, failure, 0.2],
        [success, success, failure, failure, success, 0.7],
        [success, success, failure, failure, failure, 0.3],
        [success, failure, success, success, success, 0.8],
        [success, failure, success, success, failure, 0.2],
        [success, failure, success, failure, success, 0.6],
        [success, failure, success, failure, failure, 0.4],
        [success, failure, failure, success, success, 0.6],
        [success, failure, failure, success, failure, 0.4],
        [success, failure, failure, failure, success, 0.2],
        [success, failure, failure, failure, failure, 0.8],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.6],
        [failure, success, success, failure, failure, 0.4],
        [failure, success, failure, success, success, 0.5],
        [failure, success, failure, success, failure, 0.5],
        [failure, success, failure, failure, success, 0.2],
        [failure, success, failure, failure, failure, 0.8],
        [failure, failure, success, success, success, 0.6],
        [failure, failure, success, success, failure, 0.4],
        [failure, failure, success, failure, success, 0.2],
        [failure, failure, success, failure, failure, 0.8],
        [failure, failure, failure, success, success, 0.3],
        [failure, failure, failure, success, failure, 0.7],
        [failure, failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, failure, 0.9],
    ], basics, data_types, arithmetic_operators, constants)
