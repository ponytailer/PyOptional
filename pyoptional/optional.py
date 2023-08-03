import typing as t

Value = t.TypeVar("Value", bound=t.Any)


class BaseOptional:
    def __init__(self, value: t.Any = None):
        self.value = value

    def or_else(self, value: t.Any):
        if self.value is None:
            if callable(value):
                value = value()
            return value
        return self.value

    def is_present(self):
        raise NotImplementedError

    def if_not_present(self, func: t.Callable[[], t.NoReturn]) -> t.NoReturn:
        if not self.is_present():
            func()


class Empty(BaseOptional):

    def is_present(self) -> bool:
        return False

    def or_raise(self, exc: Exception):
        raise exc

    def get(self):
        raise ValueError("value is None, can't call the get")

    def if_present(self, func: t.Callable):
        ...


class Optional(BaseOptional):

    @classmethod
    def of(cls, value: t.Any) -> "Optional":
        if value is None:
            raise ValueError("The value is None, should use the of_nullable")
        return cls.of_nullable(value)

    @classmethod
    def of_nullable(cls, value: t.Any) -> t.Union["Empty", "Optional"]:
        return Empty() if value is None else cls(value)

    @classmethod
    def empty(cls) -> "Empty":
        return Empty()

    def map(self, func: t.Callable[[Value], t.Any]) -> t.Union["Optional", "Empty"]:
        if not self.is_present():
            return Optional.empty()
        return Optional.of_nullable(func(self.value))

    def if_present(self, func: t.Callable[[Value], t.NoReturn]) -> t.NoReturn:
        if self.is_present():
            func(self.value)

    def is_present(self) -> bool:
        return self.value is not None

    def get(self) -> Value:
        if not self.is_present():
            raise ValueError("value is None, can't call the get")
        return self.value
