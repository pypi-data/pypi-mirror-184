# Readme of `yasiu.time`

Module with useful measure time decorators.

## Installation

```shell
pip install yasiu.time
```

## Time decorators

- **measure_perf_time_decorator**

  *using time.perf_counter*

- **measure_real_time_decorator**

  *using time.time*

### Import:

```py
from yasiu.time import measure_perf_time_decorator
```

### Print buffering will impact your performance!

- Use with cauction for multiple function calls

### Use examples

```py
@measure_perf_time_decorator()
def func():
    ...


@measure_perf_time_decorator(">4.1f")
def func():
    ...


@measure_perf_time_decorator(fmt=">4.1f")
def func():
    ...
```

## Console execution timer

not here yet.
