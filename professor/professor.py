import random
r = random

def main():
    #get level
    level = get_level()
    #get score
    score = run_game(level)
    #print
    print("Score:", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                print("Try again")
        except ValueError:
            print("Try a valid integer (1,2, or 3)")



def generate_integer(level):

    if level == 1:
        x = r.randint(0,9)
        y = r.randint(0,9)
        return x,y
    elif level == 2:
        x = r.randint(10,99)
        y = r.randint(10,99)
        return x,y
    elif level == 3:
        x = r.randint(100,999)
        y = r.randint(100,999)
        return x,y

def simulate_round (x,y):
    count_tries = 1
    while count_tries<=3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def run_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()