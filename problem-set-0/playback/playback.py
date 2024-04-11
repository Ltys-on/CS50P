def main():
    inputText = input("What do you want to say slowly? ")
    slowDown = inputText.replace(" ", "...")
    print(slowDown)

main()