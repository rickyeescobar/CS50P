def main():
    fname = input("File name: ").strip().lower()
    sorter(fname)

def sorter(fname):
    if fname.endswith(".gif"):
        print("image/gif")
    elif fname.endswith(".jpg"):
        print("image/jpeg")
    elif fname.endswith(".jpeg"):
        print("image/jpeg")
    elif fname.endswith(".png"):
        print("image/png")
    elif fname.endswith(".pdf"):
        print("application/pdf")
    elif fname.endswith(".txt"):
        print("text/plain")
    elif fname.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()