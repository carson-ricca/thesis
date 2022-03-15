from pgmpy.inference import DBNInference

from dbn_modelling import performance_dbn
from util import Timer

performance_node_0 = ('Performance', 0)
correctness_node_0 = ('Correctness', 0)
skipped_question_node_0 = ('Skipped Question', 0)
time_taken_node_0 = ('Time Taken', 0)
performance_node_1 = ('Performance', 1)
correctness_node_1 = ('Correctness', 1)
skipped_question_node_1 = ('Skipped Question', 1)
time_taken_node_1 = ('Time Taken', 1)


def run_simulation():
    model = performance_dbn()
    timer = Timer()
    dbn_inf = DBNInference(model)
    results = []

    # No questions answered.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1])
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time, 'No questions answered.'))

    # The student skipped the first question they are presented with.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        skipped_question_node_1: 0,
        correctness_node_1: 1
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time, 'The student skipped the first question they are presented with.'))

    # The student takes a long time but gets the question correct.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        skipped_question_node_0: 0,
        correctness_node_0: 1,
        skipped_question_node_1: 1,
        correctness_node_1: 0,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time, 'The student takes a long time but gets the question correct.'))

    # The student gets the question correct again, and spent a long amount of time working on it again.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        skipped_question_node_0: 1,
        correctness_node_0: 0,
        time_taken_node_0: 0,
        skipped_question_node_1: 1,
        correctness_node_1: 0,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time,
                    'The student gets the question correct again, and spent a long amount of time working on it again.'))

    # The student then skips the question.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        skipped_question_node_0: 1,
        correctness_node_0: 0,
        time_taken_node_0: 0,
        skipped_question_node_1: 0,
        correctness_node_1: 1,
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time, 'The student then skips the question.'))

    # The student gets the question correct again, and spent a medium amount of time working on it.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        skipped_question_node_0: 0,
        correctness_node_0: 1,
        skipped_question_node_1: 1,
        correctness_node_1: 0,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time,
                    'The student gets the question correct again, and spent a medium amount of time working on it.'))

    # The student spends a medium amount of time on a question but gets it wrong.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        skipped_question_node_0: 1,
        correctness_node_0: 0,
        time_taken_node_0: 1,
        skipped_question_node_1: 1,
        correctness_node_1: 1,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    results.append(
        (inference_value, elapsed_time, 'The student spends a medium amount of time on a question but gets it wrong.'))

    # The student gets the question correct in a long amount of time.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        skipped_question_node_0: 1,
        correctness_node_0: 1,
        time_taken_node_0: 1,
        skipped_question_node_1: 1,
        correctness_node_1: 0,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time, 'The student gets the question correct in a long amount of time.'))

    # The student gets the question correct in a short amount of time.
    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        skipped_question_node_0: 1,
        correctness_node_0: 0,
        time_taken_node_0: 0,
        skipped_question_node_1: 1,
        correctness_node_1: 0,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    results.append((inference_value, elapsed_time, 'The student gets the question correct in a short amount of time.'))

    _display_results(results)


def _display_results(results):
    for result, time, situation in results:
        print(situation)
        print(
            f'Predicted Chance the Student is Successful: '
            f'{(result[performance_node_1].values[0] * 100):.2f}% and Elapsed Time: {time:0.4f} seconds\n'
        )


if __name__ == '__main__':
    run_simulation()
