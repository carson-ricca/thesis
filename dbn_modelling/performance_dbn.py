import pgmpy.models as md
import pgmpy.inference as inf
from pgmpy.factors.discrete import TabularCPD

from constants import success, failure


def main():
    model = md.DynamicBayesianNetwork(
        [(('Overall Performance', 0), ('Success', 0)), (('Overall Performance', 0), ('Skipped Question', 0)),
         (('Overall Performance', 0), ('Time Taken', 0)), (('Overall Performance', 0), ('Overall Performance', 1))])

    overall_performance_cpt = TabularCPD(('Overall Performance', 0), 2, [
        [0.5], [0.5]
    ])

    success_cpt = TabularCPD(('Success', 0), 2, [
        [0.8, 0.1],
        [0.2, 0.9]
    ], evidence=[('Overall Performance', 0)], evidence_card=[2])

    skipped_question_cpt = TabularCPD(('Skipped Question', 0), 2, [
        [0.8, 0.1],
        [0.2, 0.9]
    ], evidence=[('Overall Performance', 0)], evidence_card=[2])

    time_taken_cpt = TabularCPD(('Time Taken', 0), 3, [
        [0.2, 0.6],
        [0.4, 0.3],
        [0.4, 0.1]
    ], evidence=[('Overall Performance', 0)], evidence_card=[2])

    overall_performance_transition_cpt = TabularCPD(('Overall Performance', 1), 2, [
        [0.7, 0.3],
        [0.3, 0.7]
    ], evidence=[('Overall Performance', 0)], evidence_card=[2])

    model.add_cpds(overall_performance_cpt, success_cpt, skipped_question_cpt, time_taken_cpt,
                   overall_performance_transition_cpt)
    model.initialize_initial_state()
    model.check_model()

    dbn_inf = inf.DBNInference(model)

    # Successful on a question.
    print(
        dbn_inf.forward_inference([('Overall Performance', 1)], {('Success', 0): 1})[('Overall Performance', 1)].values
    )

    # Not successful on a question.
    print(
        dbn_inf.forward_inference([('Overall Performance', 1)], {('Success', 0): 0})[('Overall Performance', 1)].values
    )

    # Successful on a question no skipped question.
    print(
        dbn_inf.forward_inference([('Overall Performance', 1)], {('Success', 0): 1, ('Skipped Question', 0): 0})[
            ('Overall Performance', 1)].values
    )

    # Skipped the question.
    print(
        dbn_inf.forward_inference([('Overall Performance', 1)], {('Skipped Question', 1): 0})[
            ('Overall Performance', 1)].values
    )


if __name__ == '__main__':
    main()
