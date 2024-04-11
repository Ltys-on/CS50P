def main():
    mass = int(input("Mass in KG = "))
    E = einstein(mass)
    print(E)

def einstein(m):
    c = 300000000
    return m * (c ** 2)

main()