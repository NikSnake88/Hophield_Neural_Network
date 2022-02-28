from tkinter import *
import PIL
from PIL import Image, ImageDraw
import functions as fn
import numpy as np


with open("Vesi.txt", "r") as file:
    vesa = np.genfromtxt('Vesi.txt', delimiter=' ')

def start():
    imageM = np.zeros((80,80))
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            (x, y, z) = image1.load()[i, j]
            imageM[i, j] = round((x*y*z / 2**24), 1)
    neuron = fn.pner(vesa, imageM)
    activ = fn.activation(neuron)
    if activ > 0.9:
        print('Это крест')
    else: print('Это не крест')

def saveX():
    global image_number
    filename = f'x_{image_number}.png'
    image1.save(filename)
    image_number += 1

def saveY():
    global image_number
    filename = f'y_{image_number}.png'
    image1.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill='white', width=7)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='white', width=7)
    lastx, lasty = x, y


root = Tk()

lastx, lasty = None, None
image_number = 0

cv = Canvas(root, width=80, height=80, bg='black')
# --- PIL
image1 = PIL.Image.new('RGB', (80, 80), 'black')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_start = Button(text="Start", command=start)
btn_start.pack()

btn_saveX = Button(text="Save x", command=saveX)
btn_saveX.pack(side=LEFT)

btn_saveY = Button(text="Save not x", command=saveY)
btn_saveY.pack(side=LEFT)

btn_saveY = Button(text="Clear", command=lambda: cv.delete("all"))
btn_saveY.pack(side=LEFT)

root.mainloop()