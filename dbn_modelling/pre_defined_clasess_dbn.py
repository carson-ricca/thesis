from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

pre_defined_classes_node_0 = ('Pre Defined Classes', 0)
oop_overview_node_0 = ('OOP Overview', 0)
scanner_node_0 = ('Scanner', 0)
character_node_0 = ('Character', 0)
math_node_0 = ('Math', 0)
random_node_0 = ('Random', 0)
simple_programs_node_0 = ('Simple Programs', 0)
string_node_0 = ('String', 0)
math_programs_node_0 = ('Math Programs', 0)
changing_behaviour_programs_node_0 = ('Changing Behaviour Programs', 0)
user_input_programs_node_0 = ('User Input Programs', 0)
pre_defined_classes_node_1 = ('Pre Defined Classes', 1)
oop_overview_node_1 = ('OOP Overview', 1)
scanner_node_1 = ('Scanner', 1)
character_node_1 = ('Character', 1)
math_node_1 = ('Math', 1)
random_node_1 = ('Random', 1)
simple_programs_node_1 = ('Simple Programs', 1)
string_node_1 = ('String', 1)
math_programs_node_1 = ('Math Programs', 1)
changing_behaviour_programs_node_1 = ('Changing Behaviour Programs', 1)
user_input_programs_node_1 = ('User Input Programs', 1)


