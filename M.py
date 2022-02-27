# TODO: Ему не нравится название, нужно видетиле адекватное!
import functions as fn
import numpy as np
import os
import sys # TODO: Я забыль зочем мне это надо было

corvX = 0.9
corvY = 0.15

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

#im = np.zeros((20,80,80))

#for i, imageName in enumerate(imagesX):
    #im[i] = fn.readImage('image/'+ imageName)

# TODO: захуярить в функцию

for i, imageName in enumerate(imagesX):
    im = fn.readImage('image/'+ imageName)
    #fn.saveImg(im)
    neuron = fn.pner(vesa, im)
    activ = fn.activation(neuron)
    if imageName[0] == 'x':
        while activ < corvX:
            fn.corr(neuron, activ, corvX, im, vesa)
    else:
        while activ > corvY:
            fn.corr(neuron, activ, corvY, im, vesa)
    print("Nikita: " + str(neuron))
    print("Anton: " + str(activ))

fn.vesiwrite("Vesi.txt", vesa)


#print(sys.argv)
