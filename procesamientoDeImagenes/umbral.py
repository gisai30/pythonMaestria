from PIL import Image

i = Image.open("./mascaras/bullet-angel.jpg")
#trasfor la imagen e pixeles
pixels = i.load()
width, height = i.size
varloDeEntrada = 100
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        if r <= varloDeEntrada:
            r = 0
        else:
            r = 255
        # if g <= varloDeEntrada:
        #     g = 0
        # else:
        #     g = 255
        # if b <= varloDeEntrada:
        #     b = 0
        # else:
        #     b = 255
        pixels[x, y] = (r, r, r)

i.save("./imagenesSalida/umbral.jpg")
i.close()
