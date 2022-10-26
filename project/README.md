# StockSnake

## files
1. project.py
2. requirements.py
3. README.md
4. test_project.py


#### Video Demo:  <URL https://youtu.be/ZocR_asbyao >
#### Developer's name:
>##### Ricky Escobar
#### City:
>##### Houston, Texas
#### Country:
>##### United States

#### Description:
###### StockSnake is a python app that returns realtime stock data through the FinancialModelingPrep API (FinancialModelingPrep.com) and displays it in the terminal window. This app was fun to build because it allowed me to mix my curiosity of coding with my interests in the stock market and investing.


### Required libraries:
>- import requests
>- import PIL.Image
>- from io import BytesIO
>- import json
>- import certifi
>- from textwrap import fill
>- from pyfiglet import Figlet
>- from urllib.request import urlopen, HTTPError
>- import sys

### Description of functionality:
#### `main()`
###### the main() function of project.py handles the display of the title of the program "StockSnake", a welcome message,  sends a request to the FinancialModelingPrep.com api ( `data = get_stock_data(company)` ) for the company ticker symbol that the user is prompted to input, retrieves the data for use by the following functions, generates and prints ASCII art of the company name using `generate_title(data)`, generates and prints a description paragraph about the company via `generate_description(data)`, generates and prints key data points on the business that are displayed at the option of the user via `output_control(data)`, and finally generates an ASCII art version of the company logo using `ASCII_art(data)` that is converted from a real image to ASCII characters making it displayable in the terminal

#### `get_stock_data(company)`

###### This function is responsible for accessing the Financial Modeling Prep API and requesting data on the inputted company using the company's ticker symbol (ie: tsla ). This function is also responsible for the option to exit the program via typing 'exit' into the user input prompt. The data response is retrieved with the `urlopen()` method and then read using the `response.read().decode("utf-8")` function. Then it is interpretted in JSON format via `json.loads(data)`
###### Next, we handle exeptions and alert the user if the ticker is not valid. We give the user another chance to either retry their search or to type 'exit' to exit the program.

#### `program_name_title(program_name,program_name_font)`

###### This function takes two string arguments that are established in the main function and then uses the `pyfiglet` library to create the ASCII art for the title of the program ***StockSnake***.

#### `generate_title(data)`

###### This function takes the data passed from the FMP api, finds the actual name of the company, and then converts the name into ASCII art characters using `pyfiglet` that present as a title for the company data below.

#### `generate_description(data)`

###### This function takes the data passed from the api and then formats it into a wrapped text paragraph via the `textwrap` library.

#### `output_control(data)`

###### This function takes all of the company data and allows the user to manually select which elements of data they would like to display to the user interface on terminal...
    # mark out the undesired elements using "#" besides the item you want to omit
    output =   {
        'symbol' : data['symbol'],
        'price' : data['price'],
        'beta' : data['beta'],
        #'volAvg' : data['volAvg'],
        'mktCap' : data['mktCap'],

###### ...then the still-selected data is returned to be printed by the main function.

#### `ASCII_art(data, new_wt = 50)`

###### This function takes the data from the company, uses the `requests`, `PIL`, and `io' libraries to load a picture of the company logo, resize the image, turn the image into grayscale, convert the pixels of the image into ASCII characters, and then return the ASCII image to main to be displayed.



TODO

# Thanks for reading!