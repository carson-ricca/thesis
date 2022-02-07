# Loops Testing

```
print('Loops')
    _run_inference(model, {
        'Repetition': failure,
        'Decision Diagrams': failure,
        'While Loops': success,
        'For Loops': success,
        'Variable Scope': success,
        'Simple Programs': success,
        'Nested Loops': success,
        'Programs': success
    }, 'Loops')
```

- Time: 0.0021 seconds
- Predicted Success: 0.93

```
print('Programs')
    _run_inference(model, {
        'Loops': success,
        'Repetition': success,
        'Decision Diagrams': failure,
        'While Loops': success,
        'For Loops': failure,
        'Variable Scope': success,
        'Simple Programs': failure,
        'Nested Loops': success,
    }, 'Programs')
```

- Time: 0.002 seconds
- Predicted Success: 0.7

```
print('Simple Programs')
    _run_inference(model, {
        'Loops': success,
        'Repetition': success,
        'Decision Diagrams': failure,
        'Variable Scope': success,
    }, 'Simple Programs')
```

- Time: 0.0045 seconds
- Predicted Success: 0.89

```
print('Nested Loops')
    _run_inference(model, {
        'Loops': failure,
        'Repetition': failure,
    }, 'Nested Loops')
```

- Time: 0.0059 seconds
- Predicted Success: 0.19