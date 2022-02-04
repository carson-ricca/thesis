# Basics Testing

```
print('Basics')
    _run_inference(model, {
        'Variables': success,
        'Data Types': failure,
        'Statements': success,
        'Constants': failure,
        'Arithmetic Operators': success,
        'Casting': success,
        'Simple Calculation Problems': success
    }, 'Basics')
```

- Time: 0.0015 seconds
- Predicted Success: 0.94

```
print('Simple Calculation Problems')
    _run_inference(model, {
        'Basics': success,
        'Variables': success,
        'Data Types': success,
        'Statements': failure,
        'Constants': success,
        'Arithmetic Operators': failure,
        'Casting': success,
    }, 'Simple Calculation Problems')
```

- Time: 0.0015 seconds
- Predicted Success: 0.8

```
print('Constants')
    _run_inference(model, {
        'Basics': failure,
        'Variables': failure,
        'Data Types': success,
        'Statements': success,
    }, 'Constants')
```

- Time: 0.0025 seconds
- Predicted Success: 0.1

```
print('Casting')
    _run_inference(model, {
        'Basics': success,
        'Variables': success,
        'Data Types': failure,
        'Statements': failure,
        'Constants': failure,
        'Arithmetic Operators': failure,
        'Simple Calculation Problems': success
    }, 'Casting')
```

- Time: 0.0015 seconds
- Predicted Success: 0.6