import matplotlib.pyplot as plt

from modelling import generate_oop_bayesian_network


def test_oop():
    model = generate_oop_bayesian_network()
    model.plot()
    plt.show()


if __name__ == "__main__":
    test_oop()
