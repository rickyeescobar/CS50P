from pyfiglet import Figlet
import sys
import random

def main():
    f=Figlet()

    allfonts = [i for i in f.getFonts()]


    if len(sys.argv) == 3 and ((sys.argv[1] == "-f" or sys.argv[1] == "--font")):
        f = Figlet(font=sys.argv[2])
        print("Output:")
        print(f.renderText(input("Input: ")))

    elif len(sys.argv) == 1:
        f = Figlet(font=random.choice(allfonts))
        print("Output:")
        print(f.renderText(input("Input: ")))

    else:
        sys.exit(1)



main()