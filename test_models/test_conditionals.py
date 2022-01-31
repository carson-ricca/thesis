from modelling import generate_conditionals_bayesian_network
from constants import success, failure
from util import Timer


def test_conditionals():
    model = generate_conditionals_bayesian_network()
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


def _predict_success_in_conditionals(model, boolean, decision, operators, conditional_statements,
                                     nested_conditional_statements, simple_programs, programs):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Boolean': boolean,
        'Decision': decision,
        'Operators': operators,
        'Conditional Statements': conditional_statements,
        'Nested Conditional Statements': nested_conditional_statements,
        'Simple Programs': simple_programs,
        'Programs': programs
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
