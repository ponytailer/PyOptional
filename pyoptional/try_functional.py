import typing as t


class Try:
    def __init__(self, func: t.Callable, raise_exception: bool):
        self.func = func
        self.exception_handler: t.Optional[t.Callable[[Exception], t.Any]] = None
        self.raise_exception = raise_exception

    @classmethod
    def of(cls, func: t.Callable, raise_exception: bool = False):
        return cls(func, raise_exception)

    def recover(self, exception_handler: t.Callable[[Exception], t.Any]):
        self.exception_handler = exception_handler
        return self

    def get(self) -> t.Any:
        try:
            return self.func()
        except Exception as e:
            if self.raise_exception:
                raise e
            if self.exception_handler is not None:
                return self.exception_handler(e)
