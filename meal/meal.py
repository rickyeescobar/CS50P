def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)

    if minutes.endswith("pm"):
        minutes = minutes.removesuffix("pm")
        minutes = int(minutes)
        hours = hours + 12
    elif minutes.endswith("am"):
        minutes = minutes.removesuffix("am")
        minutes = int(minutes)


    minutes = int(minutes)
    hours = hours * 60
    count = hours + minutes

    if 420 <= count <= 480 :
        print("breakfast time")
    elif 720 <= count <= 780:
        print("lunch time")
    elif 1080 <= count <= 1140:
        print("dinner time")



if __name__ == "__main__":
    main()