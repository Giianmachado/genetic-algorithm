#############################################################################################################
# Imports
#############################################################################################################
import GA
import numpy as np
import math


#############################################################################################################
# Constants
#############################################################################################################
min_value = -1
max_value = 2
population_size = 20
cromossome_size = 22
generations = 20


#############################################################################################################
# Fitness function - x^2
#############################################################################################################
def fitness(x):
    value = np.array(x).dot(2**np.arange(np.array(x).size)[::-1])
    x = min_value + ((max_value - min_value) * (value / ((2**cromossome_size) - 1)))
    return (x * math.sin( 10 * x * math.pi)) + 1


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
