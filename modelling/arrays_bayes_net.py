from pomegranate import *

from constants import success, failure


def generate_arrays_bayesian_network():
    """
    Creates the Bayesian Network for the Arrays sub-category.
    :return: The complete Bayesian Network.
    """
    arrays = _get_arrays_probability()
    data_representation = _get_data_representation_probability(arrays)
    defining_arrays = _get_defining_arrays_probability(arrays, data_representation)
    referencing_arrays = _get_referencing_arrays_probability(arrays, defining_arrays, data_representation)
    multidimensional_arrays = _get_multidimensional_arrays_probability(arrays, defining_arrays, data_representation)
    array_with_methods = _get_array_with_methods_probability(arrays, referencing_arrays, multidimensional_arrays)
    programs_with_data_sequences = _get_programs_with_data_sequences_probability(arrays, referencing_arrays,
                                                                                 array_with_methods)
    programs_with_multidimensional_data = _get_programs_with_multidimensional_data_probability(
        arrays,
        programs_with_data_sequences,
        array_with_methods,
        multidimensional_arrays)

    arrays_node = State(arrays, name='Arrays')
    data_representation_node = State(data_representation, name='Data Representation')
    defining_arrays_node = State(defining_arrays, name='Defining Arrays')
    referencing_arrays_node = State(referencing_arrays, name='Referencing Arrays')
    multidimensional_arrays_node = State(multidimensional_arrays, name='Multidimensional Arrays')
    array_with_methods_node = State(array_with_methods, name='Array with Methods')
    programs_with_data_sequences_node = State(programs_with_data_sequences, name='Programs with Data Sequences')
    programs_with_multidimensional_data_node = State(programs_with_multidimensional_data,
                                                     name='Programs with Multidimensional Data')

    model = BayesianNetwork('Arrays')
    model.add_states(arrays_node, data_representation_node, defining_arrays_node, referencing_arrays_node,
                     multidimensional_arrays_node, array_with_methods_node, programs_with_data_sequences_node,
                     programs_with_multidimensional_data_node)
    model.add_edge(arrays_node, data_representation_node)
    model.add_edge(arrays_node, defining_arrays_node)
    model.add_edge(arrays_node, referencing_arrays_node)
    model.add_edge(arrays_node, multidimensional_arrays_node)
    model.add_edge(arrays_node, array_with_methods_node)
    model.add_edge(arrays_node, programs_with_data_sequences_node)
    model.add_edge(arrays_node, programs_with_multidimensional_data_node)
    model.add_edge(data_representation_node, defining_arrays_node)
    model.add_edge(data_representation_node, referencing_arrays_node)
    model.add_edge(data_representation_node, multidimensional_arrays_node)
    model.add_edge(defining_arrays_node, referencing_arrays_node)
    model.add_edge(defining_arrays_node, multidimensional_arrays_node)
    model.add_edge(referencing_arrays_node, array_with_methods_node)
    model.add_edge(referencing_arrays_node, programs_with_data_sequences_node)
    model.add_edge(multidimensional_arrays_node, array_with_methods_node)
    model.add_edge(multidimensional_arrays_node, programs_with_multidimensional_data_node)
    model.add_edge(array_with_methods_node, programs_with_data_sequences_node)
    model.add_edge(array_with_methods_node, programs_with_multidimensional_data_node)
    model.add_edge(programs_with_data_sequences_node, programs_with_multidimensional_data_node)
    model.bake()
    return model


def _get_arrays_probability():
    """
    Gets the probability for the Arrays node.
    :return: The probability for the Arrays node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_data_representation_probability(arrays):
    """
    Gets the probability for the Data Representation node.
    :param arrays: The probability of the Arrays node.
    :return: The probability for the Data Representation node.
    """
    return ConditionalProbabilityTable([
        [success, success, 0.9],
        [success, failure, 0.1],
        [failure, success, 0.1],
        [failure, failure, 0.9]
    ], [arrays])


def _get_defining_arrays_probability(arrays, data_representation):
    """
    Gets the probability for the Defining Arrays node.
    :param arrays: The probability of the Arrays node.
    :param data_representation: The probability of the Data Representation node.
    :return: The probability for the Defining Arrays node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, 0.9],
        [success, success, failure, 0.1],
        [success, failure, success, 0.7],
        [success, failure, failure, 0.3],
        [failure, success, success, 0.6],
        [failure, success, failure, 0.4],
        [failure, failure, success, 0.1],
        [failure, failure, failure, 0.9],
    ], [arrays, data_representation])


