def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()

    # second requirement - must contain a maximum of 6 characters and
    # a minimum of two characters
    if len(s) < 2 or len(s) >6 or s.isalnum() == False:
        return False

    # first requirement - must start with two letters
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(2):
        if s[i].isalpha() == False:
            return False


    # third requirement - numbers cannot be used in middle of plate
    # numbers must be at end of plate

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # first number cannot be a 0
    i = 0

    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    return True

def r4(s):
    # fourth requirement - no periods, spaces, or punctuation marks are allowed
    for j in s:
        if j in ["."," ","!","?"]:
            return False




main()