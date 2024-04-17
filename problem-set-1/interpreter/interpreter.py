def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    match y:
        case "+":
            result = x + z
        case "-":
            result = x - z
        case "/":
            result = x / z
        case "*":
            result = x * z
        case _:
            result = "NaN"
    
    print(round(result, 1))

main()