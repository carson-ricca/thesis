from pomegranate import *


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
    return DiscreteDistribution({'Success': 0.5, 'Failure': 0.5})


def _get_conditionals_probability(basics):
    """
    Gets the probability for the Conditionals node.
    :param basics: The probability for the Basics node.
    :return: The probability for the Conditionals node.
    """
    return ConditionalProbabilityTable([
        ['Success', 'Success', 0.75],
        ['Success', 'Failure', 0.25],
        ['Failure', 'Success', 0.25],
        ['Failure', 'Failure', 0.75]
    ], [basics])


def _get_pre_defined_classes_probability(basics):
    """
    Gets the probability for the Pre-Defined Classes node.
    :param basics: The probability for the Basics node.
    :return: The probability for the Pre-Defined Classes node.
    """
    return ConditionalProbabilityTable([
        ['Success', 'Success', 0.75],
        ['Success', 'Failure', 0.25],
        ['Failure', 'Success', 0.25],
        ['Failure', 'Failure', 0.75]
    ], [basics])


def _get_loops_probability(conditionals):
    """
    Gets the probability for the Loops node.
    :param conditionals: The probability for the Conditionals node.
    :return: The probability for the Loops node.
    """
    return ConditionalProbabilityTable([
        ['Success', 'Success', 0.75],
        ['Success', 'Failure', 0.25],
        ['Failure', 'Success', 0.25],
        ['Failure', 'Failure', 0.75]
    ], [conditionals])


def _get_arrays_probability(loops):
    """
    Gets the probability for the Arrays node.
    :param loops: The probability for the Loops node.
    :return: The probability for the Arrays node.
    """
    return ConditionalProbabilityTable([
        ['Success', 'Success', 0.75],
        ['Success', 'Failure', 0.25],
        ['Failure', 'Success', 0.25],
        ['Failure', 'Failure', 0.75]
    ], [loops])


def _get_methods_probability(loops):
    """
    Gets the probability for the Methods node.
    :param loops: The probability for the Loops node.
    :return: The probability for the Methods node.
    """
    return ConditionalProbabilityTable([
        ['Success', 'Success', 0.75],
        ['Success', 'Failure', 0.25],
        ['Failure', 'Success', 0.25],
        ['Failure', 'Failure', 0.75]
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
        ['Success', 'Success', 'Success', 'Success', 0.9],
        ['Success', 'Success', 'Success', 'Failure', 0.1],
        ['Success', 'Success', 'Failure', 'Success', 0.75],
        ['Success', 'Success', 'Failure', 'Failure', 0.25],
        ['Success', 'Failure', 'Success', 'Success', 0.6],
        ['Success', 'Failure', 'Success', 'Failure', 0.4],
        ['Success', 'Failure', 'Failure', 'Success', 0.4],
        ['Success', 'Failure', 'Failure', 'Failure', 0.6],
        ['Failure', 'Failure', 'Failure', 'Success', 0.1],
        ['Failure', 'Failure', 'Failure', 'Failure', 0.9],
        ['Failure', 'Failure', 'Success', 'Success', 0.2],
        ['Failure', 'Failure', 'Success', 'Failure', 0.8],
        ['Failure', 'Success', 'Failure', 'Success', 0.4],
        ['Failure', 'Success', 'Failure', 'Failure', 0.6],
        ['Failure', 'Success', 'Success', 'Success', 0.75],
        ['Failure', 'Success', 'Success', 'Failure', 0.25],
    ], [arrays, methods, pre_defined_classes])
