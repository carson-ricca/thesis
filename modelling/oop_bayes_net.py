from pomegranate import *

from constants import success, failure


def generate_oop_bayesian_network():
    oop = _get_oop_probability()
    variable_scope = _get_variable_scope_probability(oop)
    oop_overview = _get_oop_overview_scope_probability(oop)
    multiple_classes = _get_multiple_classes_probability(oop, variable_scope, oop_overview)
    user_defined_classes = _get_user_defined_classes_probability(oop, variable_scope, oop_overview)
    creating_objects = _get_creating_objects_probability(oop, multiple_classes, user_defined_classes)
    object_interactions = _get_object_interactions_probability(oop)
    object_independence = _get_object_independence_probability(oop, creating_objects)
    special_class_method = _get_special_class_method_probability(oop, user_defined_classes)
    simple_programs = _get_simple_programs_probability(oop, object_interactions, object_independence,
                                                       special_class_method)
    static_modifier = _get_static_modifier_probability(oop)
    programs = _get_programs_probability(oop, simple_programs, static_modifier)

    oop_node = State(oop, name='OOP')
    variable_scope_node = State(variable_scope, name='Variable Scope')
    oop_overview_node = State(oop_overview, name='OOP Overview')
    multiple_classes_node = State(multiple_classes, name='Multiple Classes')
    user_defined_classes_node = State(user_defined_classes, name='User Defined Classes')
    creating_objects_node = State(creating_objects, name='Creating Objects')
    object_interactions_node = State(object_interactions, name='Object Interactions')
    object_independence_node = State(object_independence, name='Object Independence')
    special_class_method_node = State(special_class_method, name='Special Class Method')
    simple_programs_node = State(simple_programs, name='Simple Programs Node')
    static_modifier_node = State(static_modifier, name='Static Modifier')
    programs_node = State(programs, name='Programs')

    model = BayesianNetwork('OOP')
    model.add_states(oop_node, variable_scope_node, oop_overview_node, multiple_classes_node, user_defined_classes_node,
                     creating_objects_node, object_interactions_node, object_independence_node,
                     special_class_method_node, simple_programs_node, static_modifier_node, programs_node)
    model.add_edge(oop_node, variable_scope_node)
    model.add_edge(oop_node, oop_overview_node)
    model.add_edge(oop_node, multiple_classes_node)
    model.add_edge(oop_node, user_defined_classes_node)
    model.add_edge(oop_node, creating_objects_node)
    model.add_edge(oop_node, object_interactions_node)
    model.add_edge(oop_node, object_independence_node)
    model.add_edge(oop_node, special_class_method_node)
    model.add_edge(oop_node, simple_programs_node)
    model.add_edge(oop_node, static_modifier_node)
    model.add_edge(oop_node, programs_node)
    model.add_edge(variable_scope_node, multiple_classes_node)
    model.add_edge(variable_scope_node, user_defined_classes_node)
    model.add_edge(oop_overview_node, multiple_classes_node)
    model.add_edge(oop_overview_node, user_defined_classes_node)
    model.add_edge(multiple_classes_node, creating_objects_node)
    model.add_edge(user_defined_classes_node, creating_objects_node)
    model.add_edge(user_defined_classes_node, special_class_method_node)
    model.add_edge(creating_objects_node, object_independence_node)
    model.add_edge(object_interactions_node, simple_programs_node)
    model.add_edge(object_independence_node, simple_programs_node)
    model.add_edge(special_class_method_node, simple_programs_node)
    model.add_edge(simple_programs_node, programs_node)
    model.add_edge(static_modifier_node, programs_node)
    model.bake()
    return model


def _get_oop_probability():
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_variable_scope_probability(oop):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [oop])


def _get_oop_overview_scope_probability(oop):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [oop])


