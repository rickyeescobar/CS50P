def main():
    # define menu
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    tab = 0.00

    # ask customer what they want
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                tab += (float(menu[item]))
                print ("Total : $"+f"{tab:.2f}")
            # add a way to cancel out of the program using ctrl d
        except EOFError:
            print()
            break

    # turn request into title case

    # count price total

    # print total






main()

