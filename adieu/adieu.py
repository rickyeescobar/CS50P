import sys

def main():
    names = []
    try:

        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        if len(names) == 0:
            sys.exit()
        elif len(names) == 1:
            print("Adieu, adieu, to",names[0])
        elif len(names) == 2:
            print("Adieu, adieu, to",names[0],"and",names[1])
        elif len(names) >= 3:
            print("Adieu, adieu, to"," ",names[0],","," ",(", ".join(names[1:-1])),","," ","and"," ",names[-1], sep = '')
        sys.exit()

if __name__ == "__main__":
    main()