def _get_multiple_classes_probability(oop, variable_scope, oop_overview):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.8],
        [success, failure, success, failure, 0.2],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, success, success, success, 0.8],
        [failure, success, success, failure, 0.2],
        [failure, success, failure, success, 0.6],
        [failure, success, failure, failure, 0.4],
        [failure, failure, success, success, 0.5],
        [failure, failure, success, failure, 0.5],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [oop, variable_scope, oop_overview])


def _get_user_defined_classes_probability(oop, variable_scope, oop_overview):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.8],
        [success, failure, success, failure, 0.2],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, success, success, success, 0.8],
        [failure, success, success, failure, 0.2],
        [failure, success, failure, success, 0.6],
        [failure, success, failure, failure, 0.4],
        [failure, failure, success, success, 0.5],
        [failure, failure, success, failure, 0.5],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [oop, variable_scope, oop_overview])


def _get_creating_objects_probability(oop, multiple_classes, user_defined_classes):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.8],
        [success, failure, success, failure, 0.2],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, success, success, success, 0.8],
        [failure, success, success, failure, 0.2],
        [failure, success, failure, success, 0.6],
        [failure, success, failure, failure, 0.4],
        [failure, failure, success, success, 0.5],
        [failure, failure, success, failure, 0.5],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [oop, multiple_classes, user_defined_classes])


def _get_object_interactions_probability(oop):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [oop])


def _get_object_independence_probability(oop, creating_objects):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [oop, creating_objects])


def _get_special_class_method_probability(oop, user_defined_classes):
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.6],
        [success, failure, failure, 0.4],
        [failure, success, success, 0.7],
        [failure, success, failure, 0.3],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [oop, user_defined_classes])


def _get_simple_programs_probability(oop, object_interactions, object_independence, special_class_method):
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.95],
        [success, success, success, success, failure, 0.05],
        [success, success, success, failure, success, 0.8],
        [success, success, success, failure, failure, 0.2],
        [success, success, failure, success, success, 0.8],
        [success, success, failure, success, failure, 0.2],
        [success, success, failure, failure, success, 0.6],
        [success, success, failure, failure, failure, 0.4],
        [success, failure, success, success, success, 0.8],
        [success, failure, success, success, failure, 0.2],
        [success, failure, success, failure, success, 0.6],
        [success, failure, success, failure, failure, 0.4],
        [success, failure, failure, success, success, 0.6],
        [success, failure, failure, success, failure, 0.4],
        [success, failure, failure, failure, success, 0.3],
        [success, failure, failure, failure, failure, 0.7],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.6],
        [failure, success, success, failure, failure, 0.4],
        [failure, success, failure, success, success, 0.6],
        [failure, success, failure, success, failure, 0.4],
        [failure, success, failure, failure, success, 0.3],
        [failure, success, failure, failure, failure, 0.7],
        [failure, failure, success, success, success, 0.6],
        [failure, failure, success, success, failure, 0.4],
        [failure, failure, success, failure, success, 0.3],
        [failure, failure, success, failure, failure, 0.7],
        [failure, failure, failure, success, success, 0.3],
        [failure, failure, failure, success, failure, 0.7],
        [failure, failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, failure, 0.9],
    ], [oop, object_interactions, object_independence, special_class_method])


def _get_static_modifier_probability(oop):
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9],
    ], [oop])


def _get_programs_probability(oop, simple_programs, static_modifier):
    return ConditionalProbabilityTable([
        [success, success, success, success, 0.95],
        [success, success, success, failure, 0.05],
        [success, success, failure, success, 0.8],
        [success, success, failure, failure, 0.2],
        [success, failure, success, success, 0.6],
        [success, failure, success, failure, 0.4],
        [success, failure, failure, success, 0.4],
        [success, failure, failure, failure, 0.6],
        [failure, success, success, success, 0.8],
        [failure, success, success, failure, 0.2],
        [failure, success, failure, success, 0.6],
        [failure, success, failure, failure, 0.4],
        [failure, failure, success, success, 0.4],
        [failure, failure, success, failure, 0.6],
        [failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, 0.9],
    ], [oop, simple_programs, static_modifier])