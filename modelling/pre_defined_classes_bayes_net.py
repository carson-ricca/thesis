from pomegranate import *

from constants import success, failure


def get_pre_defined_classes_nodes(pre_defined_classes):
    """
    Gets the probabilities for each node and returns the nodes.
    :param pre_defined_classes: The root Pre-Defined Classes' probability.
    :return: The nodes for the rest of the model.
    """
    oop_overview = _get_oop_overview_probability(pre_defined_classes)
    scanner = _get_scanner_probability(pre_defined_classes, oop_overview)
    character = _get_character_probability(pre_defined_classes, oop_overview)
    math = _get_math_probability(pre_defined_classes, oop_overview)
    random = _get_random_probability(pre_defined_classes, oop_overview)
    math_programs = _get_math_programs_probability(pre_defined_classes, math)
    changing_behaviour_programs = _get_changing_behaviour_programs_probability(pre_defined_classes, random)
    simple_programs = _get_simple_programs_probability(pre_defined_classes, scanner, character)
    string = _get_string_probability(pre_defined_classes, character)
    programs = _get_programs_probability(pre_defined_classes, simple_programs, string)

    oop_overview_node = State(oop_overview, name='OOP Overview')
    scanner_node = State(scanner, name='Scanner')
    character_node = State(character, name='Character')
    math_node = State(math, name='Math')
    random_node = State(random, name='Random')
    math_programs_node = State(math_programs, name='Math Programs')
    changing_behaviour_programs_node = State(changing_behaviour_programs, name='Changing Behaviour Programs')
    simple_programs_node = State(simple_programs, name='Simple Programs')
    string_node = State(string, name='String')
    programs_node = State(programs, name='Programs')
    return [oop_overview_node, scanner_node, character_node, math_node, random_node, math_programs_node,
            changing_behaviour_programs_node, simple_programs_node, string_node, programs_node]


def generate_pre_defined_classes_bayesian_network():
    """
    Creates the Bayesian Network for the Pre-Defined Classes sub-categories.
    :return: The complete Bayesian Network.
    """
    pre_defined_classes = _get_pre_defined_classes_probability()
    pre_defined_classes_node = State(pre_defined_classes, name='Pre-Defined Classes')
    nodes = get_pre_defined_classes_nodes(pre_defined_classes)
    oop_overview_node = nodes[0]
    scanner_node = nodes[1]
    character_node = nodes[2]
    math_node = nodes[3]
    random_node = nodes[4]
    math_programs_node = nodes[5]
    changing_behaviour_programs_node = nodes[6]
    simple_programs_node = nodes[7]
    string_node = nodes[8]
    programs_node = nodes[9]

    model = BayesianNetwork('Pre-Defined Classes')
    model.add_states(pre_defined_classes_node, oop_overview_node, scanner_node, character_node, math_node, random_node,
                     math_programs_node, changing_behaviour_programs_node, simple_programs_node, string_node,
                     programs_node)
    model.add_edge(pre_defined_classes_node, oop_overview_node)
    model.add_edge(pre_defined_classes_node, scanner_node)
    model.add_edge(pre_defined_classes_node, character_node)
    model.add_edge(pre_defined_classes_node, math_node)
    model.add_edge(pre_defined_classes_node, random_node)
    model.add_edge(pre_defined_classes_node, simple_programs_node)
    model.add_edge(pre_defined_classes_node, string_node)
    model.add_edge(pre_defined_classes_node, math_programs_node)
    model.add_edge(pre_defined_classes_node, changing_behaviour_programs_node)
    model.add_edge(pre_defined_classes_node, programs_node)
    model.add_edge(oop_overview_node, math_node)
    model.add_edge(oop_overview_node, random_node)
    model.add_edge(oop_overview_node, scanner_node)
    model.add_edge(oop_overview_node, character_node)
    model.add_edge(math_node, math_programs_node)
    model.add_edge(random_node, changing_behaviour_programs_node)
    model.add_edge(scanner_node, simple_programs_node)
    model.add_edge(character_node, simple_programs_node)
    model.add_edge(character_node, string_node)
    model.add_edge(simple_programs_node, programs_node)
    model.add_edge(string_node, programs_node)
    model.bake()
    return model


def _get_pre_defined_classes_probability():
    """
    Gets the probability of the Pre-Defined Classes node.
    :return: The probability of the Pre-Defined Classes node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_oop_overview_probability(pre_defined_classes):
    """
    Gets the probability of the OOP Overview node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :return: The probability of the OOP Overview node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [pre_defined_classes])


def _get_scanner_probability(pre_defined_classes, oop_overview):
    """
    Gets the probability of the Scanner node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param oop_overview: The probability of the OOP Overview node.
    :return: The probability of the Scanner node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, oop_overview])


def _get_character_probability(pre_defined_classes, oop_overview):
    """
    Gets the probability of the Character node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param oop_overview: The probability of the OOP Overview node.
    :return: The probability of the Character node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, oop_overview])


def _get_math_probability(pre_defined_classes, oop_overview):
    """
    Gets the probability of the Math node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param oop_overview: The probability of the OOP Overview node.
    :return: The probability of the Math node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, oop_overview])


def _get_random_probability(pre_defined_classes, oop_overview):
    """
    Gets the probability of the Random node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param oop_overview: The probability of the OOP Overview node.
    :return: The probability of the Random node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, oop_overview])


def _get_math_programs_probability(pre_defined_classes, math):
    """
    Gets the probability of the Math Programs node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param math: The probability of the Math node.
    :return: The probability of the Math Programs node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, math])


def _get_changing_behaviour_programs_probability(pre_defined_classes, random):
    """
    Gets the probability of the Changing Behaviour Programs node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param random: The probability of the Math node.
    :return: The probability of the Changing Behaviour Programs node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, random])


def _get_simple_programs_probability(pre_defined_classes, scanner, character):
    """
    Gets the probability of the Simple Programs node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param scanner: The probability of the Scanner node.
    :param character: The probability of the Character node.
    :return: The probability of the Simple Programs node.
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
    ], [pre_defined_classes, scanner, character])


def _get_string_probability(pre_defined_classes, character):
    """
    Gets the probability of the String node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param character: The probability of the Character node.
    :return: The probability of the String node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [pre_defined_classes, character])


def _get_programs_probability(pre_defined_classes, simple_programs, string):
    """
    Gets the probability of the Programs node.
    :param pre_defined_classes: The probability of the Pre-Defined Classes node.
    :param simple_programs: The probability of the Simple Programs node.
    :param string: The probability of the String node.
    :return: The probability of the Programs node.
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
    ], [pre_defined_classes, simple_programs, string])
