from twttr import shorten

def test_twttr():
    assert shorten("Elena") == "ln"

def test_numbers():
    assert shorten("000") == "000"

def test_punct():
    assert shorten(".,.") == ".,."