def pre_defined_classes():
    model = DynamicBayesianNetwork([
        (pre_defined_classes_node_0, oop_overview_node_0),
        (pre_defined_classes_node_0, scanner_node_0),
        (pre_defined_classes_node_0, character_node_0),
        (pre_defined_classes_node_0, math_node_0),
        (pre_defined_classes_node_0, random_node_0),
        (pre_defined_classes_node_0, simple_programs_node_0),
        (pre_defined_classes_node_0, string_node_0),
        (pre_defined_classes_node_0, math_programs_node_0),
        (pre_defined_classes_node_0, changing_behaviour_programs_node_0),
        (pre_defined_classes_node_0, user_input_programs_node_0),
        (oop_overview_node_0, math_node_0),
        (oop_overview_node_0, random_node_0),
        (oop_overview_node_0, scanner_node_0),
        (oop_overview_node_0, character_node_0),
        (math_node_0, math_programs_node_0),
        (random_node_0, changing_behaviour_programs_node_0),
        (character_node_0, simple_programs_node_0),
        (character_node_0, string_node_0),
        (simple_programs_node_0, user_input_programs_node_0),
        (string_node_0, user_input_programs_node_0),
        (pre_defined_classes_node_0, pre_defined_classes_node_1),
        (oop_overview_node_0, oop_overview_node_1),
        (math_node_0, math_node_1),
        (random_node_0, random_node_1),
        (math_programs_node_0, math_programs_node_1),
        (changing_behaviour_programs_node_0, changing_behaviour_programs_node_1),
        (scanner_node_0, scanner_node_1),
        (character_node_0, character_node_1),
        (simple_programs_node_0, simple_programs_node_1),
        (string_node_0, string_node_1),
        (user_input_programs_node_0, user_input_programs_node_1),
        (pre_defined_classes_node_1, oop_overview_node_1),
        (pre_defined_classes_node_1, scanner_node_1),
        (pre_defined_classes_node_1, character_node_1),
        (pre_defined_classes_node_1, math_node_1),
        (pre_defined_classes_node_1, random_node_1),
        (pre_defined_classes_node_1, simple_programs_node_1),
        (pre_defined_classes_node_1, string_node_1),
        (pre_defined_classes_node_1, math_programs_node_1),
        (pre_defined_classes_node_1, changing_behaviour_programs_node_1),
        (pre_defined_classes_node_1, user_input_programs_node_1),
        (oop_overview_node_1, math_node_1),
        (oop_overview_node_1, random_node_1),
        (oop_overview_node_1, scanner_node_1),
        (oop_overview_node_1, character_node_1),
        (math_node_1, math_programs_node_1),
        (random_node_1, changing_behaviour_programs_node_1),
        (scanner_node_1, simple_programs_node_1),
        (character_node_1, simple_programs_node_1),
        (character_node_1, string_node_1),
        (simple_programs_node_1, user_input_programs_node_1),
        (string_node_1, user_input_programs_node_1)
    ])

    pre_defined_classes_cpd = TabularCPD(pre_defined_classes_node_0, 2, [
        [0.5], [0.5]
    ])

    oop_overview_cpd = TabularCPD(oop_overview_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [pre_defined_classes_node_0], [2])

    scanner_cpd = TabularCPD(scanner_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, oop_overview_node_0], [2, 2])

    character_cpd = TabularCPD(character_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, oop_overview_node_0], [2, 2])

    math_cpd = TabularCPD(math_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, oop_overview_node_0], [2, 2])

    random_cpd = TabularCPD(random_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, oop_overview_node_0], [2, 2])

    math_programs_cpd = TabularCPD(math_programs_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, math_node_0], [2, 2])

    changing_behaviour_programs_cpd = TabularCPD(changing_behaviour_programs_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, random_node_0], [2, 2])

    simple_programs_cpd = TabularCPD(simple_programs_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [pre_defined_classes_node_0, scanner_node_0, character_node_0], [2, 2, 2])

    string_cpd = TabularCPD(string_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [pre_defined_classes_node_0, character_node_0], [2, 2])

    user_input_programs_cpd = TabularCPD(user_input_programs_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [pre_defined_classes_node_0, simple_programs_node_0, string_node_0], [2, 2, 2])

    pre_defined_classes_transitional_cpd = TabularCPD(pre_defined_classes_node_1, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [pre_defined_classes_node_0], [2])

    oop_overview_transitional_cpd = TabularCPD(oop_overview_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [oop_overview_node_0, pre_defined_classes_node_1], [2, 2])

    scanner_transitional_cpd = TabularCPD(scanner_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [scanner_node_0, pre_defined_classes_node_1, oop_overview_node_1], [2, 2, 2])

    character_transitional_cpd = TabularCPD(character_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [character_node_0, pre_defined_classes_node_1, oop_overview_node_1], [2, 2, 2])

    math_transitional_cpd = TabularCPD(math_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [math_node_0, pre_defined_classes_node_1, oop_overview_node_1], [2, 2, 2])

    random_transitional_cpd = TabularCPD(random_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [random_node_0, pre_defined_classes_node_1, oop_overview_node_1], [2, 2, 2])

    math_programs_transitional_cpd = TabularCPD(math_programs_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [math_programs_node_0, pre_defined_classes_node_1, math_node_1], [2, 2, 2])

    changing_behaviour_programs_transitional_cpd = TabularCPD(changing_behaviour_programs_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [changing_behaviour_programs_node_0, pre_defined_classes_node_1, random_node_1], [2, 2, 2])

    simple_programs_transitional_cpd = TabularCPD(simple_programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [simple_programs_node_0, pre_defined_classes_node_1, scanner_node_1, character_node_1], [2, 2, 2, 2])

    string_transitional_cpd = TabularCPD(string_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [string_node_0, pre_defined_classes_node_1, character_node_1], [2, 2, 2])

    user_input_programs_transitional_cpd = TabularCPD(user_input_programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [user_input_programs_node_0, pre_defined_classes_node_1, simple_programs_node_1, string_node_1], [2, 2, 2, 2])

    model.add_cpds(pre_defined_classes_cpd, oop_overview_cpd, scanner_cpd, character_cpd, math_cpd, random_cpd,
                   math_programs_cpd, changing_behaviour_programs_cpd, simple_programs_cpd, string_cpd,
                   user_input_programs_cpd, pre_defined_classes_transitional_cpd, oop_overview_transitional_cpd,
                   scanner_transitional_cpd, character_transitional_cpd, math_transitional_cpd, random_transitional_cpd,
                   math_programs_transitional_cpd, changing_behaviour_programs_transitional_cpd,
                   simple_programs_transitional_cpd, string_transitional_cpd, user_input_programs_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    pre_defined_classes_model = pre_defined_classes()
