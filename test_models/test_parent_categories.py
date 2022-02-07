import matplotlib.pyplot as plt

from modelling import generate_parent_categories_bayesian_network
from constants import success, failure
from util import Timer

NODE_ORDER = {
    'Basics': 0,
    'Conditionals': 1,
    'Pre-Defined Classes': 2,
    'Loops': 3,
    'Arrays': 4,
    'Methods': 5,
    'OOP': 6
}


def test_parent_categories():
    model = generate_parent_categories_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    _make_prediction(model, success, success, success, success, success, success)
    _make_prediction(model, failure, failure, failure, failure, failure, failure)
    _make_prediction(model, failure, failure, failure, success, success, success)
    _make_prediction(model, success, success, success, failure, failure, failure)
    _make_prediction(model, success, failure, success, failure, success, failure)
    _make_prediction(model, failure, success, success, success, success, failure)

    print('OOP')
    _run_inference(model, {
        'Basics': success,
        'Conditionals': success,
        'Pre-Defined Classes': success,
        'Loops': success,
        'Arrays': success,
        'Methods': success,
    }, 'OOP')

    print('OOP')
    _run_inference(model, {
        'Basics': success,
        'Conditionals': success,
    }, 'OOP')

    print('Loops')
    _run_inference(model, {
        'Basics': success,
        'Conditionals': failure,
        'Pre-Defined Classes': success,
        'Arrays': success,
        'Methods': success,
        'OOP': failure
    }, 'Loops')

    print('Methods')
    _run_inference(model, {
        'Basics': failure,
        'Conditionals': failure,
        'Loops': success,
        'Arrays': success,
        'OOP': failure
    }, 'Methods')


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _make_prediction(model, basics, conditionals, pre_defined_classes, loops, arrays, methods):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Basics': basics,
        'Conditionals': conditionals,
        'Pre-Defined Classes': pre_defined_classes,
        'Loops': loops,
        'Arrays': arrays,
        'Methods': methods,
    })
    category_success = predictions[6].parameters[0]
    probable_success = category_success[success]
    probable_failure = category_success[failure]
    print((
        f'Basics: {basics}, Conditionals: {conditionals}, Pre-Defined Classes: {pre_defined_classes},\nLoops: {loops}, '
        f'Arrays: {arrays}, Methods: {methods}'
    ))
    print(f'OOP Success: {probable_success}, OOP Failure: {probable_failure}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_parent_categories()
