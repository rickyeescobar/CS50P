import sys
import os.path
from PIL import Image, ImageOps

def main():
    check_command_line()

    try:
        infile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exits")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(infile,size)
    muppet.paste(shirt,shirt)

    muppet.save(sys.argv[2], format = None)





def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = os.path.splitext(sys.argv[1])
    file2 = os.path.splitext(sys.argv[2])

    if check_ext(file1[1]) == False:
        sys.exit("Invalid input")
    if check_ext(file2[1]) == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_ext(file):
    if file in [".jpg",".jpeg",".png"]:
        return True
    return False


if __name__ == "__main__":
    main()