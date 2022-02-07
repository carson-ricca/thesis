from pomegranate import *
from constants import ParentCategories
from modelling import get_arrays_nodes, get_basics_nodes, get_conditionals_nodes, get_methods_nodes, get_oop_nodes, \
    get_pre_defined_classes_nodes, get_loops_nodes
from modelling.parent_categories_bayes_net import _get_basics_probability, _get_conditionals_probability, \
    _get_pre_defined_classes_probability, _get_loops_probability, _get_arrays_probability, _get_methods_probability, \
    _get_oop_probability


def generate_complete_bayesian_network():
    """
    Generates the Bayesian Network for the complete model.
    :return: The complete Bayesian Network.
    """
    basics = _get_basics_probability()
    conditionals = _get_conditionals_probability(basics)
    pre_defined_classes = _get_pre_defined_classes_probability(basics)
    loops = _get_loops_probability(conditionals)
    arrays = _get_arrays_probability(loops)
    methods = _get_methods_probability(loops)
    oop = _get_oop_probability(arrays, methods, pre_defined_classes)

    basics_node = State(basics, name=ParentCategories.BASICS)
    conditionals_node = State(conditionals, name=ParentCategories.CONDITIONALS)
    pre_defined_classes_node = State(pre_defined_classes, name=ParentCategories.PRE_DEFINED_CLASSES)
    loops_node = State(loops, name=ParentCategories.LOOPS)
    arrays_node = State(arrays, name=ParentCategories.ARRAYS)
    methods_node = State(methods, name=ParentCategories.METHODS)
    oop_node = State(oop, name=ParentCategories.OOP)

    basics_nodes = get_basics_nodes(basics)
    basics_variables_node = basics_nodes[0]
    basics_data_types_node = basics_nodes[1]
    basics_statements_node = basics_nodes[2]
    basics_constants_node = basics_nodes[3]
    basics_arithmetic_operators_node = basics_nodes[4]
    basics_casting_node = basics_nodes[5]
    basics_simple_calculation_problems_node = basics_nodes[6]

    conditionals_nodes = get_conditionals_nodes(conditionals)
    conditionals_boolean_node = conditionals_nodes[0]
    conditionals_decision_node = conditionals_nodes[1]
    conditionals_operators_node = conditionals_nodes[2]
    conditionals_conditional_statements_node = conditionals_nodes[3]
    conditionals_nested_conditional_statements_node = conditionals_nodes[4]
    conditionals_simple_programs_node = conditionals_nodes[5]
    conditionals_programs_node = conditionals_nodes[6]

    pre_defined_classes_nodes = get_pre_defined_classes_nodes(pre_defined_classes)
    pre_defined_classes_oop_overview_node = pre_defined_classes_nodes[0]
    pre_defined_classes_scanner_node = pre_defined_classes_nodes[1]
    pre_defined_classes_character_node = pre_defined_classes_nodes[2]
    pre_defined_classes_math_node = pre_defined_classes_nodes[3]
    pre_defined_classes_random_node = pre_defined_classes_nodes[4]
    pre_defined_classes_math_programs_node = pre_defined_classes_nodes[5]
    pre_defined_classes_changing_behaviour_programs_node = pre_defined_classes_nodes[6]
    pre_defined_classes_simple_programs_node = pre_defined_classes_nodes[7]
    pre_defined_classes_string_node = pre_defined_classes_nodes[8]
    pre_defined_classes_programs_node = pre_defined_classes_nodes[9]

    loops_nodes = get_loops_nodes(loops)
    loops_repetition_node = loops_nodes[0]
    loops_variable_scope_node = loops_nodes[1]
    loops_decision_diagrams_node = loops_nodes[2]
    loops_while_loops_node = loops_nodes[3]
    loops_for_loops_node = loops_nodes[4]
    loops_simple_programs_node = loops_nodes[5]
    loops_nested_loops_node = loops_nodes[6]
    loops_programs_node = loops_nodes[7]

    arrays_nodes = get_arrays_nodes(arrays)
    arrays_data_representation_node = arrays_nodes[0]
    arrays_defining_arrays_node = arrays_nodes[1]
    arrays_referencing_arrays_node = arrays_nodes[2]
    arrays_multidimensional_arrays_node = arrays_nodes[3]
    arrays_array_with_methods_node = arrays_nodes[4]
    arrays_programs_with_data_sequences_node = arrays_nodes[5]
    arrays_programs_with_multidimensional_data_node = arrays_nodes[6]

    methods_nodes = get_methods_nodes(methods)
    methods_abstraction_node = methods_nodes[0]
    methods_variable_scope_node = methods_nodes[1]
    methods_using_methods_node = methods_nodes[2]
    methods_defining_methods_node = methods_nodes[3]
    methods_method_overloading_node = methods_nodes[4]
    methods_modular_programs_node = methods_nodes[5]

    oop_nodes = get_oop_nodes(oop)
    oop_variable_scope_node = oop_nodes[0]
    oop_oop_overview_node = oop_nodes[1]
    oop_multiple_classes_node = oop_nodes[2]
    oop_user_defined_classes_node = oop_nodes[3]
    oop_creating_objects_node = oop_nodes[4]
    oop_object_interactions_node = oop_nodes[5]
    oop_object_independence_node = oop_nodes[6]
    oop_special_class_method_node = oop_nodes[7]
    oop_simple_programs_node = oop_nodes[8]
    oop_static_modifier_node = oop_nodes[9]
    oop_programs_node = oop_nodes[10]

    model = BayesianNetwork('Learning Model')
    model.add_states(basics_node, conditionals_node, pre_defined_classes_node, loops_node, arrays_node, methods_node,
                     oop_node, basics_variables_node, basics_data_types_node, basics_statements_node,
                     basics_constants_node,
                     basics_arithmetic_operators_node, basics_casting_node, basics_simple_calculation_problems_node,
                     conditionals_boolean_node, conditionals_decision_node, conditionals_operators_node,
                     conditionals_conditional_statements_node, conditionals_nested_conditional_statements_node,
                     conditionals_simple_programs_node, conditionals_programs_node,
                     pre_defined_classes_oop_overview_node, pre_defined_classes_scanner_node,
                     pre_defined_classes_character_node,
                     pre_defined_classes_math_node, pre_defined_classes_random_node,
                     pre_defined_classes_math_programs_node,
                     pre_defined_classes_changing_behaviour_programs_node, pre_defined_classes_simple_programs_node,
                     pre_defined_classes_string_node, pre_defined_classes_programs_node,
                     loops_repetition_node, loops_variable_scope_node, loops_decision_diagrams_node,
                     loops_while_loops_node, loops_for_loops_node, loops_simple_programs_node, loops_nested_loops_node,
                     loops_programs_node,
                     arrays_data_representation_node, arrays_defining_arrays_node, arrays_referencing_arrays_node,
                     arrays_multidimensional_arrays_node, arrays_array_with_methods_node,
                     arrays_programs_with_data_sequences_node, arrays_programs_with_multidimensional_data_node,
                     methods_abstraction_node, methods_variable_scope_node, methods_using_methods_node,
                     methods_defining_methods_node, methods_method_overloading_node, methods_modular_programs_node,
                     oop_variable_scope_node, oop_oop_overview_node, oop_multiple_classes_node,
                     oop_user_defined_classes_node,
                     oop_creating_objects_node, oop_object_interactions_node, oop_object_independence_node,
                     oop_special_class_method_node, oop_simple_programs_node, oop_static_modifier_node,
                     oop_programs_node)

    # Parent categories edges.
    model.add_edge(basics_node, conditionals_node)
    model.add_edge(basics_node, pre_defined_classes_node)
    model.add_edge(conditionals_node, loops_node)
    model.add_edge(loops_node, arrays_node)
    model.add_edge(loops_node, methods_node)
    model.add_edge(arrays_node, oop_node)
    model.add_edge(methods_node, oop_node)
    model.add_edge(pre_defined_classes_node, oop_node)

    # Basics sub-category edges.
    model.add_edge(basics_node, basics_variables_node)
    model.add_edge(basics_node, basics_data_types_node)
    model.add_edge(basics_node, basics_statements_node)
    model.add_edge(basics_node, basics_constants_node)
    model.add_edge(basics_node, basics_arithmetic_operators_node)
    model.add_edge(basics_node, basics_casting_node)
    model.add_edge(basics_node, basics_simple_calculation_problems_node)
    model.add_edge(basics_variables_node, basics_data_types_node)
    model.add_edge(basics_variables_node, basics_statements_node)
    model.add_edge(basics_variables_node, basics_constants_node)
    model.add_edge(basics_data_types_node, basics_arithmetic_operators_node)
    model.add_edge(basics_data_types_node, basics_casting_node)
    model.add_edge(basics_data_types_node, basics_simple_calculation_problems_node)
    model.add_edge(basics_statements_node, basics_arithmetic_operators_node)
    model.add_edge(basics_arithmetic_operators_node, basics_simple_calculation_problems_node)
    model.add_edge(basics_constants_node, basics_simple_calculation_problems_node)

    # Conditionals sub-category edges.
    model.add_edge(conditionals_node, conditionals_boolean_node)
    model.add_edge(conditionals_node, conditionals_decision_node)
    model.add_edge(conditionals_node, conditionals_operators_node)
    model.add_edge(conditionals_node, conditionals_conditional_statements_node)
    model.add_edge(conditionals_node, conditionals_nested_conditional_statements_node)
    model.add_edge(conditionals_node, conditionals_simple_programs_node)
    model.add_edge(conditionals_node, conditionals_programs_node)
    model.add_edge(conditionals_boolean_node, conditionals_decision_node)
    model.add_edge(conditionals_boolean_node, conditionals_operators_node)
    model.add_edge(conditionals_boolean_node, conditionals_conditional_statements_node)
    model.add_edge(conditionals_decision_node, conditionals_conditional_statements_node)
    model.add_edge(conditionals_operators_node, conditionals_conditional_statements_node)
    model.add_edge(conditionals_conditional_statements_node, conditionals_nested_conditional_statements_node)
    model.add_edge(conditionals_conditional_statements_node, conditionals_simple_programs_node)
    model.add_edge(conditionals_nested_conditional_statements_node, conditionals_programs_node)
    model.add_edge(conditionals_simple_programs_node, conditionals_programs_node)

    # Pre-Defined classes sub-category edges.
    model.add_edge(pre_defined_classes_node, pre_defined_classes_oop_overview_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_scanner_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_character_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_math_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_random_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_simple_programs_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_string_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_math_programs_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_changing_behaviour_programs_node)
    model.add_edge(pre_defined_classes_node, pre_defined_classes_programs_node)
    model.add_edge(pre_defined_classes_oop_overview_node, pre_defined_classes_math_node)
    model.add_edge(pre_defined_classes_oop_overview_node, pre_defined_classes_random_node)
    model.add_edge(pre_defined_classes_oop_overview_node, pre_defined_classes_scanner_node)
    model.add_edge(pre_defined_classes_oop_overview_node, pre_defined_classes_character_node)
    model.add_edge(pre_defined_classes_math_node, pre_defined_classes_math_programs_node)
    model.add_edge(pre_defined_classes_random_node, pre_defined_classes_changing_behaviour_programs_node)
    model.add_edge(pre_defined_classes_scanner_node, pre_defined_classes_simple_programs_node)
    model.add_edge(pre_defined_classes_character_node, pre_defined_classes_simple_programs_node)
    model.add_edge(pre_defined_classes_character_node, pre_defined_classes_string_node)
    model.add_edge(pre_defined_classes_simple_programs_node, pre_defined_classes_programs_node)
    model.add_edge(pre_defined_classes_string_node, pre_defined_classes_programs_node)

    # Loops sub-category edges.
    model.add_edge(loops_node, loops_repetition_node)
    model.add_edge(loops_node, loops_decision_diagrams_node)
    model.add_edge(loops_node, loops_variable_scope_node)
    model.add_edge(loops_node, loops_for_loops_node)
    model.add_edge(loops_node, loops_while_loops_node)
    model.add_edge(loops_node, loops_nested_loops_node)
    model.add_edge(loops_node, loops_simple_programs_node)
    model.add_edge(loops_node, loops_programs_node)
    model.add_edge(loops_repetition_node, loops_while_loops_node)
    model.add_edge(loops_repetition_node, loops_decision_diagrams_node)
    model.add_edge(loops_repetition_node, loops_for_loops_node)
    model.add_edge(loops_decision_diagrams_node, loops_while_loops_node)
    model.add_edge(loops_decision_diagrams_node, loops_for_loops_node)
    model.add_edge(loops_while_loops_node, loops_simple_programs_node)
    model.add_edge(loops_while_loops_node, loops_nested_loops_node)
    model.add_edge(loops_for_loops_node, loops_simple_programs_node)
    model.add_edge(loops_for_loops_node, loops_nested_loops_node)
    model.add_edge(loops_variable_scope_node, loops_simple_programs_node)
    model.add_edge(loops_variable_scope_node, loops_nested_loops_node)
    model.add_edge(loops_simple_programs_node, loops_programs_node)
    model.add_edge(loops_nested_loops_node, loops_programs_node)

    # Arrays sub-category edges.
    model.add_edge(arrays_node, arrays_data_representation_node)
    model.add_edge(arrays_node, arrays_defining_arrays_node)
    model.add_edge(arrays_node, arrays_referencing_arrays_node)
    model.add_edge(arrays_node, arrays_multidimensional_arrays_node)
    model.add_edge(arrays_node, arrays_array_with_methods_node)
    model.add_edge(arrays_node, arrays_programs_with_data_sequences_node)
    model.add_edge(arrays_node, arrays_programs_with_multidimensional_data_node)
    model.add_edge(arrays_data_representation_node, arrays_defining_arrays_node)
    model.add_edge(arrays_data_representation_node, arrays_referencing_arrays_node)
    model.add_edge(arrays_data_representation_node, arrays_multidimensional_arrays_node)
    model.add_edge(arrays_defining_arrays_node, arrays_referencing_arrays_node)
    model.add_edge(arrays_defining_arrays_node, arrays_multidimensional_arrays_node)
    model.add_edge(arrays_referencing_arrays_node, arrays_array_with_methods_node)
    model.add_edge(arrays_referencing_arrays_node, arrays_programs_with_data_sequences_node)
    model.add_edge(arrays_multidimensional_arrays_node, arrays_array_with_methods_node)
    model.add_edge(arrays_multidimensional_arrays_node, arrays_programs_with_multidimensional_data_node)
    model.add_edge(arrays_array_with_methods_node, arrays_programs_with_data_sequences_node)
    model.add_edge(arrays_array_with_methods_node, arrays_programs_with_multidimensional_data_node)
    model.add_edge(arrays_programs_with_data_sequences_node, arrays_programs_with_multidimensional_data_node)

    # Methods sub-category edges.
    model.add_edge(methods_node, methods_abstraction_node)
    model.add_edge(methods_node, methods_variable_scope_node)
    model.add_edge(methods_node, methods_using_methods_node)
    model.add_edge(methods_node, methods_defining_methods_node)
    model.add_edge(methods_node, methods_method_overloading_node)
    model.add_edge(methods_node, methods_modular_programs_node)
    model.add_edge(methods_abstraction_node, methods_using_methods_node)
    model.add_edge(methods_abstraction_node, methods_defining_methods_node)
    model.add_edge(methods_variable_scope_node, methods_defining_methods_node)
    model.add_edge(methods_using_methods_node, methods_defining_methods_node)
    model.add_edge(methods_defining_methods_node, methods_method_overloading_node)
    model.add_edge(methods_defining_methods_node, methods_modular_programs_node)
    model.add_edge(methods_method_overloading_node, methods_modular_programs_node)

    # OOP sub-category edges.
    model.add_edge(oop_node, oop_variable_scope_node)
    model.add_edge(oop_node, oop_oop_overview_node)
    model.add_edge(oop_node, oop_multiple_classes_node)
    model.add_edge(oop_node, oop_user_defined_classes_node)
    model.add_edge(oop_node, oop_creating_objects_node)
    model.add_edge(oop_node, oop_object_interactions_node)
    model.add_edge(oop_node, oop_object_independence_node)
    model.add_edge(oop_node, oop_special_class_method_node)
    model.add_edge(oop_node, oop_simple_programs_node)
    model.add_edge(oop_node, oop_static_modifier_node)
    model.add_edge(oop_node, oop_programs_node)
    model.add_edge(oop_variable_scope_node, oop_multiple_classes_node)
    model.add_edge(oop_variable_scope_node, oop_user_defined_classes_node)
    model.add_edge(oop_oop_overview_node, oop_multiple_classes_node)
    model.add_edge(oop_oop_overview_node, oop_user_defined_classes_node)
    model.add_edge(oop_multiple_classes_node, oop_creating_objects_node)
    model.add_edge(oop_user_defined_classes_node, oop_creating_objects_node)
    model.add_edge(oop_user_defined_classes_node, oop_special_class_method_node)
    model.add_edge(oop_creating_objects_node, oop_object_independence_node)
    model.add_edge(oop_object_interactions_node, oop_simple_programs_node)
    model.add_edge(oop_object_independence_node, oop_simple_programs_node)
    model.add_edge(oop_special_class_method_node, oop_simple_programs_node)
    model.add_edge(oop_simple_programs_node, oop_programs_node)
    model.add_edge(oop_static_modifier_node, oop_programs_node)

    model.bake()
    return model
