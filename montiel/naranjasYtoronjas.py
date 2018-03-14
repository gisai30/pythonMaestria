import io
from random import randrange
import numpy as np
import math

naranja = [[5,5.5],[4.5,5],[5.2,4.9]]
toronja = [[6.5,6.8],[5.9,6],[5.7,5.5]]
arrayNaraja = []
arrayToronja = []
x1 = [0,0]
y1 = [0,0]
desX1 = [0,0]
desY1 = [0,0]

for x in range(2):
    for y in range(3):
        x1[x] = x1[x] + naranja[y][x]
        y1[x] = y1[x] + toronja[y][x]

    x1[x] = x1[x] / 3
    y1[x] = y1[x] / 3

np.random.uniform(low=4.9, high=6.6)

maxLength= 100
resultado = []
for x in range(maxLength):
    numRanfom1 = np.random.uniform(low=4.9, high=6.6)
    numRanfom2 = np.random.uniform(low=4.9, high=6.6)
    numRanfom3 = np.random.uniform(low=4.9, high=6.6)
    numRanfom4 = np.random.uniform(low=4.9, high=6.6)
    arrayNaraja.append([numRanfom1,numRanfom2])
    arrayToronja.append([numRanfom3,numRanfom4])


rn = 0
rt = 0
naranjasf = []
toronjaf = []
for y in range(maxLength):
    rn = math.sqrt(math.pow((arrayNaraja[y][0]- x1[0]),2) + math.pow((x1[1] - arrayNaraja[y][1]),2))
    rt = math.sqrt(math.pow((arrayToronja[y][0]-y1[0]),2) + math.pow((y1[1] - arrayToronja[y][1]),2))

    if rn < rt:
        resultado.append([rn,rt,'Naranja'])

    else:
        resultado.append([rn,rt,'Toronja'])

print(resultado)
