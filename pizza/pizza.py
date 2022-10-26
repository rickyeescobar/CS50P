import sys
import csv
from tabulate import tabulate

try:

    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv") == True:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
        print(tabulate(menu,headers="firstrow", tablefmt="grid"))
    else:
        sys.exit(1)

except FileNotFoundError:
    print("File was not found")
    sys.exit(1)

