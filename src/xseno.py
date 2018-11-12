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
population_size = 6
cromossome_size = 1
gene_size = 22
generations = 100


#############################################################################################################
# Fitness function - x^2
#############################################################################################################
def fitness(x):
    total = 0
    for i in range(len(x)):
        value = np.array(x[i]).dot(2**np.arange(np.array(x[i]).size)[::-1])
        result = min_value + ((max_value - min_value) * (value / ((2**gene_size) - 1)))
        total = result * math.sin( 10 * result * math.pi) + 1    
    
    return total


#############################################################################################################
# Main call
#############################################################################################################
if __name__ == "__main__":

    # initial population
    chromosomes = GA.populate(population_size, cromossome_size, gene_size)

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
        chromosomes = GA.crossover(chromosomes, gene_size)

        # apply mutation
        chromosomes = GA.mutation(chromosomes)

        # print population
        for chromosome in chromosomes:
            print(fitness(chromosome), end=" ")
        print('')
