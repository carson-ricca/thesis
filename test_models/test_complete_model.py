import matplotlib.pyplot as plt

from constants import ParentCategories, Basics, Conditionals, PreDefinedClasses, Loops, Arrays, Methods, OOP, success, \
    failure
from modelling import generate_complete_bayesian_network
from util import Timer

NODE_ORDER = {
    ParentCategories.BASICS: 0,
    ParentCategories.CONDITIONALS: 1,
    ParentCategories.PRE_DEFINED_CLASSES: 2,
    ParentCategories.LOOPS: 3,
    ParentCategories.ARRAYS: 4,
    ParentCategories.METHODS: 5,
    ParentCategories.OOP: 6,
    Basics.VARIABLES: 7,
    Basics.DATA_TYPES: 8,
    Basics.STATEMENTS: 9,
    Basics.CONSTANTS: 10,
    Basics.ARITHMETIC_OPERATORS: 11,
    Basics.CASTING: 12,
    Basics.SIMPLE_CALCULATION_PROBLEMS: 13,
    Conditionals.BOOLEAN: 14,
    Conditionals.DECISION: 15,
    Conditionals.OPERATORS: 16,
    Conditionals.CONDITIONAL_STATEMENTS: 17,
    Conditionals.NESTED_CONDITIONAL_STATEMENTS: 18,
    Conditionals.SIMPLE_PROGRAMS: 19,
    Conditionals.PROGRAMS: 20,
    PreDefinedClasses.OOP_OVERVIEW: 21,
    PreDefinedClasses.SCANNER: 22,
    PreDefinedClasses.CHARACTER: 23,
    PreDefinedClasses.MATH: 24,
    PreDefinedClasses.RANDOM: 25,
    PreDefinedClasses.MATH_PROGRAMS: 26,
    PreDefinedClasses.CHANGING_BEHAVIOUR_PROGRAMS: 27,
    PreDefinedClasses.SIMPLE_PROGRAMS: 28,
    PreDefinedClasses.STRING: 29,
    PreDefinedClasses.PROGRAMS: 30,
    Loops.REPETITION: 31,
    Loops.VARIABLE_SCOPE: 32,
    Loops.DECISION_DIAGRAMS: 33,
    Loops.WHILE_LOOPS: 34,
    Loops.FOR_LOOPS: 35,
    Loops.SIMPLE_PROGRAMS: 36,
    Loops.NESTED_LOOPS: 37,
    Loops.PROGRAMS: 38,
    Arrays.DATA_REPRESENTATION: 39,
    Arrays.DEFINING_ARRAYS: 40,
    Arrays.REFERENCING_ARRAYS: 41,
    Arrays.MULTIDIMENSIONAL_ARRAYS: 42,
    Arrays.ARRAYS_WITH_METHODS: 43,
    Arrays.PROGRAMS_WITH_DATA_SEQUENCES: 44,
    Arrays.PROGRAMS_WITH_MULTIDIMENSIONAL_DATA: 45,
    Methods.ABSTRACTION: 46,
    Methods.VARIABLE_SCOPE: 47,
    Methods.USING_METHODS: 48,
    Methods.DEFINING_METHODS: 49,
    Methods.METHOD_OVERLOADING: 50,
    Methods.MODULAR_PROGRAMS: 51,
    OOP.VARIABLE_SCOPE: 52,
    OOP.OOP_OVERVIEW: 53,
    OOP.MULTIPLE_CLASSES: 54,
    OOP.USER_DEFINED_CLASSES: 55,
    OOP.CREATING_OBJECTS: 56,
    OOP.OBJECT_INTERACTIONS: 57,
    OOP.OBJECT_INDEPENDENCE: 58,
    OOP.SPECIAL_CLASS_METHOD: 59,
    OOP.SIMPLE_PROGRAMS: 60,
    OOP.STATIC_MODIFIER: 61,
    OOP.PROGRAMS: 62
}


def test_complete_model():
    model = generate_complete_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


if __name__ == '__main__':
    test_complete_model()
