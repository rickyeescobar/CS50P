def main():
    sdict = {}

    while True:
        try:
            item = input().strip().upper()
            if item in sdict:
                sdict[item] += 1
            else:
                sdict[item] = 1
        except EOFError:
            for i in sorted(sdict.keys()):
                print(sdict[i],i)
            break



main()