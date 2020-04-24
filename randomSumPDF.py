import random
import numpy as np
import matplotlib.pylab as plt

def RandomListGen(listSize, randomSumNum):
    L = []
    for i in range(listSize):
        randomNum = 0
        for j in range(randomSumNum):
            randomNum += random.random()
        L.append(randomNum)
    return L

def plotRandomList(list, randomSumNum):
    plt.clf()
    plt.plot(list, np.arange(0, randomSumNum, randomSumNum/len(list)))
    plt.show()

def PDFCalc(list, randomSumNum, gap):
    sortedList = sorted(list)
    PDF = {"0":0}
    guess = 0
    for j in sortedList:
        if (j > guess + gap):
            guess += gap
            PDF[str(guess)] = 0
        PDF[str(guess)] += 1
    return PDF

def PDFPlot(PDF):
    plt.clf()
    plt.ylim(0, max(PDF.values())*1.2)
    plt.plot(*zip(*PDF.items()))
    plt.show()

# plotRandomList(RandomListGen(10000000, 1), 1)
PDF = PDFCalc(RandomListGen(100000, 50), 50, 0.01)
PDFPlot(PDF)
