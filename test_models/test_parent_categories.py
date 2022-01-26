import matplotlib.pyplot as plt

from modelling import generate_parent_categories_bayesian_network
from constants import success, failure


def test_parent_categories():
    model = generate_parent_categories_bayesian_network()
    # model.plot()
    # plt.show()

    _make_prediction(model, success, success, success, success, success, success)
    _make_prediction(model, failure, failure, failure, failure, failure, failure)
    _make_prediction(model, failure, failure, failure, success, success, success)
    _make_prediction(model, success, success, success, failure, failure, failure)
    _make_prediction(model, success, failure, success, failure, success, failure)
    _make_prediction(model, failure, success, success, success, success, failure)


def _make_prediction(model, basics, conditionals, pre_defined_classes, loops, arrays, methods):
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
    print('-' * 150)


if __name__ == "__main__":
    test_parent_categories()
