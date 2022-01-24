from pomegranate import *

from constants import success, failure


def generate_pre_defined_classes_bayesian_network():
    pre_defined_classes = _get_pre_defined_classes_probability()
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

    pre_defined_classes_node = State(pre_defined_classes, name='Pre-Defined Classes')
    oop_overview_node = State(oop_overview, name='OOP Overview')
    scanner_node = State(scanner, name='Scanner')
    character_node = State(character, name='Character')
    math_node = State(math, name='Math')
    random_node = State(random, name='Random')
    math_programs_node = State(math_programs, name='Math Programs')
    changing_behaviour_programs_node = State(changing_behaviour_programs, name='Changing Behaviours Programs')
    simple_programs_node = State(simple_programs, name='Simple Programs')
    string_node = State(string, name='String')
    programs_node = State(programs, name='Programs')

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
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_oop_overview_probability(pre_defined_classes):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [pre_defined_classes])


def _get_scanner_probability(pre_defined_classes, oop_overview):
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