from matplotlib import pyplot as plt

from constants import success, failure
from modelling import generate_pre_defined_classes_bayesian_network
from util import Timer


def test_pre_defined_classes():
    model = generate_pre_defined_classes_bayesian_network()
    # model.plot()
    # plt.show()

    _predict_pre_defined_classes_success(model, success, success, success, success, success, success, success, success,
                                         success, success)
    _predict_pre_defined_classes_success(model, failure, failure, failure, failure, failure, failure, failure, failure,
                                         failure, failure)
    _predict_pre_defined_classes_success(model, failure, failure, failure, failure, success, success, success, success,
                                         success, success)
    _predict_pre_defined_classes_success(model, success, success, success, success, success, success, failure, failure,
                                         failure, failure)
    _predict_pre_defined_classes_success(model, success, failure, success, failure, success, failure, success, failure,
                                         success, failure)
    _predict_pre_defined_classes_success(model, failure, failure, failure, success, success, success, success, failure,
                                         failure, failure)
    _predict_pre_defined_classes_success(model, success, success, success, failure, failure, failure, success, success,
                                         success, success)


def _predict_pre_defined_classes_success(model, oop_overview, scanner, character, math, random,
                                         math_programs, changing_behaviour_programs, simple_programs,
                                         string, programs):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'OOP Overview': oop_overview,
        'Scanner': scanner,
        'Character': character,
        'Math': math,
        'Random': random,
        'Math Programs': math_programs,
        'Changing Behaviour Programs': changing_behaviour_programs,
        'Simple Programs': simple_programs,
        'String': string,
        'Programs': programs
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'OOP Overview: {oop_overview}, Scanner: {scanner}, '
        f'Character: {character},\nMath: {math}, '
        f'Random: {random}, Math Programs: {math_programs},\n'
        f'Changing Behaviour Programs: {changing_behaviour_programs}, Simple Programs: {simple_programs}, '
        f'String: {string}, Programs: {programs}'
    ))
    print((
        f'Pre-Defined Classes Success: {overall_success["Success"]}, '
        f'Pre-Defined Classes Failure: {overall_success["Failure"]}'
    ))
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_pre_defined_classes()
