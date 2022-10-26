def main():
    cname = input("camelCase: ")
    convert_name(cname)
    print()

def convert_name(cname):
    for letter in cname:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter.lower(), end="")
            
main()