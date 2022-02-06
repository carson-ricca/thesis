from pomegranate import *
from constants import high, medium, low, long, short, success, failure


def generate_performance_bayesian_network():
    """
    Creates the Bayesian Network for the student's performance within a sub-category.
    :return: The complete Bayesian Network.
    """
    overall_performance = _get_overall_performance_probability()
    average_success = _get_average_success_probability(overall_performance)
    skip_questions = _get_skip_questions_probability(overall_performance)
    time_taken = _get_time_taken_probability(overall_performance)

    overall_performance_node = State(overall_performance, name='Overall Performance')
    average_success_node = State(average_success, name='Average Success')
    skip_questions_node = State(skip_questions, name='Skip Questions')
    time_taken_node = State(time_taken, name='Time Taken')

    model = BayesianNetwork('Student Performance')
    model.add_states(overall_performance_node, average_success_node, skip_questions_node, time_taken_node)
    model.add_edge(overall_performance_node, average_success_node)
    model.add_edge(overall_performance_node, skip_questions_node)
    model.add_edge(overall_performance_node, time_taken_node)
    model.bake()
    return model


def _get_overall_performance_probability():
    """
    Gets the probability for the Overall Performance node.
    :return: The probability for the Overall Performance node.
    """
    return DiscreteDistribution({success: 0.5, failure: 0.5})


def _get_average_success_probability(overall_performance):
    """
    Gets the probability for the Average Success node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Average Success node.
    """
    return ConditionalProbabilityTable([
        [success, high, 0.75],
        [success, medium, 0.2],
        [success, low, 0.05],
        [failure, high, 0.2],
        [failure, medium, 0.2],
        [failure, low, 0.6],
    ], [overall_performance])


def _get_skip_questions_probability(overall_performance):
    """
    Gets the probability for the Skip Questions node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Skip Questions node.
    """
    return ConditionalProbabilityTable([
        [success, high, 0.1],
        [success, medium, 0.2],
        [success, low, 0.7],
        [failure, high, 0.4],
        [failure, medium, 0.4],
        [failure, low, 0.2],
    ], [overall_performance])


def _get_time_taken_probability(overall_performance):
    """
    Gets the probability for the Time Taken node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Time Taken node.
    """
    return ConditionalProbabilityTable([
        [success, long, 0.1],
        [success, medium, 0.3],
        [success, short, 0.6],
        [failure, long, 0.4],
        [failure, medium, 0.4],
        [failure, short, 0.2],
    ], [overall_performance])
