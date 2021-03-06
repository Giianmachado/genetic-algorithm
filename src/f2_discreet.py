#############################################################################################################
# Imports
#############################################################################################################
import GA
import numpy as np


#############################################################################################################
# Constants
#############################################################################################################
population_size = 10
cromossome_size = 2
gene_size = 5
generations = 1000


#############################################################################################################
# Fitness function - x^2
#############################################################################################################
def fitness(x):
    total = 0
    for i in range(len(x)):
        value = np.array(x[i]).dot(2**np.arange(np.array(x[i]).size)[::-1])
        total = total + (i * (value ** 4))
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
        if epoch % 50 == 0:
            print("Epoch: " + str(epoch))

        # print population
        if epoch % 50 == 0:
            for chromosome in chromosomes:
                print(fitness(chromosome), end=" ")
            print('')

        # selection by roullete
        chromosomes = GA.selectionByTournament(chromosomes, fitness, False)

        # apply crossover
        chromosomes = GA.crossover(chromosomes, gene_size)

        # apply mutation
        chromosomes = GA.mutation(chromosomes)

        # print population
        if epoch % 50 == 0:
            for chromosome in chromosomes:
                print(fitness(chromosome), end=" ")
            print('')
