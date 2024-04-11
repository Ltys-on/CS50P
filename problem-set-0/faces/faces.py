def main():
    inputText = input("Give me your emoji :) :( ")
    print(convert(inputText))

def convert(inputText):
    return inputText.replace(":)", "🙂").replace(":(", "🙁")

main()