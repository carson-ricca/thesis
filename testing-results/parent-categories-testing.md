# Parent Categories Testing

```
print('OOP')
    _run_inference(model, {
        'Basics': success,
        'Conditionals': success,
        'Pre-Defined Classes': success,
        'Loops': success,
        'Arrays': success,
        'Methods': success,
    }, 'OOP')
```

- Time: 0.0007 seconds
- Predicted Success: 0.9

```
print('OOP')
    _run_inference(model, {
        'Basics': success,
        'Conditionals': success,
    }, 'OOP')
```

- Time: 0.0016 seconds
- Predicted Success: 0.65

```
print('Loops')
    _run_inference(model, {
        'Basics': success,
        'Conditionals': failure,
        'Pre-Defined Classes': success,
        'Arrays': success,
        'Methods': success,
        'OOP': failure
    }, 'Loops')
```

- Time: 0.0007 seconds
- Predicted Success: 0.75

```
print('Methods')
    _run_inference(model, {
        'Basics': failure,
        'Conditionals': failure,
        'Loops': success,
        'Arrays': success,
        'OOP': failure
    }, 'Methods')
```

- Time: 0.0012 seconds
- Predicted Success: 0.54