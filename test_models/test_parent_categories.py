from modelling import generate_parent_categories_bayesian_network


def test_parent_categories():
    model = generate_parent_categories_bayesian_network()
    _make_prediction(model, 'Success', 'Success', 'Success', 'Success', 'Success', 'Success', 'Success')


def _make_prediction(model, basics, conditionals, pre_defined_classes, loops, arrays, methods, oop):
    predictions = model.predict_proba({
        'Basics': basics,
        'Conditionals': conditionals,
        'Pre-Defined Classes': pre_defined_classes,
        'Loops': loops,
        'Arrays': arrays,
        'Methods': methods,
        'OOP': oop
    })
    category_success = predictions[0].parameters[0]
    success = category_success['Success']
    failure = category_success['Failure']
    print(
        f'Basics: {basics}, Conditionals: {conditionals}, Pre-Defined Classes: {pre_defined_classes}, Loops: {loops}, Arrays: {arrays}, Methods: {methods}, OOP: {oop}')
    print(f'Success: {success}, Failure: {failure}')
    print('-' * 150)


if __name__ == "__main__":
    test_parent_categories()
