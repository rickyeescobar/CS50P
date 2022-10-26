def main():
    m = int(input("m: "))
    calculate(m)

def calculate(m):
    c = 300000000
    E = m * c **2
    print("E:",E)
    
main()