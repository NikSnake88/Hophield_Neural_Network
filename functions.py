import numpy as np
from PIL import Image 

def readImage(imageO):
    imageM = np.zeros((200,200))
    image = Image.open(imageO)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.load()[x, y] == (0, 0, 0):
                imageM[x, y] = 1
    return imageM

def vinit(n, m):
    ves = np.random.uniform(-0.3, 0.3, (n, m))
    return ves

def vw(file, v):
    with open(file, "w") as file:
        for row in v:
            file.write(' '.join(map(str, row)) + '\n') 

def pner(v, img):
    n = 0
    for i, row in enumerate(img):
        for j, value in enumerate(row):
            n += value * v[i, j]
    return n