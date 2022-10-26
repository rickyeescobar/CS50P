import sys

counter = 0


try:
    if sys.argv[1].endswith(".py") and len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            for line in file:
                if len(line.strip()) != 0 and line.strip().startswith("#") == False:
                    counter += 1

        print(counter)
    else:
        sys.exit(1)


except(FileNotFoundError):
    print("Use a valid python file")
    sys.exit