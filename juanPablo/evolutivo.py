import numpy as np

#inputs
#dominio : D
domain = [-10, 10]
#probabilidad predefinida de cruzamineto: cR
probabilityCR = 0.5
#contante de mutación: cM
mutationCM = 0.5
#numero de individuos: n
numberIndividual = 100
#dimencion: d
dimensions = 10
#vector prueba: xNew
population = []
generation = 0

#initializePopulation
population = np.array()

while(generation < 50):
    for i in range(numberIndividual):
