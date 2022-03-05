import functions as fn
import Adam as a
import numpy as np
import os

corvX = 0.95
corvY = 0.1

imagesX = os.listdir(path="./image/") 
np.random.shuffle(imagesX)
print(imagesX)

neurons = [a.Neuron(80,80) for i in range(10)]

for i in range(10):
    neurons[i].vread(str(i) +'_V.txt')


for i in range(10):
    for j, imageName in enumerate(imagesX):
        im = fn.readImage('image/'+ imageName)
        neuron = neurons[i].sum(im)
        activ = neurons[i].activation(neuron)
        #print("Nikita: " + str(neuron))
        #print("Anton: " + str(activ))
        if imageName[0] == str(i):
            while activ < corvX:
                fn.corr(activ, corvX, im, neurons[i].vesa)
                neuron = neurons[i].sum(im)
                activ = neurons[i].activation(neuron)
                #print("Nikita: " + str(neuron))
                #print("Anton: " + str(activ))
        else:
            while activ > corvY:
                fn.corr(activ, corvY, im, neurons[i].vesa)
                neuron = neurons[i].sum(im)
                activ = neurons[i].activation(neuron)
                #print("Nikita: " + str(neuron))
                #print("Anton: " + str(activ))

for i in range(10):
    neurons[i].vwrite(str(i) +'_V.txt')
