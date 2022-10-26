import working
import pytest


def test_AM():
    assert working.convert("9:00 AM to 12:00 AM") == "09:00 to 00:00"

def test_PM():
    assert working.convert("9:00 PM to 12:00 PM") == "21:00 to 12:00"

def test_time():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert working.convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_wrong_hour():
    with pytest.raises(ValueError):
        working.convert("13:00 PM to 17:00 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 9:60 PM")

def test_wrong_format():
    with pytest.raises(ValueError):
        working.convert("9AM - 9PM")
    with pytest.raises(ValueError):
        working.convert("9 to 5")

def test_wrong_format2():
    with pytest.raises(ValueError):
        working.convert("9 - 9")


if __name__ == "__main__":
    main()
