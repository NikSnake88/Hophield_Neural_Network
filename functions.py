# from email.mime import image
from operator import index
import numpy as np
from PIL import Image 

image_number = 0
alpha = 0.1

SIZE = 80
def readImage(path):
    matrx = np.zeros((80,80))
    img = Image.open(path).load()
    for i in range(SIZE):
        for j in range(SIZE):
            (r,g,b) = img[i,j]
            matrx[i,j] = r*g*b / 16777216 # 2**24
    return matrx

def corr(na, cv, img, ves):
    delta = cv - na
    for idx, value in np.ndenumerate(img):
        if value != 0:
            ves[idx] += alpha * delta * value

def saveImg(m):
    global image_number
    filename = f'image_{image_number}.txt'
    with open(filename, "w") as file:
        for row in m:
            file.write(' '.join(map(str, row)) + '\n') 
    image_number += 1
