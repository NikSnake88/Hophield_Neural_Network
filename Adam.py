import functions as fn
import numpy as np
import os
import math


class Neuron():

    def __init__(self, x, y):
        #shape = ' '
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
        n = 0
        for i, row in enumerate(img):
            for j, value in enumerate(row):
                if value != 1:
                    n += value * self.vesa[i, j]
        return n

    def activation(self, x):
        f = 1/(1 + math.exp(-x))
        return f
    
    def vwrite(self, file):
        with open(file, "w") as file:
            for row in self.vesa:
                file.write(' '.join(map(str, row)) + '\n') 