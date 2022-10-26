"""
print("meow")
print("meow")
print("meow")
"""


#while loop
#start with 0 and go to, not through the value youre interested in
'''
i = 0
while i < 3:
    print("meow")
    i += 1
'''

#for loop
# poorly designed - manually created list
'''
for i in [0, 1, 2]:
    print("meow")
'''
'''
for i in range(3):
    print("meow")
'''

# use the underscore for neccesary variables that aren't needed later
# to be more pythonic
'''
for _ in range(3):
    print("meow")


# in a very short package
print("meow\n" * 3, end="")
'''

#list - lists
# set of multiple values

# while loop
'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''


#with main - using both while and for loops with functions

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()