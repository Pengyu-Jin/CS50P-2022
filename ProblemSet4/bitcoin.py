import sys
import requests

try:
    if len(sys.argv) == 2:
        n = float(sys.argv[1])
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        sys.exit("Invalid Input")
except ValueError:
    sys.exit("Comman-line argument is not a number")

b = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
rate_float = b.json()["bpi"]["USD"]["rate_float"]
print(f"${n*rate_float:,.4f}")
