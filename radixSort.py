import random
import time

def radixSort(data, maxVal):
    iter = 0
    lenMax  = len((str)(maxVal))
    BoB = [[[] for j in range(10)] for i in range(lenMax+1)]
    tic = time.perf_counter()

    for i in range(len(data)):
        digit = data[i]%10
        BoB[0][digit].append(data[i])
        iter = iter + 1
    if (lenMax == 1):
        return BoB[0]
    for k in range(lenMax):
        for i in range(10):
            for j in range(len(BoB[k][i])):
                digit = ((int)(BoB[k][i][j]/(10**(k+1))))%10
                BoB[k+1][digit].append(BoB[k][i][j])
                iter = iter + 1
    
    sortedRes = []
    for i in range(10):
        for j in range(len(BoB[lenMax][i])):
            sortedRes.append(BoB[lenMax][i][j])

    toc  = time.perf_counter()
    t_c = toc - tic
    return (iter, t_c, sortedRes)

def dataGen(lenData, maxVal):
    data = []
    lenMax  = len((str)(maxVal))
    for i in range(lenData):
        data.append((int)(random.random()*maxVal))
    return data


lenData = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000]
maxVal  = [99, 99, 999, 999, 999, 9999, 9999, 9999, 99999, 99999, 99999, 999999, 999999, 999999, 9999999, 9999999, 9999999]
Data    = []
Iter    = []
Time    = []
Sort    = []

for i in range(len(lenData)):
    Data.append(dataGen(lenData[i], maxVal[i]))
    Otpt = radixSort(Data[i], maxVal[i])
    Iter.append(Otpt[0])
    Time.append(Otpt[1])
    Sort.append(Otpt[2])
    print(Time[i])
    print(Iter[i])
    print()
