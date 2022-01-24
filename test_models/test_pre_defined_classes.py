from matplotlib import pyplot as plt

from modelling import generate_pre_defined_classes_bayesian_network


def test_pre_defined_classes():
    model = generate_pre_defined_classes_bayesian_network()
    model.plot()
    plt.show()


if __name__ == "__main__":
    test_pre_defined_classes()
