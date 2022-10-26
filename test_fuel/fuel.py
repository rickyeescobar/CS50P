def main():

    while True:
        try:
            fraction = input("Fraction: ")

            percentage = convert(fraction)
            display = gauge(percentage)
            print(display)
            break

        except (ZeroDivisionError, ValueError):
            print("Use a correct integer input")

def convert(fraction):
    for i in fraction:
        if i.isalnum() == False:
            break
    phrase = fraction.partition(i)
    if int(phrase[0]) > int(phrase[2]):
        raise ValueError("X is larger than Y")
    if int(phrase[2]) == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    if phrase[1] == "/":
        return (int(int(phrase[0]) / int(phrase[2])*100))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()