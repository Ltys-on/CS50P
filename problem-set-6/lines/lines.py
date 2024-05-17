import sys


def main():
    count = 0

    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) <= 1:
        sys.exit("Too few command line arguments")
    elif sys.argv[1].endswith(".py"):
        try:
            with open(str(sys.argv[1]), "r") as file:
                for line in file:
                    if str(line.lstrip()) != "" and not line.lstrip().startswith("#"):
                        count += 1
        except FileNotFoundError:
            sys.exit("File does not exist.")
    else:
        sys.exit("Not a Python file")
    print(count)


if __name__ == "__main__":
    main()