def _get_referencing_arrays_probability(arrays, defining_arrays, data_representation):
    """
    Gets the probability for the Referencing Arrays node.
    :param arrays: The probability of the Arrays node.
    :param defining_arrays: The probability of the Defining Arrays node.
    :param data_representation: The probability of the Data Representation node.
    :return: The probability for the Referencing Arrays node.
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
    ], [arrays, defining_arrays, data_representation])


def _get_multidimensional_arrays_probability(arrays, defining_arrays, data_representation):
    """
    Gets the probability for the Multidimensional Arrays node.
    :param arrays: The probability of the Arrays node.
    :param defining_arrays: The probability of the Defining Arrays node.
    :param data_representation: The probability of the Data Representation node.
    :return: The probability for the Multidimensional Arrays node.
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
    ], [arrays, defining_arrays, data_representation])


def _get_array_with_methods_probability(arrays, referencing_arrays, multidimensional_arrays):
    """
    Gets the probability for the Array with Methods node.
    :param arrays: The probability of the Arrays node.
    :param referencing_arrays: The probability of the Referencing Arrays node.
    :param multidimensional_arrays: The probability of the Multidimensional Arrays node.
    :return: The probability for the Arrays with Methods node.
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
    ], [arrays, referencing_arrays, multidimensional_arrays])


def _get_programs_with_data_sequences_probability(arrays, referencing_arrays, array_with_methods):
    """
    Gets the probability for the Programs with Data Sequences node.
    :param arrays: The probability of the Arrays node.
    :param referencing_arrays: The probability of the Referencing Arrays node.
    :param array_with_methods: The probability of the Arrays with Methods node.
    :return: The probability for the Programs with Data Sequences node.
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
    ], [arrays, referencing_arrays, array_with_methods])


def _get_programs_with_multidimensional_data_probability(arrays, programs_with_data_sequences, arrays_with_methods,
                                                         multidimensional_arrays):
    """
    Gets the probability for the Multidimensional Arrays node.
    :param arrays: The probability of the Arrays node.
    :param programs_with_data_sequences: The probability of the Programs with Data Sequences node.
    :param arrays_with_methods: The probability of the Arrays with Methods node.
    :param multidimensional_arrays: THe probability of the Multidimensional Arrays node.
    :return: The probability for the Multidimensional Arrays node.
    """
    return ConditionalProbabilityTable([
        [success, success, success, success, success, 0.95],
        [success, success, success, success, failure, 0.05],
        [success, success, success, failure, success, 0.7],
        [success, success, success, failure, failure, 0.3],
        [success, success, failure, success, success, 0.8],
        [success, success, failure, success, failure, 0.2],
        [success, success, failure, failure, success, 0.6],
        [success, success, failure, failure, failure, 0.4],
        [success, failure, success, success, success, 0.8],
        [success, failure, success, success, failure, 0.2],
        [success, failure, success, failure, success, 0.7],
        [success, failure, success, failure, failure, 0.3],
        [success, failure, failure, success, success, 0.7],
        [success, failure, failure, success, failure, 0.3],
        [success, failure, failure, failure, success, 0.3],
        [success, failure, failure, failure, failure, 0.7],
        [failure, success, success, success, success, 0.8],
        [failure, success, success, success, failure, 0.2],
        [failure, success, success, failure, success, 0.7],
        [failure, success, success, failure, failure, 0.3],
        [failure, success, failure, success, success, 0.7],
        [failure, success, failure, success, failure, 0.3],
        [failure, success, failure, failure, success, 0.2],
        [failure, success, failure, failure, failure, 0.8],
        [failure, failure, success, success, success, 0.7],
        [failure, failure, success, success, failure, 0.3],
        [failure, failure, success, failure, success, 0.4],
        [failure, failure, success, failure, failure, 0.6],
        [failure, failure, failure, success, success, 0.4],
        [failure, failure, failure, success, failure, 0.6],
        [failure, failure, failure, failure, success, 0.1],
        [failure, failure, failure, failure, failure, 0.9],
    ], [arrays, programs_with_data_sequences, arrays_with_methods, multidimensional_arrays])
