import argparse
import os

from PIL import Image, UnidentifiedImageError


def main(file):
    try:
        img = Image.open(file)
    except UnidentifiedImageError:
        print("ERROR!!")
        return
    print(f"FileName: {os.path.basename(file)}\nImageSize: {img.size}\nFormat: {img.format}")
    width, height = img.size
    if width > height:  # Wide
        space = int((width - height) / 2)
        hs = height + space
        print(height, space, hs, sep=", ")
        print(space, 0, hs, height, sep=", ")
        crop_box = (space, 0, hs, height)
    else:  # Tall
        space = int((height - width) / 2)
        ws = width + space
        print(width, space, ws, sep=", ")
        print(0, space, width, ws, sep=", ")
        crop_box = (0, space, width, ws)
    path = os.path.join("./img", os.path.basename(file))
    if os.path.splitext(file)[1] == ".gif":
        artwork = gif(img, crop_box)
        artwork[0].save(path, save_all=True, append_images=artwork[1:], duration=1000 / img.info["duration"], loop=0)
    else:
        artwork = img.crop(crop_box)
        artwork.save(path)

def gif(img, crop_box):
    cropped_imgs = []
    for i in range(img.n_frames):
        img.seek(i)  # ここで image が参照しているフレームが変わっている
        cropped = img.crop(crop_box)
        cropped_imgs.append(cropped)
    return cropped_imgs

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists("./img"):
    os.mkdir("./img")

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*")
args = parser.parse_args()

for file in args.files:
    if os.path.isfile(file):
        main(file)
