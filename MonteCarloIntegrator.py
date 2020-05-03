import math
import random

def integrator(function, xMin, xMax, yMin, yMax):
    numNeedles = 20000000
    inIntegral = 0
    for i in range(numNeedles):
        needle = (xMin+random.random()*(xMax-xMin), yMin+random.random()*(yMax-yMin))
        if (needle[1] < function(needle[0])):
            inIntegral += 1
    return ((xMax-xMin)*(yMax-yMin))*inIntegral/numNeedles

print(integrator(math.sin, 0, math.pi, 0, 1))
