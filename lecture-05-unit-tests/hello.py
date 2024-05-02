def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(n="world"):
    return f"hello, {n}"


if __name__ == "__main__":
    main()