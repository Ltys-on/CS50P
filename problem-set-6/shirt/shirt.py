import sys
import os
from PIL import Image
from PIL import ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif validity_checks():
        input_image = sys.argv[1].lower()
        output_image = sys.argv[2].lower()
        shirt = Image.open("shirt.png")
        size = shirt.size
        try:
            input_image = Image.open(input_image)
        except FileNotFoundError:
            sys.exit("Input does not exist")
        input_image = ImageOps.fit(image=input_image, size=size)
        input_image.paste(shirt, shirt)
        input_image.save(output_image)


def validity_checks():
    input_file = os.path.splitext(sys.argv[1])[1].lower()
    output_file = os.path.splitext(sys.argv[2])[1].lower()
    if input_file == ".jpg" or input_file == ".png" or input_file == ".jpeg":
        if output_file == ".jpg" or output_file == ".png" or output_file == ".jpeg":
            return matching_filetype(input_file, output_file)
        sys.exit("Invalid output")
    else:
        sys.exit("Invalid input")


def matching_filetype(input_file, output_file):
    if input_file == output_file:
        return True
    sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
