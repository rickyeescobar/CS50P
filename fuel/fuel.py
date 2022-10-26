def main():

    while True:
        try:
            fraction = input("Fraction: ")
            for i in fraction:
                if i.isalnum() == False:
                    action = i
                    break
            phrase = fraction.partition(i)
            if phrase[1] == "/":
                if int(phrase[0]) == 0 or (int(phrase[0]) / int(phrase[2]) <= .01):
                    print("E")
                    break
                elif int(phrase[0]) < int(phrase[2]) and (int(phrase[0]) / int(phrase[2]) < .99):
                    print(f"{int(phrase[0]) / int(phrase[2]):.0%}")
                    break
                elif int(phrase[0]) == int(phrase[2]) or (1 >= int(phrase[0]) / int(phrase[2]) >= .99):
                    print("F")
                    break
                else:
                    pass
            else:
                pass

        except (ZeroDivisionError, ValueError):
            print("Use a correct integer input")


main()