from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference
from pgmpy.models import DynamicBayesianNetwork

performance_node_0 = ('Performance', 0)
correctness_node_0 = ('Correctness', 0)
skipped_question_node_0 = ('Skipped Question', 0)
time_taken_node_0 = ('Time Taken', 0)
performance_node_1 = ('Performance', 1)
correctness_node_1 = ('Correctness', 1)
skipped_question_node_1 = ('Skipped Question', 1)
time_taken_node_1 = ('Time Taken', 1)


def performance_dbn():
    """
    Generates the normal bayes net for the performance model (orange).

    CPD KEY NAMES:
    Performance: 0 - Success, 1 - Failure
    Correctness: 0 - Success, 1 - Failure
    Skipped Question: 0 - Yes, 1 - No
    Time Taken: Long - 0, Medium - 1, Short - 2
    :return: The generated model.
    """
    model = DynamicBayesianNetwork([
        (performance_node_0, correctness_node_0),
        (performance_node_0, skipped_question_node_0),
        (performance_node_0, time_taken_node_0),
        (performance_node_0, performance_node_1),
        (performance_node_1, correctness_node_1),
        (performance_node_1, skipped_question_node_1),
        (performance_node_1, time_taken_node_1),
    ])

    performance_cpd = TabularCPD(performance_node_0, 2, [
        [0.5], [0.5]
    ])

    correctness_cpd = TabularCPD(correctness_node_0, 2, [
        [0.9, 0.2],
        [0.1, 0.8]
    ], evidence=[performance_node_0], evidence_card=[2])

    skipped_question_cpd = TabularCPD(skipped_question_node_0, 2, [
        [0.5, 0.5],
        [0.5, 0.5]
    ], evidence=[performance_node_0], evidence_card=[2])

    time_taken_cpd = TabularCPD(time_taken_node_0, 3, [
        [0.1, 0.3],
        [0.4, 0.4],
        [0.5, 0.3]
    ], evidence=[performance_node_0], evidence_card=[2])

    performance_transitional_cpd = TabularCPD(performance_node_1, 2, [
        [0.8, 0.3],
        [0.2, 0.7]
    ], evidence=[performance_node_0], evidence_card=[2])

    model.add_cpds(performance_cpd, correctness_cpd, skipped_question_cpd, time_taken_cpd, performance_transitional_cpd)
    model.initialize_initial_state()
    model.check_model()
    return model


if __name__ == '__main__':
    performance_model = performance_dbn()
