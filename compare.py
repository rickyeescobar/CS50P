x = int(input("What's x? "))
y = int(input("What's y? "))


'''
# too longhanded, asking 3 questions

if x < y:
    print("X is less than Y")

if x > y:
    print("X is greater than Y")

if x == y:
    print("X is equal to Y")
'''

# using elif, asking 1,2, or q questions
# almost good , but not best
'''
if x < y:
    print("X is less than Y")
elif x > y:
    print("X is greater than Y")
elif x == y:
    print("X is equal to Y")
'''

# we use else at the end because we have ruled out all of the previous
# options
'''
if x < y:
    print("X is less than Y")
elif x > y:
    print("X is greater than Y")
else:
    print("X is equal to Y")
'''

# or
'''
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''

'''
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''

# or

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")