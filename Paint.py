from tkinter import *
import PIL
from PIL import Image, ImageDraw
import functions as fn
import numpy as np
import Adam as a

neurons = [a.Neuron(80,80) for i in range(10)]

for i in range(10):
    neurons[i].vread(str(i) +'_V.txt')

def start():
    ansver = [0 for k in range(2)] 
    imageM = np.zeros((80,80))
    image = image1.resize((80, 80), PIL.Image.ANTIALIAS)
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            (x, y, z) = image.load()[i, j]
            imageM[i, j] = round((x*y*z / 2**24), 1)
    for i in range(10):
        neuron = neurons[i].sum(imageM)
        activ = neurons[i].activation(neuron)
        if activ > ansver[1]:
            ansver[0] = i
            ansver[1] = activ
    
    print('Это ' + str(ansver[0]))
    return image

def saveX():
    global image_number
    filename = f'image/x_{image_number}.bmp'
    image = image1.resize((80, 80), PIL.Image.ANTIALIAS)
    image.save(filename)
    image_number += 1

def saveY():
    global image_number
    filename = f'image/y_{image_number}.bmp'
    image = image1.resize((80, 80), PIL.Image.ANTIALIAS)
    image.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill='white', width=8)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='white', width=8)
    lastx, lasty = x, y


def clear(canva, img):
    w, h = 150, 150
    x, y = 0, 0
    shape = (x, y, w, h)
    img.rectangle(shape, fill = "black")
    canva.delete("all")

root = Tk()

lastx, lasty = None, None
image_number = 0

cv = Canvas(root, width=150, height=150, bg='black')
# --- PIL
image1 = PIL.Image.new('RGB', (150, 150), 'black')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_start = Button(text="Start", command=start)
btn_start.pack()

btn_saveX = Button(text="Save x", command=saveX)
btn_saveX.pack(side=LEFT)

btn_saveY = Button(text="Save not x", command=saveY)
btn_saveY.pack(side=LEFT)

btn_clear = Button(text="Clear", command=lambda:clear(cv,draw))
btn_clear.pack(side=LEFT)

root.resizable(width=False, height=False)
root.mainloop()
