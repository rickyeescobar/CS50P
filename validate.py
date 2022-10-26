import re

#regular expression library - re
#regexes- regular expression

#re.search(pattern, string, flags=0)


email = input("What's your email? ").strip()

#use r to make a raw string so that we can use a \ to use a literal .
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org)$", email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

#1:01:46