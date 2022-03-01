import pgmpy.models as md
import pgmpy.inference as inf
from pgmpy.factors.discrete import TabularCPD


def main():
    overall_performance_node_0 = ('Overall Performance', 0)
    overall_performance_node_1 = ('Overall Performance', 1)
    success_node_0 = ('Success', 0)
    success_node_1 = ('Success', 1)
    skipped_question_node_0 = ('Skipped Question', 0)
    skipped_question_node_1 = ('Skipped Question', 1)
    time_taken_node_0 = ('Time Taken', 0)
    time_taken_node_1 = ('Time Taken', 1)

    model = md.DynamicBayesianNetwork(
        [(overall_performance_node_0, success_node_0), (overall_performance_node_0, skipped_question_node_0),
         (overall_performance_node_0, time_taken_node_0), (overall_performance_node_0, overall_performance_node_1),
         (success_node_0, success_node_1), (skipped_question_node_0, skipped_question_node_1),
         (time_taken_node_0, time_taken_node_1), (overall_performance_node_1, success_node_1),
         (overall_performance_node_1, skipped_question_node_1), (overall_performance_node_1, time_taken_node_1)])

    overall_performance_cpt = TabularCPD(overall_performance_node_0, 2, [
        [0.5], [0.5]
    ])

    success_cpt = TabularCPD(success_node_0, 2, [
        [0.8, 0.1],
        [0.2, 0.9]
    ], evidence=[overall_performance_node_0], evidence_card=[2])

    skipped_question_cpt = TabularCPD(skipped_question_node_0, 2, [
        [0.3, 0.9],
        [0.7, 0.1]
    ], evidence=[overall_performance_node_0], evidence_card=[2])

    time_taken_cpt = TabularCPD(time_taken_node_0, 3, [
        [0.2, 0.6],
        [0.4, 0.3],
        [0.4, 0.1]
    ], evidence=[overall_performance_node_0], evidence_card=[2])

    overall_performance_transition_cpt = TabularCPD(overall_performance_node_1, 2, [
        [0.7, 0.3],
        [0.3, 0.7]
    ], evidence=[overall_performance_node_0], evidence_card=[2])

    success_transition_cpt = TabularCPD(success_node_1, 2, [
        [0.7, 0.3],
        [0.3, 0.7]
    ], evidence=[success_node_0], evidence_card=[2])

    skipped_question_transitional_cpt = TabularCPD(skipped_question_node_1, 2, [
        [0.6, 0.4],
        [0.4, 0.6]
    ], evidence=[skipped_question_node_0], evidence_card=[2])

    time_taken_transitional_cpt = TabularCPD(time_taken_node_1, 3, [
        [0.6, 0.2, 0.1],
        [0.3, 0.5, 0.2],
        [0.1, 0.3, 0.7]
    ], evidence=[time_taken_node_0], evidence_card=[3])

    model.add_cpds(overall_performance_cpt, success_cpt, skipped_question_cpt, time_taken_cpt,
                   overall_performance_transition_cpt, success_transition_cpt, skipped_question_transitional_cpt,
                   time_taken_transitional_cpt)
    model.initialize_initial_state()
    model.check_model()

    dbn_inf = inf.DBNInference(model)

    # Successful on a question.
    print(
        dbn_inf.forward_inference([overall_performance_node_1], {success_node_0: 1})[overall_performance_node_1].values
    )

    # Not successful on a question.
    print(
        dbn_inf.forward_inference([overall_performance_node_1], {success_node_0: 0})[overall_performance_node_1].values
    )

    # Successful on a question no skipped question.
    print(
        dbn_inf.forward_inference([overall_performance_node_1], {success_node_0: 1, skipped_question_node_0: 0})[
            overall_performance_node_1].values
    )

    # Skipped the question.
    print(
        dbn_inf.forward_inference([overall_performance_node_1], {skipped_question_node_0: 1})[
            overall_performance_node_1].values
    )


if __name__ == '__main__':
    main()
