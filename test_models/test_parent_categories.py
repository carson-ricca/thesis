import matplotlib.pyplot as plt

from modelling import generate_parent_categories_bayesian_network
from constants import ParentCategories, success, failure
from util import Timer

NODE_ORDER = {
    ParentCategories.BASICS: 0,
    ParentCategories.CONDITIONALS: 1,
    ParentCategories.PRE_DEFINED_CLASSES: 2,
    ParentCategories.LOOPS: 3,
    ParentCategories.ARRAYS: 4,
    ParentCategories.METHODS: 5,
    ParentCategories.OOP: 6
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

    print(ParentCategories.OOP)
    _run_inference(model, {
        ParentCategories.BASICS: success,
        ParentCategories.CONDITIONALS: success,
        ParentCategories.PRE_DEFINED_CLASSES: success,
        ParentCategories.LOOPS: success,
        ParentCategories.ARRAYS: success,
        ParentCategories.METHODS: success,
    }, ParentCategories.OOP)

    print(ParentCategories.OOP)
    _run_inference(model, {
        ParentCategories.BASICS: success,
        ParentCategories.CONDITIONALS: success,
    }, ParentCategories.OOP)

    print(ParentCategories.LOOPS)
    _run_inference(model, {
        ParentCategories.BASICS: success,
        ParentCategories.CONDITIONALS: failure,
        ParentCategories.PRE_DEFINED_CLASSES: success,
        ParentCategories.ARRAYS: success,
        ParentCategories.METHODS: success,
        ParentCategories.OOP: failure
    }, ParentCategories.LOOPS)

    print(ParentCategories.METHODS)
    _run_inference(model, {
        ParentCategories.BASICS: failure,
        ParentCategories.CONDITIONALS: failure,
        ParentCategories.LOOPS: success,
        ParentCategories.ARRAYS: success,
        ParentCategories.OOP: failure
    }, ParentCategories.METHODS)


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
        ParentCategories.BASICS: basics,
        ParentCategories.CONDITIONALS: conditionals,
        ParentCategories.PRE_DEFINED_CLASSES: pre_defined_classes,
        ParentCategories.LOOPS: loops,
        ParentCategories.ARRAYS: arrays,
        ParentCategories.METHODS: methods,
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
