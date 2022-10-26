
def main():
    greeting = input("Greeting: ")
    pay = value(greeting)
    print(f"${pay}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        pay = (0)
    elif greeting.startswith("h"):
        pay = (20)
    else:
        pay = (100)
    return pay

if __name__ == "__main__":
    main()