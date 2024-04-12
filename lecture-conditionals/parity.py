def main():
    x = int(input("What is x? "))

    if isEven(x):
        print("Even")
    else:
        print("Odd")

def isEven(n):
    if n % 2 == 0:
        return n % 2 == 0
    
main()