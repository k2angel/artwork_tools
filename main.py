from PIL import Image
import argparse
import os
import glob

def main(img_path):
    img = Image.open(img_path)
    print("FileName : ",img.filename,"\nImageSize : ",img.size,sep = "")
    a = img.size[1]
    b = (img.size[0] - a) / 2
    c = a + b
    print (a,b,c)
    artwork = img.crop((b,0,c,a))
    print(b,0,c,a)
    artwork.save(os.path.basename(img_path))
    print(f"FileName : {os.path.basename(img_path)}\nImageSize : {artwork.size}")


parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--folder")
args = parser.parse_args()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if args.folder != None:
    imgs = glob.glob(args.folder + "\*.jpg")
    for img in imgs:
        main(img)
else:
    main(args.file)
