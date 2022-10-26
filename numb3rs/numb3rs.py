import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))
    sys.exit(1)

def validate(ip):

    if re.search("^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
        return True
    return False




if __name__ == "__main__":
    main()