import random


def main():
    level = get_level()
    question_number = 0
    correct_answers = 0
    while question_number < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        guess_count = 0
        while guess_count != 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess != answer:
                    print("EEE")
                    guess_count += 1
                else:
                    correct_answers += 1
                    break
            except ValueError:
                print("EEE")
                guess_count += 1
        if guess_count == 3:
            print(f"{x} + {y} = {answer}")
        question_number += 1
    print(f"Score: {correct_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                break
            else:
                raise ValueError
        except ValueError:
            continue
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    


if __name__ == "__main__":
    main()
