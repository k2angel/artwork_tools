import argparse
import os

from PIL import Image, UnidentifiedImageError


def main(file):
    try:
        img = Image.open(file)
    except UnidentifiedImageError:
        print("ERROR!!")
        return
    print(f"FileName: , {os.path.basename(file)}\nImageSize: {img.size}", sep="")
    width, height = img.size
    if width > height:  # Wide
        space = int((width - height) / 2)
        hs = height + space
        print(height, space, hs, sep=", ")
        artwork = img.crop((space, 0, hs, height))
        print(space, 0, hs, height, sep=", ")
    else:  # Tall
        space = int((height - width) / 2)
        ws = width + space
        print(width, space, ws, sep=", ")
        artwork = img.crop((0, space, width, ws))
        print(0, space, width, ws, sep=", ")
    artwork.save(os.path.join("./img", os.path.basename(file)))


os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists("./img"):
    os.mkdir("./img")

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
args = parser.parse_args()

for file in args.files:
    if os.path.isfile(file):
        main(file)
