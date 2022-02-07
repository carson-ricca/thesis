from constants import ParentCategories, Basics, success, failure
from modelling import generate_basics_bayesian_network
import matplotlib.pyplot as plt

from util import Timer

NODE_ORDER = {
    ParentCategories.BASICS: 0,
    Basics.VARIABLES: 1,
    Basics.DATA_TYPES: 2,
    Basics.STATEMENTS: 3,
    Basics.CONSTANTS: 4,
    Basics.ARITHMETIC_OPERATORS: 5,
    Basics.CASTING: 6,
    Basics.SIMPLE_CALCULATION_PROBLEMS: 7
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

    print(ParentCategories.BASICS)
    _run_inference(model, {
        Basics.VARIABLES: success,
        Basics.DATA_TYPES: failure,
        Basics.STATEMENTS: success,
        Basics.CONSTANTS: failure,
        Basics.ARITHMETIC_OPERATORS: success,
        Basics.CASTING: success,
        Basics.SIMPLE_CALCULATION_PROBLEMS: success
    }, ParentCategories.BASICS)

    print(Basics.SIMPLE_CALCULATION_PROBLEMS)
    _run_inference(model, {
        ParentCategories.BASICS: success,
        Basics.VARIABLES: success,
        Basics.DATA_TYPES: success,
        Basics.STATEMENTS: failure,
        Basics.CONSTANTS: success,
        Basics.ARITHMETIC_OPERATORS: failure,
        Basics.CASTING: success,
    }, Basics.SIMPLE_CALCULATION_PROBLEMS)

    print(Basics.CONSTANTS)
    _run_inference(model, {
        ParentCategories.BASICS: failure,
        Basics.VARIABLES: failure,
        Basics.DATA_TYPES: success,
        Basics.STATEMENTS: success,
    }, Basics.CONSTANTS)

    print(Basics.CASTING)
    _run_inference(model, {
        ParentCategories.BASICS: success,
        Basics.VARIABLES: success,
        Basics.DATA_TYPES: failure,
        Basics.STATEMENTS: failure,
        Basics.CONSTANTS: failure,
        Basics.ARITHMETIC_OPERATORS: failure,
        Basics.SIMPLE_CALCULATION_PROBLEMS: success
    }, Basics.CASTING)


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
        Basics.VARIABLES: variables,
        Basics.DATA_TYPES: data_types,
        Basics.STATEMENTS: statements,
        Basics.CONSTANTS: constants,
        Basics.ARITHMETIC_OPERATORS: arithmetic_operators,
        Basics.CASTING: casting,
        Basics.SIMPLE_CALCULATION_PROBLEMS: simple_calculation_problems
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
