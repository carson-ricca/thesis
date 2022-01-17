from modelling import generate_performance_bayesian_network


def test_overall_performance():
    model = generate_performance_bayesian_network()
    # High average success, low skip questions, short time taken.
    _make_prediction(model, 'High', 'Low', 'Short')
    # Low average success, high skip questions, long time taken.
    _make_prediction(model, 'Low', 'High', 'Long')
    # Medium average success, medium skip questions, medium time taken.
    _make_prediction(model, 'Medium', 'Medium', 'Medium')
    # High average success, high skip questions, long time taken.
    _make_prediction(model, 'High', 'High', 'Long')
    # Low average success, low skip questions, short time taken.
    _make_prediction(model, 'Low', 'Low', 'Short')
    # Medium average success, low skip questions, short time taken.
    _make_prediction(model, 'Medium', 'Low', 'Short')
    # Medium average success, high skip questions, long time taken.
    _make_prediction(model, 'Medium', 'High', 'Low')


def _make_prediction(model, average_success, skip_questions, time_taken):
    predictions = model.predict_proba({
        'Average Success': average_success,
        'Skip Questions': skip_questions,
        'Time Taken': time_taken
    })
    overall_success = predictions[0].parameters[0]
    high_success = overall_success['High']
    medium_success = overall_success['Medium']
    low_success = overall_success['Low']
    print(f'Average Success: {average_success}, Skip Questions: {skip_questions}, Time Taken: {time_taken}')
    print(f'High Success: {high_success}, Medium Success: {medium_success}, Low Success: {low_success}')
    print('-' * 150)


if __name__ == "__main__":
    test_overall_performance()
