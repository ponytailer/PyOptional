import pytest

from pyoptional import Empty, Optional


def test_of():
    ol = Optional.of("123")
    assert isinstance(ol, Optional)

    with pytest.raises(ValueError) as e:
        Optional.of(None)
        assert e.value == "The value is None, should use the of_nullable"


def test_of_nullable():
    ol = Optional.of_nullable("123")
    assert isinstance(ol, Optional)
    empty = Optional.of_nullable(None)
    assert isinstance(empty, Empty)


def test_map():
    ol = Optional.of_nullable(123)
    v = ol.map(lambda x: x + 1).get()
    assert v == 124

    with pytest.raises(ValueError) as e:
        ol.map(lambda x: None).get()
        assert e.value == "value is None, can't call the get"


def test_if_present():

    value = 1

    def func(v):
        nonlocal value
        value += v

    ol = Optional.of_nullable(123)
    ol.if_present(func)

    assert value == 124

    Optional.of_nullable(None).if_present(func)


def test_if_not_present():
    value = 1

    def func():
        nonlocal value
        value += 1

    ol = Optional.of_nullable(123)
    ol.if_not_present(func)
    assert value == 1

    ol = Optional.of_nullable(None)
    ol.if_not_present(func)
    assert value == 2


def test_is_present():
    ol = Optional.of_nullable(123)
    assert ol.is_present()

    ol = Optional.of_nullable(None)
    assert not ol.is_present()


def test_get():
    ol = Optional.of_nullable(123)
    assert ol.get() == 123

    with pytest.raises(ValueError) as e:
        Optional.of_nullable(None).get()
        assert "value is None, can't call the get" == e.value


def test_or_else():
    ol = Optional.of_nullable(None).or_else(lambda: 1)
    assert ol == 1

    ol = Optional.of_nullable(None).or_else(1)
    assert ol == 1

    ol = Optional.of_nullable(123).or_else(1)
    assert ol == 123
