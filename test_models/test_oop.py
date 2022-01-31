import matplotlib.pyplot as plt

from constants import success, failure
from modelling import generate_oop_bayesian_network
from util import Timer


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
