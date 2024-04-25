def main():
    items = []
    while True:
        try:
            item_name = str(input("")).upper()
            found = False
            for item in items:
                if item_name == item["item"]:
                    item["amount"] += 1
                    found = True
                    break
            if not found:
                    items.append({"item": item_name, "amount": 1})
        except EOFError:
            break

    items = sorted(items, key=lambda d: d["item"])
    for item in items:
        print(f"{item["amount"]} {item["item"]}")


main()
