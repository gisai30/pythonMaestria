from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open("../imagenesSalida/umbral.jpg")
pixels = i.load()
array = []
width, height = i.size


for x in range(width):
    for y in range(height):
        r, g, b = pixels[x,y]
        array.append(r)

# print(array)
#plt.plot([1,2,3,4])
plt.hist(array, 100)

plt.ylabel("some numbers")
plt.grid(True)
plt.show()
