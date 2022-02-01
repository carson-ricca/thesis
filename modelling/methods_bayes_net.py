from pomegranate import *

from constants import success, failure


def generate_methods_bayesian_network():
    """
    Creates the Bayesian Network for the Methods sub-category.
    :return: The complete Bayesian Network.
    """
    methods = _get_methods_probability()
    abstraction = _get_abstraction_probability(methods)
    variable_scope = _get_variable_scope_probability(methods)
    using_methods = _get_using_methods_probability(methods, abstraction)
    defining_methods = _get_defining_methods_probability(methods, abstraction, variable_scope, using_methods)
    method_overloading = _get_method_overloading_probability(methods, defining_methods)
    modular_programs = _get_modular_programs_probability(methods, defining_methods, method_overloading)

    methods_node = State(methods, name='Methods')
    abstraction_node = State(abstraction, name='Abstraction')
    variable_scope_node = State(variable_scope, name='Variable Scope')
    using_methods_node = State(using_methods, name='Using Methods')
    defining_methods_node = State(defining_methods, name='Defining Methods')
    method_overloading_node = State(method_overloading, name='Method Overloading')
    modular_programs_node = State(modular_programs, name='Modular Programs')

    model = BayesianNetwork('Methods')
    model.add_states(methods_node, abstraction_node, variable_scope_node, using_methods_node, defining_methods_node,
                     method_overloading_node, modular_programs_node)
    model.add_edge(methods_node, abstraction_node)
    model.add_edge(methods_node, variable_scope_node)
    model.add_edge(methods_node, using_methods_node)
    model.add_edge(methods_node, defining_methods_node)
    model.add_edge(methods_node, method_overloading_node)
    model.add_edge(methods_node, modular_programs_node)
    model.add_edge(abstraction_node, using_methods_node)
    model.add_edge(abstraction_node, defining_methods_node)
    model.add_edge(variable_scope_node, defining_methods_node)
    model.add_edge(using_methods_node, defining_methods_node)
    model.add_edge(defining_methods_node, method_overloading_node)
    model.add_edge(defining_methods_node, modular_programs_node)
    model.add_edge(method_overloading_node, modular_programs_node)
    model.bake()
    return model


def _get_methods_probability():
    """
    Gets the probability of the Methods node.
    :return: The probability of the Methods node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_abstraction_probability(methods):
    """
    Gets the probability of the Abstraction node.
    :param methods: The probability of the Methods node.
    :return: The probability of the Abstraction node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9]
    ], [methods])


def _get_variable_scope_probability(methods):
    """
    Gets the probability of the Variable Scope node.
    :param methods: The probability of the Methods node.
    :return: The probability of the Variable Scope node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9]
    ], [methods])


def _get_using_methods_probability(methods, abstraction):
    """
    Gets the probability of the Using Methods node.
    :param methods: The probability of the Methods node.
    :param abstraction: The probability of the Abstraction node.
    :return: The probability of the Using Methods node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9]
    ], [methods, abstraction])


def _get_defining_methods_probability(methods, abstraction, variable_scope, using_methods):
    """
    Gets the probability of the Defining Methods node.
    :param methods: The probability of the Methods node.
    :param abstraction: The probability of the Abstraction node.
    :param variable_scope: The probability of the Variable Scope node.
    :param using_methods: The probability of the Using Methods node.
    :return: The probability of the Defining Methods node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.95],
        [success, success, success, success, failure, 0.05],
        [success, success, success, failure, success, 0.7],
        [success, success, success, failure, failure, 0.3],
        [success, success, failure, success, success, 0.8],
        [success, success, failure, success, failure, 0.2],
        [success, success, failure, failure, success, 0.6],
        [success, success, failure, failure, failure, 0.4],
        [success, failure, success, success, success, 0.8],
        [success, failure, success, success, failure, 0.2],
        [success, failure, success, failure, success, 0.7],
        [success, failure, success, failure, failure, 0.3],
        [success, failure, failure, success, success, 0.7],
        [success, failure, failure, success, failure, 0.3],
        [success, failure, failure, failure, success, 0.3],
        [success, failure, failure, failure, failure, 0.7],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.7],
        [failure, success, success, failure, failure, 0.3],
        [failure, success, failure, success, success, 0.7],
        [failure, success, failure, success, failure, 0.3],
        [failure, success, failure, failure, success, 0.2],
        [failure, success, failure, failure, failure, 0.8],
        [failure, failure, success, success, success, 0.7],
        [failure, failure, success, success, failure, 0.3],
        [failure, failure, success, failure, success, 0.4],
        [failure, failure, success, failure, failure, 0.6],
        [failure, failure, failure, success, success, 0.4],
        [failure, failure, failure, success, failure, 0.6],
        [failure, failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, failure, 0.9]
    ], [methods, abstraction, variable_scope, using_methods])


def _get_method_overloading_probability(methods, defining_methods):
    """
    Gets the probability of the Method Overloading node.
    :param methods: The probability of the Methods node.
    :param defining_methods: The probability of the Defining Methods node.
    :return: The probability of the Method Overloading node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9]
    ], [methods, defining_methods])


def _get_modular_programs_probability(methods, defining_methods, method_overloading):
    """
    Gets the probability of the Modular Programs node.
    :param methods: The probability of the Methods node.
    :param defining_methods: The probability of the Defining Methods node.
    :param method_overloading: The probability of the Method Overloading node.
    :return: The probability of the Modular Programs node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.9],
        [success, success, success, failure, 0.1],
        [success, success, failure, success, 0.7],
        [success, success, failure, failure, 0.3],
        [success, failure, success, success, 0.7],
        [success, failure, success, failure, 0.3],
        [success, failure, failure, success, 0.3],
        [success, failure, failure, failure, 0.7],
        [failure, success, success, success, 0.8],
        [failure, success, success, failure, 0.2],
        [failure, success, failure, success, 0.4],
        [failure, success, failure, failure, 0.6],
        [failure, failure, success, success, 0.4],
        [failure, failure, success, failure, 0.6],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [methods, defining_methods, method_overloading])
