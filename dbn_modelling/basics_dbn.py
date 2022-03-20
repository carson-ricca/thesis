from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

basics_node_0 = ('Basics', 0)
variables_node_0 = ('Variables', 0)
data_types_node_0 = ('Data Types', 0)
statements_node_0 = ('Statements', 0)
constants_node_0 = ('Constants', 0)
arithmetic_operators_node_0 = ('Arithmetic Operators', 0)
casting_node_0 = ('Casting', 0)
simple_calculation_programs_node_0 = ('Simple Calculation Programs', 0)
basics_node_1 = ('Basics', 1)
variables_node_1 = ('Variables', 1)
data_types_node_1 = ('Data Types', 1)
statements_node_1 = ('Statements', 1)
constants_node_1 = ('Constants', 1)
arithmetic_operators_node_1 = ('Arithmetic Operators', 1)
casting_node_1 = ('Casting', 1)
simple_calculation_programs_node_1 = ('Simple Calculation Programs', 1)


def basics():
    model = DynamicBayesianNetwork([
        (basics_node_0, variables_node_0),
        (basics_node_0, data_types_node_0),
        (basics_node_0, statements_node_0),
        (basics_node_0, arithmetic_operators_node_0),
        (basics_node_0, constants_node_0),
        (basics_node_0, casting_node_0),
        (basics_node_0, simple_calculation_programs_node_0),
        (variables_node_0, data_types_node_0),
        (variables_node_0, statements_node_0),
        (variables_node_0, constants_node_0),
        (data_types_node_0, casting_node_0),
        (data_types_node_0, arithmetic_operators_node_0),
        (data_types_node_0, simple_calculation_programs_node_0),
        (statements_node_0, arithmetic_operators_node_0),
        (arithmetic_operators_node_0, simple_calculation_programs_node_0),
        (constants_node_0, simple_calculation_programs_node_0),
        (basics_node_0, basics_node_1),
        (variables_node_0, variables_node_1),
        (data_types_node_0, data_types_node_1),
        (statements_node_0, statements_node_1),
        (arithmetic_operators_node_0, arithmetic_operators_node_1),
        (constants_node_0, constants_node_1),
        (casting_node_0, casting_node_1),
        (simple_calculation_programs_node_0, simple_calculation_programs_node_1),
        (basics_node_1, variables_node_1),
        (basics_node_1, data_types_node_1),
        (basics_node_1, statements_node_1),
        (basics_node_1, arithmetic_operators_node_1),
        (basics_node_1, constants_node_1),
        (basics_node_1, casting_node_1),
        (basics_node_1, simple_calculation_programs_node_1),
        (variables_node_1, data_types_node_1),
        (variables_node_1, statements_node_1),
        (variables_node_1, constants_node_1),
        (data_types_node_1, casting_node_1),
        (data_types_node_1, arithmetic_operators_node_1),
        (data_types_node_1, simple_calculation_programs_node_1),
        (statements_node_1, arithmetic_operators_node_1),
        (arithmetic_operators_node_1, simple_calculation_programs_node_1),
        (constants_node_1, simple_calculation_programs_node_1),
    ])

    basics_cpd = TabularCPD(basics_node_0, 2, [
        [0.5], [0.5]
    ])

    variables_cpd = TabularCPD(variables_node_0, 2, [
        [0.8, 0.2],
        [0.2, 0.8]
    ], [basics_node_0], [2])

    data_types_cpd = TabularCPD(data_types_node_0, 2, [
        [0.9, 0.6, 0.6, 0.2],
        [0.1, 0.4, 0.4, 0.8]
    ], [basics_node_0, variables_node_0], [2, 2])

    statements_cpd = TabularCPD(statements_node_0, 2, [
        [0.9, 0.6, 0.6, 0.1],
        [0.1, 0.4, 0.4, 0.9]
    ], [basics_node_0, variables_node_0], [2, 2])

    constants_cpd = TabularCPD(constants_node_0, 2, [
        [0.9, 0.6, 0.6, 0.1],
        [0.1, 0.4, 0.4, 0.9]
    ], [basics_node_0, variables_node_0], [2, 2])

    arithmetic_operators_cpd = TabularCPD(arithmetic_operators_node_0, 2, [
        [0.95, 0.8, 0.4, 0.6, 0.7, 0.3, 0.2, 0.1],
        [0.05, 0.2, 0.6, 0.4, 0.3, 0.7, 0.8, 0.9]
    ], [basics_node_0, data_types_node_0, statements_node_0], [2, 2, 2])

    casting_cpd = TabularCPD(casting_node_0, 2, [
        [0.9, 0.6, 0.7, 0.2],
        [0.1, 0.4, 0.3, 0.8]
    ], [basics_node_0, data_types_node_0], [2, 2])

    simple_calculation_programs_cpd = TabularCPD(simple_calculation_programs_node_0, 2, [
        [0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.2, 0.8, 0.6, 0.5, 0.2, 0.6, 0.2, 0.3, 0.1],
        [0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.8, 0.2, 0.4, 0.5, 0.8, 0.4, 0.8, 0.7, 0.9]
    ], [basics_node_0, data_types_node_0, arithmetic_operators_node_0, constants_node_0],
                                                 [2, 2, 2, 2])

    basics_transitional_cpd = TabularCPD(basics_node_1, 2, [
        [0.8, 0.2],
        [0.2, 0.8]
    ], [basics_node_0], [2])

    variables_transitional_cpd = TabularCPD(variables_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [variables_node_0, basics_node_1], [2, 2])

    data_types_transitional_cpd = TabularCPD(data_types_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [data_types_node_0, basics_node_1, variables_node_1], [2, 2, 2])

    statements_transitional_cpd = TabularCPD(statements_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [statements_node_0, basics_node_1, variables_node_1], [2, 2, 2])

    constants_transitional_cpd = TabularCPD(constants_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [constants_node_0, basics_node_1, variables_node_1], [2, 2, 2])

    arithmetic_operators_transitional_cpd = TabularCPD(arithmetic_operators_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [arithmetic_operators_node_0, basics_node_1, data_types_node_1, statements_node_1],
                                                       [2, 2, 2, 2])

    casting_transitional_cpd = TabularCPD(casting_node_1, 2, [
        [0.9, 0.8, 0.8, 0.7, 0.8, 0.3, 0.3, 0.1],
        [0.1, 0.2, 0.2, 0.3, 0.2, 0.7, 0.7, 0.9]
    ], [casting_node_0, basics_node_1, data_types_node_1], [2, 2, 2])

    simple_calculation_programs_transitional_cpd = TabularCPD(simple_calculation_programs_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], [simple_calculation_programs_node_0, basics_node_1, data_types_node_1, arithmetic_operators_node_1,
                 constants_node_1], [2, 2, 2, 2, 2])

    model.add_cpds(basics_cpd, variables_cpd, data_types_cpd, statements_cpd, constants_cpd, arithmetic_operators_cpd,
                   casting_cpd, simple_calculation_programs_cpd, basics_transitional_cpd, variables_transitional_cpd,
                   data_types_transitional_cpd, statements_transitional_cpd, constants_transitional_cpd,
                   arithmetic_operators_transitional_cpd, casting_transitional_cpd,
                   simple_calculation_programs_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    basics_model = basics()
