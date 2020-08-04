import random
import copy
import matplotlib.pyplot as plt
import numpy as np

N = 8  # number of genes
P = 10  # population number
Maxgen = 100  # Generations
Pm = 0.001  # Mutation probability
Pc = 0.6  # Crossover Probability between 0.6 and 0.9


class Individual:
    def __init__(self, gene, fitness):
        self.gene = [0] * N
        self.fitness = fitness


population = []
tempPopulation1 = []
tempPopulation2 = []
stringTest1 = ""
stringTest2 = ""
bestTemp = []
worstTemp = []
globalBest = []
best = []
offspring = []
dataArray = []
totalPopFitness = 0
totalOffSpringFitness = 0
averageOffSpringFitness = 0
maxOffFitness = 0
minOffFitness = 0
arrayLength = 0
checkGeneFitness = 0
mutation = []
checkParent = 0
crossPoint = 0
length = 0
fitness = 0
offspringCheck = 0
roundNum = 1
offPopCheck = 1


for i in range(0, P):
    population.append(Individual(0, 0))
    bestTemp.append(Individual(0, 0))
    worstTemp.append(Individual(0, 0))


def create_pop():
    global totalPopFitness
    for i in range(0, P):
        population[i].fitness = 0
        for j in range(0, N):
            num = random.randint(0, 1)
            population[i].gene[j] = num
            #if population[i].gene[j] == 1:
             #   population[i].fitness += 1
              #  totalPopFitness += 1


def tournament():  # Initial Generation
    global checkParent
    global offspringCheck
    global roundNum
    global tempPopulation1

    tempPopulation1 = copy.deepcopy(population)

    for i in range(0, P):
        check = 0
        check2 = 0
        while check != 1:
            parent1 = random.randint(0, P - 1)
            parent2 = random.randint(0, P - 1)
            if parent1 != parent2:
                check = 1
        if population[parent1].fitness > population[parent2].fitness:
            parent3 = parent1
        else:
            parent3 = parent2
        while check2 != 1:
            parent1 = random.randint(0, P - 1)
            parent2 = random.randint(0, P - 1)
            if parent1 != parent2:
                check2 = 1
        if population[parent1].fitness > population[parent2].fitness:
            crossover(parent3, parent1)
        else:
            crossover(parent3, parent2)


def crossover(parent1cross, parent2cross):
    global Pc
    global crossPoint
    global offspringCheck
    global tempPopulation2

    crossPoint = random.randint(1, N-1)
    cross = random.uniform(0, 1)
    offspringCheck = len(tempPopulation1)

    if cross < Pc:
        for i in range(crossPoint, N):
            tempPopulation1[parent1cross].gene[i] = tempPopulation1[parent2cross].gene[i]
    mutation(parent1cross)


def mutation(tomutate):
    global Pm
    mutated = False
    global offPopCheck
    temp = 0
    mut = random.uniform(0, 1)
    for j in range(N):
        mut = random.uniform(0, 1)
        if mut <= Pm:
            if tempPopulation1[tomutate].gene[j] == 0:
                tempPopulation1[tomutate].gene[j] = 1
            elif tempPopulation1[tomutate].gene[j] == 1:
                tempPopulation1[tomutate].gene[j] = 0

    offspring.append(tempPopulation1[tomutate])


def parent_evaluate():  # f=x^2 for parent
    global totalPopFitness
    totalPopFitness = 0
    populationLength = len(population)

    for e in range(P):
        population[e].fitness = 0
        if population[e].gene[0] == 1:
            population[e].fitness += 128

        if population[e].gene[1] == 1:
            population[e].fitness += 64

        if population[e].gene[2] == 1:
            population[e].fitness += 32

        if population[e].gene[3] == 1:
            population[e].fitness += 16

        if population[e].gene[4] == 1:
            population[e].fitness += 8

        if population[e].gene[5] == 1:
            population[e].fitness += 4

        if population[e].gene[6] == 1:
            population[e].fitness += 2

        if population[e].gene[7] == 1:
            population[e].fitness += 1

        population[e].fitness = population[e].fitness ** 2
        totalPopFitness += population[e].fitness


