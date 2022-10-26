from numb3rs import validate
import sys
def main():

    test_good()
    test_bad()
    test_format()
    test_first_byte()
    test_range()
    sys.exit(1)

def test_good():
    assert validate("127.0.0.1") == True


def test_bad():
    assert validate("256.255.255.255") == False

def test_format():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2")== False
    assert validate("1") == False

def test_first_byte():
    assert validate("1") == False
    assert validate("a.") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("510.1.1.1") == False
    assert validate("1.510.1.1") == False
    assert validate("1.1.510.1") == False
    assert validate("1.1.1.510") == False







if __name__ == "__main__":
    main()