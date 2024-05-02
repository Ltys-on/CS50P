from fuel import convert
from fuel import gauge
import pytest


def test_correct():
    assert convert("9/10") == 90


def test_notstring():
    with pytest.raises(ValueError):
        convert("9")


def test_wrong_string():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_zeroy():
    with pytest.raises(ZeroDivisionError):
        convert("9/0")


def test_biggerx():
    with pytest.raises(ValueError):
        convert("2/1")


def test_full():
    assert gauge(99) == "F"


def test_empty():
    assert gauge(1) == "E"


def test_normal():
    assert gauge(50) == "50%"
