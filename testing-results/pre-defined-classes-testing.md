# Pre-Defined Classes Testing

```
print('Pre-Defined Classes')
    _run_inference(model, {
        'OOP Overview': success,
        'Scanner': success,
        'Character': success,
        'Math': success,
        'Random': failure,
        'Math Programs': success,
        'Changing Behaviour Programs': success,
        'Simple Programs': success,
        'String': failure,
        'Programs': success
    }, 'Pre-Defined Classes')
```

- Time: 0.0019 seconds
- Predicted Success: 0.97

```
print('Programs')
    _run_inference(model, {
        'Pre-Defined Classes': failure,
        'OOP Overview': failure,
        'Scanner': failure,
        'Character': success,
        'Math': success,
        'Random': success,
        'Math Programs': failure,
        'Changing Behaviour Programs': success,
        'Simple Programs': success,
        'String': success,
    }, 'Programs')
```

- Time: 0.0019 seconds
- Predicted Success: 0.8

```
print('Scanner')
    _run_inference(model, {
        'Pre-Defined Classes': failure,
        'OOP Overview': success,
        'Character': success,
        'Math': success,
        'Random': failure,
    }, 'Scanner')
```

- Time: 0.0044 seconds
- Predicted Success: 0.7

```
print('Math Programs')
    _run_inference(model, {
        'Pre-Defined Classes': success,
        'OOP Overview': failure,
        'Scanner': success,
        'Character': success,
        'Math': failure,
        'Random': success,
        'Changing Behaviour Programs': success,
        'Simple Programs': success,
        'String': success,
        'Programs': failure
    }, 'Math Programs')
```

- Time: 0.0019 seconds
- Predicted Success: 0.7