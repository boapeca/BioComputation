import random
import copy
import matplotlib.pyplot as plt
import math
import numpy as np

N = 10  # number of genes
P = 10  # population number
Maxgen = 500  # Generations
Pm = 0.1  # Mutation probability
Pc = 0.8  # Crossover Probability between 0.6 and 0.9


class Individual:
    def __init__(self, gene, fitness):
        self.gene = [0] * N
        self.fitness = fitness


population = []
tempPopulation1 = []
tempPopulation2 = []
bestTemp = []
worstTemp = []
globalBest = []
offspring = []
totalPopFitness = 0
totalOffSpringFitness = 0
averageOffSpringFitness = 0
maxOffFitness = 0
minOffFitness = 0
crossPoint = 0
fitness = 0
roundNum = 1


for i in range(0, P):
    population.append(Individual(0, 0))
    bestTemp.append(Individual(0, 0))
    worstTemp.append(Individual(0, 0))


def create_pop():
    global totalPopFitness
    for i in range(0, P):
        population[i].fitness = 0
        for j in range(0, N):
            num = random.uniform(-5.12, 5.12)
            population[i].gene[j] = num


def tournament():  # Initial Generation
    global roundNum
    global tempPopulation1
    tempPopulation1 = copy.deepcopy(population)
    tempPopulation2 = copy.deepcopy(population)
    for i in range(0, P):
        check = 0
        check2 = 0
        while check != 1:
            parent1 = random.randint(0, P - 1)
            parent2 = random.randint(0, P - 1)
            if parent1 != parent2:
                check = 1
        if population[parent1].fitness <= population[parent2].fitness:
            parent3 = parent1
        else:
            parent3 = parent2
        while check2 != 1:
            parent1 = random.randint(0, P - 1)
            parent2 = random.randint(0, P - 1)
            if parent1 != parent3 or parent2 != parent3:
                check2 = 1
        if population[parent1].fitness <= population[parent2].fitness:
            crossover(parent3, parent1)
        else:
            crossover(parent3, parent2)


def crossover(parent1cross, parent2cross):
    global Pc
    global crossPoint
    global tempPopulation2

    # Selects the starting point for crossover to take place
    crossPoint = random.randint(0, N)
    cross = random.uniform(0, 1)
    if cross < Pc:
        for i in range(crossPoint, N):
            tempPopulation1[parent1cross].gene[i] = tempPopulation1[parent2cross].gene[i]


    mutation(parent1cross)


def mutation(tomutate):
    global Pm
    mutated = False
    global offPopCheck

    for j in range(N):
        mut = random.uniform(0, 1)
        if mut <= Pm:
            num = random.uniform(-0.01, 0.01)
            tempPopulation1[tomutate].gene[j] += num

            if tempPopulation1[tomutate].gene[j] <= -5.12:
                tempPopulation1[tomutate].gene[j] = -5.12

            elif tempPopulation1[tomutate].gene[j] >= 5.12:
                tempPopulation1[tomutate].gene[j] = 5.12

    #for e in range(N):
        #tempPopulation1[tomutate].gene[e] = round(tempPopulation1[tomutate].gene[e], 2)

    offspring.append(tempPopulation1[tomutate])


def parent_evaluate():  # Parent Fitness : 10N + sigma X^2 -10 cos(2.pi.X)
    global totalPopFitness
    totalPopFitness = 0

    for e in range(P):
        population[e].fitness = 0
        for i in range(N):
            population[e].fitness += (population[e].gene[i] ** 2) - (10 * math.cos(2*math.pi * population[e].gene[i]))
        population[e].fitness += (10 * N)
        #population[e].fitness = round(population[e].fitness, 2)

        totalPopFitness += population[e].fitness
        totalPopFitness = round(totalPopFitness, 2)


def off_evaluate():  # Offspring Fitness : 10N + sigma X^2 -10 cos(2.pi.X)
    global totalPopFitness
    global totalOffSpringFitness
    global averageOffSpringFitness
    global maxOffFitness
    global minOffFitness
    totalOffSpringFitness = 0
    maxOffFitness = 0
    minOffFitness = 0

    offspringLength = len(offspring)
    for e in range(0, P):
        offspring[e].fitness = 0
        for i in range(N):
            #offspring[e].gene[i] = round(offspring[e].gene[i], 2)
            offspring[e].fitness += (offspring[e].gene[i] ** 2) - (10 * math.cos(2 * math.pi * offspring[e].gene[i]))
        offspring[e].fitness += (10 * N)

        offspring[e].fitness = round(offspring[e].fitness, 2)
        if e == 0:
            minOffFitness = offspring[e].fitness
            maxOffFitness = offspring[e].fitness

        if offspring[e].fitness >= maxOffFitness:
            maxOffFitness = offspring[e].fitness
            maxOffFitness = round(maxOffFitness, 2)
        if offspring[e].fitness <= minOffFitness:
            minOffFitness = offspring[e].fitness
            minOffFitness = round(minOffFitness, 2)

        # print("X^2 Value: " + str(offspring[e].fitness))
        totalOffSpringFitness += offspring[e].fitness
        totalOffSpringFitness = round(totalOffSpringFitness, 2)

    averageOffSpringFitness = totalOffSpringFitness / offspringLength
    averageOffSpringFitness = round(averageOffSpringFitness, 2)


def start():
    global totalPopFitness
    global totalOffSpringFitness
    global maxOffFitness
    global averageOffSpringFitness
    global minOffFitness

    # creates a graph for easier behaviour interpretation of the pop
    plt.ylabel("Fitness")
    plt.xlabel("Generation")
    plt.axis([0, Maxgen, 0, 250])

    # Iterates through each generation
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
        print("Min: ", minOffFitness, " Max: ", maxOffFitness)
        print("Total Parent Fitness: ", totalPopFitness)
        print("Total offspring Fitness: ", totalOffSpringFitness)
        print("Average: ", averageOffSpringFitness)
        y = averageOffSpringFitness
        x = minOffFitness
        line1 = plt.plot(i, y, 'go', label='Average')  # Average Line
        line2 = plt.plot(i, x, 'r^', label='Best')  # Max line
        plt.pause(0.01)
        file2write = open("MaxF3.txt", 'a')
        file2write.write(str(minOffFitness) + "\n ")
        file2write.close()
        file2write = open("AverageF3.txt", 'a')
        file2write.write(str(averageOffSpringFitness) + "\n ")
        file2write.close()
        print("")
    plt.legend()
    plt.show()


# Elitism substitutes the Higher fitness Offspring with the lowest fitness parent for the new population
def elitism():
    worstIndex = 0
    bestIndex = 0
    global population
    worstTemp[0] = population[0]
    for i in range(P):
        if offspring[i].fitness > bestTemp[0].fitness:
            bestIndex = i
            bestTemp[0] = offspring[i]

        if population[i].fitness <= worstTemp[0].fitness:
            worstIndex = i
            worstTemp[0] = population[i]

    # Elitism, copies worst parent in offspring pool to become new parent pop
    offspring[bestIndex] = population[worstIndex]
    population = copy.deepcopy(offspring)
    off_evaluate()

    offspring.clear()
    tempPopulation1.clear()
    tempPopulation2.clear()


create_pop()
file2write = open("MaxF3.txt", 'a')
file2write.truncate(0)
file2write = open("AverageF3.txt", 'a')
file2write.truncate(0)
start()
