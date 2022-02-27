from email.mime import image
import numpy as np
from PIL import Image 
import math

image_number = 0
alpha = 0.1

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
            n += value * v[i, j]
    return n


def activation(x):
    f = 1/(1+math.exp(-x))
    return f

def corr(np, na, cv, img, ves):
    delta = na - cv
    deriv = na*(1 - na) # производная ф-и активации сигмоиды
    for i, row in enumerate(img):
        for j, value in enumerate(row):
            ves[i, j] -= alpha * 2 * delta * deriv * img[i, j]
    
    
def saveImg(m):
    global image_number
    filename = f'image_{image_number}.txt'
    with open(filename, "w") as file:
        for row in m:
            file.write(' '.join(map(str, row)) + '\n') 
    image_number += 1
