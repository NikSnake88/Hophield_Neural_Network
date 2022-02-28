from email.mime import image
import numpy as np
from PIL import Image 
import math

image_number = 0
alpha = 0.15

def readImage(imageO):
    imageM = np.zeros((80,80))
    image = Image.open(imageO)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            #if image.load()[x, y] == (0, 0, 0):
            #    imageM[x, y] = 1
            (x, y, z) = image.load()[i, j]
            imageM[i, j] = round((x*y*z / 2**24), 1)

    return imageM

def vinit(n, m):
    ves = np.random.uniform(-0.3, 0.3, (n, m))
    return ves

def vesiwrite(file, v):
    with open(file, "w") as file:
        for row in v:
            file.write(' '.join(map(str, row)) + '\n') 

def pner(v, img):
    n = 0
    for i, row in enumerate(img):
        for j, value in enumerate(row):
            #if value != 1:
            n += value * v[i, j]
    return n


def activation(x):
    if x > 0:
        return 1
    else: 
        return 0
   # f = 1/(1+math.exp(-x))
   # return f

def corr(na, cv, img, ves):
    delta = cv - na
    for i, row in enumerate(img):
        for j, value in enumerate(row):
            if value != 0:
                ves[i, j] += alpha * delta * img[i, j]
    
    
def saveImg(m):
    global image_number
    filename = f'image_{image_number}.txt'
    with open(filename, "w") as file:
        for row in m:
            file.write(' '.join(map(str, row)) + '\n') 
    image_number += 1
