import functions as fn
import numpy as np
import os

corvX = 1
corvY = 0

# TODO: чото с ифами
if os.path.exists("Vesi.txt"):
    if os.stat("Vesi.txt").st_size == 0:
        vesa = fn.vinit(80, 80)
    else:
        with open("Vesi.txt", "r") as file:
            vesa = np.genfromtxt('Vesi.txt', delimiter=' ')
else:
    vesa = fn.vinit(80, 80)

imagesX = os.listdir(path="./image/") 
np.random.shuffle(imagesX)
print(imagesX)

#im = np.zeros((20,80,80))

#for i, imageName in enumerate(imagesX):
    #im[i] = fn.readImage('image/'+ imageName)

for i, imageName in enumerate(imagesX):
    im = fn.readImage('image/'+ imageName)
    #fn.saveImg(im)
    neuron = fn.pner(vesa, im)
    activ = fn.activation(neuron)
    #print("Nikita: " + str(neuron))
    #print("Anton: " + str(activ))
    if imageName[0] == 'x':
        while activ < corvX:
            fn.corr(activ, corvX, im, vesa)
            neuron = fn.pner(vesa, im)
            activ = fn.activation(neuron)
            #print("Nikita: " + str(neuron))
            #print("Anton: " + str(activ))
    else:
        while activ > corvY:
            fn.corr(activ, corvY, im, vesa)
            neuron = fn.pner(vesa, im)
            activ = fn.activation(neuron)
            #print("Nikita: " + str(neuron))
            #print("Anton: " + str(activ))

fn.vesiwrite("Vesi.txt", vesa)
