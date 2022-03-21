import functions as fn
import numpy as np
import os
import math


class Neuron():

    def __init__(self, x, y, shp):
        self.shape = int(shp)
        vesa = np.zeros((x, y))

    def vinit(self):
        self.vesa = np.random.uniform(-0.3, 0.3, (80, 80))

    def vread(self, path):
        if os.path.exists(path):
            if os.stat(path).st_size == 0:
                self.vesa = fn.vinit(80, 80)
            else:
                with open(path, "r") as file:
                    self.vesa = np.genfromtxt(path, delimiter=' ')
        else:
            self.vinit()

    def sum(self, img):
        n = np.sum(self.vesa * img)
        return n

    def activation(self, x):
        f = 1/(1 + math.exp(-x))
        return f
    
    def vwrite(self, file):
        with open(file, "w") as file:
            for row in self.vesa:
                file.write(' '.join(map(str, row)) + '\n') 