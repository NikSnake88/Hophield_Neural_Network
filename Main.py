import functions as fn
import numpy as np
import time
import os

gridSize = 20
inputNodes = gridSize*gridSize

pathTest = "./Test/"
pathTrain = "./Train/"
pathDeTrain = "./deTrain/"

listTest = os.listdir(path=pathTest)
imgsTest = np.array([(fn.readImage((pathTest + imgName),gridSize)).reshape(inputNodes) for imgName in listTest])

listTrain = os.listdir(path=pathTrain)
imgsTrain = np.array([(fn.readImage((pathTrain + imgName),gridSize)).reshape(inputNodes) for imgName in listTrain])
np.random.shuffle(imgsTrain)

currImages = np.zeros(inputNodes)
weights = np.zeros((inputNodes,inputNodes))

def OBUCHENIE(weights):
    for train in imgsTrain:
        weights += np.outer(train, train)
    np.fill_diagonal(weights, 0)


def RAZOBUCHENIE(weights, detrain, e):
    weights -= np.outer(detrain, detrain) * e
    np.fill_diagonal(weights, 0)

def TEST(ex):
    OBUCHENIE(weights)
    i = True
    start = time.time()
    for test in listTest:
        image_number = 0
        while i == True:
            res = fn.recovery(inputNodes,weights,gridSize,("./Test/" + test))
            for train in imgsTrain:
                if (res == train).all():
                    fn.saveImg(res.reshape((gridSize,gridSize)),("./Fin/"+ test),gridSize, "./Fin/fin.bmp")
                    i = False
                    break
            if i == True:
                fn.saveImg(res.reshape((gridSize,gridSize)),("./deTrain/de"+str(image_number)+".bmp"),gridSize, "./deTrain/de.bmp")
                RAZOBUCHENIE(weights,res, ex)
                image_number += 1
        i = True   
    end = time.time()
    print("epsilon: " + str(ex) + ", количество образов: " + str(len(imgsTest)) + ", время работы: " + format(end-start) + " сек")

#TEST(0.03)
def START(eps):
    i = 0
    OBUCHENIE(weights)
    start = time.time()
    while True:
        res = fn.recovery(inputNodes,weights,gridSize,("./test.bmp"))
        for train in imgsTrain:
            if (res == train).all() or i == 300:
                fn.saveImg(res.reshape((gridSize,gridSize)),("./Fin/fin1.bmp"),gridSize, "./Fin/fin.bmp")
                end = time.time()
                print("epsilon: " + str(eps) + ", время работы: " + format(end-start) + " сек")
                exit(0)
        RAZOBUCHENIE(weights, res,eps)
        i += 1

START(0.01)