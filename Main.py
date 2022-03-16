import functions as fn
import Adam as a
import numpy as np
import os

class iImg():
    def __init__(self, path):
        self.shape = int(path[-5])
        self.matrx = fn.readImage(path)

corvX = 0.9
corvY = 0.1

imageDir = "./image/80x/"
imagePaths = os.listdir(path=imageDir)

neurons = [a.Neuron(80,80) for i in range(10)]
for i in range(10):
    neurons[i].vread(str(i) +'_V.txt')

imgs = [iImg(imageDir + imgName) for imgName in imagePaths]
print("Imgs download: success")

loops = 0
correcting = 1
while correcting != 0:

    np.random.shuffle(imgs)
    correcting = 0

    for img in imgs:
        for idx, neuron in enumerate(neurons):
            activ = neuron.activation(neuron.sum(img.matrx))
            if img.shape == idx and activ < corvX:
                fn.corr(activ, corvX, img.matrx, neuron.vesa)
                correcting += 1
            elif img.shape != idx and activ > corvY:
                fn.corr(activ, corvY, img.matrx, neuron.vesa)
                correcting += 1
    loops += 1
    print(str(loops) + " " + str(correcting))

# for i in range(10):
#     for j, imageName in enumerate(imagePaths):
#         im = fn.readImage(imageDir + imageName)
#         neuron = neurons[i].sum(im)
#         activ = neurons[i].activation(neuron)
#         #print("Nikita: " + str(neuron))
#         #print("Anton: " + str(activ))
#         if imageName[-5] == str(i):
#             while activ < corvX:
#                 fn.corr(activ, corvX, im, neurons[i].vesa)
#                 neuron = neurons[i].sum(im)
#                 activ = neurons[i].activation(neuron)
#                 #print("Nikita: " + str(neuron))
#                 #print("Anton: " + str(activ))
#         else:
#             while activ > corvY:
#                 fn.corr(activ, corvY, im, neurons[i].vesa)
#                 neuron = neurons[i].sum(im)
#                 activ = neurons[i].activation(neuron)
#                 #print("Nikita: " + str(neuron))
#                 #print("Anton: " + str(activ))

for i in range(10):
    neurons[i].vwrite(str(i) +'_V.txt')
