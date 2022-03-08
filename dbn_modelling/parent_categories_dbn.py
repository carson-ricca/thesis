from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference
from pgmpy.models import DynamicBayesianNetwork

basics_node_0 = ('Basics', 0)
basics_node_1 = ('Basics', 1)
conditionals_node_0 = ('Conditionals', 0)
conditionals_node_1 = ('Conditionals', 1)
loops_node_0 = ('Loops', 0)
loops_node_1 = ('Loops', 1)
arrays_node_0 = ('Arrays', 0)
arrays_node_1 = ('Arrays', 1)
methods_node_0 = ('Methods', 0)
methods_node_1 = ('Methods', 1)
pre_defined_classes_node_0 = ('Pre-Defined Classes', 0)
pre_defined_classes_node_1 = ('Pre-Defined Classes', 1)
oop_node_0 = ('OOP', 0)
oop_node_1 = ('OOP', 1)


def parent_categories():
    """
    Generates the DBN for the parent categories model.

    CPD Key Names:
    All Nodes: 0 - Success, 1 - Failure
    :return: The generated model.
    """
    model = DynamicBayesianNetwork([
        (basics_node_0, conditionals_node_0),
        (basics_node_0, pre_defined_classes_node_0),
        (conditionals_node_0, loops_node_0),
        (loops_node_0, arrays_node_0),
        (loops_node_0, methods_node_0),
        (arrays_node_0, oop_node_0),
        (methods_node_0, oop_node_0),
        (pre_defined_classes_node_0, oop_node_0),
        (basics_node_0, basics_node_1),
        (conditionals_node_0, conditionals_node_1),
        (loops_node_0, loops_node_1),
        (arrays_node_0, arrays_node_1),
        (methods_node_0, methods_node_1),
        (pre_defined_classes_node_0, pre_defined_classes_node_1),
        (oop_node_0, oop_node_1),
        (basics_node_1, conditionals_node_1),
        (basics_node_1, pre_defined_classes_node_1),
        (conditionals_node_1, loops_node_1),
        (loops_node_1, arrays_node_1),
        (loops_node_1, methods_node_1),
        (arrays_node_1, oop_node_1),
        (methods_node_1, oop_node_1),
        (pre_defined_classes_node_1, oop_node_1)
    ])

    basics_cpd = TabularCPD(basics_node_0, 2, [
        [0.5], [0.5]
    ])

    conditionals_cpd = TabularCPD(conditionals_node_0, 2, [
        [0.75, 0.25],
        [0.25, 0.75]
    ], evidence=[basics_node_0], evidence_card=[2])

    pre_defined_classes_cpd = TabularCPD(pre_defined_classes_node_0, 2, [
        [0.75, 0.25],
        [0.25, 0.75]
    ], evidence=[basics_node_0], evidence_card=[2])

    loops_cpd = TabularCPD(loops_node_0, 2, [
        [0.75, 0.25],
        [0.25, 0.75]
    ], evidence=[conditionals_node_0], evidence_card=[2])

    arrays_cpd = TabularCPD(arrays_node_0, 2, [
        [0.75, 0.25],
        [0.25, 0.75]
    ], evidence=[loops_node_0], evidence_card=[2])

    methods_cpd = TabularCPD(methods_node_0, 2, [
        [0.75, 0.25],
        [0.25, 0.75]
    ], evidence=[loops_node_0], evidence_card=[2])

    oop_cpd = TabularCPD(oop_node_0, 2, [
        [0.9, 0.75, 0.6, 0.3, 0.7, 0.4, 0.4, 0.1],
        [0.1, 0.25, 0.4, 0.7, 0.3, 0.6, 0.6, 0.9]
    ], evidence=[arrays_node_0, methods_node_0, pre_defined_classes_node_0], evidence_card=[2, 2, 2])

    basics_transitional_cpd = TabularCPD(basics_node_1, 2, [
        [0.8, 0.2],
        [0.2, 0.8]
    ], evidence=[basics_node_0], evidence_card=[2])

    conditionals_transitional_cpd = TabularCPD(conditionals_node_1, 2, [
        [0.9, 0.8, 0.5, 0.1],
        [0.1, 0.2, 0.5, 0.9]
    ], evidence=[conditionals_node_0, basics_node_1], evidence_card=[2, 2])

    pre_defined_classes_transitional_cpd = TabularCPD(pre_defined_classes_node_1, 2, [
        [0.9, 0.8, 0.5, 0.1],
        [0.1, 0.2, 0.5, 0.9]
    ], evidence=[pre_defined_classes_node_0, basics_node_1], evidence_card=[2, 2])

    loops_transitional_cpd = TabularCPD(loops_node_1, 2, [
        [0.9, 0.8, 0.5, 0.1],
        [0.1, 0.2, 0.5, 0.9]
    ], evidence=[loops_node_0, conditionals_node_1], evidence_card=[2, 2])

    arrays_transitional_cpd = TabularCPD(arrays_node_1, 2, [
        [0.9, 0.8, 0.5, 0.1],
        [0.1, 0.2, 0.5, 0.9]
    ], evidence=[arrays_node_0, loops_node_1], evidence_card=[2, 2])

    methods_transitional_cpd = TabularCPD(methods_node_1, 2, [
        [0.9, 0.8, 0.5, 0.1],
        [0.1, 0.2, 0.5, 0.9]
    ], evidence=[methods_node_0, loops_node_1], evidence_card=[2, 2])

    oop_transitional_cpd = (TabularCPD(oop_node_1, 2, [
        [0.95, 0.9, 0.9, 0.7, 0.9, 0.7, 0.7, 0.6, 0.7, 0.6, 0.6, 0.4, 0.6, 0.4, 0.4, 0.1],
        [0.05, 0.1, 0.1, 0.3, 0.1, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.6, 0.4, 0.6, 0.6, 0.9]
    ], evidence=[oop_node_0, arrays_node_1, methods_node_1, pre_defined_classes_node_1], evidence_card=[2, 2, 2, 2]))

    model.add_cpds(basics_cpd, conditionals_cpd, pre_defined_classes_cpd, loops_cpd, arrays_cpd, methods_cpd, oop_cpd,
                   basics_transitional_cpd, conditionals_transitional_cpd, pre_defined_classes_transitional_cpd,
                   loops_transitional_cpd, arrays_transitional_cpd, methods_transitional_cpd, oop_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


def test_inference(model):
    dbn_inf = DBNInference(model)

    # Success in all categories in previous timestamp.
    print(
        dbn_inf.forward_inference([basics_node_1], {
            basics_node_0: 0,
            conditionals_node_0: 0,
            loops_node_0: 0,
            arrays_node_0: 0,
            methods_node_0: 0,
            pre_defined_classes_node_0: 0,
            oop_node_0: 0
        })[basics_node_1].values
    )

    # Failure in all categories in previous timestamp.
    print(
        dbn_inf.forward_inference([basics_node_1], {
            basics_node_0: 1,
            conditionals_node_0: 1,
            loops_node_0: 1,
            arrays_node_0: 1,
            methods_node_0: 1,
            pre_defined_classes_node_0: 1,
            oop_node_0: 1
        })[basics_node_1].values
    )

    # Below is a variety of different tests.
    print(
        dbn_inf.forward_inference([oop_node_1], {
            basics_node_0: 1,
            conditionals_node_0: 1,
            loops_node_0: 1,
            arrays_node_0: 1,
            methods_node_0: 1,
            pre_defined_classes_node_0: 1,
        })[oop_node_1].values
    )

    print(
        dbn_inf.forward_inference([oop_node_1], {
            basics_node_0: 0,
            conditionals_node_0: 0,
            loops_node_0: 0,
            arrays_node_0: 0,
            methods_node_0: 0,
            pre_defined_classes_node_0: 0,
        })[oop_node_1].values
    )

    print(
        dbn_inf.forward_inference([oop_node_1], {
            basics_node_0: 0,
            conditionals_node_0: 0,
            loops_node_0: 0,
            arrays_node_0: 0,
            methods_node_0: 0,
            pre_defined_classes_node_0: 0,
            oop_node_0: 1
        })[oop_node_1].values
    )

    print(
        dbn_inf.forward_inference([oop_node_1], {
            basics_node_0: 0,
            conditionals_node_0: 1,
            loops_node_0: 0,
            arrays_node_0: 1,
            methods_node_0: 0,
            pre_defined_classes_node_0: 1,
        })[oop_node_1].values
    )

    print(
        dbn_inf.forward_inference([oop_node_1], {
            basics_node_0: 1,
            conditionals_node_0: 1,
            loops_node_0: 1,
            arrays_node_0: 1,
            methods_node_0: 1,
            pre_defined_classes_node_0: 1,
            oop_node_0: 0
        })[oop_node_1].values
    )


if __name__ == '__main__':
    parent_categories_model = parent_categories()
    test_inference(parent_categories_model)
