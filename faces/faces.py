def main():
    words = input("type hello or goodbye followed by a :) or :( face")
    convert(words)

def convert(words):
    words = words.replace(":)","🙂")
    words = words.replace(":(","🙁")
    print(words)

main()