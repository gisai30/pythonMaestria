import random
from random import randrange
import matplotlib.pyplot as plt

m = []
newM = []
mejor = []

data = 0
data2 = 0

array1 = []
array2 = []

def cambiarDatos(x):
    if data2 < data:
        for y in range(10):
            m[x][y] = newM[x][y]

def createNewArray():
    for x in range(10):
        for y in range(10):
            newM[x][y] = m[x][y] +  random.gauss(0,1)

#def newData():

    #createNewArray()

for x in range(10):
    m.append([])
    newM.append([])
    for y in range(10):
        m[x].append(randrange(-10,10))
        newM[x].append(m[x][y] + random.gauss(0,1))

#newData()
for z in range(1000):
    for x in range(10):
        for y in range(10):
            data = data + (m[x][y] * m[x][y])
            data2 = data2 + (newM[x][y] * newM[x][y])
        array1.append(data)
        array2.append(data2)
        cambiarDatos(x)
        data = 0
        data2 = 0
    createNewArray()

array1 = []
for a in range(10):
    for b in range(10):
        array1.append(m[a][b])


plt.plot(array1,'ro')

plt.show()
#print(m)
