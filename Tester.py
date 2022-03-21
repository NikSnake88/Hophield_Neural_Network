import PIL
from PIL import Image, ImageDraw
import functions as fn
import numpy as np
import Adam as a
import Main as m
import os

neurons = [a.Neuron(80,80, i) for i in range(10)]

for i in range(10):
    neurons[i].vread(str(i) +'_V.txt')

imageDir = "./image/80x/"
imagePaths = os.listdir(path=imageDir)

imgs = np.array([m.iImg(imageDir + imgName) for imgName in imagePaths])

right = 0

ansver = [0 for k in range(2)] 
for img in imgs:
    for neuron in neurons:
        activ = neuron.activation(neuron.sum(img.matrx))
        if activ > ansver[1]:
            ansver[0] = neuron.shape
            ansver[1] = activ
    if ansver[0] == img.shape:
        right += 1
    
print("Верно " + str((right/50)*100) + "%")