import re

'''
name = input("what's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")

#1:19:52

'''
'''
name = input("what's your name? ").strip()
matches = re.search(r"^(.+), (.+)$",name )
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")
'''
'''
name = input("what's your name? ").strip()
matches = re.search(r"^(.+), (.+)$",name )
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")
'''
'''
name = input("what's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$",name )
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
'''

name = input("what's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$",name ):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")