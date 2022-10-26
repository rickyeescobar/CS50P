import requests
import json
import sys

try:

    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    inpt = float(sys.argv[1])

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    b = response.json()

    #print(json.dumps(b, indent=2))
    #to look at json

    btc = (b["bpi"]["USD"]["rate_float"])

    amount = inpt * btc

    print(f"${amount:,.4f}")
    sys.exit(0)



except requests.RequestException:
    print("Please try again")
    sys.exit(1)

