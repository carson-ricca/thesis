from matplotlib import pyplot as plt

from modelling import generate_loops_bayesian_network
from constants import success, failure


def test_loops():
    model = generate_loops_bayesian_network()
    model.plot()
    plt.show()
    # # All nodes are success.
    # _predict_success_in_loops(model, success, success, success, success, success, success, success, success)
    # # All nodes are failure.
    # _predict_success_in_loops(model, failure, failure, failure, failure, failure, failure, failure, success)
    # # Test more successful than failure (failure in more complex topics).
    # _predict_success_in_loops(model, success, success, success, success, failure, failure, failure, failure)
    # # Test more successful than failure (failure in easier topics).
    # _predict_success_in_loops(model, failure, failure, failure, failure, success, success, success, success)
    # # Test more failure than success (complex topics).
    # _predict_success_in_loops(model, success, success, success, failure, failure, failure, failure, failure)
    # # Test more failure than success (easier topics).
    # _predict_success_in_loops(model, failure, failure, failure, failure, failure, success, success, success)


def _predict_success_in_loops(model, repetition, decision_diagrams, while_loops, for_loops, variable_scope,
                              simple_programs, nested_loops, programs):
    predictions = model.predict_proba({
        'Repetition': repetition,
        'Decision Diagrams': decision_diagrams,
        'While Loops': while_loops,
        'For Loops': for_loops,
        'Variable Scope': variable_scope,
        'Simple Programs': simple_programs,
        'Nested Loops': nested_loops,
        'Programs': programs
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Repetition: {repetition}, Decision Diagrams: {decision_diagrams}, While Loops: {while_loops}, '
        f'For Loops: {for_loops}, Variable Scope: {variable_scope} \n'
        f'Nested Loops: {nested_loops}, '
        f'Simple Programs: {simple_programs}, Programs: {programs}'
    ))
    print(f'Success: {overall_success["Success"]}, Failure: {overall_success["Failure"]}')
    print('-' * 150)


if __name__ == "__main__":
    test_loops()
