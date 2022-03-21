from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

oop_node_0 = ('OOP', 0)
variable_scope_node_0 = ('Variable Scope', 0)
oop_overview_node_0 = ('OOP Overview', 0)
multiple_classes_node_0 = ('Multiple Classes', 0)
user_defined_classes_node_0 = ('User Defined Classes', 0)
creating_objects_node_0 = ('Creating Objects', 0)
object_interactions_node_0 = ('Object Interaction', 0)
object_independence_node_0 = ('Object Independence', 0)
special_class_method_node_0 = ('Special Class Method', 0)
simple_programs_node_0 = ('Simple Programs', 0)
static_modifier_node_0 = ('Static Modifier', 0)
programs_node_0 = ('Programs', 0)
oop_node_1 = ('OOP', 1)
variable_scope_node_1 = ('Variable Scope', 1)
oop_overview_node_1 = ('OOP Overview', 1)
multiple_classes_node_1 = ('Multiple Classes', 1)
user_defined_classes_node_1 = ('User Defined Classes', 1)
creating_objects_node_1 = ('Creating Objects', 1)
object_interactions_node_1 = ('Object Interaction', 1)
object_independence_node_1 = ('Object Independence', 1)
special_class_method_node_1 = ('Special Class Method', 1)
simple_programs_node_1 = ('Simple Programs', 1)
static_modifier_node_1 = ('Static Modifier', 1)
programs_node_1 = ('Programs', 1)


