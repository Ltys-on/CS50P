def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check to see if the first two characters are numbers
    # Check to see if str is longer than 6 characters and shorter than 2
    # Check to see if no special characters are used
    if s.isalnum() and len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha():
    # Check if numbers are in the middle of the plate
    # Check if number at the end of the plate, first number is not 0
        for l in s:
            if l.isdigit():
                i = s.index(l)
                if s[i:].isdigit() and s[i] != "0":
                    return True
                else:
                    return False
        return True

    
    
main()
        