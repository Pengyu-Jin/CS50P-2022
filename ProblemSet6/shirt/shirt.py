import sys
import os.path
from PIL import Image, ImageOps

ls = sys.argv

if len(ls) <= 2:
    sys.exit("Too few command-line arguments")
elif len(ls) > 3:
    sys.exit("Too many command-line arguments")
else:
    ext = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
    if os.path.splitext(ls[1])[1] in ext and os.path.splitext(ls[2])[1] in ext:
        if os.path.splitext(ls[1])[1] == os.path.splitext(ls[2])[1]:
            try:
                with Image.open("shirt.png") as shirt:
                    with Image.open(ls[1]) as muppet:
                        muppet = ImageOps.fit(muppet, shirt.size)
                        muppet.paste(shirt, shirt)
                        muppet.save(ls[2])
            except FileNotFoundError:
                sys.exit("Input does not exist")
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")