def oop():
    model = DynamicBayesianNetwork([
        (oop_node_0, variable_scope_node_0),
        (oop_node_0, oop_overview_node_0),
        (oop_node_0, multiple_classes_node_0),
        (oop_node_0, user_defined_classes_node_0),
        (oop_node_0, creating_objects_node_0),
        (oop_node_0, object_interactions_node_0),
        (oop_node_0, object_independence_node_0),
        (oop_node_0, special_class_method_node_0),
        (oop_node_0, simple_programs_node_0),
        (oop_node_0, static_modifier_node_0),
        (oop_node_0, programs_node_0),
        (variable_scope_node_0, multiple_classes_node_0),
        (variable_scope_node_0, user_defined_classes_node_0),
        (oop_overview_node_0, multiple_classes_node_0),
        (oop_overview_node_0, user_defined_classes_node_0),
        (multiple_classes_node_0, creating_objects_node_0),
        (user_defined_classes_node_0, creating_objects_node_0),
        (user_defined_classes_node_0, special_class_method_node_0),
        (creating_objects_node_0, object_independence_node_0),
        (object_interactions_node_0, simple_programs_node_0),
        (object_independence_node_0, simple_programs_node_0),
        (special_class_method_node_0, simple_programs_node_0),
        (simple_programs_node_0, programs_node_0),
        (static_modifier_node_0, programs_node_0),
        (oop_node_0, oop_node_1),
        (variable_scope_node_0, variable_scope_node_1),
        (oop_overview_node_0, oop_overview_node_1),
        (multiple_classes_node_0, multiple_classes_node_1),
        (user_defined_classes_node_0, user_defined_classes_node_1),
        (creating_objects_node_0, creating_objects_node_1),
        (object_interactions_node_0, object_interactions_node_1),
        (object_independence_node_0, object_independence_node_1),
        (special_class_method_node_0, special_class_method_node_1),
        (simple_programs_node_0, simple_programs_node_1),
        (static_modifier_node_0, static_modifier_node_1),
        (programs_node_0, programs_node_1),
        (oop_node_1, variable_scope_node_1),
        (oop_node_1, oop_overview_node_1),
        (oop_node_1, multiple_classes_node_1),
        (oop_node_1, user_defined_classes_node_1),
        (oop_node_1, creating_objects_node_1),
        (oop_node_1, object_interactions_node_1),
        (oop_node_1, object_independence_node_1),
        (oop_node_1, special_class_method_node_1),
        (oop_node_1, simple_programs_node_1),
        (oop_node_1, static_modifier_node_1),
        (oop_node_1, programs_node_1),
        (variable_scope_node_1, multiple_classes_node_1),
        (variable_scope_node_1, user_defined_classes_node_1),
        (oop_overview_node_1, multiple_classes_node_1),
        (oop_overview_node_1, user_defined_classes_node_1),
        (multiple_classes_node_1, creating_objects_node_1),
        (user_defined_classes_node_1, creating_objects_node_1),
        (user_defined_classes_node_1, special_class_method_node_1),
        (creating_objects_node_1, object_independence_node_1),
        (object_interactions_node_1, simple_programs_node_1),
        (object_independence_node_1, simple_programs_node_1),
        (special_class_method_node_1, simple_programs_node_1),
        (simple_programs_node_1, programs_node_1),
        (static_modifier_node_1, programs_node_1)
    ])

    oop_cpd = TabularCPD(oop_node_0, 2, [
        [0.5], [0.5]
    ])

    variable_scope_cpd = TabularCPD(variable_scope_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [oop_node_0], [2])

    oop_overview_cpd = TabularCPD(oop_overview_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [oop_node_0], [2])

    multiple_classes_cpd = TabularCPD(multiple_classes_node_0, 2, [
        [0.95, 0.8, 0.8, 0.4, 0.8, 0.6, 0.5, 0.1],
        [0.05, 0.2, 0.2, 0.6, 0.2, 0.4, 0.5, 0.9]
    ], [oop_node_0, variable_scope_node_0, oop_overview_node_0], [2, 2, 2])

    user_defined_classes_cpd = TabularCPD(user_defined_classes_node_0, 2, [
        [0.95, 0.8, 0.8, 0.4, 0.8, 0.6, 0.5, 0.1],
        [0.05, 0.2, 0.2, 0.6, 0.2, 0.4, 0.5, 0.9]
    ], [oop_node_0, variable_scope_node_0, oop_overview_node_0], [2, 2, 2])

    creating_objects_cpd = TabularCPD(creating_objects_node_0, 2, [
        [0.95, 0.8, 0.8, 0.4, 0.8, 0.6, 0.5, 0.1],
        [0.05, 0.2, 0.2, 0.6, 0.2, 0.4, 0.5, 0.9]
    ], [oop_node_0, multiple_classes_node_0, user_defined_classes_node_0], [2, 2, 2])

    object_interactions_cpd = TabularCPD(object_interactions_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [oop_node_0], [2])

    object_independence_cpd = TabularCPD(object_independence_node_0, 2, [
        [0.9, 0.6, 0.7, 0.1],
        [0.1, 0.4, 0.3, 0.9]
    ], [oop_node_0, creating_objects_node_0], [2, 2])

    special_class_method_cpd = TabularCPD(special_class_method_node_0, 2, [
        [0.9, 0.6, 0.7, 0.1],
        [0.1, 0.4, 0.3, 0.9]
    ], [oop_node_0, user_defined_classes_node_0], [2, 2])

    simple_programs_cpd = TabularCPD(simple_programs_node_0, 2, [
        [0.95, 0.8, 0.8, 0.6, 0.8, 0.6, 0.6, 0.3, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.05, 0.2, 0.2, 0.4, 0.2, 0.4, 0.4, 0.7, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [oop_node_0, object_interactions_node_0, object_independence_node_0, special_class_method_node_0], [2, 2, 2, 2])

    static_modifier_cpd = TabularCPD(static_modifier_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [oop_node_0], [2])

    programs_cpd = TabularCPD(programs_node_0, 2, [
        [0.95, 0.8, 0.6, 0.4, 0.8, 0.6, 0.4, 0.1],
        [0.05, 0.2, 0.4, 0.6, 0.2, 0.4, 0.6, 0.9]
    ], [oop_node_0, simple_programs_node_0, static_modifier_node_0], [2, 2, 2])

    oop_transitional_cpd = TabularCPD(oop_node_1, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [oop_node_0], [2])

    variable_scope_transitional_cpd = TabularCPD(variable_scope_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [variable_scope_node_0, oop_node_1], [2, 2])

    oop_overview_transitional_cpd = TabularCPD(oop_overview_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [oop_overview_node_0, oop_node_1], [2, 2])

    multiple_classes_transitional_cpd = TabularCPD(multiple_classes_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [multiple_classes_node_0, oop_node_1, variable_scope_node_1, oop_overview_node_1], [2, 2, 2, 2])

    user_defined_classes_transitional_cpd = TabularCPD(user_defined_classes_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [user_defined_classes_node_0, oop_node_1, variable_scope_node_1, oop_overview_node_1], [2, 2, 2, 2])

    creating_objects_transitional_cpd = TabularCPD(creating_objects_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [creating_objects_node_0, oop_node_1, multiple_classes_node_1, user_defined_classes_node_1], [2, 2, 2, 2])

    object_interactions_transitional_cpd = TabularCPD(object_interactions_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [object_interactions_node_0, oop_node_1], [2, 2])

    object_independence_transitional_cpd = TabularCPD(object_independence_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [object_independence_node_0, oop_node_1, creating_objects_node_1], [2, 2, 2])

    special_class_method_transitional_cpd = TabularCPD(special_class_method_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [special_class_method_node_0, oop_node_1, user_defined_classes_node_1], [2, 2, 2])

    simple_programs_transitional_cpd = TabularCPD(simple_programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], [simple_programs_node_0, oop_node_1, object_interactions_node_1, object_independence_node_1,
        special_class_method_node_1], [2, 2, 2, 2, 2])

    static_modifier_transitional_cpd = TabularCPD(static_modifier_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [static_modifier_node_0, oop_node_1], [2, 2])

    programs_transitional_cpd = TabularCPD(programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [programs_node_0, oop_node_1, simple_programs_node_1, static_modifier_node_1], [2, 2, 2, 2])

    model.add_cpds(oop_cpd, variable_scope_cpd, oop_overview_cpd, multiple_classes_cpd, user_defined_classes_cpd,
                   creating_objects_cpd, object_interactions_cpd, object_independence_cpd, special_class_method_cpd,
                   simple_programs_cpd, static_modifier_cpd, programs_cpd, oop_transitional_cpd,
                   variable_scope_transitional_cpd, oop_overview_transitional_cpd, multiple_classes_transitional_cpd,
                   user_defined_classes_transitional_cpd, creating_objects_transitional_cpd,
                   object_interactions_transitional_cpd, object_independence_transitional_cpd,
                   special_class_method_transitional_cpd, simple_programs_transitional_cpd,
                   static_modifier_transitional_cpd, programs_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    oop_model = oop()
