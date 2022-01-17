from pomegranate import *


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
    return DiscreteDistribution({'High': 1 / 3, 'Medium': 1 / 3, 'Low': 1 / 3})


def _get_average_success_probability(overall_performance):
    """
    Gets the probability for the Average Success node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Average Success node.
    """
    return ConditionalProbabilityTable([
        ['High', 'High', 0.75],
        ['High', 'Medium', 0.2],
        ['High', 'Low', 0.05],
        ['Medium', 'High', 0.5],
        ['Medium', 'Medium', 0.4],
        ['Medium', 'Low', 0.1],
        ['Low', 'High', 0.1],
        ['Low', 'Medium', 0.3],
        ['Low', 'Low', 0.6],
    ], [overall_performance])


def _get_skip_questions_probability(overall_performance):
    """
    Gets the probability for the Skip Questions node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Skip Questions node.
    """
    return ConditionalProbabilityTable([
        ['High', 'High', 0.1],
        ['High', 'Medium', 0.2],
        ['High', 'Low', 0.7],
        ['Medium', 'High', 0.2],
        ['Medium', 'Medium', 0.4],
        ['Medium', 'Low', 0.4],
        ['Low', 'High', 0.5],
        ['Low', 'Medium', 0.3],
        ['Low', 'Low', 0.2],
    ], [overall_performance])


def _get_time_taken_probability(overall_performance):
    """
    Gets the probability for the Time Taken node.
    :param overall_performance: The probability for the Overall Performance node.
    :return: The probability for the Time Taken node.
    """
    return ConditionalProbabilityTable([
        ['High', 'Long', 0.1],
        ['High', 'Medium', 0.3],
        ['High', 'Short', 0.6],
        ['Medium', 'Long', 0.2],
        ['Medium', 'Medium', 0.5],
        ['Medium', 'Short', 0.3],
        ['Low', 'Long', 0.5],
        ['Low', 'Medium', 0.4],
        ['Low', 'Short', 0.1],
    ], [overall_performance])
