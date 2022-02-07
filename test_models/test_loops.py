from matplotlib import pyplot as plt

from modelling import generate_loops_bayesian_network
from constants import ParentCategories, Loops, success, failure
from util import Timer

NODE_ORDER = {
    ParentCategories.LOOPS: 0,
    Loops.REPETITION: 1,
    Loops.VARIABLE_SCOPE: 2,
    Loops.DECISION_DIAGRAMS: 3,
    Loops.WHILE_LOOPS: 4,
    Loops.FOR_LOOPS: 5,
    Loops.SIMPLE_PROGRAMS: 6,
    Loops.NESTED_LOOPS: 7,
    Loops.PROGRAMS: 8
}


def test_loops():
    model = generate_loops_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    # All nodes are success.
    _predict_success_in_loops(model, success, success, success, success, success, success, success, success)
    # All nodes are failure.
    _predict_success_in_loops(model, failure, failure, failure, failure, failure, failure, failure, success)
    # Test more successful than failure (failure in more complex topics).
    _predict_success_in_loops(model, success, success, success, success, failure, failure, failure, failure)
    # Test more successful than failure (failure in easier topics).
    _predict_success_in_loops(model, failure, failure, failure, failure, success, success, success, success)
    # Test more failure than success (complex topics).
    _predict_success_in_loops(model, success, success, success, failure, failure, failure, failure, failure)
    # Test more failure than success (easier topics).
    _predict_success_in_loops(model, failure, failure, failure, failure, failure, success, success, success)

    print(ParentCategories.LOOPS)
    _run_inference(model, {
        Loops.REPETITION: failure,
        Loops.DECISION_DIAGRAMS: failure,
        Loops.WHILE_LOOPS: success,
        Loops.FOR_LOOPS: success,
        Loops.VARIABLE_SCOPE: success,
        Loops.SIMPLE_PROGRAMS: success,
        Loops.NESTED_LOOPS: success,
        Loops.PROGRAMS: success
    }, ParentCategories.LOOPS)

    print(Loops.PROGRAMS)
    _run_inference(model, {
        ParentCategories.LOOPS: success,
        Loops.REPETITION: success,
        Loops.DECISION_DIAGRAMS: failure,
        Loops.WHILE_LOOPS: success,
        Loops.FOR_LOOPS: failure,
        Loops.VARIABLE_SCOPE: success,
        Loops.SIMPLE_PROGRAMS: failure,
        Loops.NESTED_LOOPS: success,
    }, Loops.PROGRAMS)

    print(Loops.SIMPLE_PROGRAMS)
    _run_inference(model, {
        ParentCategories.LOOPS: success,
        Loops.REPETITION: success,
        Loops.DECISION_DIAGRAMS: failure,
        Loops.VARIABLE_SCOPE: success,
    }, Loops.SIMPLE_PROGRAMS)

    print(Loops.NESTED_LOOPS)
    _run_inference(model, {
        ParentCategories.LOOPS: failure,
        Loops.REPETITION: failure,
    }, Loops.NESTED_LOOPS)


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _predict_success_in_loops(model, repetition, decision_diagrams, while_loops, for_loops, variable_scope,
                              simple_programs, nested_loops, programs):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        Loops.REPETITION: repetition,
        Loops.DECISION_DIAGRAMS: decision_diagrams,
        Loops.WHILE_LOOPS: while_loops,
        Loops.FOR_LOOPS: for_loops,
        Loops.VARIABLE_SCOPE: variable_scope,
        Loops.SIMPLE_PROGRAMS: simple_programs,
        Loops.NESTED_LOOPS: nested_loops,
        Loops.PROGRAMS: programs
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Repetition: {repetition}, Decision Diagrams: {decision_diagrams}, While Loops: {while_loops}, '
        f'For Loops: {for_loops}, Variable Scope: {variable_scope} \n'
        f'Nested Loops: {nested_loops}, '
        f'Simple Programs: {simple_programs}, Programs: {programs}'
    ))
    print(f'Success: {overall_success["Success"]}, Failure: {overall_success["Failure"]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_loops()
