
#############################################################################################################
# Imports
#############################################################################################################
import numpy as np
import random


#############################################################################################################
# Constants
#############################################################################################################
min_value = 0
max_value = 31
generations = 200


#############################################################################################################
# Chromosome class
#############################################################################################################
class Chromosome:
    # constructor
    def __init__(self, value, fitness):
        self.value = value
        self.fitness = fitness

    # set fitness
    def setFitness(self, value):
        self.fitness = fitness(value)


#############################################################################################################
# Random population
#############################################################################################################
def populate(chromosomes):

    # generate random chromosomes
    random = np.random.randint(max_value + 1, size=chromosomes)

    # declare result
    result = []

    # loop
    for i in random:
        result.append(Chromosome(i, fitness(i)))

    # return an array of Chromosome
    return result


#############################################################################################################
# Calc fitness
#############################################################################################################
def calcFitness(chromosomes):
    # calc fitness
    for chromosome in chromosomes:
        chromosome.setFitness(chromosome.value)

    # return
    return chromosomes


#############################################################################################################
# Fitness function - x^2
#############################################################################################################
def fitness(x):
    return x * x


#############################################################################################################
# Print population
#############################################################################################################
def printPopulation(chromosomes):
    for chromosome in chromosomes:
        print("Chromosome: " + str(chromosome.value) + "  " + intToBinString(chromosome.value) +
              " \t Fitness: " + str(chromosome.fitness))
    print("\n")


#############################################################################################################
# Select by Tournament
#############################################################################################################
def selectionByTournament(chromosomes):

    # get length
    length = len(chromosomes)

    # declare result
    result = []

    # get sum of values
    for _ in range(0, length):

        # random positions
        positions = random.sample(range(0, length), 2)

        # compare
        compare = Chromosome(0, 0)

        # loop
        for position in positions:
            if chromosomes[position].fitness > compare.fitness:
                compare = chromosomes[position]

        # append selected
        result.append(compare)

    # return
    return result


#############################################################################################################
# Apply Crossover
#############################################################################################################
def applyCrossover(chromosomes):

    # get len
    length = len(chromosomes)

    # loop
    for index in range(0, length, 2):

        # get probability
        prob = random.randint(1, 101)

        # if prob is < 90 realize crossover
        if prob < 90:
            chromosomes[index] = crossover(
                chromosomes[index], chromosomes[index + 1])
            chromosomes[index +
                        1] = crossover(chromosomes[index + 1], chromosomes[index])

    # return
    return chromosomes


#############################################################################################################
# Crossover
#############################################################################################################
def crossover(gene1, gene2):

    # cut point
    cut_first = random.randint(1, 4)
    cut_last = cut_first - 5

    # calc cross
    cross = int(intToBinString(gene1.value)[
                :cut_first] + intToBinString(gene2.value)[cut_last:], 2)

    # return
    return Chromosome(cross, fitness(cross))


#############################################################################################################
# Convert int to bin string
#############################################################################################################
def intToBinString(value):
    return str('{:05b}'.format(value))


#############################################################################################################
# Mutation
#############################################################################################################
def mutation(chromosomes):

    # get index
    index = random.randint(0, len(chromosomes) - 1)

    # get bin value string
    value = intToBinString(chromosomes[index].value)

    # declare result
    result = ''

    # loop
    for letter in value:
        # get probability
        prob = random.randint(1, 101)

        # if prob is == 1 realize mutation
        if prob == 1:
            print("mutation")
            if letter == '0':
                result = result + '1'
            else:
                result = result + '0'
        else:
            result = result + letter

    # set result
    chromosomes[index] = Chromosome(int(result, 2), fitness(int(result, 2)))

    # return
    return chromosomes


#############################################################################################################
# Main call
#############################################################################################################
if __name__ == "__main__":

        # initial population
    chromosomes = populate(4)

    # log population
    print("Initial population")
    printPopulation(chromosomes)

    # loop
    for epoch in range(0, generations):

        # log epoch
        print("Epoch: " + str(epoch))

        # selection by roullete
        chromosomes = selectionByTournament(chromosomes)

        # apply crossover
        chromosomes = applyCrossover(chromosomes)

        # apply mutation
        chromosomes = mutation(chromosomes)

        # log population
        printPopulation(chromosomes)
