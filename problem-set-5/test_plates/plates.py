def main():
    plate = str(input("Input: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and s.isalnum() and len(s) <= 6 and len(s) >= 2:
        for l in s:
            if l.isdigit():
                i = s.index(l)
                if s[i:].isdigit() and s[i] != "0":
                    return True
                else:
                    return False
    else:
        return False


if __name__ == "__main__":
    main()
