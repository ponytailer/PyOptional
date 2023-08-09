# PyOptional

optional object for python

### How to install

`pip install -U optional_python`

### How to use

#### `Optional.of & Optional.of_nullable`

```python

from pyoptional import Optional

value = 1

final_value = Optional.of(value).map(lambda x: x + 1).or_else(333)
assert final_value == 1

final_value = Optional.of_nullable(None).map(lambda x: x + 1).or_else(333)
assert final_value == 333


```

#### `Optional.or_raise`

```python

from pyoptional import Optional

Optional.of_nullable(None).or_raise(ValueError("value is None"))

```

#### `Try.of`

```python

from pyoptional import Try


def func():
    return 1 / 0


def func2():
    return 2 / 1


def handle_exception(e: ZeroDivisionError):
    return "error"


result = Try.of(func).recover(handle_exception)
assert result.get() == "error"

result = Try.of(func2).recover(handle_exception)
assert result.get() == 2

result = Try.of(lambda: 1 / 000000000)

# no exception handler
assert result.get() is None

result = Try.of(lambda: 1 / 000000000, raise_exception=True)

result.get()  # will raise ZeroDivisionError

```