def main():
    answer = input("What is the the answer to the Great Question? ").lower().strip()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

main()