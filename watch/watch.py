import re
import sys


def main():
    inpt =input("HTML: ")
    match = parse(inpt)
    output_text = output(match)
    print (output_text, end='')




def parse(s):
    if match := re.search(r"\"(https?://(?:www\.)?youtube\.com/embed/(.{11}))\"",s):
       return f"https://youtu.be/{match.group(2)}"
    return f"None"

def output(match):
    output_text = match
    return output_text



if __name__ == "__main__":
    main()