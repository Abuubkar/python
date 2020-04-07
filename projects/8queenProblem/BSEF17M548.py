import numpy as np


def fitness(fitness_array):
    """
    :type fitness_array: array
    """
    fitness_score = 0
    for i in range(len(fitness_array)):
        # i is the column also
        for j in range(i + 1, len(fitness_array)):
            # checking diagonally
            if abs(fitness_array[i] - fitness_array[j]) == abs(i - j):
                # print(fitness_array[i], fitness_array[j])
                fitness_score += 1

            # checking horizontally
            if fitness_array[i] == fitness_array[j]:
                # print(fitness_array[i], fitness_array[j])
                fitness_score += 1
    return fitness_score


def filter_population():
    """
    removes two child that have bad score
    """
    population.pop(score.index(max(score)))
    score.pop(score.index(max(score)))
    population.pop(score.index(max(score)))
    score.pop(score.index(max(score)))


def mutation(array1, array2):
    fit1 = fitness(array1)
    fit2 = fitness(array2)
    if fit1 == 0 or fit2 == 0:
        return array1, array2

    array1[np.random.randint(8)] = np.random.randint(8)
    array2[np.random.randint(8)] = np.random.randint(8)
    return array1, array2


def crossover(parent1, parent2):
    return mutation(np.append(parent1[:4], parent2[4:8]),
                    np.append(parent2[:4], parent1[4:8]))


sample = np.zeros(8)
# generating initial population
population = [np.zeros(8) for _ in range(4)]
number_of_child_generated = len(population)
while True:
    score = []
    for sample_array in population:
        score.append(fitness(sample_array))

    """
    Uncomment these two lines to see all population 
    and their respective score
    """
    # print(population)
    # print(score)

    if 0 in score:
        result = population[score.index(min(score))]
        break

    # filtering population
    filter_population()
    # returns list of numpy array && updating population
    population += (crossover(population[0], population[1]))
    number_of_child_generated += 2
    print("Number of Child generated", number_of_child_generated, end="\n")

"""
printing result
"""
for column in range(len(result)):
    print()
    for row in range(len(result)):
        if result[column] == row:
            print("[Q]", end=" ")
        else:
            print("[ ]", end=" ")
print("Number of Child generated", number_of_child_generated, end="\n")
print("Result", result, end="")
