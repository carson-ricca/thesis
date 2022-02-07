from pomegranate import *
from constants import ParentCategories, Conditionals, success, failure


def get_conditionals_nodes(conditionals):
    """
    Gets the probabilities for each node and returns the nodes.
    :param conditionals: The root conditionals' probability.
    :return: The nodes for the rest of the model.
    """
    boolean = _get_boolean_probability(conditionals)
    decision = _get_decision_probability(conditionals, boolean)
    operators = _get_operators_probability(conditionals, boolean)
    conditional_statements = _get_conditional_statements_probability(conditionals, decision, operators, boolean)
    nested_conditional_statements = _get_nested_conditional_probability(conditionals, conditional_statements)
    simple_programs = _get_simple_programs_probability(conditionals, conditional_statements)
    programs = _get_programs_probability(conditionals, nested_conditional_statements, simple_programs)

    boolean_node = State(boolean, name=Conditionals.BOOLEAN)
    decision_node = State(decision, name=Conditionals.DECISION)
    operators_node = State(operators, name=Conditionals.OPERATORS)
    conditional_statements_node = State(conditional_statements, name=Conditionals.CONDITIONAL_STATEMENTS)
    nested_conditional_statements_node = State(nested_conditional_statements, name=Conditionals.NESTED_CONDITIONAL_STATEMENTS)
    simple_programs_node = State(simple_programs, name=Conditionals.SIMPLE_PROGRAMS)
    programs_node = State(programs, name=Conditionals.PROGRAMS)

    return [boolean_node, decision_node, operators_node, conditional_statements_node,
            nested_conditional_statements_node, simple_programs_node, programs_node]


def generate_conditionals_bayesian_network():
    """
    Creates the Bayesian Network for the Conditionals sub-categories.
    :return: The complete Bayesian Network.
    """
    conditionals = _get_conditionals_probability()
    conditionals_node = State(conditionals, name=ParentCategories.CONDITIONALS)
    nodes = get_conditionals_nodes(conditionals)
    boolean_node = nodes[0]
    decision_node = nodes[1]
    operators_node = nodes[2]
    conditional_statements_node = nodes[3]
    nested_conditional_statements_node = nodes[4]
    simple_programs_node = nodes[5]
    programs_node = nodes[6]

    model = BayesianNetwork('Conditionals')
    model.add_states(conditionals_node, boolean_node, decision_node, operators_node, conditional_statements_node,
                     nested_conditional_statements_node, simple_programs_node, programs_node)
    model.add_edge(conditionals_node, boolean_node)
    model.add_edge(conditionals_node, decision_node)
    model.add_edge(conditionals_node, operators_node)
    model.add_edge(conditionals_node, conditional_statements_node)
    model.add_edge(conditionals_node, nested_conditional_statements_node)
    model.add_edge(conditionals_node, simple_programs_node)
    model.add_edge(conditionals_node, programs_node)
    model.add_edge(boolean_node, decision_node)
    model.add_edge(boolean_node, operators_node)
    model.add_edge(boolean_node, conditional_statements_node)
    model.add_edge(decision_node, conditional_statements_node)
    model.add_edge(operators_node, conditional_statements_node)
    model.add_edge(conditional_statements_node, nested_conditional_statements_node)
    model.add_edge(conditional_statements_node, simple_programs_node)
    model.add_edge(nested_conditional_statements_node, programs_node)
    model.add_edge(simple_programs_node, programs_node)
    model.bake()
    return model


def _get_conditionals_probability():
    """
    Gets the probability of the Conditionals node.
    :return: The probability of the Conditionals node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_boolean_probability(conditionals):
    """
    Gets the probability of the Boolean node.
    :param conditionals: The probability of the Conditionals node.
    :return: The probability of the Boolean node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.8],
        [success, failure, 0.2],
        [failure, success, 0.3],
        [failure, failure, 0.7]
    ], [conditionals])


def _get_decision_probability(conditionals, boolean):
    """
    Gets the probability of the Decision node.
    :param conditionals: The probability of the Conditionals node.
    :param boolean: The probability of the Boolean node.
    :return: The probability of the Decision node.
    """
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
    """
    Gets the probability of the Operators node.
    :param conditionals: The probability of the Conditionals node.
    :param boolean: The probability of the Boolean node.
    :return: The probability of the Operators node.
    """
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
    """
    Gets the probability of the Conditional Statements node.
    :param conditionals: The probability of the Conditionals node.
    :param decision: The probability of the Decision node.
    :param operators: The probability of the Operators node.
    :param boolean: The probability of the Boolean node.
    :return:
    """
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
    """
    Gets the probability of the Nested Conditional node.
    :param conditionals: The probability of the Conditionals node.
    :param conditional_statements: The probability of the Conditionals Statements node.
    :return: The probability of the Nested Conditional node.
    """
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
    """
    Gets the probability of the Simple Programs node.
    :param conditionals: The probability of the Conditionals node.
    :param conditional_statements: The probability of the Conditionals Statements node.
    :return: The probability of the Simple Programs node.
    """
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
    """
    Gets the probability of the Programs node.
    :param conditionals: The probability of the Conditionals node.
    :param nested_conditionals: The probability of the Nested Conditionals node.
    :param simple_programs: The probability of the Simple Programs node.
    :return: The probability of the Programs node.
    """
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
