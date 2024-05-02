def main():
    word = str(input("Input: "))
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for l in word:
        try:
            if vowel.index(l):
                word = word.replace(l, "")
        except ValueError:
            continue
    return word


if __name__ == "__main__":
    main()
