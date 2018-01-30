from PIL import Image

i = Image.open("pokemon.jpg")
#trasfor la imagen e pixeles
pixels = i.load()
width, height = i.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (255-r, 255-g, 255-b)

i.save("./imagenesSalida/negativo.jpg")
i.close()
