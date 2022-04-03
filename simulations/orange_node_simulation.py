import pandas as pd
from pgmpy.inference import DBNInference
from matplotlib import pyplot as plt
from prettytable import PrettyTable

from constants import Difficulties
from dbn_modelling import performance_dbn
from simulations.difficulty_inference import infer_question_difficulty
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
    """
    Run the simulation to test the overall performance (orange nodes) for any sub-category (blue node).
    """
    model = performance_dbn()
    timer = Timer()
    dbn_inf = DBNInference(model)

    print('User 1')
    user_one_results = _user_one(dbn_inf, timer)
    _display_results(user_one_results)
    _difficulty_data_table(user_one_results)

    print('User 2')
    user_two_results = _user_two(dbn_inf, timer)
    _display_results(user_two_results)
    _difficulty_data_table(user_two_results)

    print('User 3')
    user_three_results = _user_three(dbn_inf, timer)
    _display_results(user_three_results)
    _difficulty_data_table(user_three_results)

    print('User 4')
    user_four_results = _user_four(dbn_inf, timer)
    _display_results(user_four_results)
    _difficulty_data_table(user_four_results)

    print('User 5')
    user_five_results = _user_five(dbn_inf, timer)
    _display_results(user_five_results)
    _difficulty_data_table(user_five_results)

    print('User 6')
    user_six_results = _user_six(dbn_inf, timer)
    _display_results(user_six_results)
    _difficulty_data_table(user_six_results)

    return [user_one_results, user_two_results, user_three_results, user_four_results, user_five_results,
            user_six_results]


def _plot_probability_data(user_results, output_path):
    """
    Plot the overall performance data on a graph.
    :param user_results: The results of the simulation.
    :param output_path: The path to save the figure to.
    """
    user_number = 1
    data = {
        'Question #': [0, 1, 2, 3, 4, 5]
    }
    for user in user_results:
        probabilities = [50]
        for probability, time, current_difficulty, difficulty in user:
            probabilities.append(probability[performance_node_1].values[0] * 100)
        data[f'User {user_number}'] = probabilities
        user_number += 1

    df = pd.DataFrame(data)
    ax = plt.gca()
    df.plot(kind='line', x='Question #', y='User 1', ax=ax, x_compat=True)
    df.plot(kind='line', x='Question #', y='User 2', ax=ax, x_compat=True)
    df.plot(kind='line', x='Question #', y='User 3', ax=ax, x_compat=True)
    df.plot(kind='line', x='Question #', y='User 4', ax=ax, x_compat=True)
    df.plot(kind='line', x='Question #', y='User 5', ax=ax, x_compat=True)
    plt.xticks(data['Question #'])
    plt.ylabel('Probability of Success')
    plt.ylim(0, 100)
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()


def _difficulty_data_table(results):
    """
    Display the predicted difficulty results in a table.
    :param results: The results of the simulation.
    """
    user_number = 1
    table = PrettyTable(
        ['Question', 'Probability of Success', 'Current Difficulty', 'Recommended Difficulty for Next Question']
    )
    for question in results:
        table.add_row(
            [user_number, f'{(question[0][performance_node_1].values[0] * 100):.2f}%', question[2], question[3]]
        )
        user_number += 1
    print(table)


def _user_one(dbn_inf, timer):
    """
    This student regularly solves the questions successfully in a short amount of time.
    :param dbn_inf: The dbn to perform inference on.
    :param timer: The timer class to keep track of how long inference takes.
    :return: A dictionary containing the probabilities and times for this user.
    """
    results = []
    current_difficulty = 'EASY'

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    return results


def _user_two(dbn_inf, timer):
    """
    This student regularly solves the questions successfully in a long amount of time.
    :param dbn_inf: The dbn to perform inference on.
    :param timer: The timer class to keep track of how long inference takes.
    :return: A dictionary containing the probabilities and times for this user.
    """
    results = []
    current_difficulty = 'EASY'

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    return results


def _user_three(dbn_inf, timer):
    """
    This student regularly gets the questions wrong in a short amount of time.
    :param dbn_inf: The dbn to perform inference on.
    :param timer: The timer class to keep track of how long inference takes.
    :return: A dictionary containing the probabilities and times for this user.
    """
    results = []
    current_difficulty = 'EASY'

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    return results


def _user_four(dbn_inf, timer):
    """
    This student regularly gets the questions wrong in a long amount of time.
    :param dbn_inf: The dbn to perform inference on.
    :param timer: The timer class to keep track of how long inference takes.
    :return: A dictionary containing the probabilities and times for this user.
    """
    results = []
    current_difficulty = 'EASY'

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    return results


def _user_five(dbn_inf, timer):
    """
    This student gets a question incorrect, then correct, and so on.
    :param dbn_inf: The dbn to perform inference on.
    :param timer: The timer class to keep track of how long inference takes.
    :return: A dictionary containing the probabilities and times for this user.
    """
    results = []
    current_difficulty = 'EASY'

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 2
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 0
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 0,
        skipped_question_node_1: 1,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 0,
        correctness_node_1: 1,
        skipped_question_node_1: 1,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    return results


def _user_six(dbn_inf, timer):
    """
    This student skips a bunch of questions in a row.
    :param dbn_inf: The dbn to perform inference on.
    :param timer: The timer class to keep track of how long inference takes.
    :return: A dictionary containing the probabilities and times for this user.
    """
    results = []
    current_difficulty = 'EASY'

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        correctness_node_1: 1,
        skipped_question_node_1: 0,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 0,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 0,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 0,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    current_difficulty = difficulty

    timer.start()
    inference_value = dbn_inf.forward_inference([performance_node_1], {
        performance_node_0: 1,
        correctness_node_1: 1,
        skipped_question_node_1: 0,
        time_taken_node_1: 1
    })
    elapsed_time = timer.stop()
    difficulty = infer_question_difficulty(inference_value[performance_node_1].values[0] * 100, current_difficulty)
    results.append((inference_value, elapsed_time, current_difficulty, difficulty))
    return results


def _display_results(results):
    """
    Display the results to the terminal.
    :param results: The results of the simulation.
    """
    for result, time, current_difficulty, difficulty in results:
        print(
            f'Predicted Chance the Student is Successful: '
            f'{(result[performance_node_1].values[0] * 100):.2f}%, Current Difficulty: {current_difficulty}'
            f', Suggested Difficulty: {difficulty}'
            f', and Elapsed Time: {time:0.4f} seconds'
        )


if __name__ == '__main__':
    simulation_results = run_simulation()
    _plot_probability_data(simulation_results, '../graphs/probability-graph.png')
