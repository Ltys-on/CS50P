def main():
    count = 0
    while count != 3:
        count += 1
        print("meow")
    
    for _ in range(3):
        print("woof")

    print("squeak\n" * 3, end="")

    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
        
    for _ in range(n):
        print("nay")


    number = getNumber()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def getNumber():
    while True:
        n = int(input("Number: "))
        while n > 0:
            return n

main()