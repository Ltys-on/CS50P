import cowsay
import sys

def main():

    if len(sys.argv) == 2:
        cowsay.trex(f"hello, {sys.argv[1]}")

main()