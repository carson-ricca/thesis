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

    s1 = Node(basics, name='Basics')
    s2 = Node(conditionals, name='Conditionals')
    s3 = Node(pre_defined_classes, name='Pre-Defined Classes')
    s4 = Node(loops, name='Loops')
    s5 = Node(arrays, name='Arrays')
    s6 = Node(methods, name='Methods')
    s7 = Node(oop, name='OOP')

    model = BayesianNetwork('Parent Categories')
    model.add_states(s1, s2, s3, s4, s5, s6, s7)
    model.add_edge(s1, s2)
    model.add_edge(s1, s3)
    model.add_edge(s2, s4)
    model.add_edge(s4, s5)
    model.add_edge(s4, s6)
    model.add_edge(s5, s7)
    model.add_edge(s6, s7)
    model.add_edge(s3, s7)
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
