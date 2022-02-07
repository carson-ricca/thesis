import matplotlib.pyplot as plt

from constants import ParentCategories, OOP, success, failure
from modelling import generate_oop_bayesian_network
from util import Timer

NODE_ORDER = {
    ParentCategories.OOP: 0,
    OOP.VARIABLE_SCOPE: 1,
    OOP.OOP_OVERVIEW: 2,
    OOP.MULTIPLE_CLASSES: 3,
    OOP.USER_DEFINED_CLASSES: 4,
    OOP.CREATING_OBJECTS: 5,
    OOP.OBJECT_INTERACTIONS: 6,
    OOP.OBJECT_INDEPENDENCE: 7,
    OOP.SPECIAL_CLASS_METHOD: 8,
    OOP.SIMPLE_PROGRAMS: 9,
    OOP.STATIC_MODIFIER: 10,
    OOP.PROGRAMS: 11
}


def test_oop():
    model = generate_oop_bayesian_network()
    # Uncomment these lines to visually plot the model.
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

    print(ParentCategories.OOP)
    _run_inference(model, {
        OOP.VARIABLE_SCOPE: success,
        OOP.OOP_OVERVIEW: success,
        OOP.MULTIPLE_CLASSES: success,
        OOP.USER_DEFINED_CLASSES: success,
        OOP.CREATING_OBJECTS: success,
        OOP.OBJECT_INTERACTIONS: success,
        OOP.OBJECT_INDEPENDENCE: success,
        OOP.SPECIAL_CLASS_METHOD: success,
        OOP.SIMPLE_PROGRAMS: success,
        OOP.STATIC_MODIFIER: success,
        OOP.PROGRAMS: success
    }, ParentCategories.OOP)

    print(OOP.PROGRAMS)
    _run_inference(model, {
        ParentCategories.OOP: success,
        OOP.VARIABLE_SCOPE: failure,
        OOP.OOP_OVERVIEW: success,
        OOP.MULTIPLE_CLASSES: success,
        OOP.USER_DEFINED_CLASSES: failure,
        OOP.CREATING_OBJECTS: success,
        OOP.OBJECT_INTERACTIONS: success,
        OOP.OBJECT_INDEPENDENCE: failure,
        OOP.SPECIAL_CLASS_METHOD: success,
        OOP.SIMPLE_PROGRAMS: success,
        OOP.STATIC_MODIFIER: success,
    }, OOP.PROGRAMS)

    print(OOP.MULTIPLE_CLASSES)
    _run_inference(model, {
        ParentCategories.OOP: success,
        OOP.VARIABLE_SCOPE: success,
        OOP.OOP_OVERVIEW: success
    }, OOP.MULTIPLE_CLASSES)

    print(OOP.STATIC_MODIFIER)
    _run_inference(model, {
        ParentCategories.OOP: failure,
        OOP.VARIABLE_SCOPE: failure,
        OOP.OOP_OVERVIEW: failure,
        OOP.MULTIPLE_CLASSES: success,
        OOP.USER_DEFINED_CLASSES: success,
        OOP.CREATING_OBJECTS: failure,
        OOP.OBJECT_INTERACTIONS: failure,
        OOP.OBJECT_INDEPENDENCE: failure,
        OOP.SPECIAL_CLASS_METHOD: failure,
        OOP.SIMPLE_PROGRAMS: success,
        OOP.PROGRAMS: failure
    }, OOP.STATIC_MODIFIER)


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
        OOP.VARIABLE_SCOPE: variable_scope,
        OOP.OOP_OVERVIEW: oop_overview,
        OOP.MULTIPLE_CLASSES: multiple_classes,
        OOP.USER_DEFINED_CLASSES: user_defined_classes,
        OOP.CREATING_OBJECTS: creating_objects,
        OOP.OBJECT_INTERACTIONS: object_interactions,
        OOP.OBJECT_INDEPENDENCE: object_independence,
        OOP.SPECIAL_CLASS_METHOD: special_class_method,
        OOP.SIMPLE_PROGRAMS: simple_programs,
        OOP.STATIC_MODIFIER: static_modifier,
        OOP.PROGRAMS: programs
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
