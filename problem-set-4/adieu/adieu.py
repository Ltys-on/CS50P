import inflect

p = inflect.engine()


def main():
    name_list = []
    while True:
        try:
            name = str(input("Name: "))
            name_list.append(name)
        except EOFError:
            print(f"\nAdieu, adieu, to {p.join(name_list)}")
            break


if __name__ == "__main__":
    main()
