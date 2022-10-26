import re
import sys


def main():
    print(convert(input("Hours: ").upper()))

def convert(s):
    if converted := re.search(r"^([0-2]?[0-9]):?([0-5]?[0-9]?) (AM|PM)? to ([0-2]?[0-9]):?([0-5]?[0-9]?) (AM|PM)?", s,re.IGNORECASE):
        pieces = converted.groups()
        if int(pieces[0]) > 12 or int(pieces[3]) >12:
            raise ValueError
        time1= new_frmt(pieces[0],pieces[1],pieces[2])
        time2= new_frmt(pieces[3],pieces[4],pieces[5])
        return f"{time1} to {time2}"
    else:
        raise ValueError



def new_frmt(hours, minutes, am_pm):
    if am_pm == "PM":
        if int(hours) == 12:
            hour = 12
        else:
            hour = int(hours) + 12
    else:
        if int(hours) == 12:
            hour = 0
        else:
            hour = int(hours)
    if minutes == '':
        new_minutes = "00"
        new_time = f"{hour:02}:{new_minutes}"
    else:
        new_time = f"{hour:02}:{minutes}"
    return new_time



if __name__ == "__main__":
    main()
'''
def main():
    print(convert(input("Hours: ").upper()))
#and (00 <= int(converted.group(2)) <= 59 or converted.group(2) == '')

def convert(s):
    if converted := re.search(r"^([0-2]?[0-9]):?([0-5]?[0-9]?) ?(AM|PM)? to ([0-2]?[0-9]):?([0-5]?[0-9]?) ?(AM|PM)?", s,re.IGNORECASE):
        if (00 <= int(converted.group(1)) <= 24 or 0 <= int(converted.group(1)) <= 24):
            if "AM" == converted.group(3) or "PM" == converted.group(3) and 1 <= int(converted.group(1)) <= 12:
                if "AM" == converted.group(3) and int(converted.group(1)) == 12:
                    output = f"00:{converted.group(2)}"
                    return output
                elif "AM" == converted.group(3) and 10 <= int(converted.group(1)) <= 11:
                    output = f"{converted.group(1)}:{converted.group(2)}"
                    return output
                elif "AM" == converted.group(3) and int(converted.group(1)) < 10:
                    output = f"0{converted.group(1)}:{converted.group(2)}"
                    return output
                elif "PM" == converted.group(3):
                    output = f"{int(converted.group(1))+12}:{converted.group(2)}"
                    return output
                return False
            elif 00 <= int(converted.group(1)) <= 24:
                if int(converted.group(1)) == 0:
                    output = f"12:{converted.group(2)} AM"
                    return output
                elif int(converted.group(1)) <= 12:
                    output = f"{converted.group(1)}:{converted.group(2)} AM"
                    return output
                elif 24 >= int(converted.group(1)) > 12:
                    output = f"{int(converted.group(1))-12}:{converted.group(2)} PM"
                    return output
        else:
            raise ValueError


if __name__ == "__main__":
    main()

    '''