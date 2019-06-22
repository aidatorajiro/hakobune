import PIL.Image
import PIL.ImageDraw
import numpy as np
from numpy.random import *
import os

w = 5
h = 5

mean_R = 55
mean_G = 127
mean_B = 204
sd_R = 70
sd_G = 40
sd_B = 10

def generate_color():
    arr = np.array((normal(mean_R, sd_R), normal(mean_G, sd_G), normal(mean_B, sd_B)))
    arr[arr > 255] = 255
    arr[arr < 0] = 0
    arr = tuple(arr.round().astype(int))
    return arr

basepath = os.path.dirname(os.path.abspath(__file__)) + "/"
img = PIL.Image.new("RGB", (w, h))
draw = PIL.ImageDraw.Draw(img)

for i in range(0, w):
    for j in range(0, h):
        draw.point([i, j], fill=generate_color())

img_resized = img.resize((w * 300, h * 300), resample=PIL.Image.BICUBIC)

img_resized.save(basepath + "002.jpg", "JPEG")
