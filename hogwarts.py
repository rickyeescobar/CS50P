students = ["Hermione", "Harry", "Ron"]

'''
print(students[0])
print(students[1])
print(students[2])
'''

'''
for student in students:
    print(student)
'''

#len - length
# using len to iterate through a list

'''
for i in range(len(students)):
    print(i + 1, students[i])
'''

# dict - dictionary
# keys and values - something associated with something else

#List example - won't scale well
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#----------------------------------------------------------------
#Dict example
students = {
"Hermione" : "Gryffindor",
"Harry" : "Gryffindor",
"Ron" : "Gryffindor",
"Draco" : "Slytherin",
}

'''
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''
# indexing the dictionary using the string in the dictionary

for student in students:
    print(student, students[student], sep = ", ")

#-----------------------------------------------------------------

#now to add more data

students = [
    {"name": "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name": "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name": "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell terrier"},
    {"name": "Draco", "house" : "Slytherin", "patronus" : None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")