def off_evaluate(): #Fitness by f=x^2
    global totalPopFitness
    global totalOffSpringFitness
    global averageOffSpringFitness
    global maxOffFitness
    global minOffFitness

    totalOffSpringFitness = 0
    maxOffFitness = 0
    minOffFitness = 0

    offspringLength = len(offspring)
    #print("Off Length: " + str(offspringLength))
    for e in range(0, offspringLength-1):
        offspring[e].fitness = 0
        if offspring[e].gene[0] == 1:
            offspring[e].fitness += 128

        if offspring[e].gene[1] == 1:
            offspring[e].fitness += 64

        if offspring[e].gene[2] == 1:
            offspring[e].fitness += 32

        if offspring[e].gene[3] == 1:
            offspring[e].fitness += 16

        if offspring[e].gene[4] == 1:
            offspring[e].fitness += 8

        if offspring[e].gene[5] == 1:
            offspring[e].fitness += 4

        if offspring[e].gene[6] == 1:
            offspring[e].fitness += 2

        if offspring[e].gene[7] == 1:
            offspring[e].fitness += 1

        if e == 0:
            minOffFitness = offspring[e].fitness
            maxOffFitness = offspring[e].fitness
        if offspring[e].fitness >= maxOffFitness:
            maxOffFitness = offspring[e].fitness
        if offspring[e].fitness <= minOffFitness:
            minOffFitness = offspring[e].fitness

        # print("X Value: " + str(offspring[e].fitness))
        offspring[e].fitness = offspring[e].fitness ** 2
        totalOffSpringFitness += offspring[e].fitness
        # print("X^2 Value: " + str(offspring[e].fitness))
    print("Min: ", minOffFitness, " Max: ", maxOffFitness)
    maxOffFitness = maxOffFitness ** 2
    minOffFitness = minOffFitness ** 2
    averageOffSpringFitness = totalOffSpringFitness / offspringLength


def start():
    global totalPopFitness
    global totalOffSpringFitness
    global maxOffFitness
    global averageOffSpringFitness
    global minOffFitness

    plt.ylabel("Fitness")
    plt.xlabel("Generation")
    plt.axis([0,Maxgen, 0, 80000])
    for i in range(Maxgen):
        offPopCheck = 0
        totalPopFitness = 0
        totalOffSpringFitness = 0
        averageOffSpringFitness = 0
        maxOffFitness = 0
        minOffFitness = 0
        parent_evaluate()
        tournament()
        off_evaluate()
        elitism()
        print("Generation: ", i + 1)
        print("Total Parent Fitness: ", totalPopFitness)
        print("Total offspring Fitness: ", totalOffSpringFitness)
        print("Average: ", averageOffSpringFitness)
        print("Max Fitness: ", maxOffFitness)
        print("Min Fitness: ", minOffFitness)
        y = averageOffSpringFitness
        x = maxOffFitness
        plt.plot(i, y, 'r^')
        plt.plot(i, x, 'bs')
        plt.pause(0.01)
        file2write = open("MaxF1.txt", 'a')
        file2write.write(str(maxOffFitness) + "\n ")
        file2write.close()
        file2write = open("AverageF1.txt", 'a')
        file2write.write(str(averageOffSpringFitness) + "\n ")
        file2write.close()
        print("")
        totalOffSpringFitness = 0
        totalPopFitness = 0
    plt.show()


def elitism():
    worstIndex = 0
    bestIndex = 0
    global population
    worstTemp[0] = offspring[0]
    for i in range(P):
       # print(population[i].gene)
        if population[i].fitness > bestTemp[0].fitness:
            bestIndex = i
            bestTemp[0] = population[i]

        if offspring[i].fitness < worstTemp[0].fitness:
            worstIndex = i
            worstTemp[0] = offspring[i]

    offspring[worstIndex] = bestTemp[0]
    population = copy.deepcopy(offspring)
    off_evaluate()
    tempPopulation1.clear()
    tempPopulation2.clear()



create_pop()
file2write = open("MaxF1.txt", 'a')
file2write.truncate(0)
file2write = open("AverageF1.txt", 'a')
file2write.truncate(0)
start()
