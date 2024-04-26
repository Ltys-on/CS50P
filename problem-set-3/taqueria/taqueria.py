def main():
    total = 0.0
    while True:
        try:
            item = str(input("Item: ").title())
            total += get_items(item)
            print(f"Total: ${total:.2f}")
        except TypeError:
            continue
        except EOFError:
            break


def get_items(i):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    for f in menu:
        if str(f) == i:
            return float(menu[f])


main()
