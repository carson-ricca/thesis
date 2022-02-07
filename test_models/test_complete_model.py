import matplotlib.pyplot as plt

from constants import success, failure
from modelling import generate_complete_bayesian_network
from util import Timer


def test_complete_model():
    model = generate_complete_bayesian_network()
    # Uncomment these lines to visually plot the model.
    # model.plot()
    # plt.show()

    timer = Timer()
    timer.start()
    predictions = model.predict_proba({'Basics': success})
    timer.stop()
    print(len(predictions))
    print(predictions)


if __name__ == '__main__':
    test_complete_model()
