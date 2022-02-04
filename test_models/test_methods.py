from matplotlib import pyplot as plt

from constants import success, failure
from modelling import generate_methods_bayesian_network
from util import Timer

NODE_ORDER = {
    'Methods': 0,
    'Abstraction': 1,
    'Variable Scope': 2,
    'Using Methods': 3,
    'Defining Methods': 4,
    'Method Overloading': 5,
    'Modular Programs': 6
}


def test_methods():
    model = generate_methods_bayesian_network()
    # model.plot()
    # plt.show()

    _predict_success_in_loops(model, success, success, success, success, success, success)
    _predict_success_in_loops(model, failure, failure, failure, failure, failure, failure)
    _predict_success_in_loops(model, failure, failure, failure, success, success, success)
    _predict_success_in_loops(model, success, success, success, failure, failure, failure)
    _predict_success_in_loops(model, failure, success, failure, success, failure, success)
    _predict_success_in_loops(model, failure, success, success, success, success, failure)

    print('Methods')
    _run_inference(model, {
        'Abstraction': success,
        'Variable Scope': success,
        'Using Methods': success,
        'Defining Methods': success,
        'Method Overloading': success,
        'Modular Programs': failure,
    }, 'Methods')

    print('Methods')
    _run_inference(model, {
        'Abstraction': failure,
        'Variable Scope': failure,
        'Using Methods': failure,
        'Defining Methods': failure,
        'Method Overloading': failure,
        'Modular Programs': failure,
    }, 'Methods')

    print('Modular Programs')
    _run_inference(model, {
        'Using Methods': success,
        'Defining Methods': failure,
        'Method Overloading': success,
    }, 'Modular Programs')

    print('Defining Methods')
    _run_inference(model, {
        'Methods': failure,
        'Abstraction': success,
        'Variable Scope': failure,
        'Using Methods': success,
        'Method Overloading': failure,
        'Modular Programs': failure,
    }, 'Defining Methods')


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _predict_success_in_loops(model, abstraction, variable_scope, using_methods, defining_methods, method_overloading,
                              modular_programs):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Abstraction': abstraction,
        'Variable Scope': variable_scope,
        'Using Methods': using_methods,
        'Defining Methods': defining_methods,
        'Method Overloading': method_overloading,
        'Modular Programs': modular_programs,
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Abstraction: {abstraction}, Variable Scope: {variable_scope}, '
        f'Using Methods: {using_methods},\nDefining Methods: {defining_methods}, '
        f'Method Overloading: {method_overloading}, Modular Programs: {modular_programs}'
    ))
    print(f'Methods Success: {overall_success["Success"]}, Methods Failure: {overall_success["Failure"]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_methods()
