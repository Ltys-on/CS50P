import sys
import requests


def main():
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
    bitcoin_price = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json"
    ).json()
    bitcoin_price_usd = float(bitcoin_price["bpi"]["USD"]["rate_float"])
    conversion_amount = bitcoin_amount * bitcoin_price_usd
    conversion_amount = round(conversion_amount, 4)
    print(f"${conversion_amount:,}")


if __name__ == "__main__":
    main()
