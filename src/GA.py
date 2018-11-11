
#############################################################################################################
# Imports
#############################################################################################################
import numpy as np
import random


#############################################################################################################
# Random population
#############################################################################################################
def populate(population_size, chromossome_size):

    # Defining the population size.
    # The population will have population_size chromosome where each chromosome has chromossome_size genes.
    pop_size = (population_size, chromossome_size)

    # Creating the initial population.
    new_population = np.random.randint(2, size=pop_size)

    # return
    return new_population


#############################################################################################################
# Select by Tournament
#############################################################################################################
def selectionByTournament(chromosomes, fitness):

    # get length
    length = len(chromosomes)

    # declare result
    result = []

    # get sum of values
    for _ in range(0, length):

        # compare
        compare = [0, 0, 0, 0, 0]

        # loop
        for position in random.sample(range(0, length), 3):
            if fitness(chromosomes[position]) > fitness(compare):
                compare = chromosomes[position]

        # append selected
        result.append(compare)

    # return
    return result


#############################################################################################################
# Crossover
#############################################################################################################
def crossover(chromosomes):
    # get len
    length = len(chromosomes)

    # declare result
    result = []

    # while len more than 1
    while length > 0:

        # get two random positions
        positions = random.sample(range(0, length), 2)
        # print(positions)

        # get probability
        prob = random.randint(1, 101)

        # if prob is < 90 realize crossover
        if prob < 90:

            # set cross values
            chromosomes[positions[0]] = crossValues(
                chromosomes[positions[0]], chromosomes[positions[1]])
            chromosomes[positions[1]] = crossValues(
                chromosomes[positions[1]], chromosomes[positions[0]])

        # pop and append selected
        result.append(chromosomes[positions[0]])
        result.append(chromosomes[positions[1]])

        # pop values
        chromosomes = [i for j, i in enumerate(
            chromosomes) if j not in positions]

        # get len
        length = len(chromosomes)

    # return
    return result


#############################################################################################################
# Crossover
#############################################################################################################
def crossValues(gene1, gene2):

    # get len
    length = len(gene1)

    # cut point
    cut_first = random.randint(1, length - 1)
    cut_last = cut_first - length

    # return
    return np.concatenate((gene1[:cut_first], gene2[cut_last:]), axis=None)


#############################################################################################################
# Mutation
#############################################################################################################
def mutation(chromosomes):

    for a in range(len(chromosomes)):
        for b in range(len(chromosomes[a])):

            # get probability
            prob = random.randint(1, 101)

            # if prob is == 1 realize mutation
            if prob < 5:
                if chromosomes[a][b] == 0:
                    chromosomes[a][b] = 1
                else:
                    chromosomes[a][b] = 0

    # return
    return chromosomes
