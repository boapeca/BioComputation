import random
import copy
import matplotlib.pyplot as plt
import numpy as np

N = 10  # number of genes
P = 10  # population number
Maxgen = 250  # Generations
Pm = 0.001  # Mutation probability
Pc = 0.6  # Crossover Probability between 0.6 and 0.9


class Individual:
    def __init__(self, gene, fitness, fitnessx, fitnessy):
        self.gene = [0] * N
        self.fitness = fitness
        self.fitnessX = fitnessx
        self.fitnessY = fitnessy


population = []
tempPopulation1 = []
tempPopulation2 = []
stringTest1 = ""
stringTest2 = ""
bestTemp = []
worstTemp = []
worstParent = []
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
    population.append(Individual(0, 0, 0, 0))
    bestTemp.append(Individual(0, 0, 0, 0))
    worstTemp.append(Individual(0, 0, 0, 0))


def create_pop():
    global totalPopFitness
    for i in range(0, P):
        population[i].fitness = 0
        for j in range(0, N):
            num = random.randint(0, 1)
            population[i].gene[j] = num


def tournament():  # Initial Generation
    global checkParent
    global offspringCheck
    global roundNum
    global tempPopulation1
    parent3 = 0
    tempPopulation1 = copy.deepcopy(population)

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
    global offspringCheck
    global tempPopulation2

    crossPoint = random.randint(0, N)
    crossPoint2 = random.randint(N/2-1, N)
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

            # print("Mutated: " + str(offspring[tomutate].gene))
    for z in range(P):
        if tomutate == z:
            offspring.append(tempPopulation1[tomutate])


def parent_evaluate():  # #fitness by f(x,y) = 0.26.( x2 + y2 ) – 0.48.x.y for parent
    global totalPopFitness
    totalPopFitness = 0
    populationLength = len(population)

    for e in range(P):
        population[e].fitnessX = 0
        population[e].fitnessY = 0
        population[e].fitness = 0

        if population[e].gene[1] == 1:
            population[e].fitnessX += 8

        if population[e].gene[2] == 1:
            population[e].fitnessX += 4

        if population[e].gene[3] == 1:
            population[e].fitnessX += 2

        if population[e].gene[4] == 1:
            population[e].fitnessX += 1

        if population[e].gene[6] == 1:
            population[e].fitnessY += 8

        if population[e].gene[7] == 1:
            population[e].fitnessY += 4

        if population[e].gene[8] == 1:
            population[e].fitnessY += 2

        if population[e].gene[9] == 1:
            population[e].fitnessY += 1

        if population[e].gene[5] == 1:
            population[e].fitnessY *= -1

        if population[e].gene[0] == 1:
            population[e].fitnessX *= -1

        population[e].fitness = 0.26 * ((population[e].fitnessX ** 2) +
                                        (population[e].fitnessY ** 2)) - \
            0.48 * population[e].fitnessX * population[e].fitnessY
        totalPopFitness += population[e].fitness


def off_evaluate(): #fitness by f(x,y) = 0.26.( x2 + y2 ) – 0.48.x.y
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
    for e in range(0, P):
        offspring[e].fitnessX = 0
        offspring[e].fitnessY = 0
        offspring[e].fitness = 0

        if offspring[e].gene[1] == 1:
            offspring[e].fitnessX += 8

        if offspring[e].gene[2] == 1:
            offspring[e].fitnessX += 4

        if offspring[e].gene[3] == 1:
            offspring[e].fitnessX += 2

        if offspring[e].gene[4] == 1:
            offspring[e].fitnessX += 1

        if offspring[e].gene[6] == 1:
            offspring[e].fitnessY += 8

        if offspring[e].gene[7] == 1:
            offspring[e].fitnessY += 4

        if offspring[e].gene[8] == 1:
            offspring[e].fitnessY += 2

        if offspring[e].gene[9] == 1:
            offspring[e].fitnessY += 1

        if offspring[e].gene[5] == 1:
            offspring[e].fitnessY *= -1

        if offspring[e].gene[0] == 1:
            offspring[e].fitnessX *= -1

        offspring[e].fitness = 0.26 * ((offspring[e].fitnessX ** 2) +
                                       (offspring[e].fitnessY ** 2)) - \
            0.48 * offspring[e].fitnessX * offspring[e].fitnessY
        totalOffSpringFitness += offspring[e].fitness
        if e == 0:
            minOffFitness = offspring[e].fitness
            maxOffFitness = offspring[e].fitness

        if offspring[e].fitness >= maxOffFitness:
            maxOffFitness = offspring[e].fitness
        if offspring[e].fitness <= minOffFitness:
            minOffFitness = offspring[e].fitness
        # print("X^2 Value: " + str(offspring[e].fitness))

    averageOffSpringFitness = totalOffSpringFitness / offspringLength


def start():
    global totalPopFitness
    global totalOffSpringFitness
    global maxOffFitness
    global averageOffSpringFitness
    global minOffFitness

    plt.ylabel("Fitness")
    plt.xlabel("Generation")
    plt.axis([0, Maxgen, -20, 200])

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
        plt.pause(0.001)
        file2write = open("MaxF2.txt", 'a')
        file2write.write(str(minOffFitness) + "\n ")
        file2write.close()
        file2write = open("AverageF2.txt", 'a')
        file2write.write(str(averageOffSpringFitness) + "\n ")
        file2write.close()
        print("")
        totalOffSpringFitness = 0
        totalPopFitness = 0
    plt.legend()
    plt.show()


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
parent_evaluate()
file2write = open("MaxF2.txt", 'a')
file2write.truncate(0)
file2write = open("AverageF2.txt", 'a')
file2write.truncate(0)
start()