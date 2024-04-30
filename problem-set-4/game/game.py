from random import randint


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                random_number = randint(1, level)
                break
        except ValueError:
            continue
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue


if __name__ == "__main__":
    main()
