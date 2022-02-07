import matplotlib.pyplot as plt

from constants import success, failure
from modelling import generate_complete_bayesian_network
from util import Timer


def test_complete_model():
    model = generate_complete_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()


def _run_inference(model, data, estimated_node):
    timer = Timer()
    timer.start()
    predictions = model.predict_proba(data)
    timer.stop()
    print(predictions[NODE_ORDER.get(estimated_node)].parameters[0][success])
    print('-' * 150)


if __name__ == '__main__':
    test_complete_model()
