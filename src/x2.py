#############################################################################################################
# Imports
#############################################################################################################
import GA
import numpy as np


#############################################################################################################
# Constants
#############################################################################################################
population_size = 6
cromossome_size = 5
generations = 10


#############################################################################################################
# Fitness function - x^2
#############################################################################################################
def fitness(x):
    value = np.array(x).dot(2**np.arange(np.array(x).size)[::-1])
    return value * value


#############################################################################################################
# Main call
#############################################################################################################
if __name__ == "__main__":

    # initial population
    chromosomes = GA.populate(population_size, cromossome_size)

    # loop
    for epoch in range(0, generations):

        # log epoch
        print("Epoch: " + str(epoch))

        # print population
        for chromosome in chromosomes:
            print(fitness(chromosome), end=" ")
        print('')

        # selection by roullete
        chromosomes = GA.selectionByTournament(chromosomes, fitness)

        # apply crossover
        chromosomes = GA.crossover(chromosomes)

        # apply mutation
        chromosomes = GA.mutation(chromosomes)

        # print population
        for chromosome in chromosomes:
            print(fitness(chromosome), end=" ")
        print('')
