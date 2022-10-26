import random
import sys
def main():

    r = random

    while True:
        try:
            level = int(input("Level: "))
            levels = [i for i in range(1,level+1)]
            if level <1:
                pass
            elif level >= 1:
                chosen = r.choice(levels)
                while True:
                    guess = int(input("Guess: "))
                    if guess > chosen:
                        print("Too large!")
                    elif guess < chosen:
                        print("Too small!")
                    elif guess == chosen:
                        print("Just right!")
                        sys.exit()
        except ValueError:
            print("type a posititive integer")
            pass


if __name__ == "__main__":
    main()
