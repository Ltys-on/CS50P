def main():
    while True:
        fraction = str(input("Fraction: "))
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = round(x / y * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
