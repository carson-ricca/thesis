# Methods Testing Results

```
print('Methods')
    _run_inference(model, {
        'Abstraction': success,
        'Variable Scope': success,
        'Using Methods': success,
        'Defining Methods': success,
        'Method Overloading': success,
        'Modular Programs': failure,
    }, 'Methods')
```

- Time: 0.0012 seconds
- Predicted Success: 0.99

```
print('Methods')
    _run_inference(model, {
        'Abstraction': failure,
        'Variable Scope': failure,
        'Using Methods': failure,
        'Defining Methods': failure,
        'Method Overloading': failure,
        'Modular Programs': failure,
    }, 'Methods')
```

- Time: 0.0013 seconds
- Predicted Success: 0.001

```
print('Modular Programs')
    _run_inference(model, {
        'Using Methods': success,
        'Defining Methods': failure,
        'Method Overloading': success,
    }, 'Modular Programs')
```

- Time: 0.0668 seconds
- Predicted Success: 0.61

```
print('Defining Methods')
    _run_inference(model, {
        'Methods': failure,
        'Abstraction': success,
        'Variable Scope': failure,
        'Using Methods': success,
        'Method Overloading': failure,
        'Modular Programs': failure,
    }, 'Defining Methods')
```

- Time: 0.0012 seconds
- Predicted Success: 0.34