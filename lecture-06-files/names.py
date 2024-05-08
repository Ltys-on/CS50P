def main():
    name = input("Name: ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


if __name__ == "__main__":
    main()