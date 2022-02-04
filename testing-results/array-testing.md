# Array Test Results

```
print('Programs with Multidimensional Data')
    _run_inference(model, {
        'Arrays': success,
        'Data Representation': success,
        'Defining Arrays': success,
        'Referencing Arrays': success,
        'Multidimensional Arrays': success,
        'Array with Methods': failure,
        'Programs with Data Sequences': failure,
    }, 'Programs with Multidimensional Data')
```

- Time: 0.0018 seconds
- Predicted Success: 0.7

```
print('Data Representation')
    _run_inference(model, {
        'Arrays': success,
    }, 'Data Representation')
```

- Time: 0.0074 seconds
- Predicted Success: 0.9

```
print('Array with Methods')
    _run_inference(model, {
        'Arrays': success,
        'Data Representation': success,
        'Defining Arrays': failure,
        'Referencing Arrays': failure,
        'Multidimensional Arrays': success,
        'Programs with Data Sequences': success,
        'Programs with Multidimensional Data': success
    }, 'Array with Methods')
```

- Time: 0.0018 seconds
- Predicted Success: 0.87

```
print('Programs with Data Sequences')
    _run_inference(model, {
        'Arrays': success,
        'Data Representation': failure,
        'Defining Arrays': failure,
        'Referencing Arrays': failure,
        'Multidimensional Arrays': success,
        'Array with Methods': failure,
    }, 'Programs with Data Sequences')
```

- Time: 0.0029 seconds
- Predicted Success: 0.3