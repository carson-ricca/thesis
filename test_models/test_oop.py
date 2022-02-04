import matplotlib.pyplot as plt

from constants import success, failure
from modelling import generate_oop_bayesian_network
from util import Timer

NODE_ORDER = {
    'OOP': 0,
    'Variable Scope': 1,
    'OOP Overview': 2,
    'Multiple Classes': 3,
    'User Defined Classes': 4,
    'Creating Objects': 5,
    'Object Interactions': 6,
    'Object Independence': 7,
    'Special Class Method': 8,
    'Simple Programs': 9,
    'Static Modifier': 10,
    'Programs': 11
}


def test_oop():
    model = generate_oop_bayesian_network()
    # model.plot()
    # plt.show()
    _predict_oop_success(model, success, success, success, success, success, success, success, success, success,
                         success, success)
    _predict_oop_success(model, failure, failure, failure, failure, failure, failure, failure, failure, failure,
                         failure, failure)
    _predict_oop_success(model, failure, failure, failure, failure, success, success, success, success, success,
                         success, success)
    _predict_oop_success(model, success, success, success, success, success, success, success, failure, failure,
                         failure, failure)
    _predict_oop_success(model, success, failure, success, failure, success, failure, success, failure, success,
                         failure, success)
    _predict_oop_success(model, failure, failure, failure, success, success, success, success, success, failure,
                         failure, failure)
    _predict_oop_success(model, success, success, success, failure, failure, failure, failure, success, success,
                         success, success)

    print('OOP')
    _run_inference(model, {
        'Variable Scope': success,
        'OOP Overview': success,
        'Multiple Classes': success,
        'User Defined Classes': success,
        'Creating Objects': success,
        'Object Interactions': success,
        'Object Independence': success,
        'Special Class Method': success,
        'Simple Programs': success,
        'Static Modifier': success,
        'Programs': success
    }, 'OOP')

    print('Programs')
    _run_inference(model, {
        'OOP': success,
        'Variable Scope': failure,
        'OOP Overview': success,
        'Multiple Classes': success,
        'User Defined Classes': failure,
        'Creating Objects': success,
        'Object Interactions': success,
        'Object Independence': failure,
        'Special Class Method': success,
        'Simple Programs': success,
        'Static Modifier': success,
    }, 'Programs')

    print('Multiple Classes')
    _run_inference(model, {
        'OOP': success,
        'Variable Scope': success,
        'OOP Overview': success
    }, 'Multiple Classes')

    print('Static Modifier')
    _run_inference(model, {
        'OOP': failure,
        'Variable Scope': failure,
        'OOP Overview': failure,
        'Multiple Classes': success,
        'User Defined Classes': success,
        'Creating Objects': failure,
        'Object Interactions': failure,
        'Object Independence': failure,
        'Special Class Method': failure,
        'Simple Programs': success,
        'Programs': failure
    }, 'Static Modifier')


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _predict_oop_success(model, variable_scope, oop_overview, multiple_classes, user_defined_classes, creating_objects,
                         object_interactions, object_independence, special_class_method, simple_programs,
                         static_modifier, programs):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Variable Scope': variable_scope,
        'OOP Overview': oop_overview,
        'Multiple Classes': multiple_classes,
        'User Defined Classes': user_defined_classes,
        'Creating Objects': creating_objects,
        'Object Interactions': object_interactions,
        'Object Independence': object_independence,
        'Special Class Method': special_class_method,
        'Simple Programs': simple_programs,
        'Static Modifier': static_modifier,
        'Programs': programs
    })
    overall_success = predictions[0].parameters[0]
    print((
        f'Variable Scope: {variable_scope}, OOP Overview: {user_defined_classes}, '
        f'Multiple Classes: {multiple_classes},\nUser Defined Classes: {user_defined_classes}, '
        f'Creating Objects: {creating_objects}, Object Interactions: {object_interactions},\n'
        f'Object Independence: {object_independence}, Special Class Method: {special_class_method},\n'
        f'Simple Programs: {simple_programs}, Static Modifier: {static_modifier}, Programs: {programs}'
    ))
    print(f'OOP Success: {overall_success["Success"]}, OOP Failure: {overall_success["Failure"]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_oop()
