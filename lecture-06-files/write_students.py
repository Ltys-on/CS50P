import csv


def main():
    name = input("Name: ")
    home = input("Home: ")

    with open("write_students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


if __name__ == "__main__":
    main()