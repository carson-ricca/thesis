from constants import success, failure
from modelling import generate_basics_bayesian_network
import matplotlib.pyplot as plt

from util import Timer

NODE_ORDER = {
    'Basics': 0,
    'Variables': 1,
    'Data Types': 2,
    'Statements': 3,
    'Constants': 4,
    'Arithmetic Operators': 5,
    'Casting': 6,
    'Simple Calculation Problems': 7
}


def test_basics():
    model = generate_basics_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    # All nodes are success.
    _predict_success_in_basics(model, success, success, success, success, success, success, success)
    # All nodes are failure.
    _predict_success_in_basics(model, failure, failure, failure, failure, failure, failure, failure)
    # Test more successful than failure (failure in more complex topics).
    _predict_success_in_basics(model, success, success, success, success, failure, failure, failure)
    # Test more successful than failure (failure in easier topics).
    _predict_success_in_basics(model, failure, failure, failure, success, success, success, success)
    # Test more failure than success (complex topics).
    _predict_success_in_basics(model, success, success, success, failure, failure, failure, failure)
    # Test more failure than success (easier topics).
    _predict_success_in_basics(model, failure, failure, failure, failure, success, success, success)

    print('Basics')
    _run_inference(model, {
        'Variables': success,
        'Data Types': failure,
        'Statements': success,
        'Constants': failure,
        'Arithmetic Operators': success,
        'Casting': success,
        'Simple Calculation Problems': success
    }, 'Basics')

    print('Simple Calculation Problems')
    _run_inference(model, {
        'Basics': success,
        'Variables': success,
        'Data Types': success,
        'Statements': failure,
        'Constants': success,
        'Arithmetic Operators': failure,
        'Casting': success,
    }, 'Simple Calculation Problems')

    print('Constants')
    _run_inference(model, {
        'Basics': failure,
        'Variables': failure,
        'Data Types': success,
        'Statements': success,
    }, 'Constants')

    print('Casting')
    _run_inference(model, {
        'Basics': success,
        'Variables': success,
        'Data Types': failure,
        'Statements': failure,
        'Constants': failure,
        'Arithmetic Operators': failure,
        'Simple Calculation Problems': success
    }, 'Casting')


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _predict_success_in_basics(model, variables, data_types, statements, constants, arithmetic_operators, casting,
                               simple_calculation_problems):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Variables': variables,
        'Data Types': data_types,
        'Statements': statements,
        'Constants': constants,
        'Arithmetic Operators': arithmetic_operators,
        'Casting': casting,
        'Simple Calculation Problems': simple_calculation_problems
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Variables: {variables}, Data Types: {data_types}, Statements: {statements}, '
        f'Constants: {constants}, \n'
        f'Arithmetic Operators: {arithmetic_operators}, '
        f'Casting: {casting}, Simple Calculation Problems: {simple_calculation_problems}'
    ))
    print(f'Basics Success: {overall_success["Success"]}, Basics Failure: {overall_success["Failure"]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_basics()
