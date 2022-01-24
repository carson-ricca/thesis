from matplotlib import pyplot as plt

from modelling import generate_methods_bayesian_network


def test_methods():
    model = generate_methods_bayesian_network()
    model.plot()
    plt.show()


if __name__ == "__main__":
    test_methods()
