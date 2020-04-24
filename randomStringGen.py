import math
import random
import string

letters = string.ascii_lowercase
Letters = string.ascii_uppercase
L = []
for i in range(len(letters)):
    L.append(letters[i])
for i in range(len(Letters)):
    L.append(Letters[i])

def fixedLenRandomString(strLen):
    return ''.join((L[random.randint(0,51)]) for i in range(strLen))

def maxLenRandomString(numStrings, maxLen):
    strings = []
    for i in range(numStrings):
        strings.append(fixedLenRandomString(random.randint(0, maxLen+1)))
    return strings

print(maxLenRandomString(20, 50))
