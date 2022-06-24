from operator import index
import numpy as np
from PIL import Image 

def readImage(path, size):
    matrx = np.ones((size,size))
    matrx = matrx*(-1)
    img = Image.open(path).load()
    for i in range(size):
        for j in range(size):
            if img[i,j] == (0):
                matrx[i,j] = 1
    return matrx

def saveImg(m,f,size,f1):
    img = Image.open(f1)
    for i in range(size):
        for j in range(size):
            if m[i,j] == 1:
                img.putpixel((i, j), (0))
    img.save(f)
                
def activation (x):
    if x > 0:
        return 1
    else: 
        return -1

def recovery(n,w,g,f):

    test = readImage((f),g)
    test = test.reshape(n)
    currImages = test

    for _ in range(150):
        test = np.array(currImages)
        
        for i in range(n):
            sumT = np.sum(w[i] * test, axis=0)
            currImages[i] = activation(sumT)

        if (currImages == test).all():
            break 
    return currImages      