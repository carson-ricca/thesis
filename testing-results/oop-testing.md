# OOP Test Results

```
print('OOP')
    _run_inference(model, {
        'Variable Scope': success,
        'OOP Overview': success,
        'Multiple Classes': success,
        'User Defined Classes': success,
        'Creating Objects': success,
        'Object Interactions': success,
        'Object Independence': success,
        'Special Class Method': success,
        'Simple Programs': success,
        'Static Modifier': success,
        'Programs': success
    }, 'OOP')
```

- Time: 0.0024 seconds
- Predicted Success: 0.99

```
print('Programs')
    _run_inference(model, {
        'OOP': success,
        'Variable Scope': failure,
        'OOP Overview': success,
        'Multiple Classes': success,
        'User Defined Classes': failure,
        'Creating Objects': success,
        'Object Interactions': success,
        'Object Independence': failure,
        'Special Class Method': success,
        'Simple Programs': success,
        'Static Modifier': success,
    }, 'Programs')
```

- Time: 0.0025 seconds
- Predicted Success: 0.95

```
print('Multiple Classes')
    _run_inference(model, {
        'OOP': success,
        'Variable Scope': success,
        'OOP Overview': success
    }, 'Multiple Classes')
```

- Time: 0.0086 seconds
- Predicted Success: 0.95

```
print('Static Modifier')
    _run_inference(model, {
        'OOP': failure,
        'Variable Scope': failure,
        'OOP Overview': failure,
        'Multiple Classes': success,
        'User Defined Classes': success,
        'Creating Objects': failure,
        'Object Interactions': failure,
        'Object Independence': failure,
        'Special Class Method': failure,
        'Simple Programs': success,
        'Programs': failure
    }, 'Static Modifier')
```

- Time: 0.0024 seconds
- Predicted Success: 0.05