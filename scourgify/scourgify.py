import os.path
import sys
import csv


try:
    if len(sys.argv) == 3 and os.path.exists(sys.argv[1]) == True:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})

            for student in students:
                #print(f"{student['name']},{student['house']}")
                student['name'] = student['name'].split(",")
                student['first'] = student['name'][1].strip()
                student['last'] = student['name'][0].strip()

            #for student in students:
                #print(f"{student['first']},{student['last']},{student['house']}")

        with open(sys.argv[2],"w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames= ["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow({"first": student["first"], "last":student["last"], "house":student["house"]})

    elif os.path.exists(sys.argv[1]) == False:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    else:
        sys.exit(1)


except FileNotFoundError:
    print("File not found")
    sys.exit(1)