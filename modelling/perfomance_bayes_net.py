from pomegranate import *
from constants import high, medium, low, long, short


def generate_performance_bayesian_network():
    """
    Creates the Bayesian Network for the student's performance within a sub-category.
    :return: The complete Bayesian Network.
    """
    overall_performance = _get_overall_performance_probability()
    average_success = _get_average_success_probability(overall_performance)
    skip_questions = _get_skip_questions_probability(overall_performance)
    time_taken = _get_time_taken_probability(overall_performance)

    s1 = Node(overall_performance, name='Overall Performance')
    s2 = Node(average_success, name='Average Success')
    s3 = Node(skip_questions, name='Skip Questions')
    s4 = Node(time_taken, name='Time Taken')

    model = BayesianNetwork('Student Performance')
    model.add_states(s1, s2, s3, s4)
    model.add_edge(s1, s2)
    model.add_edge(s1, s3)
    model.add_edge(s1, s4)
    model.bake()
    return model


def _get_overall_performance_probability():
    """
    Gets the probability for the Overall Performance node.
    :return: The probability for the Overall Performance node.
    """
    return DiscreteDistribution({high: 1 / 3, medium: 1 / 3, low: 1 / 3})


def _get_average_success_probability(overall_performance):
    """
    Gets the probability for the Average Success node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Average Success node.
    """
    return ConditionalProbabilityTable([
        [high, high, 0.75],
        [high, medium, 0.2],
        [high, low, 0.05],
        [medium, high, 0.5],
        [medium, medium, 0.4],
        [medium, low, 0.1],
        [low, high, 0.1],
        [low, medium, 0.3],
        [low, low, 0.6],
    ], [overall_performance])


def _get_skip_questions_probability(overall_performance):
    """
    Gets the probability for the Skip Questions node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Skip Questions node.
    """
    return ConditionalProbabilityTable([
        [high, high, 0.1],
        [high, medium, 0.2],
        [high, low, 0.7],
        [medium, high, 0.2],
        [medium, medium, 0.4],
        [medium, low, 0.4],
        [low, high, 0.5],
        [low, medium, 0.3],
        [low, low, 0.2],
    ], [overall_performance])


def _get_time_taken_probability(overall_performance):
    """
    Gets the probability for the Time Taken node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Time Taken node.
    """
    return ConditionalProbabilityTable([
        [high, long, 0.1],
        [high, medium, 0.3],
        [high, short, 0.6],
        [medium, long, 0.2],
        [medium, medium, 0.5],
        [medium, short, 0.3],
        [low, long, 0.5],
        [low, medium, 0.4],
        [low, short, 0.1],
    ], [overall_performance])
