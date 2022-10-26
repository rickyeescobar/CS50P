def main():
    word = input("Input: ")
    output = shorten(word)
    print(output)


def shorten(word):
    vowells = ["a","e","i","o","u","A","E","I","O","U"]
    new_word = ""
    for letter in word:
        if letter in vowells:
            new_word+=('')
        else:
            new_word+=(letter)
    return new_word

if __name__ == "__main__":
    main()