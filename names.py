#________________________________________

#writes to a file
'''
name = input("What's your name? ")

#open - allows you to read from or write to a file


with open("names.txt", "a") as file:
    file.write(f"{name}\n")

'''
#______________________________________

#Reads a file

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
