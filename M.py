import functions

import numpy as np
import os

if os.path.exists("Vesi.txt"):
    if os.stat("Vesi.txt").st_size == 0:
        vesa = functions.vinit(200, 200)
    else:
        with open("Vesi.txt", "r") as file:
            vesa = np.genfromtxt('Vesi.txt', delimiter=' ')
else:
    vesa = functions.vinit(200, 200)

im = functions.readImage("x001.bmp")

neuron = functions.pner(vesa, im)
print(neuron)
#with open("image.txt", "w") as file:
    #for row in readImage("x001.bmp"):
        #file.write(' '.join(map(str, row)) + '\n') 


functions.vw("Vesi.txt", vesa)