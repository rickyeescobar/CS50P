from plates import is_valid

def main():
    test_req1()
    test_req2()
    test_req3()
    test_req4()


#requirements:
#1 “All vanity plates must start with at least two letters.”
def test_req1():
    assert is_valid("ELENA") == True
    assert is_valid("EL1000") == True
    assert is_valid("10ELEN") == False
    assert is_valid("1111") == False

#2 “… vanity plates may contain a maximum of 6 characters
# (letters or numbers) and a minimum of 2 characters.”
def test_req2():
    assert is_valid("ELENAAA") == False
    assert is_valid("E") == False

#3 “Numbers cannot be used in the middle of a plate;
# they must come at the end. For example, AAA222 would be
# an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_req3():
    assert is_valid("EL10NA") == False
    assert is_valid("ELENA0") == False
    assert is_valid("ELENA1") == True
    assert is_valid("ELEN10") == True



#4 “No periods, spaces, or punctuation marks are allowed.”
def test_req4():
    assert is_valid("EL ENA") == False
    assert is_valid("EL.ENA") == False
    assert is_valid("E,?!") == False
    assert is_valid("ELEN11") == True


if __name__ == "__main__":
    main()