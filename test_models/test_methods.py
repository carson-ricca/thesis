from matplotlib import pyplot as plt

from constants import success, failure
from modelling import generate_methods_bayesian_network


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


def _predict_success_in_loops(model, abstraction, variable_scope, using_methods, defining_methods, method_overloading,
                              modular_programs):
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
    print('-' * 150)


if __name__ == "__main__":
    test_methods()
