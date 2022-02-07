from matplotlib import pyplot as plt

from constants import success, failure
from modelling import generate_pre_defined_classes_bayesian_network
from util import Timer

NODE_ORDER = {
    'Pre-Defined Classes': 0,
    'OOP Overview': 1,
    'Scanner': 2,
    'Character': 3,
    'Math': 4,
    'Random': 5,
    'Math Programs': 6,
    'Changing Behaviour Programs': 7,
    'Simple Programs': 8,
    'String': 9,
    'Programs': 10
}


def test_pre_defined_classes():
    model = generate_pre_defined_classes_bayesian_network()
    # Uncomment these lines to visually plot the model.
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

    print('Pre-Defined Classes')
    _run_inference(model, {
        'OOP Overview': success,
        'Scanner': success,
        'Character': success,
        'Math': success,
        'Random': failure,
        'Math Programs': success,
        'Changing Behaviour Programs': success,
        'Simple Programs': success,
        'String': failure,
        'Programs': success
    }, 'Pre-Defined Classes')

    print('Programs')
    _run_inference(model, {
        'Pre-Defined Classes': failure,
        'OOP Overview': failure,
        'Scanner': failure,
        'Character': success,
        'Math': success,
        'Random': success,
        'Math Programs': failure,
        'Changing Behaviour Programs': success,
        'Simple Programs': success,
        'String': success,
    }, 'Programs')

    print('Scanner')
    _run_inference(model, {
        'Pre-Defined Classes': failure,
        'OOP Overview': success,
        'Character': success,
        'Math': success,
        'Random': failure,
    }, 'Scanner')

    print('Math Programs')
    _run_inference(model, {
        'Pre-Defined Classes': success,
        'OOP Overview': failure,
        'Scanner': success,
        'Character': success,
        'Math': failure,
        'Random': success,
        'Changing Behaviour Programs': success,
        'Simple Programs': success,
        'String': success,
        'Programs': failure
    }, 'Math Programs')


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


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
