from PIL import Image
import numpy as np


image = Image.open("angelBW.jpg")

pixels = np.asarray(image, dtype=np.float32)
a = pixels[:,:,0]
b = []
x, y = a.shape
print(a.shape)
print(x, y)
newImage = []
gx = 0
gy = 0
g = 0
i = 0
j= 0
t = 3
t2 = 4
matriz = []
for i in range(x-t):
    temp_array = []
    for j in range(y-t):
        temp = a[i:(i+t), j:(j+t)]
        # print(temp)
        for f in range(t):
            for g in range(t):
                b.append(temp[f][g])
        temp_array.append(sorted(b)[t2])
        b = []
        # if g > t:
        #     temp_array.append(255)
        # else:
        #     temp_array.append(0)
    matriz.append(temp_array)

matriz = np.asarray(matriz, dtype=np.uint8)
Image.fromarray(matriz.astype(np.uint8)).save("holaR1.jpg")
image.close()
