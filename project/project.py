import requests
import PIL.Image
from io import BytesIO
import json
import certifi
from textwrap import fill
from pyfiglet import Figlet
from urllib.request import urlopen, HTTPError
import sys


def main():
    print("__________________________________________________________________________________")
    print("----------------------------------------------------------------------------------")
    program_name = "           StockSnake"
    program_name_font = "big"

    print(program_name_title(program_name, program_name_font))
    print("Weclome to StockSnake, a python program designed to return realtime stock data to \nyou, including price, description, industry, and more...    08.31.22   ver.0.1.31")
    print("__________________________________________________________________________________")
    print("----------------------------------------------------------------------------------")

    ''' retrieve stock data via FinancialModelingPrep.com api, requests, io, json, and certifi '''

    company = input("Input company ticker symbol ('TSLA'): ")

    data = get_stock_data(company)
    # un-comment to view full dictionary of data
    #print(data)


    print()


    ''' generate the title text of the company being searched for with FIGlet '''

    print(generate_title(data))

    ''' generate, format, and indent the description paragraph with textwrap '''

    print(generate_description(data))

    print()

    ''' prepare output data for display (user can select which data they would like to output inside the output_control() function '''

    print(output_control(data))

    ''' display the company logo (picture sourced from FMP api) via ASCII characters using the PIL library and BytesIO from io'''

    print(ASCII_art(data))


def get_stock_data(company):
    '''
    Send request and get response for realtime stock data utlizing financialmodelingprep.com
    '''
    _ = False
    while _ != True:

        try:

            if company == "exit":
                sys.exit("\nExitted Successfully: Thank you for using StockSnake!")
            if company == " ":
                company = ""
            apikey = "f5bbf2948ae805e76d05a074a877d9b7"

            def get_jsonparsed_data(url):
                """
                Receive the content of `url`, parse it as JSON and return the object.
                """
                response = urlopen(url, cafile = certifi.where())
                data = response.read().decode("utf-8")
                return json.loads(data)


            url = ("https://financialmodelingprep.com/api/v3/profile/"+company+"?"+"apikey="+apikey)
            #data = json.dumps(get_jsonparsed_data(url), sort_keys=True, indent = 4)

            data = get_jsonparsed_data(url)
            data = data[0]

            _ = True
            return data

        except (IndexError, HTTPError, NameError):
            print("\n** Inputted stock ticker was not valid, please try again or type 'exit' to exit the program **\n")
            company = input("Input company ticker symbol ('TSLA'): ")


def program_name_title(program_name, program_name_font):
    f = Figlet(font = program_name_font)
    return (f.renderText(program_name))


def generate_title(data):
    f = Figlet(font = "colossal")
    company_name = data["companyName"]
    return (f.renderText(company_name))

def generate_description(data):
    description =  data["description"]

    return fill(description, width=160,initial_indent='    ', subsequent_indent='    ')



def output_control(data):

    #change the spacing of the output via this value
    spacing = 20


    # used to generate dictionary below
    #keys = data.keys()
    #for key,value in data.items():
        #print(f" '{key}' : data['{key}'],")
        #print(f"'{key}',",end='')


    # mark out the undesired elements using "#" besides the item you want to omit
    output =   {
        'symbol' : data['symbol'],
        'price' : data['price'],
        'beta' : data['beta'],
        #'volAvg' : data['volAvg'],
        'mktCap' : data['mktCap'],
        'lastDiv' : data['lastDiv'],
        #'range' : data['range'],
        'changes' : data['changes'],
        'companyName' : data['companyName'],
        #'currency' : data['currency'],
        #'cik' : data['cik'],
        #'isin' : data['isin'],
        #'cusip' : data['cusip'],
        'exchange' : data['exchange'],
        #'exchangeShortName' : data['exchangeShortName'],
        'industry' : data['industry'],
        'website' : data['website'],
        #'description' : data['description'],
        'ceo' : data['ceo'],
        'sector' : data['sector'],
        'country' : data['country'],
        'fullTimeEmployees' : data['fullTimeEmployees'],
        'phone' : data['phone'],
        #'address' : data['address'],
        'city' : data['city'],
        'state' : data['state'],
        #'zip' : data['zip'],
        'dcfDiff' : data['dcfDiff'],
        'dcf' : data['dcf'],
        #'image' : data['image'],
        'ipoDate' : data['ipoDate'],
        #'defaultImage' : data['defaultImage'],
        'isEtf' : data['isEtf'],
        'isActivelyTrading' : data['isActivelyTrading'],
        #'isAdr' : data['isAdr'],
        #'isFund' : data['isFund'],
                }

    output_string = ""
    for i in output:
        output_string += (f"{i}:" + (' ' * (spacing - len(i)))  + f"{output[i]}\n")

    return(output_string)


def ASCII_art(data, new_wt = 50):

    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    def resize_image(image, new_wt=50):
        wt, ht = image.size
        ratio = ht / wt
        new_ht = int(0.5 * new_wt * ratio)
        resized_image = image.resize((new_wt, new_ht))
        return resized_image

    def grayscale(image):
        grayscale_image = image.convert("L")
        return(grayscale_image)

    def pixels_to_ascii(image):
        pixels = image.getdata()
        characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
        return (characters)


    #get image url and image data from financialmodelingprep api
    path = data["image"]
    response = requests.get(path)


    try:
        image = PIL.Image.open(BytesIO(response.content))
    except:
        print(path, "is not a valid pathname to an image.")

    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_wt)] for i in range(0, pixel_count, new_wt))

    return(ascii_image)


if __name__ == "__main__":
    main()