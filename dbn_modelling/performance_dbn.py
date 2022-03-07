from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import BeliefPropagation
from pgmpy.models import BayesianNetwork

performance_node = 'Performance'
correctness_node = 'Correctness'
skipped_question_node = 'Skipped Question'
time_taken_node = 'Time Taken'


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
    model = BayesianNetwork([
        (performance_node, correctness_node),
        (performance_node, skipped_question_node),
        (performance_node, time_taken_node)
    ])

    performance_cpd = TabularCPD(performance_node, 2, [
        [0.5], [0.5]
    ])

    correctness_cpd = TabularCPD(correctness_node, 2, [
        [0.9, 0.2],
        [0.1, 0.8]
    ], evidence=[performance_node], evidence_card=[2])

    skipped_question_cpd = TabularCPD(skipped_question_node, 2, [
        [0.1, 0.7],
        [0.9, 0.3]
    ], evidence=[performance_node], evidence_card=[2])

    time_taken_cpd = TabularCPD(time_taken_node, 3, [
        [0.1, 0.4],
        [0.3, 0.4],
        [0.6, 0.2]
    ], evidence=[performance_node], evidence_card=[2])

    model.add_cpds(performance_cpd, correctness_cpd, skipped_question_cpd, time_taken_cpd)
    return model


def test_inference(model):
    bp = BeliefPropagation(model)

    # Correct, not skipped, short time.
    print(bp.query([performance_node], {
        correctness_node: 0,
        skipped_question_node: 1,
        time_taken_node: 2
    }))

    # Skipped, short time.
    print(bp.query([performance_node], {
        skipped_question_node: 0,
        time_taken_node: 2
    }))

    # Correct, not skipped, long time.
    print(bp.query([performance_node], {
        correctness_node: 0,
        skipped_question_node: 1,
        time_taken_node: 0
    }))

    # Incorrect, not skipped, short time.
    print(bp.query([performance_node], {
        correctness_node: 1,
        skipped_question_node: 1,
        time_taken_node: 2
    }))

    # Correct, not skipped, medium time.
    print(bp.query([performance_node], {
        correctness_node: 0,
        skipped_question_node: 1,
        time_taken_node: 1
    }))

    # Correct.
    print(bp.query([performance_node], {
        correctness_node: 0
    }))


if __name__ == '__main__':
    performance_model = performance_dbn()
    test_inference(performance_model)
