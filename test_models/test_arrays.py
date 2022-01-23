from matplotlib import pyplot as plt

from modelling import generate_arrays_bayesian_network


def test_arrays():
    model = generate_arrays_bayesian_network()
    model.plot()
    plt.show()


if __name__ == "__main__":
    test_arrays()
