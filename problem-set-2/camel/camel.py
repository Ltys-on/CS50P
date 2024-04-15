def main():
    input_variable = input("camelCase: ").strip()
    if input_variable.islower():
        snake_case = input_variable
    elif input_variable.isupper():
        snake_case = input_variable.lower()
    else:
        snake_case = ""
        for letter in input_variable:
            if letter.isupper():
                letter = "_" + letter.lower()
            snake_case += letter
    print(snake_case)

main()
