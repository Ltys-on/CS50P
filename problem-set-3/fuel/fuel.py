def main():
    while True:
        try:
            fraction = (input("Fraction: "))
            fuel_gauge = fuel(fraction)
            if fuel_gauge <= 1 and fuel_gauge >= 0:
                print("E")
                break
            elif fuel_gauge >= 99 and fuel_gauge <= 100:
                print("F")
                break
            elif fuel_gauge < 99 and fuel_gauge > 1:
                print(f"{fuel_gauge}%")
                break
            else:
                continue
        except TypeError:
            continue

def fuel(f):
    try:
        x , y = f.split("/")
        x = int(x)
        y = int(y)
        try:
            percentage = int(round((x / y * 100)))
            if percentage > 100:
                print("Improper fraction.")
            return percentage
        except ZeroDivisionError:
            print("Can't divide by zero.")
    except ValueError:
        print("Not an integer.")


main()