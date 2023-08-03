# PyOptional
optional object for python


### How to use


####  `Optional.of & Optional.of_nullable`
```python

from pyoptional import Optional

value = 1

final_value = Optional.of(value).map(lambda x: x + 1).or_else(333)
assert final_value == 1

final_value = Optional.of_nullable(None).map(lambda x: x + 1).or_else(333)
assert final_value == 333


```

####  `or_raise`

```python

Optional.of_nullable(None).or_raise(ValueError("value is None"))

```
