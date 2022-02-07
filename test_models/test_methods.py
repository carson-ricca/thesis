from matplotlib import pyplot as plt

from constants import ParentCategories, Methods, success, failure
from modelling import generate_methods_bayesian_network
from util import Timer

NODE_ORDER = {
    ParentCategories.METHODS: 0,
    Methods.ABSTRACTION: 1,
    Methods.VARIABLE_SCOPE: 2,
    Methods.USING_METHODS: 3,
    Methods.DEFINING_METHODS: 4,
    Methods.METHOD_OVERLOADING: 5,
    Methods.MODULAR_PROGRAMS: 6
}


def test_methods():
    model = generate_methods_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    _predict_success_in_loops(model, success, success, success, success, success, success)
    _predict_success_in_loops(model, failure, failure, failure, failure, failure, failure)
    _predict_success_in_loops(model, failure, failure, failure, success, success, success)
    _predict_success_in_loops(model, success, success, success, failure, failure, failure)
    _predict_success_in_loops(model, failure, success, failure, success, failure, success)
    _predict_success_in_loops(model, failure, success, success, success, success, failure)

    print(ParentCategories.METHODS)
    _run_inference(model, {
        Methods.ABSTRACTION: success,
        Methods.VARIABLE_SCOPE: success,
        Methods.USING_METHODS: success,
        Methods.DEFINING_METHODS: success,
        Methods.METHOD_OVERLOADING: success,
        Methods.MODULAR_PROGRAMS: failure,
    }, ParentCategories.METHODS)

    print(ParentCategories.METHODS)
    _run_inference(model, {
        Methods.ABSTRACTION: failure,
        Methods.VARIABLE_SCOPE: failure,
        Methods.USING_METHODS: failure,
        Methods.DEFINING_METHODS: failure,
        Methods.METHOD_OVERLOADING: failure,
        Methods.MODULAR_PROGRAMS: failure,
    }, ParentCategories.METHODS)

    print(Methods.MODULAR_PROGRAMS)
    _run_inference(model, {
        Methods.USING_METHODS: success,
        Methods.DEFINING_METHODS: failure,
        Methods.METHOD_OVERLOADING: success,
    }, Methods.MODULAR_PROGRAMS)

    print(Methods.DEFINING_METHODS)
    _run_inference(model, {
        ParentCategories.METHODS: failure,
        Methods.ABSTRACTION: success,
        Methods.VARIABLE_SCOPE: failure,
        Methods.USING_METHODS: success,
        Methods.METHOD_OVERLOADING: failure,
        Methods.MODULAR_PROGRAMS: failure,
    }, Methods.DEFINING_METHODS)


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
        Methods.ABSTRACTION: abstraction,
        Methods.VARIABLE_SCOPE: variable_scope,
        Methods.USING_METHODS: using_methods,
        Methods.DEFINING_METHODS: defining_methods,
        Methods.METHOD_OVERLOADING: method_overloading,
        Methods.MODULAR_PROGRAMS: modular_programs,
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
