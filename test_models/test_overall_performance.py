from modelling import generate_performance_bayesian_network
from constants import high, medium, low, short, long, success, failure
from util import Timer

NODE_ORDER = {
    'Overall Performance': 0,
    'Average Success': 1,
    'Skip Questions': 2,
    'Time Taken': 3
}


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

    print('Overall Performance')
    _run_inference(model, {
        'Average Success': high,
        'Skip Questions': low,
        'Time Taken': short
    }, 'Overall Performance')

    print('Overall Performance')
    _run_inference(model, {
        'Average Success': high,
        'Skip Questions': high,
        'Time Taken': long
    }, 'Overall Performance')

    print('Overall Performance')
    _run_inference(model, {
        'Average Success': low,
        'Skip Questions': medium,
        'Time Taken': medium
    }, 'Overall Performance')

    print('Overall Performance')
    _run_inference(model, {
        'Average Success': high,
        'Skip Questions': high,
        'Time Taken': short
    }, 'Overall Performance')


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


def _make_prediction(model, average_success, skip_questions, time_taken):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba({
        'Average Success': average_success,
        'Skip Questions': skip_questions,
        'Time Taken': time_taken
    })
    overall_success = predictions[0].parameters[0]
    print(f'Average Success: {average_success}, Skip Questions: {skip_questions}, Time Taken: {time_taken}')
    print(f'Success: {overall_success[success]}, Failure: {overall_success[failure]}')
    timer.stop()
    print('-' * 150)


if __name__ == "__main__":
    test_overall_performance()
