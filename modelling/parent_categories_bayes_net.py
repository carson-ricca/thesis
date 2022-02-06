from pomegranate import *
from constants import success, failure


def generate_parent_categories_bayesian_network():
    """
    Creates the Bayesian Network for the parent categories.
    :return: The complete Bayesian Network.
    """
    basics = _get_basics_probability()
    conditionals = _get_conditionals_probability(basics)
    pre_defined_classes = _get_pre_defined_classes_probability(basics)
    loops = _get_loops_probability(conditionals)
    arrays = _get_arrays_probability(loops)
    methods = _get_methods_probability(loops)
    oop = _get_oop_probability(arrays, methods, pre_defined_classes)

    basics_node = State(basics, name='Basics')
    conditionals_node = State(conditionals, name='Conditionals')
    pre_defined_classes_node = State(pre_defined_classes, name='Pre-Defined Classes')
    loops_node = State(loops, name='Loops')
    arrays_node = State(arrays, name='Arrays')
    methods_node = State(methods, name='Methods')
    oop_node = State(oop, name='OOP')

    model = BayesianNetwork('Parent Categories')
    model.add_states(basics_node, conditionals_node, pre_defined_classes_node, loops_node, arrays_node, methods_node,
                     oop_node)
    model.add_edge(basics_node, conditionals_node)
    model.add_edge(basics_node, pre_defined_classes_node)
    model.add_edge(conditionals_node, loops_node)
    model.add_edge(loops_node, arrays_node)
    model.add_edge(loops_node, methods_node)
    model.add_edge(arrays_node, oop_node)
    model.add_edge(methods_node, oop_node)
    model.add_edge(pre_defined_classes_node, oop_node)
    model.bake()
    return model


def _get_basics_probability():
    """
    Gets the probability for the Basics node.
    :return: The probability of the Basics node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_conditionals_probability(basics):
    """
    Gets the probability for the Conditionals node.
    :param basics: The probability for the Basics node.
    :return: The probability for the Conditionals node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.75],
        [success, failure, 0.25],
        [failure, success, 0.25],
        [failure, failure, 0.75]
    ], [basics])


def _get_pre_defined_classes_probability(basics):
    """
    Gets the probability for the Pre-Defined Classes node.
    :param basics: The probability for the Basics node.
    :return: The probability for the Pre-Defined Classes node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.75],
        [success, failure, 0.25],
        [failure, success, 0.25],
        [failure, failure, 0.75]
    ], [basics])


def _get_loops_probability(conditionals):
    """
    Gets the probability for the Loops node.
    :param conditionals: The probability for the Conditionals node.
    :return: The probability for the Loops node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.75],
        [success, failure, 0.25],
        [failure, success, 0.25],
        [failure, failure, 0.75]
    ], [conditionals])


def _get_arrays_probability(loops):
    """
    Gets the probability for the Arrays node.
    :param loops: The probability for the Loops node.
    :return: The probability for the Arrays node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.75],
        [success, failure, 0.25],
        [failure, success, 0.25],
        [failure, failure, 0.75]
    ], [loops])


def _get_methods_probability(loops):
    """
    Gets the probability for the Methods node.
    :param loops: The probability for the Loops node.
    :return: The probability for the Methods node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.75],
        [success, failure, 0.25],
        [failure, success, 0.25],
        [failure, failure, 0.75]
    ], [loops])


def _get_oop_probability(arrays, methods, pre_defined_classes):
    """
    Gets the probability for the OOP node.
    :param arrays: The probability for the Arrays node.
    :param methods: The probability for the Methods node.
    :param pre_defined_classes: The probability for the Pre-Defined Classes node.
    :return: The probability for the OOP node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.9],
        [success, success, success, failure, 0.1],
        [success, success, failure, success, 0.75],
        [success, success, failure, failure, 0.25],
        [success, failure, success, success, 0.6],
        [success, failure, success, failure, 0.4],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
        [failure, failure, success, success, 0.2],
        [failure, failure, success, failure, 0.8],
        [failure, success, failure, success, 0.4],
        [failure, success, failure, failure, 0.6],
        [failure, success, success, success, 0.75],
        [failure, success, success, failure, 0.25],
    ], [arrays, methods, pre_defined_classes])
