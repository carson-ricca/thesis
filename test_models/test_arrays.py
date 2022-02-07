from matplotlib import pyplot as plt

from constants import ParentCategories, Arrays, success, failure
from modelling import generate_arrays_bayesian_network
from util import Timer

NODE_ORDER = {
    ParentCategories.ARRAYS: 0,
    Arrays.DATA_REPRESENTATION: 1,
    Arrays.DEFINING_ARRAYS: 2,
    Arrays.REFERENCING_ARRAYS: 3,
    Arrays.MULTIDIMENSIONAL_ARRAYS: 4,
    Arrays.ARRAYS_WITH_METHODS: 5,
    Arrays.PROGRAMS_WITH_DATA_SEQUENCES: 6,
    Arrays.PROGRAMS_WITH_MULTIDIMENSIONAL_DATA: 7
}


def test_arrays():
    model = generate_arrays_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    _predict_success_in_arrays(model, success, success, success, success, success, success, success)
    _predict_success_in_arrays(model, failure, failure, failure, failure, failure, failure, failure)
    _predict_success_in_arrays(model, failure, failure, failure, failure, success, success, success)
    _predict_success_in_arrays(model, success, success, success, failure, failure, failure, failure)
    _predict_success_in_arrays(model, success, failure, success, failure, success, failure, success)
    _predict_success_in_arrays(model, failure, failure, success, success, success, failure, failure)
    _predict_success_in_arrays(model, failure, success, success, success, success, success, failure)

    print(Arrays.PROGRAMS_WITH_MULTIDIMENSIONAL_DATA)
    _run_inference(model, {
        ParentCategories.ARRAYS: success,
        Arrays.DATA_REPRESENTATION: success,
        Arrays.DEFINING_ARRAYS: success,
        Arrays.REFERENCING_ARRAYS: success,
        Arrays.MULTIDIMENSIONAL_ARRAYS: success,
        Arrays.ARRAYS_WITH_METHODS: failure,
        Arrays.PROGRAMS_WITH_DATA_SEQUENCES: failure,
    }, Arrays.PROGRAMS_WITH_MULTIDIMENSIONAL_DATA)

    print(Arrays.DATA_REPRESENTATION)
    _run_inference(model, {
        ParentCategories.ARRAYS: success,
    }, Arrays.DATA_REPRESENTATION)

    print(Arrays.ARRAYS_WITH_METHODS)
    _run_inference(model, {
        ParentCategories.ARRAYS: success,
        Arrays.DATA_REPRESENTATION: success,
        Arrays.DEFINING_ARRAYS: failure,
        Arrays.REFERENCING_ARRAYS: failure,
        Arrays.MULTIDIMENSIONAL_ARRAYS: success,
        Arrays.PROGRAMS_WITH_DATA_SEQUENCES: success,
        Arrays.PROGRAMS_WITH_MULTIDIMENSIONAL_DATA: success
    }, Arrays.ARRAYS_WITH_METHODS)

    print(Arrays.PROGRAMS_WITH_DATA_SEQUENCES)
    _run_inference(model, {
        ParentCategories.ARRAYS: success,
        Arrays.DATA_REPRESENTATION: failure,
        Arrays.DEFINING_ARRAYS: failure,
        Arrays.REFERENCING_ARRAYS: failure,
        Arrays.MULTIDIMENSIONAL_ARRAYS: success,
        Arrays.ARRAYS_WITH_METHODS: failure,
    }, Arrays.PROGRAMS_WITH_DATA_SEQUENCES)


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _predict_success_in_arrays(model, data_representation, defining_arrays, referencing_arrays,
                               multidimensional_arrays, array_with_methods, programs_with_data_sequences,
                               programs_with_multidimensional_data):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        Arrays.DATA_REPRESENTATION: data_representation,
        Arrays.DEFINING_ARRAYS: defining_arrays,
        Arrays.REFERENCING_ARRAYS: referencing_arrays,
        Arrays.MULTIDIMENSIONAL_ARRAYS: multidimensional_arrays,
        Arrays.ARRAYS_WITH_METHODS: array_with_methods,
        Arrays.PROGRAMS_WITH_DATA_SEQUENCES: programs_with_data_sequences,
        Arrays.PROGRAMS_WITH_MULTIDIMENSIONAL_DATA: programs_with_multidimensional_data
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Data Representation: {data_representation}, Defining Arrays: {defining_arrays}, '
        f'Referencing Arrays: {referencing_arrays},\nMultidimensional Arrays: {multidimensional_arrays}, '
        f'Array with Methods: {array_with_methods}, Programs with Data Sequences: {programs_with_data_sequences},\n'
        f'Programs with Multidimensional Data: {programs_with_multidimensional_data}'
    ))
    print(f'Arrays Success: {overall_success["Success"]}, Arrays Failure: {overall_success["Failure"]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_arrays()
