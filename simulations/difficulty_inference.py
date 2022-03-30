difficulties = {
    0: 'EASY',
    1: 'MEDIUM',
    2: 'HARD'
}


def infer_question_difficulty(probability, current_difficulty):
    """
    Infers the difficulty of question for the user to practice based on the probability returned from the DBN.
    :param probability: The probability they are successful in a sub-category.
    :param current_difficulty: The current difficulty of question they completed.
    :return: The new difficulty they should practice.
    """
    if probability >= 80:
        new_difficulty = _increment_difficulty(current_difficulty)
    elif 50 > probability < 80:
        new_difficulty = current_difficulty
    else:
        new_difficulty = _decrement_difficulty(current_difficulty)
    return new_difficulty


def _increment_difficulty(difficulty):
    """
    A helper function when the difficulty should be increased.
    :param difficulty: The current difficulty.
    :return: The new difficulty.
    """
    if difficulty == 'EASY':
        return 'MEDIUM'
    elif difficulty == 'MEDIUM':
        return 'HARD'
    else:
        return 'HARD'


def _decrement_difficulty(difficulty):
    """
    A helper function when the difficulty should be decreased.
    :param difficulty: The current difficulty.
    :return: The new difficulty.
    :param difficulty:
    :return:
    """
    if difficulty == 'HARD':
        return 'MEDIUM'
    elif difficulty == 'MEDIUM':
        return 'EASY'
    else:
        return 'EASY'
