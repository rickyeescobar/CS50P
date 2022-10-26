'''
print("#")
print("#")
print("#")
'''


'''
for _ in range(3):
    print("#")
'''


# vertical blocks
'''
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()
'''

# Horiontal question marks
'''
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
'''

# printing a square

'''
def main():
    print_square(3)

def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print("#", end="")
        print()

main()
'''

# more pythonicly
'''
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()
'''

# showing more levels
'''
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
'''
# break points -


def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

main()