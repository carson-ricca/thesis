from modelling import generate_performance_bayesian_network
from constants import high, medium, low, short, long


def test_overall_performance():
    model = generate_performance_bayesian_network()
    # High average success, low skip questions, short time taken.
    _make_prediction(model, high, low, short)
    # Low average success, high skip questions, long time taken.
    _make_prediction(model, low, high, long)
    # Medium average success, medium skip questions, medium time taken.
    _make_prediction(model, medium, medium, medium)
    # High average success, high skip questions, long time taken.
    _make_prediction(model, high, high, long)
    # Low average success, low skip questions, short time taken.
    _make_prediction(model, low, low, short)
    # Medium average success, low skip questions, short time taken.
    _make_prediction(model, medium, low, short)
    # Medium average success, high skip questions, long time taken.
    _make_prediction(model, medium, high, low)


def _make_prediction(model, average_success, skip_questions, time_taken):
    predictions = model.predict_proba({
        'Average Success': average_success,
        'Skip Questions': skip_questions,
        'Time Taken': time_taken
    })
    overall_success = predictions[0].parameters[0]
    high_success = overall_success[high]
    medium_success = overall_success[medium]
    low_success = overall_success[low]
    print(f'Average Success: {average_success}, Skip Questions: {skip_questions}, Time Taken: {time_taken}')
    print(f'High Success: {high_success}, Medium Success: {medium_success}, Low Success: {low_success}')
    print('-' * 150)


if __name__ == "__main__":
    test_overall_performance()
