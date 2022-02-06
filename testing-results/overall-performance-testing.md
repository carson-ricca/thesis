# Overall Performance Testing
```
print('Overall Performance')
    _run_inference(model, {
        'Average Success': high,
        'Skip Questions': low,
        'Time Taken': short
    }, 'Overall Performance')
```
- Time: 0.0003 seconds
- Predicted Success: 0.98
```
print('Overall Performance')
    _run_inference(model, {
        'Average Success': high,
        'Skip Questions': high,
        'Time Taken': long
    }, 'Overall Performance')
```
- Time: 0.003 seconds
- Predicted Success: 0.19
```
print('Overall Performance')
    _run_inference(model, {
        'Average Success': low,
        'Skip Questions': medium,
        'Time Taken': medium
    }, 'Overall Performance')
```
- Time: 0.0003 seconds
- Predicted Success: 0.03
```
print('Overall Performance')
    _run_inference(model, {
        'Average Success': high,
        'Skip Questions': high,
        'Time Taken': short
    }, 'Overall Performance')
```
- Time: 0.0003 seconds
- Predicted Success: 0.74