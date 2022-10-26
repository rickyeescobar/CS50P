def main():

    # define months
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        # get user inputted date
        date = input("Date: ").title().strip()
        # separate parts
        try:
            month, day, year = date.split("/")
            if (int(month) >= 1 and int(month) <= 12) and (int(day)>= 1 and int(day) <= 31):
                break

        except:
            try:
                if "," in date:
                    date1 = date.replace(",","")
                    month1, day, year = date1.split(" ")
                    for i in range(len(months)):
                        if months[i] == month1:
                            month = i + 1
                    if (int(month) >= 1 and int(month) <= 12) and (int(day)>= 1 and int(day) <= 31):
                        break
            except:
                print()
                pass

    print(f"{year}-{int(month):02}-{int(day):02}")




main()