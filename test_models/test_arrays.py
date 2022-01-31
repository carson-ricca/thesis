from matplotlib import pyplot as plt

from constants import success, failure
from modelling import generate_arrays_bayesian_network
from util import Timer


def test_arrays():
    model = generate_arrays_bayesian_network()
    # model.plot()
    # plt.show()

    _predict_success_in_arrays(model, success, success, success, success, success, success, success)
    _predict_success_in_arrays(model, failure, failure, failure, failure, failure, failure, failure)
    _predict_success_in_arrays(model, failure, failure, failure, failure, success, success, success)
    _predict_success_in_arrays(model, success, success, success, failure, failure, failure, failure)
    _predict_success_in_arrays(model, success, failure, success, failure, success, failure, success)
    _predict_success_in_arrays(model, failure, failure, success, success, success, failure, failure)
    _predict_success_in_arrays(model, failure, success, success, success, success, success, failure)


def _predict_success_in_arrays(model, data_representation, defining_arrays, referencing_arrays,
                               multidimensional_arrays, array_with_methods, programs_with_data_sequences,
                               programs_with_multidimensional_data):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Data Representation': data_representation,
        'Defining Arrays': defining_arrays,
        'Referencing Arrays': referencing_arrays,
        'Multidimensional Arrays': multidimensional_arrays,
        'Array with Methods': array_with_methods,
        'Programs with Data Sequences': programs_with_data_sequences,
        'Programs with Multidimensional Data': programs_with_multidimensional_data
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
