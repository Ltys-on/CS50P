def main():
    coke_bottle = 50
    change = 0
    inserted = 0

    while inserted < coke_bottle:
        print(f"Amount Due: {coke_bottle - inserted}")
        change = int(input("Insert Coin: "))
        if change == 5 or change == 10 or change == 25:
            inserted += change
            if inserted >= coke_bottle:
                print(f"Change Owed: {inserted - coke_bottle}")
        else:
            print("Unrecognized coin. Try again.")

main()