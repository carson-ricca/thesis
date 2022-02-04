from modelling import generate_conditionals_bayesian_network
from constants import success, failure
from util import Timer

NODE_ORDER = {
    'Conditionals': 0,
    'Boolean': 1,
    'Decision': 2,
    'Operators': 3,
    'Conditionals Statements': 4,
    'Nested Conditional Statements': 5,
    'Simple Programs': 6,
    'Programs': 7
}


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

    print('Conditionals')
    _run_inference(model, {
        'Boolean': success,
        'Decision': success,
        'Operators': success,
        'Conditional Statements': success,
        'Nested Conditional Statements': success,
        'Simple Programs': success,
        'Programs': success
    }, 'Conditionals')

    print('Conditionals')
    _run_inference(model, {
        'Boolean': failure,
        'Decision': failure,
        'Operators': failure,
        'Conditional Statements': success,
        'Nested Conditional Statements': success,
    }, 'Conditionals')

    print('Programs')
    _run_inference(model, {
        'Conditionals': success,
        'Boolean': success,
    }, 'Programs')

    print('Operators')
    _run_inference(model, {
        'Conditionals': success,
        'Boolean': failure,
        'Decision': success,
        'Conditional Statements': success,
        'Nested Conditional Statements': success,
        'Simple Programs': success,
        'Programs': failure
    }, 'Operators')


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
