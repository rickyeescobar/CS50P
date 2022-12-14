# using list comprehension

def main():
    yell("this", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()





'''
# using a map

def main():
    yell("this", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
'''