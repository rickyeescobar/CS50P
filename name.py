#sys.argv - list that you can input from prompt

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

'''
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
'''

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


#slices - subset of a data structure

# packages - third party library we can downloaded
# can be found at pypi.org