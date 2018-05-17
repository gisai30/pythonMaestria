from PIL import Image
import numpy as np

image = Image.open("angelBW.jpg")

pixels = np.asarray(image, dtype=np.float32)
a = pixels[:,:,0]
x, y = a.shape
print(a.shape)
print(x, y)
newImage = []
gx = 0
gy = 0
g = 0
i = 0
j= 0
t = 50
matriz = []
for i in range(x-3):
    temp_array = []
    for j in range(y-3):
        temp = a[i:(i+3), j:(j+3)]
        gx = temp[1,1] - temp[0,0]
        gy = temp[1,0] - temp[0,1]
        g = (gx**2 + gy**2)**(0.5)
        if g > t:
            temp_array.append(255)
        else:
            temp_array.append(0)
    matriz.append(temp_array)

matriz = np.asarray(matriz, dtype=np.uint8)
Image.fromarray(matriz.astype(np.uint8)).save("holaR.jpg")
image.close()
