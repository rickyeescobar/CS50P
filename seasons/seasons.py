import inflect
p = inflect.engine()

import re
import sys

from datetime import date


def main():
    inpt = input("Date of Birth: ")
    dob = get_dob(inpt)
    today = get_date()
    delta = get_delta(today, dob)
    minutes = convert(delta)
    translation = translate(minutes)

    #print(dob)
    #print(today)
    #print(minutes)
    print(translation, "minutes")

def get_dob(inpt):
    # get date of birth
    if dob:= re.search(r"^([0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9])$",inpt):
        return date.fromisoformat(dob.group(1))
    else:
        sys.exit("Invalid date")

def get_date():
    #get current date
    today = date.today()
    return today

def get_delta(today, dob):
    #get delta of dates
    return today - dob

def convert(delta):
    # convert delta in days to minutes
    seconds = delta.total_seconds()
    minutes = int(seconds / 60)
    return (minutes)

def translate(minutes):
    # use inflect to get word string of minutes
    translation = p.number_to_words(minutes, andword="")
    return translation.capitalize()


if __name__ == "__main__":
    main()
