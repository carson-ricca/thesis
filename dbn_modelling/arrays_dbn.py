from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import DynamicBayesianNetwork

arrays_node_0 = ('Arrays', 0)
data_representation_node_0 = ('Data Representation', 0)
defining_arrays_node_0 = ('Defining Arrays', 0)
referencing_arrays_node_0 = ('Referencing Arrays', 0)
multidimensional_arrays_node_0 = ('Multidimensional Arrays', 0)
arrays_with_methods_node_0 = ('Arrays with Methods', 0)
programs_with_data_sequences_node_0 = ('Programs with Data Sequences', 0)
programs_with_multidimensional_data_node_0 = ('Programs with Multidimensional Data', 0)
arrays_node_1 = ('Arrays', 1)
data_representation_node_1 = ('Data Representation', 1)
defining_arrays_node_1 = ('Defining Arrays', 1)
referencing_arrays_node_1 = ('Referencing Arrays', 1)
multidimensional_arrays_node_1 = ('Multidimensional Arrays', 1)
arrays_with_methods_node_1 = ('Arrays with Methods', 1)
programs_with_data_sequences_node_1 = ('Programs with Data Sequences', 1)
programs_with_multidimensional_data_node_1 = ('Programs with Multidimensional Data', 1)


def arrays():
    model = DynamicBayesianNetwork([
        (arrays_node_0, data_representation_node_0),
        (arrays_node_0, defining_arrays_node_0),
        (arrays_node_0, referencing_arrays_node_0),
        (arrays_node_0, multidimensional_arrays_node_0),
        (arrays_node_0, arrays_with_methods_node_0),
        (arrays_node_0, programs_with_data_sequences_node_0),
        (arrays_node_0, programs_with_multidimensional_data_node_0),
        (data_representation_node_0, defining_arrays_node_0),
        (data_representation_node_0, referencing_arrays_node_0),
        (data_representation_node_0, multidimensional_arrays_node_0),
        (defining_arrays_node_0, referencing_arrays_node_0),
        (defining_arrays_node_0, multidimensional_arrays_node_0),
        (referencing_arrays_node_0, arrays_with_methods_node_0),
        (referencing_arrays_node_0, programs_with_data_sequences_node_0),
        (multidimensional_arrays_node_0, arrays_with_methods_node_0),
        (multidimensional_arrays_node_0, programs_with_multidimensional_data_node_0),
        (arrays_with_methods_node_0, programs_with_data_sequences_node_0),
        (arrays_with_methods_node_0, programs_with_multidimensional_data_node_0),
        (programs_with_data_sequences_node_0, programs_with_multidimensional_data_node_0),
        (arrays_node_0, arrays_node_1),
        (data_representation_node_0, data_representation_node_1),
        (defining_arrays_node_0, defining_arrays_node_1),
        (referencing_arrays_node_0, referencing_arrays_node_1),
        (multidimensional_arrays_node_0, multidimensional_arrays_node_1),
        (arrays_with_methods_node_0, arrays_with_methods_node_1),
        (programs_with_data_sequences_node_0, programs_with_data_sequences_node_1),
        (programs_with_multidimensional_data_node_0, programs_with_multidimensional_data_node_1),
        (arrays_node_1, data_representation_node_1),
        (arrays_node_1, defining_arrays_node_1),
        (arrays_node_1, referencing_arrays_node_1),
        (arrays_node_1, multidimensional_arrays_node_1),
        (arrays_node_1, arrays_with_methods_node_1),
        (arrays_node_1, programs_with_data_sequences_node_1),
        (arrays_node_1, programs_with_multidimensional_data_node_1),
        (data_representation_node_1, defining_arrays_node_1),
        (data_representation_node_1, referencing_arrays_node_1),
        (data_representation_node_1, multidimensional_arrays_node_1),
        (defining_arrays_node_1, referencing_arrays_node_1),
        (defining_arrays_node_1, multidimensional_arrays_node_1),
        (referencing_arrays_node_1, arrays_with_methods_node_1),
        (referencing_arrays_node_1, programs_with_data_sequences_node_1),
        (multidimensional_arrays_node_1, arrays_with_methods_node_1),
        (multidimensional_arrays_node_1, programs_with_multidimensional_data_node_1),
        (arrays_with_methods_node_1, programs_with_data_sequences_node_1),
        (arrays_with_methods_node_1, programs_with_multidimensional_data_node_1),
        (programs_with_data_sequences_node_1, programs_with_multidimensional_data_node_1)
    ])

    arrays_cpd = TabularCPD(arrays_node_0, 2, [
        [0.5], [0.5]
    ])

    data_representation_cpd = TabularCPD(data_representation_node_0, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [arrays_node_0], [2])

    defining_arrays_cpd = TabularCPD(defining_arrays_node_0, 2, [
        [0.9, 0.7, 0.6, 0.1],
        [0.1, 0.3, 0.4, 0.9]
    ], [arrays_node_0, data_representation_node_0], [2, 2])

    referencing_arrays_cpd = TabularCPD(referencing_arrays_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [arrays_node_0, defining_arrays_node_0, data_representation_node_0], [2, 2, 2])

    multidimensional_arrays_cpd = TabularCPD(multidimensional_arrays_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [arrays_node_0, defining_arrays_node_0, data_representation_node_0], [2, 2, 2])

    arrays_with_methods_cpd = TabularCPD(arrays_with_methods_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [arrays_node_0, referencing_arrays_node_0, multidimensional_arrays_node_0], [2, 2, 2])

    programs_with_data_sequences_cpd = TabularCPD(programs_with_data_sequences_node_0, 2, [
        [0.9, 0.7, 0.7, 0.3, 0.8, 0.4, 0.4, 0.1],
        [0.1, 0.3, 0.3, 0.7, 0.2, 0.6, 0.6, 0.9]
    ], [arrays_node_0, referencing_arrays_node_0, arrays_with_methods_node_0], [2, 2, 2])

    programs_with_multidimensional_data_cpd = TabularCPD(programs_with_multidimensional_data_node_0, 2, [
        [0.95, 0.7, 0.8, 0.6, 0.8, 0.7, 0.7, 0.3, 0.8, 0.7, 0.7, 0.2, 0.7, 0.4, 0.4, 0.1],
        [0.05, 0.3, 0.2, 0.4, 0.2, 0.3, 0.3, 0.7, 0.2, 0.3, 0.3, 0.8, 0.3, 0.6, 0.6, 0.9]
    ], [arrays_node_0, programs_with_data_sequences_node_0, arrays_with_methods_node_0, multidimensional_arrays_node_0],
                                                         [2, 2, 2, 2])

    arrays_transitional_cpd = TabularCPD(arrays_node_1, 2, [
        [0.9, 0.1],
        [0.1, 0.9]
    ], [arrays_node_0], [2])

    data_representation_transitional_cpd = TabularCPD(data_representation_node_1, 2, [
        [0.9, 0.8, 0.8, 0.1],
        [0.1, 0.2, 0.2, 0.9]
    ], [data_representation_node_0, arrays_node_1], [2, 2])

    defining_arrays_transitional_cpd = TabularCPD(defining_arrays_node_1, 2, [
        [0.9, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.1],
        [0.1, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.9]
    ], [defining_arrays_node_0, arrays_node_1, data_representation_node_1], [2, 2, 2])

    referencing_arrays_transitional_cpd = TabularCPD(referencing_arrays_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [referencing_arrays_node_0, arrays_node_1, defining_arrays_node_1, data_representation_node_1], [2, 2, 2, 2])

    multidimensional_arrays_transitional_cpd = TabularCPD(multidimensional_arrays_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [multidimensional_arrays_node_0, arrays_node_1, defining_arrays_node_1, data_representation_node_1],
                                                          [2, 2, 2, 2])

    arrays_with_methods_transitional_cpd = TabularCPD(arrays_with_methods_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [arrays_with_methods_node_0, arrays_node_1, defining_arrays_node_1, data_representation_node_1],
                                                      [2, 2, 2, 2])

    programs_with_data_sequences_transitional_cpd = TabularCPD(programs_with_data_sequences_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.6, 0.6, 0.3, 0.6, 0.3, 0.3, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.4, 0.4, 0.7, 0.4, 0.7, 0.7, 0.9]
    ], [arrays_with_methods_node_0, arrays_node_1, referencing_arrays_node_1, arrays_with_methods_node_1],
                                                               [2, 2, 2, 2])

    programs_with_multidimensional_data_transitional_cpd = TabularCPD(programs_with_multidimensional_data_node_1, 2, [
        [0.9, 0.9, 0.9, 0.8, 0.9, 0.8, 0.8, 0.7, 0.8, 0.8, 0.8, 0.7, 0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.4, 0.7, 0.4,
         0.4, 0.2, 0.7, 0.4, 0.4, 0.2, 0.4, 0.3, 0.2, 0.1],
        [0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.6, 0.3, 0.6,
         0.6, 0.8, 0.3, 0.6, 0.6, 0.8, 0.6, 0.7, 0.8, 0.9]
    ], [programs_with_multidimensional_data_node_0, arrays_node_1, programs_with_data_sequences_node_1,
        arrays_with_methods_node_1, multidimensional_arrays_node_1], [2, 2, 2, 2, 2])

    model.add_cpds(arrays_cpd, data_representation_cpd, defining_arrays_cpd, referencing_arrays_cpd,
                   multidimensional_arrays_cpd, arrays_with_methods_cpd, programs_with_data_sequences_cpd,
                   programs_with_multidimensional_data_cpd, arrays_transitional_cpd,
                   data_representation_transitional_cpd, defining_arrays_transitional_cpd,
                   referencing_arrays_transitional_cpd, multidimensional_arrays_transitional_cpd,
                   arrays_with_methods_transitional_cpd, programs_with_data_sequences_transitional_cpd,
                   programs_with_multidimensional_data_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    arrays_model = arrays()
