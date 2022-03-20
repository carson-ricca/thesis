from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

methods_node_0 = ('Methods', 0)
abstraction_node_0 = ('Abstraction', 0)
variable_scope_node_0 = ('Variable Scope', 0)
using_methods_node_0 = ('Using Methods', 0)
defining_methods_node_0 = ('Defining Methods', 0)
method_overloading_node_0 = ('Method Overloading', 0)
modular_programs_node_0 = ('Modular Programs', 0)
methods_node_1 = ('Methods', 1)
abstraction_node_1 = ('Abstraction', 1)
variable_scope_node_1 = ('Variable Scope', 1)
using_methods_node_1 = ('Using Methods', 1)
defining_methods_node_1 = ('Defining Methods', 1)
method_overloading_node_1 = ('Method Overloading', 1)
modular_programs_node_1 = ('Modular Programs', 1)


def methods():
    model = DynamicBayesianNetwork([
        (methods_node_0, abstraction_node_0),
        (methods_node_0, variable_scope_node_0),
        (methods_node_0, using_methods_node_0),
        (methods_node_0, defining_methods_node_0),
        (methods_node_0, method_overloading_node_0),
        (methods_node_0, modular_programs_node_0),
        (abstraction_node_0, using_methods_node_0),
        (abstraction_node_0, defining_methods_node_0),
        (variable_scope_node_0, defining_methods_node_0),
        (using_methods_node_0, defining_methods_node_0),
        (defining_methods_node_0, method_overloading_node_0),
        (defining_methods_node_0, modular_programs_node_0),
        (method_overloading_node_0, modular_programs_node_0),
        (methods_node_0, methods_node_1),
        (abstraction_node_0, abstraction_node_1),
        (variable_scope_node_0, variable_scope_node_1),
        (using_methods_node_0, using_methods_node_1),
        (defining_methods_node_0, defining_methods_node_1),
        (method_overloading_node_0, method_overloading_node_1),
        (modular_programs_node_0, modular_programs_node_1),
        (methods_node_1, abstraction_node_1),
        (methods_node_1, variable_scope_node_1),
        (methods_node_1, using_methods_node_1),
        (methods_node_1, defining_methods_node_1),
        (methods_node_1, method_overloading_node_1),
        (methods_node_1, modular_programs_node_1),
        (abstraction_node_1, using_methods_node_1),
        (abstraction_node_1, defining_methods_node_1),
        (variable_scope_node_1, defining_methods_node_1),
        (using_methods_node_1, defining_methods_node_1),
        (defining_methods_node_1, method_overloading_node_1),
        (defining_methods_node_1, modular_programs_node_1),
        (method_overloading_node_1, modular_programs_node_1)
    ])

    methods_cpd = TabularCPD(methods_node_0, 2, [
        [0.5], [0.5]
    ])

    abstraction_cpd = TabularCPD(abstraction_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [methods_node_0], [2])

    variable_scope_cpd = TabularCPD(variable_scope_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [methods_node_0], [2])

    using_methods_cpd = TabularCPD(using_methods_node_0, 2, [
        [0.9, 0.7, 0.7, 0.1],
        [0.1, 0.3, 0.3, 0.9]
    ], [methods_node_0, abstraction_node_0], [2, 2])

    defining_methods_cpd = TabularCPD(defining_methods_node_0, 2, [
        [0.95, 0.7, 0.8, 0.6, 0.8, 0.7, 0.7, 0.3, 0.8, 0.7, 0.7, 0.2, 0.7, 0.4, 0.4, 0.1],
        [0.05, 0.3, 0.2, 0.4, 0.2, 0.3, 0.3, 0.7, 0.2, 0.3, 0.3, 0.8, 0.3, 0.6, 0.6, 0.9]
    ], [methods_node_0, abstraction_node_0, variable_scope_node_0, using_methods_node_0], [2, 2, 2, 2])

    method_overloading_cpd = TabularCPD(method_overloading_node_0, 2, [
        [0.9, 0.6, 0.7, 0.1],
        [0.1, 0.4, 0.3, 0.9]
    ], [methods_node_0, defining_methods_node_0], [2, 2])

    modular_programs_cpd = TabularCPD(modular_programs_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [methods_node_0, defining_methods_node_0, method_overloading_node_0], [2, 2, 2])

    methods_transitional_cpd = TabularCPD(methods_node_1, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [methods_node_0], [2])

    abstraction_transitional_cpd = TabularCPD(abstraction_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [abstraction_node_0, methods_node_1], [2, 2])

    variable_scope_transitional_cpd = TabularCPD(variable_scope_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [variable_scope_node_0, methods_node_1], [2, 2])

    using_methods_transitional_cpd = TabularCPD(using_methods_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [using_methods_node_0, methods_node_1, abstraction_node_1], [2, 2, 2])

    defining_methods_transitional_cpd = TabularCPD(defining_methods_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], [defining_methods_node_0, methods_node_1, abstraction_node_1, variable_scope_node_1, using_methods_node_1],
                                                   [2, 2, 2, 2, 2])

    method_overloading_transitional_cpd = TabularCPD(method_overloading_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [method_overloading_node_0, methods_node_1, defining_methods_node_1], [2, 2, 2])

    modular_programs_transitional_cpd = TabularCPD(modular_programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [modular_programs_node_0, methods_node_1, defining_methods_node_1, method_overloading_node_1], [2, 2, 2, 2])

    model.add_cpds(methods_cpd, abstraction_cpd, variable_scope_cpd, using_methods_cpd, defining_methods_cpd,
                   method_overloading_cpd, modular_programs_cpd, methods_transitional_cpd, abstraction_transitional_cpd,
                   variable_scope_transitional_cpd, using_methods_transitional_cpd, defining_methods_transitional_cpd,
                   method_overloading_transitional_cpd, modular_programs_transitional_cpd)

    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    methods_model = methods()
