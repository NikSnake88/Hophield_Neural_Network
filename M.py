import numpy as np
from PIL import Image 
import os

def readImage(imageO):
    imageM = np.zeros((200,200))
    image = Image.open(imageO)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.load()[x, y] == (0, 0, 0):
                imageM[x, y] = 1
    return imageM

def inves(file, n, m):
    ves = np.random.uniform(-0.3, 0.3, (n, m))
    with open(file, "w") as file:
        for row in ves:
            file.write(' '.join(map(str, row)) + '\n') 

if os.path.exists("Vesi.txt"):
    if os.stat("Vesi.txt").st_size == 0:
        inves("Vesi.txt", 200, 200)
    else:
        with open("Vesi.txt", "r") as file:
            matrix = np.genfromtxt('Vesi.txt', delimiter=' ')
        #print(matrix)
else:
    inves("Vesi.txt", 200, 200)

readImage("x001.bmp")

with open("image.txt", "w") as file:
    for row in readImage("x001.bmp"):
        file.write(' '.join(map(str, row)) + '\n') 


