import pgmpy.models as md
import pgmpy.inference as inf
from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork

from constants import success, failure


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
    performance_node = 'Performance'
    correctness_node = 'Correctness'
    skipped_question_node = 'Skipped Question'
    time_taken_node = 'Time Taken'

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
        [0.9, 0.2]
    ], evidence=[performance_node], evidence_card=[2])

    time_taken_cpd = TabularCPD(time_taken_node, 3, [
        [0.1, 0.4],
        [0.3, 0.4],
        [0.6, 0.2]
    ], evidence=[performance_node], evidence_card=[2])

    model.add_cpds(performance_cpd, correctness_cpd, skipped_question_cpd, time_taken_cpd)

    for cpd in model.get_cpds():
        print(cpd)


if __name__ == '__main__':
    performance_dbn()
