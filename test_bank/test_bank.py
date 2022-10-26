from bank import value

def main():
    test_numbers()
    test_worlds()
    test_punctuation()

def test_numbers():
    assert value("123") == 100
    assert value("Hello 123") == 0
    assert value("hi 123") == 20

def test_words():
    assert value("heLlo") == 0
    assert value("Hi") == 20
    assert value("waddup") == 100

def test_punctuation():
    assert value("--") == 100

if __name__ == "__main__":
    main()
