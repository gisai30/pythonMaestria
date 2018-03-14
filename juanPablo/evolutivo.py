import numpy as np
import pandas as pd

def genoma(domain, dimensions):
    return np.random.uniform(low=domain[0], high=domain[1], size=dimensions)

def fitness(individuo):
    suma = 0
    for i in individuo:
        suma += i**2
    return suma
    
def cross(individuo1, individuo2, mutationCM, maxP):
    individuo1 = individuo1.tolist()
    individuo2 = individuo2.tolist()
    offSpring = []
    #punto de particion
    p = np.random.randint(low=1, high=maxP)
    if np.random.randint(low=0, high=1):
        offSpring = individuo1[:p] + individuo2[p:]
    else:
        offSpring = individuo1[p:] + individuo2[:p]

    for i,b in enumerate(offSpring):
        if np.random.rand(0,1) < mutationCM:
            offSpring[i] = np.random.uniform(low=-10, high=10)
    return np.array(offSpring)

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
#population = [genoma(domain, dimensions) for i in range(numberIndividual)]
population = []
generation = 100

#initializePopulation
# population = np.array()

score = []
for i in range(numberIndividual):
    population.append(genoma(domain, dimensions))
    score.append(fitness(population[-1]))

#data frame
for x in range(generation):
    df = pd.DataFrame({'population': population, "score": score})
    df = df.sort_values("score")
    sortPopulation = df["population"].values
    sortScore = df["score"].values

    population = []
    score = []
    for i in range(numberIndividual):
        population.append(cross(sortPopulation[np.random.randint(0,10)], sortPopulation[np.random.randint(0,99)], mutationCM, 5))
        score.append(fitness(population[-1]))

print(sortScore[0], sortPopulation[0])
print(df)
# while(generation < 50):
#     for i in range(numberIndividual):
