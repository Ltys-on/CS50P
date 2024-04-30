import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    allowed_fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        random_font = str(random.choice(allowed_fonts))
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 3:
        if str(sys.argv[1]) == "-f" or str(sys.argv[1]) == "--font":
            try:
                font = allowed_fonts.index(str(sys.argv[2]))
            except ValueError:
                sys.exit("Invalid usage")
            desired_font = str(allowed_fonts[font])
            figlet.setFont(font=desired_font)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    input_text = str(input("Input: "))
    print(f"Output:\n{figlet.renderText(input_text)}")


if __name__ == "__main__":
    main()
