from PIL import Image
import numpy as np
#np.set_printoptions(threshold=np.nan)

i = Image.open("hola.jpg")
#i.rotate(45).show()
pixels = i.load()
newPixel = []
print(i.size)
width, height = i.size

for x in range(width):
    newPixel.append([])
    for y in range(height):
        if y != (height-1):
            for z in range(4):
                r, g, b = pixels[y,x]
                r2, g2, b2 = pixels[y+1, x]
                media = int(abs(r-r2))
                newPixel[x].append([media,media,media])
        else:
            r,g,b = pixels[y,x]
            newPixel[x].append([r,r,r])

a = np.asarray(newPixel, dtype=np.uint8)
Image.fromarray(a.astype(np.uint8)).save("hola2.jpg")
i.close()

i = Image.open("hola2.jpg")
#i.rotate(45).show()
pixels = i.load()
newPixel = []
print(i.size)
width, height = i.size

for x in range(height):
    newPixel.append([])
    for y in range(width):
        if y != (width-1):
            print(x, y, width, height)
            for z in range(4):
                r, g, b = pixels[y,x]
                # r2, g2, b2 = pixels[y,x+1]
                # media = int(abs(r-r2))
                media = 200
                newPixel[x].append([media,media,media])
        else:
            r,g,b = pixels[y,x]
            newPixel[x].append([r,r,r])

a = np.asarray(newPixel, dtype=np.uint8)
Image.fromarray(a.astype(np.uint8)).save("hola3.jpg")
i.close()
# print(pixels)

# for x in range(width + 50):
#     for y in range(height):
