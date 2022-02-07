from matplotlib import pyplot as plt

from constants import ParentCategories, PreDefinedClasses, success, failure
from modelling import generate_pre_defined_classes_bayesian_network
from util import Timer

NODE_ORDER = {
    ParentCategories.PRE_DEFINED_CLASSES: 0,
    PreDefinedClasses.OOP_OVERVIEW: 1,
    PreDefinedClasses.SCANNER: 2,
    PreDefinedClasses.CHARACTER: 3,
    PreDefinedClasses.MATH: 4,
    PreDefinedClasses.RANDOM: 5,
    PreDefinedClasses.MATH_PROGRAMS: 6,
    PreDefinedClasses.CHANGING_BEHAVIOUR_PROGRAMS: 7,
    PreDefinedClasses.SIMPLE_PROGRAMS: 8,
    PreDefinedClasses.STRING: 9,
    PreDefinedClasses.PROGRAMS: 10
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

    print(ParentCategories.PRE_DEFINED_CLASSES)
    _run_inference(model, {
        PreDefinedClasses.OOP_OVERVIEW: success,
        PreDefinedClasses.SCANNER: success,
        PreDefinedClasses.CHARACTER: success,
        PreDefinedClasses.MATH: success,
        PreDefinedClasses.RANDOM: failure,
        PreDefinedClasses.MATH_PROGRAMS: success,
        PreDefinedClasses.CHANGING_BEHAVIOUR_PROGRAMS: success,
        PreDefinedClasses.SIMPLE_PROGRAMS: success,
        PreDefinedClasses.STRING: failure,
        PreDefinedClasses.PROGRAMS: success
    }, ParentCategories.PRE_DEFINED_CLASSES)

    print(PreDefinedClasses.PROGRAMS)
    _run_inference(model, {
        ParentCategories.PRE_DEFINED_CLASSES: failure,
        PreDefinedClasses.OOP_OVERVIEW: failure,
        PreDefinedClasses.SCANNER: failure,
        PreDefinedClasses.CHARACTER: success,
        PreDefinedClasses.MATH: success,
        PreDefinedClasses.RANDOM: success,
        PreDefinedClasses.MATH_PROGRAMS: failure,
        PreDefinedClasses.CHANGING_BEHAVIOUR_PROGRAMS: success,
        PreDefinedClasses.SIMPLE_PROGRAMS: success,
        PreDefinedClasses.STRING: success,
    }, PreDefinedClasses.PROGRAMS)

    print(PreDefinedClasses.SCANNER)
    _run_inference(model, {
        ParentCategories.PRE_DEFINED_CLASSES: failure,
        PreDefinedClasses.OOP_OVERVIEW: success,
        PreDefinedClasses.CHARACTER: success,
        PreDefinedClasses.MATH: success,
        PreDefinedClasses.RANDOM: failure,
    }, PreDefinedClasses.SCANNER)

    print(PreDefinedClasses.MATH_PROGRAMS)
    _run_inference(model, {
        ParentCategories.PRE_DEFINED_CLASSES: success,
        PreDefinedClasses.OOP_OVERVIEW: failure,
        PreDefinedClasses.SCANNER: success,
        PreDefinedClasses.CHARACTER: success,
        PreDefinedClasses.MATH: failure,
        PreDefinedClasses.RANDOM: success,
        PreDefinedClasses.CHANGING_BEHAVIOUR_PROGRAMS: success,
        PreDefinedClasses.SIMPLE_PROGRAMS: success,
        PreDefinedClasses.STRING: success,
        PreDefinedClasses.PROGRAMS: failure
    }, PreDefinedClasses.MATH_PROGRAMS)


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
        PreDefinedClasses.OOP_OVERVIEW: oop_overview,
        PreDefinedClasses.SCANNER: scanner,
        PreDefinedClasses.CHARACTER: character,
        PreDefinedClasses.MATH: math,
        PreDefinedClasses.RANDOM: random,
        PreDefinedClasses.MATH_PROGRAMS: math_programs,
        PreDefinedClasses.CHANGING_BEHAVIOUR_PROGRAMS: changing_behaviour_programs,
        PreDefinedClasses.SIMPLE_PROGRAMS: simple_programs,
        PreDefinedClasses.STRING: string,
        PreDefinedClasses.PROGRAMS: programs
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
