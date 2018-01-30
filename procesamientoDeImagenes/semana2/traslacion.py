from PIL import Image
import numpy as np
#np.set_printoptions(threshold=np.nan)

i = Image.open("../bailarina.jpg")
#i.rotate(45).show()
pixels = i.load()
newPixel = []
print(i.size)
width, height = i.size


for x in range(width):
    newPixel.append([])
    for y in range(height + 50):
        if y >= height:
            newPixel[x].append([255, 255, 255])
        else:
            r,g,b = pixels[y,x]
            newPixel[x].append([r, g, b])
            # newPixel[x,y] = (r,g,b)


a = np.asarray(newPixel, dtype=np.uint8)

Image.fromarray(a.astype(np.uint8)).save("hola0.jpg")

# print(pixels)

# for x in range(width + 50):
#     for y in range(height):
