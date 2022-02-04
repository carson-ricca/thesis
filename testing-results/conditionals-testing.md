# Conditionals Testing

```
print('Conditionals')
    _run_inference(model, {
        'Boolean': success,
        'Decision': success,
        'Operators': success,
        'Conditional Statements': success,
        'Nested Conditional Statements': success,
        'Simple Programs': success,
        'Programs': success
    }, 'Conditionals')
```

- Time: 0.0015 seconds
- Predicted Success: 0.94

```
print('Conditionals')
    _run_inference(model, {
        'Boolean': failure,
        'Decision': failure,
        'Operators': failure,
        'Conditional Statements': success,
        'Nested Conditional Statements': success,
    }, 'Conditionals')
```

- Time: 0.0034 seconds
- Predicted Success: 0.17

```
print('Programs')
    _run_inference(model, {
        'Conditionals': success,
        'Boolean': success,
    }, 'Programs')
```

- Time: 0.0042 seconds
- Predicted Success: 0.81

```
print('Operators')
    _run_inference(model, {
        'Conditionals': success,
        'Boolean': failure,
        'Decision': success,
        'Conditional Statements': success,
        'Nested Conditional Statements': success,
        'Simple Programs': success,
        'Programs': failure
    }, 'Operators')
```

- Time: 0.0015 seconds
- Predicted Success: 0.76