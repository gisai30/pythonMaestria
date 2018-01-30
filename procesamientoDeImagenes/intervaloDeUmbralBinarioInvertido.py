from PIL import Image

i = Image.open("bailarina.jpg")
pixels = i.load()

width, height = i.size

p1 = 50
p2 = 200

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x,y]
        if (r <= p1 or r >= p2):
            r = 0
        elif (r > p1 and r < p2):
            r = 255

        if g <= p1 or g >= p2:
            g = 0
        elif g > p1 and g < p2:
            g = 255

        if b <= p1 or b >=p2:
            b = 0
        elif b > p1 and b < p2:
            b = 255

        pixels[x, y] = (r, g, b)
i.save("./imagenesSalida/umbralBinarioInvertido.jpg")
i.close()
