from pomegranate import *
from constants import success, failure


def get_basics_nodes(basics):
    """
    Gets the probabilities for each node and returns the nodes.
    :param basics: The root Basics' probability.
    :return: The nodes for the rest of the model.
    """
    variables = _get_variables_probability(basics)
    data_types = _get_data_types_probability(basics, variables)
    statements = _get_statements_probability(basics, variables)
    constants = _get_constants_probability(basics, variables)
    arithmetic_operators = _get_arithmetic_operators_probability(basics, data_types, statements)
    casting = _get_casting_probability(basics, data_types)
    simple_calculation_problems = _get_simple_calculation_problems_probability(basics, data_types, arithmetic_operators,
                                                                               constants)

    variables_node = State(variables, name='Variables')
    data_types_node = State(data_types, name='Data Types')
    statements_node = State(statements, name='Statements')
    constants_node = State(constants, name='Constants')
    arithmetic_operators_node = State(arithmetic_operators, name='Arithmetic Operators')
    casting_node = State(casting, name='Casting')
    simple_calculation_problems_node = State(simple_calculation_problems, name='Simple Calculation Problems')

    return [variables_node, data_types_node, statements_node, constants_node, arithmetic_operators_node, casting_node,
            simple_calculation_problems_node]


def generate_basics_bayesian_network():
    """
    Creates the Bayesian Network for the Basics sub-categories.
    :return: The complete Bayesian Network.
    """
    basics = _get_basics_probability()
    basics_node = State(basics, name='Basics')
    nodes = get_basics_nodes(basics)
    variables_node = nodes[0]
    data_types_node = nodes[1]
    statements_node = nodes[2]
    constants_node = nodes[3]
    arithmetic_operators_node = nodes[4]
    casting_node = nodes[5]
    simple_calculation_problems_node = nodes[6]

    model = BayesianNetwork('Basics')
    model.add_states(basics_node, variables_node, data_types_node, statements_node, constants_node,
                     arithmetic_operators_node, casting_node, simple_calculation_problems_node)
    model.add_edge(basics_node, variables_node)
    model.add_edge(basics_node, data_types_node)
    model.add_edge(basics_node, statements_node)
    model.add_edge(basics_node, constants_node)
    model.add_edge(basics_node, arithmetic_operators_node)
    model.add_edge(basics_node, casting_node)
    model.add_edge(basics_node, simple_calculation_problems_node)
    model.add_edge(variables_node, data_types_node)
    model.add_edge(variables_node, statements_node)
    model.add_edge(variables_node, constants_node)
    model.add_edge(data_types_node, arithmetic_operators_node)
    model.add_edge(data_types_node, casting_node)
    model.add_edge(data_types_node, simple_calculation_problems_node)
    model.add_edge(statements_node, arithmetic_operators_node)
    model.add_edge(arithmetic_operators_node, simple_calculation_problems_node)
    model.add_edge(constants_node, simple_calculation_problems_node)
    model.bake()
    return model


def _get_basics_probability():
    """
    Gets the probability of the Basics node.
    :return: The probability of the Basics node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_variables_probability(basics):
    """
    Gets the probability of the Variables node.
    :param basics: The probability of the Basics node.
    :return: The probability of the Variables node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [basics])


def _get_data_types_probability(basics, variables):
    """
    Gets the probability of the Data Types node.
    :param basics: The probability of the Basics node.
    :param variables: The probability of the Variables node.
    :return: The probability of the Data Types node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8],
    ], [basics, variables])


def _get_statements_probability(basics, variables):
    """
    Gets the probability of the Statements node.
    :param basics: The probability of the Basics node.
    :param variables: The probability of the Variables node.
    :return: The probability of the Statements node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [basics, variables])


def _get_constants_probability(basics, variables):
    """
    Gets the probability of the Constants node.
    :param basics: The probability of the Basics node.
    :param variables: The probability of the Variables node.
    :return: The probability of the Constants node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [basics, variables])


def _get_arithmetic_operators_probability(basics, data_types, statements):
    """
    Gets the probability of the Arithmetic Operators node.
    :param basics: The probability of the Basics node.
    :param data_types: The probability of the Data Types node.
    :param statements: The probability of the Statements node.
    :return: The probability of the Arithmetic Operators node.
    """
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
        [failure, success, success, failure, 0.3],
        [failure, success, failure, success, 0.3],
        [failure, success, failure, failure, 0.7],
        [failure, failure, success, success, 0.2],
        [failure, failure, success, failure, 0.8],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [basics, data_types, statements])


def _get_casting_probability(basics, data_types):
    """
    Gets the probability of the Casting node.
    :param basics: The probability of the Basics node.
    :param data_types: The probability of the Data Types node.
    :return: The probability of the Casting node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.2],
        [failure, failure, failure, 0.8],
    ], [basics, data_types])


def _get_simple_calculation_problems_probability(basics, data_types, arithmetic_operators, constants):
    """
    Gets the probability of the Simple Calculation Problems node.
    :param basics: The probability of the Basics node.
    :param data_types: The probability of the Data Types node.
    :param arithmetic_operators: The probability of the Arithmetic Operators node.
    :param constants: The probability of the Constants node.
    :return: The probability of the Simple Calculation Problems node.
    """
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
    ], [basics, data_types, arithmetic_operators, constants])
