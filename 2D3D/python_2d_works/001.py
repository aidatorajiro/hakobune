import PIL.Image
import PIL.ImageDraw
import random
import os

w = 5
h = 5
basepath = os.path.dirname(os.path.abspath(__file__)) + "/"
img = PIL.Image.new("RGB", (w, h))
draw = PIL.ImageDraw.Draw(img)

for i in range(0, w):
    for j in range(0, h):
        draw.point([i, j], fill=
            (random.randint(0,255),
             random.randint(0,255),
             random.randint(0,255)))

img_resized = img.resize((w * 300, h * 300), resample=PIL.Image.BICUBIC)

img_resized.save(basepath + "001.jpg", "JPEG")
