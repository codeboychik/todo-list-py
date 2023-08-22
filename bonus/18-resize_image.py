import argparse

from PIL import Image
import sys
import ast

parser = argparse.ArgumentParser(description="Example script with command-line arguments")
parser.add_argument("--images", type=tuple, help="List of images")
parser.add_argument("--size", type=tuple, help="width and height")


images = ast.literal_eval(str(sys.argv[sys.argv.index('--images') + 1]))
size = parsed_list = ast.literal_eval(str(sys.argv[sys.argv.index('--size') + 1]))

if __name__ == "__main__":
    [
        Image
        .open(image)
        .resize(size)
        .save(image)
        for image in images
    ]
