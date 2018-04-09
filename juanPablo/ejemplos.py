import numpy as np

def modificar(Pop, n):
    fitness = np.sum(Pop**2,axis=1)
    return fitness

matriz = np.random.randint(-10,10,[3,3])
print(matriz)

print(modificar(matriz, 3))


# para crear las graficas
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
