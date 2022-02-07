import matplotlib.pyplot as plt

from modelling import generate_conditionals_bayesian_network
from constants import ParentCategories, Conditionals, success, failure
from util import Timer

NODE_ORDER = {
    ParentCategories.CONDITIONALS: 0,
    Conditionals.BOOLEAN: 1,
    Conditionals.DECISION: 2,
    Conditionals.OPERATORS: 3,
    'Conditionals Statements': 4,
    Conditionals.NESTED_CONDITIONAL_STATEMENTS: 5,
    Conditionals.SIMPLE_PROGRAMS: 6,
    Conditionals.PROGRAMS: 7
}


def test_conditionals():
    model = generate_conditionals_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    # All nodes are success.
    _predict_success_in_conditionals(model, success, success, success, success, success, success, success)
    # All nodes are failure.
    _predict_success_in_conditionals(model, failure, failure, failure, failure, failure, failure, failure)
    # Test more successful than failure (failure in more complex topics).
    _predict_success_in_conditionals(model, success, success, success, success, failure, failure, failure)
    # Test more successful than failure (failure in easier topics).
    _predict_success_in_conditionals(model, failure, failure, failure, success, success, success, success)
    # Test more failure than success (complex topics).
    _predict_success_in_conditionals(model, success, success, success, failure, failure, failure, failure)
    # Test more failure than success (easier topics).
    _predict_success_in_conditionals(model, failure, failure, failure, failure, success, success, success)

    print(ParentCategories.CONDITIONALS)
    _run_inference(model, {
        Conditionals.BOOLEAN: success,
        Conditionals.DECISION: success,
        Conditionals.OPERATORS: success,
        Conditionals.CONDITIONAL_STATEMENTS: success,
        Conditionals.NESTED_CONDITIONAL_STATEMENTS: success,
        Conditionals.SIMPLE_PROGRAMS: success,
        Conditionals.PROGRAMS: success
    }, ParentCategories.CONDITIONALS)

    print(ParentCategories.CONDITIONALS)
    _run_inference(model, {
        Conditionals.BOOLEAN: failure,
        Conditionals.DECISION: failure,
        Conditionals.OPERATORS: failure,
        Conditionals.CONDITIONAL_STATEMENTS: success,
        Conditionals.NESTED_CONDITIONAL_STATEMENTS: success,
    }, ParentCategories.CONDITIONALS)

    print(Conditionals.PROGRAMS)
    _run_inference(model, {
        ParentCategories.CONDITIONALS: success,
        Conditionals.BOOLEAN: success,
    }, Conditionals.PROGRAMS)

    print(Conditionals.OPERATORS)
    _run_inference(model, {
        ParentCategories.CONDITIONALS: success,
        Conditionals.BOOLEAN: failure,
        Conditionals.DECISION: success,
        Conditionals.CONDITIONAL_STATEMENTS: success,
        Conditionals.NESTED_CONDITIONAL_STATEMENTS: success,
        Conditionals.SIMPLE_PROGRAMS: success,
        Conditionals.PROGRAMS: failure
    }, Conditionals.OPERATORS)


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _predict_success_in_conditionals(model, boolean, decision, operators, conditional_statements,
                                     nested_conditional_statements, simple_programs, programs):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        Conditionals.BOOLEAN: boolean,
        Conditionals.DECISION: decision,
        Conditionals.OPERATORS: operators,
        Conditionals.CONDITIONAL_STATEMENTS: conditional_statements,
        Conditionals.NESTED_CONDITIONAL_STATEMENTS: nested_conditional_statements,
        Conditionals.SIMPLE_PROGRAMS: simple_programs,
        Conditionals.PROGRAMS: programs
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Boolean Expressions: {boolean}, Decision: {decision}, Operators: {operators}, '
        f'Conditional Statements: {conditional_statements}, \n'
        f'Nested Conditional Statements: {nested_conditional_statements}, '
        f'Simple Programs: {simple_programs}, Programs: {programs}'
    ))
    print(f'Success: {overall_success["Success"]}, Failure: {overall_success["Failure"]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_conditionals()
