from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75

def test_valueerror():
    with pytest.raises(ValueError):
        convert("5/3")

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"