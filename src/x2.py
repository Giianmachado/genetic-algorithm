
########################################################
# Imports
########################################################
import numpy as np


########################################################
# Constants
########################################################
min_value = 0
max_value = 31
generations = 5


########################################################
# Chromosome class
########################################################
class Chromosome:
    # constructor
    def __init__(self, value, fitness):
        self.value = value
        self.fitness = fitness

    # set fitness
    def setFitness(self, value):
        self.fitness = fitness(value)


########################################################
# Random population
########################################################
def populate(genes):

    # generate random genes
    random = np.random.randint(max_value + 1, size=genes)

    # declare result
    result = []

    # loop
    for i in random:
        result.append(Chromosome(i, 0))

    # calc fitness
    result = calcFitness(result)

    # return an array of Chromosome
    return result


########################################################
# Calc fitness
########################################################
def calcFitness(population):
    for gene in population:
        gene.setFitness(gene.value)
    return population


########################################################
# Fitness function - x^2
########################################################
def fitness(x):
    return x * x


########################################################
# Print population
########################################################
def printPopulation(population):
    for gene in population:
        print("Gene: " + str(gene.value) + " \t Fitness: " + str(gene.fitness))
    print("\n")


########################################################
# Select by Roulette
########################################################
def selectionRoulette(population):
    return population


########################################################
# Main call
########################################################
if __name__ == "__main__":

        # intial population
    population = populate(4)

    # log population
    printPopulation(population)

    # loop
    for epoch in range(0, generations):

        # selection by roullete
        population = selectionRoulette(population)

        # log population
        printPopulation(population)
