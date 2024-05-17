import sys
from tabulate import tabulate
import csv


def main():
    menu = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append(row)
        except FileNotFoundError:
            sys.exit("File does not exist")
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
