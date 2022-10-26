def main():

    x, y, z = input("Expression: ").split(" ")
    answer = float(0)
    calculate(x,y,z,answer)


def calculate(x,y,z,answer):
    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(x + z)

        case "-":
            print(x - z)

        case "*":
            print(x * z)

        case "/":
            if z != 0:
                print(x / z)
            else:
                print("Undefined")

main()