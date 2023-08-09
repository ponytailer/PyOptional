import pytest

from pyoptional import Try


def test_try():
    result = Try.of(lambda: 1 / 0).recover(lambda e: 100)
    assert result.get() == 100

    result = Try.of(lambda: 1 / 1).recover(lambda e: 100)
    assert result.get() == 1

    result = Try.of(lambda: 1 / 0)
    assert result.get() is None


def test_try_raise_exception():
    result = Try.of(lambda: 1 / 0, raise_exception=True) \
        .recover(lambda e: 100)

    with pytest.raises(ZeroDivisionError):
        result.get()

    result = Try.of(lambda: 1 / 1, raise_exception=True)
    assert result.get() == 1

    result = Try.of(lambda: 1 / 0, raise_exception=True)
    with pytest.raises(ZeroDivisionError):
        result.get()
