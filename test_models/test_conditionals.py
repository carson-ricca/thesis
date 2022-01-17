from modelling import generate_conditionals_bayesian_network


def test_conditionals():
    model = generate_conditionals_bayesian_network()

    predictions = model.predict_proba({
        'Conditionals': 'Success'
    })
    overall_success = predictions[0].parameters[0]
    print(f'Success: {overall_success["Success"]}, Failure: {overall_success["Failure"]}')
    print('-' * 150)


if __name__ == "__main__":
    test_conditionals()
